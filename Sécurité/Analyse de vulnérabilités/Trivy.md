---
role: brique
nom: Trivy
alias: [trivy, aquasecurity trivy, trivy scanner]
pitch: "Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées)."
categorie: security/analyse
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Grype]]", "[[Gitleaks]]"]
complements: ["[[Docker]]", "[[Podman]]", "[[Kubernetes]]", "[[GitHub Actions]]", "[[Dependency-Track]]", "[[Harbor]]", "[[Zot]]"]
tags: [vulnerability-scanning, sbom, secret-scanning, supply-chain, container, ci-cd]
url_docs: https://trivy.dev/latest/docs/
url_repo: https://github.com/aquasecurity/trivy
---

# Trivy

<!-- AUTO:BANDEAU:START -->
> Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Scanner en ligne de commande d'Aqua Security. Une commande, plusieurs **cibles** (image de conteneur, répertoire, dépôt Git, image de VM, cluster Kubernetes, SBOM) et plusieurs **détecteurs** : vulnérabilités des paquets d'OS et des dépendances de langage, secrets, configurations d'infrastructure (Dockerfile, Kubernetes, Terraform, Helm) et licences. Il sait aussi **produire** un SBOM (CycloneDX, SPDX) et en relire un. Les vulnérabilités viennent d'une base publiée comme artefact OCI sur `ghcr.io`, reconstruite toutes les 6 heures ; pour les paquets d'OS, Trivy suit les avis de la distribution plutôt que le NVD. Relevé le 2026-09-30 : **v0.74.0** (2026-08-14), environ 38 100 étoiles, dernier commit le jour même, licence **Apache-2.0**. C'est le scanner le plus installé du lot — scanner par défaut de Harbor et du Container Scanning de GitLab — et c'est aussi le seul à avoir été compromis : voir *Incident de 2026*.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un seul outil pour l'image livrée, le dépôt du projet, les Dockerfile et manifestes, et les secrets oubliés | Aucun moyen de transférer la base dans le site : sans elle, ni l'image ni le dépôt ne se scannent |
| Un scan de **dépôt** qui lit les verrous Python (`uv.lock`, `poetry.lock`, `Pipfile.lock`, `requirements.txt`) sans installer le projet | Un suivi dans la durée d'un parc d'images déjà livrées : Trivy ne garde rien d'un scan à l'autre |
| Un SBOM CycloneDX ou SPDX produit par la même commande que le scan | Des binaires copiés à la main ou compilés hors distribution : la documentation dit qu'il ne les analyse pas |
| Une base qui se met en miroir dans un registre interne, pour un site sans internet | Une politique qui interdit un outil dont la chaîne de publication a été compromise : à arbitrer avec le client, les versions actuelles étant publiées en releases immuables |

## Mise en œuvre

- Installation — un binaire Go unique ; paquets deb et rpm, Homebrew, images `aquasec/trivy` et `ghcr.io/aquasecurity/trivy`, script `get.trivy.dev`
- Point d'entrée — `trivy image <nom>`, `trivy fs .`, `trivy repo <url>`, `trivy k8s`, `trivy sbom <fichier>` ; `--scanners vuln,secret,misconfig,license` choisit les détecteurs (pour `image` et `fs`, vulnérabilités et secrets sont actifs d'office) ; `--format` : table, json, sarif, cyclonedx, spdx, spdx-json, gabarit ; `--severity` et `--ignore-unfixed` filtrent
- Prérequis — **épingler la version** : jamais v0.69.4 ni les images 0.69.5 et 0.69.6 ; vérifier le binaire avec cosign, comme le recommande l'éditeur ; dans GitHub Actions, épingler `aquasecurity/trivy-action` et `aquasecurity/setup-trivy` par **SHA complet**. Hors ligne : `trivy image --download-db-only` sur une machine connectée (ou `oras pull ghcr.io/aquasecurity/trivy-db:2`), copie de la base dans `${TRIVY_CACHE_DIR}/db/`, puis `--skip-db-update --skip-java-db-update --skip-check-update` ; `--offline-scan` évite Maven Central ; `--db-repository`, `--java-db-repository` et `--checks-bundle-repository` visent un miroir OCI interne (crane, ORAS ou regclient pour le remplir, media types non standard)
- Exécution — local ou en CI ; une image se lit depuis Docker, containerd, Podman (≥ 2.0, local seulement) ou un registre, dans cet ordre par défaut, ou depuis une archive tar ; aucun serveur à héberger
- Coût — gratuit. Le dépôt de la base est sous Apache-2.0, mais elle agrège des données amont « chacune avec ses propres conditions » : à relire avant de redistribuer un miroir à un client. Aucune taille officielle de la base publiée ; des agrégateurs tiers donnent 48 à 54 Mo compressés, non mesurés ici

## Incident de 2026

Établi par l'avis officiel **GHSA-69fq-xp46-6x23** (CVE-2026-33634, gravité critique, publié le 2026-03-21) et le billet d'Aqua :

- **2026-03-19** — le binaire **v0.69.4** est publié avec une charge malveillante (voleur d'identifiants), de 18 h 22 à environ 21 h 42 UTC ; **76 tags sur 77** de `trivy-action` sont réécrits vers des commits malveillants (environ 12 heures) et les tags `v0.2.0` à `v0.2.6` de `setup-trivy` (environ 4 heures). Toutes les voies de diffusion sont touchées : GHCR, ECR Public, Docker Hub, paquets deb et rpm, `get.trivy.dev`.
- **2026-03-22 et 23** — les images Docker Hub **0.69.5 et 0.69.6** sont poussées avec des identifiants d'une autre organisation GitHub de l'éditeur (environ 10 heures), sans tag GitHub correspondant.
- **Versions sûres selon Aqua** : binaire v0.69.2 et v0.69.3 (et antérieures), `trivy-action` v0.35.0, `setup-trivy` v0.2.6. Les images référencées par digest, les binaires compilés depuis les sources et Homebrew n'ont pas été touchés.
- **Cause** : Aqua la rattache à un premier incident du 2026-02-27 au 2026-03-01 (un workflow `pull_request_target` exploité, un jeton d'accès volé), dont la rotation des identifiants n'avait pas été atomique. Correctifs annoncés : jetons révoqués, `pull_request_target` supprimé, épinglage par SHA, releases immuables, attestations SLSA.
- **À faire si une CI a exécuté ces versions** (recommandations d'Aqua) : faire tourner tous les secrets accessibles au pipeline, relire les journaux du 19 au 20 mars, chercher un dépôt nommé `tpcp-docs` sur le compte de l'organisation, bloquer le domaine et l'adresse de la destination d'exfiltration.
- **Établi seulement par des tiers** : l'attribution à « TeamPCP », que le logiciel malveillant revendique et qu'Aqua dit pouvoir être une fausse piste (Wiz, StepSecurity) ; des retombées chez d'autres projets, dont deux versions de LiteLLM sur PyPI le 2026-03-24, que son éditeur rattache lui-même à la dépendance Trivy.
- **Leçon** : un scanner de sécurité en CI s'exécute avec les secrets du pipeline. Il est une surface d'attaque au même titre que l'application qu'il examine. Aqua précise que le badge « release immuable » de GitHub ne suffit pas à empêcher le déplacement d'un tag : l'épinglage par SHA reste la protection.
- Aucune activité suspecte depuis le 2026-03-23 selon l'éditeur ; trois avis plus modestes ont suivi en juin 2026 (deux traversées de chemin, une bombe tar Helm), sans rapport avec la chaîne de publication.

## Limites à connaître

- **Il ne voit que ce que les métadonnées déclarent.** Les binaires ou paquets installés hors gestionnaire, sans avis amont, échappent au scan d'OS ; pour Go, Trivy lit les modules embarqués dans le binaire mais ne dit pas si la fonction vulnérable est appelée.
- **Sur un dépôt, pas de paquets d'OS** : `trivy fs` ne détecte pas l'OS. `requirements.txt` n'est lu que pour les versions épinglées par `==`, et contient rarement les dépendances transitives : `pip freeze` ou `pip-compile` en donne la liste complète.
- **Filtrer masque.** `--ignore-unfixed` cache des vulnérabilités réelles sans correctif ; le mode de détection par défaut (`precise`) réduit le bruit au prix de détections manquées.
- **VEX expérimental** : quatre façons de fournir un document (dépôt, fichier, attestation OCI, référence dans le SBOM) ; le VEX Hub par défaut exige le réseau, sauf à l'auto-héberger.
- **Les secrets** : règles intégrées (clés AWS, jetons GitHub, GitLab, Slack…) et règles propres via `trivy-secret.yaml` ; aucune mesure de précision n'est documentée.
- Le scan de cluster Kubernetes est marqué expérimental ; l'opérateur Trivy est un projet séparé.

## Écosystème

### Alternatives

- [[Grype]] — Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours.
- [[Gitleaks]] — Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT. — pour la seule détection de secrets : un moteur spécialisé, local, sans vérification en ligne.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — une image locale se scanne par le socket Docker, sans registre.
- [[Podman]] — Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`. — Podman ≥ 2.0 local est lu directement ; le Podman distant n'est pas pris en charge.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — `trivy k8s` scanne un cluster (fonction expérimentale) ; l'opérateur Trivy est un projet distinct.
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — l'action officielle `aquasecurity/trivy-action` est celle qui a été détournée en mars 2026 : épinglage par SHA.
- [[Dependency-Track]] — Plateforme OWASP (Apache-2.0, Java) qui ingère des SBOM CycloneDX et suit dans la durée les vulnérabilités des composants d'un portefeuille de projets, avec alertes sur les nouvelles CVE, politiques et VEX — elle ne scanne rien elle-même, exige PostgreSQL, et sa documentation hors ligne est encore incomplète. — Trivy produit le SBOM CycloneDX que Dependency-Track ingère, et peut servir d'analyseur via un serveur Trivy séparé.
- [[Harbor]] — Registre d'images OCI complet (Apache-2.0, Go, CNCF gradué) : projets avec droits et quotas, SSO LDAP et OIDC, réplication et proxy cache vers d'autres registres, scan Trivy, signatures Cosign et Notation — lourd à exploiter (PostgreSQL, un cache Redis ou Valkey, 4 Go de RAM au minimum, installateur hors ligne de 700 Mo). — son adaptateur Trivy fait de Harbor un point de scan à la publication.
- [[Zot]] — Registre OCI léger en un seul binaire (Apache-2.0, Go, CNCF sandbox) : stockage sur disque ou S3 compatible, sans base de données externe, synchronisation et miroir à la demande, scan Trivy embarqué ; interface et recherche en extensions, contrôle d'accès par dépôt et non par projet. — l'embarque comme bibliothèque pour scanner les images du registre.

## Ressources

- Documentation — https://trivy.dev/latest/docs/
- Dépôt — https://github.com/aquasecurity/trivy
- Documentation — environnement isolé : https://trivy.dev/latest/docs/advanced/air-gap/
- Documentation — base de vulnérabilités et miroirs : https://trivy.dev/latest/docs/configuration/db/
- Documentation — fichiers Python lus : https://trivy.dev/latest/docs/coverage/language/python/
- Article — avis de sécurité de l'incident de mars 2026 : https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23
- Article — billet d'Aqua Security : https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/
- Article — analyse de Wiz : https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack

## Voir aussi

- [[Analyse de vulnérabilités]] — le hub du dossier
- [[Supply chain logicielle et SBOM]] — la notion : ce qu'un SBOM dit, image contre dépendances, ce qu'un scanner ne voit pas, hors ligne
- [[Comparatif - Scanners de sécurité]] — Trivy, Grype, Gitleaks, Semgrep et Dependency-Track par usage
