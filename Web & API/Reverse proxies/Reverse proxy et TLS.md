---
role: notion
nom: Reverse proxy et TLS
alias: [reverse proxy, terminaison tls, tls interne, autorité de certification interne, gateway api et ingress]
categorie: web/proxy
domaines: [infra-ops, mlops]
tags: [reverse-proxy, tls, load-balancer, kubernetes, self-hosted]
---

# Reverse proxy et TLS

## Aperçu

- Un reverse proxy est l'intermédiaire que le client prend pour le serveur : il reçoit la requête, choisit l'origine, transmet, et rend la réponse. Il porte le TLS, le routage par nom d'hôte, la répartition de charge, souvent la compression et la limitation de débit — tout ce qu'un service Python ou un serveur de modèle ne devrait pas faire lui-même.
- Le sujet a deux moitiés qui se rejoignent au certificat : **où le chiffrement s'arrête**, et **qui signe le certificat**. Sur Internet, la réponse est ACME et une autorité publique. En on-prem, où les services n'ont souvent ni nom public ni accès depuis Internet, c'est une autorité interne — et son vrai coût est de faire accepter sa racine à chaque client.

## Concepts clés

### Ce que fait un reverse proxy

- **Définition normative.** La RFC 9110 (§3.7) nomme *passerelle* l'intermédiaire qui « agit comme serveur d'origine » pour la connexion sortante mais traduit et retransmet les requêtes ; le *tunnel* est un relais aveugle, c'est le cas du passthrough TLS. La différence avec un forward proxy : celui-ci est choisi par le client, l'autre est choisi par l'exploitant du serveur.
- **Ce que MDN liste** (répartition de charge, cache du statique, compression) est moins que ce que les proxys du brain font. Routage, terminaison TLS, limitation de débit et authentification déléguée ne viennent pas de cette page : ils viennent de la documentation de chaque outil ([[Traefik]], [[Caddy]], [[Nginx]], [[HAProxy]]).

### Les en-têtes transférés, et la confiance qu'ils demandent

- **Ce que l'application voit.** Derrière un proxy, l'adresse du client est celle du proxy. Le proxy la met dans `X-Forwarded-For`, le protocole d'origine dans `X-Forwarded-Proto`, le nom d'hôte dans `X-Forwarded-Host`. La RFC 7239 a normalisé la même chose sous l'en-tête `Forwarded` (`for`, `by`, `host`, `proto`) et rappelle qu'il « ne peut pas être considéré comme correct » : chaque nœud peut l'écrire.
- **Le piège est de croire l'en-tête.** MDN : si le serveur est joignable sans passer par le proxy, aucune partie de `X-Forwarded-For` n'est fiable ; pour un usage de sécurité (limiteur, contrôle d'accès), la liste se lit **depuis la droite**, avec un nombre de proxys connu ou une liste d'adresses de confiance. La valeur la plus à gauche ne sert qu'aux journaux.
- **Côté Python.** [[Uvicorn]] lit ces en-têtes par défaut (`--proxy-headers`) mais ne fait confiance qu'à `127.0.0.1` et `::1` (`--forwarded-allow-ips`, ou `$FORWARDED_ALLOW_IPS`) ; `'*'` veut dire « tout le monde » et n'est acceptable que si chaque proxy nettoie les en-têtes. Avec [[FastAPI]], `--root-path` sert quand le proxy retire un préfixe. Avec [[Flask]], `ProxyFix` prend un **nombre** de proxys par en-tête (`x_for`, `x_proto`…), qui doit être exact.
- **Le PROXY protocol** (spécification de Willy Tarreau, versions 1 et 2) transporte adresse et port du client à travers un proxy TCP, donc aussi en passthrough. Le récepteur doit être configuré pour ne l'accepter que de sources connues, sinon un client usurpe son adresse.

### Terminaison, passthrough, re-chiffrement

- **Terminaison** : le proxy déchiffre, lit la requête HTTP, route sur son contenu. C'est le cas courant, et le seul qui permet WAF, cache, en-têtes ajoutés et routage par chemin. Derrière lui, le trafic est en clair sur le réseau interne, à moins de **re-chiffrer** vers l'origine (`proxy_ssl_*` chez Nginx, `BackendTLSPolicy` en Gateway API). Qu'un LAN partagé ne soit pas un canal de confiance est un jugement de rédaction : aucune source lue ne l'analyse comme menace. Vers un backend HTTPS, [[Nginx]] ne vérifie pas le certificat par défaut (`proxy_ssl_verify off`).
- **Passthrough** : le proxy ne lit que le ClientHello (SNI, ALPN, version) et relaie les octets chiffrés (`ssl_preread` chez Nginx, non compilé par défaut). Il ne voit ni URL, ni en-têtes, ni cookies : pas de WAF, pas de cache, pas de `X-Forwarded-*` — d'où le PROXY protocol.
- **SNI et ALPN.** Le SNI (RFC 6066) permet plusieurs noms sur une adresse, et voyage **en clair** dans le ClientHello (le chiffrement de ce champ, ECH, n'a pas été relu ici). L'ALPN (RFC 7301) négocie `h2` ou `h3` sans aller-retour. HTTP/3 (RFC 9114) tourne sur QUIC, donc sur **UDP** : le pare-feu et le proxy doivent l'ouvrir explicitement.
- **TLS 1.3** (RFC 8446) supprime les échanges de clés sans confidentialité persistante et chiffre les messages après le ServerHello ; ses données 0-RTT sont rejouables. Les profils de configuration de référence ne sont plus chez Mozilla : le wiki renvoie à `docs.tlsref.org` (version 6.0), qui décrit *modern* (TLS 1.3 seul, trois suites) et *intermediate* (TLS 1.2 et 1.3) ; le configurateur en affiche trois, avec *old*, que la page de lignes directrices ne décrit pas — écart non tranché.

### Certificats publics : ACME, et l'automatisation devenue obligatoire

- **ACME** (RFC 8555) : un compte, une commande, des autorisations prouvées par un *challenge*, une finalisation par CSR. `http-01` pose une ressource sur le port 80, joignable depuis l'autorité ; `dns-01` pose un enregistrement TXT `_acme-challenge` ; `tls-alpn-01` (RFC 8737) n'a besoin que du 443. Le wildcard passe par `dns-01` (c'est ainsi que Traefik le documente) — comme tout serveur qu'aucune autorité ne peut joindre.
- **Let's Encrypt** limite les émissions (doc mise à jour le 2026-08-05) : 50 certificats par domaine enregistré et par semaine, 5 pour un même jeu de noms, 5 échecs d'autorisation par heure. Les renouvellements annoncés par ARI en sont exemptés. Un `/data` qui n'est pas persistant, un `acme.json` perdu ou un rechargement de [[HAProxy]] qui redemande un certificat butent sur ces plafonds.
- **Les durées de vie fondent.** Le ballot SC-081v3 du CA/Browser Forum (adopté en avril 2025 ; 25 autorités pour, 0 contre, et les quatre « consommateurs » — Apple, Google, Microsoft, Mozilla — pour) fixe la durée maximale à **200 jours depuis le 2026-03-15**, 100 jours le 2027-03-15 et **47 jours le 2029-03-15** ; la réutilisation d'une validation de domaine tombe à 10 jours. Let's Encrypt suit : profil de 45 jours en option depuis le 2026-05-13, profil par défaut à 64 jours le 2027-02-10 puis 45 jours le 2028-02-16 ; un profil de 6 jours (160 heures) est disponible depuis le 2026-01-15 et devient obligatoire pour un certificat d'adresse IP. **La rotation à la main n'est plus tenable** : c'est une inférence de ces chiffres, pas une phrase de source.
- **Ce qui a disparu en route.** L'OCSP de Let's Encrypt est coupé depuis le 2025-08-06 (le remplaçant est la CRL) : l'agrafage OCSP n'a plus d'objet avec cette autorité. Le profil par défaut n'a plus l'extension `clientAuth` depuis le 2026-02-11 : un certificat public ne sert plus à authentifier un client, et Let's Encrypt renvoie ces usages vers une autorité privée.

### Une autorité interne, pour ce qui n'est pas sur Internet

- **Pourquoi.** Les exigences de base interdisent les noms internes (`.lan`, `.corp`) et les adresses réservées dans un certificat public : un service qui n'a pas de nom public ne peut pas en avoir. Il faut une autorité privée.
- **Les options.** **step-ca** (Smallstep, Apache-2.0, v0.30.2 du 2026-03-23, environ 8 900 étoiles) : un serveur ACME privé avec quatre challenges, dont `dns-01` ; une seule intermédiaire émettrice ; racine hors ligne et intermédiaire en ligne recommandées ; certificats de 24 h par défaut ; révocation passive, CRL en option ; base MySQL ou PostgreSQL pour la haute disponibilité. **cert-manager** (Apache-2.0, v1.21.2 du 2026-09-11, CNCF diplômé depuis 2024-09-29) : les émetteurs `CA`, `Vault`, `ACME` et autosigné dans Kubernetes. **Vault PKI** est sous **BUSL-1.1** depuis août 2023 ; **OpenBao** (MPL-2.0, Linux Foundation) en est le fork. **[[Caddy]]** embarque une autorité locale et un serveur ACME. **mkcert** (BSD-3-Clause) est « pour le développement, pas pour la production ». EJBCA, Dogtag et AD CS n'ont pas été documentés ici.
- **Les règles de l'art.** Un SAN par nom : la RFC 9525 interdit d'identifier un service par le Common Name. Des contraintes de nom (RFC 5280 §4.2.1.10) sur l'intermédiaire limitent les dégâts si elle fuit. Des certificats courts renouvelés par ACME valent mieux qu'une révocation.
- **Le coût réel : les clients.** Une autorité privée ne vaut que si **chaque** machine cliente la reconnaît, et il y a plusieurs magasins : le magasin système (`step ca bootstrap --install`, `caddy trust`), `certifi` pour `requests` (variable `REQUESTS_CA_BUNDLE` ou paramètre `verify` ; le flux `PreparedRequest` ignore l'environnement), `SSL_CERT_FILE` et `SSL_CERT_DIR` pour le module `ssl` de Python — qui, depuis 3.13, active `VERIFY_X509_STRICT` et peut rejeter un certificat mal formé —, `/etc/docker/certs.d/<hôte>/ca.crt` pour un registre, `NODE_EXTRA_CA_CERTS` pour Node, le magasin de Java, Firefox. Le magasin d'un conteneur applicatif n'a pas de source officielle lue ici : à tester.

### Les en-têtes de sécurité de base

- **HSTS** (RFC 6797) : `max-age` obligatoire, `includeSubDomains` optionnel ; ignoré sur un transport non sécurisé ; le premier accès reste vulnérable. **Le preload n'est pas dans la RFC** : il est géré par `hstspreload.org`, exige `max-age` d'un an au moins et `includeSubDomains`, vaut pour tous les sous-domaines — les internes compris — et ne se retire pas facilement (des mois).
- **Le reste**, selon la fiche OWASP « HTTP Headers » : `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, une `Permissions-Policy` qui coupe caméra, micro et géolocalisation, `X-Frame-Options: DENY` — que la directive CSP `frame-ancestors` remplace —, et `X-XSS-Protection` désactivé (`0`). La CSP n'a pas de valeur unique : MDN recommande `default-src` en repli et le mode `Report-Only` pour tester.
- **Limites à ne pas oublier** : Nginx plafonne le corps d'une requête à 1 Mo par défaut (413), ce qui arrête sans avertir un envoi de fichier ou de modèle ; `limit_req` limite le débit avec un seau qui fuit.

### Ingress et Gateway API en une section

- **Ingress** (Kubernetes, stable depuis 1.19) ne dit que HTTP et HTTPS, demande un contrôleur, et son API est **gelée** : plus de développement, pas de retrait prévu. Le contrôleur communautaire **ingress-nginx** a été retiré (annonce du 2025-11-11, dépôt archivé le 2026-03-24) : plus aucun correctif de sécurité, mais les installations existantes tournent encore.
- **Gateway API** sépare les rôles : le fournisseur d'infrastructure (`GatewayClass`), l'opérateur du cluster (`Gateway`), le développeur (`HTTPRoute`, `GRPCRoute`, `TLSRoute`). Version courante : v1.6.2 (2026-09-03) ; GA depuis la v1.0 (2023-10-31). Côté TLS : mode `Terminate` avec `certificateRefs`, mode `Passthrough` avec `TLSRoute`, et `BackendTLSPolicy` pour re-chiffrer vers l'origine. Traefik, Envoy Gateway, NGINX Gateway Fabric, Cilium et Istio figurent parmi les implémentations déclarées conformes ; [[HAProxy]] et [[Caddy]] n'ont qu'un support partiel ou en cours (TCPRoute expérimental pour le premier, dépôt « WIP » pour le second).
- **Migrer** : Ingress2Gateway 1.0 (2026-03-20) lit neuf fournisseurs, dont Ingress-NGINX, NGINX et Traefik ; Kubernetes insiste pour relire sa sortie avant la production. Le billet « cinq comportements surprenants » d'avant migration est à lire. Un cluster [[k3s]] a [[Traefik]] par défaut, qui lit les deux API.

## En pratique

- Un hôte, quelques conteneurs, un domaine public : [[Caddy]] (HTTPS sans y penser) ou [[Traefik]] (découverte des conteneurs dans [[Docker Compose]]).
- Un site industriel sans accès à Internet : une autorité interne (step-ca) et un proxy qui parle ACME à son adresse ; la distribution de la racine aux clients est le premier chantier, pas le dernier.
- Un service ML qui reçoit de gros corps : relever `client_max_body_size` et les délais, et dire à [[Uvicorn]] quels proxys croire.
- Exposer les métriques du proxy à [[Prometheus]] ; les tableaux de bord vont dans [[Grafana]].
- Pour [[Kubernetes]] : ne pas déployer ingress-nginx ; partir de Gateway API avec un contrôleur qui la déclare conforme.

## Approches voisines & alternatives

- [[Traefik]], [[Caddy]], [[Nginx]], [[HAProxy]] — les quatre proxys du brain ; [[Comparatif - Reverse proxies]] dit ce qui les sépare.
- **Envoy** (Apache-2.0, C++, CNCF diplômé depuis 2018, v1.39.1 du 2026-08-27, environ 29 000 étoiles), sans fiche. C'est un plan de données piloté par API (xDS), embarqué dans Istio, Cilium et Envoy Gateway. Il n'a **pas d'ACME natif** (demande ouverte depuis 2016), et un reverse proxy TLS coûte environ 40 à 50 lignes de YAML typé, sans découverte Docker. À rencontrer sans avoir à le configurer. **Envoy Gateway** (Apache-2.0, v1.9.2 du 2026-09-28, conforme Gateway API) est l'usage naturel sur Kubernetes ; son mode hors Kubernetes est déclaré expérimental, à ne pas utiliser en production.
- **Contour** (CNCF incubation, v1.33.7) est actif, mais absent de la liste des implémentations Gateway API. **Emissary** aussi est actif.
- Les VPN et réseaux maillés ne sont pas traités : écartés du périmètre.
- Voir aussi : [[OpenBao]], [[Gestion des secrets]], [[Authelia]], [[Authentik]].
- [[API REST, GraphQL et gRPC]] — les styles d'API que le proxy ou la passerelle expose, dont gRPC (HTTP/2 et trailers).

## Pour aller plus loin

- RFC 9110 §3.7 — intermédiaires : https://www.rfc-editor.org/rfc/rfc9110.html#name-intermediaries
- RFC 7239 — `Forwarded` : https://www.rfc-editor.org/rfc/rfc7239.html ; MDN — `X-Forwarded-For` : https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-For
- PROXY protocol : https://www.haproxy.org/download/3.0/doc/proxy-protocol.txt
- Uvicorn — déploiement et réglages : https://uvicorn.dev/deployment/ ; FastAPI — derrière un proxy : https://fastapi.tiangolo.com/advanced/behind-a-proxy/ ; Flask — `ProxyFix` : https://flask.palletsprojects.com/en/stable/deploying/proxy_fix/
- RFC 8446 (TLS 1.3) : https://www.rfc-editor.org/rfc/rfc8446.html ; profils : https://docs.tlsref.org/server-side-tls.html
- RFC 8555 (ACME) : https://www.rfc-editor.org/rfc/rfc8555.html ; RFC 8737 : https://www.rfc-editor.org/rfc/rfc8737.html
- Let's Encrypt — limites : https://letsencrypt.org/docs/rate-limits/ ; « From 90 to 45 » : https://letsencrypt.org/2025/12/02/from-90-to-45 ; fin d'OCSP : https://letsencrypt.org/2024/12/05/ending-ocsp/
- CA/Browser Forum — ballot SC-081v3 : https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/
- step-ca en production : https://smallstep.com/docs/step-ca/certificate-authority-server-production/ ; cert-manager : https://cert-manager.io/docs/configuration/
- RFC 9525 (identités de service) : https://www.rfc-editor.org/rfc/rfc9525.html ; RFC 5280 : https://www.rfc-editor.org/rfc/rfc5280.html
- HSTS — RFC 6797 : https://www.rfc-editor.org/rfc/rfc6797.html ; preload : https://hstspreload.org/ ; OWASP — HTTP Headers : https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
- Kubernetes — Ingress : https://kubernetes.io/docs/concepts/services-networking/ingress/ ; retraite d'ingress-nginx : https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/ ; Gateway API — TLS : https://gateway-api.sigs.k8s.io/guides/tls/ ; implémentations : https://gateway-api.sigs.k8s.io/implementations/
- Envoy — ACME (demande ouverte) : https://github.com/envoyproxy/envoy/issues/96
