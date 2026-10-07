---
role: brique
nom: Commitizen
alias: [commitizen, cz, commitizen-tools/commitizen]
pitch: "Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` — mais tout repose sur des messages de commit conformes, que seul le hook de validation impose."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[git-cliff]]", "[[release-please]]"]
complements: []
tags: [changelog, version-control, git-hooks]
url_docs: https://commitizen-tools.github.io/commitizen/
url_repo: https://github.com/commitizen-tools/commitizen
---

# Commitizen

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande, écrit en Python, qui fait tenir ensemble trois gestes autour du commit. `cz commit` pose des questions et compose un message au format [Conventional Commits](https://www.conventionalcommits.org) (la convention par défaut, remplaçable par des règles et modèles propres). `cz bump` lit l'historique depuis le dernier tag, en déduit la prochaine version selon [SemVer](https://semver.org), met à jour les fichiers qui portent le numéro, **crée le tag git** et, si `update_changelog_on_bump` est activé, met à jour le changelog au format [Keep a Changelog](https://keepachangelog.com). `cz changelog` produit le journal seul, `cz check` vérifie un message ou une série de commits, `cz init` écrit la configuration. Une règle de validation se branche comme hook `commit-msg` de [[pre-commit]]. Version 4.19.2 du 2026-10-07, licence MIT lue dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un projet Python, déjà dans Git, où un seul outil doit guider les messages, numéroter les versions et tenir le changelog | Un dépôt qui ne peut pas imposer la convention de commits : sans messages conformes, le numéro calculé est faux. Le hook `commit-msg` la fait respecter, à condition d'être installé sur chaque poste |
| Faire respecter la convention par un hook (`commit-msg` via [[pre-commit]]) plutôt que par une revue | Un changelog riche, groupé et modelé : [[git-cliff]] se pilote par un modèle de changelog complet (documentation « Templating ») et ne fait que le journal |
| Une release lancée à la main, par une commande, sur le poste ou en CI interne ([[Forgejo]], [[GitLab CE]]) | Une release proposée par une pull request et un historique squash : [[release-please]], sur GitHub |
| Un format de version autre que SemVer (le schéma de version et le fournisseur de version se règlent) | Un projet sans Python sur le poste : Commitizen demande Python 3.10 ou plus et Git 1.8.5.2 ou plus |

## Mise en œuvre

- Installation — `uv tool install commitizen` ou `pipx install commitizen` (voie recommandée par le README), `brew install commitizen`, ou comme dépendance de développement du projet
- Point d'entrée — `cz init`, puis `cz commit` (ou `cz c`) à la place de `git commit`, et `cz bump` à la release
- Prérequis — Python 3.10+, Git 1.8.5.2+
- Exécution — sur le poste, ou en CI : `cz changelog --dry-run "$(cz version -p)"` prépare des notes de version pour un message d'équipe
- Coût — gratuit sous licence MIT ; v4.19.2 du 2026-10-07, dépôt poussé le jour même

## Écosystème

### Alternatives

- [[git-cliff]] — Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas. — Commitizen fait en plus le commit guidé, le tag et la mise à jour des fichiers de version.
- [[release-please]] — Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets. — Commitizen release à la demande, depuis le poste ; release-please passe par une pull request.
- voisin : python-semantic-release — même rôle en Python (version et changelog depuis les commits), cité en texte simple, non fiché dans le brain.

## Ressources

- Documentation — https://commitizen-tools.github.io/commitizen/
- Dépôt — https://github.com/commitizen-tools/commitizen

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Commits conventionnels, versions et changelog]] — les trois conventions (Conventional Commits, SemVer, Keep a Changelog) et leur usage avec un agent
- [[Comparatif - Versions et changelog]] — ce qui départage Commitizen, git-cliff et release-please
- [[Outils de développement]] — le hub du domaine
