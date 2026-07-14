---
galaxie: wiki
type: concept
nom: LLM observability
alias: [observabilité LLM, observabilité des apps LLM, tracing LLM, online eval, monitoring LLM, traces, spans, coûts tokens]
categorie: concept/llm
domaines: [ai-eng, mlops]
tags: [llm-observability, tracing, llm]
---

# LLM observability

## Aperçu

- Comprendre ce que fait une app LLM **en production** : tracer chaque appel, mesurer coût / latence / erreurs, et noter la qualité sur le trafic réel. Le pendant **online** de l'éval offline ([[LLM eval metrics]]).
- Indispensable car un LLM est non déterministe et la qualité dérive (changement de modèle, de données, de prompt) : sans traces, on débogue à l'aveugle.

## Concepts clés

### La trace et le span
- Une requête = une **trace** ; chaque étape (appel LLM, outil, retrieval, tour d'agent) = un **span** imbriqué. On reconstitue « qui appelle quoi », avec latence et coût par span.
- C'est la granularité qui rend débogable un [[agent-loops|agent]] ou un pipeline [[RAG]] multi-étapes. Souvent bâti sur **OpenTelemetry**.

### Les signaux suivis
- **Coût** (tokens in/out × prix), **latence** (dont time-to-first-token), **débit**, **taux d'erreur / de refus**, **cache hit** (cf. [[prompt-caching]]).

### Online eval
- Scorer un échantillon du trafic en continu via [[LLM-as-judge]] ou des heuristiques ; collecter le **feedback utilisateur** (pouce, correction).
- Détecte les régressions que l'éval offline rate, parce que le trafic réel diffère du jeu de test.

### Observabilité vs éval offline
- **Offline** : jeu figé, avant déploiement, reproductible.
- **Online** : trafic réel, après déploiement, non reproductible mais représentatif. Les deux sont complémentaires.

## Les maths, simplement

- Pas de formule propre : c'est de l'**agrégation de séries temporelles** (percentiles de latence p50/p95, coût cumulé, taux d'erreur) sur des traces. La difficulté est l'**échantillonnage** — que tracer et noter sans exploser le coût — pas le calcul.

## En pratique

- Instrumenter **dès le premier prototype** : rétro-ajouter le tracing est pénible.
- Choisir une plateforme : [[Dev/Services/Langfuse|Langfuse]] (open-source, OTel), [[Dev/Services/LangSmith|LangSmith]] (écosystème LangChain), [[Dev/Services/Phoenix Arize|Phoenix Arize]] (OTel / OpenInference), [[Dev/Services/Helicone|Helicone]] (proxy / gateway, une ligne).
- Surveiller les **coûts par feature** et les **dérives de qualité**, pas seulement l'uptime.
- Boucler : les cas qui ratent en prod alimentent le jeu d'[[LLM eval metrics|éval offline]] (le « data flywheel »).

## Approches voisines & alternatives

- [[LLM eval metrics]] — l'éval offline, dont l'observabilité est le pendant en ligne.
- [[LLM-as-judge]] — sert à scorer le trafic en continu.
- [[agent-loops]] — le tracing par span est ce qui rend un agent débogable.
- [[prompt-caching]] — le cache hit est un signal clé de coût.
- [[Tool use patterns]] — chaque appel d'outil devient un span observable.

## Pour aller plus loin

- Documentation OpenTelemetry — *GenAI semantic conventions*.
- Docs Langfuse / Phoenix Arize — modèle de traces & spans.
