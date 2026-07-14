---
galaxie: meta
nom: CLAUDE
type: meta-doc
created: 2026-05-20
modified: 2026-07-07
tags: [meta]
---

# CLAUDE.md — DevBrain (routeur)

Tu es dans le DevBrain (v2, cf. `AI/design/brain-v2.md`). Ce vault sert **trois usages** :

1. **Build** — enrichir le brain agent-readable (`Dev/Services`, `Dev/Patterns`, `Dev/Outils`, `Dev/Rules`, `Dev/REX`).
2. **Projet** — utiliser le brain depuis un projet de dev (lancer Claude *dans le dossier projet*, pas ici).
3. **Wiki** — entretenir l'espace de connaissance perso de l'utilisateur (`Wiki/Concepts`, à terme `Outils`/`Workflows`/`Roadmaps`). C'est sa mémoire à lui, à toi de ne pas la salir.

## Identité utilisateur

Je suis floSa, ingénieur Data / ML / AI. Spécialité **on-prem** (industriels, ESN) — cf. `Documentation/perso/conventions.md`.

**Domaines de prédilection :**
- Data science (exploration, modélisation, viz)
- Data engineering (pipelines, ELT, qualité de la donnée)
- MLops (déploiement modèle, monitoring, infra ML)
- ML engineering (entraînement scalable, optimisation)
- AI engineering (apps LLM, RAG, agents, MCP)

**Outils du quotidien :**
- Python (uv, FastAPI, pandas, polars, scikit-learn, PyTorch)
- Docker pour le packaging
- GitHub Actions pour la CI
- Obsidian + Claude Code + DevBrain pour la connaissance

**Posture :**
- Plutôt solo, parfois en petite équipe
- Préfère les outils opinionnated et productifs (uv plutôt que pip+venv, ruff plutôt que flake8+isort+black, etc.)
- Cherche la clarté avant la cleverness

## Annonce ton mode au démarrage

Demande : "Mode build (enrichir le brain), mode projet (travailler sur un projet) ou mode wiki (gérer mes concepts / pages perso) ?"

Selon la réponse :
- **build** → lis `@CLAUDE-build.md` et applique son contexte
- **projet** → indique-lui que pour les projets, il devrait lancer `claude` *dans le dossier du projet* (pas dans le vault), où un `CLAUDE.md` issu de `CLAUDE-project.md` est déjà installé.
- **wiki** → reste ici, périmètre = `Wiki/` uniquement. Voir section *Mode wiki* ci-dessous.

Si l'utilisateur dit explicitement "mode <X>", applique sans demander.

## Voix et style

- Français par défaut.
- Phrases courtes. Pas de marketing-speak.
- Tu peux contredire. Préfère "ça ne marche pas parce que X" à "intéressante idée".
- Pas d'émojis sauf si l'utilisateur en utilise.

## Ce que tu peux faire ici par défaut

- Lire/explorer la structure du vault (`Dev/`, `Wiki/`, `MOC/`, `Documentation/`)
- Répondre à des questions générales sur le contenu
- Suggérer des fiches manquantes
- Auditer la cohérence (frontmatter, taxonomie — cf. `Documentation/general/taxonomie.md`)

## Ce que tu NE fais PAS sans confirmation explicite

- Modifier des fiches `Dev/Services/*` existantes (en mode projet : tu peux ajouter un REX dans `Dev/REX/REX - <Service>.md` mais pas modifier la fiche service elle-même)
- **Modifier ou créer des fichiers dans `Wiki/` sauf en mode wiki explicite ou demande explicite** (le wiki est l'espace perso de l'utilisateur — pas le tien)
- Supprimer quoi que ce soit
- Commit + push automatiques après validation (sans demander) ; jamais de --force/rebase sans accord
- Créer des fiches dans une `categorie` non listée dans `Documentation/general/taxonomie.md`

## Mode wiki

Périmètre **strictement limité à `Wiki/`**. Tu n'as pas le droit de toucher à `Dev/`, `MOC/`, `Documentation/` en mode wiki.

État actuel : seul `Wiki/Concepts/` est peuplé (261 fiches). `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` sont des scaffolds vides — le contenu v1 correspondant n'a pas encore été remigré (voir `Documentation/perso/reservoir-v1.md`). N'invente pas de contenu pour les combler ; demande avant de commencer une migration.

Workflow type :
1. L'utilisateur dit "ajoute le concept X" / "documente la notion Y" → invoque le skill `enrichir-brain` (il gère aussi bien `Dev/` que `Wiki/Concepts/` en un seul geste, pas besoin de bascule de mode stricte pour ce cas précis).
2. Frontmatter complet obligatoire (`galaxie: wiki`, `type: concept`, `categorie: concept/<sous-domaine>` — cf. taxonomie), gabarit `Templates/Concept-Wiki.md`.
3. Tu peux créer un sous-dossier dans `Wiki/` si une nouvelle catégorie émerge — préviens avant de le faire.

Voir `AI/design/brain-v2.md` §5.2 et §6 pour la philosophie d'ensemble du pilier wiki.

## Structure du vault (rappel)

```
Dev/                        ← galaxie agent-readable (factuel, dense)
├── Services/                (briques à déployer : frameworks, BDD, libs…)
├── Outils/                  (outils techniques utilisés : clients GUI, CLI…)
├── Patterns/                (Comparatif - <thème>.base + Pattern - <nom>.md)
├── Rules/                   (règles transverses : Rule - <nom>.md)
└── REX/                     (retours d'expérience : REX - <Nom>.md, un fichier par service)

Wiki/                       ← ESPACE PERSO DE L'UTILISATEUR (notions, skills perso)
├── Concepts/                (notions à comprendre — seul dossier peuplé aujourd'hui)
├── Outils/                  (vide — catalogue skills/extensions perso, pas encore remigré)
├── Workflows/                (vide — procédures pas-à-pas, pas encore remigré)
└── Roadmaps/                 (vide — cartes de compétences, pas encore remigré)

MOC/                        ← hubs de navigation générés (build_mocs.py)
├── Themes/                  (5 domaines : data-sci, data-eng, mlops, ml-eng, ai-eng)
├── Categories/               (familles Dev)
└── Concepts/                 (sous-domaines Wiki)

Documentation/               ← gouvernance (tags, taxonomie, thèmes, conventions perso)
├── general/                  (réutilisable : tags.md, taxonomie.md, themes.md, questions-projet.md)
└── perso/                    (conventions.md, archetypes.md, machines.md, obsidian-graph.md, reservoir-v1.md)

Templates/                   ← gabarits (Service-Dev, Concept-Wiki, Pattern, Rule, REX, REX-entry)
Projects/                    ← log des projets en cours (scaffold, vide pour l'instant)

AI/                          ← TON espace agent
├── design/brain-v2.md        (spec de référence du vault)
├── index/                    (brain-index.json/.md, liens.md — générés, ne pas éditer à la main)
├── sessions/                 (résumés auto par hook Stop)
├── scripts/                  (scripts Python/uv + PowerShell d'index et d'hygiène)
└── backlog.md / backlog-enrichissement-brain.md

.claude/skills/               ← skills custom réels
├── enrichir-brain/            (capture Dev/ + Wiki/Concepts/ — mode build+wiki)
└── planifier-projet/          (cadrage projet — mode projet)
```

**Frontières fermes** :
- `Dev/` → modifiable seulement en mode build (selon `CLAUDE-build.md`).
- `Wiki/` → modifiable seulement en mode wiki ou sur demande explicite.
- `MOC/`, `AI/index/` → générés par script, ne pas éditer à la main (relancer `AI/scripts/build_mocs.py` / `build_index.py`).
- `AI/` (hors index/) → ton espace, tu peux y écrire librement.
- `Documentation/` → modifiable en mode build ou wiki selon le sous-dossier concerné, toujours avec prudence (c'est la gouvernance du brain).
- `Inbox.md` → modifiable en tout mode (écriture par l'utilisateur seulement)

## Conventions de nommage

| Type | Format |
|------|--------|
| Service Dev | `Dev/Services/<Nom>.md` |
| Outil Dev | `Dev/Outils/<Nom>.md` |
| **REX par service** | `Dev/REX/REX - <Nom>.md` (un fichier par service) |
| Pattern | `Dev/Patterns/Pattern - <nom>.md` |
| Comparatif | `Dev/Patterns/Comparatif - <thème>.base` |
| Règle | `Dev/Rules/Rule - <nom>.md` |
| Concept Wiki | `Wiki/Concepts/<Nom>.md` |
| Entrée REX (section dans `REX - X.md`) | `## YYYY-MM-DD — <symptôme>` |

**Convention wikilinks** (qualifiés par chemin pour éviter les collisions v1/v2) :
- `[[Dev/Services/Postgres|Postgres]]` → fiche Service
- `[[Dev/REX/REX - Postgres|REX - Postgres]]` → note de bugs
- Pas d'ambiguïté possible.

## Protocole de session

### Au début de chaque session
1. Liste les 3 derniers fichiers de `AI/sessions/` :
   ```bash
   ls -t AI/sessions/ | head -3
   ```
   Lis-les pour le contexte récent.

2. Si l'un mentionne une tâche ouverte ("À reprendre"), demande si on la reprend.

### À la fin de chaque session
Si le hook Stop est configuré (cf. `AI/scripts/session_to_devbrain.py`), un résumé sera écrit automatiquement dans `AI/sessions/`. Sinon, écris-le toi-même quand l'utilisateur dit "fin de session".

## Skills disponibles

Skills custom dans `.claude/skills/` :

- **`enrichir-brain`** — capture une techno/concept dans `Dev/` **et** `Wiki/Concepts/` : crée la page demandée + ses pages connexes (alternatives, comparatif), câble les liens bidirectionnels, régénère l'index. Triggers : "ajoute X au brain", "documente Y", ou en fin de conversation "mets à jour DevBrain" (mode balayage).
- **`planifier-projet`** — au démarrage d'un projet, identifie l'archétype (cf. `Documentation/perso/archetypes.md`), interroge `AI/index/brain-index.json` et produit un cahier des charges sourcé. N'écrit rien dans le brain.

Skills officiels Obsidian (`kepano/obsidian-skills`) — apprend la syntaxe Obsidian (wikilinks, callouts, frontmatter, Bases, Canvas).

## En cas de doute

Demande. N'invente pas. Ne devine pas une catégorie, un score, une licence — demande.
