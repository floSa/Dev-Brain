---
role: brique
nom: PyJWT
alias: [pyjwt, jwt python]
pitch: "Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API."
categorie: security/auth
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [authentication, cryptography]
url_docs: https://pyjwt.readthedocs.io/
url_repo: https://github.com/jpadilla/pyjwt
---

# PyJWT

<!-- AUTO:BANDEAU:START -->
> Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation Python de référence des **JSON Web Tokens** (RFC 7519). Elle encode et
décode des tokens, signe et vérifie leur intégrité — HMAC `HS*`, RSA `RS*` et `PS*`,
ECDSA `ES*`, EdDSA — et valide les claims enregistrés : expiration `exp`, pas-avant
`nbf`, audience `aud`, émetteur `iss`. C'est le bloc bas niveau de l'authentification
**sans état** : un token signé porté par le client remplace une session serveur. Deux
propriétés commandent tout usage correct. Un JWT est **signé, pas chiffré** — le payload
se lit en base64, on n'y met donc aucun secret. Et le décodage exige une liste blanche
`algorithms=[...]` explicite : l'`alg` du header vient de l'appelant, donc de l'attaquant,
et s'y fier ouvre la confusion d'algorithme (`alg: none`, ou un RS256 vérifié comme HMAC
avec la clé publique).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Authentifier une API sans état serveur : émettre un JWT à la connexion, le vérifier à chaque requête | Serveur OAuth2 ou OIDC complet — flux authorization code, refresh, révocation : PyJWT gère le token, jamais les flux (Authlib, Keycloak, Auth0, hors brain) |
| Vérifier des tokens tiers : id_token OIDC, clé d'API signée, webhook signé (Apple, GitHub Apps) | Sessions classiques côté serveur, cookie et store : un token signé n'ajoute là que de la complexité |
| Maîtriser l'émission et la validation des tokens sans embarquer un framework d'auth complet | Chiffrer la charge utile (JWE) : PyJWT couvre JWS, la signature, pas le chiffrement |
| | Révoquer un token avant son `exp` : il n'y a pas de révocation native — durées courtes et refresh, ou liste de révocation tenue côté serveur |

## Mise en œuvre

- Installation — `uv add "pyjwt[crypto]"` pour RSA et ECDSA, qui tirent `cryptography` ; HMAC seul se passe de l'extra
- Point d'entrée — import Python, `import jwt` ; `jwt.encode` et `jwt.decode`
- Prérequis — Python ≥ 3.9 ; des horloges synchronisées entre émetteur et vérificateur, la validation de `exp` et `nbf` en dépendant — prévoir un `leeway`
- Exécution — dans le process appelant, pur calcul CPU ; rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- *Aucune alternative déclarée : pas de substitut direct fiché au brain. Pour des flux OAuth2/OIDC complets, Authlib ou un fournisseur d'identité (Keycloak, Auth0), hors brain — ils sont pointés dans le tableau ci-dessus.*

## Ressources

- Documentation — https://pyjwt.readthedocs.io/
- Dépôt — https://github.com/jpadilla/pyjwt

## Voir aussi

- [[Sécurité]] — le hub du domaine
- [[FastAPI]] — le consomme dans son pattern OAuth2 password bearer
