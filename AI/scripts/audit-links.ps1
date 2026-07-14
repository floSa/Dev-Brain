# audit-links.ps1 - Pour chaque fiche du vault, detecte les fiches
# pertinentes qui ne sont PAS encore wikilinkees. Permet de combler
# les liens manquants.
#
# Usage :
#   powershell -ExecutionPolicy Bypass -File AI/scripts/audit-links.ps1
#   -> ecrit AI/audits/links-audit-YYYY-MM-DD.md
#
#   # Auditer une seule fiche
#   powershell -File AI/scripts/audit-links.ps1 -Path "Wiki/Concepts/RAG.md"
#
#   # Limiter aux fiches d'une galaxie
#   powershell -File AI/scripts/audit-links.ps1 -Galaxie wiki
#
# Pour chaque fiche, calcule :
# - Les wikilinks deja presents
# - Le top-N candidats via le meme algo que discover-links
# - Reporte les candidats qui ne sont PAS deja wikilinkes (= liens manquants)
#
# Seuil minimal de score (default 8) pour eviter le bruit.

param(
    [string]$Path = "",
    [string]$Galaxie = "",
    [int]$TopN = 10,
    [int]$MinScore = 8
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $root

$EXCLUDE = @(".obsidian", "node_modules", ".git", "AI/sessions", "AI/audits",
             "Templates/ServiceDocs", ".claude")

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
    if ($content -notmatch '(?s)^(---\r?\n)(.+?)(\r?\n---)' ) { return $fm }
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

function Get-TitleTokens {
    param([string]$title)
    $stopwords = @("the","of","and","or","a","an","de","la","le","les","du","des","et","ou","l","d","s",
                    "in","on","at","to","for","with","by","is","are","was","were","be","been","being",
                    "this","that","these","those")
    $tokens = ($title -split '[\s\-_/\.,\(\)]+') | ForEach-Object { $_.ToLower().Trim() }
    return @($tokens | Where-Object { $_ -ne "" -and $_ -notin $stopwords -and $_.Length -gt 1 })
}

# Extraire les wikilinks deja presents dans une fiche (hors code spans/blocks)
function Get-ExistingLinks {
    param([string]$content)
    $stripped = $content -replace '(?s)```.*?```', '' -replace '`[^`]+`', ''
    $links = @{}
    $regex = [regex]'\[\[([^\]\|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]'
    foreach ($m in $regex.Matches($stripped)) {
        $target = $m.Groups[1].Value.Trim()
        if ($target -match '/') { $target = ($target -split '/')[-1] }
        $links[$target] = $true
    }
    return $links
}

# Collecte
Write-Host "Scan du vault..."
$allFiches = @()
$files = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
    $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    -not (Should-Exclude $rel)
}

foreach ($file in $files) {
    $rel = $file.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    if ($file.Name -like "Roadmap*.md") { continue }
    $name = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $fm = Parse-Frontmatter $content

    $fmGalaxie = if ($fm.ContainsKey('galaxie')) { [string]$fm['galaxie'] } else { "" }
    $fmType = if ($fm.ContainsKey('type')) { [string]$fm['type'] } else { "" }
    $fmTitle = if ($fm.ContainsKey('nom')) { [string]$fm['nom'] } else { $name }
    $fmCategorie = if ($fm.ContainsKey('categorie')) { [string]$fm['categorie'] } else { "" }
    $fmSousCat = if ($fm.ContainsKey('sous_categories')) { $fm['sous_categories'] } else { @() }
    $fmDomaines = if ($fm.ContainsKey('domaines')) { $fm['domaines'] } else { @() }
    $fmTags = if ($fm.ContainsKey('tags')) { $fm['tags'] } else { @() }
    $fmAlias = if ($fm.ContainsKey('alias')) { $fm['alias'] } else { @() }

    $allFiches += [PSCustomObject]@{
        Name           = $name
        Path           = $rel
        Galaxie        = $fmGalaxie
        Type           = $fmType
        Title          = $fmTitle
        Categorie      = $fmCategorie
        SousCategories = $fmSousCat
        Domaines       = $fmDomaines
        Tags           = $fmTags
        Alias          = $fmAlias
        Content        = $content
    }
}

# Filtres
$ficheToAudit = $allFiches
if ($Path -ne "") {
    $normPath = $Path -replace '\\', '/'
    $ficheToAudit = $allFiches | Where-Object { $_.Path -eq $normPath }
    if ($ficheToAudit.Count -eq 0) {
        Write-Host "Path non trouve: $Path"; exit 1
    }
}
if ($Galaxie -ne "") {
    $ficheToAudit = $ficheToAudit | Where-Object { $_.Galaxie -eq $Galaxie }
}

# Pour chaque fiche, calcule top candidats + filtre liens manquants
function Score-Pair {
    param($target, $f)
    $score = 0
    $reasons = @()

    # Alias match
    $allTargetTerms = @()
    if ($target.Title -ne "") { $allTargetTerms += [string]$target.Title }
    foreach ($a in $target.Alias) { if ($a -ne "") { $allTargetTerms += [string]$a } }
    $candidateTerms = @()
    if ($f.Title -ne "") { $candidateTerms += [string]$f.Title }
    foreach ($a in $f.Alias) { if ($a -ne "") { $candidateTerms += [string]$a } }

    $matched = $false
    foreach ($term in $allTargetTerms) {
        if ($matched) { break }
        $termLow = $term.ToLower()
        foreach ($ct in $candidateTerms) {
            $ctLow = $ct.ToLower()
            if ($ctLow -eq $termLow) {
                $score += 15; $reasons += "alias-exact"; $matched = $true; break
            } elseif ($ctLow.Contains($termLow) -or $termLow.Contains($ctLow)) {
                $score += 8; $reasons += "alias-partial"; $matched = $true; break
            }
        }
    }

    if ($target.Categorie -ne "" -and $f.Categorie -eq $target.Categorie) {
        $score += 10; $reasons += "categorie"
    } elseif ($target.Categorie -ne "" -and $f.Categorie -ne "") {
        $tTop = ($target.Categorie -split '/')[0]
        $fTop = ($f.Categorie -split '/')[0]
        if ($tTop -eq $fTop) { $score += 4; $reasons += "cat-top" }
    }

    $domOverlap = @($f.Domaines | Where-Object { $target.Domaines -contains $_ })
    if ($domOverlap.Count -gt 0) { $score += ($domOverlap.Count * 4); $reasons += "domaines:$($domOverlap -join '+')" }

    $scOverlap = @($f.SousCategories | Where-Object { $target.SousCategories -contains $_ })
    if ($scOverlap.Count -gt 0) { $score += ($scOverlap.Count * 3); $reasons += "souscat:$($scOverlap -join '+')" }

    $tagOverlap = @($f.Tags | Where-Object { $target.Tags -contains $_ })
    if ($tagOverlap.Count -gt 0) { $score += ($tagOverlap.Count * 2); $reasons += "tags:$($tagOverlap -join '+')" }

    $targetTokens = Get-TitleTokens $target.Title
    foreach ($a in $target.Alias) { $targetTokens += Get-TitleTokens $a }
    $targetTokens = $targetTokens | Select-Object -Unique
    $candTokens = Get-TitleTokens $f.Title
    foreach ($a in $f.Alias) { $candTokens += Get-TitleTokens $a }
    $tokenOverlap = @($candTokens | Where-Object { $targetTokens -contains $_ } | Select-Object -Unique)
    if ($tokenOverlap.Count -gt 0) { $score += $tokenOverlap.Count; $reasons += "mots:$($tokenOverlap -join '+')" }

    return @{ Score = $score; Reasons = $reasons -join " | " }
}

Write-Host "Calcul des liens manquants ($($ficheToAudit.Count) fiches a auditer)..."

$results = @()
$i = 0
$total = $ficheToAudit.Count
foreach ($target in $ficheToAudit) {
    $i++
    if ($i % 50 -eq 0) { Write-Host "  $i / $total..." }

    $existingLinks = Get-ExistingLinks $target.Content
    $candidates = @()
    foreach ($f in $allFiches) {
        if ($f.Path -eq $target.Path) { continue }
        $r = Score-Pair $target $f
        if ($r.Score -ge $MinScore -and -not $existingLinks.ContainsKey($f.Name)) {
            $candidates += [PSCustomObject]@{
                Score   = $r.Score
                Name    = $f.Name
                Title   = $f.Title
                Path    = $f.Path
                Galaxie = $f.Galaxie
                Reasons = $r.Reasons
            }
        }
    }

    $top = $candidates | Sort-Object Score -Descending | Select-Object -First $TopN
    if ($top.Count -gt 0) {
        $results += [PSCustomObject]@{
            Path        = $target.Path
            Name        = $target.Name
            Galaxie     = $target.Galaxie
            ExistingCount = $existingLinks.Count
            MissingTop  = $top
        }
    }
}

# Rapport
$today = Get-Date -Format "yyyy-MM-dd"
$reportPath = "AI/audits/links-audit-$today.md"

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("galaxie: ai")
[void]$sb.AppendLine("nom: Audit liens manquants $today")
[void]$sb.AppendLine("type: audit")
[void]$sb.AppendLine("created: $today")
[void]$sb.AppendLine("tags: [audit, links, report]")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("# Audit liens manquants - $today")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("> Genere par ``AI/scripts/audit-links.ps1`` (MinScore=$MinScore, TopN=$TopN).")
[void]$sb.AppendLine("> Pour chaque fiche, liste les fiches dont le score de similarite est >= $MinScore mais qui ne sont PAS deja wikilinkees.")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Stats")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("- Fiches auditees    : $($ficheToAudit.Count)")
[void]$sb.AppendLine("- Fiches avec liens manquants : $($results.Count)")
[void]$sb.AppendLine("- Total liens manquants candidats : $(($results | ForEach-Object { $_.MissingTop.Count } | Measure-Object -Sum).Sum)")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## Liens manquants par fiche")
[void]$sb.AppendLine("")

# Trier par nb de liens manquants (les fiches les plus orphelines en premier)
$resultsSorted = $results | Sort-Object { $_.MissingTop.Count } -Descending
foreach ($r in $resultsSorted) {
    [void]$sb.AppendLine("### ``$($r.Path)`` ($($r.MissingTop.Count) liens proposes)")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("| Score | Wikilink suggere | Galaxie | Justification |")
    [void]$sb.AppendLine("|---:|---|---|---|")
    foreach ($m in $r.MissingTop) {
        $link = if ($m.Title -ne $m.Name -and $m.Title -ne "") { "[[$($m.Name)|$($m.Title)]]" } else { "[[$($m.Name)]]" }
        [void]$sb.AppendLine("| $($m.Score) | ``$link`` | $($m.Galaxie) | $($m.Reasons) |")
    }
    [void]$sb.AppendLine("")
}

[System.IO.File]::WriteAllText($reportPath, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

Write-Host ""
Write-Host "Rapport ecrit : $reportPath"
Write-Host ""
Write-Host "Resume :"
Write-Host "  Fiches auditees                : $($ficheToAudit.Count)"
Write-Host "  Fiches avec liens manquants    : $($results.Count)"
Write-Host "  Total candidats (score >= $MinScore) : $(($results | ForEach-Object { $_.MissingTop.Count } | Measure-Object -Sum).Sum)"
