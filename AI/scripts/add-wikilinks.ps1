# add-wikilinks.ps1 - Wikilinke la premiere occurrence d'un nom dans un fichier
# (ou liste de fichiers). Sans toucher aux occurrences deja wikilinkees ni au
# frontmatter ni au code.
#
# Usage :
#   pwsh AI/scripts/add-wikilinks.ps1 -Name "BigQuery" -Files "a.md","b.md"
#   pwsh AI/scripts/add-wikilinks.ps1 -Name "Snowflake" -All     # cherche toutes les fiches qui le mentionnent
#
# Par defaut : dry-run (affiche les changements sans ecrire). Ajouter -Apply pour ecrire.

param(
    [Parameter(Mandatory)][string]$Name,
    [string[]]$Files = @(),
    [switch]$All,
    [switch]$Apply
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

# Si -All, scanner tout le vault
if ($All) {
    Write-Host "Recherche des fichiers contenant '$Name'..." -ForegroundColor DarkGray
    $candidates = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
        $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
        -not (Should-Exclude $rel)
    }
    $Files = @()
    foreach ($f in $candidates) {
        $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        # Strip frontmatter + code blocks pour le check
        $body = $content -replace '(?s)^---\r?\n.+?\r?\n---\r?\n', '' `
                          -replace '(?s)```.+?```', '' `
                          -replace '`[^`]+`', ''
        $pattern = '\b' + [regex]::Escape($Name) + '\b'
        # Si l'occurrence existe ET pas deja wikilinkee (verifier qu'on n'a pas que des [[Name]])
        $wikilinked = [regex]::Matches($body, '\[\[' + [regex]::Escape($Name) + '(?:\|[^\]]+)?\]\]').Count
        $bare = ([regex]::Matches($body, $pattern).Count) - $wikilinked
        if ($bare -gt 0) {
            $Files += $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
        }
    }
}

if ($Files.Count -eq 0) {
    Write-Host "Aucun fichier a traiter."
    exit 0
}

Write-Host ""
Write-Host "Traitement de $($Files.Count) fichier(s) pour '$Name'" -ForegroundColor Cyan
if (-not $Apply) { Write-Host "  (DRY RUN - ajouter -Apply pour ecrire)" -ForegroundColor Yellow }
Write-Host ""

# Self-link guard : ne pas wikilinker une fiche vers elle-meme
$selfFile = "$Name.md"

$changed = 0
foreach ($rel in $Files) {
    $full = Join-Path $root $rel
    if (-not (Test-Path $full)) {
        Write-Host "  [SKIP] $rel (introuvable)" -ForegroundColor DarkGray
        continue
    }
    if ([System.IO.Path]::GetFileName($rel) -eq $selfFile) {
        Write-Host "  [SKIP] $rel (self-link)" -ForegroundColor DarkGray
        continue
    }

    $content = [System.IO.File]::ReadAllText($full, [System.Text.Encoding]::UTF8)

    # Pattern : Name avec word-boundary, pas precede de [[ ni suivi de ]]
    # On replace la PREMIERE occurrence
    $pattern = '(?<!\[\[)\b' + [regex]::Escape($Name) + '\b(?!\]\])'

    # Eviter dans les zones interdites : frontmatter + code blocks
    # On split le contenu en zones safe / non-safe et on ne replace que dans safe.
    # Approche simple : remplacer dans tout le contenu sauf si l'occurrence est dans
    # un code block ou frontmatter. On le fait via une boucle de regex avec callback.

    $regex = [regex]::new($pattern)
    $newContent = $content
    $offset = 0
    $done = $false

    # Marquer les zones a eviter (frontmatter + code blocks + inline code)
    $forbidden = New-Object System.Collections.Generic.List[object]
    foreach ($m in [regex]::Matches($content, '(?s)^---\r?\n.+?\r?\n---\r?\n')) {
        $start = $m.Index
        $end = $start + $m.Length
        $forbidden.Add(@{Start=$start; End=$end}) | Out-Null
    }
    foreach ($m in [regex]::Matches($content, '(?s)```.+?```')) {
        $start = $m.Index
        $end = $start + $m.Length
        $forbidden.Add(@{Start=$start; End=$end}) | Out-Null
    }
    foreach ($m in [regex]::Matches($content, '`[^`]+`')) {
        $start = $m.Index
        $end = $start + $m.Length
        $forbidden.Add(@{Start=$start; End=$end}) | Out-Null
    }

    function Is-Forbidden {
        param([int]$pos, $ranges)
        foreach ($r in $ranges) {
            if ($pos -ge $r.Start -and $pos -lt $r.End) { return $true }
        }
        return $false
    }

    $matches = $regex.Matches($content)
    $targetMatch = $null
    foreach ($m in $matches) {
        if (-not (Is-Forbidden $m.Index $forbidden)) {
            $targetMatch = $m
            break
        }
    }

    if ($null -eq $targetMatch) {
        Write-Host "  [SKIP] $rel (aucune mention hors zone interdite)" -ForegroundColor DarkGray
        continue
    }

    $newContent = $content.Substring(0, $targetMatch.Index) + "[[" + $Name + "]]" + $content.Substring($targetMatch.Index + $targetMatch.Length)

    # Contexte pour le rapport
    $ctxStart = [Math]::Max(0, $targetMatch.Index - 40)
    $ctxEnd = [Math]::Min($content.Length, $targetMatch.Index + $targetMatch.Length + 40)
    $ctx = $content.Substring($ctxStart, $ctxEnd - $ctxStart) -replace "`r?`n", " "

    Write-Host "  [+] $rel" -ForegroundColor Green
    Write-Host "      ...$ctx..." -ForegroundColor DarkGray

    if ($Apply) {
        [System.IO.File]::WriteAllText($full, $newContent, (New-Object System.Text.UTF8Encoding $false))
        $changed++
    }
}

Write-Host ""
if ($Apply) {
    Write-Host "$changed fichier(s) modifie(s)." -ForegroundColor Cyan
} else {
    Write-Host "Dry run termine. Ajouter -Apply pour ecrire les changements." -ForegroundColor Yellow
}
