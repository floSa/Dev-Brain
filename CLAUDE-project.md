---
nom: CLAUDE-project
role: gouvernance
created: 2026-05-20
modified: 2026-09-05
tags: [meta]
---

# CLAUDE.md — Projet : <NOM_DU_PROJET>

> Ce fichier est un **template**. Copie-le vers `<dossier_du_projet>/CLAUDE.md` et adapte les placeholders `<...>`.

Tu travailles sur le projet **<NOM_DU_PROJET>** (type : `<CLI | Web app | Library | ML pipeline | Data pipeline>`).

Stack : `<liste rapide, ex: Python 3.12, FastAPI, Postgres, Redis>`.

## Accès au DevBrain

Le **DevBrain** est accessible via MCP sous le nom `devbrain`. Outils :

- `mcp__devbrain__search` — recherche full-text dans le brain
- `mcp__devbrain__list_files_in_dir` — lister un dossier
- `mcp__devbrain__get_file_contents` — lire une note précise
- `mcp__devbrain__patch_content` — modifier une section
- `mcp__devbrain__append_content` — append à un fichier

Si le MCP n'est pas dispo : **alerte explicitement l'utilisateur**, ne fais pas de fallback silencieux.

## Comment le brain est rangé (v3)

Une seule chose à retenir : **un dossier par domaine, à la racine**. Il n'y a plus de galaxie
`Dev/` ni `Wiki/`, plus de dossier `Services/` ni `Concepts/`. Une **notion** (ce qu'il faut
comprendre) et une **brique** (ce qu'on déploie) du même sujet vivent dans le même dossier ;
c'est le champ `role:` de leur frontmatter qui les distingue, pas leur chemin.

```
<20 dossiers de domaine>/     Bases de données/, Machine Learning/, LLM & IA générative/,
│                             Data & pipelines/, DevOps/, Web & API/, Stockage/…
├── <Domaine>.md              la page hub du dossier — l'aiguillage, à lire en premier
├── <Sous-domaine>/           quand un sous-domaine atteint 5 pages (Vectoriel/, …)
│   ├── <Sous-domaine>.md     hub, lui aussi
│   ├── <Brique>.md           la fiche d'une techno (role: brique)
│   ├── <Notion>.md           la notion du sujet    (role: notion)
│   └── Comparatif - <thème>.base
├── <Brique>.md               idem, au niveau du domaine
└── <Notion>.md               idem

Métiers/                      6 hubs transverses : Data Science, Data Engineering,
                              MLOps, ML Engineering, AI Engineering,
                              Infrastructure & Ops
Patterns/Pattern - <nom>.md   architectures éprouvées
Rules/Rule - <nom>.md         règles transverses
Home.md                       la porte d'entrée du vault
```

**Le hub d'un domaine est la meilleure entrée** quand tu ne connais pas le nom de la brique
qu'il te faut : il porte `## Ce qu'il faut comprendre` (les confusions du domaine, levées) et
`## Choisir` (l'aiguillage écrit à la main). Le lire évite de comparer trois candidats là où le
hub dit que la question ne se pose pas.

## Au kickoff du projet

Invoque le skill **`planifier-projet`** (installé dans le DevBrain, `.claude/skills/planifier-projet/`) — pas dans ce dépôt projet. Il :

1. Identifie l'**archétype** du projet (`Documentation/perso/archetypes.md` du brain : analyse de données, app interactive, ML/IA algorithmique, pipeline data, RAG/app LLM, tuto, réplique perso).
2. Ne pose que les questions pertinentes (`Documentation/perso/conventions.md` et `Documentation/general/questions-projet.md` du brain — cadrage, exécution, données, IA/LLM, légal, qualité ; axe transverse **on-prem / air-gapped**).
3. Pour chaque brique technique nécessaire, entre par le hub du domaine si besoin, interroge `AI/index/brain-index.json` et propose 2-3 candidats sourcés — chacun avec son pitch, sa **nature** (`famille:`) et son **langage**.
4. Produit un cahier des charges qui **contraint** la suite du développement. N'écrit rien dans le brain.

Si le skill n'est pas invocable depuis le projet (il vit dans le repo DevBrain, pas dans celui-ci), demande directement à l'utilisateur de lancer `claude` à la racine de son vault DevBrain pour ce cadrage (l'emplacement dépend de la machine — ne suppose aucun chemin), ou interroge le brain toi-même via MCP en suivant le même protocole.

## Avant tout choix techno

Consulte le DevBrain :

1. **Entre par le hub du domaine** si tu ne sais pas quoi chercher : `<Domaine>/<Domaine>.md`.
2. Cherche les **briques pertinentes** :
   ```
   mcp__devbrain__search avec mots-clés du besoin
   ```
3. Pour chaque brique envisagée, lis sa fiche `<Domaine>/[<Sous-domaine>/]<Nom>.md`. Sa
   section `## Pièges` porte les pièges connus et les retours d'expérience datés ; son
   `maturite:` dit si elle est vivante — **une brique `deprecated` ne se propose pas** sans
   annoncer son état, et son `alternatives:` nomme ses successeurs.
4. Cherche un **Pattern existant** : `Patterns/Pattern - <nom>.md` (ex: Agent ReAct, RAG basique, Pipeline ELT moderne, Forecasting production).
5. Cherche un **Comparatif** : `<Domaine>/[<Sous-domaine>/]Comparatif - <thème>.base` — il vit **dans le dossier de ses membres**, donc à côté des fiches qu'il compare.

Propose-moi un stack motivé en citant les fiches et patterns du brain. **Wikilinks nus** si tu
en écris : `[[Qdrant]]`, jamais un chemin — le vault se réorganise encore (lots 4 à 6), et un
lien qui porte un chemin casse au premier déplacement.

## Règles à appliquer

Lis depuis devbrain les règles pertinentes dans `Rules/Rule - *.md` (le brain n'a aujourd'hui
que 5 règles génériques — pas encore de déclinaison par type de projet ou par stack ; applique
celles qui sont pertinentes, signale l'absence de règle si le sujet n'est pas couvert plutôt
que d'improviser).

Strictness (champ `strictness` du frontmatter Rule) :
- **must** : bloquant, applique sans demander
- **should** : applique par défaut, signale les écarts dans tes outputs
- **nice-to-have** : applique si possible

## Documentation du projet (à ton initiative, pas encore cadrée par le brain)

Le brain n'a pas (encore) de gabarits `Rules/Documentation/*` ni `Templates/ServiceDocs/` par
type de service — ce pan de la v1 n'a pas été remigré. En attendant, documente le projet avec
un bon sens standard :

- `docs/PLAN.md` / `docs/ARCHITECTURE.md` en phase de cadrage.
- Un `README.md` par service intégré s'il y a plusieurs composants.
- `docs/adr/NNNN-<sujet>.md` pour les décisions structurelles.
- `docs/DEPLOY.md` / `docs/OPERATIONS.md` avant mise en prod.

Si tu identifies un besoin récurrent qui mériterait une règle générique dans le brain,
propose-le pour une session en mode brain plutôt que de le garder local au projet.

## Log de bug (workflow important)

Il n'existe pas (encore) de skill `log-bug`. Quand tu rencontres un bug lié à une brique
utilisée :

1. Reproduis et confirme la cause racine.
2. Note dans `Projects/<projet>/Bugs.md` (DevBrain, via MCP) le détail du bug et le contexte projet — ce dossier `Projects/` est un scaffold vide aujourd'hui, crée le fichier si besoin.
3. **Signale-le** à l'utilisateur comme piège à capitaliser dans la section `## Pièges` de la fiche de la brique. Tu n'écris pas dans l'arbre des domaines depuis un projet : cette capture se fait en mode brain, dans le vault, et elle déclenche la règle de propagation.

Format attendu de l'entrée, quand elle sera écrite dans le vault :
`- YYYY-MM-DD — <symptôme> : <correctif>.` Un incident né entre deux briques s'inscrit **une
seule fois**, sous celle qui a porté le correctif, les autres nommées en clair dans la ligne.

## Audit ponctuel

Une fois par sprint, demande-moi (ou propose) :

```
Audit du projet contre les Rules du devbrain (Rules/) applicables à ce type de projet.
Liste les écarts must. Liste les écarts should avec mon jugement requis.
```

## Ce que tu NE fais PAS

- **N'écris rien dans le brain depuis un projet.** Ni dans l'arbre des 20 domaines, ni dans `Métiers/`, `Patterns/`, `Rules/`. Ces pages sont factuelles et durables ; elles se modifient en mode brain, dans le vault, où la règle de propagation s'applique.
- Ne crée pas de nouvelles règles ni de nouveaux patterns dans le brain (ça se fait en mode brain).
- Ne supprime rien dans le brain.
- Ne duplique pas le brain dans le projet (pas de `cp -r` du DevBrain).
- N'écris pas de wikilink qualifié par chemin vers une page du brain : il cassera.

## Voix et style

- Français par défaut.
- Phrases courtes. Pas de marketing-speak.
- Tu peux contredire.
