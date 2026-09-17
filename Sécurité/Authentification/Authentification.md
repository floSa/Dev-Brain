---
role: hub
nom: Authentification
alias: [authentification, sso, identité, fournisseurs d'identité, iam]
pitch: Prouver qui appelle — vérifier un jeton dans le code d'une API, ou déléguer la connexion à un fournisseur d'identité ou à un portail placé devant le reverse proxy.
domaines: [infra-ops, ai-eng]
tags: [authentication, sso, identity-provider]
---

# Authentification

> Prouver qui appelle — vérifier un jeton dans le code d'une API, ou déléguer la connexion à un fournisseur d'identité ou à un portail placé devant le reverse proxy.

## Ce qu'il faut comprendre

- **Trois niveaux, qui ne se remplacent pas.** Vérifier un jeton dans le code ([[PyJWT]]) ; émettre ces jetons et tenir les utilisateurs ([[Keycloak]], [[Authentik]]) ; décider à l'entrée du proxy sans que l'application sache rien ([[Authelia]], et le mode *forward auth* d'Authentik). [[OAuth2 et OpenID Connect]] est la notion qui les relie : flux, jetons, pièges.
- **Un fournisseur d'identité n'est pas une bibliothèque de jetons.** PyJWT vérifie une signature et des revendications ; il ne fait ni les flux, ni la révocation, ni le MFA. À l'inverse, le fournisseur ne dit pas ce qu'un utilisateur a le droit de faire dans l'application.
- **Un seul des trois a une édition payante.** [[Authentik]] est open-core (audit renforcé, PAM, provisioning, certificats clients dans l'édition Enterprise) ; [[Keycloak]] et [[Authelia]] sont Apache-2.0, sans fonction gardée. [[Comparatif - Fournisseurs d'identité]] tranche.
- **SAML n'est pas partout** : [[Keycloak]] et [[Authentik]] le servent, [[Authelia]] non. Le rythme des avis de sécurité diffère beaucoup, et il est une charge d'exploitation à part entière.
- **Le proxy compte.** Chaque fournisseur suppose des en-têtes `X-Forwarded-*` écrasés par le proxy de confiance : [[Reverse proxy et TLS]] traite la confiance à leur accorder.
- Les secrets d'un fournisseur (`client_secret`, clé de signature) sont des secrets comme les autres : [[Gestion des secrets]].

## Choisir

- Vérifier ou émettre un JWT en Python, sans serveur → [[PyJWT]].
- Comprendre les flux, les jetons et les pièges avant de choisir → [[OAuth2 et OpenID Connect]].
- Un fournisseur complet, avec SAML et la fédération d'un annuaire d'entreprise → [[Keycloak]].
- Un fournisseur avec des parcours composables et un portail de forward auth, quitte à payer certaines fonctions → [[Authentik]].
- Un portail léger devant un proxy, un MFA, un OIDC simple, sans SAML → [[Authelia]].
- Comparer les trois → [[Comparatif - Fournisseurs d'identité]].

<!-- AUTO:START -->
### Notions
- [[OAuth2 et OpenID Connect]] — domaines : infra-ops, ai-eng

### Briques
- [[Authelia]] — Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante).
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter.
- [[PyJWT]] — Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.

### Comparatifs
- [[Comparatif - Fournisseurs d'identité]]
<!-- AUTO:END -->
