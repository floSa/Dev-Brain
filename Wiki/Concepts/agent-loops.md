---
galaxie: wiki
type: concept
nom: agent-loops
alias: [agent loop, boucle d'agent, boucle perception-action, agentic loop]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm, tool-use]
---

# agent-loops

## Aperçu

- La boucle qui fait tourner un agent : le LLM **observe**, décide d'une **action** (souvent un appel d'outil), lit le **résultat**, recommence — jusqu'à une condition d'arrêt.
- C'est le moteur d'exécution sous les [[Agent patterns]] : un agent = un LLM + une boucle + des outils.

## Concepts clés

### Le cycle perception → décision → action → observation
- **Perception** : l'état courant (requête + historique + dernière observation) entre dans le prompt.
- **Décision** : le modèle produit soit une réponse finale, soit un appel d'outil (cf. [[Tool use patterns]]).
- **Action + observation** : l'outil s'exécute, son résultat est réinjecté dans le contexte au tour suivant.

### Conditions d'arrêt
- Réponse finale émise, budget d'étapes atteint, budget de tokens/coût atteint, ou erreur irrécupérable. En définir **au moins une dure**.

### Bornage
- Plafond d'itérations $T_{\max}$ **obligatoire** : sans lui, la boucle peut tourner indéfiniment (outil qui échoue en boucle, objectif jamais jugé atteint).

### Accumulation du contexte
- À chaque tour le contexte grossit (historique + observations) → coût et latence croissent, et la fenêtre finit par saturer. D'où le besoin de [[Agent memory]] (résumé, troncature, récupération).

## Les maths, simplement

- Coût cumulé sur une boucle de $T$ étapes, si le contexte croît linéairement : $C \approx c_{\text{tok}} \sum_{t=1}^{T} (b + t\,\delta)$, où $b$ est le prompt de base, $\delta$ l'ajout par tour et $c_{\text{tok}}$ le prix par token. Le terme en $t$ rend le coût **quadratique** en $T$.
- Conséquence : doubler le nombre d'étapes fait **plus que doubler** la facture — d'où le bornage et la compression du contexte.

## En pratique

- Toujours fixer $T_{\max}$ + un budget de coût ; logguer chaque tour (pensée, outil, observation) pour le débogage — cf. [[LLM observability]].
- Gérer explicitement les **échecs d'outil** : retry borné, message d'erreur réinjecté, sortie d'échec propre.
- [[Dev/Services/LangGraph|LangGraph]] expose la boucle comme un graphe à état persistant et reprise ; [[Dev/Services/LangChain|LangChain]] et [[Dev/Services/PydanticAI|PydanticAI]] fournissent une boucle ReAct prête à l'emploi.
- Piège : juger « tâche accomplie » par le seul LLM — sans critère externe, il s'arrête trop tôt ou jamais.

## Approches voisines & alternatives

- [[Agent patterns]] — les façons d'organiser cette boucle (ReAct, plan-execute, réflexion).
- [[Tool use patterns]] — l'étape « action » de la boucle.
- [[Agent memory]] — gère le contexte qui s'accumule à chaque tour.
- [[Multi-agent systems]] — plusieurs boucles qui se coordonnent.
- [[Human-in-the-loop]] — suspendre la boucle avant une action à fort enjeu pour une validation humaine.
- Alternative : un **enchaînement fixe** (workflow sans boucle) — pas de condition d'arrêt à gérer, mais aucune adaptation aux observations.

## Pour aller plus loin

- Yao et al. (2022) — *ReAct* (formalise pensée / action / observation).
- Anthropic (2024) — *Building Effective Agents* (la boucle minimale d'un agent).
- Liés : [[Context engineering]], [[LLM observability]], [[tool-use]].
