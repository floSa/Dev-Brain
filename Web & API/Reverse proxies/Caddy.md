---
role: brique
nom: Caddy
alias: [caddy server]
pitch: "Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire."
categorie: web/proxy
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[Traefik]]", "[[Nginx]]", "[[HAProxy]]"]
complements: ["[[Docker Compose]]", "[[Prometheus]]", "[[Authelia]]", "[[Authentik]]"]
tags: [reverse-proxy, tls, self-hosted]
url_docs: https://caddyserver.com/docs/
url_repo: https://github.com/caddyserver/caddy
---

# Caddy

<!-- AUTO:BANDEAU:START -->
> Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur web et reverse proxy en Go qui passe en HTTPS **dès qu'il connaît un nom d'hôte**, sans réglage : Let's Encrypt, puis ZeroSSL en secours, pour un nom public ; sa propre autorité (`tls internal`) pour un nom privé. Le format natif est le JSON, le Caddyfile n'en est qu'un adaptateur ; une API d'administration (`localhost:2019`) recharge la configuration sans coupure. Pour l'on-prem, c'est l'autorité interne qui compte : certificats feuilles de 12 h et intermédiaire de 7 jours par défaut, `caddy trust` pour installer la racine dans le magasin local, et la directive `acme_server` qui fait d'un Caddy un serveur ACME interne qu'un autre Caddy interroge par `acme_ca`. Relevé le 2026-09-30 : **v2.11.4** (2026-06-03), environ 76 200 étoiles, dernier commit du jour, aucune release depuis quatre mois.

Licence **Apache-2.0**. Le README présente Caddy comme un projet de ZeroSSL, société de HID Global ; la marque appartient à Stack Holdings GmbH. Aucune édition payante ni fonction verrouillée n'a été trouvée : le seul volet commercial est le support, par le sponsoring.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Quelques services derrière un fichier lisible, et un HTTPS auquel il n'y a plus à penser | Des conteneurs qui apparaissent et disparaissent : aucune découverte native ; `caddy-docker-proxy` (MIT, v2.13.1 du 2026-07-02) est le projet d'un particulier et exige le socket Docker → [[Traefik]] |
| Des certificats internes sans outil de plus : autorité locale, serveur ACME interne, `acme_ca` vers step-ca | Un ingress Kubernetes : le contrôleur officiel est « WIP », dernière release v0.2.1 en novembre 2023, et l'implémentation Gateway API l'est aussi → [[Traefik]] |
| HTTP/3 par défaut et des journaux JSON structurés sans configuration | Un DNS-01 (wildcard, hôte injoignable depuis Internet) ou un WAF : chaque module se compile avec `xcaddy`, et toute mise à jour reconstruit le binaire |
| | Un débit maximal sous forte charge : le seul essai comparatif détaillé (2022) place nginx optimisé devant à partir de 500 clients simultanés, avec le ramasse-miettes de Go en cause — ancien, à refaire avant d'en conclure → [[Nginx]], [[HAProxy]] |

## Mise en œuvre

- Installation — image officielle `caddy` (volumes `/data` et `/config`) ou paquets Debian et Fedora ; modules tiers par `xcaddy build --with <module>`
- Point d'entrée — un Caddyfile : `app.exemple.lan { reverse_proxy app:8000 }` ; `caddy validate`, puis `caddy reload`
- Prérequis — `/data` **persistant**, sinon les certificats sont réémis à chaque redémarrage et les limites de débit ACME s'appliquent ; ports 80 et 443 joignables pour HTTP-01 et TLS-ALPN-01 ; dans Docker, `localhost` désigne le conteneur, pas l'hôte ; en service, `sudo caddy trust` à lancer soi-même
- Prérequis — certificats : challenge DNS-01 par un module (`caddy-dns/cloudflare` : Apache-2.0, environ 1 000 étoiles) ; `acme_ca` et `acme_ca_root` pour un serveur interne (documenté par Smallstep) ; racine de l'autorité locale à distribuer à la main aux autres clients ; on-demand TLS réservé aux domaines vérifiés par un point `ask`, faute de quoi un attaquant peut épuiser les ressources ; mTLS par `client_auth`
- Exécution — journaux d'accès **désactivés par défaut** (directive `log`) ; métriques Prometheus sur `:2019/metrics` (option `metrics`, `per_host` gonfle la cardinalité) ; `trusted_proxies` ne fait confiance à personne par défaut ; **l'API d'administration reconfigure tout le serveur** : en boucle locale par défaut, avec des correctifs de sécurité en 2.11.1 et 2.11.3 — la restreindre (socket Unix) ou la couper (`admin off`, au prix du rechargement à chaud)
- Coût — gratuit sous Apache-2.0 ; support par sponsoring

## Écosystème

### Alternatives

- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — découvre ses routes tout seul, là où Caddy demande un Caddyfile.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — la référence installée, sans HTTPS automatique de série.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise. — la répartition de charge d'abord, sans serveur de fichiers.

### Compléments

- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — l'image officielle et ses deux volumes tiennent dans un service de la pile
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — Caddy expose ses métriques sur son port d'administration
- [[Authelia]] — Portail d'authentification et de SSO placé devant un reverse proxy (forward auth pour Traefik, Caddy et Nginx) : mot de passe plus MFA (TOTP, WebAuthn, Duo), utilisateurs en fichier ou LDAP, et fournisseur OIDC certifié — pas de SAML, pas de déconnexions OIDC (Apache-2.0, Go, communautaire, aucune offre payante). — l'exemple officiel de la directive `forward_auth` de Caddy nomme Authelia.
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — page d'intégration du forward auth avec Caddy.

## Ressources

- Documentation — https://caddyserver.com/docs/
- Dépôt — https://github.com/caddyserver/caddy
- Documentation — HTTPS automatique : https://caddyserver.com/docs/automatic-https
- Documentation — reverse proxy en démarrage rapide : https://caddyserver.com/docs/quick-starts/reverse-proxy
- Documentation — directive `tls` : https://caddyserver.com/docs/caddyfile/directives/tls
- Documentation — API d'administration : https://caddyserver.com/docs/api
- Dépôt — caddy-docker-proxy : https://github.com/lucaslorentz/caddy-docker-proxy
- Dépôt — contrôleur d'ingress : https://github.com/caddyserver/ingress
- Documentation — Caddy comme client d'un step-ca : https://smallstep.com/docs/tutorials/acme-protocol-acme-clients/

## Voir aussi

- [[Reverse proxies]] — le hub du sous-domaine
- [[Comparatif - Reverse proxies]] — ce qui départage les quatre proxys : configuration, découverte, certificats, performance, exploitation
- [[Reverse proxy et TLS]] — la notion : terminaison TLS, ACME contre autorité interne, en-têtes, Ingress et Gateway API
