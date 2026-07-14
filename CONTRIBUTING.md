---
galaxie: meta
nom: CONTRIBUTING
type: meta-doc
created: 2026-05-20
modified: 2026-07-07
tags: [meta]
---

# Contribuer à DevBrain

> Ce document s'adresse à **toi dans 6 mois** ou à un collègue qui rejoint le brain. Lis-le avant de toucher au repo.

## Philosophie en 3 lignes

1. **Trois usages, trois modes** : `build` (enrichir le brain agent), `project` (utiliser le brain depuis un projet), `wiki` (gérer ses concepts/notions perso).
2. **Frontières strictes** : chaque pilier a sa zone modifiable selon le mode. Pas de cross-écriture sans confirmation.
3. **Frontmatter > prose** : la connaissance "factuelle" (Services, Outils) est en YAML dense, queryable. La prose est pour la nuance.

## Anatomie du repo (v2)

| Dossier | Mode autorisé | Rôle | Ouvrir avec |
|---|---|---|---|
| `Dev/Services/` | build | Fiches techniques par outil déployé (agent-readable) | skill `enrichir-brain` |
| `Dev/Outils/` | build | Fiches outils techniques utilisés (clients GUI, CLI…) | skill `enrichir-brain` |
| `Dev/Patterns/` | build | Patterns archi + comparatifs `.base` | skill `enrichir-brain` |
| `Dev/Rules/` | build | Règles transverses | éditeur direct |
| `Dev/REX/` | build, project | REX par service | éditeur direct / `mcp__devbrain__patch_content` (pas de skill dédié en v2) |
| `Wiki/Concepts/` | wiki (+ build via `enrichir-brain`) | Notions à retrouver vite | skill `enrichir-brain` / Templater `Concept-Wiki` |
| `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` | wiki | Vides — contenu v1 pas encore remigré | — |
| `MOC/` | généré | Hubs de navigation (Themes/Categories/Concepts) | `AI/scripts/build_mocs.py`, ne pas éditer à la main |
| `Documentation/` | build/wiki selon sous-dossier | Gouvernance : tags, taxonomie, thèmes, conventions perso | éditeur direct |
| `Projects/` | build (log) | Suivi des projets actifs — scaffold vide aujourd'hui | éditeur direct |
| `Templates/` | build, wiki | Gabarits Templater | éditeur direct |
| `AI/` | tous (agent) | Espace de l'agent (design, index généré, sessions, scripts, backlog) | agent uniquement |
| `.claude/` | tous | Config Claude Code + skills custom (`enrichir-brain`, `planifier-projet`) | éditeur, voir `.claude/README.md` |
| `docs/install/` | tous | Captures et ressources pour `INSTALL.md` | éditeur direct |

## Règles de modification

### Dev/ (Services, Outils, Patterns, Rules) — strict

- **Frontmatter obligatoire et conforme** au schéma de `CLAUDE-build.md`.
- **Taxonomie verrouillée** : catégories dans `Documentation/general/taxonomie.md` uniquement — pas d'en inventer. Si rien ne va, ouvrir une discussion avant.
- **Statuts** : `actif | en-eval | abandonne` — pour `Dev/Services/` **et** `Dev/Outils/` (même échelle depuis la v2).
- **Tags** : uniquement ceux de `Documentation/general/tags.md` — proposer avant d'ajouter.
- Le champ `score` a été **supprimé en v2** (jamais fiable) — ne pas le réintroduire.

### Wiki — souple mais formaté

- Frontmatter obligatoire (`galaxie: wiki`, `type: concept`, `categorie: concept/<sous-domaine>`, `domaines:`, `tags:`), champs plus libres qu'en Dev.
- Nouveau sous-dossier `Wiki/<nom>/` OK si une nouvelle catégorie émerge.
- Wikilinks : ne pas créer de `[[X]]` vers du vide. Soit créer la cible, soit utiliser une référence inline.
- `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` sont vides : le workflow `discovered → tested → used → abandoned` hérité de la v1 n'a pas été retranché ni reconfirmé pour la v2 — à trancher si/quand ce pilier est remigré (cf. `Documentation/perso/reservoir-v1.md`).

### CLAUDE\*.md — modifier avec prudence

- `CLAUDE.md` (routeur) : ne touche que si tu ajoutes un mode ou une frontière.
- `CLAUDE-build.md` (contexte build) : ajouts de taxonomie OK, refonte = discussion.
- `CLAUDE-project.md` : c'est un **template** copié dans des projets externes. Modifier rétro-impacte les projets futurs.

## Workflow type

### Ajouter un Service ou un Outil

```
mode build
> ajoute le service <nom>, voici l'URL : <url>
```

Le skill `enrichir-brain` :
1. Vérifie non-duplication (alias inclus)
2. Extrait depuis l'URL via `defuddle`
3. Identifie les pages connexes nécessaires (alternatives, comparatif)
4. Te montre la fiche avant écriture, synchronise les alternatives bidirectionnellement, régénère l'index

Tu valides, il écrit dans `Dev/Services/<Nom>.md` (ou `Dev/Outils/<Nom>.md`).

### Ajouter un concept Wiki

```
mode wiki
> ajoute le concept <nom>
```

Le skill `enrichir-brain` fait l'équivalent dans `Wiki/Concepts/<nom>.md`.

### Logger un bug rencontré

Pas de skill dédié en v2. En mode build ou project :
```
> log un bug : <symptôme> sur <service>
```
Crée ou enrichis `Dev/REX/REX - <Service>.md` avec une entrée datée, au format standard (cf. `CLAUDE-build.md`).

### Comparer des services

```
mode build
> compare <X> et <Y> et <Z> sur la catégorie <cat>
```

Le skill `enrichir-brain` crée/met à jour `Dev/Patterns/Comparatif - <thème>.base`.

## Commits

Format **Conventional Commits**, en français OK pour la description :

```
feat(<scope>): ajout de X
fix(<scope>): correction Y
docs(<scope>): améliore Z
chore(<scope>): refactor/nettoyage W
```

Scopes courants : `services`, `outils`, `wiki`, `patterns`, `rules`, `rex`, `moc`, `documentation`, `infra`, `docs`, `templates`.

Exemples vus dans l'historique récent :
- `docs(brain): catégorie automation + 5 services no-code`
- `docs(outils): Postman, Bruno (clients d'API) + Continue, Aider, Cline (assistants IA de code)`
- `docs(services): faker, Mimesis, SDV — génération de données factices & synthétiques`

## Ce qui n'est pas toléré

- Mettre `maturite: production` ou `status: actif` sur une fiche jamais vérifiée en réel.
- Wikilinks vers du vide (`[[Truc]]` sans fichier `Truc.md`).
- Modifier une fiche `status: abandonne` sans discussion.
- Push direct sur `main` avec `--force` (sauf cas exceptionnel discuté).
- Commit des fichiers `.obsidian/plugins/`, `.obsidian/community-plugins.json`, `.obsidian/graph.json` (déjà gitignorés).
- Commit de secrets, clés API, URLs avec tokens (cf. `.gitignore`).

## MCP Obsidian — convention d'utilisation

Quand le MCP `devbrain` (instance de `mcp-obsidian`) est connecté (`claude mcp list` → `✓ Connected`), les skills qui touchent au vault **préfèrent les outils `mcp__devbrain__*` aux outils standard** :

- `mcp__devbrain__read_file_content` au lieu de `Read` pour les .md du vault
- `mcp__devbrain__create_file` / `patch_content` / `append_to_file` au lieu de `Write` / `Edit`
- `mcp__devbrain__search_files` au lieu de `Grep` pour la recherche full-text
- `mcp__devbrain__list_files_in_dir` au lieu de `Glob`

Raison : le MCP respecte le format Obsidian (frontmatter, wikilinks, properties typées) et déclenche la ré-indexation du vault (Bases mises à jour, backlinks recalculés).

**Fallback** sur les outils standard si Obsidian n'est pas ouvert ou MCP non configuré — cas dégradé mais fonctionnel.

## Setup local

Voir [`INSTALL.md`](INSTALL.md) — guide pas à pas avec captures.

Au premier clone :
1. Copier `.claude/settings.example.json` → `.claude/settings.json` (lis avant)
2. Copier `.claude/settings.local.example.json` → `.claude/settings.local.json`
3. Personnaliser `CLAUDE.md` (identité utilisateur)

## En cas de doute

Pose la question avant d'agir. La taxonomie est délibérément étroite — l'inventer rend le brain inutile à terme.
