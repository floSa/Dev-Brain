# discover-links.ps1 - Trouve les fiches du vault candidates a etre wikilinkees
# avec une nouvelle fiche (ou avec une fiche existante).
#
# Usage :
#
# 1. Avant creation : passer les metadata
#    powershell -File AI/scripts/discover-links.ps1 `
#        -Title "Adam optimizer" `
#        -Categorie "concept/optimization" `
#        -Domaines "ml-eng,ai-eng" `
#        -SousCategories "optimizer,gradient-descent,deep-learning"
#
# 2. Pour fiche existante : passer le path
#    powershell -File AI/scripts/discover-links.ps1 -Path "Wiki/Concepts/RAG.md"
#
# 3. Top-N (default 15)
#    -TopN 20
#
# Sortie : tableau markdown des candidats trie par score decroissant
# avec leur path et les wikilinks pre-formates a copier-coller.

param(
    [string]$Path = "",
    [string]$Title = "",
    [string]$Categorie = "",
    [string]$Domaines = "",         # comma-separated
    [string]$SousCategories = "",   # comma-separated
    [string]$Tags = "",             # comma-separated
    [string]$Alias = "",            # comma-separated
    [int]$TopN = 15,
    [string]$Galaxie = ""           # optionnel filtre dev/wiki/skills
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

# Parse YAML frontmatter simple (key: value | key: [a, b, c])
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

            # List : [a, b, c]
            if ($val -match '^\[(.*)\]$') {
                $items = $matches[1] -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") } | Where-Object { $_ -ne "" }
                $fm[$key] = $items
            }
            # Quoted string : "..."
            elseif ($val -match '^"(.*)"$') {
                $fm[$key] = $matches[1]
            }
            # Scalar
            else {
                $fm[$key] = $val
            }
        }
    }
    return $fm
}

function To-Array {
    param($value)
    if ($null -eq $value) { return ,@() }
    if ($value -is [string]) {
        if ($value.Trim() -eq "") { return ,@() }
        return ,@($value)
    }
    return ,@($value)
}

function Split-CSV {
    param([string]$s)
    if ($s -eq "") { return @() }
    return @($s -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" })
}

# Tokens d'un titre (pour matching mots)
function Get-TitleTokens {
    param([string]$title)
    $stopwords = @("the","of","and","or","a","an","de","la","le","les","du","des","et","ou","l","d","s",
                    "in","on","at","to","for","with","by","is","are","was","were","be","been","being",
                    "this","that","these","those")
    $tokens = ($title -split '[\s\-_/\.,\(\)]+') | ForEach-Object { $_.ToLower().Trim() }
    return @($tokens | Where-Object { $_ -ne "" -and $_ -notin $stopwords -and $_.Length -gt 1 })
}

# Collecte de toutes les fiches du vault
Write-Host "Scan du vault..."
$allFiches = @()
$files = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
    $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    -not (Should-Exclude $rel)
}

foreach ($file in $files) {
    $rel = $file.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    if ($file.Name -like "Roadmap*.md") { continue }   # skip roadmaps
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
    }
}

# Determiner les metadata de la "fiche cible"
$target = @{
    Name           = $Title
    Title          = $Title
    Path           = $Path
    Categorie      = $Categorie
    SousCategories = Split-CSV $SousCategories
    Domaines       = Split-CSV $Domaines
    Tags           = Split-CSV $Tags
    Alias          = Split-CSV $Alias
}

if ($Path -ne "") {
    $absPath = Join-Path $root $Path
    if (Test-Path $absPath) {
        $c = [System.IO.File]::ReadAllText($absPath, [System.Text.Encoding]::UTF8)
        $fm = Parse-Frontmatter $c
        if ($fm.ContainsKey('nom')) {
            $arr = @(To-Array $fm['nom'])
            if ($arr.Count -gt 0) { $target.Title = $arr[0]; $target.Name = $target.Title }
        }
        if ($target.Name -eq "") { $target.Name = [System.IO.Path]::GetFileNameWithoutExtension($Path) }
        if ($fm.ContainsKey('categorie')) {
            $arr = @(To-Array $fm['categorie'])
            if ($arr.Count -gt 0) { $target.Categorie = $arr[0] }
        }
        if ($fm.ContainsKey('sous_categories')) { $target.SousCategories = $fm['sous_categories'] }
        if ($fm.ContainsKey('domaines')) { $target.Domaines = $fm['domaines'] }
        if ($fm.ContainsKey('tags')) { $target.Tags = $fm['tags'] }
        if ($fm.ContainsKey('alias')) { $target.Alias = $fm['alias'] }
    } else {
        Write-Host "Path non trouve: $Path"
        exit 1
    }
}

if ($target.Title -eq "") {
    Write-Host ""
    Write-Host "Erreur : Specifier au minimum -Title ou -Path"
    Write-Host ""
    Write-Host "Exemples :"
    Write-Host "  -Title 'Adam' -Categorie 'concept/optimization' -Domaines 'ml-eng' -SousCategories 'optimizer,gradient'"
    Write-Host "  -Path 'Wiki/Concepts/RAG.md'"
    exit 1
}

# Tokens du titre cible
$targetTokens = Get-TitleTokens $target.Title
foreach ($a in $target.Alias) { $targetTokens += Get-TitleTokens $a }
$targetTokens = $targetTokens | Select-Object -Unique

# Scoring
$candidates = @()
foreach ($f in $allFiches) {
    # Skip soi-meme
    # Normaliser le path pour comparaison (slash unifie)
    $normalizedPath = $Path -replace '\\', '/'
    if ($normalizedPath -ne "" -and $f.Path -eq $normalizedPath) { continue }
    if ($Path -eq "" -and $f.Name -eq $target.Name) { continue }

    # Optional galaxie filter
    if ($Galaxie -ne "" -and $f.Galaxie -ne $Galaxie) { continue }

    $score = 0
    $reasons = @()

    # 1. Alias match dans le titre/alias de la candidate
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
                $score += 15
                $reasons += "alias-exact"
                $matched = $true
                break
            } elseif ($ctLow.Contains($termLow) -or $termLow.Contains($ctLow)) {
                $score += 8
                $reasons += "alias-partial"
                $matched = $true
                break
            }
        }
    }

    # 2. Same categorie
    if ($target.Categorie -ne "" -and $f.Categorie -eq $target.Categorie) {
        $score += 10
        $reasons += "categorie"
    } elseif ($target.Categorie -ne "" -and $f.Categorie -ne "") {
        # Same top-level (concept/llm vs concept/statistics)
        $tTop = ($target.Categorie -split '/')[0]
        $fTop = ($f.Categorie -split '/')[0]
        if ($tTop -eq $fTop) {
            $score += 4
            $reasons += "categorie-top"
        }
    }

    # 3. Domaines overlap
    $domOverlap = @($f.Domaines | Where-Object { $target.Domaines -contains $_ })
    if ($domOverlap.Count -gt 0) {
        $score += ($domOverlap.Count * 4)
        $reasons += "domaines:$($domOverlap -join '+')"
    }

    # 4. Sous-categories overlap
    $scOverlap = @($f.SousCategories | Where-Object { $target.SousCategories -contains $_ })
    if ($scOverlap.Count -gt 0) {
        $score += ($scOverlap.Count * 3)
        $reasons += "sous-cat:$($scOverlap -join '+')"
    }

    # 5. Tags overlap
    $tagOverlap = @($f.Tags | Where-Object { $target.Tags -contains $_ })
    if ($tagOverlap.Count -gt 0) {
        $score += ($tagOverlap.Count * 2)
        $reasons += "tags:$($tagOverlap -join '+')"
    }

    # 6. Title token overlap
    $candTokens = Get-TitleTokens $f.Title
    foreach ($a in $f.Alias) { $candTokens += Get-TitleTokens $a }
    $tokenOverlap = @($candTokens | Where-Object { $targetTokens -contains $_ } | Select-Object -Unique)
    if ($tokenOverlap.Count -gt 0) {
        $score += $tokenOverlap.Count
        $reasons += "mots:$($tokenOverlap -join '+')"
    }

    if ($score -gt 0) {
        $candidates += [PSCustomObject]@{
            Score   = $score
            Name    = $f.Name
            Title   = $f.Title
            Path    = $f.Path
            Galaxie = $f.Galaxie
            Type    = $f.Type
            Reasons = $reasons -join " | "
        }
    }
}

# Tri et top-N
$top = $candidates | Sort-Object -Property Score -Descending | Select-Object -First $TopN

# Sortie
Write-Host ""
Write-Host "Cible: $($target.Title)"
Write-Host "  categorie    : $($target.Categorie)"
Write-Host "  domaines     : $($target.Domaines -join ', ')"
Write-Host "  sous_cat     : $($target.SousCategories -join ', ')"
Write-Host "  tags         : $($target.Tags -join ', ')"
Write-Host ""
Write-Host "Top $TopN candidats a wikilinker :"
Write-Host ""

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("| Score | Wikilink | Galaxie | Type | Justification |")
[void]$sb.AppendLine("|---:|---|---|---|---|")
foreach ($c in $top) {
    $linkName = $c.Name
    if ($c.Title -ne $c.Name -and $c.Title -ne "") {
        $wikilink = "[[$linkName|$($c.Title)]]"
    } else {
        $wikilink = "[[$linkName]]"
    }
    [void]$sb.AppendLine("| $($c.Score) | ``$wikilink`` | $($c.Galaxie) | $($c.Type) | $($c.Reasons) |")
}

Write-Host $sb.ToString()

# Section copier-coller
Write-Host ""
Write-Host "--- Section 'Liens internes' a copier (top 8) ---"
Write-Host ""
Write-Host "**Liens internes** :"
foreach ($c in ($top | Select-Object -First 8)) {
    $linkName = $c.Name
    if ($c.Title -ne $c.Name -and $c.Title -ne "") {
        Write-Host "- [[$linkName|$($c.Title)]]"
    } else {
        Write-Host "- [[$linkName]]"
    }
}
