---
galaxie: meta
nom: lot-3-arborescence
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 3 — Déplacement des fichiers vers l'arbre unique

Effort : **une session par groupe de domaines**. C'est le lot le plus visible et le plus
mécanique. Il doit tourner **seul** : aucun autre lot ne touche des fichiers en même temps.

Prérequis : lot 2 fait, validateur au vert.

## Contexte

`Dev/Services` porte 297 fichiers à plat, `Wiki/Concepts` 299. Aucun sous-dossier nulle part.
Le volet fichiers d'Obsidian est donc inutilisable pour se repérer, et le seul découpage
existant — `Services/` contre `Outils/` — a été mesuré non discriminant.

La v3 remplace les deux galaxies par **un arbre de domaines**. La nature de la page, elle, est
déjà portée par `role:` depuis le lot 2.

Arbre complet, page par page : [[AI/design/v3-arborescence|v3-arborescence]].

## Périmètre

- Déplacement de 682 fichiers par `git mv`.
- Création des dossiers et des pages `hub`.
- Suppression de `MOC/` (39 pages), absorbé par les hubs.
- `build_mocs.py`, qui cesse de générer `MOC/` et génère les zones `AUTO` des hubs.

**Hors périmètre** : le corps des fiches, la recatégorisation des notions, les comparatifs.

## Règle de rangement — mécanique, aucun arbitrage

1. Un dossier par domaine, nommé avec son libellé français (table `DOM_LABEL` de la spec,
   reprise de `CAT_LABEL` de `build_mocs.py`).
2. Un sous-dossier dès qu'un sous-domaine atteint **5 pages**. En-dessous, les pages restent au
   niveau du domaine.
3. Le chemin se **dérive** de `categorie:`. Personne ne choisit un dossier.
4. Tout dossier porte une page à son nom, `role: hub`.

## Procédure

### Ordre des domaines

Commencer par **Bases de données** : 47 pages, quatre sous-dossiers propres, **zéro notion à
arbitrer**. C'est le domaine qui valide la méthode au moindre risque.

Ensuite, par taille croissante de difficulté : `Data & pipelines`, `Outils de développement`,
les 15 petits domaines, puis `LLM` et `Machine Learning` en dernier — ce sont eux qui portent
les notions non catégorisées, et le lot 4 devra repasser derrière.

### Pour chaque domaine

1. Créer l'arborescence du domaine et ses sous-dossiers.
2. `git mv` chaque page vers son dossier dérivé de `categorie:`.
3. Créer la page `hub` de chaque dossier créé, avec sa zone `<!-- AUTO -->` vide.
4. Fusionner la notion chapeau homonyme dans le hub quand elle existe — cas
   `Wiki/Concepts/Bases de données.md` et `MOC/Categories/Bases de données.md`, qui sont la
   **seule collision de nom du vault** et listent les mêmes briques. Le corps écrit à la main
   de la notion devient le corps du hub ; la liste générée devient la zone `AUTO`.
5. Relancer `build_mocs.py` pour remplir les zones `AUTO`.
6. Vérifier qu'aucun wikilink n'est cassé.

### Les wikilinks

4 333 liens du vault sont **nus** (`[[Page]]`) et 3 676 **qualifiés** (`[[Dossier/Page|X]]`).
Les qualifiés portent l'ancien chemin et cassent au déplacement.

Deux options, à trancher au début du lot et à appliquer partout :

- **Tout passer en nu.** Obsidian résout par nom de fichier ; après la fusion de la seule
  collision (étape 4), aucune ambiguïté ne subsiste. Le déplacement devient indolore, et les
  déplacements futurs aussi.
- **Tout requalifier** au nouveau chemin. Plus explicite hors Obsidian, mais chaque
  déplacement ultérieur rouvre le chantier.

Recommandation : **le nu**, précisément parce que la collision qui le rendait dangereux
disparaît à l'étape 4. À confirmer par floSa avant la première conversion.

## Critères d'acceptation

- [ ] `Dev/`, `Wiki/` et `MOC/` n'existent plus.
- [ ] Le chemin de chaque page concorde avec son `categorie:`.
- [ ] Chaque dossier porte une page `role: hub` à son nom.
- [ ] Aucun wikilink cassé — vérifié par `check_brain.py`.
- [ ] `build_mocs.py` remplit les zones `AUTO` des hubs et ne crée plus `MOC/`.
- [ ] Aucun fichier perdu : le compte avant et après est identique, hors fusions documentées.

## Interdictions

- **Aucun `rm`.** Un `git mv` déplace, il ne supprime pas. Les seules disparitions autorisées
  sont les fusions de l'étape 4, et chacune s'écrit dans les *Remontées*.
- Ne pas modifier le corps des fiches, sauf le corps du hub issu de la fusion.
- Ne pas recatégoriser une notion — c'est le lot 4. Une notion sans sous-domaine reste au
  niveau de son domaine, en attente.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md, AI/design/v3-arborescence.md puis
AI/migration/lot-3-arborescence.md.

Applique le lot 3 pour le domaine « Bases de données » uniquement, et arrête-toi
là pour que je valide la méthode avant que tu déroules les autres domaines.

Aucun rm : uniquement git mv. Clôture avec le skill cloturer-brain.
```
