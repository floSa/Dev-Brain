---
role: brique
nom: just
alias: [casey/just, justfile, Just command runner]
pitch: "Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre recettes et chargement de `.env` — mais un lanceur seulement, pas un système de build."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[mise]]", "[[Task]]"]
complements: []
tags: [task-runner]
url_docs: https://just.systems/man/en/
url_repo: https://github.com/casey/just
---

# just

<!-- AUTO:BANDEAU:START -->
> Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre recettes et chargement de `.env` — mais un lanceur seulement, pas un système de build.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Lanceur de commandes de projet : les commandes qu'on retape sans cesse (tests, formatage, build, lancement) s'écrivent une fois, sous le nom de **recettes**, dans un fichier `justfile` à la racine, et se lancent par `just <recette>`. La syntaxe s'inspire de `make`, sans ses pièges : le README précise que `just` est un lanceur de commandes et non un système de build, qu'il n'a pas besoin de `.PHONY`, qu'il signale les erreurs de syntaxe avec leur contexte, résout statiquement les recettes inconnues et les dépendances circulaires avant d'exécuter quoi que ce soit, et se lance depuis n'importe quel sous-répertoire du projet. Une recette accepte des paramètres, des options et des drapeaux ; elle peut s'écrire dans un autre langage (Python, Node.js) par une ligne *shebang*. Les fichiers `.env` se chargent, `just --list` énumère les recettes, et un `justfile` se découpe en modules et en imports. Version 1.58.0 du 2026-08-03, dépôt poussé le 2026-10-02. Licence CC0-1.0 (domaine public) lue dans le dépôt ; le README prend, depuis la 1.0, un engagement de compatibilité ascendante.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un point d'entrée unique des commandes du projet, lisible par un humain **et par un agent** : `just --list` donne l'inventaire, le `justfile` dit comment lancer les tests (cf. [[Fichiers de contexte pour agents]]) | Il faut aussi installer les bonnes versions de Node.js, de Python ou de Go : `just` lance des commandes et n'installe rien, c'est le rôle de [[mise]] |
| Remplacer un Makefile qu'on n'utilise que comme liste de commandes, sans les règles de dépendances de fichiers | Un graphe de build qui compare les dates de fichiers pour ne reconstruire que ce qui change : `just` n'est pas un système de build |
| Un seul binaire, sans dépendance sur Linux, macOS et Windows, utilisable en CI interne ([[Forgejo]], [[GitLab CE]], [[Woodpecker CI]]) | Des scripts qui doivent tourner sur une machine sans `sh` : le README demande alors de choisir un autre interpréteur par la directive `shell` |
| Des recettes avec paramètres, dépendances et variables d'environnement lues dans `.env` | Un seul script d'une dizaine de lignes : un fichier shell versionné suffit, sans outil de plus à installer |

## Mise en œuvre

- Installation — binaire précompilé, `cargo install just`, ou les paquets de la plupart des distributions et gestionnaires (le README les liste par système) ; une action GitHub et une image Docker existent
- Point d'entrée — le fichier `justfile` à la racine ; `just` lance la première recette, `just <recette>` une recette nommée, `just --list` les liste
- Prérequis — un interpréteur de commandes (`sh` par défaut, un autre se choisit)
- Exécution — sur le poste ou en CI ; complétion pour les principaux shells
- Coût — gratuit, domaine public (CC0-1.0)

## Écosystème

### Alternatives

- [[mise]] — Outil en ligne de commande (MIT, Rust) qui installe les outils de développement d'un projet (Node.js, Python, Go et des centaines d'autres), fixe ses variables d'environnement et lance ses tâches depuis un seul `mise.toml` — mais une version demandée comme « 24 » suit la série : il faut une épingle exacte ou un fichier de verrou pour que toute l'équipe ait la même. — ses tâches recouvrent les recettes de `just` ; `just` ne fait que les lancer, et ne gère ni outils ni versions.
- [[Task]] — Lanceur de commandes de projet (MIT, Go) qui lit un fichier `Taskfile.yml` : tâches, dépendances entre tâches, variables, vérification des fichiers sources pour ne refaire que ce qui a changé, inclusion de Taskfiles venus d'une URL ou d'un dépôt — mais la syntaxe est du YAML avec gabarits, plus lourde que celle d'un justfile. — là où just lit des recettes courtes dans un justfile, Task lit du YAML avec suivi des fichiers sources.
- voisin : Make, que just et Task remplacent pour ce seul usage.

## Ressources

- Documentation — https://just.systems/man/en/
- Dépôt — https://github.com/casey/just

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Cycle de vie d'un projet assisté par agent]] — le fil conducteur du sous-domaine
- [[Fichiers de contexte pour agents]] — y citer les commandes d'un `justfile`
- [[Outils de développement]] — le hub du domaine
