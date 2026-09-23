---
role: brique
nom: Ansible
alias: [ansible, ansible-core, ansible-playbook]
pitch: "Gestion de configuration sans agent (ansible-core en GPL-3.0-or-later, Python, Red Hat/IBM) : des playbooks YAML exécutés depuis un nœud de contrôle par SSH sur des machines qui n'ont besoin que de Python — idempotent module par module, sans état ni détection de dérive ; l'offre payante est Ansible Automation Platform, pas l'outil."
categorie: devops/infrastructure
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[OpenTofu]]", "[[Docker]]", "[[Kubernetes]]", "[[SOPS]]"]
tags: [infrastructure-as-code, reproducibility]
url_docs: https://docs.ansible.com/
url_repo: https://github.com/ansible/ansible
---

# Ansible

<!-- AUTO:BANDEAU:START -->
> Gestion de configuration sans agent (ansible-core en GPL-3.0-or-later, Python, Red Hat/IBM) : des playbooks YAML exécutés depuis un nœud de contrôle par SSH sur des machines qui n'ont besoin que de Python — idempotent module par module, sans état ni détection de dérive ; l'offre payante est Ansible Automation Platform, pas l'outil.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de **gestion de configuration** : on décrit l'état voulu d'une machine (paquets installés, fichiers, services, utilisateurs) dans des **playbooks** YAML, et Ansible l'applique depuis un **nœud de contrôle**. Les machines gérées n'exécutent **aucun agent** : le contrôleur s'y connecte en SSH (ou WinRM), y pousse de petits programmes Python (les modules), les exécute et les efface. La cible n'a besoin que de Python et d'un compte SSH. Relevé le 2026-10-01 : **ansible-core 2.21.4** (2026-09-08) et paquet communautaire **`ansible` 14.4.0** (2026-09-08), 70 821 étoiles sur `ansible/ansible`, langage Python.

**Trois objets portent le même nom, et la licence n'est pas la même.**

- **`ansible-core`** — le moteur, le langage de playbooks et les modules de base. Licence **GPL-3.0-or-later** (fichier `COPYING` du dépôt, confirmé par PyPI). Par convention, `module_utils` est en BSD-2-Clause pour permettre à des modules tiers de s'en servir.
- **Le paquet `ansible`** — `ansible-core` plus un agrégat de **92 collections** (version 14). Il est déclaré GPL-3.0-or-later, mais les collections ont chacune leur licence : sur les 44 qui la renseignent dans Galaxy, la plupart sont en GPL (2 ou 3), quelques-unes en Apache-2.0, MIT ou BSD-3-Clause ; **48 collections n'ont aucune licence dans leurs métadonnées Galaxy**, il faut lire leur fichier `LICENSE`.
- **Ansible Automation Platform (AAP)** — produit **Red Hat sous abonnement** : contrôleur web, Automation Hub supporté, images d'exécution certifiées, support. Son amont, **AWX** (Apache-2.0, 15 600 étoiles), a un bandeau d'avertissement dans son README : « Releases of this project are now paused », la dernière release annoncée datant du 2 juillet 2024 — le flux des releases porte pourtant un tag 24.6.1 daté du 2025-03-12, les deux sources ne concordent pas. Le dépôt reste actif (dernier commit le 2026-09-30) mais n'est pas une base de production sans réserve.

**Ce qu'une ESN peut faire.** Avec `ansible-core` et le paquet communautaire : l'utiliser chez un client, écrire et livrer ses propres playbooks et rôles, l'exploiter comme outil d'automatisation, sans abonnement. Modifier **et** redistribuer Ansible lui-même, ou un plugin Python chargé dans le processus du contrôleur, engage la GPL (ou la licence de la collection). Aucune page de documentation lue ne dit si un playbook est une œuvre dérivée : la lecture courante est qu'un playbook YAML qui ne fait qu'appeler Ansible reste distinct, mais elle n'est **pas attestée** par la documentation — à faire valider avant une redistribution commerciale. Ce qui est payant : AAP, pas l'outil. Les règles de marque (« Ansible », logos AWX) ne sont pas lues ici.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Configurer des serveurs existants (paquets, fichiers, services) sans rien installer dessus | Créer l'infrastructure elle-même (machines, réseaux, disques) avec un état suivi : [[OpenTofu]] s'y prête mieux |
| Reproduire le même serveur chez plusieurs clients à partir d'un dépôt de playbooks | Détecter la dérive en continu : Ansible n'a pas de fichier d'état, il ne voit que ce qu'un playbook vérifie à l'exécution |
| Un parc de quelques machines à plusieurs centaines, accessible en SSH | Plusieurs milliers de machines avec des temps d'exécution courts : le modèle « poussé depuis un contrôleur » ralentit |
| Un outil que l'ESN peut livrer sans licence | Un client Python ancien ou absent sur les cibles, et aucune possibilité d'y mettre un Python récent |

## Mise en œuvre

- Installation — `pip install ansible-core` (Python 3.12 à 3.14 côté **contrôleur** pour la 2.21 ; Python 3.9 à 3.14 côté **cible**) ou le paquet `ansible` avec les collections. Un contrôleur Windows natif n'est pas supporté, WSL est toléré hors production
- Point d'entrée — un **inventaire** (hôtes et groupes), des **playbooks** YAML, des **rôles** réutilisables, des **collections** (modules, plugins, rôles distribués via Galaxy)
- Prérequis — SSH vers les cibles et Python dessus ; le module `raw` sert aux cibles minimales sans Python ; Windows se pilote par `psrp`, `winrm` ou SSH (depuis la 2.18). Pour les secrets, `ansible-vault` chiffre une variable ou un fichier ; pour un chiffrement versionnable dans Git, la collection `community.sops` (livrée dans le paquet 14) s'appuie sur [[SOPS]] ; voir [[Gestion des secrets]]
- Exécution — un playbook parcourt les hôtes par lots (5 processus parallèles par défaut, stratégie `linear`) ; `--check` simule et `--diff` montre les changements
- Coût — gratuit ; le coût est la maintenance des playbooks et d'un nœud de contrôle

**En réseau fermé** (les mécanismes sont dans la documentation officielle). `ansible-galaxy collection download` récupère des collections et leurs dépendances en archive pour une installation hors ligne ; `ansible-galaxy collection install` les installe depuis des archives locales. Un serveur Galaxy interne est possible avec **galaxy_ng** (greffon Pulp, GPL-2.0). `pip download` puis `pip install --no-index --find-links` pour `ansible-core` et ses dépendances. Les **execution environments** (images de conteneur contenant `ansible-core`, `ansible-runner` et les collections) se construisent avec `ansible-builder` et se lancent avec `ansible-navigator` ; `ansible-builder` exige Podman ou Docker et des images de base de la famille RPM, ce qui gêne un client Debian. Le dépôt de paquets système des cibles (dnf, apt) reste à miroiter à part, hors périmètre d'Ansible.

## Limites à connaître

- **Pas d'état, pas de plan.** `--check` n'est pas un `terraform plan` : un module sans support du mode vérification « ne rapporte rien et ne fait rien », et une tâche qui dépend du résultat d'une tâche précédente ne se simule pas fidèlement.
- **L'idempotence est une propriété des modules, pas du langage.** `command` et `shell` rejouent la commande à chaque exécution, sauf si `creates` ou `removes` est donné (ce qui active aussi le mode vérification).
- **Python sur le contrôleur** : la 2.21 exige 3.12 ou plus, ce qu'une distribution ancienne ne fournit pas. Un Python parallèle, ou un execution environment, règle le problème.
- **Collections de licences hétérogènes** : voir plus haut, vérifier avant de redistribuer le paquet complet.
- **Calendrier court** : trois versions d'`ansible-core` sont maintenues (la 2.21 jusqu'en novembre 2027 d'après endoflife.date), une seule version majeure du paquet `ansible` à la fois. Une installation chez un client se périme en deux ans.
- **Parc important** : aucune mesure officielle relevée ; la lenteur sur un grand parc est connue mais non chiffrée ici.

## Écosystème

### Alternatives

- Aucune alternative déclarée : les concurrents directs n'ont pas de fiche. **SaltStack** (Apache-2.0, Broadcom ; v3008 LTS du 2026-05-27) exige un agent (minion) ou `salt-ssh`. **Puppet** (Perforce) a figé son dépôt public en 2024 (v8.10.0) et distribue ses paquets sous licence commerciale au-delà de 25 nœuds ; son fork communautaire **OpenVox** (Apache-2.0) est actif. **Chef** (Progress) exige une licence pour les installations hors distributions officielles. Tous trois fonctionnent avec un serveur et un agent, là où Ansible n'a ni l'un ni l'autre ; c'est la raison de ne pas leur donner de fiche ici.

### Compléments

- [[OpenTofu]] — Provisionnement d'infrastructure déclaratif avec un état (MPL-2.0, Go, fork de Terraform 1.5 sous la Linux Foundation, CNCF sandbox) : des fichiers HCL, un plan avant chaque changement, des fournisseurs pour VMware, Proxmox, libvirt, Kubernetes ; chiffrement d'état natif, miroir de fournisseurs pour le réseau fermé — Terraform, lui, est sous BUSL depuis 2023. — complément, pas concurrent : OpenTofu crée l'infrastructure et suit son état, Ansible configure ce qu'il a créé.
- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — la collection `community.docker`, livrée dans le paquet, installe le moteur sur un hôte et lance des conteneurs depuis un playbook.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — la collection `kubernetes.core`, livrée dans le paquet, applique des manifestes et des charts sur un cluster.
- [[SOPS]] — Chiffre les valeurs d'un fichier YAML, JSON, ENV ou INI en laissant clés et structure lisibles (MPL-2.0, Go, CNCF Sandbox) — clés age, PGP, KMS cloud ou Transit de Vault ou OpenBao ; le fichier chiffré se versionne dans Git, mais sans serveur : ni audit, ni révocation, ni rotation automatique. — la collection `community.sops`, livrée dans le paquet, lit les fichiers de secrets chiffrés par SOPS.

## Ressources

- Documentation — https://docs.ansible.com/
- Dépôt — https://github.com/ansible/ansible
- Dépôt — https://raw.githubusercontent.com/ansible/ansible/devel/COPYING
- Documentation — installation : https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
- Documentation — calendrier de maintenance : https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html
- Documentation — mode vérification : https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html
- Documentation — installer des collections : https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html
- Documentation — execution environments : https://docs.ansible.com/ansible/latest/getting_started_ee/index.html
- Dépôt — collections du paquet 14 : https://github.com/ansible-community/ansible-build-data
- Dépôt — AWX : https://github.com/ansible/awx

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Infrastructure as code — configuration, provisionnement et idempotence]] — la notion : impératif et déclaratif, configuration et provisionnement, idempotence, dérive, sans agent ou avec agent, réseau fermé.
