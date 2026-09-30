---
role: brique
nom: Nginx
alias: [nginx.conf]
pitch: "Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24."
categorie: web/proxy
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Traefik]]", "[[Caddy]]", "[[HAProxy]]"]
complements: ["[[Uvicorn]]", "[[Docker Compose]]", "[[Kubernetes]]", "[[Argo CD]]", "[[Prometheus]]", "[[FastAPI]]", "[[Flask]]", "[[Authelia]]", "[[Authentik]]"]
tags: [reverse-proxy, tls, load-balancer, kubernetes, self-hosted]
url_docs: https://nginx.org/en/docs/
url_repo: https://github.com/nginx/nginx
---

# Nginx

<!-- AUTO:BANDEAU:START -->
> Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C | open-core | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur web et reverse proxy en C, piloté par des fichiers texte (`nginx.conf`) : `nginx -s reload` valide la configuration, démarre de nouveaux processus et laisse les anciens finir leurs connexions ; en cas d'erreur, l'ancienne configuration reste. Deux branches : la **stable** (1.30.5) et la **mainline** (1.31.6), toutes deux du 2026-09-15 — la mainline corrige un dépassement de tampon dans HTTP/3 (CVE-2026-90439). Licence BSD 2-clauses, miroir GitHub à environ 31 800 étoiles, propriété de F5 depuis 2019. Adoption : 30,8 % des sites dont le serveur est connu (W3Techs, 2026-09-30), en recul sur Netcraft depuis janvier 2026.

**Trois choses portent le nom, à ne pas confondre.** (1) Le serveur libre de nginx.org. (2) **NGINX Plus**, l'édition payante de F5 : abonnement, licence JWT, rapport d'usage obligatoire à F5 (y compris hors ligne, avec NGINX Instance Manager, sinon le trafic est bloqué après 180 jours de grâce). Elle garde pour elle les health checks actifs, l'API de reconfiguration, l'authentification JWT et les métriques par upstream ; l'écart se réduit (`resolve`, `sticky learn`, `drain`, `least_time` sont descendus dans l'édition libre). (3) Les contrôleurs Kubernetes, dont l'un est **arrêté** :

- **kubernetes/ingress-nginx** (communautaire, Apache-2.0) : retraite annoncée le 2025-11-11, dépôt archivé le 2026-03-24, plus aucun correctif de sécurité. Il a porté la faille « IngressNightmare » (CVE-2025-1974, CVSS 9.8, exécution de code à distance). Rien de neuf ne s'y déploie.
- **F5 NGINX Ingress Controller** (Apache-2.0, v5.6.3 du 2026-09-16) et **NGINX Gateway Fabric** (Gateway API, v2.7.2) : deux produits distincts, maintenus par F5.

**Ce que la retraite change pour qui connaît `nginx.conf`** : aucun contrôleur n'expose la configuration brute. Les annotations `nginx.ingress.kubernetes.io/*` et les *snippets* n'ont pas d'équivalent un pour un, et c'est l'injection de configuration par annotation qui portait IngressNightmare. Kubernetes recommande Gateway API, avec l'outil Ingress2Gateway 1.0 (2026-03-20) pour migrer.

**Forks** (sans fiche) : freenginx (Maxim Dounin, 2024, fork né d'un désaccord avec F5 sur le traitement des failles du HTTP/3 expérimental ; licence de type BSD, actif) ; Angie (Web Server LLC, BSD-2-Clause, v1.12.2 du 2026-09-18, ACME natif avec DNS-01, édition PRO à côté) ; OpenResty (nginx + Lua).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un proxy et des fichiers statiques dans un seul processus, avec la documentation la plus abondante | Des certificats sans effort : le module ACME officiel (`nginx-acme`, Rust, Apache-2.0, v0.4.1) ne fait que HTTP-01 et TLS-ALPN-01, sans wildcard ni DNS-01 → [[Caddy]], [[Traefik]] |
| Un serveur d'application à mettre derrière : la doc d'[[Uvicorn]] recommande Nginx devant | Des conteneurs qui bougent : aucune découverte native ; `nginx-proxy` + `acme-companion` (MIT) sont des projets tiers → [[Traefik]] |
| Un ingress Kubernetes maintenu : F5 NGINX Ingress Controller ou NGINX Gateway Fabric | Des health checks actifs, une API de reconfiguration ou du JWT sans payer Plus |
| Des réglages fins connus (timeouts, tampons, limites) | HTTP/3 sans réserve : la doc du module le dit encore expérimental, et les failles HTTP/3 se sont succédé en 2026 |

## Mise en œuvre

- Installation — image `nginx` (stable ou mainline) ou paquets nginx.org ; module ACME : paquet `nginx-module-acme`
- Point d'entrée — `nginx.conf` : `server { listen 443 ssl; ssl_certificate …; location / { proxy_pass http://app:8000; proxy_set_header Host $host; } }` ; `nginx -t`, puis `nginx -s reload`
- Prérequis — un nom d'hôte statique dans `proxy_pass` est résolu **une seule fois**, au démarrage : `server … resolve;` dans un `upstream` (édition libre depuis 1.27.3) ou une variable avec `resolver`, sinon « host not found in upstream » ; `proxy_ssl_verify` est **désactivé** par défaut vers un backend HTTPS ; `client_max_body_size` vaut 1 Mo, un envoi de fichier ou de modèle échoue en 413
- Prérequis — certificats : `ssl_certificate` et `ssl_certificate_key` ; `ssl_protocols TLSv1.2 TLSv1.3` par défaut ; module ACME vers une autorité interne : `acme_issuer x { uri …; ssl_trusted_certificate …; }` ; l'agrafage OCSP est désactivé par défaut et sans objet avec Let's Encrypt, dont les répondeurs OCSP sont coupés depuis le 2025-08-06
- Exécution — `stub_status` (sept compteurs) et `nginx-prometheus-exporter` (Apache-2.0) ; les métriques par upstream demandent Plus ; correctifs de branche stable environ mensuels
- Coût — gratuit sous BSD-2-Clause ; Plus par abonnement, prix non publié

## Écosystème

### Alternatives

- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — découvre ses routes tout seul, là où Nginx demande un fichier édité.
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — l'HTTPS automatique de série, y compris avec une autorité interne.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise. — la répartition de charge d'abord, health checks actifs en édition libre.

### Compléments

- [[Uvicorn]] — Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI. — sa documentation recommande Nginx devant ses processus
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — `nginx-proxy` et `acme-companion` lisent les conteneurs de la pile
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — via les contrôleurs de F5, jamais via ingress-nginx
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — sa documentation décrit le F5 NGINX Ingress Controller pour exposer le serveur
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — par `nginx-prometheus-exporter`, en lisant `stub_status`
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — sa documentation le cite comme proxy possible.
- [[Flask]] — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions. — sa documentation lui consacre une page, avec `ProxyFix` côté application.
- [[Authelia]] — Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante). — intégration par `auth_request`, module à compiler (`--with-http_auth_request_module`).
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — page d'intégration par `auth_request`, ingress-nginx compris.

## Ressources

- Documentation — https://nginx.org/en/docs/
- Dépôt — https://github.com/nginx/nginx
- Documentation — module ACME : https://nginx.org/en/docs/http/ngx_http_acme_module.html
- Documentation — module `upstream` (ce qui est réservé à Plus) : https://nginx.org/en/docs/http/ngx_http_upstream_module.html
- Article — retraite d'ingress-nginx : https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/
- Article — Ingress2Gateway 1.0 : https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/
- Documentation — F5 NGINX Ingress Controller : https://docs.nginx.com/nginx-ingress-controller/
- Documentation — NGINX Gateway Fabric : https://docs.nginx.com/nginx-gateway-fabric/
- Documentation — fork freenginx : https://freenginx.org/
- Documentation — fork Angie : https://en.angie.software/

## Voir aussi

- [[Reverse proxies]] — le hub du sous-domaine
- [[Comparatif - Reverse proxies]] — ce qui départage les quatre proxys : configuration, découverte, certificats, performance, exploitation
- [[Reverse proxy et TLS]] — la notion : terminaison TLS, ACME contre autorité interne, en-têtes, Ingress et Gateway API
