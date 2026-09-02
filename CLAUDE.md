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

1. **Build** — enrichir le brain agent-readable — quatre piliers Dev : `Dev/Services`, `Dev/Outils`, `Dev/Patterns`, `Dev/Rules`.
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

- Modifier des fiches `Dev/Services/*` existantes (y compris leur section `## Pièges`) — en mode projet, aucune écriture dans `Dev/`
- **Modifier ou créer des fichiers dans `Wiki/` sauf en mode wiki explicite ou demande explicite** (le wiki est l'espace perso de l'utilisateur — pas le tien)
- Supprimer quoi que ce soit
- Committer ou pousser sans avoir clôturé : toute écriture dans `Dev/` ou `Wiki/` se clôt par le skill `cloturer-brain`, **seul endroit où la politique git du vault est écrite** (régénération, validateur vert, vérification de divergence, puis commit et intégration en fast-forward d'office). Jamais de `--force` ni de `rebase` sans accord explicite.
- Créer des fiches dans une `categorie` non listée dans `Documentation/general/taxonomie.md`

## Mode wiki

Périmètre **strictement limité à `Wiki/`**. Tu n'as pas le droit de toucher à `Dev/`, `MOC/`, `Documentation/` en mode wiki.

État actuel : seul `Wiki/Concepts/` est peuplé (261 fiches). `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` sont des scaffolds vides — le contenu v1 correspondant n'a pas encore été remigré (voir `Documentation/perso/reservoir-v1.md`). N'invente pas de contenu pour les combler ; demande avant de commencer une migration.

Workflow type :
1. L'utilisateur dit "ajoute le concept X" / "documente la notion Y" → invoque le skill `enrichir-brain` (il gère aussi bien `Dev/` que `Wiki/Concepts/` en un seul geste, pas besoin de bascule de mode stricte pour ce cas précis).
2. Frontmatter complet obligatoire (`role: notion`, `categorie: concept/<sous-domaine>` — cf. taxonomie), gabarit `Templates/Concept-Wiki.md`.
3. Tu peux créer un sous-dossier dans `Wiki/` si une nouvelle catégorie émerge — préviens avant de le faire.

Voir `AI/design/brain-v2.md` §5.2 et §6 pour la philosophie d'ensemble du pilier wiki.

## Structure du vault (rappel)

```
Dev/                        ← briques agent-readable (factuel, dense)
├── Services/                (briques à déployer : frameworks, BDD, libs…)
├── Outils/                  (outils techniques utilisés : clients GUI, CLI…)
├── Patterns/                (Comparatif - <thème>.base + Pattern - <nom>.md)
└── Rules/                   (règles transverses : Rule - <nom>.md)

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

Templates/                   ← gabarits (Service-Dev, Concept-Wiki, Pattern, Rule)
Projects/                    ← log des projets en cours (scaffold, vide pour l'instant)

AI/                          ← TON espace agent
├── design/brain-v2.md        (spec de référence du vault)
├── index/                    (brain-index.json/.md, liens.md — générés, ne pas éditer à la main)
├── sessions/                 (résumés auto par hook Stop)
├── scripts/                  (scripts Python/uv + PowerShell d'index et d'hygiène)
└── backlog.md / backlog-enrichissement-brain.md

.claude/skills/               ← skills custom réels
├── enrichir-brain/            (capture Dev/ + Wiki/Concepts/ — mode build+wiki)
├── cloturer-brain/            (clôture : régénère, valide, commit — après TOUTE écriture)
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
| Pattern | `Dev/Patterns/Pattern - <nom>.md` |
| Comparatif | `Dev/Patterns/Comparatif - <thème>.base` |
| Règle | `Dev/Rules/Rule - <nom>.md` |
| Concept Wiki | `Wiki/Concepts/<Nom>.md` |
| **Entrée d'expérience datée** (dans `## Pièges` de la fiche concernée) | `- YYYY-MM-DD — <symptôme> : <correctif>.` — la date distingue le vécu du piège documenté |
| **Incident né entre deux briques** | s'inscrit **sous la brique qui a porté le correctif**, une seule fois, les autres briques nommées **en clair** dans la ligne ; la fiche de l'autre brique **ne le mentionne pas** (une entrée dupliquée serait une seconde chose à synchroniser) |

Ces deux dernières conventions remplacent la ligne « Entrée REX » retirée avec le pilier REX (cf. `CLAUDE-build.md`, *Corps de la fiche Service/Outil*).

**Deux axes de rangement, pas un.** Une fiche Dev porte `categorie:` (le **domaine** — de
quoi ça parle, 94 valeurs en 20 préfixes) *et* `famille:` (la **nature** — ce que c'est, 9
valeurs fermées : `paquet`, `plateforme`, `application`, `cli`, `saas`, `extension`,
`specification`, `modele`, `annuaire`). Ne jamais choisir ces deux valeurs à l'intuition :
`Documentation/general/taxonomie.md` porte un arbre de décision déterministe, questions
fermées en ordre strict. Les deux champs sont des règles dures du validateur et sont indexés.

**Un troisième champ, `role:`**, porte ce que la page **est** : `brique`, `notion`,
`pattern`, `rule` — et bientôt `hub` (lot 3) et `comparatif` (lot 5). Il a remplacé
`galaxie:` et `type:` au lot 2 de la migration v3 (cf. `AI/design/brain-v3.md` §3) : le
premier ne servait qu'à la couleur du graphe, le second ne décrivait que le dossier d'accueil.
`famille:` reste la nature **technique** d'une brique (est-ce un paquet ou une plateforme ?) ;
`role:` est la nature **éditoriale** de la page (est-ce une brique ou une notion ?). Les deux
ne se recouvrent pas.

`hosted:` et `scaling:` n'existent que si `famille:` vaut `plateforme`, `saas` ou
`application` — une bibliothèque ne s'héberge pas. `hosted:` est une **liste**
(`[self]`, `[managed]`, `[self, managed]`), jamais un scalaire. `complements:` est le
symétrique d'`alternatives:` : ce qui s'utilise **avec** la brique, quand `alternatives:`
dit ce qui s'utilise **à sa place**.

**Mise à jour d'une page existante** : jamais un patch improvisé. Un champ modifié a des consommateurs (lignes `## Alternatives` des citeurs, comparatifs `.base`, hubs MOC, index) → suivre la *Procédure — mode mise à jour* de `.claude/skills/enrichir-brain/SKILL.md`, qui donne pour chaque champ la liste des consommateurs et la commande de vérification.

**Convention wikilinks** — **nus**, jamais qualifiés par chemin :
- `[[Postgres]]` → la fiche, quel que soit son dossier.
- `[[Postgres|la base]]` → le pipe ne sert qu'à changer le **texte affiché**, jamais à
  porter un chemin.

La convention qualifiée d'avant le lot 3 visait des collisions de nom entre v1 et v2 qui
n'existent plus : le réservoir v1 est hors du vault, et la dernière collision interne —
`Dev/Services/hdbscan.md` contre `Wiki/Concepts/HDBSCAN.md`, que le système de fichiers
Windows ne distingue même pas — est tombée avec le renommage de la notion en
`Clustering hiérarchique par densité`. Obsidian résout un lien nu par nom de fichier.

La raison de tenir le nu : un lien qualifié porte un chemin, donc casse au déplacement.
La v3 déplace 682 fichiers au lot 3, puis encore aux lots 4 à 6. Avec des liens nus,
un `git mv` ne touche aucun lien. **Avant de créer une page, vérifier que son nom de
fichier est unique dans le vault** — c'est la seule contrainte que le nu impose.

## Protocole de session

### Au début de chaque session

0. **Vérifier que le `main` local suit `origin/main` — avant tout commit ou push** :
   ```bash
   git fetch origin
   git log HEAD..origin/main --oneline   # commits distants absents en local
   git merge-base HEAD origin/main       # doit renvoyer un ancêtre commun
   ```
   Si `origin/main` contient des commits absents en local, ou si `merge-base` ne trouve
   **aucun** ancêtre commun (historiques divergents ou republiés), **s'arrêter et signaler
   l'écart à l'utilisateur** avant d'écrire ou de committer quoi que ce soit — ne jamais
   travailler ni pousser sur une base potentiellement obsolète.
   > Cause de la règle : le 2026-07-29, une session a travaillé plusieurs heures sur un
   > `main` local vieux de trois semaines sans vérifier que `origin/main` avait été
   > republié entre-temps (repo republié en snapshot, historiques sans ancêtre commun,
   > 33 pages créées côté distant invisibles en local). Le travail a dû être reporté
   > après coup dans un worktree isolé — resté correct par chance, pas par méthode.

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
