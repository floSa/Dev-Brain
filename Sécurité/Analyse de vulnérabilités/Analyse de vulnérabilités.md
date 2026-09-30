---
role: hub
nom: Analyse de vulnérabilités
alias: [analyse de vulnérabilités, scanners de sécurité, scanner de vulnérabilités, sast, sca, détection de secrets, sbom]
pitch: Savoir ce que contient ce qu'on livre et ce que ça expose — composants vulnérables d'une image ou d'un dépôt, secrets oubliés dans l'historique Git, failles dans le code, et suivi des versions déjà livrées.
domaines: [infra-ops, mlops]
tags: [vulnerability-scanning, sbom, secret-scanning, sast, supply-chain]
---

# Analyse de vulnérabilités

> Savoir ce que contient ce qu'on livre et ce que ça expose — composants vulnérables d'une image ou d'un dépôt, secrets oubliés dans l'historique Git, failles dans le code, et suivi des versions déjà livrées.

## Ce qu'il faut comprendre

- **Quatre questions, quatre familles d'outils, qui ne se remplacent pas.** Les **composants** d'une image ou d'un dépôt ont-ils une faille connue ? ([[Trivy]], [[Grype]]). Un **secret** dort-il dans le code ou dans l'historique Git ? ([[Gitleaks]], et le détecteur de [[Trivy]]). Le **code** lui-même contient-il un motif dangereux ? ([[Semgrep]]). Et, une fois livré, **qui a reçu quoi** quand une nouvelle faille paraît ? ([[Dependency-Track]]). [[Supply chain logicielle et SBOM]] est la notion qui les relie : ce qu'est un SBOM, VEX, image contre dépendances, ce qu'un scanner ne voit pas.
- **Un scanner tourne avec les droits de votre pipeline.** En mars 2026, la chaîne de publication de [[Trivy]] a été compromise : binaire, tags de l'action GitHub et images Docker Hub. Épingler les actions par SHA, vérifier les binaires et garder un miroir interne des versions validées font partie de l'usage, pas d'un durcissement facultatif.
- **Hors ligne, la base de vulnérabilités est une donnée à transporter.** [[Trivy]] la sert comme artefact OCI, [[Grype]] refuse de scanner avec une base de plus de 120 heures, [[Dependency-Track]] veut des miroirs NVD et OSV internes à construire. Sa date fait partie du résultat.
- **Deux scanners, deux listes.** Sur un même SBOM, [[Trivy]] et [[Grype]] ne rendent pas les mêmes résultats : la différence vient de la source de données par écosystème. Un scan ne prouve pas une absence.
- **La licence de ce que l'outil charge compte autant que celle du code.** [[Semgrep]] a un moteur en LGPL-2.1 et des règles sous licence d'usage interne, qui interdit de les redistribuer ou de les offrir en service ; les autres outils du dossier sont en Apache-2.0 ou MIT.
- **Un secret détecté est un secret compromis** : le retirer du dernier commit ne l'efface pas de l'historique. Où le ranger ensuite : [[Gestion des secrets]].

## Choisir

- Les composants d'une image, d'un dépôt Python ou d'un SBOM, avec secrets et IaC en plus → [[Trivy]].
- La même comparaison à partir d'un SBOM rejouable, sur une base qu'on importe à la main → [[Grype]].
- Un secret en dur à bloquer avant le commit ou à chercher dans l'historique d'un dépôt client → [[Gitleaks]].
- Le code source, avec des règles qu'on écrit soi-même → [[Semgrep]].
- Le suivi de ce qui a été livré à plusieurs clients, avec alerte sur les nouvelles failles → [[Dependency-Track]].
- Comparer, avec les candidats écartés et leurs raisons → [[Comparatif - Scanners de sécurité]].
- Comprendre ce qu'un SBOM peut et ne peut pas dire → [[Supply chain logicielle et SBOM]].

<!-- AUTO:START -->
### Notions
- [[Supply chain logicielle et SBOM]] — domaines : infra-ops, mlops

### Briques
- [[Dependency-Track]] — Plateforme OWASP (Apache-2.0, Java) qui ingère des SBOM CycloneDX et suit dans la durée les vulnérabilités des composants d'un portefeuille de projets, avec alertes sur les nouvelles CVE, politiques et VEX — elle ne scanne rien elle-même, exige PostgreSQL, et sa documentation hors ligne est encore incomplète.
- [[Gitleaks]] — Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT.
- [[Grype]] — Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours.
- [[Semgrep]] — Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer.
- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées).

### Comparatifs
- [[Comparatif - Scanners de sécurité]]
<!-- AUTO:END -->
