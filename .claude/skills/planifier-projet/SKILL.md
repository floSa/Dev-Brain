---
name: planifier-projet
description: |
  Use this skill at the kickoff of a new project, when the user wants a plan or a
  stack proposal grounded in the DevBrain v2. Triggers: "propose-moi un plan",
  "je veux une appli qui fait X", "quel stack pour ce projet", "aide-moi à cadrer".
  Identifies the project archetype, asks only the relevant scoping questions,
  queries AI/index/brain-index.json to surface 2-3 candidates per brick (each with
  its one-line pitch) as choice questions, then produces a sourced plan that will
  constrain the downstream dev AI.
---

# Skill — planifier-projet

Skill de **cadrage** projet. Implémente le workflow W2 de `AI/design/brain-v2.md` (§2, §7.2, §8). Interroge surtout les `role: brique` (+ quelques `role: notion`) et produit un cahier des charges sourcé. N'écrit aucune fiche dans le brain.

## Quand l'utiliser

- Démarrage de projet : « je veux une appli copie de tel jeu », « propose-moi un plan », « quel stack ? ».

Distinct de :
- `enrichir-brain` (capture de connaissance dans le brain).

## Pré-requis

Mode build ou projet. Lit `AI/index/brain-index.json`, `Dev/` (Services, Patterns, Rules), et `Documentation/`. Sortie : un plan verbal, ou écrit dans `Projects/<projet>/` si l'utilisateur le demande.

## Appuis

- `AI/index/brain-index.json` — pour filtrer les candidats **sans lire 160 fichiers** (pitch, tags, categorie, famille, **role**, **maturite**, alternatives, complements). `maturite` est le critère éliminatoire : il est dans l'index, ne plus supposer qu'il faut ouvrir la fiche pour le connaître.
- `AI/scripts/query_index.py` — la requête bornée sur cet index ; renvoie `maturite` par défaut, et sait filtrer dessus (`--maturite`), ainsi que sur `--role` et `--famille`.
- `Documentation/perso/archetypes.md` — les 7 archétypes.
- `Documentation/general/questions-projet.md` — checklist de cadrage (branchée par archétype).
- `Documentation/perso/conventions.md` — stacks par défaut de floSa.

## Procédure

1. **Lire la description** du projet fournie par l'utilisateur.
2. **Identifier l'archétype** (`Documentation/perso/archetypes.md`) :
   1. Analyse / exploration · 2. App data/ML interactive · 3. ML/IA algorithmique ·
   4. Pipeline data / ingestion · 5. RAG / app LLM · 6. Tuto / apprentissage · 7. Réplique ludique.
   L'archétype conditionne **quelles** questions poser.
3. **Poser tôt l'axe transverse on-premise** (`questions-projet.md`) : cloud autorisé ou **on-prem strict / air-gapped** ? GPU ou CPU only ? Données qui sortent du réseau client ? Ces réponses éliminent d'emblée des candidats (ex. API LLM interdite si air-gapped).
4. **Ne poser que les questions pertinentes** de la checklist (cadrage, exécution, données, IA/LLM, légal, qualité). Utiliser des **questions à choix** pour que l'utilisateur tranche vite.
5. **Pour chaque brique nécessaire** (BDD, framework, LLM, orchestration…) :
   - requêter `AI/index/brain-index.json` (filtrer par `categorie`, `tags`, contraintes) ;
   - **appliquer la règle de filtrage `maturite`** ci-dessous **avant** de retenir
     la moindre candidate ;
   - proposer **2-3 candidats**, chacun affiché avec son **pitch d'une ligne** (champ `pitch:` de l'index) ;
   - laisser l'utilisateur trancher.
6. **Produire le plan / cahier des charges**, sourcé : chaque choix renvoie à sa fiche (`[[Dev/Services/...]]`, `[[Pattern - ...]]`, `[[Rules/...]]`) et porte la raison du choix + les alternatives écartées. Inclure les risques connus depuis la section `## Pièges` des fiches retenues.

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
| `maturite: null` (notion, pattern, rule) | pas de filtre — le champ ne s'applique pas à ces rôles. |

Trois conséquences opérationnelles :

1. **Écarter n'est pas taire.** Une brique `deprecated` retirée de la liste se mentionne dans la
   ligne `**Écartés**` du plan, avec sa raison réelle (« dépréciée »), pas un motif inventé.
2. **`alternatives:` porte la succession.** Dès qu'une candidate est écartée, ce sont les cibles
   de son `alternatives:` qu'il faut proposer à la place. Le champ est **dans l'index**, donc
   sans lecture supplémentaire :
   ```bash
   uv run AI/scripts/query_index.py --name "<Écartée>" --fields nom,maturite,alternatives
   ```
   `remplace_par:` a été supprimé au lot 2 : il était vide sur 293 des 297 fiches, et les 4 qui
   le portaient avaient déjà leurs cibles dans `alternatives:`. Ne plus le chercher.
3. **Ne jamais adoucir un état.** « Un peu ancien », « en cours de stabilisation » pour une brique
   `deprecated` est un mensonge par euphémisme. Le mot du frontmatter, ou rien.

Vérification d'un doute, en une commande :

```bash
uv run AI/scripts/query_index.py --categorie <cat> --role brique
```

La sortie porte `role`, `famille` et `maturite` pour chaque correspondance.

## Format de sortie

```markdown
## Cadrage
- Archétype : <n°/nom> · Périmètre : perso/pro · Exécution : <où> · On-prem : <oui/non> · GPU : <oui/non>

## Stack proposé
### <Brique> : <Choix retenu>
**Pourquoi** : <2 lignes, depuis le pitch + la fiche>
**État** : <à renseigner si `maturite: deprecated`/`experimental`/`beta` ; sinon omettre>
**Écartés** : <Candidat B> (raison), <Candidat C> (raison — « abandonnée, remplacée par <X> » le cas échéant)
**Source** : [[Dev/Services/<Choix>]]

## Patterns appliqués
- [[Pattern - <Y>]]

## Risques connus
- (depuis la section `## Pièges` des fiches retenues)

## Contraintes pour l'IA de dev
- <règles issues de Dev/Rules/ + conventions perso>
```

## Anti-patterns

- Proposer un candidat absent de l'index (= choix non sourcé).
- Poser toutes les questions de la checklist quel que soit l'archétype.
- Oublier l'axe on-prem / air-gapped alors qu'il élimine des options.
- Recopier un pitch divergent : toujours réutiliser celui de l'index.
- Proposer une brique `maturite: deprecated` sans le dire — l'index porte le champ, l'ignorer est une faute.
- Proposer une brique `en-eval` ou `deprecated` **sans annoncer son état** : le candidat est
  légitime, le silence sur son état ne l'est pas.
- Écarter une fiche sans regarder son `alternatives:`, qui nomme ses successeurs.

## Voir aussi

- `enrichir-brain` — si une brique utile manque dans le brain, l'ajouter d'abord.
- `AI/design/brain-v2.md` §2, §7.2, §8 — spec de référence.
