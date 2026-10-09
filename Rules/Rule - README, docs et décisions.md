---
role: rule
domaine: docs
applicable: global
strictness: should
tags: [rule, documentation, adr]
---

# Rule — README, docs et décisions

## Principe

La documentation d'un projet tient en quatre endroits : un `README.md` pour qui arrive, un dossier `documentation/` pour le fond (cadrage, spécification, décisions), un `AGENTS.md` court pour l'agent de code, et des décisions consignées une par fichier au format MADR.

Ce qui se perd dans un projet n'est pas le code, c'est le pourquoi. Un fichier par décision le garde pour la personne ou l'agent qui reprend le projet six mois plus tard.

## MUST

- Écrire un `README.md` à la racine : ce que fait le projet, comment l'installer, le lancer et le tester.
- Ranger la documentation de fond dans `documentation/` : `cadrage.md`, `specification.md`, `decisions/`.
- Consigner chaque décision d'architecture dans un fichier `documentation/decisions/NNNN-titre.md`, au format MADR.
- Garder `AGENTS.md` court : commandes exactes, conventions qui s'écartent du standard, pièges. Ni résumé du README, ni arborescence.
- Mettre la documentation touchée à jour dans le même commit que le changement qu'elle décrit.
- Ne mettre aucun secret dans le `README.md`, `documentation/` ni `AGENTS.md` : ils sont versionnés.

## SHOULD

- Distinguer quatre types de pages (repères Diátaxis) : un tutoriel pour apprendre en faisant, un guide pratique pour une tâche, une référence pour consulter un fait, une explication pour comprendre le pourquoi. Ne pas les mêler dans une même page.
- Ouvrir le `README.md` par une phrase qui dit ce que fait le projet, puis la commande de démarrage rapide, avant tout détail.
- Écrire la documentation avec les outils du code : texte brut, relue en revue, publiée par la CI. [[MkDocs]] suffit pour un site ; [[mkdocstrings]] en tire la référence de l'API depuis les docstrings.
- Dessiner les schémas en texte ([[Mermaid]], [[D2]]) pour qu'ils se versionnent et se relisent en diff.
- Dans une décision, nommer les options écartées et la raison : c'est ce que l'ADR garde et que le code ne dit pas.
- Remplacer une décision par une nouvelle décision qui la cite, sans effacer l'ancienne.

## NICE-TO-HAVE

- Un fichier `documentation/glossaire.md` quand le projet a un vocabulaire métier (industrie, ESN, domaine du client).
- Un `CHANGELOG.md` rédigé pour le lecteur du client ([[Rule - Commits conventionnels et versions automatiques]]).
- Une vérification en CI des liens et du build de la documentation.

## Pour AGENTS.md

- Documentation de fond dans `documentation/` : cadrage, spécification, décisions.
- Une décision d'architecture = un fichier `documentation/decisions/NNNN-titre.md` au format MADR.
- Mettre à jour le `README.md` et `documentation/` dans le même commit que le changement.
- Garder ce fichier court : commandes, conventions, pièges. Aucun secret.

## Exemples

### Bon

```text
mon-projet/
├── README.md              # quoi, installer, lancer, tester
├── AGENTS.md              # court : commandes, conventions, pièges
└── documentation/
    ├── cadrage.md
    ├── specification.md
    └── decisions/
        ├── 0001-choix-de-la-base.md
        └── 0002-ordonnanceur.md
```

```markdown
# Utiliser Postgres plutôt que SQLite

## Context and Problem Statement
Plusieurs processus écrivent en parallèle.

## Considered Options
* SQLite
* Postgres

## Decision Outcome
Chosen option: « Postgres », parce que l'écriture concurrente est nécessaire.
```

### Mauvais

```text
mon-projet/
├── README.md      # « TODO »
├── notes.md       # décisions mêlées aux brouillons
└── AGENTS.md      # 900 lignes, recopie du README et de l'arborescence
```

## Exceptions

- Script jetable : un commentaire en tête du fichier tient lieu de `README.md`.
- Documentation imposée par le client (gabarit, format de livrable) : le gabarit du client prime pour le livrable ; `documentation/decisions/` reste le journal interne.

## Voir aussi

- [[MADR - le modèle de fiche]] — le gabarit des fichiers de décision
- [[ADR et design docs]] — la notion : ce qu'est un ADR et pourquoi
- [[Diátaxis et docs-as-code]] — les quatre types de pages et la documentation écrite comme du code
- [[Fichiers de contexte pour agents]] — ce qui va dans `AGENTS.md` et ce qui va ailleurs
- [[AGENTS.md - le format]] — la fiche du format
- [[Rule - Structure de projet]], [[Rule - Projet assisté par agent]]
- [[MkDocs]], [[mkdocstrings]], [[D2]] — les outils de documentation et de schéma
