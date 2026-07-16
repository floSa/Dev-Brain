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

Skill de **cadrage** projet. Implémente le workflow W2 de `AI/design/brain-v2.md` (§2, §7.2, §8). Interroge surtout la galaxie Dev (+ quelques Concepts Wiki) et produit un cahier des charges sourcé. N'écrit aucune fiche dans le brain.

## Quand l'utiliser

- Démarrage de projet : « je veux une appli copie de tel jeu », « propose-moi un plan », « quel stack ? ».

Distinct de :
- `enrichir-brain` (capture de connaissance dans le brain).

## Pré-requis

Mode build ou projet. Lit `AI/index/brain-index.json`, `Dev/` (Services, Patterns, Rules), et `Documentation/`. Sortie : un plan verbal, ou écrit dans `Projects/<projet>/` si l'utilisateur le demande.

## Appuis

- `AI/index/brain-index.json` — pour filtrer les candidats **sans lire 160 fichiers** (pitch, tags, categorie, galaxie).
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
   - proposer **2-3 candidats**, chacun affiché avec son **pitch d'une ligne** (champ `pitch:` de l'index) ;
   - laisser l'utilisateur trancher.
6. **Produire le plan / cahier des charges**, sourcé : chaque choix renvoie à sa fiche (`[[Dev/Services/...]]`, `[[Pattern - ...]]`, `[[Rules/...]]`) et porte la raison du choix + les alternatives écartées. Inclure les risques connus si un `Dev/REX/REX - <X>.md` existe.

## Format de sortie

```markdown
## Cadrage
- Archétype : <n°/nom> · Périmètre : perso/pro · Exécution : <où> · On-prem : <oui/non> · GPU : <oui/non>

## Stack proposé
### <Brique> : <Choix retenu>
**Pourquoi** : <2 lignes, depuis le pitch + la fiche>
**Écartés** : <Candidat B> (raison), <Candidat C> (raison)
**Source** : [[Dev/Services/<Choix>]]

## Patterns appliqués
- [[Pattern - <Y>]]

## Risques connus
- (depuis [[REX - <X>]] si présent)

## Contraintes pour l'IA de dev
- <règles issues de Dev/Rules/ + conventions perso>
```

## Anti-patterns

- Proposer un candidat absent de l'index (= choix non sourcé).
- Poser toutes les questions de la checklist quel que soit l'archétype.
- Oublier l'axe on-prem / air-gapped alors qu'il élimine des options.
- Recopier un pitch divergent : toujours réutiliser celui de l'index.

## Voir aussi

- `enrichir-brain` — si une brique utile manque dans le brain, l'ajouter d'abord.
- `AI/design/brain-v2.md` §2, §7.2, §8 — spec de référence.
