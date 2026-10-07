---
role: brique
nom: release-please
alias: [Release Please, googleapis/release-please]
pitch: "Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets."
categorie: devtools/projet
famille: cli
domaines: [ai-eng, mlops]
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Commitizen]]", "[[git-cliff]]"]
complements: []
tags: [changelog, version-control]
url_docs: https://github.com/googleapis/release-please
url_repo: https://github.com/googleapis/release-please
---

# release-please

<!-- AUTO:BANDEAU:START -->
> Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les fichiers de version, pose le tag et crée la release GitHub — mais il vise l'API GitHub (jeton GitHub exigé) et ne publie pas les paquets.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de release, écrit en TypeScript et publié par Google (organisation `googleapis`), qui automatise le journal des changements, les versions et la release **par une pull request**. Il lit l'historique depuis le dernier tag, y cherche des commits conventionnels (`fix:` donne un correctif, `feat:` une mineure, `feat!:` une majeure) et ouvre une *release PR*, qu'il remet à jour à chaque nouveau commit fusionné. Quand cette pull request est fusionnée, il met à jour le changelog et les fichiers de version propres au langage (`package.json`, par exemple), pose le tag et crée la release GitHub. Des étiquettes (`autorelease: pending`, puis `tagged`) disent où en est la pull request. Le README précise qu'il ne publie pas vers les gestionnaires de paquets et ne gère pas de branches complexes. Des stratégies existent par type de dépôt : Node, Python, Rust, Go, Java et Maven, Ruby, PHP, Helm, Terraform et d'autres, plus `simple` (un `version.txt`). Un fichier de manifeste permet de publier plusieurs artefacts depuis un seul dépôt. Version 17.11.2 du 2026-08-24, licence Apache-2.0 lue dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un projet sur GitHub, où la release se décide en relisant et en fusionnant une pull request | Une forge auto-hébergée : la commande demande un jeton GitHub et une adresse `<propriétaire>/<dépôt>` ; `--api-url` change l'adresse de l'API, par défaut `api.github.com`, mais le README ne documente ni [[Forgejo]] ni [[GitLab CE]] |
| Un monorepo dont les paquets sortent à des versions différentes (configuration par manifeste) | Des pull requests fusionnées en merge commits, dont les messages n'ont de sens que dans leur branche : le README recommande vivement le squash-merge, pour que le journal de la pull request de release reflète `main` |
| Aucune commande de release à lancer à la main : la fusion de la pull request suffit | Une release lancée depuis le poste, sans pull request : [[Commitizen]] (`cz bump`) ou [[git-cliff]] |
| Garder un contrôle humain avant chaque release, sur la version et le journal proposés | Un journal à la forme très personnalisée : [[git-cliff]] se règle par un modèle complet ; release-please offre des options de personnalisation (`docs/customizing.md`), que cette fiche n'a pas détaillées |

## Mise en œuvre

- Installation — GitHub Action `googleapis/release-please-action` (voie recommandée par le README), ou le paquet npm `release-please` en ligne de commande
- Point d'entrée — l'action, ou en ligne de commande `release-please release-pr --token=$GITHUB_TOKEN --repo-url=<propriétaire>/<dépôt>` pour la pull request, puis `release-please github-release` pour la release ; `release-please bootstrap` amorce un manifeste dans un dépôt existant
- Prérequis — un dépôt GitHub, un jeton GitHub avec droit d'écriture, des commits conventionnels ([[Commits conventionnels, versions et changelog]])
- Exécution — en CI sur GitHub ; la publication vers un registre de paquets est un autre travail, à brancher sur l'étiquette `autorelease: tagged`
- Coût — gratuit sous licence Apache-2.0 ; v17.11.2 du 2026-08-24, dépôt poussé le 2026-10-05

## Écosystème

### Alternatives

- [[Commitizen]] — Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` — mais tout repose sur des messages de commit conformes, que seul le hook de validation impose. — une release lancée à la main, sans pull request, et sans dépendance à GitHub.
- [[git-cliff]] — Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et calcule la prochaine version SemVer avec `--bump` — mais il produit le journal et le numéro, pas le tag : `--tag` ne le crée pas. — le journal seul, sur n'importe quelle forge.
- voisin : python-semantic-release — version et changelog depuis les commits, côté Python, cité en texte simple, non fiché dans le brain.

## Ressources

- Documentation — https://github.com/googleapis/release-please
- Dépôt — https://github.com/googleapis/release-please-action
- Dépôt — https://github.com/googleapis/release-please

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Commits conventionnels, versions et changelog]] — les trois conventions et leur usage avec un agent
- [[Comparatif - Versions et changelog]] — ce qui départage release-please, Commitizen et git-cliff
- [[Outils de développement]] — le hub du domaine
