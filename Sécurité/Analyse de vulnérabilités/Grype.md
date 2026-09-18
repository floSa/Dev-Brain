---
role: brique
nom: Grype
alias: [grype, anchore grype, syft et grype]
pitch: "Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours."
categorie: security/analyse
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Trivy]]"]
complements: ["[[Docker]]", "[[Podman]]", "[[GitHub Actions]]"]
tags: [vulnerability-scanning, sbom, supply-chain, container, ci-cd]
url_docs: https://oss.anchore.com/docs/
url_repo: https://github.com/anchore/grype
---

# Grype

<!-- AUTO:BANDEAU:START -->
> Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Scanner de vulnérabilités en ligne de commande, édité par **Anchore** avec son compagnon **Syft**, qui génère le SBOM. Les deux forment un couple : Syft dresse la liste des composants d'une image, d'un répertoire ou d'une archive ; Grype la compare à sa base. Grype accepte aussi un SBOM déjà produit (Syft, SPDX, CycloneDX) — un SBOM se **rescanne** donc à chaque nouvelle base, sans retoucher l'image. Sa base est reconstruite chaque jour à partir de 18 fournisseurs (NVD, GitHub Security Advisories, Debian, Ubuntu, Red Hat, Alpine, Wolfi, Chainguard, Amazon…), enrichie par EPSS et CISA KEV. Relevé le 2026-09-30 : Grype **v0.119.0** (2026-09-17), environ 13 000 étoiles, 28 versions en 12 mois ; Syft **v1.52.0** (2026-09-17), environ 9 600 étoiles. Les deux en **Apache-2.0** ; la base est publiée « sans coût » par Anchore, sans licence distincte indiquée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un SBOM à produire une fois (Syft) puis à rescanner quand la base change — le schéma d'un site qui livre des images | Des secrets, des configurations d'infrastructure ou des licences à contrôler dans le même passage : Grype ne fait que les vulnérabilités |
| Un site isolé : la base s'importe depuis un fichier (`grype db import`) et un miroir interne se sert par HTTP | Une base qui ne peut pas être rafraîchie au moins tous les 5 jours : le scan échoue tant qu'on n'a pas réglé l'âge maximal |
| Des faux positifs à documenter : règles `ignore` dans `.grype.yaml`, VEX OpenVEX ou CSAF | Une politique qui exige un éditeur avec une fondation ou un comité : dépôt d'entreprise, sans gouvernance formelle |
| Un éditeur et un dépôt sans incident de chaîne d'approvisionnement relevé | Un besoin de scan de cluster Kubernetes natif : aucune fonction documentée dans les pages lues |

## Mise en œuvre

- Installation — un binaire Go unique pour Grype et un pour Syft ; images et paquets des versions publiées
- Point d'entrée — `syft <image> -o cyclonedx-json > sbom.json` puis `grype sbom:sbom.json`, ou directement `grype <image>` ; `--from` : docker, podman, containerd, archives, répertoire, registre, SBOM, purl ; `--fail-on <sévérité>` (code de sortie 2), `--only-fixed`, `--vex`, `.grype.yaml`
- Prérequis — **la base a un âge maximal** : `GRYPE_DB_MAX_ALLOWED_BUILT_AGE` vaut 120 h par défaut, et `GRYPE_DB_VALIDATE_AGE=false` coupe la vérification. Hors ligne : `GRYPE_DB_AUTO_UPDATE=false`, `GRYPE_CHECK_FOR_APP_UPDATE=false`, `grype db import <archive>` (local ou URL, avec somme de contrôle) ; un miroir interne reproduit `databases/v6/latest.json` et l'archive `.tar.zst` qu'il désigne. La base v6 pèse environ 175 Mio (mesuré le 2026-09-30, en-tête HTTP). Syft travaille hors ligne par défaut ; `--enrich` ajoute des recherches en ligne
- Exécution — local ou CI, sans serveur ; sans `--platform`, Syft lit une image multi-architecture en `linux/amd64`
- Coût — gratuit ; l'offre commerciale d'Anchore (Anchore Enterprise) est bâtie sur les deux outils, et ce qu'elle ajoute n'a pas été relevé ici

## Limites à connaître

- **Deux scanners, deux listes.** Sur un même SBOM, le résultat dépend de la source de données du paquet : une discussion du dépôt Trivy (n° 10447) relève 1 vulnérabilité côté Trivy et 37 côté Grype sur un SBOM Conan, la différence venant de la base utilisée pour cet écosystème ; il a fallu `--add-cpes-if-none` côté Trivy. Ne jamais conclure d'un seul scanner.
- **CPE ou natif** : la correspondance par CPE se règle par langage (`using-cpes`) et produit des faux positifs ; `--show-suppressed` montre ce qui a été filtré.
- **Seul l'installé se voit dans une image** : Syft, sur une image, ne lit que les métadonnées des paquets installés, non les fichiers d'intention (`requirements.txt`). Par défaut il lit la vue aplatie : un fichier supprimé dans une couche ancienne n'apparaît pas (`--scope all-layers` le garde).
- **Avis de sécurité** : un seul sur Grype (GHSA-6gxw-85q2-q646, CVE-2025-65965, haut, 8,2, 2025-11-24) — identifiants de registre écrits en clair dans les sorties JSON produites avec `--file` ; touche les versions v0.68.0 à v0.104.0, corrigé en v0.104.1. Syft : deux avis modérés sur 12 mois (GHSA-rjcw-vg7j-m9rc, corrigé en v1.42.3 ; GHSA-mw2c-m758-9v5q, corrigé en v1.52.0). Seule la dernière version est corrigée.
- **Aucune compromission de chaîne d'approvisionnement relevée** dans les avis GitHub des dépôts `grype`, `syft`, `scan-action` et `sbom-action`, ni dans les articles sur les campagnes de 2025-2026 consultés. Ce n'est pas une preuve d'absence.
- **Adoption** : GitLab a retenu Trivy comme scanner par défaut de son Container Scanning et annonce l'arrêt de son analyseur Grype à GitLab 19.0 ; aucune intégration par défaut de Grype dans Harbor n'a été trouvée.
- Syft n'a pas de fiche séparée dans ce brain (plafond de cinq briques) ; ce qui précède vaut pour lui.

## Écosystème

### Alternatives

- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — le même besoin avec secrets et IaC en plus, là où Grype se concentre sur la liste des composants et sa base.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — une image locale s'analyse par `--from docker`.
- [[Podman]] — Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`. — `--from podman` lit une image locale.
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — `anchore/scan-action` (et `anchore/sbom-action` pour Syft) ; le README recommande d'épingler l'action par SHA.

## Ressources

- Documentation — https://oss.anchore.com/docs/
- Dépôt — https://github.com/anchore/grype
- Dépôt — Syft, le générateur de SBOM : https://github.com/anchore/syft
- Documentation — la base de vulnérabilités : https://oss.anchore.com/docs/guides/vulnerability/database/
- Documentation — filtrer les résultats et VEX : https://oss.anchore.com/docs/guides/vulnerability/filter-results/
- Documentation — formats de SBOM de Syft : https://oss.anchore.com/docs/guides/sbom/formats/
- Article — avis de sécurité de Grype : https://github.com/anchore/grype/security/advisories

## Voir aussi

- [[Analyse de vulnérabilités]] — le hub du dossier
- [[Supply chain logicielle et SBOM]] — la notion : SBOM, VEX, image contre dépendances, hors ligne
- [[Comparatif - Scanners de sécurité]] — Trivy, Grype, Gitleaks, Semgrep et Dependency-Track par usage
