---
role: brique
nom: Task
alias: [taskfile, go-task, go-task/task, Taskfile.yml]
pitch: "Lanceur de commandes de projet (MIT, Go) qui lit un fichier `Taskfile.yml` : tâches, dépendances entre tâches, variables, vérification des fichiers sources pour ne refaire que ce qui a changé, inclusion de Taskfiles venus d'une URL ou d'un dépôt — mais la syntaxe est du YAML avec gabarits, plus lourde que celle d'un justfile."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[just]]"]
complements: []
tags: [task-runner]
url_docs: https://taskfile.dev
url_repo: https://github.com/go-task/task
---

# Task

<!-- AUTO:BANDEAU:START -->
> Lanceur de commandes de projet (MIT, Go) qui lit un fichier `Taskfile.yml` : tâches, dépendances entre tâches, variables, vérification des fichiers sources pour ne refaire que ce qui a changé, inclusion de Taskfiles venus d'une URL ou d'un dépôt — mais la syntaxe est du YAML avec gabarits, plus lourde que celle d'un justfile.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande (`task`) qui remplace le `Makefile` par un fichier YAML, `Taskfile.yml`, que toute l'équipe sait lire. Chaque **tâche** a une description, des alias, des commandes (`cmds`), des dépendances (`deps`), des conditions préalables (`preconditions`, avec un message d'erreur) et des variables. `task --list` affiche les tâches du projet, `task build` en lance une. Le site le présente comme « un outil de build rapide et multiplateforme inspiré de Make » : même fichier sous Linux, macOS et Windows, en local comme en CI, avec un suivi des fichiers `sources` et générés pour **sauter le travail déjà à jour**, et des Taskfiles distants inclus depuis une URL ou un dépôt git pour partager des flux entre projets. Un binaire Go sans runtime.

Il tient le rôle de [[just]] : un point d'entrée commun (`task test`, `task lint`, `task up`) que l'humain, la CI et un agent appellent de la même façon. Version 3.54.0 du 2026-10-01, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07. Le site publie aussi une carte de la documentation pour les agents (`/llms.txt`).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un fichier de tâches en YAML, lisible par des collègues qui n'écrivent pas de Makefile | Une syntaxe courte, proche de make, avec chargement de `.env` : [[just]] |
| Ne refaire que ce qui a changé : `sources` et fichiers générés servent de test de fraîcheur | Un gestionnaire d'outils et de versions qui porte aussi des tâches : [[mise]] |
| Partager des tâches entre dépôts par inclusion d'un Taskfile distant | Tout ce qui doit tourner sur un poste sans le binaire : il faut l'installer (brew, winget, scoop, npm, apt, dnf, apk…) |
| Le même point d'entrée pour l'humain, la CI et l'agent de code, listé par `task --list` | Rien d'écrit en YAML : les gabarits `{{.VAR}}` dans les commandes se lisent moins bien qu'une recette de justfile |

## Mise en œuvre

- Installation — Homebrew, winget, Scoop, npm, apt, dnf, apk et d'autres ; une page du site liste tous les modes
- Point d'entrée — créer `Taskfile.yml` (avec `version: '3'`), puis `task --list` et `task <nom>` ; des variables se passent en ligne de commande (`task b APP=demo`)
- Prérequis — aucun pour le binaire
- Exécution — sur le poste ou en CI ; rien à héberger
- Coût — gratuit sous licence MIT ; des parrainages financent le projet

## Écosystème

### Alternatives

- [[just]] — Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre recettes et chargement de `.env` — mais un lanceur seulement, pas un système de build. — là où Task lit du YAML avec suivi des fichiers, just lit des recettes courtes dans un justfile.
- voisin : [[mise]] — gestionnaire d'outils et de versions, qui porte aussi un lanceur de tâches.

## Ressources

- Documentation — https://taskfile.dev
- Dépôt — https://github.com/go-task/task

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Fichiers de contexte pour agents]] — le point d'entrée que l'agent doit connaître
- [[Outils de développement]] — le hub du domaine
