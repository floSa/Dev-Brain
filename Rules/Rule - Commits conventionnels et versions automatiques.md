---
role: rule
domaine: git
applicable: global
strictness: should
tags: [rule, git-hooks, changelog, version-control]
---

# Rule — Commits conventionnels et versions automatiques

## Principe

Les messages de commit suivent la grammaire des commits conventionnels, un contrôle avant commit les vérifie, et la prochaine version se calcule depuis eux au lieu de s'écrire à la main.

La grammaire est ce qui rend le calcul possible : `fix` donne un correctif, `feat` une nouvelle fonction, un changement incompatible un changement majeur. Sans contrôle mécanique, la convention se perd au troisième commit pressé.

## MUST

- Écrire chaque message sous la forme `type(scope): description`, avec `feat` et `fix` comme types qui comptent pour la version.
- Marquer un changement incompatible par `!` après le type, ou par un pied de page `BREAKING CHANGE:`.
- Faire vérifier le message par un hook `commit-msg` : un message non conforme est refusé.
- Lancer lint, format et types par un hook avant chaque commit (pre-commit ou Lefthook).
- Calculer la version depuis les commits (SemVer) au lieu de l'écrire à la main, et poser un tag à chaque livraison.
- Tenir un `CHANGELOG.md` par version, généré puis relu avant la livraison.

## SHOULD

- Choisir l'outil de version selon la forge. [[Commitizen]] guide la saisie, vérifie les messages (`cz check`) et calcule la version (`cz bump`). [[python-semantic-release]] calcule la version, tague et publie sur GitHub, GitLab, Gitea ou Bitbucket. [[release-please]] tient à jour une pull request de release, mais exige un jeton GitHub : à écarter sur une forge auto-hébergée.
- Générer le changelog avec [[git-cliff]] si le projet veut un gabarit à soi.
- Rejouer la vérification des messages en CI : un hook local se contourne, la CI non.
- Sur un poste sans réseau, préférer [[Lefthook]] (un binaire, des commandes locales) à [[pre-commit]], dont les dépôts de hooks et leurs paquets sont à miroiter.
- Une application ou un modèle de ML n'a pas d'API publique à déclarer : versionner le code par CalVer ou par SemVer d'API, et le modèle par un identifiant d'entraînement et de jeu de données.

## NICE-TO-HAVE

- Lister les scopes admis dans la configuration de l'outil, pour qu'un scope inventé soit refusé.
- Publier le changelog dans la fiche de release, rédigé pour le lecteur du client plutôt que pour l'équipe.

## Pour AGENTS.md

- Message de commit : commits conventionnels, `type(scope): description`. Le hook `commit-msg` refuse le reste.
- Changement incompatible : `!` après le type ou pied `BREAKING CHANGE:`.
- La version et le changelog se calculent depuis les commits : ne pas les éditer à la main.
- Un commit par sujet : un seul `feat` pour dix changements fausse la version.

## Exemples

### Bon

```text
feat(api)!: retirer l'endpoint /v1/predict

BREAKING CHANGE: remplacé par /v2/predict, voir la migration.
```

```yaml
# lefthook.yml : contrôle avant commit, message vérifié par Commitizen
pre-commit:
  commands:
    lint:
      run: uv run ruff check {staged_files}
commit-msg:
  commands:
    conventionnel:
      run: uv run cz check --commit-msg-file {1}
```

### Mauvais

```text
modifs diverses
```

```text
feat: un seul commit pour dix changements, dont deux incompatibles
```

## Exceptions

- Dépôt hérité sans convention : l'adopter à partir d'une date donnée, sans réécrire l'historique.
- Bibliothèque en `0.y.z` : le seuil majeur n'a pas de sens, mais la convention de message s'applique quand même.
- Livraison client à numéro imposé : le numéro suit le contrat, le changelog garde la grammaire.

## Voir aussi

- [[Commits conventionnels, versions et changelog]] — la notion : Conventional Commits, SemVer, Keep a Changelog, CalVer
- [[Comparatif - Versions et changelog]] — départager les outils de version et de changelog
- [[Rule - Git et identité]] — le même hook `commit-msg`, pour l'identité et le co-auteur
- [[Rule - Qualité stricte]] — les contrôles avant commit
- [[Commitizen]], [[python-semantic-release]], [[release-please]], [[git-cliff]] — les outils de version
- [[pre-commit]], [[Lefthook]] — les gestionnaires de hooks
