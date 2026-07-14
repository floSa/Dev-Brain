---
galaxie: dev
type: service
nom: PyJWT
alias: [pyjwt, jwt python]
pitch: "Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API."
categorie: auth
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [authentication, cryptography]
url_docs: https://pyjwt.readthedocs.io/
url_repo: https://github.com/jpadilla/pyjwt
---

# PyJWT

## Pourquoi

Bibliothèque Python de référence pour les **JSON Web Tokens** (RFC 7519). Elle encode et décode des tokens, **signe et vérifie** leur intégrité (HMAC `HS*`, RSA `RS*`/`PS*`, ECDSA `ES*`, EdDSA), et **valide les claims** enregistrés : expiration (`exp`), pas-avant (`nbf`), audience (`aud`), émetteur (`iss`). C'est le bloc bas niveau de l'**auth stateless** : un token signé porté par le client remplace une session serveur. Largement utilisée sous le capot des couches d'auth (dont `fastapi` + OAuth2 password bearer).

## Quand l'utiliser

- **Authentifier une API** sans état serveur : émettre un JWT à la connexion, le vérifier à chaque requête.
- **Vérifier des tokens tiers** : valider un id_token OIDC, une clé d'API signée, un webhook signé (Apple, GitHub Apps).
- Quand on veut **maîtriser** l'émission et la validation des tokens, sans framework d'auth complet.

## Quand NE PAS l'utiliser

- Besoin d'un **serveur OAuth2 / OIDC** complet (flux authorization code, refresh, révocation) → une solution dédiée (Authlib, Keycloak, Auth0) ; PyJWT ne gère que le token, pas les flux.
- **Sessions classiques** côté serveur (cookie + store) → un token signé apporte surtout de la complexité ici.
- Chiffrer le contenu du token (JWE) → PyJWT couvre **JWS** (signature), pas le chiffrement de charge utile.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add "pyjwt[crypto]"` pour les algorithmes RSA/ECDSA (tire `cryptography`). HMAC seul ne nécessite pas l'extra.
- **Single-node**, pur calcul ; aucune infrastructure. Python 3.9+.

## Pièges

- **`algorithms=[...]` obligatoire au décodage** : sans liste blanche explicite, on s'expose à l'attaque de confusion d'algorithme (`alg: none`, ou RS256 vérifié comme HMAC avec la clé publique). Ne jamais faire confiance à l'`alg` du header.
- Un JWT est **signé, pas chiffré** : tout le payload est lisible (base64). N'y mettre aucun secret.
- **Pas de révocation native** : un token valide l'est jusqu'à `exp`. Garder des durées courtes + refresh, ou une liste de révocation côté serveur.
- L'horloge compte : la validation de `exp`/`nbf` suppose des horloges synchronisées (prévoir un `leeway`).

## Alternatives

Pas de substitut direct référencé dans le brain. Pour des **flux OAuth2/OIDC complets**, regarder Authlib ou un fournisseur d'identité (Keycloak, Auth0) — non référencés ici. PyJWT reste le défaut pour la simple manipulation de tokens.

## Liens

- [[Dev/Services/FastAPI|FastAPI]] — consomme PyJWT dans son pattern OAuth2 password bearer.
- Doc : https://pyjwt.readthedocs.io/ · Repo : https://github.com/jpadilla/pyjwt
