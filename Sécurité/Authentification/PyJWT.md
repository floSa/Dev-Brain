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
complements: ["[[FastAPI]]"]
tags: [authentication, cryptography]
url_docs: https://pyjwt.readthedocs.io/
url_repo: https://github.com/jpadilla/pyjwt
---

# PyJWT

<!-- AUTO:BANDEAU:START -->
> Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
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

Relevé le 2026-09-30 : **2.15.1** (2026-09-28), environ 5 700 étoiles, licence MIT, Python ≥ 3.9 (classifiers 3.9 à 3.15) ; mainteneur principal jpadilla, dernier commit humain le 2026-09-28. La série a vu quatre versions en cinq mois (2.13.0 le 2026-05-21, 2.14.0 le 2026-09-11, 2.15.0 le 2026-09-23), toutes portées par des correctifs de sécurité — voir *Limites à connaître*. Les options de vérification (`verify_signature`, `verify_exp`, `verify_nbf`, `verify_iat`, `verify_aud`, `verify_iss`, `verify_sub`, `verify_jti`) valent vrai par défaut ; `algorithms` reste obligatoire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Authentifier une API sans état serveur : émettre un JWT à la connexion, le vérifier à chaque requête | Serveur OAuth2 ou OIDC complet — flux authorization code, refresh, révocation : PyJWT gère le token, jamais les flux ([[Keycloak]], [[Authentik]] ou [[Authelia]] ; Authlib, hors brain) |
| Vérifier des tokens tiers : id_token OIDC, clé d'API signée, webhook signé (Apple, GitHub Apps) | Sessions classiques côté serveur, cookie et store : un token signé n'ajoute là que de la complexité |
| Maîtriser l'émission et la validation des tokens sans embarquer un framework d'auth complet | Chiffrer la charge utile (JWE) : PyJWT couvre JWS, la signature, pas le chiffrement |
| | Révoquer un token avant son `exp` : il n'y a pas de révocation native — durées courtes et refresh, ou liste de révocation tenue côté serveur |

## Mise en œuvre

- Installation — `uv add "pyjwt[crypto]>=2.15.1"` pour RSA et ECDSA, qui tirent `cryptography` ; HMAC seul se passe de l'extra ; **borner par le bas**, les correctifs de 2026 sont nombreux
- Point d'entrée — import Python, `import jwt` ; `jwt.encode` et `jwt.decode`
- Prérequis — Python ≥ 3.9 ; des horloges synchronisées entre émetteur et vérificateur, la validation de `exp` et `nbf` en dépendant — prévoir un `leeway`
- Exécution — dans le process appelant, pur calcul CPU ; rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage
- Point d'entrée — pour vérifier le jeton d'un fournisseur d'identité, `PyJWKClient(jwks_uri)` récupère et met en cache les clés publiques, puis `jwt.decode(token, signing_key, algorithms=["RS256"], audience=…, issuer=…)` ; `options={"require": ["exp", "iss"]}` rend des revendications obligatoires, `leeway` tolère un écart d'horloge

## Limites à connaître

- **21 avis de sécurité sur 36 mois, dont 19 entre mai et septembre 2026** (page des avis du dépôt). Deux critiques : des extensions `crit` inconnues acceptées (CVE-2026-32597, 2026-03-12, corrigée en 2.12.0) et un contournement de la détection PEM qui permet de falsifier un jeton (CVE-2026-102268, 2026-09-11). Sept de gravité haute : des **clés publiques** (JWK, DER, PEM, BOM) acceptées comme secret HMAC — la confusion d'algorithme sous ses variantes —, des clés HMAC vides via `PyJWK` et `PyJWKClient`, et un `PyJWKClient` qui suivait les redirections.
- Les changements de comportement à connaître : `alg="none"` doit être demandé explicitement (2.10.0), `iss` doit être une chaîne et un avertissement signale les clés trop courtes (2.11.0, `enforce_minimum_key_length=True` en fait une erreur), une clé HMAC vide ou au format JWK est refusée (2.13.0), le client JWKS ne suit plus les redirections (2.14.0).
- La version qui corrige un des avis de septembre (GHSA-gvp8-978c-rx2q, mutation du dictionnaire `options`) n'a pas pu être vérifiée : partir de la dernière.

## Écosystème

### Alternatives

- *Aucune alternative déclarée : pas de substitut direct fiché au brain. Pour des flux OAuth2/OIDC complets, un fournisseur d'identité — [[Keycloak]], [[Authentik]], [[Authelia]] — émet les jetons que PyJWT vérifie ; parmi les bibliothèques Python, Authlib (1.8.0), joserfc (1.7.5) et jwcrypto (1.6.1) sont actives, python-jose n'a pas eu de version depuis mai 2025 — hors brain.*

### Compléments

- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — le tutoriel de FastAPI sur OAuth2 avec JWT s'appuie sur PyJWT.

## Ressources

- Documentation — https://pyjwt.readthedocs.io/
- Dépôt — https://github.com/jpadilla/pyjwt

## Voir aussi

- [[Authentification]] — le hub du sous-domaine
- [[OAuth2 et OpenID Connect]] — la notion : flux, jetons, pièges, ce que fait un fournisseur d'identité
- [[Comparatif - Fournisseurs d'identité]] — les fournisseurs qui émettent les jetons que PyJWT vérifie
