---
galaxie: meta
nom: lot-6-gabarit
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 6 — Conversion des fiches au nouveau gabarit

Effort : **25 fiches par conversation au maximum**, 336 fiches au total — soit une quinzaine de
conversations. C'est le lot le plus long, et le seul qui touche au texte.

Mesure du 2026-09-04 : 64 lignes et 407 mots médians par fiche, lues *et* réécrites, soit 3 à
4 k tokens chacune. Au-delà de 25, la conversation sature avant la fin du domaine.

Prérequis : lots 2 et 3 faits. **Jamais en parallèle d'un autre lot** — le 3 déplace les fiches
que le 6 réécrit.

## Contexte

Le gabarit actuel est suivi à 100 % : 336 fiches sur 336 portent `Pourquoi`, `Quand
l'utiliser`, `Quand NE PAS l'utiliser`, `Pièges` et `Liens`. Ce n'est donc pas un problème de
discipline, c'est le gabarit lui-même qui est en cause. Sept sections pour 407 mots médians,
soit 58 mots par section : les titres pèsent plus que leur contenu.

Trois mesures qui commandent les changements :

| Constat | Mesure |
|---|---|
| `Pièges` ne contient pas de retours d'expérience | 336 sections remplies, **1 seule** avec une entrée datée |
| `Déploiement & coût` reformule le frontmatter | 84,5 % contiennent « gratuit » (= `licence_type`), 4,4 % mentionnent une plateforme |
| `Liens` fait trois métiers à la fois | sur la page Faker, Mimesis apparaît en `Alternatives` **et** en `Liens` |

Le gabarit cible et le raisonnement complet : [[AI/design/brain-v3|brain-v3]] §6.

## Périmètre

- Le corps des 336 fiches `role: brique`.
- Le bandeau généré des 299 `role: notion` — leur corps, lui, n'est **pas** touché.
- Le nouveau script `build_bandeau.py`.

## Le principe, en une phrase

**Une ligne, une étiquette, une idée.** Aucune prose hors de `## Définition`. C'est le format
de la section `## Alternatives`, la seule que l'usage a validée, généralisé à toute la page.

## Procédure

### 1. Écrire `build_bandeau.py`

Il compose le bandeau de chaque page depuis son frontmatter, dans une zone `<!-- AUTO -->` :
`Nature` (dérivé de `famille:` + `langage:`), `Licence`, `Exécution`, `Maturité`. Idempotent,
relançable, jamais édité à la main.

### 2. Convertir, domaine par domaine

Correspondance de départ, à ne pas appliquer aveuglément :

| Ancienne section | Devient |
|---|---|
| `## Pourquoi` | `## Définition` — prose, 4 à 6 lignes, **sans redire le bandeau** |
| `## Quand l'utiliser` + `## Quand NE PAS l'utiliser` | un tableau `Prendre si / Écarter si` |
| `## Déploiement & coût` | `## Mise en œuvre`, cinq étiquettes fixes |
| `## Pièges` | **dissoute** — voir ci-dessous |
| `## Alternatives` | `## Écosystème` → `### Alternatives` + `### Compléments` |
| `## Liens` | scindée en `## Ressources` (externe, étiqueté) et `## Voir aussi` (interne) |

### 3. Dissoudre `Pièges` correctement

C'est l'étape qui demande du jugement, et elle ne se scripte pas. Chaque puce part vers l'un
de trois endroits :

- **une limite de conception qui oriente un choix** → colonne `Écarter si`, avec le lien vers
  l'alternative. Exemple mesuré : « Faker tire les champs indépendamment, email et nom ne
  correspondent pas » n'est pas un piège, c'est le critère qui fait choisir SDV ;
- **une limite qui n'oriente rien mais qu'il faut savoir** → `## Définition` ;
- **un retour d'expérience daté** → section `## Retours`, qui n'existe **que** dans ce cas.
  Une seule fiche du vault est concernée.

Aucune puce n'est supprimée sans avoir trouvé sa destination.

### 4. Remplir `complements:`

Le champ a été ouvert vide au lot 2. Le remplir ici, quand le voisinage de la fiche est sous
les yeux : pgvector et Postgres, Faker et pandas. Réciprocité obligatoire.

## Critères d'acceptation

- [ ] Aucune fiche ne porte plus `Pourquoi`, `Quand l'utiliser`, `Quand NE PAS l'utiliser`,
      `Déploiement & coût` ni `Pièges`.
- [ ] Chaque cellule `Écarter si` contient un wikilink.
- [ ] Chaque puce de `Ressources` porte une étiquette du vocabulaire fermé.
- [ ] `Mise en œuvre` porte ses cinq étiquettes.
- [ ] Aucune cible n'apparaît dans deux sections de la même page.
- [ ] `## Définition` ne recontient ni la famille, ni la licence, ni la maturité.
- [ ] `check_brain.py` au vert.

## Interdictions

- **Ne pas inventer de contenu.** Une cellule `Écarter si` qui n'a pas de source dans la fiche
  d'origine se laisse vide et se signale. Un tableau à moitié rempli honnêtement vaut mieux
  qu'un tableau complet inventé.
- Ne pas supprimer une puce de `Pièges` sans lui avoir trouvé une destination.
- Ne pas toucher au corps des notions.
- Ne pas traiter plus d'un domaine par conversation.

## Réserve connue

331 puces `Liens` sur 336 portent déjà une étiquette, mais **286 valent « Doc »**. Le vault ne
contient presque aucun tutoriel, article ou papier. Typer les liens ne les crée pas : la
section `## Ressources` sera souvent réduite à deux lignes, et c'est normal. Les enrichir est
un chantier distinct, à ouvrir plus tard.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md puis AI/migration/lot-6-gabarit.md.

Écris d'abord AI/scripts/build_bandeau.py, puis convertis les fiches du domaine
<NOM DU DOMAINE> uniquement.

Montre-moi trois fiches converties — une librairie, une plateforme, une application
à interface — avant de dérouler le reste du domaine.

Traite au maximum 25 fiches. Termine en me listant nommément celles qui restent dans
le domaine, pour que la conversation suivante reprenne exactement là.

N'invente aucun contenu : une cellule sans source dans la fiche d'origine reste vide
et tu me la signales. Clôture avec le skill cloturer-brain.
```
