---
role: comparatif
nom: Comparatif - Versions et changelog
categorie: devtools/projet
tags: [changelog]
---

# Comparatif - Versions et changelog

> On tranche sur : ce que l'outil produit (journal seul, ou aussi version, tag et release), qui le déclenche (une commande sur le poste ou la fusion d'une pull request), la forge qu'il suppose, la discipline qu'il exige des messages de commit, la liberté de forme du journal, et le langage à installer.

![[Comparatif - Versions et changelog.base]]

## Ce qui départage

- [[Commitizen]] — **la release par commandes, sur le poste** : `cz commit` guide le message, `cz bump` calcule la version, met à jour les fichiers qui la portent, crée le tag et, si l'option est activée, le changelog. Le prix : Python 3.10 ou plus, et une convention de commits qu'un hook `commit-msg` doit faire respecter sur chaque poste pour que le numéro calculé soit juste.
- [[git-cliff]] — **le journal, rien d'autre, mais à la forme voulue** : un binaire Rust, un modèle Tera, des analyseurs à expressions régulières pour un historique indiscipliné, et `--bump` pour le numéro. Le prix : il ne crée pas le tag et ne touche à aucun fichier de version ; la release reste à écrire autour.
- [[release-please]] — **la release par pull request, sur GitHub** : une *release PR* tenue à jour depuis les commits conventionnels, qui, fusionnée, met à jour changelog et fichiers de version, pose le tag et crée la release GitHub. Le prix : la commande exige un jeton GitHub et une adresse `<propriétaire>/<dépôt>` ; le README ne documente pas d'autre forge, et recommande le squash-merge.
- [[python-semantic-release]] — **la release automatique en CI, côté Python, sur plusieurs forges** : un analyseur de commits décide s'il faut une version et laquelle, puis `semantic-release version` met à jour les fichiers de version, écrit le changelog, pose le tag et publie la release sur GitHub, GitLab, Gitea ou Bitbucket. Le prix : l'envoi du paquet vers PyPI n'est pas son travail (la documentation ajoute une action à part dans la CI), et le numéro calculé n'est juste que si les commits suivent la convention.


**Critère par critère**

**Ce que l'outil produit.** [[python-semantic-release]] : la version, les fichiers de version, le changelog, le tag et la release sur la forge ; pas l'envoi vers PyPI. [[Commitizen]] : le message de commit, la version, le tag, les fichiers de version et le changelog. [[git-cliff]] : le changelog et, sur demande, le numéro de la prochaine version, affiché ou calculé par `--bump` ; ni tag, ni fichier de version, ni release. [[release-please]] : la pull request, puis, à sa fusion, le changelog, les fichiers de version, le tag et la release GitHub ; la publication vers les registres de paquets n'en fait pas partie.

**Déclenchement.** [[python-semantic-release]] : `semantic-release version`, pensé pour la CI et lancé aussi en local. [[Commitizen]] : une commande lancée à la main (`cz bump`) ou en CI. [[git-cliff]] : une commande (`git cliff`), dans un script de release ou en CI. [[release-please]] : une GitHub Action, ou les commandes `release-pr` puis `github-release` ; la fusion de la pull request de release vaut décision.

**Forge supposée.** [[python-semantic-release]] a des modules pour GitHub, GitLab, Gitea et Bitbucket. [[Commitizen]] et [[git-cliff]] ne demandent que Git : ils tournent sur [[Forgejo]], [[GitLab CE]] ou un dépôt sans forge. [[release-please]] parle à l'API GitHub (`--api-url` en change l'adresse, par défaut `api.github.com`) ; sur une forge auto-hébergée, rien n'est documenté.

**Discipline des messages.** [[Commitizen]] : la plus forte — questions guidées à l'écriture, `cz check` pour valider un message ou une série de commits, hook `commit-msg` par [[pre-commit]]. [[git-cliff]] : la plus tolérante — des analyseurs à expressions régulières classent aussi des messages qui ne suivent pas la convention. [[release-please]] : suppose des commits conventionnels, et un historique linéaire par squash-merge.

**Liberté de forme du journal.** [[Commitizen]] : le format Keep a Changelog, avec des règles et des modèles personnalisables. [[git-cliff]] : un modèle complet (`cliff.toml`, syntaxe Tera). [[release-please]] : des options de personnalisation (`docs/customizing.md`), que ce comparatif n'a pas évaluées.

**Langage et installation.** [[python-semantic-release]] : Python, `pip` ou conda-forge, ou une action GitHub. [[Commitizen]] : Python, par `uv tool` ou `pipx`. [[git-cliff]] : un binaire Rust, sans runtime. [[release-please]] : une action GitHub, ou le paquet npm en ligne de commande.

**Licence et entretien.** [[Commitizen]] : MIT, v4.19.2 du 2026-10-07. [[git-cliff]] : Apache-2.0, v2.14.2 du 2026-09-18. [[release-please]] : Apache-2.0, v17.11.2 du 2026-08-24, dépôt poussé le 2026-10-05. [[python-semantic-release]] : MIT, v10.7.0 du 2026-09-22, dépôt poussé le 2026-10-05. Aucune des quatre n'est archivée ; les quatre sont libres au sens de la règle du brain.

**On tranche, sur site, dans cet ordre** : une forge auto-hébergée ou un dépôt hors GitHub → [[Commitizen]] si l'on veut une seule commande qui fait version, tag et journal, [[git-cliff]] si le journal est le seul besoin ou si la forme doit être fine ; un projet sur GitHub, où la release se valide en relisant une pull request → [[release-please]] ; un projet qui n'a pas Python → [[git-cliff]], un seul binaire ; un projet Python dont la release doit sortir seule en CI, sur GitLab ou Gitea compris → [[python-semantic-release]]. L'agent qui commite doit suivre la convention de l'une comme de l'autre : un hook `commit-msg` la lui impose.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Gestion de projet]] — le hub du dossier.
- [[Commits conventionnels, versions et changelog]] — les trois conventions sur lesquelles reposent ces outils, et leur usage avec un agent.
