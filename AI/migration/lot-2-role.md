---
galaxie: meta
nom: lot-2-role
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 2 — `role:` remplace `galaxie:` et `type:`, nettoyage du frontmatter

Effort : **une session**. 682 pages touchées au frontmatter, aucune au corps. Aucun fichier
déplacé.

Prérequis : la spec [[AI/design/brain-v3|brain-v3]] validée par floSa.

## Contexte

La v3 range sur deux axes : le **dossier** porte le domaine, le champ **`role:`** porte la
nature de la page. Ce lot pose le second axe, sans toucher au premier — donc sans déplacer un
seul fichier. Le vault reste utilisable et le graphe gagne ses couleurs définitives dès la fin
du lot.

Mesures qui justifient les suppressions de champs :

| Champ | Mesure au 2026-09-04 |
|---|---|
| `type:` | 57 fiches de nature identique réparties 34 `outil` / 23 `service`, sans discriminant. Il ne décrit que le dossier |
| `status:` | 272 fiches sur 336 sont `actif` + `production` ; 7 des 8 `abandonne` sont `deprecated`. Redondant avec `maturite` |
| `remplace_par:` | vide sur **297 fiches sur 297** |
| `hosted:` | `both` sur 82 fiches ; et **177 `paquet`** portent une valeur d'hébergement alors qu'une bibliothèque ne s'héberge pas |
| `scaling:` | `single-node` sur 212 fiches, valeur par défaut de tout ce qui n'est pas distribué |

## Périmètre

- Le frontmatter des 682 pages de `Dev/` et `Wiki/`.
- `.obsidian/graph.json` — groupes de couleur.
- Les six scripts qui lisent `galaxie` : `build_index.py`, `build_links.py`, `build_mocs.py`,
  `check_brain.py`, `query_index.py`, `sync_reservoir.py`.
- Les trois skills et les fichiers `CLAUDE*.md`, pour la cohérence du vocabulaire.

**Hors périmètre** : le corps des pages, l'emplacement des fichiers, `MOC/`.

## Procédure

### 1. Poser `role:`

Correspondance mécanique, aucun jugement :

| Origine | `role:` |
|---|---|
| `Dev/Services/*` et `Dev/Outils/*` | `brique` |
| `Wiki/Concepts/*` et `Wiki/Outils/*` | `notion` |
| `Dev/Patterns/Pattern - *.md` | `pattern` |
| `Dev/Rules/*` | `rule` |

Les comparatifs `.base` n'ont pas de frontmatter : ils prendront `role: comparatif` au lot 5,
quand ils deviendront des pages.

### 2. Supprimer les champs morts

`galaxie:`, `type:`, `status:`, `remplace_par:` sur toutes les pages concernées.

Avant de supprimer `status:`, **lister les fiches où il contredit `maturite:`** — l'audit axe 4
en avait relevé deux. Elles ne sont pas supprimées en silence : la valeur juste est reportée
dans `maturite:` et le cas est écrit dans les *Remontées* du pilote.

### 3. Corriger `hosted:` et `scaling:`

- `hosted: both` devient la liste `hosted: [self, managé]`.
- Les deux champs sont **retirés** des fiches dont `famille:` n'est pas `plateforme`, `saas`
  ou `application`. Environ 218 fiches.

### 4. Ajouter `complements:`

Champ vide sur toutes les fiches, symétrique d'`alternatives:`. Il sera rempli au fil de
l'eau — ce lot ne fait que l'ouvrir.

### 5. Adapter les scripts et le validateur

- Remplacer partout la lecture de `galaxie`/`type` par `role`.
- `check_brain.py` : nouvelle énumération fermée de `role:` ; `hosted` et `scaling` deviennent
  **conditionnels à `famille:`** ; suppression des règles portant sur les champs supprimés.
- Les gabarits de `Templates/` suivent.

### 6. Recolorer le graphe

Dans `.obsidian/graph.json`, remplacer les requêtes sur `galaxie` par des requêtes sur `role` :
`hub` orange, `notion` vert, `brique` bleu, `comparatif` rouge, `pattern` et `rule` gris.
Conserver les couleurs actuelles de Dev et Wiki pour `brique` et `notion` — floSa y est
habitué.

## Critères d'acceptation

- [ ] Aucune page ne porte plus `galaxie:`, `type:`, `status:` ni `remplace_par:`.
- [ ] Chaque page de `Dev/` et `Wiki/` porte un `role:` de l'énumération fermée.
- [ ] Aucun `hosted: both` ne subsiste.
- [ ] `hosted:` et `scaling:` n'existent que sur les familles `plateforme`, `saas`, `application`.
- [ ] `uv run AI/scripts/check_brain.py` au vert.
- [ ] `build_index.py`, `build_mocs.py`, `build_links.py` tournent sans erreur.
- [ ] Les contradictions `status`/`maturite` rencontrées sont dans les *Remontées*.

## Interdictions

- Ne déplacer aucun fichier — c'est le lot 3.
- Ne modifier aucun corps de page — c'est le lot 6.
- Ne pas ajouter d'exception au validateur pour le faire passer au vert.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md puis AI/migration/lot-2-role.md, et applique le lot 2
intégralement.

Périmètre strict : le frontmatter, les scripts, le validateur, les gabarits et les
couleurs du graphe. Aucun fichier déplacé, aucun corps de page modifié.

Travaille par script plutôt qu'à la main sur 682 pages, et montre-moi le script
avant de le lancer. Clôture avec le skill cloturer-brain.
```
