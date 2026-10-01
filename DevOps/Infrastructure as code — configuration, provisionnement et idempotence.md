---
role: notion
nom: Infrastructure as code — configuration, provisionnement et idempotence
alias: [Infrastructure as code : configuration, provisionnement et idempotence, infrastructure as code, iac, idempotence, dérive de configuration, provisionnement et configuration]
categorie: devops/infrastructure
domaines: [infra-ops, mlops]
tags: [infrastructure-as-code, reproducibility]
---

# Infrastructure as code — configuration, provisionnement et idempotence

## Aperçu

- Décrire une infrastructure en **fichiers versionnés** plutôt que par des gestes à la main : ce qui est écrit peut être relu, rejoué, comparé et refait chez un autre client. Deux métiers se cachent sous le même nom : **provisionner** (créer les machines, réseaux, disques) et **configurer** (installer et régler ce qui tourne sur une machine).
- Deux outils fichés couvrent ces deux métiers et **se complètent** : [[OpenTofu]] provisionne et suit un état ; [[Ansible]] configure sans agent. Ils ne sont pas concurrents, et aucun comparatif ne les réunit pour cette raison. Ce qui est concurrent est ailleurs : [[Comparatif - Registres d'images]] pour héberger les images.
- Pour le passage d'une machine à un cluster, voir [[Du Compose à Kubernetes — quand changer d'échelle]] : cette page ne le répète pas.

## Concepts clés

### Déclaratif et impératif

- Selon le glossaire d'Ansible, une description **déclarative** est celle de l'état final plutôt que de la suite d'étapes pour y arriver ; l'impératif est la suite d'étapes. Un script shell est impératif.
- **La frontière est moins nette qu'on le dit.** Un playbook Ansible est une liste de tâches **ordonnées**, dont chacune vise un état (« ce paquet est présent ») : déclaratif par tâche, séquentiel dans l'ensemble. OpenTofu décrit un **ensemble de ressources** et en déduit l'ordre ; c'est son plan qui dit ce qui changera.
- Le critère utile n'est pas l'étiquette : c'est de savoir si on peut **rejouer sans craindre** (idempotence) et **voir avant d'appliquer** (plan).

### Provisionnement et configuration

- **Provisionner** : faire exister l'infrastructure — machines virtuelles, réseaux, volumes, objets d'un cluster. L'outil garde un **état** pour savoir ce qu'il a créé ; c'est le métier d'[[OpenTofu]].
- **Configurer** : amener une machine existante à l'état voulu — paquets, fichiers, services, comptes. L'outil se connecte et agit ; c'est le métier d'[[Ansible]].
- La documentation d'OpenTofu l'écrit à sa manière : les *provisioners*, qui lancent des commandes sur la machine qu'on vient de créer, sont déconseillés — elle recommande de faire la configuration pendant la construction d'une image plutôt que pendant le déploiement. La séparation se tient donc par l'outillage : créer d'un côté, configurer de l'autre.
- **Le cas où un seul des deux suffit** : quelques machines déjà installées à configurer, pas de provisionnement ; ou une infrastructure sur un fournisseur dont tout se règle par API, avec des images toutes prêtes.

### Idempotence

- Le glossaire d'Ansible la définit ainsi : le résultat d'une opération faite une fois est exactement le même que celui de la même opération répétée. Rejouer un playbook sur une machine déjà conforme ne change rien.
- **Elle est une propriété de chaque module, pas du langage.** Les modules Ansible qui visent un état (`package`, `file`, `service`) la fournissent ; `command` et `shell` rejouent la commande à chaque fois, sauf si `creates` ou `removes` dit quand ne rien faire. C'est exactement la différence avec un script shell : l'idempotence y est à écrire à la main, à chaque ligne.
- Sans elle, rejouer est dangereux, donc on ne rejoue pas, donc la dérive s'installe.

### État et dérive

- **L'état d'OpenTofu** relie les objets du système distant aux ressources déclarées dans la configuration ; il sert à suivre ce qui a été créé et accélère les gros déploiements. Avant chaque opération, OpenTofu rafraîchit l'état contre la réalité, ce qui révèle ce qu'on a changé à la main ailleurs. Le verrouillage d'état empêche deux exécutions simultanées. Voir [[OpenTofu]] pour les backends et le chiffrement.
- **Ansible n'a pas d'état** : il ne sait que ce que le playbook vérifie à l'exécution. `--check` simule et `--diff` montre les écarts, mais ce n'est pas un plan (cf. la fiche [[Ansible]]).
- **La dérive** est l'écart entre ce qui est décrit et ce qui existe, né d'un changement manuel. Elle se détecte en rejouant (Ansible, OpenTofu) ou en continu par un agent qui réconcilie ([[Argo CD]] sur un cluster). Elle se **supprime** en interdisant la modification à la main, pas en la détectant.

### Sans agent et avec agent

- **Sans agent** : un contrôleur se connecte aux machines et agit, rien n'est installé dessus. La documentation d'Ansible demande seulement Python et un compte SSH sur la cible ; Salt propose aussi `salt-ssh`, qui exécute sans minion. Avantage sur site : rien à installer ni à mettre à jour chez le client avant le premier jour. Prix : le contrôleur doit voir toutes les machines, et la configuration n'est appliquée que quand on la lance.
- **Avec agent** : un démon sur chaque machine tire sa configuration d'un serveur et la réapplique en continu (usage courant de Puppet, Chef, Salt avec minion — voir la situation de chacun dans la fiche [[Ansible]]). Avantage : la dérive se corrige seule. Prix : un serveur et des agents à exploiter, et des paquets qui, chez certains éditeurs, sont passés sous licence commerciale.
- Sur du matériel client où on n'a qu'un accès temporaire, **sans agent** est le choix qui demande le moins.

### Serveur modifié et image immuable

- Un serveur qu'on modifie au fil du temps finit par ne ressembler à aucun autre : un serveur « flocon de neige ». Un serveur **immuable** n'est jamais modifié après son déploiement : on le **remplace** par un nouveau construit depuis une image testée. Martin Fowler publie cette idée le 13 juin 2013, sous la plume de Kief Morris : tout changement se fait dans l'image de base, qui est testée puis déployée.
- Un conteneur est l'image immuable la plus répandue ([[Docker]], [[Podman]]) ; le registre qui range ces images est [[Harbor]] ou [[Zot]]. Une image de machine virtuelle se construit avec un outil comme Packer (sous BUSL, voir la fiche [[OpenTofu]]).
- **Sur le matériel d'un client, l'immuable a ses limites** : on ne remplace pas un serveur physique comme une machine virtuelle. Dans ce cas, la configuration rejouable ([[Ansible]]) tient la place de l'image. Aucune source sérieuse sur cette frontière n'a été trouvée : c'est un constat de terrain, pas une règle sourcée.

### Les secrets dans le code

- Un dépôt d'infrastructure contient des mots de passe, des clés, des certificats, ou du moins leur emplacement. La **gestion** (coffre, chiffrement versionné, rotation) est dans [[Gestion des secrets]], avec [[SOPS]] et [[OpenBao]] ; cette page ne la répète pas.
- Ce qui est propre à l'IaC : un secret créé par OpenTofu **entre dans le fichier d'état**, qu'il faut donc chiffrer ou protéger ; Ansible lit ses secrets par `ansible-vault` ou par la collection `community.sops`. Les fiches [[OpenTofu]] et [[Ansible]] donnent les mécanismes.

### En réseau fermé

- **Les dépendances sont à miroiter** : les collections Ansible (`ansible-galaxy collection download`, serveur Galaxy interne), les fournisseurs d'OpenTofu (`tofu providers mirror`, bloc `provider_installation`), les paquets pip de l'outil lui-même, les images de conteneur (registre interne : [[Harbor]] ou [[Zot]]) et, à part, les dépôts de paquets système des cibles.
- **Le contrôleur d'Ansible a besoin de Python récent** ; un *execution environment* (une image de conteneur qui embarque l'outil et ses collections) règle le cas d'une distribution cliente ancienne.
- **Le fichier de verrou** d'OpenTofu fige les empreintes des fournisseurs : à préparer pour chaque plateforme avant de couper la ligne.
- Les règles d'un pipeline sur site, où ces outils s'exécutent souvent, sont dans [[Pipelines CI-CD on-prem — runners, secrets et artefacts]].

## En pratique

- **Quand un script shell suffit** : une machine, une seule fois, sans la refaire ; ou un geste qui n'a rien à voir avec l'état (une sauvegarde, un redémarrage). **Quand il ne suffit plus** : dès qu'on veut le rejouer sans risque, sur plusieurs machines, ou le confier à quelqu'un d'autre — c'est-à-dire dès que l'idempotence devient nécessaire. Aucune source n'a été trouvée qui chiffre ce seuil ; le critère donné ici est un critère d'usage.
- **Un découpage simple pour un client on-prem** : OpenTofu pour créer les machines virtuelles si un hyperviseur a une API (vSphere, Proxmox, libvirt) ; Ansible pour les configurer ; un registre interne pour les images ; les secrets chiffrés dans le dépôt par SOPS ; le tout rejouable depuis un poste ou un runner sur site.
- **Sans hyperviseur ni API** (serveurs physiques installés à la main) : OpenTofu n'a rien à piloter ; Ansible seul suffit.
- **Pièges** : un playbook qui marche une fois mais pas deux (un `command` sans `creates`) ; un état OpenTofu perdu ou non verrouillé ; une modification manuelle « juste pour tester » qui devient la configuration réelle ; des collections ou des fournisseurs téléchargés au premier jour, jamais miroités ; un secret dans l'état en clair.

## Approches voisines & alternatives

- **Pulumi** décrit l'infrastructure dans un langage général (TypeScript, Python, Go) ; sans fiche, la raison est dans [[OpenTofu]].
- **Terraform** : même modèle qu'OpenTofu, sous licence BUSL ; voir la fiche [[OpenTofu]] pour ce que l'ESN peut en faire.
- **Puppet, Chef, SaltStack** : gestion de configuration avec agent ; la fiche [[Ansible]] dit pourquoi ils n'ont pas de fiche.
- **Le GitOps** déplace la réconciliation de l'infrastructure vers un agent qui tire depuis Git : [[Argo CD]] pour un cluster.
- **Un orchestrateur** ([[Kubernetes]], [[k3s]]) fait de la configuration en continu pour les conteneurs : voir [[Du Compose à Kubernetes — quand changer d'échelle]].

## Pour aller plus loin

- Documentation — glossaire d'Ansible (idempotence, déclaratif) : https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html
- Documentation — provisioners d'OpenTofu, dernier recours : https://opentofu.org/docs/language/resources/provisioners/syntax/
- Documentation — état d'OpenTofu : https://opentofu.org/docs/language/state/
- Documentation — Salt SSH : https://docs.saltproject.io/en/latest/topics/ssh/index.html
- Article — Kief Morris, « ImmutableServer », martinfowler.com, 13 juin 2013 : https://martinfowler.com/bliki/ImmutableServer.html
