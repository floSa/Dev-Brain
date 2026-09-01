---
galaxie: meta
nom: lot-8-durcissement
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 8 — Durcissement du validateur

Effort : **une demi-session**. Dernier lot.

Prérequis : tous les autres lots faits, validateur au vert.

## Contexte

Le principe tenu depuis la v2 : **on ne durcit pas une règle que le vault viole encore.** Les
règles nouvelles entrent donc en avertissement, et ne passent en erreur dure qu'une fois le
contenu conforme. Ce lot fait ce passage, en dernier, quand le coût de la mise en conformité
est nul par construction.

## Les dix règles de la v3

Spec complète : [[AI/design/brain-v3|brain-v3]] §10.

| # | Règle | État visé |
|---|---|---|
| 1 | Réciprocité d'`alternatives:` et de `complements:` | dure |
| 2 | Le dossier d'une page concorde avec son `categorie:` | dure après lot 3 |
| 3 | Toute brique du dossier apparaît dans le hub du dossier | dure |
| 4 | Une brique isolée dans un dossier peuplé est signalée | **avertissement, définitif** |
| 5 | Toute cellule `Écarter si` contient un wikilink | dure |
| 6 | Réinjection du pitch dans `Alternatives` et `Compléments` | dure |
| 7 | Étiquettes fermées de `Ressources` et `Mise en œuvre` | dure |
| 8 | Pas de double citation d'une cible dans deux sections | dure |
| 9 | Le bandeau généré concorde avec le frontmatter | dure |
| 10 | `## Définition` ne recontient pas famille, licence ni maturité | dure après lot 6 |

La règle 4 reste un **avertissement pour toujours** : une brique peut légitimement n'avoir
aucune alternative. La signaler aide, l'interdire mentirait.

## Procédure

1. Lancer `check_brain.py` et relever le nombre de violations de chaque règle encore souple.
2. Pour chaque règle à **zéro violation** : passer en dure, immédiatement.
3. Pour chaque règle à violations résiduelles : les corriger si elles sont mécaniques, ou les
   écrire dans les *Remontées* du pilote si elles demandent un arbitrage. Ne pas durcir avant.
4. Rebrancher le hook `Stop` — l'audit axe 3 avait mesuré qu'il n'avait **jamais tourné** et
   ne pouvait pas tourner : aucun `settings.json` versionné, chemin de vault faux en dur dans
   `session_to_devbrain.py`. Vérifier que les deux causes sont levées.
5. Mettre à jour le tableau d'avancement du pilote et clore la migration.

## Critères d'acceptation

- [ ] Chaque règle est soit dure, soit souple avec un motif écrit.
- [ ] Aucune exception ajoutée au validateur pour faire passer une règle.
- [ ] Le hook `Stop` tourne réellement — vérifié en fin de session, pas supposé.
- [ ] `AI/design/brain-v2.md` porte une mention en tête renvoyant vers la v3.
- [ ] Le pilote est à jour et la migration close.

## Interdictions

- Ne pas durcir une règle avec des violations résiduelles, même peu nombreuses. Une règle dure
  qui échoue au quotidien finit désactivée, et on perd les dix.
- Ne pas supprimer `AI/design/brain-v2.md` : il documente les arbitrages de la v2 qui restent
  valides, notamment les deux axes `categorie:` × `famille:` et la convention de réinjection
  du pitch.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md §10 puis AI/migration/lot-8-durcissement.md.

Mesure les violations de chaque règle encore souple, durcis uniquement celles à zéro
violation, et montre-moi la liste de ce qui reste avant de conclure.

Vérifie que le hook Stop tourne réellement, ne te contente pas de le déclarer.
```
