---
role: comparatif
nom: Comparatif - Reverse proxies
categorie: web/proxy
tags: [reverse-proxy]
---

# Comparatif - Reverse proxies

> On tranche sur : la façon dont le proxy apprend ses routes (fichier, conteneurs qui bougent), la gestion des certificats (ACME, autorité interne), ce que la licence laisse hors de l'édition libre — trois des quatre ont une offre payante qui verrouille des fonctions, seul Caddy n'en a pas — et ce que coûte son exploitation.

![[Comparatif - Reverse proxies.base]]

## Ce qui départage

- [[Traefik]] — les routes viennent des labels Docker ou des ressources Kubernetes (Ingress, IngressRoute, Gateway API), sans fichier à éditer ni rechargement ; ACME intégré et pointable vers une autorité interne ; livré par défaut dans k3s. Le prix : OIDC, JWT, WAF et Let's Encrypt partagé entre instances sont dans l'offre payante Traefik Hub, le socket Docker donne l'accès à l'hôte, et chaque mineure n'a que 6 mois de support actif.
- [[Caddy]] — un fichier de quelques lignes suffit et l'HTTPS est automatique, y compris avec sa propre autorité pour les noms privés et un serveur ACME interne. Seul des quatre à n'avoir aucune édition payante trouvée. Le prix : aucune découverte de conteneurs native, et tout module (DNS-01, WAF) oblige à recompiler le binaire.
- [[Nginx]] — la référence installée (30,8 % des sites dont le serveur est connu), proxy et serveur de fichiers dans un seul processus, configuration écrite à la main. Le module ACME officiel ne fait ni wildcard ni DNS-01, les health checks actifs et l'API dynamique sont dans NGINX Plus, et le nom recouvre aussi un contrôleur Kubernetes **archivé** (ingress-nginx) à ne pas confondre avec ceux de F5.
- [[HAProxy]] — la répartition de charge TCP et HTTP la plus outillée de l'édition libre (health checks actifs, stick-tables, rechargement sans coupure, branche LTS de cinq ans). Le prix : aucun fichier statique, l'ACME natif est encore expérimental, le WAF et la synchronisation multi-nœuds sont dans Enterprise.

**Critère par critère**

**Configuration.** Traefik : statique plus dynamique, tout en labels ou en CRD. Caddy : un Caddyfile ou du JSON, rechargé par une API d'administration à protéger. Nginx : `nginx.conf`, rechargé par signal ; un nom d'hôte statique n'est résolu qu'au démarrage. HAProxy : un `haproxy.cfg` avec `frontend` et `backend`, une Runtime API sur socket.

**Découverte Docker et Kubernetes.** Native chez Traefik seul (provider Docker, Ingress, IngressRoute, Gateway API v1.6.2, couche de compatibilité ingress-nginx). Chez les trois autres, il faut un projet tiers ou une API : `caddy-docker-proxy` (particulier, MIT) et un ingress officiel « WIP » pour Caddy ; `nginx-proxy` et les contrôleurs de F5 pour Nginx ; `resolvers` DNS, `server-template`, Data Plane API et un contrôleur officiel dont la Gateway API se limite à TCPRoute pour HAProxy.

**Certificats.** ACME intégré chez Traefik (HTTP-01, TLS-ALPN-01, DNS-01, mono-instance en édition libre) et chez Caddy (idem, DNS-01 par module, stockage partageable entre instances). Nginx : module officiel en HTTP-01 et TLS-ALPN-01 seulement. HAProxy : natif depuis la 3.2 mais expérimental, HTTP-01 seul géré de bout en bout. Traefik, Caddy et Nginx documentent la visée d'un serveur ACME interne comme step-ca, chacun avec son réglage pour faire confiance à sa racine (`caCertificates`, `acme_ca_root`, `ssl_trusted_certificate`) ; pour HAProxy, le paramètre `directory` de la section `acme` le suggère, non testé ici. Seul Caddy embarque sa propre autorité.

**Performance.** Aucune source du brain ne départage sérieusement les quatre. Un essai de 2026 à 5 000 requêtes par seconde (Caddy 2.11.2, Nginx 1.28.3, Traefik 3.6.13, HAProxy 3.3.6 ; dépôt archivé, matériel non précisé) donne Caddy et HAProxy à environ 0,41 ms en HTTP/1.1 et Traefik en tête en HTTPS (environ 0,48 ms), sans erreur. Un billet de mars 2026 (4 vCPU, fichier de 164 octets) mesure, en requêtes par seconde en HTTP puis HTTPS : Nginx 60 382 et 53 162, HAProxy 57 164 et 51 298, Caddy 51 826 et 47 437 — versions inégales, un seul test. Un essai de 2022 place Nginx optimisé devant Caddy au-delà de 500 clients simultanés. Pour Traefik, aucune mesure indépendante et récente : le seul chiffre trouvé vient d'un concurrent (2020). Le projet HAProxy publie 2,04 millions de requêtes par seconde sur une instance (2021). Les comparaisons de blog concluent que l'application reste le goulot avant le proxy ; c'est un constat de blog, non une mesure.

**Exploitation.** Métriques Prometheus natives chez Traefik, Caddy (`metrics`) et HAProxy (export intégré à compiler ou dans l'image officielle) ; chez Nginx, `stub_status` et un exporteur séparé, les métriques par upstream étant dans Plus. Journaux d'accès : désactivés par défaut chez Caddy (directive `log`), au format common ou JSON chez Traefik, envoyés en syslog par HAProxy. Cycle de vie : Traefik demande une montée de version tous les six mois environ ; HAProxy a une LTS de cinq ans ; Nginx publie des correctifs de sa branche stable environ chaque mois, avec de nombreuses failles HTTP/3 corrigées en 2026.

**Pas de fiche ici**, faute d'avoir passé le critère « éprouvé et utile en on-prem » :

- Envoy — Apache-2.0, C++, CNCF diplômé depuis 2018, v1.39.1 (2026-08-27), environ 29 000 étoiles : éprouvé, mais c'est un plan de données piloté par API, embarqué dans Istio, Cilium et Envoy Gateway. Pas d'ACME natif (demande ouverte depuis 2016), environ 40 à 50 lignes de YAML pour un reverse proxy TLS, aucune découverte Docker. Le mode hors Kubernetes d'Envoy Gateway est déclaré expérimental, « à ne pas utiliser en production ». Mentionné dans la notion.
- kubernetes/ingress-nginx — archivé le 2026-03-24, plus de correctifs de sécurité ; voir la fiche de [[Nginx]].
- freenginx (fork de Nginx par un ancien développeur principal, 2024), Angie (fork d'anciens développeurs de Nginx, ACME natif avec DNS-01, édition PRO à côté), OpenResty (Nginx et Lua), Tengine : décrits dans la fiche de [[Nginx]], sans fiche propre.
- Contour (CNCF incubation, v1.33.7) : actif, mais absent de la liste des implémentations Gateway API. Emissary : actif.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Reverse proxies]] — le hub du dossier.
- [[Reverse proxy et TLS]] — la notion : terminaison TLS, ACME contre autorité interne, en-têtes, Ingress et Gateway API.
