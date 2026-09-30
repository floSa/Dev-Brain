---
role: brique
nom: HAProxy
alias: [haproxy.cfg]
pitch: "Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise."
categorie: web/proxy
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Traefik]]", "[[Caddy]]", "[[Nginx]]"]
complements: ["[[Kubernetes]]", "[[Prometheus]]"]
tags: [reverse-proxy, tls, load-balancer, self-hosted]
url_docs: https://docs.haproxy.org/
url_repo: https://github.com/haproxy/haproxy
---

# HAProxy

<!-- AUTO:BANDEAU:START -->
> Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C | open-core | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Répartiteur de charge et reverse proxy L4 et L7 en C, dont Willy Tarreau est le développeur principal, HAProxy Technologies étant l'entreprise qui vend le support et l'édition Enterprise, configuré dans un `haproxy.cfg` (sections `global`, `defaults`, `frontend`, `backend`). Il ne lit **aucun fichier après son démarrage** : pas de serveur de fichiers statiques, et les certificats obtenus par ACME sont à ressortir par la Runtime API. Le rechargement se fait sans coupure en mode master-worker. Relevé le 2026-09-30 : **3.4.6** (2026-09-28), branche **LTS 3.4** sortie le 2026-06-03 et soutenue jusqu'au deuxième trimestre 2031 ; miroir GitHub à environ 6 900 étoiles. Une branche paraît tous les six mois, les paires sont LTS.

**Licence** : GPL-2.0 pour l'essentiel du code, LGPL pour les en-têtes exportables (des modules non GPL restent possibles), exception pour lier OpenSSL — GitHub n'en tire aucun identifiant de licence. **L'offre est à cœur ouvert** : HAProxy Enterprise ne retire rien, il ajoute le WAF, la gestion des robots, le CAPTCHA, SAML, les modules de haute disponibilité, la synchronisation des maps, ACL et clés de tickets TLS entre nœuds, le plan de contrôle Fusion et le support. L'édition libre garde health checks, stick-tables, rate limiting, Lua, cache, Data Plane API et images Docker.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Répartir la charge avec précision, TCP autant que HTTP | Servir des fichiers statiques ou un site : rien n'est lu sur disque après le démarrage → [[Nginx]], [[Caddy]] |
| Des health checks actifs, des stick-tables et un rate limiting sans licence | Des certificats automatiques sans effort : l'ACME natif (depuis 3.2) est **expérimental** en 3.4 et demande `expose-experimental-directives` ; HAProxy ne gère seul que HTTP-01, DNS-01 passe par la Data Plane API, un script Lua ou un outil tiers → [[Caddy]], [[Traefik]] |
| Une branche LTS de cinq ans, et Prometheus intégré depuis la 2.0 | Des conteneurs qui apparaissent et disparaissent : pas de découverte Docker native, seulement `resolvers` DNS et `server-template`, ou la Data Plane API (Consul, AWS) → [[Traefik]] |
| Un rechargement sans perte de connexion sur du trafic soutenu | Un ingress Kubernetes HTTP : le contrôleur officiel (`haproxytech/kubernetes-ingress`, Apache-2.0, v3.2.15) n'offre côté Gateway API que TCPRoute, expérimental ; un WAF ou du multi-nœuds synchronisé sans payer |

## Mise en œuvre

- Installation — image officielle `haproxy` (compilée avec QUIC, Lua et l'export Prometheus) ; dépôt haproxy.debian.net ; paquets « Performance Packages » gratuits de HAProxy Technologies avec AWS-LC, dès la 3.2
- Point d'entrée — `frontend fe { bind :443 ssl crt /etc/haproxy/site.pem alpn h2,http/1.1 ; default_backend be }` et `backend be { server app1 10.0.0.11:8080 check }` ; une socket `stats socket` pour la Runtime API
- Prérequis — certificat, chaîne et clé dans **un même** PEM ; un binaire compilé à la main demande `USE_PROMEX=1` pour l'export Prometheus ; OpenSSL 3.x coûte cher sur la reprise de session TLS (le projet publie 1 500 connexions par seconde sur OpenSSL 3.0.2 contre 183 000 avec AWS-LC), d'où les paquets ci-dessus
- Prérequis — certificats : `crt-list` et `crt-store` ; section `acme` dont `directory` désigne l'autorité (une autorité interne compatible ACME est suggérée par ce paramètre, non testée ici) ; liaison de compte externe (EAB) en 3.4 ; sans persistance sur disque, un rechargement redemande le certificat et les limites de débit de l'autorité s'appliquent ; mTLS par `verify required ca-file`
- Exécution — page de statistiques, environ 150 métriques Prometheus, journaux envoyés en syslog (pas de fichier tenu par HAProxy) ; la 3.3 a supprimé la section `program`
- Coût — gratuit sous GPL-2.0 ; Enterprise sur devis

## Écosystème

### Alternatives

- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — découvre ses routes tout seul, là où HAProxy demande un fichier ou une API.
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — les certificats automatiques, et un serveur de fichiers en plus.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — proxy et serveur de fichiers dans un seul processus, health checks actifs réservés à Plus.

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — via le contrôleur d'ingress officiel de HAProxy Technologies
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — l'export est intégré, sans exporteur séparé

## Ressources

- Documentation — https://docs.haproxy.org/
- Dépôt — https://github.com/haproxy/haproxy
- Documentation — versions maintenues : https://www.haproxy.org/
- Documentation — manuel de configuration 3.4 : https://docs.haproxy.org/3.4/configuration.html
- Documentation — édition libre et Enterprise : https://www.haproxy.com/products/upgrade-haproxy-to-haproxy-enterprise
- Documentation — ACME natif, état et limites : https://github.com/haproxy/wiki/wiki/ACME:--native-haproxy
- Dépôt — contrôleur d'ingress : https://github.com/haproxytech/kubernetes-ingress
- Article — piles SSL et performance : https://www.haproxy.com/blog/state-of-ssl-stacks

## Voir aussi

- [[Reverse proxies]] — le hub du sous-domaine
- [[Comparatif - Reverse proxies]] — ce qui départage les quatre proxys : configuration, découverte, certificats, performance, exploitation
- [[Reverse proxy et TLS]] — la notion : terminaison TLS, ACME contre autorité interne, en-têtes, Ingress et Gateway API
