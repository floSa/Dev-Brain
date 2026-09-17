---
role: brique
nom: Traefik
alias: [traefik proxy]
pitch: "Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub."
categorie: web/proxy
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[Caddy]]", "[[Nginx]]", "[[HAProxy]]"]
complements: ["[[Docker Compose]]", "[[k3s]]", "[[Kubernetes]]", "[[Argo CD]]", "[[Prometheus]]", "[[FastAPI]]"]
tags: [reverse-proxy, tls, load-balancer, container, kubernetes, self-hosted]
url_docs: https://doc.traefik.io/traefik/
url_repo: https://github.com/traefik/traefik
---

# Traefik

<!-- AUTO:BANDEAU:START -->
> Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-core | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Reverse proxy en Go dont la configuration se scinde en deux : la partie **statique** (points d'entrée, fournisseurs, résolveurs de certificats), lue au démarrage, et la partie **dynamique** (routeurs, services, middlewares), recalculée à chaud à partir des *providers*. Le provider Docker surveille les événements du démon et lit les labels des conteneurs ; les providers Kubernetes lisent les ressources Ingress, les CRD IngressRoute et Gateway API. Un conteneur qui démarre avec ses labels est routé sans rechargement ni fichier à éditer. Relevé le 2026-09-30 : **v3.7.13** (2026-09-04), environ 65 000 étoiles ; la v2.11 est sortie du support de sécurité le 2026-09-07.

**Licence : le dépôt est MIT, mais l'offre a deux étages.** Le proxy est libre. **Traefik Hub**, propriétaire et facturé sur devis, ajoute ce qu'un service exposé réclame vite : JWT, OIDC, LDAP, introspection OAuth2, WAF Coraza, rate limit partagé entre instances, Let's Encrypt partagé entre instances. Le verrou est fonctionnel, pas juridique : l'édition libre garde BasicAuth, DigestAuth et ForwardAuth (déléguer l'authentification à un service externe). Les sources de l'éditeur se contredisent : la page d'accueil de la doc Hub dit que l'édition libre inclut JWT, OIDC et LDAP, le tableau des fonctions et la liste des middlewares disent le contraire ; la présente fiche suit ces deux derniers.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des conteneurs qui apparaissent et disparaissent, et un proxy qui suit sans qu'un fichier soit à éditer | Une authentification OIDC, JWT ou LDAP, un WAF ou un rate limit partagé, sans payer Hub : rien de tout cela n'est dans l'édition libre, il faut un service devant (ForwardAuth) |
| Un cluster [[k3s]] : Traefik y est livré par défaut, et le même binaire lit Ingress, IngressRoute et Gateway API | Plusieurs instances qui doivent chacune obtenir des certificats Let's Encrypt : le stockage `acme.json` est mono-instance dans l'édition libre, la doc oriente vers cert-manager |
| Un ingress à remplacer après l'arrêt d'ingress-nginx : une couche de compatibilité lit ses annotations (Traefik v3.6.2 ou plus) | Des annotations ingress-nginx à reprendre telles quelles : le support est partiel, à vérifier annotation par annotation avant de migrer |
| Un tableau de bord, des métriques Prometheus et des traces OpenTelemetry sans module à ajouter | Le débit brut comme critère : aucune mesure indépendante et récente n'a été trouvée pour Traefik (cf. le comparatif) |
| | Le cycle de mises à jour à ne pas subir : 6 mois de support actif par mineure, puis un support de sécurité limité — v3.6 est déjà hors support |

## Mise en œuvre

- Installation — image `traefik:v3.7` ; en [[Docker Compose]], un service avec `--providers.docker=true` et le socket monté ; sur k3s, déjà présent (`--disable=traefik` pour mettre le sien)
- Point d'entrée — des labels sur chaque conteneur : `traefik.http.routers.app.rule=Host(`app.exemple.lan`)`, `traefik.http.routers.app.tls=true`, `traefik.http.services.app.loadbalancer.server.port=8080`
- Prérequis — **le socket Docker donne l'accès à l'hôte** : la doc l'écrit, et propose un proxy de socket (Tecnativa), le TLS client sur le démon ou SSH ; `exposedByDefault` vaut `true`, à passer à `false` ; l'exemple officiel `--api.insecure=true` ouvre le tableau de bord sans authentification, à ne pas garder
- Prérequis — certificats : résolveur ACME intégré : HTTP-01, TLS-ALPN-01, DNS-01 (fournisseurs de la bibliothèque lego ; le wildcard exige DNS-01) ; `caServer` vise un serveur ACME interne comme step-ca et `caCertificates` fait confiance à sa racine ; renouvellement 30 jours avant l'échéance ; mTLS par les options TLS (`clientAuth`)
- Exécution — HTTP/3 (UDP, même port), TCP, UDP, gRPC, PROXY protocol v1 et v2 ; arrêt gracieux de 10 s par défaut ; le passage de v2 à v3 a cassé la syntaxe des règles, et les noms de routeurs générés par le provider Kubernetes ont changé à la v3.7.10 (tableaux de bord et requêtes à revoir)
- Coût — proxy gratuit sous MIT ; Traefik Hub sur devis, facturé par nœud, avec un jeton de licence annuel et 30 jours de grâce

## Écosystème

### Alternatives

- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — HTTPS automatique avec un fichier de quelques lignes, mais sans découverte de conteneurs native.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — la référence installée, écrite à la main : pas de découverte de conteneurs.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise. — le choix quand le besoin est la répartition de charge, TCP comme HTTP.

### Compléments

- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — le provider Docker lit les labels des services de la pile
- [[k3s]] — Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem. — Traefik y est l'ingress livré par défaut
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — Traefik y tient le rôle de contrôleur Ingress ou Gateway API
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — sa documentation décrit Traefik pour exposer le serveur, TLS terminé au proxy et `--insecure` côté Argo CD
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — Traefik expose ses métriques nativement
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — sa documentation prend Traefik pour exemple de proxy, avec `--root-path` et `--forwarded-allow-ips`.

## Ressources

- Documentation — https://doc.traefik.io/traefik/
- Dépôt — https://github.com/traefik/traefik
- Documentation — édition libre et Hub, fonction par fonction : https://doc.traefik.io/traefik/features/
- Documentation — résolveurs ACME : https://doc.traefik.io/traefik/v3.7/reference/install-configuration/tls/certificate-resolvers/acme/
- Documentation — provider Docker et risque du socket : https://doc.traefik.io/traefik/v3.7/reference/install-configuration/providers/docker/
- Documentation — provider Ingress NGINX : https://doc.traefik.io/traefik/v3.7/reference/install-configuration/providers/kubernetes/kubernetes-ingress-nginx/
- Documentation — versions et fin de support : https://doc.traefik.io/traefik/deprecation/releases/
- Documentation — licence de Traefik Hub : https://doc.traefik.io/traefik-hub/legal/licensing

## Voir aussi

- [[Reverse proxies]] — le hub du sous-domaine
- [[Comparatif - Reverse proxies]] — ce qui départage les quatre proxys : configuration, découverte, certificats, performance, exploitation
- [[Reverse proxy et TLS]] — la notion : terminaison TLS, ACME contre autorité interne, en-têtes, Ingress et Gateway API
