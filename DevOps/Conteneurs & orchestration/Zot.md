---
role: brique
nom: Zot
alias: [zot, zot registry, project-zot]
pitch: "Registre OCI léger en un seul binaire (Apache-2.0, Go, CNCF sandbox) : stockage sur disque ou S3 compatible, sans base de données externe, synchronisation et miroir à la demande, scan Trivy embarqué ; interface et recherche en extensions, contrôle d'accès par dépôt et non par projet."
categorie: devops/conteneur
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[Harbor]]"]
complements: ["[[Docker]]", "[[Kubernetes]]", "[[Trivy]]"]
tags: [container-registry, self-hosted, supply-chain]
url_docs: https://zotregistry.dev/
url_repo: https://github.com/project-zot/zot
---

# Zot

<!-- AUTO:BANDEAU:START -->
> Registre OCI léger en un seul binaire (Apache-2.0, Go, CNCF sandbox) : stockage sur disque ou S3 compatible, sans base de données externe, synchronisation et miroir à la demande, scan Trivy embarqué ; interface et recherche en extensions, contrôle d'accès par dépôt et non par projet.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Registre d'images **conforme à OCI**, écrit pour être simple : un **binaire unique**, sans privilège root et sans dépendance externe, qui range les images au format OCI *image layout* et parle la spécification de distribution OCI, sans protocole propriétaire. Les fonctions en plus (recherche, synchronisation, scan, métriques, interface) sont des **extensions** du binaire complet. Relevé le 2026-10-01 : **v2.1.21** (2026-09-06), 2 824 étoiles, langage Go, licence **Apache-2.0**. **CNCF sandbox** depuis le 2022-12-13. Cinq mainteneurs listés (Microsoft, Ciroos AI, Geico, Luxoft, AMD) ; la documentation dit que le projet vient de Cisco, sponsor et utilisateur, qui n'a plus de mainteneur listé aujourd'hui. Aucun fichier d'adoptants n'a été trouvé : l'adoption hors Cisco n'est pas établie ici.

**Licence : sans restriction.** Apache-2.0, aucune édition payante relevée : une ESN peut l'installer chez un client, le redistribuer et le proposer comme service. Le projet ne promet ni rythme de versions ni support (page des versions) ; environ une version corrective par mois.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un registre sur une petite machine ou un poste d'atelier, sans PostgreSQL ni cache à exploiter | Des projets avec rôles, comptes robots et quotas de stockage par projet : la documentation lue ne décrit que des politiques d'accès par dépôt |
| Un miroir de registres amont, à la demande ou périodique, avec filtres sur les étiquettes et sur les images signées | Une réplication multi-sites toute faite et une interface de gestion complète : [[Harbor]] est plus mûr |
| Un artefact simple à livrer en réseau fermé : le binaire, 218 Mio pour la version complète, 81 Mio pour la minimale (v2.1.21) | Un client qui veut un projet porté par de nombreuses entreprises depuis des années : Zot est sandbox, avec cinq mainteneurs |
| Du scan Trivy sans service séparé | Un besoin de haute disponibilité clés en main : le mode scale-out existe mais sans auto-guérison |

## Mise en œuvre

- Installation — le binaire (version complète avec extensions, ou minimale), une image de conteneur, ou un déploiement sur Kubernetes ; un fichier de configuration JSON
- Point d'entrée — un fichier de configuration qui déclare le stockage, l'adresse d'écoute, l'authentification et les extensions ; puis `docker push` ou `skopeo copy` vers `zot.exemple:5000/image`
- Prérequis — un stockage : disque local (NFS accepté), S3 compatible, GCS ou Azure Blob. La déduplication passe par des liens physiques ; sur un stockage distant elle exige un cache (DynamoDB, Redis ou BoltDB, ce dernier mono-instance). Pas de base de données externe. Authentification : htpasswd (bcrypt), LDAP, jeton porteur (JWT, OIDC), mTLS, clés d'API ; autorisation par politiques à cinq types (défaut, utilisateur, groupe, anonyme, administrateur), avec des globs et des expressions CEL
- Exécution — ramasse-miettes en ligne, sans arrêt (`gcDelay`, `gcInterval`), vérification périodique de l'intégrité (*scrub*) ; politiques de rétention avec essai à blanc ; métriques Prometheus par extension, ou par l'exporteur externe `zxp` avec le build minimal
- Coût — gratuit ; le coût est la veille sur le projet jeune et l'absence d'un éditeur unique. L'empreinte mémoire n'est documentée par aucun chiffre officiel : la mesurer (l'outil `zb` sert à l'évaluer)

**Fonctions utiles sur site.** La **synchronisation** (`sync`) combine le mode périodique (`pollInterval`) et le mode à la demande (`onDemand`, pull-through) vers tout registre conforme à la spécification de distribution, avec filtres de préfixe et d'étiquette ; `onlySigned: true` ne synchronise que le contenu signé Cosign ou Notation ; la documentation déconseille le mode périodique avec Docker Hub à cause des limites de pull. Le **scan** embarque [[Trivy]] comme bibliothèque ; `dbRepository` et `javaDBRepository` peuvent pointer vers un miroir interne, présenté comme la voie pour le réseau fermé ; la mise à jour de la base invalide le cache et force un nouveau scan complet ; le scan n'est pas supporté en scale-out. La **recherche** (GraphQL) et le CVE se configurent sous l'extension `search`.

**Réseau fermé.** Le binaire est autonome. Pour charger des images sans Internet : `skopeo copy` ou `crane pull` vers une archive, transport physique, puis `skopeo copy` ou `crane push` vers Zot ; la synchronisation ne sert qu'avec un lien réseau vers l'amont. Aucune documentation de Zot ne décrit ce procédé complet : c'est une composition d'outils.

## Limites à connaître

- **Plus jeune et plus petit que Harbor** : sandbox CNCF depuis 2022, 2 824 étoiles contre 29 478, cinq mainteneurs. La page de comparaison du dépôt date de 2021 (Zot 1.3.0) et ne vaut plus.
- **Pas de projets ni de quotas documentés.** Le contrôle d'accès est par dépôt. L'absence de quotas n'est pas prouvée, la documentation de rétention dit simplement ne pas en parler : à tester avant de promettre.
- **Extensions : build complet seulement.** Le binaire minimal n'a ni recherche, ni synchronisation, ni scan, ni interface.
- **Haute disponibilité** : deux voies, aucune clés en main. Actif/passif ou actif/actif avec `sync` et un répartiteur de charge (réplication planifiée, donc une fenêtre de perte si l'actif tombe juste après un push) ; ou scale-out, des instances qui partagent S3 et un cache, sans auto-guérison, avec les dépôts d'une instance en panne indisponibles, et sans CVE ni *trust*.
- **Adoption non établie** hors du sponsor d'origine.

## Écosystème

### Alternatives

- [[Harbor]] — Registre d'images OCI complet (Apache-2.0, Go, CNCF gradué) : projets avec droits et quotas, SSO LDAP et OIDC, réplication et proxy cache vers d'autres registres, scan Trivy, signatures Cosign et Notation — lourd à exploiter (PostgreSQL, un cache Redis ou Valkey, 4 Go de RAM au minimum, installateur hors ligne de 700 Mo). — le registre complet, avec projets, quotas et SSO, au prix d'une exploitation plus lourde.
- voisin : le registre **intégré à une forge** — [[GitLab CE]] ou [[Forgejo]] — quand la forge est déjà installée.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — le client qui pousse et tire les images.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — le cluster qui tire ses images d'un registre interne ; Zot s'installe aussi sur Kubernetes.
- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — embarqué dans Zot comme bibliothèque, sans binaire séparé.

## Ressources

- Documentation — https://zotregistry.dev/
- Dépôt — https://github.com/project-zot/zot
- Documentation — synchronisation : https://zotregistry.dev/v2.1.21/articles/mirroring/
- Documentation — installation sur Kubernetes : https://zotregistry.dev/v2.1.21/install-guides/install-guide-k8s/
- Documentation — CNCF : https://www.cncf.io/projects/zot/
- Dépôt — mainteneurs : https://github.com/project-zot/zot/blob/main/MAINTAINERS.md

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Registres d'images]] — le comparatif : poids, droits, miroir, scan, licence.
