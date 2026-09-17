---
role: hub
nom: Reverse proxies
alias: [proxys inverses, reverse proxies, load balancers]
pitch: Exposer des services derrière un nom, un certificat et une répartition de charge — le proxy qui reçoit le monde, et l'autorité qui signe ce qu'il présente.
domaines: [infra-ops, mlops]
tags: [reverse-proxy, tls, load-balancer]
---

# Reverse proxies

> Exposer des services derrière un nom, un certificat et une répartition de charge — le proxy qui reçoit le monde, et l'autorité qui signe ce qu'il présente.

## Ce qu'il faut comprendre

- **Deux questions, pas une.** Le choix du proxy ([[Traefik]], [[Caddy]], [[Nginx]], [[HAProxy]]) est la plus visible ; celle qui coûte est **qui signe le certificat et comment les clients lui font confiance**. [[Reverse proxy et TLS]] les traite ensemble : terminaison, passthrough, ACME, autorité interne, en-têtes, Ingress et Gateway API.
- **Trois des quatre ont une offre payante qui garde des fonctions.** Traefik Hub (OIDC, JWT, WAF, Let's Encrypt partagé), NGINX Plus (health checks actifs, API dynamique, JWT), HAProxy Enterprise (WAF, robots, synchronisation multi-nœuds). Le proxy libre suffit à exposer un service ; l'authentification, le WAF et la haute disponibilité des certificats sont ce qu'il faut prévoir ailleurs. Seul [[Caddy]] n'a pas d'édition payante trouvée.
- **Le proxy qui découvre ses routes est celui qui suit des conteneurs.** Seul [[Traefik]] lit Docker et Kubernetes nativement. Les autres se configurent par fichier ; c'est un avantage quand la liste des services ne bouge pas.
- **Nginx désigne trois choses.** Le serveur libre, l'offre payante, et des contrôleurs Kubernetes dont celui de la communauté (ingress-nginx) est **archivé** depuis le 2026-03-24. La fiche de [[Nginx]] les sépare.
- **Le piège est dans l'application, pas dans le proxy** : elle ne lit les en-têtes `X-Forwarded-*` que si on lui dit en quels proxys avoir confiance ([[Uvicorn]], [[FastAPI]], [[Flask]]).
- **Les VPN et réseaux maillés ne sont pas traités**, et Envoy n'a pas de fiche : le motif est dans [[Comparatif - Reverse proxies]].

## Choisir

- Des conteneurs Docker ou un cluster [[k3s]] qui bougent → [[Traefik]].
- Quelques services, un fichier lisible, du HTTPS sans y penser, éventuellement avec une autorité interne → [[Caddy]].
- La référence installée, un serveur de fichiers et un proxy dans un processus → [[Nginx]].
- La répartition de charge TCP et HTTP, des health checks actifs en édition libre → [[HAProxy]].
- Comprendre TLS, ACME et l'autorité interne avant de choisir → [[Reverse proxy et TLS]].

<!-- AUTO:START -->
### Notions
- [[Reverse proxy et TLS]] — domaines : infra-ops, mlops

### Briques
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24.
- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub.

### Comparatifs
- [[Comparatif - Reverse proxies]]
<!-- AUTO:END -->
