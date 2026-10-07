---
role: brique
nom: python-semantic-release
alias: [semantic-release, PSR, Python Semantic Release, python-semantic-release/python-semantic-release]
pitch: "Outil en ligne de commande Python (MIT) qui lit les commits d'un dépôt, calcule la prochaine version SemVer, met à jour les fichiers de version, génère le changelog, pose le tag et publie la release sur GitHub, GitLab, Gitea ou Bitbucket — mais l'envoi du paquet vers PyPI n'est pas son travail, la documentation le confie à une étape de la CI."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Commitizen]]", "[[git-cliff]]", "[[release-please]]"]
complements: []
tags: [changelog, version-control]
url_docs: https://python-semantic-release.readthedocs.io/en/stable/
url_repo: https://github.com/python-semantic-release/python-semantic-release
---

# python-semantic-release

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande Python (MIT) qui lit les commits d'un dépôt, calcule la prochaine version SemVer, met à jour les fichiers de version, génère le changelog, pose le tag et publie la release sur GitHub, GitLab, Gitea ou Bitbucket — mais l'envoi du paquet vers PyPI n'est pas son travail, la documentation le confie à une étape de la CI.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande (`semantic-release`) qui automatise la **release** d'un projet à partir des messages de commit. Un *analyseur de commits* lit l'historique depuis la dernière version, en tire l'impact de chaque changement (correctif, fonctionnalité, rupture) et décide s'il faut sortir une version et laquelle, selon SemVer. Il propose plusieurs analyseurs prêts à l'emploi (conventionnel, Angular, emoji, scipy) et accepte le sien. La commande `semantic-release version` met à jour les fichiers qui portent la version (par défaut `pyproject.toml`, réglable), lance éventuellement une commande de construction, écrit le changelog, commite, pose le tag et publie la release sur la forge ; `changelog`, `publish` et `generate-config` font le reste. La configuration vit dans `pyproject.toml`, table `[tool.semantic_release]`, ou dans un fichier choisi par `-c`.

Il est conçu pour tourner dans la CI, mais s'exécute aussi en local. Il s'inspire du `semantic-release` de JavaScript sans en partager le code. Une GitHub Action officielle existe ; les modules de forge couvrent GitHub, GitLab, Gitea et Bitbucket. **La documentation est nette sur un point** : l'outil n'est pas responsable de l'envoi des artefacts vers PyPI ; l'exemple de workflow ajoute pour cela l'action `pypa/gh-action-pypi-publish` après la release. Version 10.7.0 du 2026-09-22, licence MIT lue dans le dépôt (et dans les métadonnées PyPI), Python 3.8 ou plus, dépôt poussé le 2026-10-05.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un projet Python dont la version se déduit des commits, sans relire de pull request de release | Une release validée par la relecture d'une pull request : [[release-please]], sur GitHub |
| Une forge hors GitHub : GitLab, Gitea ou Bitbucket sont pris en charge par des modules dédiés | Un journal seul, à la forme très libre, pour un historique peu discipliné : [[git-cliff]] |
| Tout dans un seul outil Python, réglé dans `pyproject.toml`, avec un guide pour `uv` et pour les monorepos | Guider l'écriture des messages sur le poste : [[Commitizen]] pose un assistant de commit et un hook de validation |
| Un pipeline CI qui sort la release à chaque fusion sur la branche principale | Une équipe qui ne suit pas les commits conventionnels : le numéro calculé sera faux (cf. [[Commits conventionnels, versions et changelog]]) |

## Mise en œuvre

- Installation — `python3 -m pip install python-semantic-release`, ou conda-forge, ou l'action GitHub ; `uv tool` convient aussi
- Point d'entrée — `semantic-release generate-config` pour voir la configuration par défaut, puis `semantic-release version` ; le guide de démarrage détaille le reste
- Prérequis — Python 3.8 ou plus, un historique de commits cohérent, un jeton de forge pour publier la release
- Exécution — en CI ou en local ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[Commitizen]] — Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` — mais tout repose sur des messages de commit conformes, que seul le hook de validation impose. — là où python-semantic-release automatise toute la release en CI, Commitizen guide aussi l'écriture du commit sur le poste.
- [[git-cliff]] — Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas. — le journal seul, à la forme voulue, sans le tag ni les fichiers de version.
- [[release-please]] — Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets. — la release validée par une pull request, là où python-semantic-release la sort directement.

## Ressources

- Documentation — https://python-semantic-release.readthedocs.io/en/stable/
- Dépôt — https://github.com/python-semantic-release/python-semantic-release

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Comparatif - Versions et changelog]] — où ces outils se départagent
- [[Commits conventionnels, versions et changelog]] — la convention sur laquelle il repose
- [[Outils de développement]] — le hub du domaine
