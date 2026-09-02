---
name: planifier-projet
description: |
  Use this skill at the kickoff of a new project, when the user wants a plan or a
  stack proposal grounded in the DevBrain v3. Triggers: "propose-moi un plan",
  "je veux une appli qui fait X", "quel stack pour ce projet", "aide-moi a cadrer".
  Identifies the project archetype, asks only the relevant scoping questions,
  queries AI/index/brain-index.json to surface 2-3 candidates per brick (each with
  its one-line pitch, its famille and its langage) as choice questions, then
  produces a sourced plan that will constrain the downstream dev AI. Reads the
  domain hub when the name of the needed brick is unknown. Never writes into the
  brain.
---

# Skill — planifier-projet

Skill de **cadrage** projet. Implémente le workflow W2 de `AI/design/brain-v2.md` (§2, §7.2,
§8), sur la structure v3. Interroge surtout les `role: brique` (+ quelques `role: notion`) et
produit un cahier des charges sourcé. **N'écrit aucune fiche dans le brain**, et n'écrit rien
dans l'arbre des domaines.

## Quand l'utiliser

- Démarrage de projet : « je veux une appli copie de tel jeu », « propose-moi un plan », « quel stack ? ».

Distinct de :
- `enrichir-brain` (capture de connaissance dans le brain — à invoquer si une brique utile manque).

## Pré-requis

Lit `AI/index/brain-index.json`, les pages de l'arbre des 20 domaines, `Patterns/`, `Rules/`
et `Documentation/`. Sortie : un plan verbal, ou écrit dans `Projects/<projet>/` si
l'utilisateur le demande.

## Appuis

- `AI/index/brain-index.json` — pour filtrer les candidats **sans lire les fiches** : `path`, `pitch`, `tags`, `categorie`, **`famille`**, `role`, **`maturite`**, `alternatives`, `complements`, `domaines`, `alias`.
- `AI/scripts/query_index.py` — la requête bornée sur cet index. Filtre sur `--categorie`, `--role`, **`--famille`**, `--maturite`, `--tag` ; renvoie `famille` et `maturite` par défaut (ce sont des critères éliminatoires : les masquer ferait filtrer à l'aveugle).
- **Les hubs de l'arbre** — `<Domaine>/<Domaine>.md`, `role: hub`. La porte d'entrée quand le nom de la brique cherchée est inconnu (cf. *Entrer par le hub*).
- `Documentation/perso/archetypes.md` — les 7 archétypes.
- `Documentation/general/questions-projet.md` — checklist de cadrage (branchée par archétype).
- `Documentation/perso/conventions.md` — stacks par défaut de floSa.
- `Documentation/general/taxonomie.md` — les 20 domaines et leur portée, si le besoin ne se rattache à aucun hub évident.

---

## Entrer par le hub quand le nom de la brique est inconnu

C'est le gain v3 de ce skill. Avant, un besoin sans nom de produit (« il me faut de quoi
stocker des embeddings ») obligeait à deviner des tags. Maintenant, le **domaine est un
dossier**, et son hub est écrit pour aiguiller.

```bash
ls -1 */[!C]*.md | grep -E '^([^/]+)/\1\.md$'    # les hubs de domaine, un par dossier racine
```

Ou plus simplement : `Home.md` porte l'arbre, et chaque dossier de domaine porte une page à
son nom. Le hub donne deux choses qu'aucune requête ne donne :

- `## Ce qu'il faut comprendre` — les confusions du domaine, levées. Souvent la vraie réponse à « quelle brique me faut-il ? ».
- `## Choisir` — l'aiguillage écrit à la main : « du Postgres déjà en place → pgvector, et la question est réglée ».

Lire le hub **avant** de requêter l'index évite de proposer trois candidats là où le hub dit
que la question ne se pose pas. Il ne dispense pas de la requête : sa zone `<!-- AUTO -->`
liste les briques du dossier, mais `maturite` et `famille` viennent de l'index.

---

## Procédure

1. **Lire la description** du projet fournie par l'utilisateur.
2. **Identifier l'archétype** (`Documentation/perso/archetypes.md`) :
   1. Analyse / exploration · 2. App data/ML interactive · 3. ML/IA algorithmique ·
   4. Pipeline data / ingestion · 5. RAG / app LLM · 6. Tuto / apprentissage · 7. Réplique ludique.
   L'archétype conditionne **quelles** questions poser.
3. **Poser tôt l'axe transverse on-premise** (`questions-projet.md`) : cloud autorisé ou
   **on-prem strict / air-gapped** ? GPU ou CPU only ? Données qui sortent du réseau client ?
   Ces réponses éliminent d'emblée des candidats (ex. API LLM interdite si air-gapped).
4. **Ne poser que les questions pertinentes** de la checklist (cadrage, exécution, données,
   IA/LLM, légal, qualité). Utiliser des **questions à choix** pour que l'utilisateur tranche vite.
5. **Pour chaque brique nécessaire** (BDD, framework, LLM, orchestration…) :
   - nom de brique inconnu → **lire d'abord le hub du domaine** (ci-dessus) ;
   - requêter l'index (`--categorie`, `--famille`, `--tag`, contraintes du cadrage) ;
   - **appliquer la règle de filtrage `maturite`** ci-dessous **avant** de retenir la moindre candidate ;
   - proposer **2-3 candidats**, chacun affiché au **format de candidature** ci-dessous ;
   - laisser l'utilisateur trancher.
6. **Produire le plan / cahier des charges**, sourcé : chaque choix renvoie à sa fiche par un
   **wikilink nu** (`[[Qdrant]]`, `[[Pattern - RAG basique]]`, `[[Rule - ...]]`) et porte la
   raison du choix + les alternatives écartées. Inclure les risques connus depuis la section
   `## Pièges` des fiches retenues.

---

## Format de candidature — `famille` et `langage` sont affichés, pas devinés

C'est la demande explicite de floSa : « pour fabriquer de la donnée : **Faker, librairie
Python** ». La nature et le langage d'une brique décident souvent plus vite que sa prose.

```
- Faker — paquet Python — Génère des données factices réalistes (noms, adresses, dates)…
- Mimesis — paquet Python — …
- SDV — paquet Python — …
```

| Ce qui s'affiche | D'où ça vient | Comment l'obtenir |
|---|---|---|
| le **pitch** | champ `pitch:` | index — **jamais retapé**, toujours copié |
| la **nature** (`famille:`) | 9 valeurs fermées : `paquet`, `plateforme`, `application`, `cli`, `saas`, `extension`, `specification`, `modele`, `annuaire` | index (`--famille` filtre, et le champ est renvoyé par défaut) |
| le **langage** (`langage:`) | langage d'implémentation | **pas dans l'index** — se lit dans le frontmatter de la fiche (cf. ci-dessous) |
| l'**état** (`maturite:`) | enum fermée | index, renvoyé par défaut |

**`famille:` filtre.** Un besoin exprimé comme une nature se requête comme une nature — c'est
un critère, pas une lecture :

```bash
# « une bibliothèque Python pour fabriquer de la donnée », pas une plateforme à héberger
uv run AI/scripts/query_index.py --categorie data/synthetique --famille paquet
# « une plateforme à self-héberger », pas une lib à importer
uv run AI/scripts/query_index.py --categorie llm/orchestration --famille plateforme
```

**`langage:` ne filtre pas encore** : le champ existe sur les fiches mais **n'est pas indexé**
(`brain-index.json` porte `alias, alternatives, categorie, complements, domaines, famille,
maturite, nom, path, pitch, role, tags` — et pas `langage`). Le lire est donc une lecture de
fichier, bornée aux 2-3 candidates **déjà retenues** — jamais un balayage :

```bash
# après avoir réduit à 2-3 candidates par l'index, sur leurs `path`
sed -n '/^langage:/p' "Data & pipelines/Faker.md" "Data & pipelines/Mimesis.md"
```

> C'est une limite de l'outillage, pas une consigne de confort : indexer `langage:` le
> rendrait filtrable comme `famille:`. Remonté au lot 7, à trancher — les scripts étaient
> hors de son périmètre.

---

## Critères structurés — `Prendre si` / `Écarter si`

Le gabarit v3 (`AI/design/brain-v3.md` §6) donne à chaque brique un tableau
`## Prendre si / Écarter si` : des critères **structurés**, à confronter au cadrage, au lieu
d'une prose à interpréter. Chaque cellule `Écarter si` porte un wikilink vers ce qu'il faut
prendre à la place — c'est une exclusion **sourcée**, qui donne directement le candidat suivant.

**Aucune fiche ne le porte encore** : c'est le **lot 6** qui convertira les fiches au nouveau
gabarit, domaine par domaine. Écrire ce skill comme si la section existait serait écrire une
fiction. Donc, tant que le lot 6 n'est pas passé :

| Si la fiche porte… | Lire |
|---|---|
| `## Prendre si / Écarter si` (après lot 6) | le tableau, et **suivre le wikilink** de la cellule `Écarter si` qui s'applique |
| `## Quand l'utiliser` / `## Quand NE PAS l'utiliser` (aujourd'hui) | ces deux sections — le « quand NE PAS » porte déjà les wikilinks vers les alternatives |

Dans les deux cas, la règle est la même : **une exclusion se justifie et nomme la suite.**
Écarter sans dire vers quoi n'aide personne.

---

## Règle de filtrage — `maturite`

Le champ est dans `brain-index.json`. Il n'y a donc **aucune excuse** à proposer une brique
morte : la lire est un `p.get("maturite")`, pas une ouverture de fiche.

`maturite:` porte **seul** cette information depuis le lot 2 de la migration v3. `status:` a
été supprimé — il était redondant (272 fiches sur 336 étaient `actif` + `production`), et sa
valeur `en-eval` disait l'état d'évaluation de floSa, pas la maturité du produit.

| État de la candidate | Décision |
|---|---|
| `maturite: deprecated` | **jamais proposée d'office.** Écartée avant même le décompte des 2-3 candidats ; proposable seulement si rien d'autre ne couvre le besoin, et alors **état annoncé en clair**. |
| `maturite: experimental` / `beta` | proposable, mention de la maturité si la brique est structurante. |
| `maturite: null` (notion, pattern, rule, hub) | pas de filtre — le champ ne s'applique pas à ces rôles. |

Trois conséquences opérationnelles :

1. **Écarter n'est pas taire.** Une brique `deprecated` retirée de la liste se mentionne dans la
   ligne `**Écartés**` du plan, avec sa raison réelle (« dépréciée »), pas un motif inventé.
2. **`alternatives:` porte la succession.** Dès qu'une candidate est écartée, ce sont les cibles
   de son `alternatives:` qu'il faut proposer à la place. Le champ est **dans l'index**, donc
   sans lecture supplémentaire :
   ```bash
   uv run AI/scripts/query_index.py --name "<Écartée>" --fields nom,path,maturite,alternatives
   ```
   `remplace_par:` a été supprimé au lot 2 : il était vide sur 293 des 297 fiches, et les 4 qui
   le portaient avaient déjà leurs cibles dans `alternatives:`. Ne plus le chercher.
3. **Ne jamais adoucir un état.** « Un peu ancien », « en cours de stabilisation » pour une brique
   `deprecated` est un mensonge par euphémisme. Le mot du frontmatter, ou rien.

Vérification d'un doute, en une commande :

```bash
uv run AI/scripts/query_index.py --categorie <cat> --role brique
```

La sortie porte `path`, `role`, `famille` et `maturite` pour chaque correspondance.

---

## Où sont les patterns et les règles

Depuis le lot 3, ils sont **groupés par rôle**, à la racine, et non plus dans une galaxie :

- `Patterns/Pattern - <nom>.md` (`role: pattern`) — une architecture éprouvée. Aucune `categorie:` : un pattern enjambe plusieurs domaines par construction.
- `Rules/Rule - <nom>.md` (`role: rule`) — une règle transverse. Aucune `categorie:` non plus : elle est transverse par définition.

```bash
ls -1 Patterns/ Rules/
uv run AI/scripts/query_index.py --role pattern --fields nom,path
uv run AI/scripts/query_index.py --role rule --fields nom,path
```

Le brain n'a aujourd'hui que **5 patterns** et **5 règles**, toutes génériques — pas encore de
déclinaison par type de projet ou par stack. Appliquer celles qui sont pertinentes, et
**signaler l'absence** de règle si le sujet n'est pas couvert, plutôt que d'improviser.

---

## Format de sortie

```markdown
## Cadrage
- Archétype : <n°/nom> · Périmètre : perso/pro · Exécution : <où> · On-prem : <oui/non> · GPU : <oui/non>

## Stack proposé
### <Besoin> : <Choix retenu>
**Ce que c'est** : <famille> <langage>            ← ex. « paquet Python », « plateforme Rust »
**Pourquoi** : <2 lignes, depuis le pitch + la fiche>
**État** : <à renseigner si `maturite` vaut deprecated / experimental / beta ; sinon omettre>
**Écartés** : <Candidat B> — <raison, et vers quoi elle renvoie> · <Candidat C> — <raison>
**Source** : [[<Choix>]]                          ← wikilink NU, jamais de chemin

## Patterns appliqués
- [[Pattern - <Y>]]

## Risques connus
- (depuis la section `## Pièges` des fiches retenues)

## Contraintes pour l'IA de dev
- <règles issues de Rules/ + conventions perso>
```

**Wikilinks nus, jamais qualifiés par chemin.** `[[Qdrant]]`, pas
`[[Bases de données/Vectoriel/Qdrant|Qdrant]]` : un chemin casse au prochain `git mv`, et les
lots 4 à 6 en feront encore. Le plan d'un projet vit plus longtemps que l'arborescence du
vault.

## Anti-patterns

- Proposer un candidat absent de l'index (= choix non sourcé).
- Poser toutes les questions de la checklist quel que soit l'archétype.
- Oublier l'axe on-prem / air-gapped alors qu'il élimine des options.
- Recopier un pitch divergent : toujours réutiliser celui de l'index.
- **Afficher un candidat sans sa nature ni son langage** quand le besoin est exprimé en ces termes (« une lib Python pour… ») : c'est ce que la nature du champ `famille:` sert à trancher.
- **Balayer les fiches pour lire `langage:`** : le champ se lit sur les 2-3 candidates déjà retenues, jamais sur un domaine entier.
- Proposer une brique `maturite: deprecated` sans le dire — l'index porte le champ, l'ignorer est une faute.
- Proposer une brique `experimental` ou `beta` **sans annoncer son état** : le candidat est légitime, le silence sur son état ne l'est pas.
- Écarter une fiche sans regarder son `alternatives:`, qui nomme ses successeurs — ou l'écarter sans dire vers quoi.
- Deviner un aiguillage que le hub du domaine donne déjà écrit.
- **Écrire quoi que ce soit dans le brain** : ce skill lit. Une brique manquante se capture avec `enrichir-brain`, et c'est une autre décision.

## Voir aussi

- `enrichir-brain` — si une brique utile manque dans le brain, l'ajouter d'abord.
- `AI/design/brain-v3.md` §6 (le gabarit `Prendre si / Écarter si`), §12 (l'impact sur ce skill).
- `AI/design/brain-v2.md` §2, §7.2, §8 — spec du workflow de cadrage.
- `AI/migration/lot-7-skills.md` — le lot qui a écrit cette version, et la remontée sur `langage:`.
