---
role: brique
nom: mise
alias: [mise-en-place, jdx/mise]
pitch: "Outil en ligne de commande (MIT, Rust) qui installe les outils de développement d'un projet (Node.js, Python, Go et des centaines d'autres), fixe ses variables d'environnement et lance ses tâches depuis un seul `mise.toml` — mais une version demandée comme « 24 » suit la série : il faut une épingle exacte ou un fichier de verrou pour que toute l'équipe ait la même."
categorie: devtools/paquet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[just]]"]
complements: []
tags: [task-runner, reproducibility, package-manager]
url_docs: https://mise.jdx.dev
url_repo: https://github.com/jdx/mise
---

# mise

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, Rust) qui installe les outils de développement d'un projet (Node.js, Python, Go et des centaines d'autres), fixe ses variables d'environnement et lance ses tâches depuis un seul `mise.toml` — mais une version demandée comme « 24 » suit la série : il faut une épingle exacte ou un fichier de verrou pour que toute l'équipe ait la même.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui gère trois choses du poste de développement et les range dans un seul fichier, `mise.toml`, versionné avec le projet. Les **outils** : Node.js, Python, Go et des centaines d'autres, avec une version par projet. Les **variables d'environnement** du projet, y compris le chargement de fichiers `.env`. Les **tâches** : des commandes nommées, lancées avec les outils et l'environnement qu'elles demandent. Une partie « bootstrap » déclare aussi la préparation de la machine : paquets système, fichiers de configuration personnels, services. Le README insiste : on utilise les parties qu'on veut, à partir d'un seul outil ou d'une seule tâche. L'activation dans le shell est facultative : `mise exec node@24 -- node --version` installe l'outil au besoin et le lance sans toucher à la configuration, et `mise run` installe ce qui manque avant d'exécuter une tâche. Version 2026.10.3 du 2026-10-05, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un projet qui mêle plusieurs langages (Python et Node.js, par exemple) et veut un seul fichier pour la chaîne d'outils, partagé avec la CI | Un projet purement Python : [[uv]] installe déjà les versions de Python, les dépendances et les outils isolés, sans second outil |
| Une même commande de tâche sur le poste et en CI, avec les bonnes versions chargées d'office | Seulement une liste de commandes à lancer : [[just]] suffit et ne touche pas aux versions d'outils |
| Épingler les outils par version exacte ou par fichier de verrou, pour que l'équipe et la CI aient les mêmes | Une version demandée sans épingle (« 24 ») : elle suit la série et change d'une machine à l'autre, le README le dit |
| Préparer un poste neuf par une déclaration (outils, paquets système, services) plutôt que par un script | Un environnement totalement isolé du réseau : l'installation d'un outil télécharge sa version, il faut un miroir (non vérifié ici) |

## Mise en œuvre

- Installation — `curl https://mise.run | sh` (macOS, Linux), `winget install jdx.mise` (Windows), ou les paquets des distributions (guide d'installation de la documentation)
- Point d'entrée — `mise.toml` à la racine : `[tools]` (`node = "24"`), `[env]`, `[tasks.<nom>]` ; `mise use python@3.14` ajoute un outil, `mise install` installe ceux d'un projet existant, `mise run <tâche>` lance une tâche, `mise tasks ls` les liste
- Prérequis — aucun runtime à fournir : un binaire unique ; l'activation du shell (`eval "$(mise activate bash)"`) est facultative
- Exécution — sur le poste et en CI ; les tâches se déclarent en TOML ou en scripts dans `mise-tasks/`, avec des dépendances (les prérequis peuvent s'exécuter en parallèle) et des modèles de tâches
- Coût — gratuit sous licence MIT ; versions calendaires (`2026.10.3`)

## Écosystème

### Alternatives

- [[just]] — Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre recettes et chargement de `.env` — mais un lanceur seulement, pas un système de build. — pour la seule partie « tâches » ; il ne gère ni outils ni versions.
- voisin : [[uv]] — gestionnaire de paquets et de projets Python, qui télécharge et installe aussi les versions de Python ; recouvre mise sur le seul périmètre Python.

## Ressources

- Documentation — https://mise.jdx.dev
- Dépôt — https://github.com/jdx/mise

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Packaging Python et environnements reproductibles]] — épingler les versions pour reproduire un environnement
- [[Gestion de projet]] — le sous-domaine où vit son voisin [[just]]
