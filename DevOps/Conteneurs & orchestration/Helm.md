---
role: brique
nom: Helm
alias: [helm, helm chart, helm charts]
pitch: "Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé)."
categorie: devops/conteneur
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: []
complements: ["[[Kubernetes]]", "[[k3s]]", "[[Argo CD]]", "[[GitLab CE]]"]
tags: [kubernetes]
url_docs: https://helm.sh/docs/
url_repo: https://github.com/helm/helm
---

# Helm

<!-- AUTO:BANDEAU:START -->
> Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Gestionnaire de paquets pour [[Kubernetes]]. Un **chart** est un ensemble de fichiers qui
décrit des ressources liées : des gabarits (`templates/`, syntaxe de templates Go), des valeurs
par défaut (`values.yaml`), des métadonnées versionnées (`Chart.yaml`). Installer un chart crée
une **release**, une instance nommée que Helm sait mettre à jour et rétablir à une révision
précédente. Les charts se publient dans des dépôts ou dans un registre OCI (`helm push`,
`helm install oci://…`) et se découvrent sur Artifact Hub. Relevé le 2026-09-30 : **Helm 4**
est la version courante (v4.0.0 le 2025-11-12, dernière v4.3.0 le 2026-09-09) ; Helm 3, à sa
dernière version fonctionnelle **v3.22.0** (2026-09-10), ne reçoit plus que des correctifs.
Environ 30 300 étoiles, Apache-2.0, projet CNCF diplômé (graduated) le 2020-05-01.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Installer un logiciel tiers sur un cluster : la plupart publient un chart, avec ses valeurs à surcharger plutôt que des manifestes à éditer | Des manifestes maison, sans paquet à partager : Kustomize (Apache-2.0), intégré à `kubectl` depuis la 1.14, les décline par environnement sans gabarits |
| Déployer la même application sur plusieurs environnements avec des valeurs différentes, et revenir en arrière en une commande | Voir ce qu'une mise à jour va changer avant de l'appliquer : Helm ne le fait pas seul, il faut le plugin `helm diff` (Apache-2.0) |
| Une chaîne GitOps : [[Argo CD]] sait rendre un chart | Des CRD à tenir à jour : le répertoire `crds/` d'un chart n'est jamais réinstallé s'il existe déjà, jamais mis à jour par un `upgrade` ni un `rollback`, jamais supprimé |
| Un registre OCI déjà en place pour les images : les charts s'y rangent aussi | Des secrets versionnés avec les valeurs : Helm ne chiffre rien, il faut un outil à part, comme `helm-secrets` avec SOPS |

## Mise en œuvre

- Installation — binaire `helm` depuis les releases, ou un gestionnaire de paquets
- Point d'entrée — `helm install`, `helm upgrade --install`, `helm rollback` ; `helm template` rend les manifestes sans rien appliquer
- Prérequis — un accès `kubectl` à un cluster ; les charts tiers se lisent avant de s'installer, ils s'exécutent avec les droits du compte qui les installe
- Exécution — depuis un poste ou une CI. Les hooks (neuf types : avant et après installation, mise à jour, suppression, retour arrière, et test) se déclarent par annotation
- Coût — gratuit sous Apache-2.0

## Limites à connaître

- **Deux branches, deux calendriers de fin de vie.** Le README dit que Helm 3 reçoit des correctifs de bogues jusqu'au 2026-07-08 et des correctifs de sécurité jusqu'au 2026-11-11 ; le billet du projet sur la fin de vie de Helm 3 parle de février 2027 pour la sécurité. Les deux sources ne s'accordent pas : à trancher sur la page du projet le jour où la migration se décide.
- **Pas de réconciliation en continu.** Helm applique à la demande. Ce qui a dérivé dans le cluster depuis n'est ni détecté ni corrigé, ce que fait un contrôleur GitOps comme [[Argo CD]].

## Écosystème

### Alternatives

- *Aucune alternative fichée : Kustomize (Apache-2.0, intégré à `kubectl` depuis la 1.14, sans gabarits, par superpositions de correctifs) et Tanka (Jsonnet, Apache-2.0) sont les autres manières de produire des manifestes, aucune n'a de fiche.*

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — la cible des charts
- [[k3s]] — Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem. — un contrôleur Helm y est intégré
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — rend les charts depuis Git
- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes. — son chart officiel, l'une des méthodes d'installation décrites.

## Ressources

- Documentation — https://helm.sh/docs/
- Dépôt — https://github.com/helm/helm
- Documentation — les charts : https://helm.sh/docs/topics/charts/
- Documentation — les hooks : https://helm.sh/docs/topics/charts_hooks/
- Article — Helm 4 est sorti : https://helm.sh/blog/
- Dépôt — le plugin `helm diff` : https://github.com/databus23/helm-diff
- Dépôt — Artifact Hub : https://github.com/artifacthub/hub

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
