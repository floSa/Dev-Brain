---
galaxie: meta
type: session
date: 2026-06-04
mode: build
tags: [session, build, v2]
---

# Session 2026-06-04 — Reconstruction DevBrain v2 (fondation + batch de validation)

Spec de référence : `AI/design/brain-v2.md` (récupérée depuis la branche `claude/great-galileo-3ef2bd`).
Principe : rangement par **audience** (Dev/ pour l'IA, Wiki/ pour l'humain). Le contenu v1 reste **réservoir de référence** (non migré, non modifié).

## Fait

### ÉTAPE 1 — Fondation
- Arborescence v2 : `Dev/{Services,Patterns,Rules,REX}`, `Documentation/{general,perso}`, `AI/index/`.
- `Documentation/general/` : `tags.md` (vocabulaire contrôlé, 7 tags du batch), `taxonomie.md`, `themes.md` (5 domaines), `questions-projet.md` (checklist §8).
- `Documentation/perso/` : `conventions.md`, `archetypes.md` (7 archétypes), `machines.md` (scaffold).
- `Templates/` : `Service-Dev.md` + `Concept-Wiki.md`, conformes §5 (frontmatter exact, ton impersonnel).

### ÉTAPE 2 — Script d'index
- `AI/scripts/build_index.py` : scanne `Dev/` + `Wiki/`, génère `AI/index/brain-index.json`.
- Python via **uv** (PEP 723, deps inline `pyyaml`). Cross-OS, aucun chemin absolu, sortie déterministe.
- Lancement : `uv run AI/scripts/build_index.py`.

### ÉTAPE 3 — Batch de validation (cluster bases vectorielles)
- Concept Wiki : `Wiki/Concepts/Bases de données vectorielles.md`.
- Services Dev : `Weaviate`, `Qdrant`, `pgvector` (pitch propre, alternatives croisées réutilisant le pitch cible).
- Comparatif : `Dev/Patterns/Comparatif - Bases vectorielles.base`.
- Liens Dev↔Wiki câblés ; index régénéré.

### ÉTAPE 4 — Skills + test
- `Skills/enrichir-brain/SKILL.md` (W1, §7.1) et `Skills/planifier-projet/SKILL.md` (W2, §7.2).
- Test : ajout de `Milvus` via le protocole enrichir-brain → réciprocité des alternatives **vérifiée** (4/4), `.base` capte Milvus automatiquement, Dev↔Wiki OK.

## Décisions
- Frontmatter Service/Concept strictement §5 : pas de `created`/`modified` ; champs morts supprimés (`score`, `mes_projets`, etc.).
- Liens vers les services v2 **qualifiés par chemin** (`[[Dev/Services/Qdrant|Qdrant]]`) à cause des collisions de noms avec le réservoir v1.
- Catégories `concept/*` dérivées du réservoir v1 + spec — **à valider** par floSa.
- `.gitkeep` dans `Dev/Rules` et `Dev/REX` (vides après le batch).

## À reprendre
- Valider les catégories `concept/*` et le vocabulaire de tags de départ.
- §10 : plan de migration du contenu v1 (remplir `pitch`/`scaling`, élaguer les champs morts, repasser au gabarit v2).
- MOC par thème (`Documentation/themes.md` → pages-index).
- Réécrire les autres scripts utilitaires v1 (PowerShell → Python) si besoin.
- Skills v1 à porter/retirer (`add-service`, `cross-link`, `process-inbox`…) vers la logique v2.
