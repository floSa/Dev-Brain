---
galaxie: wiki
type: concept
nom: Routing and cascading
alias: [routing, query routing, semantic routing, model routing, model cascading, cascade de modèles, routage et cascade]
categorie: concept/llm
domaines: [ai-eng]
tags: [routing, llm, rag]
---

# Routing and cascading

## Aperçu

- Deux décisions d'**aiguillage** pour servir chaque requête au meilleur coût.
- **Routing** : diriger une requête vers la bonne ressource (index, source, outil, modèle). **Cascading** : enchaîner des modèles du moins cher au plus cher et s'arrêter dès que la réponse suffit.

## Concepts clés

### Query routing
- Classer l'intention de la requête → choisir l'index, la source de données ou l'outil adéquat (RAG multi-sources, agents).
- Implémentations : classifieur LLM, règles, ou **semantic routing** (comparer l'[[embeddings|embedding]] de la requête à des prototypes — rapide, sans appel LLM).

### Model routing
- Choisir le modèle selon la **difficulté** estimée : un [[Small Language Models|petit modèle]] pour le trivial, un gros modèle pour le complexe.

### Cascading
- Appeler d'abord un modèle léger ; un **score de confiance** (self-check, vérificateur, longueur) décide s'il faut **escalader** vers un modèle plus cher.
- Réduit le coût **moyen** : la plupart des requêtes se règlent à l'étage bon marché.

### Au niveau infra
- Une passerelle comme [[Dev/Services/LiteLLM|LiteLLM]] fait du routage / fallback entre fournisseurs (coût, charge, panne) — du routing d'infrastructure, complémentaire du routing sémantique applicatif.

## Les maths, simplement

- Coût espéré d'une cascade à deux étages : $E[\text{coût}] = c_1 + (1 - p_1)\,c_2$, où $c_i$ est le coût de l'étage $i$ et $p_1$ la probabilité que l'étage léger suffise.
- Gain net tant que $p_1$ est élevé et $c_2 \gg c_1$. La contrepartie : l'escalade ne doit pas trop souvent **rater** une requête que l'étage léger a mal traitée — d'où la qualité du critère d'escalade.

## En pratique

- Garder le routeur **simple et mesurable** : c'est lui-même une source d'erreurs (mauvais aiguillage = mauvaise réponse, silencieusement).
- Préférer le **semantic routing** quand la latence compte (pas d'appel LLM pour décider).
- Cascading : définir explicitement le critère d'escalade et **mesurer coût ET qualité** ensemble — optimiser le coût seul fait chuter la qualité sans le voir.
- Un [[LLM caching|cache de réponses]] en amont court-circuite toute la cascade sur les requêtes déjà vues.

## Approches voisines & alternatives

- [[Advanced RAG]] — le routing est une de ses briques (diriger vers le bon index).
- [[Query transformations]] — souvent en amont : transformer la requête, puis l'aiguiller.
- [[Small Language Models]] — l'étage léger naturel d'une cascade.
- [[LLM caching]] — l'étage 0, avant tout modèle.
- [[RAG eval]] — pour valider que le routeur dirige bien et que la cascade ne dégrade pas.
- [[Dev/Services/LiteLLM|LiteLLM]] — routage / fallback multi-fournisseurs au niveau passerelle.

## Pour aller plus loin

- Chen et al. (2023) — *FrugalGPT* (cascade de LLM pour réduire le coût).
- Ong et al. (2024) — *RouteLLM* (router apprenant fort/faible).
