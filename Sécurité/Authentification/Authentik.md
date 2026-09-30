---
role: brique
nom: Authentik
alias: [authentik sso, goauthentik]
pitch: "Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois."
categorie: security/auth
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Keycloak]]", "[[Authelia]]"]
complements: ["[[Traefik]]", "[[Caddy]]", "[[Nginx]]", "[[Airflow]]", "[[Langfuse]]"]
tags: [authentication, sso, identity-provider, self-hosted]
url_docs: https://docs.goauthentik.io/
url_repo: https://github.com/goauthentik/authentik
---

# Authentik

<!-- AUTO:BANDEAU:START -->
> Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-core | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Fournisseur d'identité dont la logique de connexion se **construit** : chaque parcours (connexion, inscription, récupération de mot de passe, enrôlement MFA) est un *flux* fait d'étapes (*stages*) et de politiques que l'administrateur assemble dans l'interface, au lieu de choisir parmi des options figées. Il sert des applications par OIDC et OAuth 2.0, SAML, LDAP, SCIM et RADIUS, et protège celles qui n'ont aucune notion de connexion par un *proxy provider* — trois modes : proxy, *forward auth* par application, *forward auth* au niveau du domaine. Des **outposts** (proxy, LDAP, RADIUS, accès distant) s'exécutent à part et exposent des métriques Prometheus. Les utilisateurs sont dans PostgreSQL ; **Redis a été retiré** à la version 2025.10. Relevé le 2026-09-30 : **2026.8.3** (2026-09-17), environ 25 800 étoiles ; la certification OpenID a été obtenue à la 2026.8, avec l'échange de jetons et l'enregistrement dynamique de clients.

**Licence : MIT pour le cœur, propriétaire pour un dossier.** Le fichier LICENSE prévoit des exceptions : le site en CC BY-SA 4.0, et `authentik/enterprise/` sous une licence propriétaire — libre pour le développement et le test, abonnement obligatoire en production. Les deux éditions **partagent les mêmes images** ; la clé de licence se valide localement, donc en réseau isolé. Prix public : édition libre gratuite, sans support ; **Enterprise 5 $ par utilisateur et par mois** (facturation annuelle, plus 0,02 $ par utilisateur externe) ; Enterprise Plus à partir de 20 k$ par an, avec support dédié — mêmes fonctions.

**Ce que l'édition Enterprise verrouille** (page « enterprise features ») : le provisioning (comptes d'agents, départs planifiés, synchronisation Google Workspace et Entra ID, fournisseurs SSF et WS-Federation, OAuth pour SCIM), l'accès privilégié temporaire avec approbation (PAM), l'historique de mots de passe, les certificats clients et RADIUS EAP-TLS, l'audit renforcé (valeurs avant et après, exports, revues périodiques) et les connecteurs d'appareils. La même liste range aussi les « sources OAuth et SAML externes » côté payant, ce qui surprend pour des sources : point à revérifier à la source avant de compter dessus.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un fournisseur d'identité **et** un portail de forward auth dans un seul produit, avec une interface pour composer les parcours | L'audit renforcé, le provisioning vers Entra ou Google, le PAM ou les certificats clients sont nécessaires sans budget : ils sont dans l'édition payante |
| Une équipe qui veut LDAP, RADIUS ou SCIM servis en plus d'OIDC et de SAML | Le SAML **côté source** (recevoir des assertions d'un autre fournisseur) est critique : cette surface a concentré la plupart des avis de 2026 |
| Des applications sans authentification derrière [[Traefik]], [[Caddy]] ou [[Nginx]] : chacun a sa page officielle d'intégration | Un projet à support long : seules deux versions (2026.5.x et 2026.8.x) reçoivent des correctifs, sans rétrogradation possible |
| Un environnement Kubernetes ou Compose, PostgreSQL déjà exploité (16 dans le Compose officiel) | Un parc minuscule où un portail à fichier YAML suffit : [[Authelia]] tient dans quelques dizaines de mégaoctets |
| | Une fédération multi-*realms* éprouvée par de très grands parcs et un support vendu par un grand éditeur : [[Keycloak]] |

## Mise en œuvre

- Installation — Docker Compose officiel : `postgres:16-alpine`, un service `server` et un service `worker` (`ghcr.io/goauthentik/server:2026.8.3`, ports 9000 et 9443) ; chart Helm à `https://charts.goauthentik.io`, dont le PostgreSQL embarqué est réservé au test
- Point d'entrée — l'interface d'administration ; pour un proxy, un *provider* de type proxy par application et un outpost, puis la page d'intégration du proxy visé (Traefik, Caddy, Nginx, ainsi qu'Envoy et HAProxy)
- Prérequis — 2 cœurs et 2 Go de RAM au minimum documentés ; **le worker monte le socket Docker** dans le Compose, ce que la documentation déconseille sans proxy de socket ; à la 2026.8, les en-têtes de proxy ne sont crus que des proxys de confiance : renseigner `AUTHENTIK_LISTEN__TRUSTED_PROXY_CIDRS` **avant** de migrer, sous peine d'erreurs HTTP et HTTPS
- Exécution — mise à jour : sauvegarder PostgreSQL d'abord, **aucun retour arrière**, ne pas sauter de version majeure, et faire tourner instance et outposts à la même version
- Coût — édition libre gratuite ; Enterprise à 5 $ par utilisateur et par mois

## Limites à connaître

- **Des avis de sécurité critiques en 2026** : une exécution de code à distance authentifiée par l'endpoint de test des mappings (CVE-2026-25227, 2026-02-12), un XSS réfléchi (CVE-2026-42849, 2026-05-12), un contournement d'étape de source par un POST vide (CVE-2026-49448, 2026-05-28).
- **Deux avis touchent directement le forward auth derrière un proxy** : un contournement avec un cookie de session malformé sous Traefik et Caddy (CVE-2026-25748, 2026-02-12, gravité haute) et un accès non authentifié par l'en-tête `X-Original-URI` en mode Nginx (GHSA-5wcc-hf24-rf5h, 2026-05-12, sans CVE). Un critique plus ancien, par `X-Forwarded-For` (CVE-2024-47070), date de septembre 2024, juste avant la fenêtre de 24 mois.
- La plupart des autres avis hauts portent sur les **sources SAML**, les élévations de privilèges, le contournement du MFA par courriel et des secrets lisibles avec la seule permission de lecture (septembre 2026).
- Aucune liste d'utilisateurs de l'outil n'est publiée par le projet. Le montant de financement de l'éditeur ne figure que dans des agrégateurs, non retenu ici.

## Écosystème

### Alternatives

- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — la référence installée et le support d'un grand éditeur, contre des flux configurables et un seul produit pour le portail et le fournisseur.
- [[Authelia]] — Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante). — le portail léger, sans édition payante, contre un fournisseur plus large mais plus lourd.

### Compléments

- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — page d'intégration officielle du *provider* proxy avec forward auth.
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — page d'intégration officielle du forward auth.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — page d'intégration officielle, dont ingress-nginx.
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le fournisseur `authentik` figure dans la liste OAuth du provider FAB.
- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry. — variables d'environnement `AUTH_AUTHENTIK_*` dédiées à l'authentification unique.

## Ressources

- Documentation — https://docs.goauthentik.io/
- Dépôt — https://github.com/goauthentik/authentik
- Documentation — fonctions Enterprise : https://docs.goauthentik.io/enterprise/enterprise-features/
- Documentation — tarifs : https://goauthentik.io/pricing/
- Documentation — licence du dossier Enterprise : https://github.com/goauthentik/authentik/blob/main/authentik/enterprise/LICENSE
- Documentation — proxy provider et forward auth : https://docs.goauthentik.io/add-secure-apps/providers/proxy/
- Documentation — installation Compose : https://docs.goauthentik.io/install-config/install/docker-compose/
- Documentation — mise à jour : https://docs.goauthentik.io/install-config/upgrade/
- Documentation — notes de la 2026.8 : https://docs.goauthentik.io/releases/2026.8/
- Documentation — avis de sécurité : https://github.com/goauthentik/authentik/security/advisories

## Voir aussi

- [[Authentification]] — le hub du sous-domaine
- [[Comparatif - Fournisseurs d'identité]] — ce qui départage les trois fournisseurs : protocoles, fédération, MFA, empreinte, exploitation, fonctions payantes
- [[OAuth2 et OpenID Connect]] — la notion : flux, jetons, pièges, ce que fait un fournisseur d'identité
