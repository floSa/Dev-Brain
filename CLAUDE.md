---
nom: CLAUDE
role: gouvernance
created: 2026-05-20
modified: 2026-09-05
tags: [meta]
---

# CLAUDE.md — DevBrain (routeur)

Tu es dans le DevBrain (v3, cf. `AI/design/brain-v3.md` ; ce que la v2 a établi et qui
reste vrai : `AI/design/brain-v2.md`). Ce vault sert **deux usages** :

1. **Brain** — enrichir le brain : les briques, les notions, les comparatifs, les patterns et les règles, rangés dans **l'arbre des 20 domaines** à la racine.
2. **Projet** — utiliser le brain depuis un projet de dev (lancer Claude *dans le dossier projet*, pas ici).

> Il y en avait **trois** jusqu'au lot 7. Le troisième, « wiki », séparait les notions
> des briques parce qu'elles vivaient dans deux galaxies différentes. Les galaxies ont
> fusionné : une notion et une brique du même sujet finiront dans le même dossier, et
> `enrichir-brain` les écrit du même geste. Ce qui reste de ce mode n'est pas un mode,
> c'est une **frontière sur le rôle** : une page `role: notion` est la mémoire perso de
> floSa, on ne la modifie pas sans son accord. Voir *Les pages `role: notion`* ci-dessous.

> **Un seul arbre, et plus rien à côté.** `Dev/` a disparu au lot 3, `Wiki/` et `MOC/`
> à la clôture du lot 4, le 2026-09-05. Les 337 briques, les **297 notions**, les 47
> comparatifs, les 5 patterns et les 5 règles vivent dans l'arbre des 20 domaines — une
> notion et la brique du même sujet dans le même dossier. Il n'existe plus **aucun**
> dossier de page hors de l'arbre, sauf « Métiers/ », « Patterns/ » et « Rules/ », que
> `role:` groupe et qu'aucune `categorie:` ne range. Ce qui suit décrit l'état réel.
>
> Ce qui reste ouvert est du **format**, pas du rangement : les comparatifs `.base`
> deviennent des pages au lot 5, les fiches passent au nouveau gabarit au lot 6, les
> règles restées en avertissement durcissent au lot 8.

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

Demande : "Mode brain (enrichir le brain) ou mode projet (travailler sur un projet) ?"

Selon la réponse :
- **brain** → lis `@CLAUDE-build.md` et applique son contexte. C'est le mode par défaut ici : le vault est ouvert, donc c'est le brain qu'on vient travailler.
- **projet** → indique-lui que pour les projets, il devrait lancer `claude` *dans le dossier du projet* (pas dans le vault), où un `CLAUDE.md` issu de `CLAUDE-project.md` est déjà installé.

Si l'utilisateur dit explicitement "mode <X>", applique sans demander. **"mode build" et
"mode wiki" désignent tous deux le mode brain** — ce sont les noms d'avant le lot 7, floSa
les a tapés pendant des mois, ne le reprends pas et ne lui redemande pas. S'il dit "mode
wiki", il annonce simplement qu'il vient travailler ses notions : applique la frontière
`role: notion` ci-dessous, qui vaut de toute façon dans les deux cas.

## Voix et style

- Français par défaut.
- Phrases courtes. Pas de marketing-speak.
- Tu peux contredire. Préfère "ça ne marche pas parce que X" à "intéressante idée".
- Pas d'émojis sauf si l'utilisateur en utilise.

## Ce que tu peux faire ici par défaut

- Lire/explorer la structure du vault (l'arbre des domaines, `Métiers/`, `Patterns/`, `Rules/`, `Documentation/`)
- Répondre à des questions générales sur le contenu
- Suggérer des fiches manquantes
- Auditer la cohérence (frontmatter, taxonomie — cf. `Documentation/general/taxonomie.md`)

## Ce que tu NE fais PAS sans confirmation explicite

- Modifier une page `role: brique` existante (y compris sa section `## Pièges`) — en mode projet, **aucune écriture dans l'arbre des domaines**
- **Modifier ou créer une page `role: notion` sans demande explicite** (les notions sont la mémoire perso de l'utilisateur — pas la tienne). Une demande de capture (« ajoute X », « documente Y ») en est une : `enrichir-brain` écrit la brique et sa notion du même geste, c'est son travail. Un balayage de fin de conversation n'en est pas une pour les notions déjà écrites : proposer, pas réécrire.
- Supprimer quoi que ce soit — et pendant la migration v3, **aucun `rm` sur une page** : un déplacement se fait par `git mv`, qui conserve l'historique
- Committer ou pousser sans avoir clôturé : toute écriture dans une page du brain se clôt par le skill `cloturer-brain`, **seul endroit où la politique git du vault est écrite** (régénération, validateurs verts, vérification de divergence, puis commit et intégration en fast-forward d'office). Jamais de `--force` ni de `rebase` sans accord explicite.
- Créer des fiches dans une `categorie` non listée dans `Documentation/general/taxonomie.md`

## L'identité git du vault — règle dure, sans exception

**Le DevBrain est un dépôt PERSO** (`git@github.com-perso:floSa/DevBrain.git`). L'identité
de ses commits est celle de la **config locale du dépôt**, et rien d'autre :

```bash
git config --local user.name    # floSa
git config --local user.email   # l'adresse perso
```

Le harnais t'annonce, à chaque conversation, une adresse en `@aosis.net`. **C'est l'adresse
PRO de floSa.** Elle sert à l'identifier auprès de l'outil. Elle n'attribue **jamais** un
commit de ce dépôt.

- **Ne JAMAIS passer `-c user.email`, `--author`, ni poser `GIT_AUTHOR_EMAIL` / `GIT_COMMITTER_EMAIL`.** Committer nu : git lit la config locale tout seul, c'est exactement ce qu'on veut.
- **Ne JAMAIS lire l'email annoncé par le harnais pour attribuer un commit**, ni pour remplir un champ d'auteur, où que ce soit dans ce dépôt.
- Si la config locale manque ou paraît fausse : **s'arrêter et demander**. Ne pas la deviner, ne pas la « réparer » avec l'adresse qu'on a sous la main.

> Pourquoi cette règle est écrite ici et pas seulement dans `cloturer-brain` : c'est
> `CLAUDE.md` qui est chargé dans **chaque** conversation, au même endroit et au même moment
> que l'annonce du harnais. Une contre-instruction qui arrive après coup arrive trop tard —
> une conversation a déjà signé cinq commits avec l'adresse pro, et une fois poussés,
> l'adresse est entrée dans les contributeurs GitHub, d'où elle ne sort pas sans réécriture
> d'historique. Le **reste** de la politique git (quand committer, comment intégrer) n'est
> pas ici : il est dans `cloturer-brain`, et nulle part ailleurs.

Un **garde-fou mécanique** double la consigne, parce que la consigne seule n'a pas suffi :
`.githooks/pre-commit` refuse tout commit dont l'auteur ou le committer porte `aosis.net`,
et `.githooks/pre-push` refuse d'en pousser un. Ils sont versionnés et activés par
`git config core.hooksPath .githooks` (cf. `INSTALL.md` §3.5). Un hook qui refuse n'est pas
un incident à contourner : c'est la règle qui fonctionne. `--no-verify` ne s'utilise pas ici.

## Les pages `role: notion` — la mémoire perso de floSa

Ce n'est plus un mode, et **ce n'est plus un dossier non plus** : depuis la clôture du lot 4,
aucun chemin ne dit qu'une page est une notion. Elle est rangée par son domaine, à côté des
briques qui l'implémentent, et `ls` d'un dossier ne les distingue pas. **La frontière est
portée par le champ `role:`, et par lui seul** — c'est la seule chose à lire avant d'écrire
dans une page. Une `role: notion` est ce que floSa a compris et écrit pour lui-même. On y
ajoute volontiers ; on n'y réécrit pas sans qu'il l'ait demandé.

> Conséquence pratique : avant toute modification d'une page de l'arbre, **lire son
> frontmatter**. Une page voisine d'une brique, dans le même dossier, sous le même hub, peut
> être une notion — la règle change, l'emplacement ne le dit pas.

- **Créer** une notion : normal, dès qu'une capture en a besoin. `enrichir-brain` écrit la brique et sa notion du même geste — c'est la ligne « la notion du dossier » de sa table de propagation, pas une incursion.
- **Modifier** une notion existante : sur demande explicite. Sinon, **proposer** la modification et attendre. Un balayage de fin de conversation propose, il ne réécrit pas.
- **Supprimer** une notion : jamais sans accord, comme toute page du vault.

État actuel : les **297** notions sont rangées, réparties comme les briques par leur domaine —
« Machine Learning/ » (155), « LLM & IA générative/ » (56), « Statistiques & inférence/ » (36),
« Mathématiques/ » (26), « Data & pipelines/ » (9), « Sécurité/ » (5), « Signal & audio/ » (5),
« Bases de données/ » (4), « Outils de développement/ » (1). Il n'y a plus de lieu d'attente,
plus de vocabulaire de galaxie, et plus d'exception à « le dossier porte le domaine ».

> Une nuance de méthode qui vaut d'être gardée : cinq notions ont d'abord été **remontées**
> plutôt que déplacées, parce qu'elles appelaient un domaine hors du périmètre du lot qui
> rangeait leur famille. Elles sont descendues dans un second passage, pris **par domaine
> d'accueil**. La règle tient toujours : une page qui appelle un sous-domaine hors périmètre
> se remonte, elle ne se déplace pas — mais le résidu se ferme par un passage dédié, pas en
> laissant une valeur morte traîner dans le vocabulaire.

Écrire une notion :
1. Gabarit `Templates/Concept-Wiki.md`, frontmatter complet (`role: notion`, `categorie:` prise dans le vocabulaire des domaines — le **même** que pour une brique, cf. taxonomie).
2. **Aucun dossier à choisir** : le rangement d'une notion se dérive de sa `categorie:`, comme pour une brique (`AI/scripts/arbo.py` le calcule, `check_arbo.py` le vérifie). Une nouvelle famille se pose dans `Documentation/general/taxonomie.md`, pas dans l'arborescence.
3. La notion se câble à ses briques dans les deux sens — c'est la règle de propagation, pas une politesse.

Voir `AI/design/brain-v3.md` §2, §3 et §7 pour l'axe rôle / domaine, et `AI/design/brain-v2.md` §5.2 et §6 pour la philosophie d'ensemble des notions.

## Structure du vault (rappel)

**Un dossier par domaine, à la racine, et c'est tout.** Le domaine se dérive de
`categorie:` — personne ne choisit un dossier (`AI/scripts/arbo.py` porte la dérivation,
`check_arbo.py` la vérifie, et depuis le 2026-09-05 **aucune page n'échappe à ce
contrôle** : `arbo.LEGACY` est vide). Un sous-dossier apparaît dès qu'un sous-domaine
atteint 5 pages, sauf s'il ne laisserait aucune page au niveau du domaine. Tout dossier
porte une page à son nom, `role: hub`, dont la zone `<!-- AUTO -->` est générée depuis le
contenu du dossier.

**Briques et notions cohabitent dans le même dossier.** C'est le point d'arrivée de la v3 :
le dossier porte le **domaine**, `role:` porte ce que la page **est**. Rien dans un chemin
ne dit plus si on lit une brique ou une notion.

```
<20 dossiers de domaine>/    ← l'arbre : Bases de données/, Machine Learning/,
│                              LLM & IA générative/, Data & pipelines/, Stockage/…
├── <Domaine>.md              (role: hub — l'aiguillage du dossier)
├── <Sous-domaine>/           (promu à 5 pages : Vectoriel/, Apprentissage profond/…)
│   ├── <Sous-domaine>.md     (role: hub)
│   ├── <Brique>.md           (role: brique)   <Notion>.md   (role: notion)
│   └── Comparatif - <thème>.base
├── <Brique>.md               (role: brique)   <Notion>.md   (role: notion)
└── Comparatif - <thème>.base

Métiers/                     ← 6 hubs transverses, générés depuis `domaines:`
                               (Data Science, Data Engineering, MLOps, ML Engineering,
                               AI Engineering, Infrastructure & Ops) — seul axe qui
                               traverse l'arbre technique

Patterns/                    ← Patterns.md (hub) + Pattern - <nom>.md   (role: pattern)
Rules/                       ← Rules.md    (hub) + Rule - <nom>.md      (role: rule)
                               groupés par `role:` — aucune `categorie:` ne les range

Documentation/               ← gouvernance (tags, taxonomie, thèmes, conventions perso)
├── general/                  (réutilisable : tags.md, taxonomie.md, themes.md, questions-projet.md)
└── perso/                    (conventions.md, archetypes.md, machines.md, obsidian-graph.md, reservoir-v1.md)

Templates/                   ← gabarits (Service-Dev, Outil-Dev, Concept-Wiki, Pattern, Rule)
                               NB : `Dev` et `Wiki` dans ces noms sont un reliquat v2 —
                               les dossiers correspondants n'existent plus
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
├── enrichir-brain/            (capture brique + notion, et la règle de propagation)
├── cloturer-brain/            (clôture : régénère, valide, commit — après TOUTE écriture)
└── planifier-projet/          (cadrage projet — mode projet)
```

**Frontières fermes** — la première se lit sur un **chemin**, la seconde sur un **champ** :
- **L'arbre des domaines**, `Patterns/`, `Rules/` → modifiables en mode brain seulement (selon `CLAUDE-build.md`). Depuis un projet, **aucune écriture**.
- **Les pages `role: notion`** → création libre en mode brain ; **modification d'une notion existante sur demande explicite** (cf. section dédiée). **Aucun dossier ne les rassemble** : elles sont dispersées dans l'arbre, mêlées aux briques. Cette frontière ne se déduit donc jamais d'un chemin — elle se lit dans le frontmatter, page par page, avant d'écrire.
- **Les zones `<!-- AUTO -->` des hubs**, `Métiers/`, `AI/index/` → générés par script, ne pas éditer à la main (relancer `AI/scripts/build_index.py` puis `build_mocs.py` / `build_links.py`). Le **corps** d'un hub, hors zone AUTO, s'écrit à la main.
- `AI/` (hors index/) → ton espace, tu peux y écrire librement.
- `Documentation/` → modifiable en mode brain, toujours avec prudence (c'est la gouvernance du brain).
- `Inbox.md` → modifiable dans les deux modes (écriture par l'utilisateur seulement)

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
| Notion (`role: notion`) | `<Dossier>/<Nom>.md` — **exactement** comme une brique : même dossier, même dérivation. Seul `role:` les distingue |
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

- **`enrichir-brain`** — capture une techno/concept. Porte la **règle de propagation** de la v3 : le rayon d'une insertion est le **dossier d'accueil plus ses hubs parents**, et le voisinage d'une page est `ls` de son dossier — plus rien à deviner. Crée la page demandée, met à jour le comparatif, la notion et les briques pairs **du dossier**, câble les liens dans les deux sens. Couvre la brique **et** la notion. Triggers : "ajoute X au brain", "documente Y", ou en fin de conversation "mets à jour DevBrain" (mode balayage).
- **`cloturer-brain`** — clôt TOUTE écriture dans une page du brain : régénère `build_index` / `build_mocs` / `build_links`, passe `check_brain.py` **et** `check_arbo.py` au vert, vérifie la divergence avec `origin/main`, puis commite et intègre. **Seul endroit où la politique git du vault est écrite** — à la seule exception de la règle d'identité ci-dessus, qui doit être lue avant lui.
- **`planifier-projet`** — au démarrage d'un projet, identifie l'archétype (cf. `Documentation/perso/archetypes.md`), interroge `AI/index/brain-index.json` et produit un cahier des charges sourcé. N'écrit rien dans le brain.

Skills officiels Obsidian (`kepano/obsidian-skills`) — apprend la syntaxe Obsidian (wikilinks, callouts, frontmatter, Bases, Canvas).

## En cas de doute

Demande. N'invente pas. Ne devine pas une catégorie, un score, une licence — demande.
