---
galaxie: wiki
type: concept
nom: Agent memory
alias: [mémoire d'agent, agent memory, mémoire LLM]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm, retrieval]
---

# Agent memory

## Aperçu

- Ce qu'un agent retient au-delà d'un seul appel : le **scratchpad** de la tâche en cours (court terme) et les connaissances **persistées** entre sessions (long terme).
- Sans mémoire, un agent recommence de zéro à chaque tour et sature sa fenêtre de contexte.

## Concepts clés

### Court terme (contexte de travail)
- Historique de la boucle courante : messages, pensées, observations d'outils. Vit dans la fenêtre de contexte, disparaît à la fin de la tâche.

### Long terme (persistée)
- Stockée hors contexte (fichier, base, [[Bases de données vectorielles]]) et **récupérée** au besoin — c'est du [[RAG]] appliqué à l'historique de l'agent, via des [[embeddings]].

### Types de mémoire
- **Épisodique** (événements passés : « ce qui s'est dit »), **sémantique** (faits stabilisés sur l'utilisateur / le domaine), **procédurale** (recettes, instructions apprises).

### Gestion de la fenêtre
- Le contexte est borné → stratégies : **troncature** (garder les N derniers tours), **résumé progressif** (compresser l'ancien), **récupération sélective** (ne ramener que le pertinent).

## Les maths, simplement

- Sous un budget de fenêtre $W$ tokens, on doit respecter $\sum_i s_i \le W$ où $s_i$ est la taille de chaque souvenir injecté → on sélectionne le top-$k$ des souvenirs les plus pertinents : $\operatorname{top\text{-}k}_m \cos(\mathbf{e}_q, \mathbf{e}_m)$, $\mathbf{e}$ étant l'embedding de la requête $q$ et du souvenir $m$.
- Intuition : la mémoire long terme est un problème de **récupération sous contrainte de budget** — exactement le compromis du RAG.

## En pratique

- Le court terme suffit pour des tâches courtes ; n'ajouter du long terme que si l'agent doit se souvenir entre sessions ou dépasse la fenêtre.
- **Résumer** plutôt que tronquer brutalement quand l'historique compte ; garder les ancres (objectif, décisions clés) en clair.
- Outillage : [[Dev/Services/Letta|Letta]] (ex-MemGPT) fait de la mémoire persistante hiérarchique sa **primitive centrale** ; [[Dev/Services/LangGraph|LangGraph]] persiste l'état entre les pas (checkpointers) ; les frameworks RAG ([[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/LangChain|LangChain]]) fournissent stockage et récupération de mémoire.
- Pièges : mémoire qui enfle sans tri (bruit, coût) ; souvenirs périmés jamais invalidés ; fuite de données entre utilisateurs si la mémoire n'est pas cloisonnée.

## Approches voisines & alternatives

- [[RAG]] / [[Advanced RAG]] — la même mécanique de récupération, appliquée à la mémoire.
- [[embeddings]] / [[Bases de données vectorielles]] — le socle de la mémoire long terme.
- [[agent-loops]] — c'est le contexte qui s'y accumule que la mémoire gère.
- [[Agent patterns]] — la mémoire conditionne les patrons (réflexion, plan-execute).
- [[mcp-protocol]] — les *resources* MCP sont un canal d'alimentation de la mémoire long terme.
- Alternative : **tout garder dans le contexte** (fenêtres longues) — simple, mais coûteux et plafonné ; la récupération reste préférable au-delà d'un certain volume.

## Pour aller plus loin

- Park et al. (2023) — *Generative Agents* (mémoire épisodique + récupération + réflexion).
- Packer et al. (2023) — *MemGPT* (gestion de la mémoire comme une hiérarchie type OS).
