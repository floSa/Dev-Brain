---
role: brique
nom: Semgrep
alias: [semgrep, semgrep ce, semgrep community edition, semgrep oss]
pitch: "Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer."
categorie: security/analyse
famille: cli
licence_type: open-core
maturite: production
alternatives: []
complements: ["[[GitHub Actions]]", "[[Ruff]]", "[[pre-commit]]"]
tags: [sast, supply-chain, ci-cd]
url_docs: https://docs.semgrep.dev/
url_repo: https://github.com/semgrep/semgrep
---

# Semgrep

<!-- AUTO:BANDEAU:START -->
> Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI | open-core | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil d'**analyse statique de sécurité** : il cherche dans le code source des **motifs** décrits par des règles YAML qui ressemblent au code qu'elles visent (`eval(...)`, une requête SQL concaténée, une fonction dangereuse appelée avec une variable non validée). Une seule commande, plus de 30 langages annoncés ; Python est en disponibilité générale, Dockerfile et YAML restent expérimentaux. Trois morceaux, trois régimes : le **moteur** de l'édition communautaire (CE) est en LGPL-2.1 ; les **règles** maintenues par Semgrep sont sous une licence à part, l'usage interne seul ; le moteur et les règles **payants** (analyse entre fichiers, secrets, chaîne d'approvisionnement, triage assisté) appartiennent à la plateforme de l'éditeur. Relevé le 2026-09-30 : **v1.178.0** (2026-09-23), environ 16 800 étoiles, environ une version par semaine, dernier commit le jour même. La licence du moteur est celle de la fiche ; celle des règles est la contrainte : voir *Prérequis*.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Du code Python, JavaScript, Java ou Go à passer en revue en CI, avec des règles **écrites par l'équipe** (le motif ressemble au code) | Une analyse de flux de données entre fichiers et entre fonctions : l'édition communautaire se limite à un fichier, le taint à une fonction |
| Un site sans internet : `--config` vers un répertoire de règles local suffit, sans compte | Livrer les règles du registre à un client ou lui offrir le scan comme service : la licence des règles l'interdit au-delà de l'usage interne — à trancher avec un juriste |
| Un moteur que GitLab utilise pour son SAST Python, avec ses propres règles | Un suivi des résultats dans le temps, des commentaires sur les pull requests, un tableau de bord : absents de l'édition communautaire, il faut exporter en SARIF ou JSON |
| Une sortie SARIF ou JSON qui se branche sur l'outillage de la CI | Un code privé à passer dans CodeQL : son interface en ligne de commande n'autorise les bases de données que pour du code open source, hors licence GitHub payante |

## Mise en œuvre

- Installation — `pipx install semgrep` ou `uv tool install semgrep` (roues binaires sur PyPI pour Linux, macOS et Windows, ce dernier en bêta) ; image `semgrep/semgrep`
- Point d'entrée — `semgrep scan --config ./regles/ .` ; `--sarif`, `--json`, `--junit-xml`, `--gitlab-sast` ; `# nosemgrep` (avec l'identifiant de règle si besoin) et `.semgrepignore` ; `--baseline-commit <sha>` ne montre que ce qui est neuf. `semgrep ci` s'appuie sur la plateforme : `--config` n'y est pas pris en charge
- Prérequis — **hors ligne** : les règles du registre (`p/python`, `auto`) exigent le réseau ; constituer un répertoire de règles (les siennes, ou une copie de `semgrep-rules`, dont la licence suit la copie), puis `--metrics=off` et `--disable-version-check`. La télémétrie est **active par défaut** (`--metrics auto`, envoyée quand les règles viennent du registre ou qu'on est connecté : version, identifiant anonyme, noms de règles hachés, durées, nombre de résultats ; le code et les règles privées n'en font pas partie). **Licence des règles** : « Semgrep Rules License v. 1.0 » (mise à jour du 2024-12-13) — usage pour ses propres besoins internes seulement, ni distribution ni mise à disposition en service, avertissements de copyright à conserver ; le texte ne définit pas « internal business purposes ». La documentation de déploiement CE va plus loin : pour rester strictement open source, n'exécuter que des règles sous licence ouverte (champ `metadata.license`) ou les siennes
- Exécution — local ou CI ; la documentation fournit des modèles pour GitHub Actions (conteneur `semgrep/semgrep`), GitLab CI, Jenkins, Bitbucket, Buildkite, CircleCI et Azure Pipelines ; l'action `semgrep-action` est archivée depuis 2024-04-09
- Coût — le moteur et les règles communautaires sont gratuits ; le reste est l'offre payante de l'éditeur, dont les tarifs n'ont pas été relevés

## Limites à connaître

- **Ce que la communauté n'a pas.** La page officielle de comparaison donne, pour la CE : propagation de constantes intra-fichier et taint sur une seule fonction ; aucun SCA, aucun scan de secrets ; pas de règles « Pro ». Une étude de Doyensec publiée le 2025-06-26, **financée par Semgrep**, mesure sur des applications volontairement vulnérables 48 % de vrais positifs pour la CE contre 72 % pour l'offre payante sur WebGoat, 44 % contre 75 % sur Juice Shop. Aucune source indépendante exploitable sur le taux de faux positifs n'a été trouvée.
- **Changement de 2024 et fork.** Le 2024-12-13, l'éditeur a renommé « Semgrep OSS » en « Community Edition », placé les règles sous la licence d'usage interne, et réservé certains champs des sorties au moteur connecté. Un consortium de sociétés de sécurité (dont Aikido, Endor Labs, Orca) a lancé en réaction le fork **Opengrep** (LGPL-2.1, environ 3 100 étoiles) : il écrit que des éléments ont été déplacés derrière un paywall ; le fondateur de Semgrep répond que le changement visait les éditeurs qui redistribuaient le dépôt de règles et qu'un usage sans « bundling and reselling » n'est pas touché. Le dépôt `opengrep-rules` est archivé depuis 2025-11-28, instantané du 2024-12-13. Les deux récits sont écrits tels quels, sans arbitrage ici.
- **Hors ligne, deux points à tester.** Les exemples de CI officiels utilisent `--config auto`, donc le réseau ; le comportement de `semgrep ci` sans jeton n'est pas documenté dans les pages lues.
- **Avis de sécurité** : aucun avis GitHub publié ; un CVE embarqué dans d'anciennes versions (CVE-2023-32758, déni de service par expression régulière dans `giturlparse`, 7,5, publié le 2025-01-23). Dans son billet sur la campagne visant Trivy et d'autres éditeurs de sécurité en mars-avril 2026, l'éditeur écrit que Semgrep n'est pas touché : déclaration non recoupée. Aucune compromission de paquet, d'image ou d'action trouvée.
- **Adoption** : environ 18,8 millions de téléchargements PyPI sur le dernier mois (pypistats ; chiffre qui inclut les CI et miroirs).

## Écosystème

### Alternatives

- *Aucune alternative déclarée : Bandit n'a pas de fiche (maintenance faible, et les règles `S` de Ruff reprennent ses tests) ; CodeQL et SonarQube n'entrent pas dans le critère — le [[Comparatif - Scanners de sécurité]] dit pourquoi.*

### Compléments

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la documentation Semgrep en donne un modèle par conteneur `semgrep/semgrep`, sans jeton.
- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil. — ses règles `S` sont un portage de flake8-bandit (documentation de Ruff) : un premier filet de motifs simples, dans l'outil de lint déjà installé, que Semgrep prolonge avec des règles propres et d'autres langages.
- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent. — dépôt officiel `semgrep/pre-commit` (hooks `semgrep` et `semgrep-ci`) ; avec des règles locales le hook tourne sans réseau, un `--config` pointant vers une URL le réclame.

## Ressources

- Documentation — https://docs.semgrep.dev/
- Dépôt — https://github.com/semgrep/semgrep
- Documentation — licences (moteur, règles) : https://docs.semgrep.dev/licensing
- Documentation — texte de la Semgrep Rules License v1.0 : https://semgrep.dev/legal/rules-license/
- Documentation — édition communautaire contre plateforme : https://docs.semgrep.dev/semgrep-pro-vs-oss
- Documentation — déploiement de l'édition communautaire : https://docs.semgrep.dev/deployment/oss-deployment
- Documentation — métriques et télémétrie : https://docs.semgrep.dev/metrics
- Article — l'annonce de décembre 2024 : https://semgrep.dev/blog/2024/important-updates-to-semgrep-oss
- Article — le fork Opengrep vu par InfoQ : https://www.infoq.com/news/2025/02/semgrep-forked-opengrep
- Dépôt — Opengrep : https://github.com/opengrep/opengrep

## Voir aussi

- [[Analyse de vulnérabilités]] — le hub du dossier
- [[Supply chain logicielle et SBOM]] — la notion : ce qu'un scanner voit et ne voit pas
- [[Comparatif - Scanners de sécurité]] — Trivy, Grype, Gitleaks, Semgrep et Dependency-Track par usage
