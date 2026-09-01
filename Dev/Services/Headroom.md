---
galaxie: dev
type: service
nom: Headroom
alias: [headroom, headroom-ai, headroomlabs]
pitch: "Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande."
categorie: llm/context
famille: paquet
licence_type: open-source
hosted: self
maturite: beta
langage: "Python, TypeScript, Rust"
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [llm, context-engineering, token-optimization, caching, mcp]
url_docs: https://headroom-docs.vercel.app/docs
url_repo: https://github.com/headroomlabs-ai/headroom
---

# Headroom

## Pourquoi

Le poste de dépense d'un agent n'est pas le prompt système, c'est ce que les outils renvoient : sorties de commandes, logs, fichiers entiers, chunks de RAG. Headroom s'insère **entre l'application et le modèle** et réécrit ce flux entrant sous une forme plus courte, avant facturation.

La propriété qui distingue l'approche est la **réversibilité**. L'original est conservé côté local et le modèle reçoit un outil `headroom_retrieve` : quand la version comprimée ne suffit pas, il redemande le contenu intégral. La compression devient un pari révocable, pas une perte de contexte définitive.

Quatre modes d'insertion, du plus intrusif au moins : **bibliothèque** (`compress(messages)` en Python ou TypeScript), **proxy** transparent (`headroom proxy --port 8787`, aucun changement de code), **enrobage d'agent** (`headroom wrap claude`, et une quinzaine d'assistants de code reconnus), **serveur MCP** exposant les outils de compression, de récupération et de statistiques.

Les gains annoncés sont **auto-déclarés par le projet** : de l'ordre de 15 à 20 % de tokens en moins sur un agent de code, 60 à 95 % sur du JSON verbeux. Aucune mesure indépendante n'est publiée — à revalider sur sa propre charge avant d'en faire une hypothèse de budget. Le projet est **pré-1.0** (v0.37.0 en août 2026).

## Quand l'utiliser

- Agent de code ou agent outillé dont les sorties d'outils saturent la fenêtre de contexte.
- Pipeline RAG qui envoie beaucoup de chunks redondants ou de JSON structuré.
- Réduire la facture de tokens **sans toucher au code** de l'application (mode proxy).
- Besoin de garantir que rien n'est perdu : le modèle peut toujours redemander l'original.

## Quand NE PAS l'utiliser

- Problème de **routage** ou d'abstraction multi-fournisseurs, pas de volume : c'est le rôle d'une passerelle comme [[Dev/Services/LiteLLM|LiteLLM]].
- Besoin de **mesurer** ce qui est envoyé plutôt que de le réduire → outils d'observabilité LLM (cf. [[Comparatif - Observabilité LLM]]).
- Contexte déjà court et maîtrisé : une brique de plus dans le chemin critique pour un gain marginal.
- Contraintes de latence dures : la compression ajoute une étape avant chaque appel.

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; s'exécute **en local**, aucune donnée sortante ajoutée par la brique elle-même.
- `pip install "headroom-ai[all]"`, `uv tool install`, `npm install headroom-ai`, ou image `ghcr.io/headroomlabs-ai/headroom`.
- Mode proxy = un processus à superviser sur le poste ou le serveur applicatif (single-node).
- Intégration [[Dev/Services/LiteLLM|LiteLLM]] par callback : `litellm.callbacks = [HeadroomCallback()]`.
- Le cache des originaux occupe du disque et contient le contexte brut — à traiter comme une donnée sensible.

## Pièges

- **Chiffres auto-déclarés** : les 60-95 % concernent du JSON, cas le plus favorable ; sur du texte ou du code, l'ordre de grandeur annoncé tombe à 15-20 %.
- La compression **change le prompt** : tout jugement de qualité doit être rejoué après activation, pas supposé stable.
- Le gain net dépend du **taux de récupération** : un modèle qui appelle souvent `headroom_retrieve` annule l'économie.
- **Pré-1.0** à cadence de release élevée, sur un chemin critique — épingler la version.
- Le mode `wrap` dépend de l'assistant ciblé ; la matrice d'intégrations bouge, se référer au dépôt plutôt qu'à une liste figée.

## Alternatives

Aucune brique équivalente n'est référencée dans le brain à ce jour : la catégorie `llm/context` est neuve et Headroom y est seul.

## Liens

- S'intègre à [[Dev/Services/LiteLLM|LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[Context engineering]] — concept : composition et budget du contexte
- [[Harnais d'agent]] — concept : ce qui entoure le modèle dans une boucle d'agent
- [[Agent memory]] — concept : persistance du contexte entre sessions
- [[Tokenization]] — concept : l'unité que l'on cherche à économiser
- [[mcp-protocol]] — concept : le protocole par lequel Headroom expose ses outils
- Doc : https://headroom-docs.vercel.app/docs
