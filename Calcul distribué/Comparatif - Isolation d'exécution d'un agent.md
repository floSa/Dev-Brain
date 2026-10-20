---
role: comparatif
nom: Comparatif - Isolation d'exécution d'un agent
categorie: compute/a-la-demande
tags: [sandbox, ai-security, agents]
---

# Comparatif - Isolation d'exécution d'un agent

> On tranche sur : **où s'applique la règle** (dans un processus local confiné, dans une microVM ou un noyau émulé créés à la demande, dans le harnais lui-même), **ce qui est isolé** (fichiers, appels système, réseau, secrets), la licence et l'hébergement — plus ce que chaque frontière laisse à découvert. **Aucun classement** : aucune des sources lues ne donne de mesure comparable entre ces outils, et un contrôle appliqué hors du modèle ne se note pas sur une échelle.

![[Comparatif - Isolation d'exécution d'un agent.base]]

## Ce qui départage

- [[OpenShell]] — le **runtime à politique** : un gateway, un superviseur et une sandbox ; la règle est un fichier YAML appliqué par le noyau (Landlock, seccomp) et par un proxy qui filtre le réseau par hôte, programme, méthode et chemin et ajoute lui-même les identifiants. Auto-hébergé, Apache-2.0. Le prix : Linux 6.2 ou plus, une version 0.1.x, et des défauts permissifs (inspection en `audit`, fichiers en `best_effort`) tant qu'on ne les change pas.
- [[sandbox-runtime]] — l'**enveloppe de processus** : une commande préfixée par `srt`, bubblewrap sur Linux, Seatbelt sur macOS, un proxy à liste de domaines ; fichiers et réseau isolés ensemble, sans conteneur ni gateway. Apache-2.0. Le prix : une préversion, des listes de domaines et non de requêtes, Windows en alpha.
- [[E2B]] — la **microVM à la demande** : un bac à sable Firecracker à noyau dédié, créé et détruit par SDK ; cloud managé ou auto-hébergé (Terraform). Apache-2.0. Le prix : l'isolation du calcul ne filtre pas le réseau sortant, et un secret monté est donné au code non fiable.
- [[Daytona]] — la **microVM managée avec état** : noyau dédié et snapshots qui permettent de retrouver son espace de travail ; passé closed-source en juin 2026. Le prix : plus aucun moyen d'auditer l'isolation, et les snapshots font survivre la surface d'attaque d'une session à l'autre.
- [[Modal]] — le **noyau émulé** : des conteneurs isolés par gVisor, avec un GPU disponible à l'intérieur ; service propriétaire, sans auto-hébergement. Le prix : gVisor n'est pas une microVM, à mesurer pour du code franchement hostile.
- [[DeepSeek Harness]] — l'**isolation dans le harnais** : un bac à sable local (bwrap et Landlock, Seatbelt, jeton restreint sous Windows) qui ne gouverne que les effets sur les fichiers, et des plugins qui s'exécutent dans le processus hôte, hors de lui. MIT. Le prix : ni réseau ni visibilité des processus confinés, et un éditeur qui recommande lui-même une machine jetable.

Ils ne répondent pas à la même question. Trois s'**exécutent à côté de l'agent** et lui imposent une frontière ([[OpenShell]], [[sandbox-runtime]], le bac à sable de [[DeepSeek Harness]]) ; trois **fournissent l'endroit où le code tourne** ([[E2B]], [[Daytona]], [[Modal]]). Un même agent peut combiner les deux : un runtime à politique **dans** une microVM.

**Critère par critère**

| Brique | Où s'applique la règle | Ce qui est isolé | Ce qui reste à découvert | Licence et hébergement |
|---|---|---|---|---|
| [[OpenShell]] | un superviseur hors du processus de l'agent ; noyau et proxy | fichiers (Landlock), appels système (seccomp), réseau (proxy à politique), identifiants (substitués) | une politique trop large ; l'inspection en `audit` ; une évasion de la sandbox (six CVE corrigées en v0.0.34) | Apache-2.0 ; auto-hébergé |
| [[sandbox-runtime]] | le système d'exploitation, autour du processus enveloppé | fichiers et réseau (liste de domaines) ; identifiants masquables | tout ce qui tourne hors du processus enveloppé ; Windows en alpha | Apache-2.0 ; local |
| [[E2B]] | une microVM Firecracker créée par SDK | tout le calcul du code exécuté, noyau dédié | le réseau sortant sans liste blanche ; les secrets montés ; les ressources sans plafond | Apache-2.0 ; managé ou auto-hébergé |
| [[Daytona]] | une microVM managée, noyau dédié, snapshots | le calcul du code exécuté | l'audit de l'isolation (fermée) ; la persistance des snapshots | source-available ; managé seulement |
| [[Modal]] | gVisor, un noyau en espace utilisateur | le calcul du code exécuté, avec un GPU | un niveau d'isolation inférieur à une microVM | propriétaire ; managé seulement |
| [[DeepSeek Harness]] | le harnais ; un bac à sable local pour les commandes | les **effets sur les fichiers** uniquement | le réseau, les processus ; tout plugin installé (dans le processus hôte) | MIT ; local |

**Où s'applique la règle.** Hors du modèle dans tous les cas : c'est le point commun, et celui de [[Garde-fous hors modèle]]. Le noyau (Landlock, seccomp, bubblewrap, Seatbelt) ou un hyperviseur applique ; ni le prompt ni le modèle n'ont voix au chapitre. La différence tient à **qui configure** : un fichier de politique relu comme du code chez [[OpenShell]] et [[sandbox-runtime]], un SDK qui crée un bac à sable chez [[E2B]], [[Daytona]] et [[Modal]], des préréglages de permission chez [[DeepSeek Harness]].

**Ce qui est isolé.** [[OpenShell]] et [[sandbox-runtime]] traitent fichiers, réseau et identifiants par une même politique ; [[OpenShell]] y ajoute un filtre d'appels système détaillé et l'inspection de la méthode et du chemin des requêtes. Les microVM isolent **le calcul** avec un noyau propre mais laissent au réseau et aux secrets le soin d'être traités à part : voir [[Sandboxing de code généré]]. Le bac à sable de [[DeepSeek Harness]] ne couvre que les fichiers.

**Licence et hébergement.** Quatre briques sont libres et auto-hébergeables ou locales ([[OpenShell]], [[sandbox-runtime]], [[E2B]], [[DeepSeek Harness]]). [[Daytona]] et [[Modal]] sont managés seulement. Rien de payant n'est requis pour les quatre premières ; l'usage d'un fournisseur managé suppose un compte et une facturation à la consommation.

**Maturité.** [[OpenShell]] (0.1.x) et [[sandbox-runtime]] (préversion bêta) sont jeunes ; [[DeepSeek Harness]] est une préversion développeur qui annonce des changements incompatibles ; [[E2B]] et [[Modal]] sont déclarés en production. Aucune mesure indépendante de la résistance à un attaquant qui s'adapte n'a été trouvée pour les trois premiers.

**Pas de fiche ici**, pour ce qui n'est pas une brique du brain :

- **La microVM, gVisor, le conteneur** — des technologies d'isolation, décrites dans [[Sandboxing de code généré]] : elles disent la solidité du mur, pas ce qui le traverse ([[Isolation par politique déclarative]]).
- **Le bac à sable de Claude Code** — il ne couvre que les commandes du shell (ses outils de fichiers, ses serveurs MCP et ses hooks tournent hors de lui) et n'existe pas sous Windows natif d'après sa documentation relevée le 2026-10-20 ; son code ouvert, `sandbox-runtime`, a sa fiche, l'agent lui-même n'en a pas.
- **Les services d'exécution fermés ou payants sans version sur site** — cités en texte simple quand un client les utilise.

Un bac à sable ne dispense pas du moindre pouvoir : il **contient** l'exécution, il n'empêche ni l'action erronée sur un outil autorisé ni la fuite par un canal permis ([[Excessive agency et lethal trifecta]]).

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Calcul distribué]] — le hub du dossier.
- [[Sandboxing de code généré]] — la notion : conteneur, gVisor, microVM, et ce que l'isolation du calcul ne règle pas.
- [[Garde-fous hors modèle]] — l'isolation parmi les quatre mécanismes qui s'appliquent hors du modèle.
