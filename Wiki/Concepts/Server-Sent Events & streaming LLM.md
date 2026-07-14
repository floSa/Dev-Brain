---
galaxie: wiki
type: concept
nom: Server-Sent Events & streaming LLM
alias: [SSE, server-sent events, streaming LLM, streaming de tokens, sse-starlette, text/event-stream, EventSource]
categorie: concept/llm
domaines: [ai-eng]
tags: [streaming, llm, web-framework]
---

# Server-Sent Events & streaming LLM

## Aperçu

- Un LLM génère **token par token** ; le streaming pousse chaque token au client dès qu'il est produit, au lieu d'attendre la réponse complète. Le time-to-first-token devient court et l'attente perçue s'effondre.
- **SSE** (Server-Sent Events) : canal HTTP **unidirectionnel** serveur → client (`text/event-stream`), simple et natif navigateur (`EventSource`). C'est le transport par défaut du streaming LLM.

## Concepts clés

### Le protocole SSE
- Une seule requête HTTP reste ouverte ; le serveur émet des **événements** texte `data: …\n\n`. Reconnexion automatique, champs `event:` / `id:` optionnels. Plus léger qu'un WebSocket quand le flux ne va que dans un sens.

### Côté serveur : générateur asynchrone
- L'endpoint renvoie un **générateur** qui `yield` chaque chunk au fil de la génération. En Python/ASGI : `sse-starlette` (`EventSourceResponse`) au-dessus de [[Dev/Services/FastAPI|FastAPI]] / Starlette ; les SDK LLM exposent un mode `stream=True` dont on itère les deltas.

### Format des chunks
- Chaque événement transporte un **delta** de texte (token ou sous-token, cf. [[Tokenization]]). Convention OpenAI : objets JSON `chat.completion.chunk`, flux clôturé par `data: [DONE]`. Le client reconstitue la réponse par concaténation.

### Fin, erreurs, annulation
- Signaler la fin proprement. Une erreur **après** le premier octet ne peut plus changer le code HTTP (déjà `200`) → il faut la passer **dans le flux**. Détecter la déconnexion client pour arrêter la génération et ne pas brûler des tokens pour rien.

## Les maths, simplement

- Pas de maths à proprement parler, mais un changement de modèle de latence. Sans streaming, l'attente vaut $T_{\text{total}} = n \cdot t_{\text{token}}$ ($n$ tokens, $t_{\text{token}}$ par token). Avec streaming, l'utilisateur lit dès le **time-to-first-token** $t_{\text{TTFT}} \ll T_{\text{total}}$, le reste défilant au débit de génération (tokens/s).

## En pratique

- **Quand** : toute UX conversationnelle (chat) ou réponse longue ; réduit l'abandon. Inutile pour un appel court non affiché (extraction, batch) où l'on ne veut que le résultat final.
- **Stack Python** : `EventSourceResponse` de `sse-starlette`, ou `StreamingResponse` ASGI nu ; itérer le `stream=True` du SDK et relayer chaque delta. Penser à désactiver le buffering proxy (nginx `X-Accel-Buffering: no`).
- **Streaming + sortie structurée** : tension réelle — un JSON n'est valide qu'une fois **complet**. Streamer le raisonnement en texte puis l'objet final, ou parser le flux de façon tolérante (cf. [[Structured outputs]]).
- **Observabilité** : tracer TTFT, tokens/s et taux de déconnexion (cf. [[LLM observability]]) ; prévoir retries / fallback (cf. [[Reliability patterns]]), délicats une fois le flux commencé.

## Approches voisines & alternatives

- [[Decoding strategies]] — c'est le décodage token par token qui **produit** le flux streamé.
- [[Tokenization]] — l'unité qui circule dans chaque événement.
- **WebSocket** (pas de page) — canal **bidirectionnel** ; à préférer si le client doit aussi pousser pendant la génération (voix, interruptions). Plus lourd que SSE pour un simple flux serveur → client.
- **HTTP chunked / NDJSON / gRPC streaming** (pas de page) — autres transports de flux côté serveur.
- [[Inference optimization]] — continuous batching et KV-cache alimentent plusieurs flux SSE en parallèle côté serveur.

## Pour aller plus loin

- WHATWG *HTML Living Standard* — Server-Sent Events (`EventSource`, `text/event-stream`).
- Documentation `sse-starlette` — `EventSourceResponse`, gestion de la déconnexion client.
- Conventions de streaming des API LLM (`chat.completion.chunk`, sentinelle `data: [DONE]`).
