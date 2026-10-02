---
role: notion
nom: Du Compose à Kubernetes — quand changer d'échelle
alias: [compose vers kubernetes, quand passer à kubernetes, migrer de compose à k8s, gitops]
categorie: devops/conteneur
domaines: [mlops, infra-ops]
tags: [container, kubernetes, gitops, ci-cd]
---

# Du Compose à Kubernetes — quand changer d'échelle

## Aperçu

- Passer d'une pile décrite dans un `compose.yaml` sur une machine à un cluster Kubernetes n'est pas une montée en gamme du même outil : c'est un **changement de métier**. Compose lance des conteneurs ; Kubernetes maintient un état voulu sur un parc de machines, et demande à quelqu'un de le faire vivre.
- La question utile n'est pas « Kubernetes est-il meilleur ? » mais « quel besoin précis Compose ne couvre-t-il plus, et qui opère le remède ? ». Entre les deux, des paliers existent, et [[k3s]] en est le plus court.

## Concepts clés

### Ce que Compose ne fait pas

- **Une seule machine.** La documentation de [[Docker Compose]] présente comme la voie la plus simple d'exécuter l'application sur un serveur unique, et renvoie vers Swarm ou vers un hôte distant (`DOCKER_HOST`) pour aller plus loin. Aucun mécanisme ne replace un service sur une autre machine quand la première tombe.
- **Une reprise limitée au `restart:`.** Les politiques `no`, `on-failure`, `always`, `unless-stopped` relancent un conteneur ; la politique ne s'active qu'après dix secondes d'exécution réussie. La page consultée ne dit rien d'un redémarrage sur un `healthcheck` en échec : c'est une absence de mention, pas une limite écrite.
- **Pas de mise à l'échelle selon la charge, pas de déploiement progressif garanti.** Ce dernier point est une déduction du périmètre mono-hôte : la documentation officielle ne contient pas d'avertissement explicite. Elle ne précise pas non plus quelles clés de la section `deploy:` sont honorées hors Swarm.
- **Ce que Compose fait bien, et qu'il faut lui reconnaître** : décrire une pile en un fichier versionné, attendre qu'un service soit sain avant d'en démarrer un autre (`depends_on` avec `condition: service_healthy`, `up --wait`), réserver un GPU, itérer en développement avec `watch`.

### Ce qu'apportent k3s et Kubernetes

- **La liste officielle de [[Kubernetes]]** : découverte de services et équilibrage de charge, orchestration du stockage, déploiements et retours arrière automatisés, placement automatique, auto-réparation, gestion des secrets et de la configuration, mise à l'échelle horizontale.
- **Ce qu'il n'est pas**, selon la même page : ni plateforme de build ni de CI/CD, ni middleware, ni base de données, et il n'impose ni journalisation, ni supervision, ni alerte. Ces choix restent à faire.
- **[[k3s]] est le même Kubernetes, avec les choix faits** : un binaire, un réseau, un ingress, un stockage local et une base de cluster livrés, 2 cœurs et 2 Go de RAM pour un serveur, un mode hors ligne documenté. L'API est la même : ce qu'on y écrit se déplace ensuite vers un cluster complet.
- **La sortie de Compose vers un cluster** passe par Kompose (Apache-2.0, dernière version relevée v1.38.0 en janvier 2026, dont l'éditeur reconnaît que la conversion n'est « pas toujours un pour un ») ou par Compose Bridge (génère des manifestes Kubernetes et une superposition Kustomize ; licence et version non trouvées). Ni l'un ni l'autre ne dispense de relire le résultat.

### Ce qu'ils coûtent

- **Du temps, plus que de l'argent.** La licence est Apache-2.0 des deux côtés. Le coût est l'exploitation : trois versions par an, environ **14 mois** de correctifs (12 mois plus 2 de maintenance), une politique de compatibilité qui interdit de sauter une version mineure — soit une ou deux montées séquentielles par an.
- **La haute disponibilité a un plancher.** Kubernetes : au moins 3 nœuds de plan de contrôle et un équilibreur de charge devant l'API. k3s : au moins 3 serveurs avec etcd embarqué, ou 2 avec une base externe ; le stockage par défaut, SQLite, ne sert qu'un serveur.
- **Ce qu'on ajoute soi-même en on-prem.** Sur Kubernetes nu : un réseau (CNI), un ingress — **Ingress NGINX a cessé toute maintenance en mars 2026**, la voie recommandée est Gateway API —, du stockage, un équilibreur de charge sans cloud (MetalLB), la supervision. k3s en livre une partie, ce qui la rend moins souple.
- **Ce que disent les enquêtes.** Selon l'enquête annuelle 2025 de la CNCF (publiée le 2026-01-20), 82 % des **utilisateurs de conteneurs** font tourner Kubernetes en production, contre 66 % en 2023 : la base est celle de gens qui ont déjà des conteneurs, pas celle de toutes les organisations. Défis cités : changements culturels avec l'équipe de développement 47 %, manque de formation 36 %, sécurité 36 %, complexité 34 % — la complexité n'arrive qu'en quatrième position de cette liste ; la taille de l'échantillon n'est pas dans le communiqué (la presse annonce 628 répondants).

### Le critère de bascule

Aucune source ne publie un seuil. Ce que les sources disent, en désaccord ou en écho :

- **Un blogueur** (Dwayne Charrington, 2026-01-17 — une opinion, pas une mesure) place Compose suffisant jusqu'à une petite poignée de services, un serveur en dessous de 10 000 requêtes par minute, deux serveurs derrière un équilibreur en dessous de 100 000, et juge Kubernetes défendable vers cinquante services sur vingt serveurs.
- **Un autre billet, plus mince** (dev.to, auteur peu identifié) reste sur Compose si tout tient sur une machine, avec un trafic prévisible et une petite équipe infra, et bascule à partir de huit services déployés indépendamment, de plusieurs équipes ou de SLA contractuels à pénalités.
- **37signals** a bâti Kamal, un outil de déploiement par SSH, et écrit qu'il rend le système indépendant du fournisseur d'une façon que Kubernetes n'avait jamais permise, sans donner de seuil ; **Gitpod** l'a quitté pour des environnements de développement, en écrivant qu'il reste un bon choix pour des charges applicatives.

**Lecture de cette page, à contredire si l'usage l'exige** — pas un seuil publié. Quitter Compose se justifie quand au moins un de ces besoins devient réel, **et** que quelqu'un peut porter le plan de contrôle :

1. **Un service doit survivre à la perte d'une machine sans intervention humaine** (haute disponibilité).
2. **Plusieurs équipes déploient chacune leurs services**, avec des droits et des quotas séparés (RBAC, espaces de noms).
3. **La charge demande de la mise à l'échelle automatique**, ou des GPU à allouer dynamiquement.
4. **Un outil dont on a besoin n'existe que sur Kubernetes** : un serving de modèle comme [[KServe]], un pilotage par [[Argo CD]].

Aucun de ces quatre besoins n'est atteint par le seul fait d'avoir « beaucoup de conteneurs ». Un seul serveur qui redémarre proprement (`restart:`, ou des fichiers Quadlet sous [[Podman]]) couvre déjà bien des cas.

### Le GitOps en une section

- **Idée.** Le dépôt Git est la source de vérité de ce qui doit tourner ; un agent installé dans le cluster tire cet état et le réconcilie en continu, au lieu qu'un pipeline le pousse.
- **Les quatre principes d'OpenGitOps (v1.0.0)**, paraphrasés : l'état voulu est **déclaratif** ; il est **versionné et immuable**, avec son historique complet ; des agents le **tirent automatiquement** depuis la source ; des agents **observent en continu** l'état réel et cherchent à le rétablir.
- **Les outils.** [[Argo CD]] (interface web, SSO, multi-clusters) et Flux (v2.9.5 au 2026-08-31, Apache-2.0, sans fiche ici) sont tous deux diplômés à la CNCF. [[Helm]] est l'une des façons de produire les manifestes ; [[GitHub Actions]] reste la CI qui construit l'image.
- **Les pièges documentés.** Les secrets ne se versionnent pas en clair : Flux le déconseille et propose SOPS, Sealed Secrets ou External Secrets Operator ; Argo CD conseille de séparer le dépôt de configuration du dépôt de code, pour éviter les boucles de CI et garder un historique lisible. Une conférence de 2026 (Koray Oksay, Kubermatic, CfgMgmtCamp Gand, résumé lu seulement) liste parmi les fautes courantes d'ignorer la dérive, de copier une configuration sans l'adapter et d'ignorer les échecs de réconciliation.
- **Ce que le GitOps demande d'abord** : Kubernetes. Sans cluster, l'idée reste bonne mais l'outillage dont il est question ici n'a pas d'objet.

## En pratique

- Rester sur **une machine avec [[Docker Compose]]** tant que le service peut tomber quelques minutes et que la reprise se fait à la main ; ajouter `restart: unless-stopped`, des `healthcheck` et `depends_on` sur l'état sain.
- Pour aller **un peu plus loin sans cluster** : un hôte distant piloté par `DOCKER_HOST`, ou des unités systemd générées par Quadlet avec [[Podman]].
- Passer à **[[k3s]]** avant Kubernetes : un binaire, trois serveurs pour la haute disponibilité, et l'API de Kubernetes pour la suite. Déclarer les applications par charts [[Helm]] dès le premier jour, puis piloter depuis Git avec [[Argo CD]] quand l'équipe compte plus d'une personne.
- Prévoir dès le départ : un calendrier de mises à jour mineures, la sauvegarde d'etcd, un ingress qui ne soit pas Ingress NGINX, et une réponse pour les secrets.
- Vérifier ce que la migration change vraiment : une pile Compose convertie automatiquement se relit ligne à ligne.

## Approches voisines & alternatives

- **Docker Swarm.** Le mode intégré à Docker Engine n'est pas déclaré déprécié ; le projet autonome « Classic Swarm » n'est plus développé. Mirantis a annoncé en juillet 2025 cinq années de support supplémentaires pour son produit, environ jusqu'en 2030 (engagement d'un vendeur). Hors du brain.
- **Kamal** (37signals, MIT, v2.12.0). Déploiement de conteneurs par SSH, avec redémarrages progressifs et un proxy ; impératif, sans réconciliation d'état ; un équilibreur externe est requis en multi-serveurs. Hors du brain.
- **HashiCorp Nomad.** Planificateur de conteneurs, de binaires et de machines virtuelles, sous licence BSL 1.1 dont le titulaire est IBM : le comparatif du dossier dit pourquoi il n'a pas de fiche.
- **Les distributions Kubernetes** autres que k3s : RKE2, Talos Linux, MicroK8s, OKD.
- Pour les modèles : [[KServe]] et [[Seldon Core]] présupposent un cluster ; [[Ray Serve]] et [[BentoML]] se déploient aussi sur une machine seule.
- Voir aussi : [[Reverse proxy et TLS]], [[Traefik]], [[Harbor]], [[Zot]], [[Comparatif - Registres d'images]].
- [[Packaging Python et environnements reproductibles]] — l'image reproductible : verrou, empreinte de l'image de base, réseau fermé.

## Pour aller plus loin

- Docker — Compose en production : https://docs.docker.com/compose/how-tos/production/
- Kubernetes — ce qu'est et n'est pas Kubernetes : https://kubernetes.io/docs/concepts/overview/
- CNCF — enquête annuelle 2025, communiqué du 2026-01-20 : https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
- OpenGitOps — les principes : https://opengitops.dev/
- Charrington — Docker Compose is all you need (opinion) : https://ilikekillnerds.com/2026/01/17/docker-compose-is-all-you-need-and-kubernetes-people-are-in-denial/
- Ona (ex-Gitpod) — We are leaving Kubernetes : https://ona.com/stories/we-are-leaving-kubernetes
- 37signals — Introducing MRSK (Kamal) : https://world.hey.com/dhh/introducing-mrsk-9330a267
- Kompose : https://kompose.io/
- Compose Bridge : https://docs.docker.com/compose/bridge/
