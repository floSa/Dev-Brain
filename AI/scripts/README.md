---
type: doc
created: 2026-05-21
modified: 2026-05-21
tags: [doc, scripts, audit]
---

# AI/scripts — outils de maintenance du vault

Cinq scripts PowerShell + un Python (hook session) pour auditer et maintenir le vault. Tous tournent depuis n'importe où, ils se replacent à la racine du vault automatiquement.

## Vue d'ensemble

| Script | Quand l'utiliser | Sortie |
|---|---|---|
| **`audit-vault.ps1`** | Audit global mensuel | `AI/audits/audit-YYYY-MM-DD.md` |
| **`report-ghosts.ps1`** | Lister tous les wikilinks fantômes du vault, groupés par cible | `AI/audits/ghosts-YYYY-MM-DD.md` |
| **`find-connexes.ps1`** | Avant/pendant/après création d'une fiche, voir qui la mentionne + fantômes dans la fiche | terminal |
| **`discover-links.ps1`** | Suggérer des wikilinks pour une fiche (top-N par scoring metadata) | terminal |
| **`audit-links.ps1`** | Trouver les wikilinks **manquants** : mentions sans wikilink | `AI/audits/links-audit-YYYY-MM-DD.md` |
| `gen-stubs-batch.ps1` | Générer en batch des stubs vides (déprécié — utiliser le skill `add-service`) | crée les `.md` |
| `session_to_devbrain.py` | Hook Stop Claude Code, résumé auto en fin de session | `AI/sessions/...` |

## Workflow type "création d'une nouvelle fiche"

1. **Avant** : `find-connexes -Name "NouveauTruc"` → voir qui mentionne déjà (à wikilinker après création)
2. **Pendant la rédaction** : remplir le frontmatter
3. **Après le draft** :
   - `find-connexes -Path "Services/X/NouveauTruc.md"` → fantômes que tu viens de créer + connexes
   - Corriger les fantômes (créer / dewikilinker)
4. **Optionnel** : `discover-links -Path "..."` pour enrichir les liens internes

## Workflow type "audit mensuel"

```powershell
# 1. État global du vault (parasites 0-byte, fiches sans galaxie, etc.)
powershell -File AI/scripts/audit-vault.ps1 -Cleanup -Force

# 2. Tous les fantômes restants, groupés par cible
powershell -File AI/scripts/report-ghosts.ps1

# 3. Tous les wikilinks manquants (mentions sans [[ ]])
powershell -File AI/scripts/audit-links.ps1
```

Puis ouvrir les 3 rapports dans `AI/audits/`, traiter en batch.

## Détail par script

### `audit-vault.ps1`

État global du vault. Pour chaque `.md` : galaxie, taille, frontmatter, sections clés (TL;DR, Code minimal, Pour aller plus loin pour les Concepts), wikilinks fantômes.

```powershell
# Audit simple
powershell -File AI/scripts/audit-vault.ps1

# + cleanup auto des fichiers 0-byte créés par clic accidentel sur fantômes
powershell -File AI/scripts/audit-vault.ps1 -Cleanup -Force
```

### `report-ghosts.ps1`

Liste les wikilinks fantômes du vault, **groupés par cible** (= rapport actionable). Trois buckets :

- **ALIAS-FIX** : une fiche existante a la cible dans son champ `alias:` → renommer le wikilink
- **A CREER** : 3+ références → candidat sérieux à la création
- **A DECIDER** : 2 références → décision au cas par cas
- **FAIBLE** : 1 référence → probablement dewikilinker

```powershell
powershell -File AI/scripts/report-ghosts.ps1
# Output : AI/audits/ghosts-YYYY-MM-DD.md + résumé terminal

# Filtrer par galaxie de la source
powershell -File AI/scripts/report-ghosts.ps1 -Galaxie wiki

# Ne signaler que les cibles avec 2+ refs
powershell -File AI/scripts/report-ghosts.ps1 -MinRefs 2
```

### `find-connexes.ps1`

Audit ciblé sur **une fiche** : qui la mentionne + fantômes qu'elle contient + suggestions par scoring metadata.

```powershell
# Par nom (pas besoin que la fiche existe)
powershell -File AI/scripts/find-connexes.ps1 -Name "SQLite"

# Par path (utilise aussi le frontmatter de la cible pour le scoring)
powershell -File AI/scripts/find-connexes.ps1 -Path "Services/Databases/SQLite.md"
```

Trois sections en sortie :
1. **[FORT] / [MOYEN] / [FAIBLE]** : pages qui mentionnent la cible (alternatives frontmatter / wikilinks corps / mentions texte sans lien)
2. **Wikilinks fantômes DANS la cible** (si `-Path`)
3. **Suggestions par scoring metadata** (catégorie, sous_categories, domaines, tags)

### `discover-links.ps1`

Suggère le top-N candidats à wikilinker pour une fiche, par scoring metadata (alias-exact +15, alias-partial +8, même catégorie +10, top-level cat +4, per domaine +4, per sous-cat +3, per tag +2, per mot +1).

```powershell
# Pour une fiche existante
powershell -File AI/scripts/discover-links.ps1 -Path "Wiki/Concepts/RAG.md"

# Pour une fiche pas encore créée
powershell -File AI/scripts/discover-links.ps1 `
    -Title "Adam optimizer" `
    -Categorie "concept/optimization" `
    -Domaines "ml-eng,ai-eng" `
    -SousCategories "optimizer,gradient-descent"
```

Sortie : tableau markdown trié par score + section "Liens internes" prête à coller.

### `audit-links.ps1`

Inverse de `discover-links` : pour chaque fiche du vault, trouve les candidats **non encore wikilinkés** (= liens manquants à ajouter).

```powershell
# Tout le vault
powershell -File AI/scripts/audit-links.ps1

# Une seule fiche
powershell -File AI/scripts/audit-links.ps1 -Path "Wiki/Concepts/RAG.md"

# Une galaxie
powershell -File AI/scripts/audit-links.ps1 -Galaxie wiki

# Seuil minimum de score (défaut 8)
powershell -File AI/scripts/audit-links.ps1 -MinScore 12
```

## Conventions communes

- **Exclusions** : tous les scripts ignorent `.obsidian/`, `.git/`, `node_modules/`, `AI/sessions/`, `AI/audits/`, `_orphans/`, `.claude/`
- **Encoding** : UTF-8 partout (les scripts lisent explicitement en UTF-8 même si Windows PS 5.1)
- **Helper functions** dupliquées (`Parse-Frontmatter`, `Should-Exclude`) pour rester self-contained ; refactor possible en module si ça grossit
- **PowerShell 5.1** : tous les scripts marchent sur PS 5.1 natif Windows (pas besoin de pwsh 7)
