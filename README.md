# DevBrain

**Ma mémoire technique personnelle : un vault Obsidian versionné, lisible par moi comme par un agent IA, pour ne plus jamais rechoisir un outil ou refaire une erreur déjà loguée.**

![Obsidian](https://img.shields.io/badge/Obsidian-vault-7C3AED?logo=obsidian&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package_manager-DE5FE9?logo=uv&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-agent-D97757)

DevBrain est ma mémoire technique personnelle pour mes projets de dev (data science, data engineering, MLOps, ML/AI engineering). C'est un vault Obsidian versionné dans ce repo : des fiches structurées sur les outils, frameworks, patterns et retours d'expérience que j'utilise, écrites pour être lues aussi bien par moi que par un agent IA. Le but : ne plus jamais rechoisir une base vectorielle ou refaire une erreur déjà loguée — le brain garde la mémoire, le projet suivant en profite directement.

Il est fait pour être utilisé avec [Claude Code](https://docs.claude.com/en/docs/claude-code), qui le lit et l'enrichit à travers trois skills : `enrichir-brain` pour y ajouter une fiche, `cloturer-brain` pour clore toute écriture (régénérer, valider, committer), `planifier-projet` pour partir d'un cadrage de projet sourcé par le brain. Inspiré du [LLM Wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Installer

Deux choses, pas plus :

1. **Le vault** : cloner ce repo et l'ouvrir comme coffre Obsidian (+ 4 plugins : Local REST API, Templater, Dataview, File Hider).
2. **Les skills** : rien à faire — `enrichir-brain`, `cloturer-brain` et `planifier-projet` sont déjà dans `.claude/skills/`, chargés automatiquement dès que tu lances `claude` dans ce dossier. Invocables en langage naturel ("ajoute Qdrant au brain") ou en commande slash (`/enrichir-brain`, `/cloturer-brain`, `/planifier-projet`).

```bash
git clone https://github.com/floSa/DevBrain.git ~/DevBrain
```

**Guide pas à pas complet (avec captures d'écran) :** [INSTALL.md](INSTALL.md).

Pré-requis : Obsidian, Git, Node.js ≥ 18, Python ≥ 3.10, [`uv`](https://docs.astral.sh/uv/), Claude Code.

## Comment on l'alimente, comment on l'utilise

| | |
|---|---|
| **L'alimenter** | "ajoute Qdrant au brain", "documente le concept RAG" → le skill `enrichir-brain` crée/complète la page dans le dossier que sa `categorie:` donne — brique et notion du même sujet y vivent côte à côte —, câble les liens, régénère l'index. |
| **L'utiliser depuis un projet** | Depuis un *autre* projet, lancer `claude` avec `CLAUDE-project.md` en template → le skill `planifier-projet` interroge le brain et propose un stack sourcé (2-3 candidats par brique, avec pitch). |
| **Logger un retour d'expérience** | "log un bug : timeout sur Postgres" → pas de skill dédié aujourd'hui, Claude écrit à la main dans la section `## Pièges` de la brique concernée. |

## Ce que contient le brain

| | |
|---|---|
| **L'arbre** | 20 dossiers de domaine à la racine — 337 briques, 297 notions, 47 comparatifs, et une page hub par dossier |
| **Hors de l'arbre** | `Métiers/` (6 hubs transverses, générés depuis `domaines:`), `Patterns/` et `Rules/`, groupés par `role:` — aucune `categorie:` ne les range |
| **Skills** | `enrichir-brain` (capture), `cloturer-brain` (clôture + politique git), `planifier-projet` (cadrage) |
| **Rangement** | trois axes : `role:` ce que la page **est**, `categorie:` son **domaine** (qui donne son dossier), `famille:` la **nature technique** d'une brique — arbres de décision dans `Documentation/general/taxonomie.md` |
| **Garde-fous** | `check_brain.py` (le contenu) et `check_arbo.py` (le rangement), tous deux à passer au vert avant tout commit |

## Structure

```
DevBrain/
├── CLAUDE.md, CLAUDE-build.md, CLAUDE-project.md   ← contexte Claude Code (routeur + modes)
├── INSTALL.md / CONTRIBUTING.md / CHANGELOG.md      ← docs méta
│
├── <20 dossiers de domaine>/     ← l'arbre : Bases de données/, Machine Learning/,
│   │                               LLM & IA générative/, Data & pipelines/, Stockage/…
│   ├── <Domaine>.md              (role: hub — zone <!-- AUTO --> générée)
│   ├── <Sous-domaine>/           (promu à 5 pages, avec son propre hub)
│   ├── <Brique>.md               (role: brique)  <Notion>.md  (role: notion)
│   └── Comparatif - <thème>.base
│
├── Métiers/                      ← 6 hubs transverses, générés depuis `domaines:`
├── Patterns/                     ← Pattern - <nom>.md   (role: pattern)
├── Rules/                        ← Rule - <nom>.md      (role: rule)
├── Documentation/                ← gouvernance (tags, taxonomie, conventions perso)
├── Templates/                    ← gabarits Templater
├── Projects/                     ← log des projets en cours (scaffold, vide)
├── AI/                           ← espace agent (design, index généré, sessions, scripts)
└── .claude/skills/               ← enrichir-brain/, cloturer-brain/, planifier-projet/
```

## Conventions clés

- **Wikilinks nus, jamais qualifiés par chemin** : `[[Postgres]]`. Un lien qualifié casse au déplacement — le lot 3 a déplacé 682 fichiers sans en toucher un seul. Le pipe ne sert qu'à changer le texte affiché (`[[Postgres|la base]]`).
- **Frontmatter dense sur chaque brique** (`role`, `pitch`, `categorie`, `famille`, `licence_type`, `maturite`, `alternatives`, `complements`, `tags`…) — sert d'index plat pour Claude, sans avoir à charger le contenu.
- **Trois niveaux de règle** : `must` (bloquant), `should` (par défaut, écarts signalés), `nice-to-have` (si possible).

## Contribution

Repo privé. Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour l'anatomie du repo et les règles de modification par dossier.

## Licence

MIT — voir `LICENSE`.

## Crédits

- [Andrej Karpathy — LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Steph Ango (kepano) — Obsidian Skills](https://github.com/kepano/obsidian-skills)
- Ian Sinnott, MarkusPfundstein, et la communauté Obsidian + Claude Code
