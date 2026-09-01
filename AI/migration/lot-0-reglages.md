---
galaxie: meta
nom: lot-0-reglages
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 0 — Réglages Obsidian

Effort : **15 minutes**. Aucune page modifiée. Entièrement réversible.

C'est le seul lot qui améliore l'usage **avant** toute refonte. Il peut tourner tout de suite,
même si la spec n'est pas validée : rien de ce qu'il fait ne présume de la v3.

## Contexte

Deux mesures du 2026-09-04 expliquent l'essentiel de la gêne à la navigation.

**Le graphe est écrasé par un artefact.** `AI/index/liens.md` porte **10 335 wikilinks** et
n'est pas masqué du graphe. Les 682 pages du vault, elles, portent 8 009 liens au total. Ce
fichier généré crée donc à lui seul plus d'arêtes que tout le contenu écrit à la main : dans
le graphe, tout est à un saut de tout, et aucune structure n'est lisible.

**La définition n'est jamais visible.** Les fiches portent 18 propriétés (médiane et maximum),
qu'Obsidian rend en panneau vertical avant le titre. Sur un écran de portable, le corps de la
page commence sous la ligne de flottaison.

## Périmètre

Deux fichiers de configuration. **Aucune page de contenu.**

- `.obsidian/app.json` — champ `userIgnoreFilters`
- le réglage d'éditeur, par l'interface

## Procédure

### 1. Masquer l'index généré du graphe

Ajouter `"AI/index/"` au tableau `userIgnoreFilters` de `.obsidian/app.json`. Le tableau
contient déjà `AI/scripts/`, `AI/design/`, `Templates/` et les fichiers racine — `AI/index/`
manquait, alors que c'est le dossier qui pèse le plus lourd dans le graphe.

Vérification : rouvrir le graphe. `liens.md` et `brain-index.md` doivent avoir disparu, et les
grappes par domaine doivent devenir visibles.

### 2. Masquer le panneau de propriétés

Réglages → Éditeur → **Propriétés dans le document** → **Masqué**.

Les propriétés restent accessibles par la barre latérale, restent éditables, et restent lues
par tous les scripts. Seul l'affichage en tête de page disparaît.

Vérification : ouvrir `Dev/Services/Faker.md`. Le titre doit être la première chose visible.

### 3. Tester la variante « comparatif en un seul fichier »

Ouvrir une note de brouillon, y écrire un bloc de code contenant la requête d'un comparatif
existant (copier le contenu de `Dev/Patterns/Comparatif - Bases vectorielles.base`), en
essayant l'identifiant de bloc `base`. Si le tableau s'affiche, le noter dans les *Remontées*
du pilote : le lot 5 supprimera alors 47 fichiers au lieu de les conserver.

Supprimer la note de brouillon ensuite.

## Critères d'acceptation

- [ ] Le graphe n'affiche plus `liens.md` ni `brain-index.md`.
- [ ] Le titre d'une fiche est la première chose visible à l'ouverture.
- [ ] Le résultat du test de bloc de code est écrit dans les *Remontées* du pilote.
- [ ] `git diff` ne montre que `.obsidian/app.json`.

## Interdictions

- Ne modifier aucune page de contenu.
- Ne pas toucher `colorGroups` de `graph.json` — les couleurs par `role:` viennent au lot 2,
  quand le champ existera.
- Ne pas lancer les scripts de génération.

## Prompt à coller dans une conversation neuve

```
Lis AI/migration/lot-0-reglages.md et applique-le intégralement.

Périmètre strict : les deux réglages Obsidian décrits, plus le test de la variante
comparatif. Aucune page de contenu ne doit être modifiée.

À la fin, montre-moi git diff avant de committer, et reporte le résultat du test
dans la section Remontées de AI/migration/README.md.
```
