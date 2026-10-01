---
role: brique
nom: OpenTofu
alias: [opentofu, tofu, terraform open source, fork de terraform]
pitch: "Provisionnement d'infrastructure déclaratif avec un état (MPL-2.0, Go, fork de Terraform 1.5 sous la Linux Foundation, CNCF sandbox) : des fichiers HCL, un plan avant chaque changement, des fournisseurs pour VMware, Proxmox, libvirt, Kubernetes ; chiffrement d'état natif, miroir de fournisseurs pour le réseau fermé — Terraform, lui, est sous BUSL depuis 2023."
categorie: devops/infrastructure
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: []
complements: ["[[Ansible]]", "[[OpenBao]]", "[[Kubernetes]]", "[[Harbor]]"]
tags: [infrastructure-as-code, reproducibility]
url_docs: https://opentofu.org/docs/
url_repo: https://github.com/opentofu/opentofu
---

# OpenTofu

<!-- AUTO:BANDEAU:START -->
> Provisionnement d'infrastructure déclaratif avec un état (MPL-2.0, Go, fork de Terraform 1.5 sous la Linux Foundation, CNCF sandbox) : des fichiers HCL, un plan avant chaque changement, des fournisseurs pour VMware, Proxmox, libvirt, Kubernetes ; chiffrement d'état natif, miroir de fournisseurs pour le réseau fermé — Terraform, lui, est sous BUSL depuis 2023.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de **provisionnement** : on décrit dans des fichiers HCL les ressources voulues (machines virtuelles, réseaux, disques, objets d'un cluster), `tofu plan` calcule l'écart avec la réalité et `tofu apply` l'applique. Un **fichier d'état** retient ce qui existe, ce qui permet de modifier ou de détruire proprement. Les **fournisseurs** (providers) sont des greffons qui parlent à chaque système. Relevé le 2026-10-01 : **v1.13.0** (2026-09-30), 30 337 étoiles, langage Go, licence **MPL-2.0** (fichier `LICENSE` du dépôt).

**Terraform et OpenTofu : la situation.** Le 10 août 2023, HashiCorp a fait passer Terraform (versions 1.6.0 et suivantes) de la MPL-2.0 à la **Business Source License 1.1**. Un manifeste a demandé le retour à une licence libre ; sans réponse, le fork est parti de Terraform 1.5.x, la dernière version sous MPL, et la Linux Foundation l'a annoncé le 20 septembre 2023 sous le nom OpenTofu. Le projet a été accepté à la **CNCF le 23 avril 2025, au niveau sandbox** (pas incubating). IBM a racheté HashiCorp (opération finalisée le 27 février 2025) : le fichier de licence de Terraform nomme aujourd'hui IBM comme concédant. Terraform n'a pas de fiche ici.

**Ce que la BUSL de Terraform permet à une ESN** (texte de l'*Additional Use Grant*, relu le 2026-10-01) : l'usage en production est autorisé, sauf à offrir Terraform à des tiers « sur une base hébergée ou embarquée » pour concurrencer les versions payantes d'IBM. Un produit non payant n'est jamais concurrent ; l'usage interne à une organisation et à ses affiliés non plus. Utiliser Terraform chez un client pour déployer son infrastructure est donc permis ; l'inclure ou le revendre dans une offre payante qui recouvre HCP Terraform ou Terraform Enterprise demande une licence commerciale. Chaque version bascule en MPL-2.0 quatre ans après sa première distribution publique. Les fournisseurs de HashiCorp restent en MPL-2.0. **OpenTofu, en MPL-2.0, n'a aucune de ces restrictions** : une ESN peut l'utiliser, le redistribuer et le proposer comme service. **Packer** (construction d'images de machines) a suivi Terraform : BUSL depuis la 1.10, dernière version MPL la 1.9.5, aucun fork établi trouvé ; pas de fiche.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Décrire une infrastructure (machines, réseaux, ressources de cluster) avec un plan avant chaque changement | Seulement configurer des machines qui existent déjà : [[Ansible]] suffit |
| Un client qui interdit une licence non libre : la MPL-2.0 est sans condition | Une équipe qui a déjà tout en Terraform et n'a pas de contrainte de licence : la bascule se justifie surtout par la licence |
| Des fournisseurs pour l'on-prem : vSphere, Proxmox, libvirt, OpenStack, Kubernetes | Peu de ressources, une seule fois : un script shell suffit |
| Un site isolé : un miroir de fournisseurs fonctionne sans Internet | Un besoin de langage général (boucles, classes, tests unitaires) plutôt que HCL : Pulumi vise ce cas, sans fiche ici |

## Mise en œuvre

- Installation — un binaire ; `tofu init` télécharge les fournisseurs, `tofu plan` puis `tofu apply`
- Point d'entrée — des fichiers `.tf` : blocs `provider`, `resource`, `variable`, `output`, `module` ; un fichier de verrou `.terraform.lock.hcl` fige les versions et les empreintes des fournisseurs. `registry.opentofu.org` est le registre par défaut : les fournisseurs y sont ajoutés par demande validée par l'équipe et les versions publiées sont immuables. Relevé le 2026-10-01 : `hashicorp/kubernetes`, `hashicorp/helm`, `hashicorp/vault`, `vmware/vsphere`, `kreuzwerker/docker`, `goharbor/harbor`, `bpg/proxmox`, `dmacvicar/libvirt` et `terraform-provider-openstack/openstack` y figurent
- Prérequis — un **backend d'état** : `local` (par défaut), `s3` (AWS ou compatible, la documentation cite MinIO), `http`, `pg`, `kubernetes`, `consul`, `azurerm`, `gcs` ; l'état est en JSON. Le chiffrement de l'état et des plans est natif (AES-GCM), avec des fournisseurs de clé : PBKDF2 (phrase secrète), AWS KMS, GCP KMS, Azure Key Vault, **OpenBao** (moteur Transit), OVHcloud KMS, ou une commande externe ; voir [[OpenBao]] et [[Gestion des secrets]]
- Exécution — `tofu plan` calcule l'écart entre le code et la réalité, `tofu apply` l'applique et met l'état à jour, `tofu destroy` détruit ce que l'état décrit
- Coût — gratuit ; le coût est la sauvegarde et le verrouillage de l'état, et la veille sur les fournisseurs

**En réseau fermé** (documentation officielle). `tofu providers mirror -platform=linux_amd64 <dossier>` télécharge les fournisseurs du projet et génère l'index d'un miroir réseau ; relancée, la commande complète le miroir existant. Le fichier de configuration du CLI (`.tofurc`) déclare un bloc `provider_installation` avec `filesystem_mirror` (dossier local), `network_mirror` (HTTPS interne) ou, depuis la 1.10, `oci_mirror` (registre OCI interne) ; la documentation recommande de n'activer que le miroir et d'exclure `direct`. `tofu providers lock -platform=…` prépare le fichier de verrou pour chaque plateforme cible ; depuis la 1.12, `tofu init` y inscrit les empreintes de toutes les plateformes. Les modules se copient en local ou se référencent par chemin relatif.

## Limites à connaître

- **L'état est la pièce critique.** Perdu, il faut réimporter chaque ressource ; partagé sans verrou, il se corrompt. Prévoir un backend avec verrou (S3 compatible avec verrou natif depuis la 1.10, ou PostgreSQL) et des sauvegardes.
- **Les secrets entrent dans l'état.** Un mot de passe de base créé par un fournisseur y est écrit en clair : c'est la raison du chiffrement natif, qui ne remplace pas un coffre.
- **La compatibilité avec Terraform est de fait, pas contractuelle.** Le fork part de la 1.5 ; les deux outils ont divergé depuis (chiffrement d'état, `for_each` sur les fournisseurs, registres OCI côté OpenTofu ; fonctionnalités propres à Terraform de l'autre côté). Les fournisseurs communautaires restent partagés, mais la documentation lue ne détaille pas la compatibilité du format d'état.
- **Les fournisseurs on-prem sont communautaires et inégaux.** Au 2026-10-01, `Telmate/proxmox` est toujours en candidate de version (v3.0.2-rc10) et `terraform-provider-openstack` n'a pas de version depuis novembre 2025. Vérifier la dernière version avant de s'engager.
- **Gouvernance jeune** : accepté à la CNCF en sandbox en 2025, avec un soutien financier d'entreprises ; le projet n'a pas dix ans de recul.
- **Date d'introduction du chiffrement** : la page de documentation l'étiquette « 1.13.0 and later » alors que les notes de la 1.7 l'annoncent ; l'étiquette semble celle de la page, pas de la fonction.

## Écosystème

### Alternatives

- Aucune alternative déclarée : **Terraform** est sous BUSL (voir *Définition*), **Pulumi** (Apache-2.0, 25 750 étoiles, v3.266.0 du 2026-09-30) décrit l'infrastructure en TypeScript, Python, Go, C#, Java ou YAML. Son état est par défaut dans **Pulumi Cloud** (service commercial) ; un état auto-hébergé existe (`pulumi login file://…`, S3, Azure Blob, GCS, PostgreSQL), mais les fournisseurs se téléchargent depuis GitHub et `get.pulumi.com` et les SDK de langage depuis PyPI ou npm : le réseau fermé demande plus de miroirs qu'avec OpenTofu, et l'hébergement de la plateforme (Pulumi Self-Hosted) est une fonction de l'offre Enterprise. Écarté ici par le plafond de quatre briques du lot, pas pour un défaut rédhibitoire.

### Compléments

- [[Ansible]] — Gestion de configuration sans agent (ansible-core en GPL-3.0-or-later, Python, Red Hat/IBM) : des playbooks YAML exécutés depuis un nœud de contrôle par SSH sur des machines qui n'ont besoin que de Python — idempotent module par module, sans état ni détection de dérive ; l'offre payante est Ansible Automation Platform, pas l'outil. — complément, pas concurrent : OpenTofu crée l'infrastructure et suit son état, Ansible configure ce qu'il a créé.
- [[OpenBao]] — Serveur de secrets sous MPL-2.0, fork communautaire de HashiCorp Vault (LF Edge puis OpenSSF, Go) : coffre clé-valeur, secrets dynamiques de bases de données, PKI, Transit, scellement Shamir ou auto-unseal, Raft intégré — sans fonction gardée en payant, mais qui diverge volontairement de Vault et ne corrige que sa dernière version. — fournisseur de clé du chiffrement natif de l'état (moteur Transit) ; le fournisseur `hashicorp/vault` sert de client pour gérer ses ressources.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — les fournisseurs `hashicorp/kubernetes` et `hashicorp/helm` créent des ressources d'un cluster, mais l'état dérive vite si un outil GitOps agit aussi dessus.
- [[Harbor]] — Registre d'images OCI complet (Apache-2.0, Go, CNCF gradué) : projets avec droits et quotas, SSO LDAP et OIDC, réplication et proxy cache vers d'autres registres, scan Trivy, signatures Cosign et Notation — lourd à exploiter (PostgreSQL, un cache Redis ou Valkey, 4 Go de RAM au minimum, installateur hors ligne de 700 Mo). — le fournisseur `goharbor/harbor` d'OpenTofu décrit projets, utilisateurs et réplications.

## Ressources

- Documentation — https://opentofu.org/docs/
- Dépôt — https://github.com/opentofu/opentofu
- Dépôt — https://raw.githubusercontent.com/opentofu/opentofu/main/LICENSE
- Documentation — miroir de fournisseurs : https://opentofu.org/docs/cli/commands/providers/mirror/
- Documentation — fichier de configuration du CLI : https://opentofu.org/docs/cli/config/config-file/
- Documentation — chiffrement de l'état : https://opentofu.org/docs/language/state/encryption/
- Documentation — CNCF : https://www.cncf.io/projects/opentofu/
- Documentation — Linux Foundation : https://www.linuxfoundation.org/press/announcing-opentofu
- Dépôt — Terraform : https://raw.githubusercontent.com/hashicorp/terraform/main/LICENSE
- Article — HashiCorp passe à la BSL : https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license
- Documentation — rachat par IBM : https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform
- Documentation — Pulumi, état et backends : https://www.pulumi.com/docs/iac/concepts/state-and-backends/

## Voir aussi

- [[DevOps]] — le hub du domaine
