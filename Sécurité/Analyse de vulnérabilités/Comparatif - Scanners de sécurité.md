---
role: comparatif
nom: Comparatif - Scanners de sécurité
categorie: security/analyse
tags: [vulnerability-scanning]
---

# Comparatif - Scanners de sécurité

> On tranche sur : l'usage (composants d'une image ou d'un dépôt, secrets, code source, suivi dans la durée), le fonctionnement hors ligne, la licence de ce que l'outil charge en plus du code (règles, base de vulnérabilités), l'état de maintenance, et les incidents de sécurité subis par l'outil lui-même.

![[Comparatif - Scanners de sécurité.base]]

## Ce qui départage

- [[Trivy]] — le tout-en-un : vulnérabilités d'image, de dépôt et de SBOM, plus secrets, configurations IaC et licences, avec SBOM CycloneDX et SPDX en sortie ; scanner par défaut de Harbor et du Container Scanning de GitLab. Le prix : c'est le seul du lot dont la chaîne de publication a été compromise (2026-03-19 au 2026-03-23, binaire, tags de l'action, images Docker Hub), même si les versions sûres sont publiées et les correctifs annoncés ; sa base agrège des données amont « chacune avec ses propres conditions ».
- [[Grype]] — le comparateur de SBOM : Syft dresse la liste, Grype la confronte à une base quotidienne de 18 sources et se rejoue sur un SBOM déjà livré. Le prix : uniquement des vulnérabilités (ni secrets ni IaC), un scan qui échoue si la base a plus de 120 heures, et une liste de résultats qui diffère de celle de Trivy sur un même SBOM.
- [[Gitleaks]] — les secrets en dur dans l'historique Git, en local et sans compte, avec un hook pre-commit. Le prix : l'auteur l'a déclaré complet et se consacre à Betterleaks ; 46 % de précision mesurée en 2023 ; l'action GitHub officielle est sous licence à clé pour les organisations.
- [[Semgrep]] — le code source lui-même, par motifs, avec des règles qu'on écrit. Le prix : l'édition communautaire n'analyse ni entre fichiers ni entre fonctions, et les règles du registre sont sous une licence d'usage interne qui interdit de les redistribuer ou de les offrir en service — le seul du lot dont la licence touche directement une ESN.
- [[Dependency-Track]] — le seul à **garder la mémoire** : il ingère les SBOM de chaque version livrée et alerte quand une nouvelle CVE touche l'une d'elles. Le prix : un serveur Java avec PostgreSQL à exploiter, aucun scanner intégré, CycloneDX seul, et une documentation hors ligne que le projet déclare inachevée.

**Critère par critère**

**Usage.** Composants d'une **image** : [[Trivy]] et [[Grype]] (Syft en amont pour ce dernier). Composants d'un **dépôt** : [[Trivy]] lit `uv.lock`, `poetry.lock`, `Pipfile.lock` et `requirements.txt` sans installer le projet ; [[Grype]] scanne un répertoire ou un SBOM. **Secrets** : [[Gitleaks]] en spécialiste ; [[Trivy]] en ajoute un détecteur aux règles intégrées, sans mesure de précision documentée. **Code** : [[Semgrep]] seul — aucun des quatre autres ne lit le code source. **Suivi d'un parc livré** : [[Dependency-Track]] seul.

**Hors ligne.** [[Gitleaks]] : tout est local, la documentation n'évoque pourtant pas l'hors ligne (à vérifier sur le site cible). [[Trivy]] : la base s'extrait comme artefact OCI (`trivy image --download-db-only`, ORAS) et se sert depuis un registre interne ; `--skip-db-update`, `--skip-java-db-update`, `--offline-scan` ; le bundle de contrôles IaC est embarqué dans le binaire ; aucun âge maximal de base trouvé. [[Grype]] : `grype db import` d'une archive d'environ 175 Mio, miroir HTTP interne possible, **mais le scan échoue au-delà de 120 heures** sauf réglage. [[Semgrep]] : des règles locales suffisent (`--config ./regles/`) ; le registre exige le réseau et la télémétrie est active par défaut (`--metrics=off`). [[Dependency-Track]] : l'analyseur interne ne sort pas, NVD et OSV se servent depuis des miroirs internes à construire soi-même, GitHub Advisories ne se mire pas.

**Intégration CI.** [[Trivy]] : `aquasecurity/trivy-action`, détournée en mars 2026 — épingler par SHA ; tâche Azure DevOps officielle. [[Grype]] : `anchore/scan-action` (SARIF par défaut) et `anchore/sbom-action` ; l'analyseur Grype de GitLab est déprécié et cesse à GitLab 19.0. [[Gitleaks]] : hook pre-commit officiel, `gitleaks-action` à clé de licence pour les organisations — appeler le binaire directement évite la question. [[Semgrep]] : conteneur `semgrep/semgrep` avec des modèles pour sept CI ; l'action `semgrep-action` est archivée. [[Dependency-Track]] : API REST, plugin Jenkins, GitHub Action.

**Faux positifs.** Aucun scanner ne se lit seul : sur un même SBOM, [[Trivy]] et [[Grype]] divergent (1 contre 37 résultats pour un SBOM Conan, discussion n° 10447 du dépôt Trivy). [[Trivy]] : `.trivyignore.yaml` avec expiration, `--ignore-unfixed` (masque du réel), VEX expérimental. [[Grype]] : règles `ignore`, VEX OpenVEX et CSAF, `--show-suppressed`. [[Gitleaks]] : `gitleaks:allow`, `.gitleaksignore`, `--baseline-path`. [[Semgrep]] : `nosemgrep`, `--baseline-commit` ; l'étude financée par l'éditeur donne 44 à 48 % de vrais positifs pour l'édition communautaire sur des applications de démonstration. [[Dependency-Track]] : états d'analyse, suppression justifiée, VEX CycloneDX, qui survivent aux réévaluations.

**Licence.** [[Trivy]], [[Grype]] et [[Dependency-Track]] : Apache-2.0. [[Gitleaks]] : MIT (l'action : licence personnalisée). [[Semgrep]] : moteur LGPL-2.1, règles sous « Semgrep Rules License v1.0 » — **c'est la seule licence restrictive du lot**, avec l'offre payante de l'éditeur pour ce que la communauté n'a pas. Aucune **base de vulnérabilités** n'a de licence distincte de celle du code, ni pour [[Trivy]] ni pour [[Grype]] : Anchore publie la sienne « sans coût », celle de Trivy agrège des sources aux conditions propres ; [[Dependency-Track]] demande un compte gratuit pour OSS Index et réserve Snyk et VulnDB à des abonnements.

**Maintenance et incidents de l'outil lui-même.** [[Trivy]] : v0.74.0 (2026-08-14), incident critique GHSA-69fq-xp46-6x23 de mars 2026. [[Grype]] : v0.119.0 (2026-09-17), un avis haut (CVE-2025-65965, identifiants de registre écrits dans les sorties JSON, corrigé en 0.104.1), aucune compromission relevée. [[Gitleaks]] : v8.30.1 (2026-03-21), aucune version depuis, correctifs de sécurité seulement, pas d'avis GitHub publié. [[Semgrep]] : v1.178.0 (2026-09-23), une version par semaine, pas d'avis GitHub publié. [[Dependency-Track]] : v5.1.1 (2026-09-20), neuf avis sans aucun de 2026, v4 en fin de vie prévue fin 2026.

**Pas de fiche ici**, faute d'avoir passé le critère « éprouvé et utile en on-prem » (le plafond est de cinq briques) :

- **Syft** — Apache-2.0, v1.52.0 (2026-09-17), environ 9 600 étoiles : le générateur de SBOM d'Anchore, compagnon de Grype. Non retenu à part : Trivy produit aussi un SBOM, et la fiche [[Grype]] documente ce qui le concerne. C'est le premier candidat à une fiche si un site a besoin d'un générateur indépendant du scanner.
- **TruffleHog** — **AGPL-3.0**, v3.97.9 (2026-09-24), environ 28 200 étoiles, plus de 800 détecteurs. Trois raisons de ne pas le retenir pour cet usage : la licence, dont aucune source officielle ne dit l'effet pour un usage interne ou une livraison à un client ; la **vérification active**, qui envoie chaque secret candidat au fournisseur concerné (désactivable par `--no-verification`) ; la vérification de mise à jour au lancement (désactivable par `--no-update`). Sans ces deux options, il n'est pas utilisable hors ligne. Un CVE d'exécution de code via `core.fsmonitor` (CVE-2025-41390, Cisco Talos, 7,8) a été corrigé en octobre 2025. Il reste le bon choix quand la vérification de vivacité est voulue.
- **pip-audit** — PyPA, Apache-2.0, v2.10.1 (2026-06-10), environ 24,5 millions de téléchargements mensuels PyPI. Écarté : **aucun mode hors ligne documenté** (son mainteneur écrit qu'il a toujours besoin d'une forme d'accès en ligne), pas de prise en charge de `uv.lock` (demande fermée « non prévue » en juillet 2026, renvoi vers `uv audit`), et des paquets Python seulement. Il reste pertinent dans un poste connecté qui ne veut que du PyPI.
- **Bandit** — PyCQA, Apache-2.0, v1.9.4 (2026-02-25), environ 8 300 étoiles. Écarté : aucun commit humain depuis février 2026, ni version depuis, et les règles `S` de [[Ruff]] sont un portage de flake8-bandit (documentation de Ruff) ; trois tests récents de Bandit (B613 à B615) n'apparaissent pas dans les codes de Ruff.
- **OSV-Scanner** (Google, Apache-2.0, v2.6.0 du 2026-09-14) — hors des candidats d'origine, mais à connaître : il lit `uv.lock` et `pylock.toml` et a un vrai mode hors ligne (`--offline`, bases téléchargeables).
- **Betterleaks** (MIT, successeur annoncé de Gitleaks, v1.9.0 du 2026-09-29, environ 2 100 étoiles) : trop récent pour le critère. **Opengrep** (fork LGPL-2.1 de Semgrep, environ 3 100 étoiles) : dépôt de règles archivé depuis novembre 2025. **detect-secrets** (Yelp), **git-secrets** (AWS), **Kingfisher** (MongoDB), **ggshield** (GitGuardian, clé d'API requise, donc impraticable hors ligne) : non évalués en détail. **CodeQL** : son interface en ligne de commande n'autorise les bases de données que pour du code open source, hors licence GitHub payante. **SonarQube Community Build** : sources en désaccord sur ce que l'édition libre comprend.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Analyse de vulnérabilités]] — le hub du dossier.
- [[Supply chain logicielle et SBOM]] — la notion : SBOM, VEX, image contre dépendances, ce qu'un scanner ne voit pas, hors ligne.
