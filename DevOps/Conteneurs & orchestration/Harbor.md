---
role: brique
nom: Harbor
alias: [harbor, goharbor, harbor registry]
pitch: "Registre d'images OCI complet (Apache-2.0, Go, CNCF gradué) : projets avec droits et quotas, SSO LDAP et OIDC, réplication et proxy cache vers d'autres registres, scan Trivy, signatures Cosign et Notation — lourd à exploiter (PostgreSQL, un cache Redis ou Valkey, 4 Go de RAM au minimum, installateur hors ligne de 700 Mo)."
categorie: devops/conteneur
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Zot]]"]
complements: ["[[Docker]]", "[[Kubernetes]]", "[[Helm]]", "[[Trivy]]", "[[Keycloak]]", "[[OpenTofu]]"]
tags: [container-registry, self-hosted, supply-chain]
url_docs: https://goharbor.io/docs/main/
url_repo: https://github.com/goharbor/harbor
---

# Harbor

<!-- AUTO:BANDEAU:START -->
> Registre d'images OCI complet (Apache-2.0, Go, CNCF gradué) : projets avec droits et quotas, SSO LDAP et OIDC, réplication et proxy cache vers d'autres registres, scan Trivy, signatures Cosign et Notation — lourd à exploiter (PostgreSQL, un cache Redis ou Valkey, 4 Go de RAM au minimum, installateur hors ligne de 700 Mo).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Registre d'images de conteneurs **auto-hébergé**, bâti sur la **CNCF Distribution** (le registre de référence) à laquelle il ajoute ce qu'un registre nu n'a pas : des **projets** avec rôles, des comptes robots, des quotas de stockage, l'authentification LDAP ou OIDC, le scan de vulnérabilités, la signature, la réplication et le proxy cache. Relevé le 2026-10-01 : **v2.15.2** (2026-07-02 ; deux préversions 2.15.3 en cours), 29 478 étoiles, langage Go, licence **Apache-2.0**. **CNCF gradué** (accepté le 2018-07-31, gradué le 2020-06-15). Douze mainteneurs listés, issus de plusieurs entreprises, dont VMware, Tencent, OVH Cloud et DataDog ; les affiliations du fichier `MAINTAINERS.md` n'ont pas été revérifiées (VMware est aujourd'hui sous Broadcom).

**Licence : sans restriction.** Apache-2.0, aucune édition payante : une ESN peut l'installer chez un client, le redistribuer et le proposer comme service.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs équipes ou plusieurs clients avec des droits différents par projet, et des quotas | Une seule personne et quelques images : un registre léger suffit ([[Zot]]) |
| Du SSO sur un fournisseur existant (LDAP, OIDC avec [[Keycloak]] ou [[Authentik]]) | Une machine avec moins de 4 Go de RAM : c'est le minimum de la documentation |
| Un miroir de Docker Hub ou d'autres registres (proxy cache), pour ne plus dépendre des quotas de pull | Un client qui ne veut pas exploiter PostgreSQL et un cache en plus du registre |
| Le scan de vulnérabilités et la signature intégrés au registre | Un besoin de haute disponibilité sans cluster : elle passe par le chart Helm et suppose PostgreSQL, un cache et un stockage externes |

## Mise en œuvre

- Installation — l'**installateur hors ligne** (`harbor-offline-installer`, 696 Mio pour la 2.15.2, images comprises) ou en ligne, avec `docker compose` ; ou le chart Helm `harbor-helm` ; HTTPS conseillé, ports 80 et 443
- Point d'entrée — l'interface web et l'API, puis `docker login` et `docker push` vers `harbor.exemple/projet/image` ; un **projet** regroupe les dépôts, les droits, les quotas, la rétention et l'immutabilité des étiquettes
- Prérequis — 2 CPU, 4 Go de RAM et 40 Go de disque au minimum, 4 CPU, 8 Go et 160 Go recommandés (documentation), Docker Engine plus récent que 20.10 et Compose plus récent que 2.3. Composants : portail, cœur, registre, tâches, [[Postgres]], un cache ; les notes de la 2.15.2 annoncent le remplacement de Redis par Valkey comme cache. L'authentification se choisit au départ : on ne bascule plus de la base locale vers LDAP ou OIDC dès qu'un utilisateur local autre que `admin` existe
- Exécution — stockage sur disque par défaut, ou S3 compatible, Azure, GCS, Swift ou OSS ; le **ramasse-miettes** libère l'espace des images supprimées (le quota n'est libéré qu'après lui) ; métriques [[Prometheus]] désactivées par défaut (`metric.enabled`, port 9090) ; un tableau de bord [[Grafana]] d'exemple est dans le dépôt
- Coût — gratuit ; le coût est l'exploitation (sauvegardes de PostgreSQL et du stockage, mises à niveau, ramasse-miettes)

**Fonctions utiles sur site.** Le **scan** utilise [[Trivy]] (activé par `--with-trivy`). La **réplication** pousse ou tire vers Harbor, Docker Hub, GHCR, GCR, ACR, ECR, JFrog et d'autres, et réplique les signatures Cosign ; elle n'est pas supportée entre versions différentes de Harbor. Le **proxy cache** (pull-through) s'adosse à Docker Hub, GHCR, Quay, ECR et d'autres : l'image en cache est servie si l'amont est injoignable, on ne peut pas y pousser, et la vérification de mise à jour par requête HEAD ne consomme pas le quota Docker Hub. Les **signatures** passent par Cosign et Notation ; Notary v1 est retiré. Une **SBOM** SPDX se génère avec Trivy depuis la 2.11. Les règles d'**immutabilité** et de **rétention** se posent par projet (jusqu'à 15 règles). Les charts Helm et les artefacts OCI sont des objets de premier rang.

**Réseau fermé.** Trois choses à amener à la main : l'installateur hors ligne (images de Harbor), les images à héberger (voir plus bas) et la **base de vulnérabilités de Trivy**. La page de documentation « Import Vulnerability Data to an Offline Harbor » ne décrit que Clair, retiré depuis la 2.2 : le procédé actuel est dans le modèle `harbor.yml` du dépôt et le README de l'adaptateur Trivy. Il faut `trivy.skip_update: true` **et** `trivy.offline_scan: true` (le commentaire du modèle précise que le second n'empêche pas le téléchargement de la base), puis monter `trivy.db` et `metadata.json` dans le cache de l'adaptateur, et la base Java à part. Autre voie : pointer `db_repository` vers un registre interne qui miroite les bases. Moins de vulnérabilités sont détectées hors ligne dans les JAR. Pour **charger des images** sans Internet, la réplication ne sert que si les deux registres se voient ; sinon `skopeo copy` vers un dossier ou une archive OCI, `docker save` ou `crane pull`, transport par le support de la zone, puis `skopeo copy` ou `crane push` vers Harbor. Aucune documentation de Harbor ne décrit ce procédé complet : c'est une composition d'outils.

## Limites à connaître

- **Lourd pour ce qu'il fait.** Plusieurs conteneurs, une base PostgreSQL, un cache, un installateur de près de 700 Mio, 160 Go de disque recommandés avant la première image. Pour un registre d'une machine d'atelier, c'est disproportionné.
- **Mise à niveau : sauvegarder avant.** La 2.15.2 fait passer automatiquement la base PostgreSQL interne de la version 15 à la 18 (`pg_upgrade` au démarrage, initialisation plus longue) ; avec des données non ASCII, un `reindexdb` est à lancer en fenêtre de maintenance. L'outil de migration ne documente que les chemins depuis la 2.12. Une base PostgreSQL externe exige la version 12 ou plus.
- **Quota : seulement le stockage, par projet.** Un blob partagé est compté une fois par projet, donc la somme des quotas peut dépasser le disque réel ; les charts Helm ne sont pas comptés ; un push peut être refusé tard, en cours de transfert.
- **Haute disponibilité : par Helm seulement.** Au moins deux réplicas de chaque composant, PostgreSQL et cache externes, stockage partagé. La page de documentation dit que Redis Cluster n'est pas supporté ; elle semble ancienne, la configuration actuelle montre `redis+sentinel`.
- **Scan hors ligne : documentation éclatée** (voir plus haut), à tester avant de promettre le résultat à un client.
- **Gouvernance : plusieurs entreprises, aucun éditeur unique.** Pas de support contractuel de l'amont ; des éditeurs en vendent un.

## Écosystème

### Alternatives

- [[Zot]] — Registre OCI léger en un seul binaire (Apache-2.0, Go, CNCF sandbox) : stockage sur disque ou S3 compatible, sans base de données externe, synchronisation et miroir à la demande, scan Trivy embarqué ; interface et recherche en extensions, contrôle d'accès par dépôt et non par projet. — le registre léger, sans PostgreSQL ni projets ; moins de gestion de droits et de quotas, bien moins d'exploitation.
- voisin : le registre **intégré à une forge** — [[GitLab CE]] en livre un (Free, à activer) et [[Forgejo]] des registres de paquets dont un OCI : pas de service de plus si la forge est déjà là ; la réplication et le proxy cache de Harbor ne figurent pas dans la documentation lue de ces forges.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — le client qui pousse et tire les images.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — le cluster qui tire ses images d'un registre interne ; la haute disponibilité de Harbor passe par son chart Helm.
- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé). — les charts s'y rangent aussi, comme artefacts OCI.
- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — le scanner par défaut de Harbor, par un adaptateur.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — fournisseur OIDC cité par la documentation de Harbor, avec Okta et dex ; [[Authentik]] s'y branche de la même façon, comme tout fournisseur OIDC.
- [[OpenTofu]] — Provisionnement d'infrastructure déclaratif avec un état (MPL-2.0, Go, fork de Terraform 1.5 sous la Linux Foundation, CNCF sandbox) : des fichiers HCL, un plan avant chaque changement, des fournisseurs pour VMware, Proxmox, libvirt, Kubernetes ; chiffrement d'état natif, miroir de fournisseurs pour le réseau fermé — Terraform, lui, est sous BUSL depuis 2023. — le fournisseur `goharbor/harbor` décrit projets, utilisateurs et réplications en code.

## Ressources

- Documentation — https://goharbor.io/docs/main/
- Dépôt — https://github.com/goharbor/harbor
- Documentation — prérequis : https://goharbor.io/docs/main/install-config/installation-prereqs/
- Documentation — réplication : https://goharbor.io/docs/main/administration/configuring-replication/
- Documentation — proxy cache : https://goharbor.io/docs/main/administration/configure-proxy-cache/
- Documentation — haute disponibilité : https://goharbor.io/docs/main/install-config/harbor-ha-helm/
- Dépôt — modèle de configuration : https://github.com/goharbor/harbor/blob/main/make/harbor.yml.tmpl
- Dépôt — adaptateur Trivy : https://github.com/goharbor/harbor-scanner-trivy
- Documentation — Trivy hors ligne : https://trivy.dev/docs/latest/guide/advanced/air-gap/
- Article — notes de la v2.15.2 : https://github.com/goharbor/harbor/releases/tag/v2.15.2
- Documentation — CNCF : https://www.cncf.io/projects/harbor/
- Dépôt — mainteneurs : https://github.com/goharbor/community/blob/main/MAINTAINERS.md

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Registres d'images]] — le comparatif : poids, droits, miroir, scan, licence.
