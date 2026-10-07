---
role: brique
nom: git-cliff
alias: [git cliff, cliff, orhun/git-cliff]
pitch: "Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[Commitizen]]", "[[release-please]]", "[[python-semantic-release]]"]
complements: []
tags: [changelog, version-control]
url_docs: https://git-cliff.org/docs
url_repo: https://github.com/orhun/git-cliff
---

# git-cliff

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande, un binaire écrit en Rust, qui lit l'historique Git et en écrit un changelog. Les commits sont classés par la convention Conventional Commits, ou par des analyseurs à expressions régulières quand l'historique n'est pas conforme. La mise en forme tient dans un fichier `cliff.toml` (TOML de préférence, YAML accepté) et dans un modèle Tera, syntaxe proche de Jinja2 : le journal prend la forme voulue, pas celle d'un outil. Les commandes courantes : `git cliff` écrit le changelog entier, `--unreleased` ne traite que les commits depuis le dernier tag, `--latest` que la dernière version, `--tag 1.0.0` nomme les changements non publiés sans créer le tag, `-o` écrit dans un fichier, `--prepend CHANGELOG.md` ajoute en tête. `--bump` calcule la prochaine version SemVer : `fix:` incrémente le correctif, `feat:` la mineure, un changement cassant la majeure ; `--bumped-version` l'affiche seule, `--bump major|minor|patch` la force. Version 2.14.2 du 2026-09-18, licence Apache-2.0 lue dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un changelog dont la forme se règle finement par modèle, pour n'importe quel langage : l'outil ne sait rien du projet, seulement de Git | Un outil qui fait aussi le tag, la mise à jour des fichiers de version et le commit de release : [[Commitizen]] le fait en une commande |
| Un historique mal discipliné : des analyseurs à expressions régulières regroupent des commits qui ne suivent pas la convention | Une release portée par une pull request : [[release-please]] la tient à jour ; git-cliff n'ouvre rien |
| Un seul binaire, sans Python ni Node, utilisable en CI interne ([[Forgejo]], [[GitLab CE]], [[Woodpecker CI]]) | Un guidage à l'écriture des messages : git-cliff les lit, il ne les corrige pas ; il faut un outil de commit, ou un hook de validation avec [[pre-commit]] |
| Des notes de release pour la dernière version seulement (`--latest`) ou les commits non publiés (`--unreleased`) | Une publication de la release sur la forge ou sur un registre de paquets : le rôle de l'outil s'arrête au journal et au numéro |

## Mise en œuvre

- Installation — binaire Rust (`cargo install git-cliff`), paquets des distributions listés dans la documentation (état des paquets suivi par repology), ou image Docker
- Point d'entrée — `git cliff` dans le dépôt ; fichier de configuration cherché dans l'ordre `cliff.toml`, `.cliff.toml`, `.config/cliff.toml`, puis dans les répertoires parents, puis dans la configuration globale de l'utilisateur
- Prérequis — Git ; aucun autre langage
- Exécution — sur le poste ou en CI ; les variables d'environnement surchargent la configuration. Les commandes de pré et post-traitement s'ignorent avec `--no-exec`
- Coût — gratuit sous licence Apache-2.0 ; v2.14.2 du 2026-09-18, dépôt poussé le même jour

## Écosystème

### Alternatives

- [[Commitizen]] — Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` — mais tout repose sur des messages de commit conformes, que seul le hook de validation impose. — git-cliff ne fait que le journal et le numéro ; Commitizen y ajoute le commit guidé et le tag.
- [[release-please]] — Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets. — git-cliff peut tourner partout où Git tourne ; release-please suppose GitHub.
- [[python-semantic-release]] — Outil en ligne de commande Python (MIT) qui lit les commits d'un dépôt, calcule la prochaine version SemVer, met à jour les fichiers de version, génère le changelog, pose le tag et publie la release sur GitHub, GitLab, Gitea ou Bitbucket — mais l'envoi du paquet vers PyPI n'est pas son travail, la documentation le confie à une étape de la CI. — le journal seul pour git-cliff ; python-semantic-release tient aussi la version, le tag et la release.

## Ressources

- Documentation — https://git-cliff.org/docs
- Dépôt — https://github.com/orhun/git-cliff

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Commits conventionnels, versions et changelog]] — les trois conventions et leur usage avec un agent
- [[Comparatif - Versions et changelog]] — ce qui départage git-cliff, Commitizen et release-please
- [[Outils de développement]] — le hub du domaine
