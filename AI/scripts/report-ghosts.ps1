# report-ghosts.ps1 - Rapport vault-wide des wikilinks fantomes (cibles inexistantes)
#
# Pour chaque cible referencee mais inexistante, liste les fiches qui la
# referencent. Permet de decider en batch : creer la fiche, dewikilinker,
# ou fusionner avec un alias existant.
#
# Usage :
#   powershell -File AI/scripts/report-ghosts.ps1
#   -> ecrit AI/audits/ghosts-YYYY-MM-DD.md + affiche un resume terminal
#
#   # Seuil min de references pour signaler (default 1)
#   -MinRefs 2
#
#   # Filtrer par galaxie de la source
#   -Galaxie wiki
#
# Heuristiques :
# - Suggere "ALIAS ?" si une fiche existante a la cible dans son champ alias
# - Trie par nombre de references (plus reference = plus prioritaire)

param(
    [int]$MinRefs = 1,
    [string]$Galaxie = "",
    [switch]$NoFile
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $root

$EXCLUDE = @(".obsidian", "node_modules", ".git", "AI/sessions", "AI/audits",
             "Templates", ".claude", "_orphans")

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

Write-Host "Scan du vault..." -ForegroundColor DarkGray

# Tous les .md du vault, pour resolution des wikilinks (incluant Templates)
$NEVER = @(".obsidian", "node_modules", ".git", "_orphans", ".claude")
$allFiles = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
    $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    foreach ($e in $NEVER) {
        if ($rel.StartsWith($e + "/") -or $rel -eq $e) { return $false }
    }
    return $true
}

# Fichiers a SCANNER pour les wikilinks (exclut Templates et audits)
$files = $allFiles | Where-Object {
    $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    -not (Should-Exclude $rel)
}

# Index des fiches existantes (par nom et par alias) -> base sur allFiles
$byName = @{}
$byAlias = @{}        # alias -> nom de fiche reelle
foreach ($f in $allFiles) {
    $n = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    if (-not $byName.ContainsKey($n)) {
        $byName[$n] = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    }
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $fm = Parse-Frontmatter $content
    if ($fm.ContainsKey('alias')) {
        foreach ($a in $fm['alias']) {
            if ($a -ne "" -and -not $byAlias.ContainsKey($a)) { $byAlias[$a] = $n }
        }
    }
    if ($fm.ContainsKey('nom')) {
        $nm = [string]$fm['nom']
        if ($nm -ne "" -and $nm -ne $n -and -not $byAlias.ContainsKey($nm)) { $byAlias[$nm] = $n }
    }
}

$scannedMsg = "  " + $files.Count + " fiches scannees (sur " + $allFiles.Count + " indexees)"
Write-Host $scannedMsg -ForegroundColor DarkGray

# Collecte des fantomes : cible inexistante -> { sources: [paths], suggestionAlias: string|null }
$ghosts = @{}

foreach ($f in $files) {
    $rel = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'

    # Filtrage galaxie
    if ($Galaxie -ne "") {
        $content_fm = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        $fm = Parse-Frontmatter $content_fm
        $g = if ($fm.ContainsKey('galaxie')) { [string]$fm['galaxie'] } else { "" }
        if ($g -ne $Galaxie) { continue }
        $content = $content_fm
    } else {
        $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    }

    # Strip code blocks et templater <% ... %> pour eviter les faux positifs
    $cleaned = $content -replace '(?s)```.+?```', '' -replace '`[^`]+`', '' -replace '(?s)<%.+?%>', ''

    # Tous les wikilinks
    $matches = [regex]::Matches($cleaned, '\[\[([^\]]+)\]\]')
    foreach ($m in $matches) {
        $raw = $m.Groups[1].Value
        # Strip alias et fragment
        $key = $raw -replace '\|.*$', '' -replace '#.*$', ''
        if ($key.Contains('/')) { $key = $key.Substring($key.LastIndexOf('/') + 1) }
        $key = $key.Trim()
        if ($key -eq "") { continue }

        # Existe-t-il une fiche du meme nom ?
        if ($byName.ContainsKey($key)) { continue }

        # FANTOME
        if (-not $ghosts.ContainsKey($key)) {
            $aliasSuggestion = if ($byAlias.ContainsKey($key)) { $byAlias[$key] } else { $null }
            $ghosts[$key] = [PSCustomObject]@{
                Target = $key
                Sources = @()
                AliasOf = $aliasSuggestion
            }
        }
        if ($ghosts[$key].Sources -notcontains $rel) {
            $ghosts[$key].Sources += $rel
        }
    }
}

# Tri par nombre de references desc, puis alpha
$sorted = $ghosts.GetEnumerator() | ForEach-Object { $_.Value } |
    Where-Object { $_.Sources.Count -ge $MinRefs } |
    Sort-Object { -$_.Sources.Count }, Target

Write-Host ""
Write-Host "=== Rapport fantomes ===" -ForegroundColor Yellow
Write-Host "Total cibles fantomes : $($sorted.Count)" -ForegroundColor Cyan
Write-Host ""

# Grouper en buckets
$aliasable = @($sorted | Where-Object { $null -ne $_.AliasOf })
$prio = @($sorted | Where-Object { $null -eq $_.AliasOf -and $_.Sources.Count -ge 3 })
$mid = @($sorted | Where-Object { $null -eq $_.AliasOf -and $_.Sources.Count -eq 2 })
$low = @($sorted | Where-Object { $null -eq $_.AliasOf -and $_.Sources.Count -eq 1 })

# Section ALIAS-MATCHES : pure correction
if ($aliasable.Count -gt 0) {
    Write-Host "[ALIAS-FIX] $($aliasable.Count) fantome(s) ont un alias correspondant" -ForegroundColor Green
    Write-Host "  -> renommer [[X]] en [[<vrai-nom>]] dans les sources" -ForegroundColor DarkGray
    Write-Host ""
    foreach ($g in $aliasable) {
        Write-Host ("  [[{0}]] -> [[{1}]]  ({2} ref)" -f $g.Target, $g.AliasOf, $g.Sources.Count) -ForegroundColor Green
        foreach ($s in $g.Sources) { Write-Host "      $s" -ForegroundColor DarkGray }
    }
    Write-Host ""
}

# Section CREER : tres reference, fiche legitime probable
if ($prio.Count -gt 0) {
    Write-Host "[A CREER ?] $($prio.Count) fantome(s) avec 3+ references - fiches legitimes ?" -ForegroundColor Yellow
    Write-Host ""
    foreach ($g in $prio) {
        Write-Host ("  [[{0}]]  ({1} ref)" -f $g.Target, $g.Sources.Count) -ForegroundColor Yellow
        foreach ($s in $g.Sources) { Write-Host "      $s" -ForegroundColor DarkGray }
    }
    Write-Host ""
}

# Section A DECIDER
if ($mid.Count -gt 0) {
    Write-Host "[A DECIDER] $($mid.Count) fantome(s) avec 2 references" -ForegroundColor DarkYellow
    Write-Host ""
    foreach ($g in $mid) {
        Write-Host ("  [[{0}]]  ({1} ref)" -f $g.Target, $g.Sources.Count) -ForegroundColor DarkYellow
        foreach ($s in $g.Sources) { Write-Host "      $s" -ForegroundColor DarkGray }
    }
    Write-Host ""
}

# Section LOW
if ($low.Count -gt 0) {
    Write-Host "[FAIBLE] $($low.Count) fantome(s) avec 1 reference - probablement a dewikilinker" -ForegroundColor DarkGray
    Write-Host ""
    foreach ($g in $low) {
        Write-Host ("  [[{0}]] dans {1}" -f $g.Target, $g.Sources[0]) -ForegroundColor DarkGray
    }
    Write-Host ""
}

# Ecrire le rapport markdown
if (-not $NoFile) {
    $date = Get-Date -Format "yyyy-MM-dd"
    $outDir = Join-Path $root "AI/audits"
    if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force $outDir | Out-Null }
    $outPath = Join-Path $outDir "ghosts-$date.md"

    $sb = [System.Text.StringBuilder]::new()
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("type: audit")
    [void]$sb.AppendLine("kind: ghosts")
    [void]$sb.AppendLine("date: $date")
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("# Audit wikilinks fantomes - $date")
    [void]$sb.AppendLine("")
    $totalLine = "Total cibles fantomes : **" + $sorted.Count + "**"
    [void]$sb.AppendLine($totalLine)
    [void]$sb.AppendLine("")
    if ($Galaxie -ne "") {
        $gLine = "Filtre galaxie : ``" + $Galaxie + "``"
        [void]$sb.AppendLine($gLine)
        [void]$sb.AppendLine("")
    }

    # Helper pour ajouter une section detaillee au markdown
    $lines = New-Object System.Collections.ArrayList

    # Construction du markdown en assemblant des strings simples
    function Add-Line {
        param([System.Collections.ArrayList]$arr, [string]$s)
        [void]$arr.Add($s)
    }

    $lines = New-Object System.Collections.ArrayList

    if ($aliasable.Count -gt 0) {
        Add-Line $lines ("## ALIAS-FIX " + $aliasable.Count)
        Add-Line $lines ""
        Add-Line $lines "Renommer le wikilink vers le vrai nom de fiche."
        Add-Line $lines ""
        foreach ($g in $aliasable) {
            $head = "### ``[[" + $g.Target + "]]`` -> ``[[" + $g.AliasOf + "]]`` " + $g.Sources.Count + " ref"
            Add-Line $lines $head
            Add-Line $lines ""
            foreach ($s in $g.Sources) { Add-Line $lines ("- " + $s) }
            Add-Line $lines ""
        }
    }

    if ($prio.Count -gt 0) {
        Add-Line $lines ("## A CREER - " + $prio.Count + " cible(s) avec 3+ refs")
        Add-Line $lines ""
        Add-Line $lines "Fantomes references 3+ fois - candidats serieux a la creation."
        Add-Line $lines ""
        foreach ($g in $prio) {
            $head = "### ``[[" + $g.Target + "]]`` " + $g.Sources.Count + " ref"
            Add-Line $lines $head
            Add-Line $lines ""
            foreach ($s in $g.Sources) { Add-Line $lines ("- " + $s) }
            Add-Line $lines ""
        }
    }

    if ($mid.Count -gt 0) {
        Add-Line $lines ("## A DECIDER - " + $mid.Count + " cible(s) avec 2 refs")
        Add-Line $lines ""
        Add-Line $lines "Fantomes references 2 fois - decision au cas par cas."
        Add-Line $lines ""
        foreach ($g in $mid) {
            $head = "### ``[[" + $g.Target + "]]`` " + $g.Sources.Count + " ref"
            Add-Line $lines $head
            Add-Line $lines ""
            foreach ($s in $g.Sources) { Add-Line $lines ("- " + $s) }
            Add-Line $lines ""
        }
    }

    if ($low.Count -gt 0) {
        Add-Line $lines ("## FAIBLE - probablement a dewikilinker - " + $low.Count + " cible(s)")
        Add-Line $lines ""
        Add-Line $lines "Une seule reference. Le plus souvent : retirer le wikilink."
        Add-Line $lines ""
        foreach ($g in $low) {
            $line = "- ``[[" + $g.Target + "]]`` dans " + $g.Sources[0]
            Add-Line $lines $line
        }
        Add-Line $lines ""
    }

    foreach ($l in $lines) { [void]$sb.AppendLine($l) }

    [System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.Encoding]::UTF8)
    Write-Host "Rapport ecrit : $outPath" -ForegroundColor Cyan
}
