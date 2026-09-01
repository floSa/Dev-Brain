---
galaxie: meta
nom: lot-4-notions
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 4 — Recatégorisation des 205 notions

Effort : **deux à trois sessions**, par lots de domaine. C'est le **seul poste de travail non
mécanique** de toute la migration.

Prérequis : lot 3 fait pour le domaine concerné.

## Contexte

Les deux galaxies utilisent deux vocabulaires pour le même territoire : **94 sous-domaines**
côté Dev, **11** côté Wiki. En fusionnant l'arbre :

| Situation | Nombre |
|---|---|
| Notions qui tombent directement dans un sous-dossier existant | 89 |
| Notions qui tombent sur le bon domaine mais **sans sous-domaine** | 187 |
| Notions dont le domaine lui-même reste à déterminer | 18 |

Sans ce lot, `Machine Learning/` porterait 67 notions à plat et `LLM/` 57 — exactement le tas
que la v3 cherche à supprimer.

Liste nominative, avec cases à cocher : [[AI/design/v3-arborescence|v3-arborescence]],
sections *À arbitrer* de chaque domaine et *Hors arbre*.

## Périmètre

- Le champ `categorie:` des 205 notions listées, et leur emplacement.
- Le vocabulaire de `Documentation/general/taxonomie.md`, à **étendre** : le vocabulaire Dev
  ne couvre pas les mathématiques ni les statistiques théoriques, qui portent à elles seules
  63 notions.

**Hors périmètre** : le corps des notions, les briques, les comparatifs.

## Procédure

### Par domaine, dans cet ordre

`math` (26) et `stats` (37) d'abord — ce sont eux qui exigent de créer du vocabulaire, et il
vaut mieux le faire à froid. Puis `llm` (57), puis `ml` (67). Les 18 sans domaine en dernier,
une fois que le vocabulaire final est connu.

### Pour chaque notion

1. Lire la page — son titre, son `## Aperçu`, ses tags, ses liens sortants.
2. Dériver le sous-domaine par l'arbre de décision de `taxonomie.md`, **pas à l'intuition**.
3. Si aucune valeur existante ne convient : **proposer** une valeur nouvelle, ne pas
   l'inventer seule. Les propositions sont regroupées et soumises à floSa par lot, pas une
   par une.
4. Appliquer la règle de promotion à 5 pages : un sous-domaine qui atteint le seuil devient un
   dossier, sinon la notion reste au niveau du domaine.

### Les 18 sans domaine

La plupart sont en fait évidentes une fois posée la question « de quoi ça parle » :
`ORM` → `database/orm`, `Migrations de schéma` → `database/migration`,
`Web scraping` → `data/scraping`, `Notebooks-as-code` → `devtools/notebook`,
`Index ANN — internes` → `database/vecteur`. Les proposer groupées, en une seule question.

Les notions de sécurité IA (`Prompt injection`, `Jailbreaking and defenses`, `Guardrails`)
n'ont pas de domaine dans le vocabulaire actuel : c'est une **vraie** décision, à remonter.

## Critères d'acceptation

- [ ] Aucune notion ne reste sur une `categorie: concept/*`.
- [ ] Toute valeur nouvelle de `categorie:` est écrite dans `taxonomie.md` avec sa frontière,
      et son libellé de dossier est ajouté à `DOM_LABEL` ou `SUB_LABEL`.
- [ ] Chaque notion est dans le dossier que sa catégorie implique.
- [ ] Les cases de `v3-arborescence.md` sont cochées au fur et à mesure.
- [ ] `check_brain.py` au vert.

## Interdictions

- **Ne jamais inventer une valeur de catégorie en silence.** Une valeur hors vocabulaire est
  une faute ; une proposition explicite est le comportement attendu.
- Ne pas réécrire le corps d'une notion. Ce lot range, il n'édite pas.
- Ne pas traiter plus d'un domaine par conversation — le contexte sature et la qualité de
  l'arbitrage tombe sans signal.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md, AI/design/v3-arborescence.md puis
AI/migration/lot-4-notions.md.

Traite le domaine <NOM DU DOMAINE> uniquement.

Pour chaque notion, dérive le sous-domaine par l'arbre de décision de
Documentation/general/taxonomie.md. Regroupe tes propositions de valeurs nouvelles
et pose-les-moi en une fois avant d'écrire quoi que ce soit.

Clôture avec le skill cloturer-brain.
```
