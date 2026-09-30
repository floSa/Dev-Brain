---
role: brique
nom: Authelia
alias: [authelia sso, portail d'authentification]
pitch: "Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante)."
categorie: security/auth
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Keycloak]]", "[[Authentik]]"]
complements: ["[[Traefik]]", "[[Caddy]]", "[[Nginx]]"]
tags: [authentication, sso, identity-provider, self-hosted, reverse-proxy]
url_docs: https://www.authelia.com/
url_repo: https://github.com/authelia/authelia
---

# Authelia

<!-- AUTO:BANDEAU:START -->
> Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Portail d'authentification et de SSO qui se **place à côté d'un reverse proxy**, jamais devant les applications : à chaque requête, le proxy demande à Authelia « cette personne a-t-elle le droit ? », et Authelia répond oui, non, ou redirige vers son portail de connexion. Le mécanisme est celui du *forward auth* : l'application n'a aucune notion de connexion à porter, ce qui en fait le moyen de protéger un outil qui n'a pas d'authentification (ou seulement un mot de passe unique). Le premier facteur est un mot de passe (fichier YAML de comptes hachés, ou annuaire LDAP : OpenLDAP, FreeIPA, Active Directory) ; le second, TOTP, clé de sécurité, passkey WebAuthn ou push Duo. Relevé le 2026-09-30 : **v4.39.28** (2026-09-17), environ 29 100 étoiles ; aucune 4.40 publiée, alors que la feuille de route l'annonce en cours.

**Ce que le nom laisse croire : un fournisseur OIDC, mais partiel.** Authelia est aussi un fournisseur OpenID Connect **certifié** (profils Basic, Implicit, Hybrid, Form Post, Config OP ; PKCE, PAR, *device flow*, *client credentials*) : une application qui sait faire de l'OIDC s'y branche directement, et la documentation compte plus de 200 guides d'intégration de clients. Ce que la documentation déclare **non implémenté** : les déconnexions OIDC (*Session Management*, *Back-Channel*, *Front-Channel*, *RP-Initiated*), CIBA, l'échange de jetons, le mTLS client. **SAML n'est pas fourni** : le fournisseur SAML 2.0 est « planifié », sans échéance ni bibliothèque choisie. L'OIDC est la seule implémentation de fournisseur d'identité. Les deux pages de la documentation se contredisent sur l'enregistrement dynamique de clients (« non implémenté » dans l'introduction, « Beta 8 » dans la feuille de route) : la fiche suit l'introduction.

**Licence : Apache-2.0, et aucune offre commerciale trouvée.** Projet communautaire créé en 2016, financé par Open Collective, sans fondation ni éditeur. Rien n'est réservé à une édition payante — mais rien n'est vendu non plus : ni support contractuel, ni SLA.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Protéger derrière un proxy des outils qui n'ont pas d'authentification, ou seulement un mot de passe partagé, avec un MFA en plus | SAML : Authelia n'est pas un fournisseur SAML, ni aujourd'hui ni à une date annoncée — [[Keycloak]] ou [[Authentik]] |
| Une petite équipe et un annuaire simple : un fichier YAML ou un LDAP existant, un binaire Go, une mémoire annoncée « normalement sous 30 Mo » | Des utilisateurs qui s'inscrivent, des flux personnalisés, un annuaire à administrer par une interface : pas d'inscription intégrée, les comptes se déclarent en configuration |
| Un proxy [[Traefik]], [[Caddy]] ou [[Nginx]] qui délègue à un service : chacun a sa page d'intégration officielle | Une déconnexion unique propagée à toutes les applications par OIDC : les spécifications de sortie ne sont pas implémentées |
| Des applications qui parlent OIDC et une équipe qui veut un fournisseur léger, certifié, sans JVM | Une multi-location (plusieurs *realms* d'organisations distinctes) ou une fédération vers d'autres fournisseurs d'identité, qui sont le métier de [[Keycloak]] |
| | Un support contractuel : le projet est communautaire, sans édition ni offre commerciale |

## Mise en œuvre

- Installation — image `authelia/authelia` ou `ghcr.io/authelia/authelia` (moins de 20 Mo annoncés), ou un binaire unique ; un chart Helm officiel existe à `https://charts.authelia.com`, **déclaré en bêta** et sujet à ruptures
- Point d'entrée — un fichier de configuration YAML, une base de stockage (SQLite, MySQL ou PostgreSQL, avec une clé de chiffrement de 20 caractères au moins) et, côté proxy, un point d'appel : `/api/authz/forward-auth` pour Traefik (ForwardAuth), `forward_auth` pour Caddy, `/api/authz/auth-request` pour Nginx (`auth_request`, avec les modules `http_auth_request` et `http_realip`)
- Prérequis — **HTTPS uniquement** ; les trois pages d'intégration insistent sur la liste des proxys de confiance, qui décide des en-têtes `X-Forwarded-*` crus ; la haute disponibilité demande des sessions dans Redis (Sentinel pris en charge) — sans Redis, Authelia garde un état local
- Exécution — Authelia n'est jamais connecté directement aux applications ; en OIDC, les applications l'appellent, et il tient alors le rôle de serveur d'autorisation
- Coût — gratuit ; les ruptures de la 4.39 (revendications par défaut du jeton d'identité alignées sur la spécification, image de base minimale glibc, `VOLUME` supprimé) se lisent dans les notes de version ; des dépréciations sont annoncées pour la v5.0.0

## Limites à connaître

- **Aucun avis de sécurité de gravité haute ou critique sur 24 mois** : un modéré (CVE-2026-47203, identifiant non canonisé en Basic Auth avec LDAP, 2026-05-26) et trois faibles ; le dernier avis de gravité haute date de 2021 (contournement d'authentification par l'URI sous Nginx, CVE-2021-32637). C'est le plus faible historique des trois fournisseurs du brain, ce qui tient aussi à sa surface bien plus petite.
- La sécurité de l'ensemble repose sur la **chaîne proxy → Authelia** : un proxy qui laisse passer des en-têtes forgés, ou des applications joignables sans le proxy, annulent la protection.
- Aucune liste d'utilisateurs de l'outil n'est publiée (pas d'`ADOPTERS.md` trouvé) : l'adoption se juge à la taille du dépôt et à la place dans les documentations d'applications tierces.

## Écosystème

### Alternatives

- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — le fournisseur complet, avec SAML et la fédération, contre le portail léger.
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — même terrain (forward auth et OIDC), avec un modèle de flux et une interface d'administration, mais sur PostgreSQL et avec une édition payante.

### Compléments

- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — sa page d'intégration décrit le middleware ForwardAuth vers `/api/authz/forward-auth` ; l'OIDC natif du proxy est dans l'offre Hub, payante.
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — l'exemple officiel de la directive `forward_auth` de Caddy nomme Authelia.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — l'intégration passe par `auth_request`, module à compiler.

## Ressources

- Documentation — https://www.authelia.com/
- Dépôt — https://github.com/authelia/authelia
- Documentation — architecture : https://www.authelia.com/overview/prologue/architecture/
- Documentation — fournisseur OpenID Connect et fonctions non implémentées : https://www.authelia.com/integration/openid-connect/introduction/
- Documentation — feuille de route (SAML, déconnexions OIDC) : https://www.authelia.com/roadmap/active/openid-connect-1.0-provider/
- Documentation — intégration Traefik : https://www.authelia.com/integration/proxies/traefik/
- Documentation — intégration Caddy : https://www.authelia.com/integration/proxies/caddy/
- Documentation — intégration Nginx : https://www.authelia.com/integration/proxies/nginx/
- Documentation — politique de sécurité : https://github.com/authelia/authelia/blob/master/SECURITY.md

## Voir aussi

- [[Authentification]] — le hub du sous-domaine
- [[Comparatif - Fournisseurs d'identité]] — ce qui départage les trois fournisseurs : protocoles, fédération, MFA, empreinte, exploitation, fonctions payantes
- [[OAuth2 et OpenID Connect]] — la notion : flux, jetons, pièges, ce que fait un fournisseur d'identité
