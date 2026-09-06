---
role: comparatif
nom: Comparatif - Observabilité LLM
categorie: llm/observabilite
tags: [llm-observability, tracing]
---

# Comparatif - Observabilité LLM

> On tranche sur : comment la trace est captée — proxy sur le chemin critique ou SDK OpenTelemetry —, et sur la licence, qui décide de l'auto-hébergement.

![[Comparatif - Observabilité LLM.base]]

## Ce qui départage

- [[Langfuse]] — le seul dont le **cœur est MIT**, donc le seul qui passe une exigence OSI stricte, et il réunit traces, prompts versionnés, évals et datasets dans un même workflow. Deux réserves : c'est de l'**open-core** — vérifier que la fonction visée n'est pas dans `ee/` — et le self-host de prod veut ClickHouse + Postgres + Redis.
- [[Phoenix Arize]] — bâti **nativement sur OpenTelemetry / OpenInference** : l'instrumentation est portable et ne couple à aucun éditeur de framework, et le self-host tient en un conteneur. Sa licence **ELv2 est *source-available*, pas OSI** — c'est le point qui bloque en procurement, pas une fonction manquante.
- [[LangSmith]] — le produit **propriétaire** de LangChain Inc. : l'intégration la plus serrée avec LangChain/LangGraph, éval continue et déploiement d'agents inclus. Le self-host est **réservé à l'offre entreprise** ; une petite équipe reste sur le SaaS.
- [[Helicone]] — le seul en **mode proxy** : on change l'URL de base et on obtient logs, coûts, cache et rate-limiting sans instrumenter le code — au prix d'un intermédiaire sur le chemin critique des appels. Racheté par Mintlify le 3 mars 2026 et passé en **maintenance mode** : plus de roadmap, à écarter pour un projet à horizon long.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
