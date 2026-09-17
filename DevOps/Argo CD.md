---
role: brique
nom: Argo CD
alias: [argocd, argo-cd, argo cd, argo]
pitch: "Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé)."
categorie: devops/ci
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: []
complements: ["[[Kubernetes]]", "[[Helm]]", "[[GitHub Actions]]", "[[Traefik]]", "[[Nginx]]"]
tags: [ci-cd, kubernetes, gitops, self-hosted]
url_docs: https://argo-cd.readthedocs.io/
url_repo: https://github.com/argoproj/argo-cd
---

# Argo CD

<!-- AUTO:BANDEAU:START -->
> Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de livraison continue « GitOps » pour [[Kubernetes]]. Le dépôt Git dit ce qui doit tourner ;
Argo CD, installé **dans** le cluster, compare cet état voulu à l'état réel — manifestes bruts,
charts [[Helm]], Kustomize ou Jsonnet — et signale l'écart, ou le corrige. Le principe se lit
dans les quatre règles d'OpenGitOps : état déclaré, versionné, tiré automatiquement et réconcilié
en continu. Composants : un serveur d'API (interface web, CLI, SSO), un serveur de dépôts qui
rend les manifestes, un contrôleur qui réconcilie, un Redis de cache et, en option, Dex pour le
SSO. Une ressource `Application` décrit un déploiement, une `ApplicationSet` en génère plusieurs
depuis un dépôt, une liste ou des clusters. Relevé le 2026-09-30 : **v3.5.3** (2026-09-14),
environ 24 300 étoiles, Apache-2.0 ; projet Argo diplômé (graduated) à la CNCF le 2022-12-06.
Les mainteneurs viennent de plusieurs entreprises (Intuit, Akuity, Red Hat, Octopus Deploy).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un cluster Kubernetes déjà en place, dont on veut que l'état se lise et se rejoue depuis Git, avec la trace de qui a changé quoi | Pas de Kubernetes : l'outil n'en a aucun usage |
| Une interface web qui montre l'écart entre Git et le cluster, et des droits d'accès (RBAC, SSO) par équipe | Un cluster unique et petit, une équipe d'une personne : `kubectl apply` depuis une CI, ou [[Helm]] seul, est plus léger que cinq composants à opérer |
| Plusieurs clusters à piloter depuis un seul point, ou des dizaines d'applications déclarées par `ApplicationSet` | Des secrets en clair dans le dépôt : Argo CD n'en chiffre pas ; la doc recommande de les gérer **sur le cluster cible** (Sealed Secrets, External Secrets Operator) |
| Séparer la CI, qui construit l'image, du CD, qui la déploie : [[GitHub Actions]] pousse dans Git, Argo CD tire | Une réponse rapide à un incident : la boucle de réconciliation est de 120 secondes plus une gigue de 60, sauf webhook |

## Mise en œuvre

- Installation — manifeste `install.yaml` (ou la variante haute disponibilité `ha/install.yaml`) appliqué sur le cluster ; un chart Helm existe, maintenu par la communauté ; les mises à jour demandent `--server-side --force-conflicts`, certaines CRD dépassant la limite de l'application côté client
- Point d'entrée — l'interface web, la CLI `argocd`, des ressources `Application` versionnées dans Git
- Prérequis — un cluster Kubernetes compatible (la 3.5 prend en charge 1.33 à 1.36) ; en haute disponibilité, au moins 3 nœuds. La synchronisation automatique, le prune et le self-heal sont **désactivés par défaut** : à activer application par application
- Exécution — dans le cluster, plusieurs composants ; le contrôleur se partage par sharding, avec 20 processeurs de statut et 10 d'opérations par défaut, et 50 et 25 conseillés pour 1 000 applications. Aucun chiffre de CPU ou de RAM par composant n'est publié
- Coût — gratuit sous Apache-2.0 ; le coût est l'exploitation des composants et la discipline du dépôt de configuration

## Limites à connaître

- **Des failles graves récentes autour du calcul de différences.** Avis GHSA-3v3m-wc6v-x4x3 (critique, 2026-05-01) : extraction de Secrets Kubernetes par le `ServerSideDiff` ; GHSA-rg3g-4rw9-gqrp (modérée, 2026-05-13) : autre fuite de Secrets par le même mécanisme ; GHSA-h98r-wv3h-fr38 (haute, 2026-05-13) : XSS stocké permettant à un développeur de devenir administrateur. Les numéros de versions corrigées n'ont été relevés que dans des relais tiers (branches 3.2, 3.3 et 3.4) : à lire dans l'avis avant de mettre à jour.
- **Un plugin de secrets peut ruiner la protection.** La doc met en garde contre la génération de secrets dans les manifestes (`argocd-vault-plugin`) : Argo CD conserve les manifestes générés en clair dans son Redis.
- **Ce qu'il ne remplace pas.** Il déploie, il ne construit pas d'image et ne lance pas de tests : la CI reste à part.

## Écosystème

### Alternatives

- *Aucune alternative fichée : Flux (v2.9.5 le 2026-08-31, environ 8 400 étoiles, Apache-2.0, CNCF diplômé le 2022-11-30) est l'autre contrôleur GitOps de référence, décrit comme une solution de livraison continue pour Kubernetes construite sur le GitOps Toolkit ; il n'a pas de fiche.*

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — le seul environnement où il sert
- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé). — l'une des sources de manifestes qu'il sait rendre
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la CI qui construit l'image et met à jour le dépôt de configuration
- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — la documentation d'Argo CD donne la configuration pour exposer le serveur derrière lui : TLS terminé au proxy, `--insecure` côté Argo CD.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — la documentation d'Argo CD décrit le F5 NGINX Ingress Controller pour exposer le serveur.

## Ressources

- Documentation — https://argo-cd.readthedocs.io/
- Dépôt — https://github.com/argoproj/argo-cd
- Documentation — architecture : https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/
- Documentation — gestion des secrets : https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/
- Documentation — haute disponibilité : https://argo-cd.readthedocs.io/en/stable/operator-manual/high_availability/
- Documentation — les principes d'OpenGitOps : https://opengitops.dev/
- Article — avis de sécurité du projet : https://github.com/argoproj/argo-cd/security/advisories

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Conteneurs & orchestration]] — le sous-domaine des orchestrateurs qu'il pilote
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
