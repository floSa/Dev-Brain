---
galaxie: meta
nom: CLAUDE
type: meta-doc
created: 2026-05-20
modified: 2026-09-05
tags: [meta]
---

# CLAUDE.md — DevBrain (routeur)

Tu es dans le DevBrain (v3, cf. `AI/design/brain-v3.md` ; ce que la v2 a établi et qui
reste vrai : `AI/design/brain-v2.md`). Ce vault sert **trois usages** :

1. **Build** — enrichir le brain agent-readable : les briques, les comparatifs, les patterns et les règles, rangés dans **l'arbre des 20 domaines** à la racine.
2. **Projet** — utiliser le brain depuis un projet de dev (lancer Claude *dans le dossier projet*, pas ici).
3. **Wiki** — entretenir l'espace de connaissance perso de l'utilisateur : les pages `role: notion`. C'est sa mémoire à lui, à toi de ne pas la salir.

> **Un seul arbre depuis le lot 3 de la v3.** `Dev/` n'existe plus : les 337 briques,
> les 47 comparatifs, les 5 patterns et les 5 règles sont descendus dans l'arbre.
> **`Wiki/Concepts/` et `MOC/Concepts/` existent encore** — 297 notions et leurs 10 MOC
> d'entrée — et c'est le **lot 4** qui les descendra, pas le lot 3. Tout ce qui suit
> décrit cet état-là, pas la cible finale.

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
- **wiki** → reste ici, périmètre = les pages `role: notion` (aujourd'hui toutes sous `Wiki/Concepts/`). Voir section *Mode wiki* ci-dessous.

Si l'utilisateur dit explicitement "mode <X>", applique sans demander.

## Voix et style

- Français par défaut.
- Phrases courtes. Pas de marketing-speak.
- Tu peux contredire. Préfère "ça ne marche pas parce que X" à "intéressante idée".
- Pas d'émojis sauf si l'utilisateur en utilise.

## Ce que tu peux faire ici par défaut

- Lire/explorer la structure du vault (l'arbre des domaines, `Métiers/`, `Patterns/`, `Rules/`, `Wiki/Concepts/`, `MOC/Concepts/`, `Documentation/`)
- Répondre à des questions générales sur le contenu
- Suggérer des fiches manquantes
- Auditer la cohérence (frontmatter, taxonomie — cf. `Documentation/general/taxonomie.md`)

## Ce que tu NE fais PAS sans confirmation explicite

- Modifier une page `role: brique` existante (y compris sa section `## Pièges`) — en mode projet, **aucune écriture dans l'arbre des domaines**
- **Modifier ou créer une page `role: notion` sauf en mode wiki explicite ou demande explicite** (le wiki est l'espace perso de l'utilisateur — pas le tien)
- Supprimer quoi que ce soit — et pendant la migration v3, **aucun `rm` sur une page** : un déplacement se fait par `git mv`, qui conserve l'historique
- Committer ou pousser sans avoir clôturé : toute écriture dans une page du brain se clôt par le skill `cloturer-brain`, **seul endroit où la politique git du vault est écrite** (régénération, validateur vert, vérification de divergence, puis commit et intégration en fast-forward d'office). Jamais de `--force` ni de `rebase` sans accord explicite.
- Créer des fiches dans une `categorie` non listée dans `Documentation/general/taxonomie.md`

## Mode wiki

Périmètre **strictement limité aux pages `role: notion`**. Depuis la v3, le périmètre se
lit sur le **rôle** et non sur un dossier : c'est le rôle qui survivra au lot 4, le
dossier non. Tu n'as pas le droit de toucher aux `role: brique`, `pattern`, `rule`, `hub`,
ni à `Documentation/`, en mode wiki.

État actuel : les **297** notions sont toutes sous `Wiki/Concepts/`, et le **lot 4** les
descendra dans l'arbre des domaines, avec les 10 `MOC/Concepts/` qui sont aujourd'hui leur
porte d'entrée. Jusque-là, ces deux dossiers restent en place et sont le lieu normal d'une
notion. `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` sont des scaffolds **vides** —
le contenu v1 correspondant n'a pas été remigré (voir `Documentation/perso/reservoir-v1.md`)
et, la v3 n'ayant plus de galaxie `Wiki/`, il n'est pas acquis qu'ils soient reconduits.
N'invente pas de contenu pour les combler ; demande avant de commencer une migration.

Workflow type :
1. L'utilisateur dit "ajoute le concept X" / "documente la notion Y" → invoque le skill `enrichir-brain` (il gère la brique et la notion en un seul geste, pas besoin de bascule de mode stricte pour ce cas précis).
2. Frontmatter complet obligatoire (`role: notion`, `categorie: concept/<sous-domaine>` — cf. taxonomie), gabarit `Templates/Concept-Wiki.md`.
3. **Ne crée pas de sous-dossier dans `Wiki/`** : le rangement d'une notion se dérivera de sa `categorie:` au lot 4, comme pour une brique. Une nouvelle famille se pose dans `Documentation/general/taxonomie.md`, pas dans l'arborescence.

Voir `AI/design/brain-v3.md` §2, §3 et §7 pour l'axe rôle / domaine, et `AI/design/brain-v2.md` §5.2 et §6 pour la philosophie d'ensemble du pilier wiki.

## Structure du vault (rappel)

**Un dossier par domaine, à la racine.** Le domaine se dérive de `categorie:` — personne
ne choisit un dossier (`AI/scripts/arbo.py` porte la dérivation, `check_arbo.py` la
vérifie). Un sous-dossier apparaît dès qu'un sous-domaine atteint 5 pages, sauf s'il ne
laisserait aucune page au niveau du domaine. Tout dossier porte une page à son nom,
`role: hub`, dont la zone `<!-- AUTO -->` est générée depuis le contenu du dossier.

```
<20 dossiers de domaine>/    ← l'arbre : Bases de données/, Machine Learning/,
│                              LLM & IA générative/, Data & pipelines/, Stockage/…
├── <Domaine>.md              (role: hub — l'aiguillage du dossier)
├── <Sous-domaine>/           (promu à 5 pages : Vectoriel/, Apprentissage profond/…)
│   ├── <Sous-domaine>.md     (role: hub)
│   └── <Brique>.md           (role: brique) + Comparatif - <thème>.base
└── <Brique>.md               (role: brique) + Comparatif - <thème>.base

Métiers/                     ← 5 hubs transverses, générés depuis `domaines:`
                               (Data Science, Data Engineering, MLOps, ML Engineering,
                               AI Engineering) — seul axe qui traverse l'arbre technique

Patterns/                    ← Patterns.md (hub) + Pattern - <nom>.md   (role: pattern)
Rules/                       ← Rules.md    (hub) + Rule - <nom>.md      (role: rule)
                               groupés par `role:` — aucune `categorie:` ne les range

Wiki/Concepts/               ← 297 notions (role: notion) — EN ATTENTE DU LOT 4
MOC/Concepts/                ← 10 MOC générées, leur seule porte d'entrée (R7)
                               les deux meurent ensemble au lot 4, PAS avant
Wiki/Outils|Workflows|Roadmaps/  ← scaffolds vides, non remigrés (cf. reservoir-v1.md)

Documentation/               ← gouvernance (tags, taxonomie, thèmes, conventions perso)
├── general/                  (réutilisable : tags.md, taxonomie.md, themes.md, questions-projet.md)
└── perso/                    (conventions.md, archetypes.md, machines.md, obsidian-graph.md, reservoir-v1.md)

Templates/                   ← gabarits (Service-Dev, Outil-Dev, Concept-Wiki, Pattern, Rule)
Projects/                    ← log des projets en cours (scaffold, vide pour l'instant)
Home.md                      ← porte d'entrée du vault : l'arbre, les métiers, le reste

AI/                          ← TON espace agent
├── design/brain-v3.md        (spec de référence ; brain-v2.md pour ce qui reste vrai)
├── design/v3-arborescence.md (l'arbre page par page, annoté au fil des lots)
├── migration/                (un fichier par lot, avec ses Remontées)
├── index/                    (brain-index.json/.md, liens.md — générés, ne pas éditer à la main)
├── sessions/                 (résumés auto par hook Stop)
├── scripts/                  (scripts Python/uv + PowerShell d'index et d'hygiène)
└── backlog.md / backlog-enrichissement-brain.md

.claude/skills/               ← skills custom réels
├── enrichir-brain/            (capture brique + notion — mode build+wiki)
├── cloturer-brain/            (clôture : régénère, valide, commit — après TOUTE écriture)
└── planifier-projet/          (cadrage projet — mode projet)
```

**Frontières fermes** :
- **L'arbre des domaines**, `Patterns/`, `Rules/` → modifiables seulement en mode build (selon `CLAUDE-build.md`).
- **Les pages `role: notion`** (aujourd'hui `Wiki/Concepts/`) → modifiables seulement en mode wiki ou sur demande explicite.
- **Les zones `<!-- AUTO -->` des hubs**, `Métiers/`, `MOC/`, `AI/index/` → générés par script, ne pas éditer à la main (relancer `AI/scripts/build_index.py` puis `build_mocs.py` / `build_links.py`). Le **corps** d'un hub, hors zone AUTO, s'écrit à la main.
- `AI/` (hors index/) → ton espace, tu peux y écrire librement.
- `Documentation/` → modifiable en mode build ou wiki selon le sous-dossier concerné, toujours avec prudence (c'est la gouvernance du brain).
- `Inbox.md` → modifiable en tout mode (écriture par l'utilisateur seulement)

## Conventions de nommage

Le chemin n'est plus à choisir : il se **dérive** de `categorie:`, et `<Dossier>` ci-dessous
désigne le dossier que la dérivation donne (domaine, ou sous-domaine s'il est promu).

| Type | Format |
|------|--------|
| Brique (`role: brique`) | `<Dossier>/<Nom>.md` |
| Hub (`role: hub`) | `<Dossier>/<Dossier>.md` — la page porte le nom de son dossier |
| Comparatif | `<Dossier>/Comparatif - <thème>.base` — dans le dossier de ses membres |
| Pattern (`role: pattern`) | `Patterns/Pattern - <nom>.md` |
| Règle (`role: rule`) | `Rules/Rule - <nom>.md` |
| Notion (`role: notion`) | `Wiki/Concepts/<Nom>.md` — **jusqu'au lot 4**, qui la descendra dans `<Dossier>/` |
| **Entrée d'expérience datée** (dans `## Pièges` de la fiche concernée) | `- YYYY-MM-DD — <symptôme> : <correctif>.` — la date distingue le vécu du piège documenté |
| **Incident né entre deux briques** | s'inscrit **sous la brique qui a porté le correctif**, une seule fois, les autres briques nommées **en clair** dans la ligne ; la fiche de l'autre brique **ne le mentionne pas** (une entrée dupliquée serait une seconde chose à synchroniser) |

Ces deux dernières conventions remplacent la ligne « Entrée REX » retirée avec le pilier REX (cf. `CLAUDE-build.md`, *Corps de la fiche Service/Outil*).

**Deux axes de rangement, pas un.** Une brique porte `categorie:` (le **domaine** — de
quoi ça parle, 94 valeurs en 20 préfixes) *et* `famille:` (la **nature** — ce que c'est, 9
valeurs fermées : `paquet`, `plateforme`, `application`, `cli`, `saas`, `extension`,
`specification`, `modele`, `annuaire`). Ne jamais choisir ces deux valeurs à l'intuition :
`Documentation/general/taxonomie.md` porte un arbre de décision déterministe, questions
fermées en ordre strict. Les deux champs sont des règles dures du validateur et sont indexés.

**Un troisième champ, `role:`**, porte ce que la page **est** : `brique`, `notion`,
`pattern`, `rule`, `hub` — et bientôt `comparatif` (lot 5). Il a remplacé
`galaxie:` et `type:` au lot 2 de la migration v3 (cf. `AI/design/brain-v3.md` §3) : le
premier ne servait qu'à la couleur du graphe, le second ne décrivait que le dossier d'accueil.
`famille:` reste la nature **technique** d'une brique (est-ce un paquet ou une plateforme ?) ;
`role:` est la nature **éditoriale** de la page (est-ce une brique ou une notion ?). Les deux
ne se recouvrent pas.

Un `role: hub` ne porte **pas** de `categorie:` : un hub ne se range pas, il *est* le
rangement — son domaine est son chemin. `role: pattern` et `role: rule` n'en portent pas
non plus, et c'est délibéré : un pattern enjambe plusieurs domaines par construction, une
règle est transverse par définition. C'est `role:` qui les groupe, dans `Patterns/` et
`Rules/`.

`hosted:` et `scaling:` n'existent que si `famille:` vaut `plateforme`, `saas` ou
`application` — une bibliothèque ne s'héberge pas. `hosted:` est une **liste**
(`[self]`, `[managed]`, `[self, managed]`), jamais un scalaire. `complements:` est le
symétrique d'`alternatives:` : ce qui s'utilise **avec** la brique, quand `alternatives:`
dit ce qui s'utilise **à sa place**.

**Le voisinage d'une page est `ls` de son dossier.** C'est ce que l'arbre achète
(`brain-v3.md` §10) : insérer une brique met à jour le hub du dossier et ses hubs parents
(générés), puis le comparatif, la notion et les briques pairs **du dossier** — plus rien à
deviner à partir des tags.

**Mise à jour d'une page existante** : jamais un patch improvisé. Un champ modifié a des consommateurs (lignes `## Alternatives` des citeurs, comparatifs `.base`, zones AUTO des hubs, index) → suivre la *Procédure — mode mise à jour* de `.claude/skills/enrichir-brain/SKILL.md`, qui donne pour chaque champ la liste des consommateurs et la commande de vérification.

**Convention wikilinks** — **nus**, jamais qualifiés par chemin :
- `[[Postgres]]` → la fiche, quel que soit son dossier.
- `[[Postgres|la base]]` → le pipe ne sert qu'à changer le **texte affiché**, jamais à
  porter un chemin.

La convention qualifiée d'avant le lot 3 visait des collisions de nom entre v1 et v2 qui
n'existent plus : le réservoir v1 est hors du vault, et la dernière collision interne —
la brique `hdbscan` contre la notion `HDBSCAN`, que le système de fichiers Windows ne
distingue même pas — est tombée avec le renommage de la notion en
`Clustering hiérarchique par densité`. Obsidian résout un lien nu par nom de fichier.

La raison de tenir le nu : un lien qualifié porte un chemin, donc casse au déplacement.
Le lot 3 a déplacé 682 fichiers sans toucher un seul lien ; les lots 4 à 6 en déplaceront
encore. **Avant de créer une page, vérifier que son nom de fichier est unique dans le
vault, à la casse près** — c'est la seule contrainte que le nu impose, et elle vaut aussi
pour le nom de chaque hub à créer.

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

- **`enrichir-brain`** — capture une techno/concept : crée la page demandée + ses pages connexes (alternatives, comparatif), câble les liens bidirectionnels, régénère l'index. Couvre la brique **et** la notion. Triggers : "ajoute X au brain", "documente Y", ou en fin de conversation "mets à jour DevBrain" (mode balayage). *Sa procédure parle encore en chemins `Dev/…` : c'est le **lot 7** qui la réécrit sur l'arbre. En attendant, lire ses commandes comme des exemples et viser le dossier réel de la page.*
- **`cloturer-brain`** — clôt TOUTE écriture dans une page du brain : régénère `build_index` / `build_mocs` / `build_links`, passe `check_brain.py` **et** `check_arbo.py` au vert, vérifie la divergence avec `origin/main`, puis commite et intègre. **Seul endroit où la politique git du vault est écrite.**
- **`planifier-projet`** — au démarrage d'un projet, identifie l'archétype (cf. `Documentation/perso/archetypes.md`), interroge `AI/index/brain-index.json` et produit un cahier des charges sourcé. N'écrit rien dans le brain.

Skills officiels Obsidian (`kepano/obsidian-skills`) — apprend la syntaxe Obsidian (wikilinks, callouts, frontmatter, Bases, Canvas).

## En cas de doute

Demande. N'invente pas. Ne devine pas une catégorie, un score, une licence — demande.
