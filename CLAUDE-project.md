---
galaxie: meta
nom: CLAUDE-project
type: meta-doc
created: 2026-05-20
modified: 2026-07-07
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
- `mcp__devbrain__patch_content` — modifier une section (utilisé pour logger un REX)
- `mcp__devbrain__append_content` — append à un fichier

Si le MCP n'est pas dispo : **alerte explicitement l'utilisateur**, ne fais pas de fallback silencieux.

## Au kickoff du projet

Invoque le skill **`planifier-projet`** (installé dans le DevBrain, `.claude/skills/planifier-projet/`) — pas dans ce dépôt projet. Il :

1. Identifie l'**archétype** du projet (`Documentation/perso/archetypes.md` du brain : analyse de données, app interactive, ML/IA algorithmique, pipeline data, RAG/app LLM, tuto, réplique perso).
2. Ne pose que les questions pertinentes (`Documentation/perso/conventions.md` et `Documentation/general/questions-projet.md` du brain — cadrage, exécution, données, IA/LLM, légal, qualité ; axe transverse **on-prem / air-gapped**).
3. Pour chaque brique technique nécessaire, interroge `AI/index/brain-index.json` et propose 2-3 candidats sourcés (pitch d'une ligne chacun).
4. Produit un cahier des charges qui **contraint** la suite du développement. N'écrit rien dans le brain.

Si le skill n'est pas invocable depuis le projet (il vit dans le repo DevBrain, pas dans celui-ci), demande directement à l'utilisateur de lancer `claude` dans `~/DevBrain` pour ce cadrage, ou interroge le brain toi-même via MCP en suivant le même protocole.

## Avant tout choix techno

Consulte le DevBrain :

1. Cherche les **Services/Outils pertinents** :
   ```
   mcp__devbrain__search avec mots-clés du besoin
   ```
2. Pour chaque service envisagé, lis :
   - `Dev/Services/<nom>.md` (la fiche)
   - `Dev/REX/REX - <nom>.md` (s'il existe — pièges connus)
3. Cherche un **Pattern existant** : `Dev/Patterns/Pattern - <type>.md` (ex: Agent ReAct, RAG basique, Pipeline ELT moderne, Forecasting production).
4. Cherche un **Comparatif** : `Dev/Patterns/Comparatif - <thème>.base` filtré par catégorie.

Propose-moi un stack motivé en citant les fiches/patterns du brain.

## Règles à appliquer

Lis depuis devbrain les règles pertinentes dans `Dev/Rules/Rule - *.md` (le brain n'a aujourd'hui que 5 règles génériques — pas encore de déclinaison par type de projet ou par stack ; applique celles qui sont pertinentes, signale l'absence de règle si le sujet n'est pas couvert plutôt que d'improviser).

Strictness (champ `strictness` du frontmatter Rule) :
- **must** : bloquant, applique sans demander
- **should** : applique par défaut, signale les écarts dans tes outputs
- **nice-to-have** : applique si possible

## Documentation du projet (à ton initiative, pas encore cadrée par le brain)

Le brain v2 n'a pas (encore) de gabarits `Rules/Documentation/*` ni `Templates/ServiceDocs/` par type de service — ce pan de la v1 n'a pas été remigré. En attendant, documente le projet avec un bon sens standard :

- `docs/PLAN.md` / `docs/ARCHITECTURE.md` en phase de cadrage.
- Un `README.md` par service intégré s'il y a plusieurs composants.
- `docs/adr/NNNN-<sujet>.md` pour les décisions structurelles.
- `docs/DEPLOY.md` / `docs/OPERATIONS.md` avant mise en prod.

Si tu identifies un besoin récurrent qui mériterait une règle générique dans le brain, propose-le en mode build plutôt que de le garder local au projet.

## Log de bug (workflow important)

Il n'existe pas (encore) de skill `log-bug` en v2. Quand tu rencontres un bug lié à un service utilisé :

1. Reproduis et confirme la cause racine.
2. Note dans `Projects/<projet>/Bugs.md` (DevBrain, via MCP) le détail du bug, contexte projet — ce dossier `Projects/` est un scaffold vide aujourd'hui, crée le fichier si besoin.
3. **Et** ajoute (ou crée) un REX dans `Dev/REX/REX - <service>.md`, au format standard, via `mcp__devbrain__patch_content` / `append_content`.

Format REX :

```markdown
## YYYY-MM-DD — <Symptôme court>

**Symptôme** : <détails>
**Cause racine** : <explication>
**Fix** :
1. ...
2. ...
**Référence** : [[Projects/<projet>/Bugs#YYYY-MM-DD]]
**Leçon** : <synthèse réutilisable>
```

C'est ainsi que le brain s'enrichit naturellement depuis les projets.

## Audit ponctuel

Une fois par sprint, demande-moi (ou propose) :

```
Audit du projet contre les Rules du devbrain (Dev/Rules/) applicables à ce type de projet.
Liste les écarts must. Liste les écarts should avec mon jugement requis.
```

## Ce que tu NE fais PAS

- Ne modifie pas les fiches `Dev/Services/` ou `Dev/Outils/`. Elles sont **factuelles et durables** ; tu ne les touches qu'en mode BUILD.
- Tu peux écrire dans `Dev/REX/REX - <service>.md` (création ou append d'une nouvelle entrée datée) — c'est l'usage prévu du mode projet.
- Ne crée pas de nouvelles règles dans le brain (ça se fait en mode BUILD du brain).
- Ne supprime rien dans le brain.
- Ne dupliques pas le brain dans le projet (pas de `cp -r` du DevBrain).

## Voix et style

- Français par défaut.
- Phrases courtes. Pas de marketing-speak.
- Tu peux contredire.
