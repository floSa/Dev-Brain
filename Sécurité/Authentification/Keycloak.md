---
role: brique
nom: Keycloak
alias: [keycloak sso, red hat build of keycloak, rhbk]
pitch: "Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter."
categorie: security/auth
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Authentik]]", "[[Authelia]]"]
complements: ["[[Grafana]]", "[[Airflow]]", "[[Langfuse]]", "[[Argo CD]]", "[[Kubernetes]]", "[[OpenMetadata]]", "[[DataHub]]", "[[CVAT]]"]
tags: [authentication, sso, identity-provider, self-hosted]
url_docs: https://www.keycloak.org/documentation
url_repo: https://github.com/keycloak/keycloak
---

# Keycloak

<!-- AUTO:BANDEAU:START -->
> Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Fournisseur d'identité et de gestion des accès en Java sur Quarkus. Il tient les **utilisateurs** dans une base SQL (ou les fédère depuis LDAP, Active Directory, SSSD et FreeIPA), authentifie (mot de passe, TOTP et HOTP, WebAuthn, passkeys, codes de récupération) et émet les jetons de ses applications par **OpenID Connect, OAuth 2.0 et SAML 2.0**, fournisseur comme service. Il sait aussi jouer l'intermédiaire (*identity brokering*) vers des fournisseurs sociaux, OIDC, SAML, SPIFFE ou Kubernetes. L'isolation se fait par *realm* : un espace d'utilisateurs, de clients et de politiques par organisation. SCIM est documenté mais classé *preview* dans les notes de la 26.7. Relevé le 2026-09-30 : **26.7.4** (2026-09-16), environ 37 100 étoiles, dernier commit le jour même ; une mineure environ tous les trois mois, des correctifs toutes les deux à quatre semaines, des rétroportages sur les branches précédentes.

**Licence : Apache-2.0, et rien n'est gardé en payant.** Aucune fonction du dépôt n'est réservée à une édition. Red Hat vend un support à long terme d'une build maison, la *Red Hat build of Keycloak* ; le contenu exact de cette offre n'a pas été trouvé. **Statut CNCF : incubating**, accepté le 2023-04-10 ; le site de la fondation ne mentionne aucune graduation. La gouvernance est par consensus des mainteneurs, à la majorité des deux tiers en cas d'objection.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Du SAML 2.0 et de l'OIDC servis ensemble, avec fédération d'un annuaire d'entreprise (LDAP ou AD) que l'organisation garde | Une petite équipe qui veut juste protéger quelques outils derrière un proxy : la JVM, la base et la surface d'administration coûtent plus que [[Authelia]] |
| Plusieurs organisations ou environnements isolés dans une seule instance (*realms*) | Un service à démarrer dans peu de mémoire : 1 250 Mo de RAM par pod pour 10 000 sessions en cache selon la documentation, avant le système |
| Le produit auquel les documentations d'applications pensent d'abord : [[Grafana]], [[Airflow]], [[Langfuse]] et [[Argo CD]] ont chacun leur page ou leurs variables pour lui | Des flux de connexion à composer en interface avec des étapes et des politiques : c'est le modèle d'[[Authentik]] |
| Un support commercial possible (Red Hat) et un projet adossé à la CNCF, sans édition qui verrouille | Un rythme de correctifs de sécurité à ne pas suivre : 13 avis de gravité haute en 24 mois |
| | Une haute disponibilité simple : le multi-cluster v2, sans Infinispan externe, est encore *preview* |

## Mise en œuvre

- Installation — image `quay.io/keycloak/keycloak` (OpenJDK 21 ; Java 25 pris en charge depuis la 26.6.0) ; opérateur Kubernetes et OpenShift, par OLM ou `kubectl` — aucun chart Helm officiel trouvé dans la documentation de l'opérateur
- Point d'entrée — la console d'administration, un *realm* par organisation, un *client* par application ; la commande `kc.sh start` avec `--hostname`, `--proxy-headers` et la base ; les bases prises en charge sont PostgreSQL 14 à 18, MariaDB, MySQL 8.0 et 8.4, MSSQL et Oracle — la base `dev-file` n'est que pour le développement
- Prérequis — derrière un reverse proxy : `--proxy-headers forwarded|xforwarded`, avec `proxy-trusted-addresses` (par défaut, toutes les adresses sont de confiance) ; le proxy doit **écraser** les en-têtes `X-Forwarded-*` et supprimer `X-Real-IP` et `X-Original-URL` ; trois modes : ré-chiffrement (recommandé), passthrough (avec `--proxy-protocol-enabled`) et *edge* (`--http-enabled=true`)
- Exécution — dimensionnement documenté : 1 vCPU pour 15 connexions par mot de passe par seconde ; haute disponibilité en cluster unique, ou multi-cluster v1 (Infinispan externe et répartiteur), ou v2 *preview* (environ deux fois plus de CPU et d'IOPS d'écriture sur la base) ; la migration de la base se fait au démarrage ou par scripts SQL générés
- Coût — gratuit sous Apache-2.0 ; support optionnel chez Red Hat

## Limites à connaître

- **Aucun avis critique en 24 mois, mais 13 de gravité haute, dont 11 en cinq mois** (mai à septembre 2026) : contournement de la protection anti-rejeu (CVE-2026-90997, 2026-09-16), confusion d'algorithme JWT (CVE-2026-11800, 2026-06-26), forge de rôle par la politique d'enregistrement dynamique par défaut (CVE-2026-16102, 2026-08-06), import de métadonnées d'un courtier SAML qui désactive la vérification de signature (CVE-2026-16443), assertions SAML chiffrées mal validées (CVE-2026-2092, 2026-05-29), contournement d'autorisation par URI non normalisée (CVE-2026-15573). La note de la 26.7.4 annonce à elle seule six CVE. **Suivre les versions de correctif est une charge d'exploitation.**
- **Ruptures de comportement dans la série 26** : rejet par défaut des URI de redirection contenant `state` ou `code` (26.7.3), DN d'autorité exigé pour X.509 (26.7.0), audience vérifiée à l'introspection (26.6.2), normalisation des URI dans les services d'autorisation (26.7.4). Lire les notes avant chaque mise à jour.
- `hostname-strict` vaut vrai par défaut : un nom d'hôte mal déclaré derrière un proxy casse les redirections plutôt que de tomber en silence.
- L'empreinte JVM et la surface de configuration sont plus lourdes que celles d'[[Authelia]], ce qui est le prix de l'étendue fonctionnelle.

## Écosystème

### Alternatives

- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — même terrain (OIDC, SAML, LDAP), avec une interface de flux composables, contre une référence plus installée.
- [[Authelia]] — Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante). — le portail léger, sans SAML, contre un fournisseur complet.

### Compléments

- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — sa documentation a une page dédiée à Keycloak (`auth.generic_oauth`).
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — fournisseur `keycloak` du provider FAB, et un *auth manager* Keycloak déclaré alpha.
- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry. — variables `AUTH_KEYCLOAK_*` dédiées à l'authentification unique.
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — sa documentation décrit Keycloak en OIDC natif avec PKCE.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — l'opérateur Keycloak s'y déploie ; l'API de Kubernetes accepte l'OIDC mais ne fournit pas de fournisseur.
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — SSO listé parmi les fournisseurs de la page de sécurité d'OpenMetadata.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — OIDC : la documentation de DataHub le cite en lien de référence, sans guide dédié.
- [[CVAT]] — Outil d'annotation pour la vision — images, vidéo, nuages de points 3D — avec boîtes, polygones, masques, squelettes, cuboïdes et suivi d'objets par interpolation, 27 formats d'export et pré-annotation par fonctions serverless (SAM, YOLOv7, Detectron2) ; MIT, mais SSO, contrôle qualité automatique, analytics et agents sont réservés à l'édition Enterprise. — guide de configuration OIDC et SAML dans la page SSO de CVAT, valable pour l'édition Enterprise seulement.

## Ressources

- Documentation — https://www.keycloak.org/documentation
- Dépôt — https://github.com/keycloak/keycloak
- Documentation — derrière un reverse proxy : https://www.keycloak.org/server/reverseproxy
- Documentation — bases de données : https://www.keycloak.org/server/db
- Documentation — dimensionnement mémoire et CPU : https://www.keycloak.org/high-availability/single-cluster/concepts-memory-and-cpu-sizing
- Documentation — haute disponibilité : https://www.keycloak.org/high-availability/introduction
- Documentation — mise à jour : https://www.keycloak.org/docs/latest/upgrading/index.html
- Documentation — avis de sécurité : https://github.com/keycloak/keycloak/security/advisories
- Documentation — gouvernance et adopteurs : https://github.com/keycloak/keycloak/blob/main/GOVERNANCE.md
- Documentation — statut CNCF : https://www.cncf.io/projects/keycloak/

## Voir aussi

- [[Authentification]] — le hub du sous-domaine
- [[Comparatif - Fournisseurs d'identité]] — ce qui départage les trois fournisseurs : protocoles, fédération, MFA, empreinte, exploitation, fonctions payantes
- [[OAuth2 et OpenID Connect]] — la notion : flux, jetons, pièges, ce que fait un fournisseur d'identité
