---
role: brique
nom: sandbox-runtime
alias: [srt, Anthropic Sandbox Runtime, anthropic sandbox-runtime, "@anthropic-ai/sandbox-runtime", anthropics/sandbox-runtime]
pitch: "Outil en ligne de commande et bibliothèque de bac à sable léger d'Anthropic (Apache-2.0, préversion bêta) — restrictions de fichiers et de réseau au niveau du système d'exploitation, sans conteneur : Seatbelt sur macOS, bubblewrap sur Linux, proxy HTTP et SOCKS5 à liste de domaines ; Windows en alpha."
categorie: security/ia
famille: cli
licence_type: open-source
maturite: beta
langage: TypeScript
alternatives: ["[[OpenShell]]", "[[E2B]]"]
complements: []
tags: [ai-security, sandbox, agents]
url_docs: https://github.com/anthropics/sandbox-runtime#readme
url_repo: https://github.com/anthropics/sandbox-runtime
---

# sandbox-runtime

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande et bibliothèque de bac à sable léger d'Anthropic (Apache-2.0, préversion bêta) — restrictions de fichiers et de réseau au niveau du système d'exploitation, sans conteneur : Seatbelt sur macOS, bubblewrap sur Linux, proxy HTTP et SOCKS5 à liste de domaines ; Windows en alpha.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande (`srt`) et bibliothèque TypeScript qui **enveloppent un processus** dans un bac à sable au niveau du système d'exploitation, sans conteneur : on déclare les chemins lisibles et inscriptibles et les domaines joignables, et tout le reste est refusé. Il sert à confiner un agent, un serveur MCP local, une commande de shell ou un programme quelconque. C'est le paquet ouvert sur lequel Anthropic a bâti le bac à sable de son agent de code ; il ne contient pas cet agent. Fichiers et réseau sont isolés ensemble : sans isolation des fichiers, un processus compromis exfiltre des clés SSH ; sans isolation du réseau, il s'échappe vers Internet. Principe : [[Isolation par politique déclarative]].

Relevé le 2026-10-20 : licence **Apache-2.0** lue dans le fichier `LICENSE` du dépôt `anthropics/sandbox-runtime` ; v0.0.81 publiée le 2026-10-20, dépôt créé le 2025-10-20, 5,6 k étoiles. Le README se présente comme un aperçu de recherche destiné à faire avancer l'écosystème : l'API et les formats de configuration peuvent changer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Confiner **un processus local** (agent, serveur MCP, commande) sans Docker ni gateway : une commande préfixée par `srt` | Le besoin est une **flotte** d'agents avec plan de contrôle, politiques distribuées et approbation formelle → [[OpenShell]] |
| Une **politique courte** en JSON (`filesystem`, `network`), lisible et versionnée | Une microVM à noyau dédié pour du code hostile multi-locataire → [[E2B]] |
| Linux ou macOS : bubblewrap et Seatbelt sont des primitives du système, sans démon à installer | Une isolation sous **Windows natif** sans réserve : le support y est en **alpha**, avec des limites listées (traces d'un service système, SMB, WSL) |
| Masquer des **identifiants** : l'environnement et les fichiers sensibles sont refusés ou remplacés par une valeur factice que le proxy remplace à la sortie | Un durcissement qui résiste à un code qui crée ses propres espaces de noms utilisateur : ils sont **refusés** par défaut (Chromium, podman rootless, bubblewrap imbriqué cessent de fonctionner) |
| Un outil fin à embarquer dans un harnais maison (API `SandboxManager`, proxy autonome `srt proxy` avec décideur externe) | Un contrôle fin sur les **requêtes** (méthode, chemin) livré clés en main : les listes standard portent sur des **domaines** ; une décision par requête passe par le mode proxy autonome avec un processus décideur à écrire |

## Mise en œuvre

- Installation — `npm install -g @anthropic-ai/sandbox-runtime` ; Node.js 22.12 ou plus (champ `engines` du paquet) ; sous Linux : `bubblewrap`, `socat` et `ripgrep` à installer par le gestionnaire de paquets
- Point d'entrée — `srt "curl example.com"` : la commande est exécutée dans le bac à sable ; la politique se lit dans `~/.srt-settings.json` (`filesystem.denyRead`, `allowWrite`, `denyWrite`, `network.allowedDomains`, `deniedDomains`) ; usage comme bibliothèque par `SandboxManager`
- Prérequis — macOS (`sandbox-exec`, sans dépendance) ou Linux (bubblewrap 0.4.0 ou plus) ; sur Ubuntu 24.04 et plus, désactiver `kernel.apparmor_restrict_unprivileged_userns` ou accorder `userns` par un profil AppArmor ; Windows : alpha, étape d'installation élevée unique
- Exécution — en local, un processus enveloppé ; le trafic HTTP et HTTPS passe par un proxy, le reste du TCP par un proxy SOCKS5, tous deux sur la machine hôte
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Par défaut : lecture partout, écriture nulle part, réseau nul.** La lecture est autorisée sauf refus explicite (modèle « refuser puis réautoriser ») ; l'écriture et le réseau sont refusés sauf autorisation. Les secrets lisibles (clés SSH, `.env`) se protègent par `denyRead`.
- **Des listes de domaines, pas de politique de requête intégrée** : le filtre standard porte sur le nom de l'hôte. Le README décrit aussi des options qui **affaiblissent** la frontière (`enableWeakerNestedSandbox`, `allowAppleEvents` : « le bac à sable ne fournit plus d'isolation d'exécution de code », `enableWeakerNetworkIsolation`) : les laisser à leur valeur par défaut.
- **Windows (alpha)** : le filtre réseau ne suit pas un thread qui change de jeton avant de créer une socket ni le trafic qu'un service système porte pour le compte du processus ; un accès SMB local a été observé ; WSL répond à un processus confiné. Ne pas s'appuyer sur les listes de domaines pour ces cas.
- **Couvre les processus qu'il enveloppe, pas ce qui tourne autour** : un outil du harnais qui s'exécute hors du processus enveloppé reste hors de la frontière. Même remarque que pour tout bac à sable de commandes : voir [[Garde-fous hors modèle]].
- **Une préversion de recherche** : pas d'audit publié lu à la source, aucune mesure indépendante trouvée, versions 0.0.x très fréquentes.

## Écosystème

### Alternatives

- [[OpenShell]] — Runtime de bac à sable pour agents d'IA de NVIDIA (Apache-2.0) — une politique déclarative en YAML appliquée hors de l'agent : Landlock et seccomp pour les fichiers et les appels système, un proxy qui filtre le réseau par hôte, programme, méthode et chemin et ajoute les identifiants à la place de l'agent ; jeune (0.1.4 le 2026-10-13), à passer en mode enforce. — un gateway, un superviseur et des politiques inspectant méthode et chemin, au prix d'un déploiement (Docker, Podman, Kubernetes ou microVM) et d'un noyau Linux 6.2 ou plus.
- [[E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform. — une microVM à noyau dédié créée à la demande, au lieu d'un processus local confiné.

## Ressources

- Documentation — https://github.com/anthropics/sandbox-runtime#readme
- Dépôt — https://github.com/anthropics/sandbox-runtime

## Voir aussi

- [[Isolation par politique déclarative]] — le principe : fichiers, réseau, identifiants, politique par défaut refus
- [[Garde-fous hors modèle]] — l'isolation parmi les quatre mécanismes, et ce que la couverture partielle laisse à découvert
- [[Sandboxing de code généré]] — conteneur, gVisor, microVM : la solidité du mur
- [[Comparatif - Isolation d'exécution d'un agent]] — cinq mises en œuvre, sans classement
- [[Systèmes IA]] — le hub du dossier
