---
role: brique
nom: OpenShell
alias: [openshell, NVIDIA OpenShell, NVIDIA/OpenShell, OpenShell sandbox]
pitch: "Runtime de bac à sable pour agents d'IA de NVIDIA (Apache-2.0) — une politique déclarative en YAML appliquée hors de l'agent : Landlock et seccomp pour les fichiers et les appels système, un proxy qui filtre le réseau par hôte, programme, méthode et chemin et ajoute les identifiants à la place de l'agent ; jeune (0.1.4 le 2026-10-13), à passer en mode enforce."
categorie: security/ia
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: Rust
scaling: single-node
alternatives: ["[[sandbox-runtime]]", "[[E2B]]"]
complements: []
tags: [ai-security, sandbox, agents, self-hosted]
url_docs: https://docs.nvidia.com/openshell/latest/index.html
url_repo: https://github.com/NVIDIA/OpenShell
---

# OpenShell

<!-- AUTO:BANDEAU:START -->
> Runtime de bac à sable pour agents d'IA de NVIDIA (Apache-2.0) — une politique déclarative en YAML appliquée hors de l'agent : Landlock et seccomp pour les fichiers et les appels système, un proxy qui filtre le réseau par hôte, programme, méthode et chemin et ajoute les identifiants à la place de l'agent ; jeune (0.1.4 le 2026-10-13), à passer en mode enforce.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Runtime de bac à sable **à héberger soi-même** pour des agents d'IA : on déclare dans une politique YAML ce que chaque agent peut toucher (fichiers, appels système, destinations réseau, identifiants), et OpenShell l'applique **hors du processus de l'agent**. Trois composants : un **gateway** (plan de contrôle : cycle de vie des sandboxes, distribution des politiques), un **superviseur** (côté de confiance : vérifie chaque connexion, résout le DNS, ajoute les identifiants réels) et la **sandbox** (Landlock, seccomp, identité sans privilèges), qui partage la frontière avec l'agent et ne prend aucune décision de politique. Principe : [[Garde-fous hors modèle]] ; mécanismes : [[Isolation par politique déclarative]].

Relevé le 2026-10-20 : dépôt `NVIDIA/OpenShell` créé le 2026-02-24, poussé le jour même, 16,7 k étoiles, 554 tickets et demandes de fusion ouverts (compteur de l'API GitHub) ; **v0.1.4** publiée le 2026-10-13 (0.1.0 le 2026-09-25) ; licence **Apache-2.0** lue dans le fichier `LICENSE`. Jeune, avec une cadence de versions stables d'environ une par semaine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent doit lire des fichiers, installer des paquets et appeler des API, avec des **droits déclarés** plutôt que donnés en bloc | Le besoin est d'isoler du **code hostile multi-locataire** à grande échelle : une microVM managée est plus étanche → [[E2B]] |
| Les **secrets ne doivent jamais entrer dans le processus** de l'agent : le superviseur ajoute la vraie clé aux seules requêtes vers un endpoint approuvé | La machine n'est pas sous Linux 6.2 ou plus avec Landlock actif : le socle obligatoire refuse de démarrer |
| Une règle réseau doit porter sur la **méthode et le chemin** (un `GET` oui, un `POST` non) : inspection REST, WebSocket ou GraphQL | Un simple confinement de commande sans gateway ni Kubernetes suffit → [[sandbox-runtime]] |
| Des politiques **versionnées**, relues comme un changement de sécurité, avec un conseiller qui propose et un vérificateur formel qui compare | Une assurance de résistance à un attaquant qui s'adapte : aucune mesure indépendante n'a été trouvée |
| Changer de harnais d'agent sans changer la gouvernance : OpenShell est un runtime, pas un harnais | Un durcissement par défaut : plusieurs réglages sont **permissifs** tant qu'on ne les change pas (voir *Limites*) |

## Mise en œuvre

- Installation — `curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh` installe le CLI et un gateway local ; paquets Debian, RPM, Homebrew et snap ; SDK `uv add openshell` (Python), `@nvidia/openshell-sdk` (TypeScript), Go et Rust
- Point d'entrée — `openshell sandbox create --name demo` crée un bac à sable avec une image minimale Ubuntu 24.04 sans agent ; la politique s'applique à la création (`--policy`) ou à chaud (`openshell policy update`, `openshell policy set`) pour le réseau
- Prérequis — Linux Debian ou Ubuntu (x86_64, aarch64) ou macOS sur Apple Silicon avec Docker Desktop ; Windows avec WSL 2 est expérimental ; Docker Engine 28 ou plus, Podman 5, Kubernetes 1.29 avec Helm, ou une machine avec virtualisation (microVM, libkrun) ; **Landlock ABI 3 au minimum, soit un noyau Linux 6.2 ou plus**, sinon la sandbox ne démarre pas
- Exécution — auto-hébergé : gateway local, conteneur ou chart Helm ; le README du chart Helm annonce que le chemin Kubernetes est **expérimental** et sujet à changements incompatibles, alors que la matrice de support le déclare supporté
- Coût — gratuit, Apache-2.0 ; le gateway envoie une **télémétrie anonyme** (catégories opérationnelles et compteurs, ni noms, ni chemins, ni invites, ni identifiants) qu'on désactive par `OPENSHELL_TELEMETRY_ENABLED=false` ; point à régler pour un site isolé

## Limites à connaître

- **Plusieurs défauts sont permissifs.** L'inspection de requêtes (`enforcement`) est en mode **`audit`** : la requête qui viole la règle est autorisée et seulement journalisée, l'agent peut encore écrire ou supprimer sur une API que la règle aurait refusée ; il faut passer en `enforce`. La politique de fichiers supplémentaire est en `best_effort` (elle peut ignorer des chemins introuvables, avec une alerte de gravité haute) ; `hard_requirement` refuse de démarrer. Le Policy Advisor est **désactivé** par défaut ; son approbation automatique est optionnelle. Un endpoint en `tls: skip` n'a ni substitution d'identifiants ni inspection.
- **Six CVE corrigées en v0.0.34.** Le bulletin NVIDIA du 2026-08-25 (CVE-2026-65093, 65083, 65092, 65091, 65086, 65085) couvre les versions 0 à 0.0.33 : évasion de sandbox (CVSS 9,9), API de provisionnement (9,9), contournement de la politique REST de niveau 7 par traversée de chemin (8,5), injection de commande par un gateway malveillant (8,8), et deux de gravité moyenne. Mettre à jour au-delà de la v0.0.34 ; l'évasion rappelle qu'**aucune sandbox n'est une frontière absolue**.
- **Aucune mesure indépendante.** Pas de taux de blocage, pas de test d'évasion publié, pas de coût de performance chiffré dans la documentation ; le communiqué parle d'un surcoût « minimal » sans nombre. Ce que NVIDIA dit de la plateforme qui entoure OpenShell est auto-rapporté.
- **Périmètre.** OpenShell est la partie logicielle disponible de l'« Open Agent Safety Platform » annoncée le 2026-09-28. Le composant matériel (Sentry, sur carte BlueField-4) n'a pas de disponibilité publique établie : il n'est pas fiché ici.
- **Un contrôle externe ne règle pas tout** : une politique trop large, la fuite par un outil autorisé ([[Excessive agency et lethal trifecta]]) et l'erreur de jugement d'un agent qui respecte les règles restent à découvert.

## Écosystème

### Alternatives

- [[sandbox-runtime]] — Outil en ligne de commande et bibliothèque de bac à sable léger d'Anthropic (Apache-2.0, préversion bêta) — restrictions de fichiers et de réseau au niveau du système d'exploitation, sans conteneur : Seatbelt sur macOS, bubblewrap sur Linux, proxy HTTP et SOCKS5 à liste de domaines ; Windows en alpha. — une enveloppe de processus sans gateway ni politique inspectant les requêtes, plus légère à poser, moins fine sur le réseau.
- [[E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform. — une microVM à noyau dédié, créée à la demande par SDK, au lieu d'un processus confiné par une politique.

## Ressources

- Documentation — https://docs.nvidia.com/openshell/latest/index.html
- Dépôt — https://github.com/NVIDIA/OpenShell

## Voir aussi

- [[Garde-fous hors modèle]] — le principe : une règle appliquée par le runtime tient même si le modèle se trompe
- [[Isolation par politique déclarative]] — Landlock, seccomp, proxy et identifiants substitués
- [[Sandboxing de code généré]] — la solidité du mur (conteneur, gVisor, microVM), que la politique complète
- [[Excessive agency et lethal trifecta]] — ce qu'aucune sandbox ne corrige
- [[Comparatif - Isolation d'exécution d'un agent]] — OpenShell face aux autres mises en œuvre, sans classement
- [[Systèmes IA]] — le hub du dossier
