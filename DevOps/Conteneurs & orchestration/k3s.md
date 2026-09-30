---
role: brique
nom: k3s
alias: [rancher k3s]
pitch: "Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem."
categorie: devops/conteneur
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Kubernetes]]", "[[Docker Compose]]"]
complements: ["[[Helm]]", "[[Traefik]]"]
tags: [container, kubernetes, self-hosted]
url_docs: https://docs.k3s.io/
url_repo: https://github.com/k3s-io/k3s
---

# k3s

<!-- AUTO:BANDEAU:START -->
> Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Distribution de [[Kubernetes]] emballée dans **un seul binaire** de moins de 100 Mo, maintenue
par SUSE (Rancher), avec des résultats de conformité déposés auprès de la CNCF. C'est la même
API que Kubernetes : `kubectl`, les manifestes et les charts [[Helm]] fonctionnent tels quels.
Ce qui change, c'est ce qu'on n'a pas à choisir : le moteur `containerd`, le réseau Flannel,
CoreDNS, l'ingress **Traefik**, un équilibreur `ServiceLB`, un provisionneur de volumes local
et `metrics-server` sont livrés. Le stockage du cluster est **SQLite** par défaut, ou un etcd
embarqué, ou une base externe (PostgreSQL, MySQL, MariaDB, etcd). Relevé le 2026-09-30 :
**v1.37.0+k3s1** (2026-09-14, alignée sur Kubernetes 1.37.0), environ 34 100 étoiles,
Apache-2.0 ; projet de la CNCF au niveau Sandbox.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un cluster Kubernetes sur quelques machines ou un seul serveur, sans passer une semaine à choisir CNI, ingress et stockage | Un cluster dont chaque brique doit être choisie et validée par une équipe de sécurité : les composants livrés sont réécrits à chaque démarrage et ne se modifient pas, on les désactive (`--disable=traefik`) pour mettre les siens |
| Un site industriel ou un client **déconnecté d'Internet** : trois méthodes air-gap documentées (registre privé, archive d'images, miroir de registre embarqué) | Une haute disponibilité avec le stockage par défaut : SQLite ne sert qu'**un seul** serveur ; deux voies, un etcd embarqué (au moins 3 serveurs) ou une base externe |
| Des machines modestes : 2 cœurs et 2 Go de RAM pour un serveur, 1 cœur et 512 Mo pour un agent | Un besoin de fonctions d'entreprise (isolation multi-locataire poussée, support commercial du plan de contrôle) : c'est l'offre de SUSE, hors de cette fiche |
| Installer et déclarer par fichiers : un manifeste posé dans le répertoire `manifests/` est appliqué tout seul, le contrôleur Helm intégré lit des ressources `HelmChart` | |

## Mise en œuvre

- Installation — `curl -sfL https://get.k3s.io | sh -` sur le serveur ; un agent se joint avec `K3S_URL` et `K3S_TOKEN` ; hors ligne, `INSTALL_K3S_SKIP_DOWNLOAD=true` avec le binaire et les images déposés à la main
- Point d'entrée — `kubectl` avec le fichier `/etc/rancher/k3s/k3s.yaml` ; des manifestes déposés dans `/var/lib/rancher/k3s/server/manifests` ; des ressources `HelmChart`
- Prérequis — un SSD, parce qu'etcd écrit beaucoup ; un nom d'hôte unique par nœud ; en haute disponibilité, `--cluster-init` sur le premier serveur d'un etcd embarqué, un nombre **impair** d'au moins trois serveurs, et une adresse d'enregistrement fixe recommandée. Un plan de contrôle de 2 CPU et 4 Go convient de 0 à 350 agents, 4 CPU et 8 Go jusqu'à 900
- Exécution — sur du Linux ; les mises à jour se font à la main ou avec le `system-upgrade-controller` ; sur un cluster à plusieurs serveurs, les manifestes utilisateur sont à synchroniser à la main entre serveurs
- Coût — gratuit sous Apache-2.0 ; le support commercial passe par SUSE, prix non relevé

## Écosystème

### Alternatives

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — la version complète, sans les choix faits pour soi.
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — ce qu'on quitte pour passer à k3s.

### Compléments

- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé). — un contrôleur Helm est intégré à k3s
- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — c'est l'ingress que k3s livre par défaut.

## Ressources

- Documentation — https://docs.k3s.io/
- Dépôt — https://github.com/k3s-io/k3s
- Documentation — prérequis matériels : https://docs.k3s.io/installation/requirements
- Documentation — installation hors ligne : https://docs.k3s.io/installation/airgap
- Documentation — haute disponibilité avec etcd embarqué : https://docs.k3s.io/datastore/ha-embedded
- Documentation — choix du stockage du cluster : https://docs.k3s.io/datastore

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Orchestration de conteneurs]] — ce qui départage les moteurs, la pile locale et les orchestrateurs du dossier
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
