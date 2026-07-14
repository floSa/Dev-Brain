---
galaxie: wiki
type: concept
nom: LLM caching
alias: [response caching, cache de réponses LLM, semantic cache, cache sémantique, exact-match cache, GPTCache]
categorie: concept/llm
domaines: [ai-eng]
tags: [caching, llm, semantic-search, in-memory]
---

# LLM caching

## Aperçu

- Mettre en cache la **réponse** d'un LLM pour éviter de réappeler le modèle sur une requête déjà traitée. Cache **applicatif**, au-dessus de l'API.
- Deux variantes : **exact-match** (clé = hash du prompt) et **sémantique** (clé = embedding ; on sert si une requête passée est assez proche).

## Concepts clés

### Exact-match
- Clé = hash du prompt. Simple et sûr, mais ne fait mouche que sur un prompt **identique**. Store rapide en mémoire ([[Dev/Services/Redis|Redis]]).

### Cache sémantique
- Encoder la requête en [[embeddings|embedding]], chercher la plus proche déjà vue ([[Hybrid retrieval|recherche]] de similarité), servir sa réponse si la similarité dépasse un **seuil**.
- Bien plus de hits (paraphrases, reformulations) mais risque de **faux positifs** : servir la réponse d'une question proche mais pas équivalente.

### Le seuil est l'arbitrage central
- Seuil trop bas → faux positifs (mauvaise réponse servie) ; trop haut → peu de hits. À calibrer et **mesurer**, jamais à deviner.

### Invalidation
- Les réponses se périment (données qui changent, modèle mis à jour) → TTL et **versionnage de la clé** par modèle et version de prompt.

### Quoi cacher
- De préférence du **déterministe** (température basse, requêtes idempotentes). Cloisonner par utilisateur tout contenu personnalisé ou sensible pour ne pas fuiter une réponse d'un user à un autre.

### À ne pas confondre avec le cache de préfixes
- Ici on **évite l'appel entier** ; le [[prompt-caching]] réutilise seulement le calcul du préfixe, la génération a quand même lieu.

## Les maths, simplement

- Coût (ou latence) moyen $\approx (1 - h)\,c_{\text{LLM}} + c_{\text{cache}}$, où $h$ = taux de hit et $c_{\text{cache}} \ll c_{\text{LLM}}$. Tout l'enjeu est de monter $h$ sans dégrader la qualité.
- Pour le cache sémantique, le seuil de similarité $\tau$ pilote une matrice **précision / rappel** : monter $\tau$ augmente la précision (moins de faux positifs) au prix du rappel (moins de hits).

## En pratique

- Outillage : **GPTCache** (lib dédiée), [[Dev/Services/Redis|Redis]] (exact, ou vectoriel pour le sémantique), souvent branché en passerelle ([[Dev/Services/LiteLLM|LiteLLM]] gère le caching).
- Toujours **mesurer les faux positifs** du cache sémantique sur un échantillon avant de l'activer en prod.
- Couplage [[Routing and cascading|cascade]] : le cache est l'**étage 0**, consulté avant tout modèle — le hit le moins cher possible.

## Approches voisines & alternatives

- [[prompt-caching]] — cache du **calcul du préfixe** côté serveur, complémentaire (niveau en dessous).
- [[embeddings]] — la clé du cache sémantique.
- [[Routing and cascading]] — le cache court-circuite la cascade sur les requêtes connues.
- [[Dev/Services/Redis|Redis]] — store de référence (exact ou vectoriel).
- [[Dev/Services/LiteLLM|LiteLLM]] — caching intégré au niveau passerelle.

## Pour aller plus loin

- Zilliz — *GPTCache: Semantic cache for LLMs*.
- Documentation LiteLLM — *Caching*.
