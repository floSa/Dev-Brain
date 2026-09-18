---
role: brique
nom: Dependency-Track
alias: [dependency-track, owasp dependency-track, dependency track, dtrack]
pitch: "Plateforme OWASP (Apache-2.0, Java) qui ingère des SBOM CycloneDX et suit dans la durée les vulnérabilités des composants d'un portefeuille de projets, avec alertes sur les nouvelles CVE, politiques et VEX — elle ne scanne rien elle-même, exige PostgreSQL, et sa documentation hors ligne est encore incomplète."
categorie: security/analyse
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: []
complements: ["[[Trivy]]"]
tags: [vulnerability-scanning, sbom, supply-chain, self-hosted]
url_docs: https://dependencytrack.org/
url_repo: https://github.com/DependencyTrack/dependency-track
---

# Dependency-Track

<!-- AUTO:BANDEAU:START -->
> Plateforme OWASP (Apache-2.0, Java) qui ingère des SBOM CycloneDX et suit dans la durée les vulnérabilités des composants d'un portefeuille de projets, avec alertes sur les nouvelles CVE, politiques et VEX — elle ne scanne rien elle-même, exige PostgreSQL, et sa documentation hors ligne est encore incomplète.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur qui garde en mémoire **ce que contient chaque version livrée**. On lui envoie un SBOM CycloneDX par son API à chaque build (`PUT` ou `POST` sur `/api/v1/bom`, ou un plugin de CI) ; il range les composants par projet et par version, les rapproche de ses bases de vulnérabilités et **réévalue en continu** : une CVE publiée demain sur un composant livré hier fait apparaître une alerte, sans relancer aucun scan d'image. C'est ce que ni Trivy ni Grype ne font, puisqu'ils jugent à l'instant du scan. Les résultats se trient (états d'analyse, suppressions justifiées, VEX CycloneDX en import et export), se règlent par des politiques en CEL et se notifient (Slack, Teams, Mattermost, WebEx, webhook, e-mail, Jira — page de la v4, à reconfirmer en v5). Projet **OWASP Flagship**, co-dirigé par Steve Springett et Niklas Düster. Relevé le 2026-09-30 : **v5.1.1** (2026-09-20), environ 4 200 étoiles, dernier commit le 2026-09-29, licence **Apache-2.0**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs clients, plusieurs versions livrées, et la question « ce paquet touché par la CVE du jour, qui l'a reçu ? » | Un seul projet et un besoin ponctuel : un scan en CI avec un scanner suffit, sans serveur ni base à exploiter |
| Des SBOM CycloneDX déjà produits en CI, à centraliser et à suivre | Des SBOM au format SPDX seulement : aucune mention de SPDX dans la documentation lue, CycloneDX seul est accepté |
| Un site qui peut héberger PostgreSQL et un serveur Java : le quickstart est un fichier Docker Compose officiel | Aucune source de vulnérabilités atteignable et aucun moyen d'y transférer des données : il faut alimenter un miroir interne NVD ou OSV à la main |
| Des décisions de triage à garder et à réutiliser entre versions (VEX, suppression justifiée) | Un besoin de scanner une image : il n'y a aucun scanner intégré, seulement l'ingestion de SBOM |

## Mise en œuvre

- Installation — images `apiserver` et `frontend` (`ghcr.io/dependencytrack/` et Docker Hub), Docker Compose officiel avec `postgres:18-alpine` ; **v5 : PostgreSQL seul** (H2, MySQL et SQL Server abandonnés), images conteneur uniquement (plus de WAR) ; épingler les tags `X.Y.Z`
- Point d'entrée — l'API REST (envoi de BOM, avec clé d'API), le frontend, les plugins Jenkins et GitHub Action ; identité par OIDC ou LDAP (pages v5 existantes, contenu non relu ici)
- Prérequis — 2 Go de RAM et 4 cœurs par instance de départ, PostgreSQL à 8 Go et 4 cœurs recommandés (4 Go et 2 cœurs au minimum) ; au moins deux instances avec un stockage partagé (NFS ou S3) en production. **Hors ligne** : l'analyseur interne ne fait aucun appel sortant ; NVD et OSV se servent depuis un serveur HTTP interne (NVD au format de flux JSON 2.0, fichiers META et GZ ; OSV : un `all.zip` par écosystème et `modified_id.csv`) ; GitHub Advisories ne se mire pas (API GraphQL paginée) : la documentation recommande OSV, qui l'ingère ; OSS Index, Snyk et VulnDB appellent leurs API à chaque analyse. **Aucun outil officiel pour fabriquer le miroir NVD ou OSV interne n'est documenté**, et la page « Running air-gapped » se déclare elle-même inachevée : notifications et métadonnées de dépôts sortent vers internet par défaut
- Exécution — serveur permanent ; migration de v4 vers v5 sans passage en place : hors ligne, avec fenêtre de maintenance
- Coût — gratuit. Sources de données : NVD (clé d'API facultative, mais sans clé le premier miroir est très long), OSV sans authentification, GitHub Advisories avec un jeton sans droits ; OSS Index demande un compte depuis septembre 2025, migré vers « Sonatype Guide » avec des limites de crédits ; Snyk (plan entreprise) et VulnDB (abonnement) sont payantes

## Limites à connaître

- **La qualité suit celle des SBOM.** La correspondance se fait par PURL pour GitHub Advisories et OSV, par CPE pour le NVD ; la documentation note que la plupart des générateurs émettent des PURL mais pas de CPE, d'où peu de résultats NVD sur les paquets. Un même problème sous deux alias (CVE et GHSA) donne deux résultats, dédoublonnés dans les seules métriques.
- **Version en transition.** La v5 (issue du projet Hyades, dépôt archivé le 2026-05-29) est sortie le 2026-06-07 ; la v4 est en maintenance, fin de vie « décembre 2026 » selon la page du dépôt et « environ six mois » après la v5 selon le billet d'annonce. Pour un déploiement neuf : la v5. Plusieurs pages de documentation restent celles de la v4.
- **Avis de sécurité** : neuf avis sur la page du dépôt, aucun daté de 2026 ; les trois plus récents sont modérés (XXE à la validation de BOM XML, 4.11.0 à 4.13.5, corrigé en 4.13.6 ; fuite d'identifiants d'un dépôt NuGet privé, corrigée en 4.13.5 ; inclusion de fichier local par les modèles de notification, corrigée en 4.12.6). Aucune compromission d'image ni de release trouvée, sans recherche dédiée.
- **Adoption** : le projet revendique plus de 20 000 organisations et plus d'un million de SBOM sur une instance, sans preuve indépendante ; environ 198 500 téléchargements par semaine de l'image `apiserver` sur Docker Hub.
- L'enquête de l'ENISA de 2026 sur l'adoption des SBOM (78 % des organisations en génèrent, peu les exploitent) ne cite pas Dependency-Track.

## Écosystème

### Alternatives

- *Aucune alternative déclarée : OWASP Dependency-Check (scanneur ponctuel sans suivi), GUAC et DefectDojo n'ont pas de fiche ; Grype et Trivy produisent ou relisent un SBOM mais ne gardent rien — voir le [[Comparatif - Scanners de sécurité]].*

### Compléments

- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — Trivy produit le SBOM CycloneDX que Dependency-Track ingère, et sert d'analyseur de vulnérabilités via un serveur Trivy séparé.

## Ressources

- Documentation — https://dependencytrack.org/
- Dépôt — https://github.com/DependencyTrack/dependency-track
- Documentation — déploiement en production : https://dependencytrack.github.io/docs/next/guides/administration/deploying-to-production/
- Documentation — exécuter sans accès internet : https://dependencytrack.github.io/docs/next/guides/administration/running-air-gapped/
- Documentation — ce qui change en v5 : https://dependencytrack.github.io/docs/next/concepts/changes-in-v5/
- Documentation — échanger des VEX : https://dependencytrack.github.io/docs/next/guides/user/exchanging-vex-documents/
- Article — la sortie de la v5 : https://owasp.github.io/blog/2026/06/09/dependency-track-v5
- Article — la version 5.1 : https://dependencytrack.org/news/dependency-track-5-1

## Voir aussi

- [[Analyse de vulnérabilités]] — le hub du dossier
- [[Supply chain logicielle et SBOM]] — la notion : SBOM, VEX, suivi dans la durée, hors ligne
- [[Comparatif - Scanners de sécurité]] — Trivy, Grype, Gitleaks, Semgrep et Dependency-Track par usage
