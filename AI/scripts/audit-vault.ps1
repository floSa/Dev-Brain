# Audit DevBrain - Genere un rapport sur l'etat du vault.
#
# Usage :
#   powershell -ExecutionPolicy Bypass -File AI/scripts/audit-vault.ps1
#   -> ecrit AI/audits/audit-YYYY-MM-DD.md
#
# Verifie pour chaque .md :
# - Galaxie (dev / wiki / skills / aucune)
# - Taille (vide / stub / normal / complet)
# - Frontmatter (galaxie, type, modified)
# - Sections cles pour Concepts (TL;DR, Code minimal, Pour aller plus loin)
# - Wikilinks fantomes
#
# Options :
#   -Cleanup    : supprime les fichiers 0-byte trouves (parasites Obsidian
#                 crees par clic sur wikilinks fantomes). Demande
#                 confirmation par fichier sauf si -Force.
#   -Force      : utilise avec -Cleanup pour supprimer sans confirmation.

param(
    [switch]$Cleanup,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $root

# Cleanup des fichiers 0-byte avant tout
if ($Cleanup) {
    Write-Host "Recherche des fichiers .md 0-byte (parasites)..."
    $zeros = Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
        $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
        if ($rel.StartsWith(".git/")) { return $false }
        if ($rel.StartsWith(".obsidian/")) { return $false }
        $_.Length -eq 0
    }
    if ($zeros.Count -eq 0) {
        Write-Host "  Aucun fichier 0-byte trouve."
    } else {
        Write-Host "  $($zeros.Count) fichier(s) 0-byte detectes :"
        foreach ($z in $zeros) {
            $rel = $z.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
            if ($Force) {
                Remove-Item $z.FullName -Force
                Write-Host "    supprime: $rel"
            } else {
                $ans = Read-Host "    Supprimer '$rel' ? (y/N)"
                if ($ans -eq "y") {
                    Remove-Item $z.FullName -Force
                    Write-Host "      OK supprime"
                }
            }
        }
    }
    Write-Host ""
}

# Bornes de taille (lignes de contenu hors frontmatter)
$THRESHOLD_EMPTY = 10
$THRESHOLD_STUB = 50
$THRESHOLD_COMPLETE = 200

# Dossiers a exclure de l'audit
# - .obsidian, node_modules, .git : techniques
# - AI/sessions, AI/audits : auto-generes
# - Templates/ServiceDocs : fragments copies dans projets (pas du wiki content)
# - .claude : config Claude Code local
$EXCLUDE = @(".obsidian", "node_modules", ".git", "AI/sessions", "AI/audits",
             "Templates/ServiceDocs", ".claude")

function Get-MarkdownFiles {
    Get-ChildItem -Path . -Filter "*.md" -Recurse -File | Where-Object {
        $rel = $_.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
        $skip = $false
        foreach ($e in $EXCLUDE) {
            if ($rel.StartsWith($e + "/") -or $rel -eq $e) { $skip = $true; break }
        }
        -not $skip
    }
}

function Get-Galaxie {
    param([string]$relPath, [string]$content)
    if ($content -match '(?m)^galaxie:\s*([a-z]+)') {
        return $matches[1]
    }
    if ($relPath -match '^AI/skills/') { return "skills" }
    if ($relPath -match '^(Services|Bugs|Patterns|Rules|Projects|Templates)/') { return "dev?" }
    if ($relPath -match '^Wiki/') { return "wiki?" }
    if ($relPath -match '^AI/(audits|decisions|scripts)/') { return "meta?" }
    # docs meta racine
    if ($relPath -notmatch '/' -and $relPath -match '\.md$') { return "meta?" }
    return ""
}

function Get-FrontmatterField {
    param([string]$content, [string]$field)
    if ($content -match "(?m)^${field}:\s*(.+)$") {
        return $matches[1].Trim()
    }
    return ""
}

function Get-Status {
    param([int]$lines)
    if ($lines -le $THRESHOLD_EMPTY) { return "VIDE" }
    if ($lines -le $THRESHOLD_STUB)  { return "STUB" }
    if ($lines -le $THRESHOLD_COMPLETE) { return "NORMAL" }
    return "COMPLET"
}

function Get-ContentLines {
    param([string]$content)
    $lines = $content -split "`n"
    $inFm = $false
    $bodyLines = 0
    $first = $true
    foreach ($l in $lines) {
        if ($first -and $l.Trim() -eq "---") { $inFm = $true; $first = $false; continue }
        $first = $false
        if ($inFm -and $l.Trim() -eq "---") { $inFm = $false; continue }
        if ($inFm) { continue }
        if ($l.Trim() -ne "") { $bodyLines++ }
    }
    return $bodyLines
}

function Has-Section {
    param([string]$content, [string]$pattern)
    return $content -match $pattern
}

# Collecte
Write-Host "Scan en cours..."
$files = Get-MarkdownFiles
$entries = @()

foreach ($file in $files) {
    $rel = $file.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)

    $bodyLines = Get-ContentLines $content
    $galaxie = Get-Galaxie -relPath $rel -content $content
    $type = Get-FrontmatterField $content 'type'
    $modified = Get-FrontmatterField $content 'modified'
    $status = Get-Status $bodyLines

    $isConcept = $rel -match '^Wiki/Concepts/'
    $hasTldr = if ($isConcept) { Has-Section $content '(?m)^##\s*TL;DR' } else { $true }
    $hasCode = if ($isConcept) { Has-Section $content '(?m)^##\s*Code minimal' } else { $true }
    $hasFurther = if ($isConcept) { Has-Section $content '(?m)^##\s*Pour aller plus loin' } else { $true }

    $entries += [PSCustomObject]@{
        Path        = $rel
        Galaxie     = if ($galaxie) { $galaxie } else { "-" }
        Type        = if ($type) { $type } else { "-" }
        Lines       = $bodyLines
        Status      = $status
        Modified    = if ($modified) { $modified } else { "-" }
        IsConcept   = $isConcept
        HasTldr     = $hasTldr
        HasCode     = $hasCode
        HasFurther  = $hasFurther
        NoGalaxie   = ($galaxie -eq "" -or $galaxie.EndsWith("?"))
    }
}

# Wikilinks fantomes
Write-Host "Scan wikilinks..."
$existing = @{}
foreach ($f in $files) {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $existing[$name] = $true
}

$broken = @{}
foreach ($f in $files) {
    if ($f.Name -like "Roadmap*.md") { continue }
    $rel = $f.FullName.Substring($root.Path.Length + 1) -replace '\\', '/'

    # Skip Templates/ (placeholders attendus) - les Templates pre-remplissent des
    # wikilinks qui n'existent pas encore (et c'est le but du template).
    if ($rel.StartsWith("Templates/")) { continue }

    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    $stripped = $content -replace '(?s)```.*?```', '' -replace '`[^`]+`', ''

    $regex = [regex]'\[\[([^\]\|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]'
    foreach ($m in $regex.Matches($stripped)) {
        $target = $m.Groups[1].Value.Trim()

        # Skip placeholders Templater (contiennent < > ou tp.)
        if ($target -match '[<>]' -or $target -match '\btp\.') { continue }

        if ($target -match '/') { $target = ($target -split '/')[-1] }
        if (-not $existing.ContainsKey($target)) {
            if (-not $broken.ContainsKey($target)) { $broken[$target] = @() }
            $broken[$target] += $rel
        }
    }
}

# Generation du rapport
$today = Get-Date -Format "yyyy-MM-dd"
$reportPath = "AI/audits/audit-$today.md"

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("galaxie: ai")
[void]$sb.AppendLine("nom: Audit vault $today")
[void]$sb.AppendLine("type: audit")
[void]$sb.AppendLine("created: $today")
[void]$sb.AppendLine("tags: [audit, vault, report]")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("# Audit DevBrain - $today")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("> Genere par ``AI/scripts/audit-vault.ps1``. Re-run pour rafraichir.")
[void]$sb.AppendLine("")

# Stats globales
$total = $entries.Count
$byGalaxie = $entries | Group-Object -Property Galaxie | Sort-Object Name
$byStatus = $entries | Group-Object -Property Status

[void]$sb.AppendLine("## Stats globales")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("- **Total .md** : $total")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Par galaxie")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Galaxie | Compte |")
[void]$sb.AppendLine("|---|---:|")
foreach ($g in $byGalaxie) {
    [void]$sb.AppendLine("| $($g.Name) | $($g.Count) |")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Galaxies suffixees avec ? = devinees par chemin, frontmatter ``galaxie:`` manquant.")
[void]$sb.AppendLine("")

[void]$sb.AppendLine("### Par statut taille")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Bornes : VIDE <= $THRESHOLD_EMPTY lignes / STUB <= $THRESHOLD_STUB / NORMAL <= $THRESHOLD_COMPLETE / COMPLET au-dela.")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Statut | Compte |")
[void]$sb.AppendLine("|---|---:|")
foreach ($s in @("VIDE","STUB","NORMAL","COMPLET")) {
    $count = ($entries | Where-Object Status -eq $s).Count
    [void]$sb.AppendLine("| $s | $count |")
}
[void]$sb.AppendLine("")

# Section : pages sans etiquette galaxie
$noGalaxie = $entries | Where-Object NoGalaxie | Sort-Object Path
[void]$sb.AppendLine("## Pages SANS etiquette ``galaxie:`` ($($noGalaxie.Count))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Frontmatter incomplet -> pas de couleur dans le graph view Obsidian.")
[void]$sb.AppendLine("")
if ($noGalaxie.Count -gt 0) {
    [void]$sb.AppendLine("| Fichier | Galaxie devinee | Lignes | Action |")
    [void]$sb.AppendLine("|---|---|---:|---|")
    foreach ($e in $noGalaxie) {
        $action = if ($e.Status -eq "VIDE") { "SUPPRIMER ?" }
                  elseif ($e.Status -eq "STUB") { "completer ou supprimer" }
                  else { "ajouter ``galaxie:`` au frontmatter" }
        [void]$sb.AppendLine("| ``$($e.Path)`` | $($e.Galaxie) | $($e.Lines) | $action |")
    }
} else {
    [void]$sb.AppendLine("Aucune.")
}
[void]$sb.AppendLine("")

# Section : pages VIDES
$empty = $entries | Where-Object Status -eq "VIDE" | Sort-Object Path
[void]$sb.AppendLine("## Pages VIDES ($($empty.Count))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Moins de $THRESHOLD_EMPTY lignes de contenu. Candidats a la suppression.")
[void]$sb.AppendLine("")
if ($empty.Count -gt 0) {
    [void]$sb.AppendLine("| Fichier | Galaxie | Lignes |")
    [void]$sb.AppendLine("|---|---|---:|")
    foreach ($e in $empty) {
        [void]$sb.AppendLine("| ``$($e.Path)`` | $($e.Galaxie) | $($e.Lines) |")
    }
} else {
    [void]$sb.AppendLine("Aucune.")
}
[void]$sb.AppendLine("")

# Section : pages STUB
$stubs = $entries | Where-Object Status -eq "STUB" | Sort-Object Path
[void]$sb.AppendLine("## Pages STUB ($($stubs.Count))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Entre $($THRESHOLD_EMPTY+1) et $THRESHOLD_STUB lignes. A completer ou decider.")
[void]$sb.AppendLine("")
if ($stubs.Count -gt 0) {
    [void]$sb.AppendLine("| Fichier | Galaxie | Type | Lignes |")
    [void]$sb.AppendLine("|---|---|---|---:|")
    foreach ($e in $stubs) {
        [void]$sb.AppendLine("| ``$($e.Path)`` | $($e.Galaxie) | $($e.Type) | $($e.Lines) |")
    }
} else {
    [void]$sb.AppendLine("Aucune.")
}
[void]$sb.AppendLine("")

# Section : Concepts qui manquent de sections cles
$conceptsMissing = $entries | Where-Object { $_.IsConcept -and (-not $_.HasTldr -or -not $_.HasCode -or -not $_.HasFurther) } | Sort-Object Path
[void]$sb.AppendLine("## Fiches Concepts incompletes ($($conceptsMissing.Count))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Sections attendues : TL;DR / Code minimal / Pour aller plus loin.")
[void]$sb.AppendLine("")
if ($conceptsMissing.Count -gt 0) {
    [void]$sb.AppendLine("| Fichier | TL;DR | Code minimal | Pour aller plus loin |")
    [void]$sb.AppendLine("|---|:-:|:-:|:-:|")
    foreach ($e in $conceptsMissing) {
        $t = if ($e.HasTldr) { "Y" } else { "N" }
        $c = if ($e.HasCode) { "Y" } else { "N" }
        $fu = if ($e.HasFurther) { "Y" } else { "N" }
        [void]$sb.AppendLine("| ``$($e.Path)`` | $t | $c | $fu |")
    }
} else {
    [void]$sb.AppendLine("Aucune.")
}
[void]$sb.AppendLine("")

# Section : wikilinks fantomes
[void]$sb.AppendLine("## Wikilinks fantomes ($($broken.Count))")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Liens ``[[X]]`` vers des fichiers inexistants (hors Roadmap, hors code spans/blocks).")
[void]$sb.AppendLine("")
if ($broken.Count -gt 0) {
    [void]$sb.AppendLine("| Lien fantome | Sources |")
    [void]$sb.AppendLine("|---|---|")
    foreach ($k in ($broken.Keys | Sort-Object)) {
        $sources = ($broken[$k] | Select-Object -Unique) -join ", "
        [void]$sb.AppendLine("| ``[[$k]]`` | $sources |")
    }
} else {
    [void]$sb.AppendLine("Aucun.")
}
[void]$sb.AppendLine("")

# Section : tableau complet par galaxie
[void]$sb.AppendLine("## Tableau complet")
[void]$sb.AppendLine("")
foreach ($g in $byGalaxie) {
    $galaxieFiles = $entries | Where-Object Galaxie -eq $g.Name | Sort-Object Path
    [void]$sb.AppendLine("### Galaxie ``$($g.Name)`` ($($galaxieFiles.Count))")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("| Fichier | Type | Statut | Lignes | Modified |")
    [void]$sb.AppendLine("|---|---|---|---:|---|")
    foreach ($e in $galaxieFiles) {
        [void]$sb.AppendLine("| ``$($e.Path)`` | $($e.Type) | $($e.Status) | $($e.Lines) | $($e.Modified) |")
    }
    [void]$sb.AppendLine("")
}

[System.IO.File]::WriteAllText($reportPath, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

Write-Host ""
Write-Host "Rapport ecrit : $reportPath"
Write-Host ""
Write-Host "Resume :"
Write-Host "  Total .md            : $total"
Write-Host "  Sans galaxie         : $($noGalaxie.Count)"
Write-Host "  Vides                : $($empty.Count)"
Write-Host "  Stubs                : $($stubs.Count)"
Write-Host "  Concepts incomplets  : $($conceptsMissing.Count)"
Write-Host "  Wikilinks fantomes   : $($broken.Count)"
