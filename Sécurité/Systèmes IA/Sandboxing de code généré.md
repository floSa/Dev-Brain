---
role: notion
nom: Sandboxing de code généré
alias: [sandboxing, sandbox, bac à sable, code execution sandbox, exécution isolée, microVM]
categorie: security/ia
domaines: [ai-eng]
tags: [agents, llm, ai-security, container]
---

# Sandboxing de code généré

## Aperçu

- Exécuter du code **produit par un LLM** — ou fourni par un utilisateur — dans un environnement isolé, jetable, dont la compromission n'atteint pas l'hôte ni les autres tenants.
- Le point de départ est une hypothèse simple : le code généré est **non fiable par construction**. Non par malveillance du modèle, mais parce que son entrée peut l'être ([[Prompt injection]]) et parce qu'il n'a pas été relu.

## Concepts clés

### Le degré d'isolation

Trois niveaux, du plus perméable au plus étanche :

| Mécanisme | Isolation | Démarrage | Remarque |
|---|---|---|---|
| **Conteneur** (namespaces, cgroups) | kernel **partagé** | ~ms | une évasion de conteneur atteint l'hôte |
| **Kernel en espace utilisateur** (gVisor) | syscalls interceptés | sous-seconde | compromis courant ; surface réduite sans VM complète |
| **microVM** (Firecracker) | kernel **dédié**, matériel virtualisé | ~100-200 ms | le plus étanche des trois |

Le conteneur seul ne suffit pas pour du code hostile : c'est un mécanisme de packaging, pas une frontière de sécurité.

### Ce qui fuit quand le calcul est isolé

L'isolation du calcul ne règle pas tout. Restent à traiter explicitement :

- le **réseau sortant** — sans filtrage, un bac à sable parfaitement isolé exfiltre quand même (`curl` vers un domaine tiers) ;
- les **secrets** — une clé d'API montée dans le bac à sable est une clé donnée au code non fiable ;
- les **ressources** — CPU, mémoire, durée : sans plafond, une boucle infinie devient un déni de service et une facture ;
- la **persistance** — ce qui survit entre deux exécutions redevient un canal d'attaque.

### Éphémère contre stateful

Un bac à sable jetable est le plus sûr : chaque exécution repart d'un état propre. Mais un agent qui travaille sur un dépôt a besoin de retrouver son espace de travail. Les plateformes répondent par des **snapshots** — état figé, repris à la demande — qui rétablissent la continuité au prix d'une surface d'attaque persistante.

## En pratique

- **Ne jamais exécuter du code généré dans le processus de l'agent** (`exec`, `eval`) ni sur la machine hôte : c'est le défaut le plus fréquent et le plus coûteux.
- Choisir selon le risque : conteneur pour du code interne de confiance, microVM ou gVisor dès que l'entrée est publique ou multi-tenant.
- Poser d'emblée les **plafonds** — délai maximum, mémoire, réseau en liste blanche — plutôt que d'attendre l'incident.
- Backends courants côté agents : local, Docker, SSH, puis les plateformes managées [[E2B]] (Firecracker), [[Modal]] (gVisor, GPU disponible), [[Daytona]]. [[Hermes Agent]] les expose comme backends interchangeables.
- Piège : croire qu'un bac à sable rend l'agent sûr. Il **contient les dégâts de l'exécution**, il n'empêche ni l'action erronée sur les outils légitimes, ni l'exfiltration par un canal autorisé.

## Approches voisines & alternatives

- [[Prompt injection]] — la raison d'être du sandboxing : l'entrée non fiable devient du code exécuté.
- [[AI security]] — le cadre général des risques d'un système LLM.
- [[Guardrails]] — filtrent en amont ce qui entre et sort ; complémentaires, pas substituables.
- [[Human-in-the-loop]] — faire valider une action à fort enjeu plutôt que de l'isoler.
- [[agent-loops]] — l'exécution de code est une action de la boucle, avec son coût et sa latence.
- Alternative : **ne pas exécuter de code du tout** — restreindre l'agent à des outils fixes et audités. Beaucoup plus sûr, nettement moins capable.

## Pour aller plus loin

- Firecracker (AWS, 2020) — microVM légère conçue pour le multi-tenant, socle de nombreux bacs à sable.
- gVisor (Google) — kernel en espace utilisateur interceptant les syscalls.
- Liés : [[Agent skills]] (un skill peut embarquer du code à exécuter), [[Agent evaluation]].
