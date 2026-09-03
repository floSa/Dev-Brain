---
nom: CONTRIBUTING
role: gouvernance
created: 2026-05-20
modified: 2026-09-05
tags: [meta]
---

# Contribuer à DevBrain

> Ce document s'adresse à **toi dans 6 mois** ou à un collègue qui rejoint le brain. Lis-le avant de toucher au repo.

## Philosophie en 3 lignes

1. **Deux usages, deux modes** : `brain` (enrichir le brain, depuis le vault) et `project` (utiliser le brain depuis un projet de dev). Il y en avait trois jusqu'au lot 7 ; « wiki » n'était pas un mode mais une frontière sur le rôle.
2. **Deux axes de rangement, et le dossier se dérive.** `categorie:` dit le domaine, `famille:` dit la nature technique, `role:` dit ce que la page est. Le chemin d'une page est une **conséquence** de sa `categorie:` — personne ne choisit un dossier.
3. **Frontmatter > prose** : la connaissance factuelle (les briques) est en YAML dense, queryable. La prose est pour la nuance.

## Anatomie du repo (v3)

**Un dossier par domaine, à la racine** — c'est toute la structure. `Dev/`, `MOC/Categories/`
et `MOC/Types/` n'existent plus depuis le lot 3.

| Dossier | Mode | Rôle | Ouvrir avec |
|---|---|---|---|
| **`<Domaine>/`** ×20 | brain | L'arbre : `Bases de données/`, `Machine Learning/`, `LLM & IA générative/`, `Data & pipelines/`… Contient les briques (`role: brique`), les comparatifs `.base`, et une page hub à son nom | skill `enrichir-brain` |
| `<Domaine>/<Sous-domaine>/` | brain | Promu quand un sous-domaine atteint 5 pages (`Vectoriel/`, `Apprentissage profond/`…), sauf s'il ne laisse aucune page au domaine | idem |
| `<Domaine>/<Domaine>.md` | **généré + main** | La page hub du dossier (`role: hub`). Corps à la main, zone `<!-- AUTO -->` générée | corps : éditeur · AUTO : `build_mocs.py` |
| `Métiers/` | **généré** | 5 hubs transverses (Data Science, Data Engineering, MLOps, ML Engineering, AI Engineering), générés depuis `domaines:` | `AI/scripts/build_mocs.py` |
| `Patterns/` | brain | `Pattern - <nom>.md` (`role: pattern`) — groupés par rôle, sans `categorie:` | éditeur / `enrichir-brain` |
| `Rules/` | brain | `Rule - <nom>.md` (`role: rule`) — idem | éditeur direct |
| `Wiki/Concepts/` | brain | Les 297 notions (`role: notion`). **Descendront dans l'arbre au lot 4** | `enrichir-brain` / Templater `Concept-Wiki` |
| `MOC/Concepts/` | **généré** | 10 MOC, seule porte d'entrée de 30 notions. Meurent avec `Wiki/Concepts/` au lot 4 | `build_mocs.py`, ne pas éditer à la main |
| `Wiki/Outils|Workflows|Roadmaps/` | — | Scaffolds **vides** — contenu v1 pas remigré, reconduction non acquise | — |
| `Documentation/` | brain | Gouvernance : tags, taxonomie, thèmes, conventions perso | éditeur direct |
| `Projects/` | brain (log) | Suivi des projets actifs — scaffold vide aujourd'hui | éditeur direct |
| `Templates/` | brain | Gabarits Templater | éditeur direct |
| `AI/` | agent | Espace de l'agent : design, migration, index généré, sessions, scripts, backlog | agent uniquement |
| `.claude/` | tous | Config Claude Code + skills custom (`enrichir-brain`, `cloturer-brain`, `planifier-projet`) | éditeur, voir `.claude/README.md` |
| `.githooks/` | tous | Hooks git versionnés — le garde-fou d'identité (cf. *Commits*) | éditeur, activation dans `INSTALL.md` §3.5 |
| `docs/install/` | tous | Captures et ressources pour `INSTALL.md` | éditeur direct |

## Règles de modification

### Les pages du brain — strict

- **Frontmatter obligatoire et conforme** au gabarit de son `role:` (cf. `CLAUDE-build.md`). Un champ hors gabarit fait échouer le validateur en dur.
- **Le dossier se dérive**, il ne se choisit pas : `categorie:` → `AI/scripts/arbo.py` → chemin. `check_arbo.py` le vérifie et propose le déplacement.
- **Taxonomie verrouillée** : les valeurs de `categorie:` et `famille:` viennent de `Documentation/general/taxonomie.md`, qui porte un arbre de décision déterministe pour chacune. Pas d'en inventer. Si rien ne va, ouvrir une discussion avant.
- **`maturite:`** porte seul l'état d'une brique : `production | beta | experimental | deprecated`. `status:` a été supprimé au lot 2 — ne pas le réintroduire.
- **Tags** : uniquement ceux de `Documentation/general/tags.md` — proposer avant d'ajouter.
- Le champ `score` a été **supprimé en v2** (jamais fiable) — ne pas le réintroduire.
- **Wikilinks nus** : `[[Qdrant]]`, jamais `[[Bases de données/Vectoriel/Qdrant|Qdrant]]`. Un lien qualifié casse au `git mv`, et les lots 4 à 6 en feront encore. Contrepartie : un nom de fichier neuf doit être **unique dans le vault**, à la casse près.
- **Une insertion se propage.** Le rayon est le dossier d'accueil plus ses hubs parents — hub, comparatif, notion, briques pairs. C'est la table P1→P6 de `enrichir-brain`, et ce n'est pas optionnel.
- **Les zones `<!-- AUTO -->` sont générées** : une édition manuelle sera écrasée à la clôture. Le corps d'un hub, lui, s'écrit à la main et ne se répare pas tout seul.

### Les notions (`role: notion`) — l'espace perso de floSa

- Frontmatter obligatoire et **fermé** : `role`, `nom`, `alias`, `categorie`, `domaines`, `tags`. Rien d'autre.
- **Créer** une notion : normal, dès qu'une capture en a besoin. **Modifier** une notion existante : sur demande explicite de floSa.
- Wikilinks : ne pas créer de `[[X]]` vers du vide (`check_brain` R2 le refuse en dur).
- Pas de nouveau sous-dossier dans `Wiki/` : le rangement se dérivera de `categorie:` au lot 4.
- `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` sont vides : le workflow `discovered → tested → used → abandoned` hérité de la v1 n'a été ni retranché ni reconfirmé — à trancher si/quand ce pilier est remigré (cf. `Documentation/perso/reservoir-v1.md`).

### `CLAUDE*.md` — modifier avec prudence

- `CLAUDE.md` (routeur) : ne touche que si tu ajoutes un mode ou une frontière. Il porte aussi la **règle d'identité git**, qui doit y rester.
- `CLAUDE-build.md` (contexte brain) : ajouts de taxonomie OK, refonte = discussion.
- `CLAUDE-project.md` : c'est un **template** copié dans des projets externes. Modifier rétro-impacte les projets futurs.

## Workflow type

### Ajouter une brique

```
mode brain
> ajoute <nom>, voici l'URL : <url>
```

Le skill `enrichir-brain` :
1. Vérifie la non-duplication (alias inclus) et l'unicité du nom de fichier
2. Dérive `categorie:`, `famille:`, puis le **dossier d'accueil**
3. Liste le **rayon de propagation** — `ls` du dossier — et remplit la table P1→P6 nominativement
4. Vérifie les faits sur le web, écrit la fiche, synchronise les alternatives dans les deux sens
5. Confronte `git status` au contenu du dossier, et signale tout écart

Tu valides, il écrit dans `<Dossier>/<Nom>.md`. Puis `cloturer-brain` régénère, valide et commite.

### Ajouter une notion

```
mode brain
> ajoute le concept <nom>
```

Même skill. La notion va dans `Wiki/Concepts/<Nom>.md` jusqu'au lot 4, et se câble à ses
briques **dans les deux sens**.

### Logger un bug rencontré

Pas de skill dédié. En mode brain :
```
> log un bug : <symptôme> sur <brique>
```
Ajoute l'entrée datée dans la section `## Pièges` de la fiche : `- YYYY-MM-DD — <symptôme> :
<correctif>.` Un incident inter-briques s'inscrit **une seule fois**, sous celle qui a porté
le correctif (cf. `CLAUDE-build.md`).

### Comparer des briques

```
mode brain
> compare <X> et <Y> et <Z>
```

`enrichir-brain` crée/met à jour `<Dossier>/Comparatif - <thème>.base`, **dans le dossier de
ses membres**, filtré par `categorie` — jamais par chemin ni par liste de noms codée en dur.

## Commits

### Identité — règle dure

Le DevBrain est un dépôt **perso**. L'identité de ses commits est celle de la **config locale
du dépôt** :

```bash
git config --local user.name    # floSa
git config --local user.email   # l'adresse perso
```

Claude Code annonce à chaque conversation une adresse en `@aosis.net` : c'est l'adresse **pro**
de floSa, elle n'attribue **jamais** un commit d'ici. Jamais de `-c user.email`, jamais de
`--author`, jamais d'`GIT_AUTHOR_EMAIL`.

**Un garde-fou versionné le vérifie** : `.githooks/pre-commit` refuse un tel commit,
`.githooks/pre-push` refuse de le pousser. À activer une fois par clone :

```bash
git config core.hooksPath .githooks
```

Détails et dépannage : `INSTALL.md` §3.5. Politique git complète :
`.claude/skills/cloturer-brain/SKILL.md`, **seul endroit où elle est écrite**.

### Messages

Format **Conventional Commits**, en français OK pour la description :

```
feat(<scope>): ajout de X
fix(<scope>): correction Y
docs(<scope>): améliore Z
chore(<scope>): refactor/nettoyage W
```

Scopes courants : `brain`, `briques`, `notions`, `patterns`, `rules`, `hubs`, `documentation`,
`infra`, `docs`, `templates`, `v3` (pour les lots de migration).

Un message multi-lignes se passe par **`git commit -F <fichier>`**, pas par `-m` : les
backticks du texte seraient interprétés par le shell et remplaceraient silencieusement un
morceau du message.

## Ce qui n'est pas toléré

- Mettre `maturite: production` sur une fiche jamais vérifiée en réel.
- Wikilinks vers du vide (`[[Truc]]` sans fichier `Truc.md`) — refusé en dur par `check_brain` (R2).
- Wikilinks qualifiés par chemin — ils cassent au prochain déplacement.
- Poser une page ailleurs que dans le dossier que sa `categorie:` désigne.
- Modifier une fiche `maturite: deprecated` sans discussion.
- **`rm` sur une page** pendant la migration v3 : un déplacement se fait par `git mv`, une suppression se demande.
- Committer avec une adresse `@aosis.net`, ou contourner les hooks avec `--no-verify`.
- Push direct sur `main` avec `--force` (sauf cas exceptionnel discuté). Réécriture d'historique : décision de floSa, jamais d'un agent.
- Trailer `Co-Authored-By` : les commits sont à floSa seul.
- Commit des fichiers `.obsidian/plugins/`, `.obsidian/community-plugins.json`, `.obsidian/graph.json` (déjà gitignorés).
- Commit de secrets, clés API, URLs avec tokens (cf. `.gitignore`).

## MCP Obsidian — convention d'utilisation

Quand le MCP `devbrain` (instance de `mcp-obsidian`) est connecté (`claude mcp list` →
`✓ Connected`), les skills qui touchent au vault **préfèrent les outils `mcp__devbrain__*` aux
outils standard** :

- `mcp__devbrain__read_file_content` au lieu de `Read` pour les .md du vault
- `mcp__devbrain__create_file` / `patch_content` / `append_to_file` au lieu de `Write` / `Edit`
- `mcp__devbrain__search_files` au lieu de `Grep` pour la recherche full-text
- `mcp__devbrain__list_files_in_dir` au lieu de `Glob`

Raison : le MCP respecte le format Obsidian (frontmatter, wikilinks, properties typées) et
déclenche la ré-indexation du vault (Bases mises à jour, backlinks recalculés).

**Fallback** sur les outils standard si Obsidian n'est pas ouvert ou MCP non configuré — cas
dégradé mais fonctionnel.

## Setup local

Voir [`INSTALL.md`](INSTALL.md) — guide pas à pas avec captures.

Au premier clone :
1. `git config core.hooksPath .githooks` — active le garde-fou d'identité (§3.5)
2. Copier `.claude/settings.example.json` → `.claude/settings.json` (lis avant)
3. Copier `.claude/settings.local.example.json` → `.claude/settings.local.json`
4. Personnaliser `CLAUDE.md` (identité utilisateur)

## En cas de doute

Pose la question avant d'agir. La taxonomie est délibérément étroite — l'inventer rend le
brain inutile à terme.
