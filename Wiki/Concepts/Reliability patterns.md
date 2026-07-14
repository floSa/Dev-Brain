---
galaxie: wiki
type: concept
nom: Reliability patterns
alias: [patrons de fiabilité, reliability patterns, fiabilité des apps LLM]
categorie: concept/llm
domaines: [ai-eng]
tags: [reliability, llm, agents]
---

# Reliability patterns

## Aperçu

- Patrons pour rendre une app LLM **fiable en production** malgré un composant non déterministe, faillible et soumis à des quotas.
- Principe : ne jamais faire confiance à un appel LLM ou outil unique — encadrer, valider, prévoir l'échec.

## Concepts clés

### Retries & backoff
- Rejouer un appel échoué (timeout, 429, 5xx) avec **backoff exponentiel + jitter**. Distinguer les erreurs **transitoires** (à rejouer) des erreurs **permanentes** (à remonter).

### Timeouts & circuit breakers
- Borner chaque appel par un **timeout** ; couper un fournisseur défaillant par un **circuit breaker** pour ne pas propager la panne ni épuiser le budget.

### Fallback & dégradation gracieuse
- Bascule **modèle** ou **fournisseur** quand le primaire échoue ou sature ([[Dev/Services/LiteLLM|LiteLLM]] : routage + fallback). Préférer une réponse dégradée (modèle plus petit, réponse partielle, message honnête) à un plantage.

### Validation & repair
- Valider la sortie contre un schéma et, si invalide, **réinjecter l'erreur** pour correction (boucle de réparation bornée) — cf. [[Structured outputs]], [[Dev/Services/Instructor|Instructor]].

### Garde-fous des effets de bord
- Outils à effet de bord (écriture, paiement, mail) : **idempotence**, permissions, et [[Human-in-the-loop|human-in-the-loop]] sur les actions à fort enjeu. Borner les itérations d'agent pour éviter l'emballement (cf. [[agent-loops]]).

## Les maths, simplement

- Fiabilité d'une chaîne de $k$ étapes indépendantes à fiabilité $p$ : $p^k$ — chute géométrique. À $p=0{,}99$, $k=20$ donne $\approx 0{,}82$.
- Un retry qui ramène l'échec transitoire de $q$ à $q^2$ sur deux tentatives relève $p$ par étape — d'où l'effet de levier des retries sur la trajectoire entière.

## En pratique

- Hiérarchiser : **timeout + retry/backoff** d'abord (gain maximal pour un coût minimal), puis fallback, puis circuit breaker.
- Rendre les **outils idempotents** ou ajouter une clé d'idempotence : un retry ne doit pas payer deux fois.
- **Observer pour fiabiliser** : taux d'erreur, latence p95, coût par requête — [[LLM observability]], [[Dev/Services/Langfuse|Langfuse]].
- Définir une **dégradation gracieuse** explicite par cas d'usage, plutôt que de laisser remonter une exception brute à l'utilisateur.
- Piège : retries agressifs sans backoff → amplification d'une panne fournisseur (effet tempête).

## Approches voisines & alternatives

- [[Tool use patterns]] — la robustesse des appels d'outils (validation d'arguments, retries) est une brique de fiabilité.
- [[Structured outputs]] — la validation + repair est le patron de fiabilité des sorties.
- [[agent-loops]] — bornage des itérations et sortie d'échec.
- [[Agent evaluation]] — mesurer la fiabilité (taux de réussite, erreur composée) avant et après les garde-fous.
- [[Context engineering]] — un contexte maîtrisé réduit les échecs (dépassement de fenêtre, dérive).
- [[Human-in-the-loop]] — le garde-fou humain sur les actions irréversibles à fort enjeu.

## Pour aller plus loin

- Anthropic (2024) — *Building Effective Agents* (garde-fous, quand borner une boucle).
- Michael Nygard — *Release It!* : patterns de résilience (retries, circuit breaker, bulkhead) transposés aux appels LLM.
