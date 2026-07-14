---
galaxie: wiki
type: concept
nom: Human-in-the-loop
alias: [HITL, human in the loop, supervision humaine, validation humaine, intervention humaine]
categorie: concept/llm
domaines: [ai-eng]
tags: [human-in-the-loop, agents, reliability, llm]
---

# Human-in-the-loop

## Aperçu

- Insérer un **point de contrôle humain** dans une boucle d'agent : avant une action à fort enjeu, l'agent **s'arrête** et attend une validation, une correction ou un rejet.
- Réponse pragmatique au caractère non déterministe d'un agent : on ne lui confie pas les actions **irréversibles** (paiement, suppression, envoi) sans garde-fou humain.

## Concepts clés

### Approuver / éditer / rejeter
- Trois interventions de base à un point d'arrêt : **approuver** l'action proposée, l'**éditer** (corriger les arguments) avant exécution, ou **rejeter** et faire reprendre l'agent autrement.

### Où placer le point d'arrêt
- Typiquement **avant un appel d'outil à effet de bord** (cf. [[Tool use patterns]]) : l'agent propose l'action, la boucle ([[agent-loops]]) suspend, l'humain tranche, puis l'exécution reprend. Placer trop de points → l'humain devient le goulot ; trop peu → on perd le filet.

### Cibler par le risque
- Calibrer selon l'enjeu : action **réversible et peu coûteuse** → laisser passer ; **irréversible ou sensible** → exiger validation. Un seuil de **confiance** ou de **montant** déclenche l'escalade.

### Persistance & reprise
- HITL impose de **suspendre puis reprendre** une exécution potentiellement longue : l'état de l'agent doit être persisté en attendant la décision humaine (checkpointing), pas gardé en mémoire vive.

### HITL d'exécution vs HITL d'apprentissage
- Ici : contrôle **au moment de l'action** (faire/ne pas faire). À distinguer du feedback humain d'**entraînement** (RLHF, annotation de préférences) qui façonne le modèle en amont, pas une décision en production.

## Les maths, simplement

- Arbitrage du seuil d'escalade : déclencher la revue humaine quand le risque attendu dépasse son coût. Avec une probabilité d'erreur $p$, un coût d'erreur $C_{\text{err}}$ et un coût de revue $C_{\text{rev}}$, escalader si $p \cdot C_{\text{err}} > C_{\text{rev}}$.
- Conséquence : sur une action **irréversible** ($C_{\text{err}}$ très grand), on escalade même quand $p$ est faible — le rappel prime sur le confort.

## En pratique

- [[Dev/Services/LangGraph|LangGraph]] expose le HITL nativement : `interrupt` sur un nœud + état persistant (checkpointer) pour suspendre/reprendre ; [[Dev/Services/CrewAI|CrewAI]] et [[Dev/Services/PydanticAI|PydanticAI]] prévoient des points de validation et la durabilité d'exécution.
- Rendre les outils sensibles **idempotents** et journaliser la décision humaine (qui a approuvé quoi) — cf. [[LLM observability]].
- Combiner avec les [[Guardrails|garde-fous]] : un garde-fou peut **router vers une revue humaine** plutôt que bloquer sèchement.
- Définir une **politique d'escalade** explicite par type d'action plutôt que de demander validation partout — sinon l'humain sature et approuve sans lire (validation-tampon).
- Pièges : interruptions trop fréquentes (l'humain devient le goulot et tamponne) ; pas de timeout sur l'attente humaine (l'agent reste bloqué) ; oublier de persister l'état (impossible de reprendre).

## Approches voisines & alternatives

- [[Reliability patterns]] — le HITL sur les actions à fort enjeu est l'un de ses garde-fous d'effet de bord.
- [[agent-loops]] — c'est la boucle que le point d'arrêt suspend puis relance.
- [[Tool use patterns]] — le HITL s'insère juste avant l'appel d'outil à effet de bord.
- [[Guardrails]] — alternative ou complément automatique : bloquer/filtrer par règle au lieu d'escalader.
- [[Agent evaluation]] — mesurer où l'agent échoue aide à cibler les points d'arrêt utiles.
- Alternative : **pleine autonomie** (aucun point d'arrêt) — acceptable seulement quand toutes les actions sont réversibles et à faible enjeu.

## Pour aller plus loin

- Anthropic (2024) — *Building Effective Agents* (garde-fous, supervision des actions sensibles).
- Docs LangGraph — *Human-in-the-loop* (`interrupt`, reprise depuis un checkpoint).
- Liés : [[Reliability patterns]], [[Guardrails]], [[agent-loops]].
