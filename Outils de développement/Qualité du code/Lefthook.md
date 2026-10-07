---
role: brique
nom: Lefthook
alias: [lefthook, evilmartians/lefthook]
pitch: "Gestionnaire de crochets git (MIT, Go) distribué en binaire unique qui lit un fichier `lefthook.yml`, lance les commandes en parallèle et choisit les fichiers à leur passer — mais il ne fournit pas de bibliothèque de contrôles prête à l'emploi : chaque commande est à écrire ou à appeler depuis le projet."
categorie: devtools/qualite
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[pre-commit]]"]
complements: []
tags: [git-hooks]
url_docs: https://lefthook.dev/
url_repo: https://github.com/evilmartians/lefthook
---

# Lefthook

<!-- AUTO:BANDEAU:START -->
> Gestionnaire de crochets git (MIT, Go) distribué en binaire unique qui lit un fichier `lefthook.yml`, lance les commandes en parallèle et choisit les fichiers à leur passer — mais il ne fournit pas de bibliothèque de contrôles prête à l'emploi : chaque commande est à écrire ou à appeler depuis le projet.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Gestionnaire de **crochets git** (les petits programmes que git lance avant un commit ou une poussée) pour des projets Node.js, Ruby, Python ou autres. Un fichier `lefthook.yml` à la racine liste, pour chaque crochet (`pre-commit`, `pre-push`…), les commandes à lancer ; `lefthook install` pose les crochets dans le dépôt. Il est écrit en Go, distribué en **un binaire sans dépendance**, et peut lancer les commandes **en parallèle** (`parallel: true`). Il contrôle les fichiers passés à chaque commande (liste personnalisée ou prédéfinie, d'après la documentation). Version 2.1.17 du 2026-10-05, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-06. Éditeur : Evil Martians.

**Différence avec pre-commit.** [[pre-commit]] est un cadre qui télécharge et isole des *hooks* publiés par d'autres dépôts, chacun dans son environnement. Lefthook, lui, lance les commandes déjà présentes sur la machine ou dans le projet : rien à télécharger, mais aucun catalogue de contrôles prêts.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des crochets rapides : exécution parallèle, et liste de fichiers maîtrisée par commande | Un catalogue de hooks maintenus par d'autres (Ruff, Gitleaks, formatage…) installés sans écrire de commande : [[pre-commit]] |
| Un projet qui n'est pas Python : le binaire existe par npm, gem, pipx, Go, Homebrew, apt, winget | L'équipe n'a pas de convention sur les outils installés : Lefthook suppose que les commandes sont présentes sur chaque poste |
| Pas d'environnement Python à installer sur une machine ou un conteneur de CI | Le projet utilise déjà pre-commit et s'en trouve bien : migrer n'apporte que la vitesse |
| Mêmes crochets pour des agents de code qui committent : le crochet les arrête comme un humain, cf. [[Revue, tests et définition de terminé avec un agent]] | Remplacer la CI : un crochet local se contourne, la CI reste le dernier filet |

## Mise en œuvre

- Installation — `npm install lefthook --save-dev`, `gem install lefthook`, `pipx install lefthook`, `go install github.com/evilmartians/lefthook/v2@latest`, ou Homebrew, apt, winget
- Point d'entrée — écrire `lefthook.yml`, puis `lefthook install` ; la documentation décrit `jobs`, les filtres de fichiers et les options
- Prérequis — aucun pour le binaire ; les commandes appelées doivent exister
- Exécution — sur le poste, au moment des commandes git ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent. — là où Lefthook lance des commandes locales en parallèle, pre-commit installe des hooks publiés, chacun isolé.

## Ressources

- Documentation — https://lefthook.dev/
- Dépôt — https://github.com/evilmartians/lefthook

## Voir aussi

- [[Qualité du code]] — le hub du sous-domaine
- [[Ruff]] — un contrôle typique à brancher sur un crochet
- [[Outils de développement]] — le hub du domaine
