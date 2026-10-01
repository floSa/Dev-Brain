---
role: notion
nom: Gestion des secrets
alias: [secrets management, gestion de secrets, coffre à secrets, secret zéro, rotation des secrets]
categorie: security/secrets
domaines: [infra-ops, mlops]
tags: [secrets-management, cryptography, self-hosted]
---

# Gestion des secrets

## Aperçu

- Un **secret** est ce qui ouvre autre chose : un mot de passe de base, une clé d'API, une clé de chiffrement, une clé privée de certificat, un `client_secret` OAuth. La gestion des secrets répond à quatre questions : où il est **stocké**, comment il **arrive** à l'application, qui peut le **lire** (et qui l'a lu), et comment il est **changé**.
- Sur site, sans cloud, la difficulté n'est pas de trouver un outil : c'est que **chaque solution déplace le problème d'un cran**. Le coffre a besoin d'être déverrouillé, le fichier chiffré a besoin d'une clé, l'orchestrateur a besoin d'un jeton. Le premier secret — celui qu'aucun outil ne fournit — se traite explicitement, ou il se retrouve dans un fichier `.env` oublié.

## Concepts clés

### Ce qu'il ne faut pas faire

- **Des secrets dans le dépôt.** Le rapport GitGuardian 2026 (cinquième édition) compte 28 649 024 nouveaux secrets dans les commits publics de GitHub en 2025, soit +34 % en un an ; 32,2 % des dépôts internes contiennent au moins un secret en dur ; 64 % des secrets détectés en 2022 sont encore actifs quatre ans plus tard. Un secret commité est à considérer comme **compromis** : le retirer du dernier commit ne l'efface pas de l'historique.
- **Des secrets dans une image.** `ENV` et `ARG` d'un Dockerfile s'incrustent dans les couches et les métadonnées de l'image ; Docker le signale par le contrôle de construction `SecretsUsedInArgOrEnv`, et propose à la place `RUN --mount=type=secret` (BuildKit), qui n'existe que le temps de l'instruction.
- **Des secrets dans l'environnement du processus.** OWASP, Docker et Kubernetes le déconseillent : les variables sont lisibles par les processus du même contexte, héritées par les processus enfants, et peuvent finir dans les journaux ou les vidages mémoire (CWE-526 ; `/proc/<pid>/environ`). Kubernetes classe les variables d'environnement moins sûres que les volumes montés. **Désaccord de sources** : le facteur III des Twelve-Factor Apps recommande l'environnement pour la *configuration*, mais ne parle pas de secrets en tant que tels ; les quatre autres sources visent, elles, les secrets.
- **Croire que base64 protège.** Un Secret Kubernetes est stocké non chiffré dans etcd par défaut ; base64 est un encodage. Quiconque peut créer un Pod dans le namespace en lit les Secrets, et le droit `list` équivaut à lire les valeurs.

### Trois façons de faire arriver un secret

- **Un fichier monté par la plateforme.** Docker Compose déclare `secrets:` et monte un fichier dans `/run/secrets/<nom>` (Linux seulement) ; Swarm les transporte en TLS mutuel, les monte en tmpfs et les efface à l'arrêt (500 Ko au plus, immuables : la rotation passe par un nom versionné) ; Kubernetes monte des volumes en tmpfs. L'application lit un **fichier**, pas une variable — [[Pydantic Settings]] lit un répertoire de secrets, [[python-dotenv]] sert au développement local.
- **Un fichier chiffré versionné avec le code.** [[SOPS]] (avec age), ou Sealed Secrets (`kubeseal` chiffre avec la clé publique du contrôleur, seul le contrôleur déchiffre). Le secret suit le dépôt, sans serveur.
- **Un coffre interrogé à l'exécution.** [[OpenBao]] (ou Vault) authentifie le demandeur, applique une politique, journalise et peut fabriquer un secret éphémère. Sous Kubernetes, External Secrets Operator (CNCF Sandbox depuis 2022, plus de 50 backends) synchronise un coffre vers des Secrets natifs, et le pilote CSI *Secrets Store* monte les valeurs en volume sans passer par l'API Secret.

### Coffre ou fichier chiffré

- La documentation de Flux est la seule source lue qui compare les deux. **Chiffré dans Git** (SOPS, Sealed Secrets) : versionnable, transparent pour l'application ; mais l'historique garde le chiffré indéfiniment, et un compte Git compromis déchiffre tout si les clés ne sont pas séparées. **Magasin externe** : redondance, usage hybride Kubernetes et hors Kubernetes ; mais lenteur au provisionnement d'un cluster, incertitude sur la version lue quand le secret est mutable, point de défaillance unique. Flux recommande de **ne pas co-localiser le chiffré et les clés de déchiffrement**.
- La règle de pouce qui en découle, non sourcée : le fichier chiffré suffit tant que les secrets changent rarement, par des humains, et que personne n'a besoin de savoir *qui a lu quoi* ; le coffre devient utile dès qu'il faut des secrets à durée de vie courte, un journal d'accès ou la révocation immédiate.

### Rotation

- OWASP : automatiser la rotation des secrets de **service** ; les mots de passe d'**utilisateurs** ne changent qu'en cas de compromission (NIST). Préférer les secrets **dynamiques** et temporaires.
- **Secrets dynamiques** : le moteur de bases de données de Vault et d'OpenBao fabrique des identifiants uniques par demandeur (traçables par nom d'utilisateur SQL) avec un bail — Vault : durée par défaut d'une heure, maximum de 24 h — et les révoque à l'expiration. Les **rôles statiques** font tourner le mot de passe d'un compte existant ; ne jamais en confier le compte racine de la base au coffre lui-même.
- Un secret qui ne peut pas tourner sans redémarrage de l'application n'est pas *changé* : il est *espéré* inchangé. Prévoir la double clé pendant la transition.

### Le secret zéro

- Formulation de la documentation de Vault : si l'on peut remettre **le premier secret** d'un émetteur à un consommateur de façon sûre, tous les suivants s'authentifient sur la confiance ainsi établie. Trois approches : l'intégration à la plateforme (cloud), un **orchestrateur de confiance** (Terraform, Chef…), l'agent Vault. Hors cloud, seul le deuxième reste.
- **AppRole** : un `role_id` (public) et un `secret_id` (secret) que l'orchestrateur remet enveloppé dans un jeton de *response wrapping* — à usage unique et à durée courte : masqué dans les journaux, interception détectable, durée bornée.
- **Déverrouiller le coffre lui-même.** Au démarrage, Vault et OpenBao sont *scellés*. Par défaut, la clé de déverrouillage est découpée en parts de Shamir, distribuées à des personnes, dont un seuil est requis. L'**auto-unseal** confie le déverrouillage à un HSM, à un KMS ou au Transit d'une **autre** instance : sur site, la variante Transit ou PKCS#11. La perte de la clé du mécanisme externe rend le cluster **irrécupérable**, même depuis les sauvegardes (avertissement de la documentation d'OpenBao).
- **Avec SOPS**, le secret zéro est la clé privée age : hors du dépôt, sur un disque chiffré ou un jeton matériel ; la documentation de SOPS ne recommande pas de procédure de bootstrap.
- Le secret zéro ne disparaît donc jamais : il se **déplace** vers un orchestrateur, une personne ou une clé matérielle, et se protège là, avec les moyens de l'organisation.

## En pratique

- **Un site avec quelques services en [[Docker Compose]]** : `secrets:` en fichiers, générés hors dépôt, ou [[SOPS]] avec une clé age par personne autorisée ; la clé privée n'entre pas dans le dépôt.
- **Un cluster [[Kubernetes]]** : chiffrer etcd (`EncryptionConfiguration` ; les fournisseurs `aescbc`, `aesgcm`, `secretbox` ou `kms`, KMS v2 stable depuis la 1.29 — la documentation n'y nomme aucun plugin sur site), limiter `list` et `watch` par RBAC, ne jamais commiter un manifeste Secret. Puis choisir : SOPS et Flux, ou un [[OpenBao]] avec External Secrets Operator.
- **Un secret d'authentification** : le `client_secret` d'un client OAuth ([[OAuth2 et OpenID Connect]]), la clé de signature d'un [[Keycloak]] ou d'un [[Authentik]] et la clé privée d'un certificat ([[Reverse proxy et TLS]]) sont des secrets comme les autres.
- **Après une fuite** : révoquer et changer le secret, pas seulement nettoyer le dépôt. La **détection** des secrets dans le code et les images est un autre sujet, non traité ici.

## Approches voisines & alternatives

- [[OpenBao]] et [[SOPS]] sont les deux briques du brain ; [[OpenBao]] est le fork open source de HashiCorp Vault, dont la licence BUSL est expliquée dans sa fiche.
- **KMS et HSM** : ils protègent des *clés*, pas des secrets applicatifs ; Kubernetes s'en sert pour chiffrer etcd, OpenBao pour son scellement.
- **age** (BSD-3-Clause, Go, v1.3.2 du 2026-08-29) est l'outil de chiffrement de fichiers dont SOPS reprend les clés : X25519 ou clés SSH, ChaCha20-Poly1305, pas de négociation d'algorithmes. Le README ne le compare pas formellement à PGP.
- **Sealed Secrets** (Apache-2.0, v0.40.0 du 2026-09-10) : chiffrement asymétrique pour Kubernetes seulement. Le dépôt est passé de `bitnami-labs` à `bitnami` ; le retrait du catalogue d'images Bitnami annoncé par Broadcom en 2025 ne mentionne pas Sealed Secrets, mais aucune source primaire ne confirme qu'il n'est pas touché.
- **Configuration applicative** ([[python-dotenv]], [[Pydantic Settings]]) : elles *lisent* un secret, elles ne le gardent pas.
- Voir aussi : [[Gitleaks]], [[Pipelines CI-CD on-prem — runners, secrets et artefacts]], [[Ansible]], [[OpenTofu]].

## Pour aller plus loin

- OWASP — Secrets Management Cheat Sheet : https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- The Twelve-Factor App, III — Config : https://12factor.net/config
- Docker — secrets dans Compose : https://docs.docker.com/compose/how-tos/use-secrets/ ; secrets de build : https://docs.docker.com/build/building/secrets/ ; contrôle `SecretsUsedInArgOrEnv` : https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/
- Kubernetes — Secrets : https://kubernetes.io/docs/concepts/configuration/secret/ ; bonnes pratiques : https://kubernetes.io/docs/concepts/security/secrets-good-practices/ ; chiffrement au repos : https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/ ; fournisseur KMS : https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
- CWE-526 — variables d'environnement : https://cwe.mitre.org/data/definitions/526.html
- Flux — gestion des secrets : https://fluxcd.io/flux/security/secrets-management/ ; avec SOPS : https://fluxcd.io/flux/guides/mozilla-sops/
- Vault — introduction sûre du premier secret : https://developer.hashicorp.com/vault/tutorials/app-integration/secure-introduction ; AppRole : https://developer.hashicorp.com/vault/docs/auth/approle ; *response wrapping* : https://developer.hashicorp.com/vault/docs/concepts/response-wrapping
- OpenBao — scellement : https://openbao.org/docs/concepts/seal/ ; secrets de bases de données : https://openbao.org/docs/secrets/databases/
- External Secrets Operator : https://external-secrets.io/latest/ ; Secrets Store CSI Driver : https://github.com/kubernetes-sigs/secrets-store-csi-driver ; Sealed Secrets : https://github.com/bitnami/sealed-secrets ; age : https://github.com/FiloSottile/age
- GitGuardian — State of Secrets Sprawl 2026 : https://www.gitguardian.com/state-of-secrets-sprawl-report-2026
