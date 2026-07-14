# find-connexes.ps1 - Liste les fiches connexes a une fiche donnee
#
# A invoquer AVANT/PENDANT/APRES la creation d'une fiche pour :
#   - voir quelles fiches existantes la mentionnent deja (a mettre a jour)
#   - reperer les wikilinks fantomes (cibles inexistantes) qu'elle contient
#   - decouvrir les fiches connexes par metadata (scoring discover-links style)
#
# Usage :
#
# 1. Par nom (cherche dans tout le vault) :
#    pwsh AI/scripts/find-connexes.ps1 -Name "SQLite"
#
# 2. Par path (utilise aussi le frontmatter de la fiche pour le scoring) :
#    pwsh AI/scripts/find-connexes.ps1 -Path "Services/Databases/SQLite.md"
#
# 3. Limiter les sorties :
#    -TopSuggest 10           (default 15, suggestions par scoring metadata)
#    -ShowMentions:$false     (n'affiche pas les mentions brutes en texte)

param(
    [string]$Path = "",
    [string]$Name = "",
    [int]$TopSuggest = 15,
    [switch]$ShowMentions = $true
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $root

$EXCLUDE = @(".obsidian", "node_modules", ".git", "AI/sessions", "AI/audits",
             "Templates/ServiceDocs", ".claude", "_orphans")

function Should-Exclude {
    param([string]$relPath)
    foreach ($e in $EXCLUDE) {
        if ($relPath.StartsWith($e + "/") -or $relPath -eq $e) { return $true }
    }
    return $false
}

function Parse-Frontmatter {
    param([string]$content)
    $fm = @{}
    if ($content -notmatch '(?s)^(---\r?\n)(.+?)(\r?\n---)') { return $fm }
    $yaml = $matches[2]
    foreach ($line in ($yaml -split "`n")) {
        $line = $line.Trim()
        if ($line -eq "" -or $line.StartsWith("#")) { continue }
        if ($line -match '^([a-zA-Z_]+):\s*(.*)$') {
            $key = $matches[1].Trim()
            $val = $matches[2].Trim()
            if ($val -match '^\[(.*)\]$') {
                $items = $matches[1] -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") } | Where-Object { $_ -ne "" }
                $fm[$key] = $items
            } elseif ($val -match '^"(.*)"$') {
                $fm[$key] = $matches[1]
            } else {
                $fm[$key] = $val
            }
        }
    }
    return $fm
}

# Resout un wikilink [[X]] vers un fichier reel ; renvoie $null si fantome
function Resolve-Wikilink {
    param([string]$target, [hashtable]$byName)
    # Nettoyer alias et fragment : [[X|alias]], [[X#section]], [[Folder/X]]
    $t = $target -replace '#.*$', '' -replace '\|.*$', ''
    $t = $t.Trim()
    # Si chemin avec slash, garder uniquement le nom du fichier
    if ($t.Contains('/')) {
        $t = $t.Substring($t.LastIndexOf('/') + 1)
    }
    if ($byName.ContainsKey($t)) { return $byName[$t] }
    return $null
}

# Determine la cible
$targetName = ""
$targetPath = ""
$targetContent = ""
$targetFm = @{}

if ($Path -ne "") {
    $absPath = Join-Path $root $Path
    if (-not (Test-Path $absPath)) {
        Write-Host "Path non trouve: $Path" -ForegroundColor Red
        exit 1
    }
    $targetPath = ($Path -replace '\\', '/')
    $targetName = [System.IO.Path]::GetFileNameWithoutExtension($absPath)
    $targetContent = [System.IO.File]::ReadAllText($absPath, [System.Text.Encoding]::UTF8)
    $targetFm = Parse-Frontmatter $targetContent
} elseif ($Name -ne "") {
    $targetName = $Name
} else {
    Write-Host ""
    Write-Host "Erreur : Specifier -Name ou -Path" -ForegroundColor Red
    Write-Host ""
    Write-Host "Exemples :"
    Write-Host "  -Name 'SQLite'"
    Write-Host "  -Path 'Services/Databases/SQLite.md'"
    exit 1
}

# Scan du vault
Write-Host "Scan du vault..." -ForegroundColor DarkGray
$files = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
    $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    -not (Should-Exclude $rel)
}

# Index des fiches par nom (sans extension)
$filesByName = @{}
foreach ($f in $files) {
    $n = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    if (-not $filesByName.ContainsKey($n)) { $filesByName[$n] = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/' }
}

# Aliases de la cible (depuis le frontmatter si Path fourni)
$targetAliases = @($targetName)
if ($targetFm.ContainsKey('alias')) {
    foreach ($a in $targetFm['alias']) {
        if ($a -ne "") { $targetAliases += $a }
    }
}
if ($targetFm.ContainsKey('nom')) {
    $nm = [string]$targetFm['nom']
    if ($nm -ne "" -and $targetAliases -notcontains $nm) { $targetAliases += $nm }
}
$targetAliases = $targetAliases | Select-Object -Unique

# Recherche dans tous les fichiers
$inFrontmatterAlternatives = @()   # [FORT]
$inWikilinks = @()                  # [MOYEN]
$inPlainText = @()                  # [FAIBLE]

foreach ($f in $files) {
    $rel = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    if ($rel -eq $targetPath) { continue }
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    # 1. Frontmatter alternatives:
    $fm = Parse-Frontmatter $content
    if ($fm.ContainsKey('alternatives')) {
        foreach ($alt in $fm['alternatives']) {
            # Strip [[...]] et garder le nom
            $altClean = $alt -replace '^\s*\[\[', '' -replace '\]\]\s*$', ''
            $altClean = $altClean -replace '\|.*$', ''   # alias
            if ($altClean -eq "") { continue }
            foreach ($ta in $targetAliases) {
                if ($altClean -ieq $ta) {
                    $inFrontmatterAlternatives += $rel
                    break
                }
            }
            if ($inFrontmatterAlternatives -contains $rel) { break }
        }
    }

    # 2. Wikilinks dans le corps
    $wikilinkMatches = [regex]::Matches($content, '\[\[([^\]]+)\]\]')
    $hasWikilink = $false
    foreach ($m in $wikilinkMatches) {
        $target = $m.Groups[1].Value -replace '\|.*$', '' -replace '#.*$', ''
        if ($target.Contains('/')) { $target = $target.Substring($target.LastIndexOf('/') + 1) }
        $target = $target.Trim()
        foreach ($ta in $targetAliases) {
            if ($target -ieq $ta) {
                $hasWikilink = $true
                break
            }
        }
        if ($hasWikilink) { break }
    }
    if ($hasWikilink -and ($inFrontmatterAlternatives -notcontains $rel)) {
        $inWikilinks += $rel
    }

    # 3. Mention en texte (word-boundary, sans wikilink, sans frontmatter alternatives)
    if (-not $hasWikilink -and ($inFrontmatterAlternatives -notcontains $rel) -and $ShowMentions) {
        # Strip le frontmatter pour eviter les faux positifs
        $body = $content -replace '(?s)^---\r?\n.+?\r?\n---\r?\n', ''
        # Strip aussi les wikilinks pour ne pas re-detecter
        $body = $body -replace '\[\[[^\]]+\]\]', ''
        foreach ($ta in $targetAliases) {
            if ($ta.Length -lt 3) { continue }   # skip aliases trop courts (faux positifs)
            $pattern = '\b' + [regex]::Escape($ta) + '\b'
            if ([regex]::IsMatch($body, $pattern, 'IgnoreCase')) {
                $inPlainText += $rel
                break
            }
        }
    }
}

# Wikilinks fantomes DANS la fiche cible (si -Path fourni)
$ghostsInTarget = @()
if ($targetPath -ne "" -and $targetContent -ne "") {
    $matches = [regex]::Matches($targetContent, '\[\[([^\]]+)\]\]')
    $seen = @{}
    foreach ($m in $matches) {
        $raw = $m.Groups[1].Value
        $resolved = Resolve-Wikilink -target $raw -byName $filesByName
        if ($null -eq $resolved) {
            $key = ($raw -replace '\|.*$', '' -replace '#.*$', '').Trim()
            if ($key -ne "" -and -not $seen.ContainsKey($key)) {
                $seen[$key] = $true
                $ghostsInTarget += $key
            }
        }
    }
}

# Sortie
Write-Host ""
Write-Host "Cible : $targetName" -ForegroundColor Cyan
if ($targetPath) { Write-Host "  path     : $targetPath" }
if ($targetAliases.Count -gt 1) { Write-Host "  aliases  : $($targetAliases -join ', ')" }
Write-Host ""

# ====== Section 1 : pages qui mentionnent la cible ======
Write-Host "=== Pages qui mentionnent '$targetName' ===" -ForegroundColor Yellow
Write-Host ""

if ($inFrontmatterAlternatives.Count -gt 0) {
    Write-Host "[FORT] dans 'alternatives:' du frontmatter ($($inFrontmatterAlternatives.Count)) :" -ForegroundColor Green
    foreach ($p in $inFrontmatterAlternatives) { Write-Host "  - $p" }
    Write-Host ""
}

if ($inWikilinks.Count -gt 0) {
    Write-Host "[MOYEN] wikilink [[$targetName]] dans le corps ($($inWikilinks.Count)) :" -ForegroundColor DarkYellow
    foreach ($p in $inWikilinks) { Write-Host "  - $p" }
    Write-Host ""
}

if ($ShowMentions -and $inPlainText.Count -gt 0) {
    Write-Host "[FAIBLE] mention '$targetName' en texte sans wikilink ($($inPlainText.Count)) :" -ForegroundColor DarkGray
    foreach ($p in $inPlainText | Select-Object -First 20) { Write-Host "  - $p" }
    if ($inPlainText.Count -gt 20) { Write-Host "  ... et $($inPlainText.Count - 20) autres" }
    Write-Host ""
}

if ($inFrontmatterAlternatives.Count -eq 0 -and $inWikilinks.Count -eq 0 -and $inPlainText.Count -eq 0) {
    Write-Host "  (aucune mention trouvee)" -ForegroundColor DarkGray
    Write-Host ""
}

# ====== Section 2 : wikilinks fantomes dans la cible ======
if ($targetPath -ne "") {
    Write-Host "=== Wikilinks fantomes DANS la cible ===" -ForegroundColor Yellow
    Write-Host ""
    if ($ghostsInTarget.Count -gt 0) {
        Write-Host "  $($ghostsInTarget.Count) cible(s) pointe(nt) vers des fiches inexistantes :"
        foreach ($g in $ghostsInTarget) { Write-Host "  - [[$g]]" -ForegroundColor Red }
        Write-Host ""
        Write-Host "  -> a creer, dewikilinker, ou redirected vers un alias existant"
    } else {
        Write-Host "  (aucun fantome - tous les wikilinks pointent vers des fiches existantes)" -ForegroundColor Green
    }
    Write-Host ""
}

# ====== Section 3 : suggestions par scoring metadata (si Path fourni) ======
if ($targetPath -ne "" -and $targetFm.Count -gt 0) {
    Write-Host "=== Suggestions par scoring metadata (top $TopSuggest) ===" -ForegroundColor Yellow
    Write-Host "  -> lancer 'discover-links.ps1 -Path $targetPath' pour le detail"
    Write-Host ""

    # Quick scoring inline : categorie / sous_categories / domaines / tags
    $tgtCat = if ($targetFm.ContainsKey('categorie')) { [string]$targetFm['categorie'] } else { "" }
    $tgtSC = if ($targetFm.ContainsKey('sous_categories')) { $targetFm['sous_categories'] } else { @() }
    $tgtDom = if ($targetFm.ContainsKey('domaines')) { $targetFm['domaines'] } else { @() }
    $tgtTags = if ($targetFm.ContainsKey('tags')) { $targetFm['tags'] } else { @() }

    $scored = @()
    foreach ($f in $files) {
        $rel = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
        if ($rel -eq $targetPath) { continue }
        # Skip si deja mentionnee
        if ($inFrontmatterAlternatives -contains $rel) { continue }
        if ($inWikilinks -contains $rel) { continue }

        $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        $fm = Parse-Frontmatter $content
        $score = 0
        $reasons = @()

        if ($tgtCat -ne "" -and $fm.ContainsKey('categorie') -and [string]$fm['categorie'] -eq $tgtCat) {
            $score += 10; $reasons += "categorie"
        }
        if ($fm.ContainsKey('sous_categories')) {
            $overlap = @($fm['sous_categories'] | Where-Object { $tgtSC -contains $_ })
            if ($overlap.Count -gt 0) { $score += $overlap.Count * 3; $reasons += "sc:$($overlap -join '+')" }
        }
        if ($fm.ContainsKey('domaines')) {
            $overlap = @($fm['domaines'] | Where-Object { $tgtDom -contains $_ })
            if ($overlap.Count -gt 0) { $score += $overlap.Count * 4; $reasons += "dom:$($overlap -join '+')" }
        }
        if ($fm.ContainsKey('tags')) {
            $overlap = @($fm['tags'] | Where-Object { $tgtTags -contains $_ })
            if ($overlap.Count -gt 0) { $score += $overlap.Count * 2; $reasons += "tag:$($overlap -join '+')" }
        }

        if ($score -gt 0) {
            $scored += [PSCustomObject]@{
                Score = $score
                Path = $rel
                Reasons = $reasons -join " | "
            }
        }
    }

    $top = $scored | Sort-Object -Property Score -Descending | Select-Object -First $TopSuggest
    if ($top.Count -gt 0) {
        foreach ($s in $top) {
            Write-Host ("  {0,3}  {1}" -f $s.Score, $s.Path) -ForegroundColor DarkCyan
            Write-Host "       $($s.Reasons)" -ForegroundColor DarkGray
        }
    } else {
        Write-Host "  (aucune suggestion - frontmatter de la cible pauvre)" -ForegroundColor DarkGray
    }
    Write-Host ""
}

# Resume
$totalMentions = $inFrontmatterAlternatives.Count + $inWikilinks.Count + $inPlainText.Count
Write-Host "Resume : $totalMentions page(s) mentionnent '$targetName'" -NoNewline -ForegroundColor Cyan
if ($targetPath -ne "") {
    Write-Host " | $($ghostsInTarget.Count) fantome(s) dans la cible" -ForegroundColor Cyan
} else {
    Write-Host ""
}
