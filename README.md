# DevBrain

**Ma mémoire technique personnelle : un vault Obsidian versionné, lisible par moi comme par un agent IA, pour ne plus jamais rechoisir un outil ou refaire une erreur déjà loguée.**

![Obsidian](https://img.shields.io/badge/Obsidian-vault-7C3AED?logo=obsidian&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package_manager-DE5FE9?logo=uv&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-agent-D97757)

DevBrain est ma mémoire technique personnelle pour mes projets de dev (data science, data engineering, MLOps, ML/AI engineering). C'est un vault Obsidian versionné dans ce repo : des fiches structurées sur les outils, frameworks, patterns et retours d'expérience que j'utilise, écrites pour être lues aussi bien par moi que par un agent IA. Le but : ne plus jamais rechoisir une base vectorielle ou refaire une erreur déjà loguée — le brain garde la mémoire, le projet suivant en profite directement.

Il est fait pour être utilisé avec [Claude Code](https://docs.claude.com/en/docs/claude-code), qui le lit et l'enrichit à travers deux skills : `enrichir-brain` pour y ajouter une fiche, `planifier-projet` pour partir d'un cadrage de projet sourcé par le brain. Inspiré du [LLM Wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Installer

Deux choses, pas plus :

1. **Le vault** : cloner ce repo et l'ouvrir comme coffre Obsidian (+ 4 plugins : Local REST API, Templater, Dataview, File Hider).
2. **Les skills** : rien à faire — `enrichir-brain` et `planifier-projet` sont déjà dans `.claude/skills/`, chargés automatiquement dès que tu lances `claude` dans ce dossier. Invocables en langage naturel ("ajoute Qdrant au brain") ou en commande slash (`/enrichir-brain`, `/planifier-projet`).

```bash
git clone https://github.com/floSa/DevBrain.git ~/DevBrain
```

**Guide pas à pas complet (avec captures d'écran) :** [INSTALL.md](INSTALL.md).

Pré-requis : Obsidian, Git, Node.js ≥ 18, Python ≥ 3.10, [`uv`](https://docs.astral.sh/uv/), Claude Code.

## Comment on l'alimente, comment on l'utilise

| | |
|---|---|
| **L'alimenter** | "ajoute Qdrant au brain", "documente le concept RAG" → le skill `enrichir-brain` crée/complète la fiche dans `Dev/` (technique) ou `Wiki/Concepts/` (notion), câble les liens, régénère l'index. |
| **L'utiliser depuis un projet** | Depuis un *autre* projet, lancer `claude` avec `CLAUDE-project.md` en template → le skill `planifier-projet` interroge le brain et propose un stack sourcé (2-3 candidats par brique, avec pitch). |
| **Logger un retour d'expérience** | "log un bug : timeout sur Postgres" → pas de skill dédié aujourd'hui, Claude écrit à la main dans `Dev/REX/REX - <service>.md`. |

## Ce que contient le brain

| | |
|---|---|
| **Dev/** (agent-readable) | Services, Outils, Patterns/Comparatifs, Règles, REX |
| **Wiki/** (perso) | Concepts (notions DS/ML/AI eng) — `Outils/`, `Workflows/`, `Roadmaps/` pas encore repeuplés |
| **MOC/** | hubs de navigation générés automatiquement |
| **Skills** | `enrichir-brain`, `planifier-projet` |

## Structure

```
DevBrain/
├── CLAUDE.md, CLAUDE-build.md, CLAUDE-project.md   ← contexte Claude Code (routeur + modes)
├── INSTALL.md / CONTRIBUTING.md / CHANGELOG.md      ← docs méta
│
├── Dev/                          ← galaxie agent-readable (factuel, dense)
│   ├── Services/                 (briques à déployer : frameworks, BDD, libs…)
│   ├── Outils/                   (outils utilisés : clients GUI, CLI…)
│   ├── Patterns/                 (Comparatif - <thème>.base + Pattern - <nom>.md)
│   ├── Rules/                    (règles transverses : Rule - <nom>.md)
│   └── REX/                      (retours d'expérience : REX - <Nom>.md)
│
├── Wiki/                         ← galaxie perso (humain, narratif)
│   ├── Concepts/                 (notions DS/ML/AI eng — peuplé)
│   └── Outils/ Workflows/ Roadmaps/   (vides, pas encore remigrés depuis v1)
│
├── MOC/                          ← hubs de navigation générés (Themes/Categories/Concepts)
├── Documentation/                ← gouvernance (tags, taxonomie, conventions perso)
├── Templates/                    ← gabarits Templater
├── Projects/                     ← log des projets en cours (scaffold, vide)
├── AI/                           ← espace agent (design, index généré, sessions, scripts)
└── .claude/skills/               ← enrichir-brain/, planifier-projet/
```

## Conventions clés

- **Wikilinks qualifiés par chemin** : `[[Dev/Services/Postgres|Postgres]]` (fiche), `[[Dev/REX/REX - Postgres|REX - Postgres]]` (retours d'expérience).
- **Frontmatter dense sur chaque fiche Service** (`pitch`, `categorie`, `licence_type`, `hosted`, `maturite`, `alternatives`, `status`, `tags`...) — sert d'index plat pour Claude, sans avoir à charger le contenu.
- **Trois niveaux de règle** : `must` (bloquant), `should` (par défaut, écarts signalés), `nice-to-have` (si possible).

## Contribution

Repo privé. Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour l'anatomie du repo et les règles de modification par dossier.

## Licence

MIT — voir `LICENSE`.

## Crédits

- [Andrej Karpathy — LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Steph Ango (kepano) — Obsidian Skills](https://github.com/kepano/obsidian-skills)
- Ian Sinnott, MarkusPfundstein, et la communauté Obsidian + Claude Code
