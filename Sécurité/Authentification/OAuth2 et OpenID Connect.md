---
role: notion
nom: OAuth2 et OpenID Connect
alias: [oauth2, oauth 2.0, oidc, openid connect, authorization code pkce, jeton d'accès, id token]
categorie: security/auth
domaines: [infra-ops, ai-eng]
tags: [authentication, sso, identity-provider]
---

# OAuth2 et OpenID Connect

## Aperçu

- **OAuth 2.0** (RFC 6749) est un cadre de **délégation d'accès** : une application obtient d'un serveur d'autorisation un jeton limité, avec lequel elle appelle une API au nom d'un utilisateur, sans jamais voir son mot de passe. Ce n'est pas, en soi, un protocole d'authentification.
- **OpenID Connect** (OIDC Core 1.0) ajoute par-dessus la couche d'**identité** : un *ID token*, un JWT qui dit **qui** s'est authentifié, quand et comment, plus une découverte (`/.well-known/openid-configuration`) et des jeux de clés publiques (JWKS).
- En on-prem, les deux se rencontrent au même endroit : un **fournisseur d'identité** ([[Keycloak]], [[Authentik]], [[Authelia]]) joue le serveur d'autorisation et le fournisseur OIDC, et chaque application — une API [[FastAPI]], [[Grafana]], [[Airflow]] — délègue la connexion. Le code de l'application se réduit à **vérifier des jetons** ([[PyJWT]]).

## Concepts clés

### Les quatre rôles

- **Propriétaire de la ressource** (l'utilisateur), **client** (l'application qui demande l'accès), **serveur d'autorisation** (émet les jetons), **serveur de ressources** (l'API qui les reçoit). En OIDC, le serveur d'autorisation devient le *OpenID Provider* et le client le *Relying Party*.
- Un client est **confidentiel** s'il sait garder un secret (un service côté serveur) et **public** sinon (application native, page web dans un navigateur). La différence commande le flux : un client public ne peut prouver son identité que par PKCE.

### Le flux à retenir : code d'autorisation avec PKCE

- Le client redirige l'utilisateur vers le serveur d'autorisation avec un `code_challenge` (le condensé S256 d'un `code_verifier` tiré au hasard), un `state` ou un `nonce` et un `redirect_uri`. Après connexion, le serveur renvoie un **code** à usage unique ; le client l'échange contre les jetons en présentant le `code_verifier`. Un code volé en route ne sert à rien sans lui.
- **PKCE** (RFC 7636) : la RFC 9700 le rend obligatoire pour les clients publics et le recommande aux confidentiels ; le serveur doit refuser un `code_verifier` sans `code_challenge` (attaque par rétrogradation).
- **Les flux à écarter** : l'*implicit* est déconseillé (RFC 9700 §2.1.2, « SHOULD NOT ») et le *password* interdit (§2.4, « MUST NOT »). L'ébauche OAuth 2.1 supprime les deux.
- **Les deux autres flux utiles** : le *client credentials* (RFC 6749 §4.4) pour un service qui agit pour lui-même — un ordonnanceur qui appelle une API, sans utilisateur ; le *device authorization grant* (RFC 8628) pour un appareil ou une CLI sans navigateur.

### Trois jetons, trois destinataires

- **Jeton d'accès** : destiné à l'**API**. Opaque, ou un JWT au profil de la RFC 9068 (`typ: at+jwt`, avec `iss`, `exp`, `aud`, `sub`, `client_id`, `iat`, `jti`). Il est **porteur** (RFC 6750) : quiconque le détient s'en sert jusqu'à son expiration.
- **ID token** : destiné au **client**, jamais à l'API. C'est la preuve de connexion d'OIDC ; il porte `iss`, `sub`, `aud` (le `client_id`), `exp`, `nonce`. Le présenter comme jeton d'accès à une API est une confusion de types que la RFC 8725 (§3.11-3.12) demande d'empêcher par un typage explicite.
- **Jeton de rafraîchissement** : destiné au serveur d'autorisation, pour obtenir un nouveau jeton d'accès sans reconnecter l'utilisateur. Pour un client public, il doit être lié à son émetteur ou **rotatif** (RFC 9700 §2.2.2) : rejouer un ancien jeton révoque le jeton actif.

### Vérifier un jeton côté API

- Avec un JWT, la vérification est locale : récupérer les clés publiques par le `jwks_uri` de la découverte, vérifier la **signature**, puis `iss` (exact), `aud` (contient l'API visée), `exp` et `nbf`. Sans elles, un jeton décodé n'est qu'un JSON lu.
- **Fixer la liste des algorithmes** attendus (RFC 8725 §3.1) : ne jamais se fier à l'`alg` du jeton, sinon `alg: none` ou un RS256 vérifié comme HMAC avec la clé publique passent. [[PyJWT]] l'exige : `algorithms=[...]` est obligatoire, et son `PyJWKClient` met en cache le JWKS.
- Avec un jeton opaque, l'API interroge le serveur par **introspection** (RFC 7662) ; la **révocation** (RFC 7009) et l'**échange de jetons** (RFC 8693, délégation d'un service à un autre) complètent le tableau.
- La bibliothèque est elle-même une surface d'attaque : PyJWT a publié 21 avis de sécurité sur 36 mois, 19 entre mai et septembre 2026, dont deux critiques (cf. sa fiche). Épingler une version récente et surveiller ses avis fait partie du travail.

### Ce que fait le fournisseur d'identité

- Il **authentifie** (mot de passe, MFA, passkeys), **fédère** (annuaires LDAP, autres fournisseurs), **émet** les jetons, **publie** sa découverte et ses clés, et tient la **session** de l'utilisateur — d'où le SSO : la deuxième application ne redemande rien tant que la session vit.
- Il ne décide pas ce qu'un utilisateur a le droit de faire *dans* l'application : rôles et groupes voyagent en revendications, mais l'autorisation métier reste au code de l'API.
- **Deux formes, à ne pas confondre** : un fournisseur complet qui émet des jetons pour l'application ([[Keycloak]], [[Authentik]]), et un **portail devant le reverse proxy** qui décide d'ouvrir ou non la porte sans que l'application ne sache rien ([[Authelia]] en mode *forward auth*). Le second protège une application qui n'a aucune notion de connexion ; le premier suppose qu'elle en ait une.

### Déconnexion

- OIDC a trois spécifications de sortie, toutes *Final* : *Session Management* (iframe et `postMessage`, que le blocage des cookies tiers peut casser), *Front-Channel Logout* et *Back-Channel Logout* (un *logout token* JWT envoyé au serveur de chaque application). Tous les fournisseurs ne les implémentent pas — [[Authelia]] annonce ne pas fournir les déconnexions OIDC.

## En pratique

- **Une API Python** : émettre ses propres jetons ne vaut que pour un besoin minimal ([[PyJWT]] et le tutoriel de [[FastAPI]] sur OAuth2 avec mot de passe). Dès qu'il y a plusieurs applications ou de vrais utilisateurs, déléguer à un fournisseur d'identité et **valider** ses jetons.
- **Derrière un reverse proxy** : le proxy peut déléguer l'authentification à un service (`forward_auth` de [[Caddy]], `auth_request` de [[Nginx]], ForwardAuth de [[Traefik]]) ; le middleware OIDC de Traefik est réservé à sa version commerciale Hub. **oauth2-proxy** (MIT, CNCF Sandbox, v7.15.4 du 2026-08-20) est le service intermédiaire courant quand l'application n'a pas de SSO.
- **Ce que la documentation officielle des outils du brain dit** (relevé du 2026-09-30) : [[Grafana]] (OSS, page Keycloak dédiée), [[Airflow]] (fournisseurs `keycloak` et `authentik` dans le provider FAB ; un *auth manager* Keycloak existe, déclaré alpha), [[Langfuse]] (variables dédiées Keycloak et Authentik, OIDC générique), [[Argo CD]] (OIDC natif ou Dex, page Keycloak). [[MLflow]] n'a qu'une authentification HTTP Basic ; son SSO passe par un plugin communautaire ou un proxy. Le SSO de [[Dify]] est dans son édition Enterprise. Kubernetes accepte l'OIDC pour son API (`--oidc-issuer-url`, ou la configuration d'authentification structurée) mais ne fournit pas de fournisseur.
- **Une horloge juste** : `exp` et `nbf` supposent des horloges synchronisées entre le serveur d'autorisation et l'API ; prévoir un `leeway` de quelques secondes.

### Les pièges documentés

- **`redirect_uri`** : comparaison de chaînes **exacte** (RFC 9700 §2.1, §4.1.3), jamais un préfixe ni un joker.
- **`state`, `nonce`, PKCE** : le client doit prévenir le CSRF ; la valeur est propre à la transaction et liée au navigateur qui l'a lancée.
- **Confusion d'émetteur** (*mix-up*) : un client qui parle à plusieurs serveurs vérifie l'`iss` de la réponse (RFC 9207, RFC 9700 §4.4).
- **`aud` et `iss` non vérifiés** : un jeton valide émis pour une autre application passe alors pour le sien (RFC 8725 §3.8-3.9).
- **Jeton de durée longue et stocké n'importe où** : la RFC 9700 ne fixe pas de règle de stockage ; les applications de navigateur ont leur propre BCP (RFC 10017, août 2026 — numéro, date et statut vérifiés, contenu non relu ici).
- **Un JWT ne se révoque pas** avant `exp` : durées courtes, rafraîchissement rotatif, ou liste de `jti` révoqués (OWASP).

## Approches voisines & alternatives

- **OAuth 2.1** : l'ébauche `draft-ietf-oauth-v2-1-16` (2026-09-03, *Active Internet-Draft*, jalon « envoi à l'IESG » en décembre 2026) remplacerait les RFC 6749 et 6750 en supprimant *implicit* et *password* et en imposant PKCE et le `redirect_uri` exact. Ce n'est pas une RFC : la RFC 9700 est le texte publié qui porte déjà ces règles.
- **SAML 2.0** : protocole d'entreprise que fournit [[Keycloak]] (fournisseur et service) et que [[Authelia]] ne fournit pas. [[Comparatif - Fournisseurs d'identité]] compare les protocoles servis par chaque brique.
- **Sessions de serveur classiques**, **clés d'API** et **mTLS** (RFC 8705, jetons liés à un certificat) répondent à d'autres besoins ; [[PyJWT]] rappelle quand un token signé n'apporte que de la complexité.
- **Bibliothèques Python voisines** de PyJWT : Authlib (client et serveur OAuth, 1.8.0 du 2026-08-30), joserfc (1.7.5), jwcrypto (1.6.1) ; python-jose n'a pas eu de version depuis mai 2025.
- **Gestion des secrets** : un `client_secret` est un secret comme un autre — [[Gestion des secrets]].

## Pour aller plus loin

- RFC 6749 (OAuth 2.0) : https://www.rfc-editor.org/rfc/rfc6749.html ; RFC 6750 (Bearer) : https://www.rfc-editor.org/rfc/rfc6750.html
- RFC 9700 (Best Current Practice for OAuth 2.0 Security, janvier 2025) : https://www.rfc-editor.org/rfc/rfc9700.html
- RFC 7636 (PKCE) : https://www.rfc-editor.org/rfc/rfc7636.html ; RFC 8628 (device) : https://www.rfc-editor.org/rfc/rfc8628.html ; RFC 9207 (identification de l'émetteur) : https://www.rfc-editor.org/rfc/rfc9207.html
- RFC 7662 (introspection) : https://www.rfc-editor.org/rfc/rfc7662.html ; RFC 7009 (révocation) : https://www.rfc-editor.org/rfc/rfc7009.html ; RFC 8693 (échange de jetons) : https://www.rfc-editor.org/rfc/rfc8693.html
- RFC 7519 (JWT) : https://www.rfc-editor.org/rfc/rfc7519.html ; RFC 8725 (JWT BCP) : https://www.rfc-editor.org/rfc/rfc8725.html ; RFC 9068 (jetons d'accès JWT) : https://www.rfc-editor.org/rfc/rfc9068.html
- RFC 9449 (DPoP) : https://www.rfc-editor.org/rfc/rfc9449.html ; RFC 9126 (PAR) : https://www.rfc-editor.org/rfc/rfc9126.html ; RFC 8414 (métadonnées) : https://www.rfc-editor.org/rfc/rfc8414.html
- OpenID Connect Core 1.0 : https://openid.net/specs/openid-connect-core-1_0.html ; liste des spécifications : https://openid.net/developers/specs/
- OAuth 2.1 (ébauche) : https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
- OWASP — OAuth2 Cheat Sheet : https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html ; JWT Cheat Sheet : https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html
- oauth2-proxy : https://oauth2-proxy.github.io/oauth2-proxy/
