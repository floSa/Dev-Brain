---
role: brique
nom: Headroom
alias: [headroom, headroom-ai, headroomlabs]
pitch: "Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande."
categorie: llm/memoire
famille: paquet
licence_type: open-source
maturite: beta
langage: "Python, TypeScript, Rust"
alternatives: []
complements: []
tags: [llm, context-engineering, token-optimization, caching, mcp]
url_docs: https://headroom-docs.vercel.app/docs
url_repo: https://github.com/headroomlabs-ai/headroom
---

# Headroom

<!-- AUTO:BANDEAU:START -->
> Couche de compression de contexte locale et réversible (Apache-2.0) — comprime sorties d'outils, logs, fichiers et chunks RAG avant le modèle, en bibliothèque, en proxy, en enrobage d'agent ou en serveur MCP ; l'outil `headroom_retrieve` rend l'original récupérable à la demande.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python, TypeScript, Rust | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Le poste de dépense d'un agent n'est pas le prompt système, c'est ce que les outils
renvoient : sorties de commandes, logs, fichiers entiers, chunks de RAG. Headroom s'insère
**entre l'application et le modèle** et réécrit ce flux entrant sous une forme plus courte,
avant facturation. La propriété qui distingue l'approche est la **réversibilité** :
l'original reste côté local et le modèle reçoit un outil `headroom_retrieve` pour redemander
le contenu intégral quand la version comprimée ne suffit pas — la compression devient un pari
révocable, pas une perte définitive. Quatre modes d'insertion, du plus intrusif au moins :
bibliothèque, proxy transparent, enrobage d'agent, serveur MCP. Les gains annoncés — de
l'ordre de 15 à 20 % de tokens en moins sur un agent de code, 60 à 95 % sur du JSON verbeux —
sont **auto-déclarés par le projet**, sans mesure indépendante publiée : à revalider sur sa
propre charge avant d'en faire une hypothèse de budget.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Agent de code ou agent outillé dont les sorties d'outils saturent la fenêtre de contexte | Le problème est le routage ou l'abstraction multi-fournisseurs, pas le volume → [[LiteLLM]] |
| Pipeline RAG qui envoie beaucoup de chunks redondants ou de JSON structuré | Il s'agit de mesurer ce qui est envoyé plutôt que de le réduire → [[Comparatif - Observabilité LLM]] |
| Réduire la facture de tokens sans toucher au code de l'application, en mode proxy | Contexte déjà court et maîtrisé, ou contraintes de latence dures : une brique de plus dans le chemin critique pour un gain marginal |
| Garantir que rien n'est perdu : le modèle peut toujours redemander l'original | Le gain net dépend du taux de récupération — un modèle qui rappelle souvent l'original annule l'économie |
| | La compression **change le prompt** : tout jugement de qualité doit être rejoué après activation, jamais supposé stable |
| | Pré-1.0 à cadence de release élevée, sur un chemin critique : épingler la version |

## Mise en œuvre

- Installation — `pip install "headroom-ai[all]"`, `uv tool install`, `npm install headroom-ai`, ou l'image `ghcr.io/headroomlabs-ai/headroom`
- Point d'entrée — quatre modes : bibliothèque `compress(messages)` en Python ou TypeScript, proxy transparent `headroom proxy --port 8787`, enrobage `headroom wrap <assistant>` (la matrice d'assistants reconnus bouge, se référer au dépôt), serveur MCP exposant compression, récupération et statistiques
- Prérequis — le cache des originaux occupe du disque et contient le contexte brut : à traiter comme une donnée sensible
- Exécution — en local, aucune donnée sortante ajoutée par la brique elle-même ; le mode proxy est un processus à superviser, mono-nœud
- Coût — gratuit ; une intégration par callback existe côté passerelle (`litellm.callbacks = [HeadroomCallback()]`)

## Écosystème

### Alternatives

Aucune brique équivalente n'est référencée dans le brain à ce jour : la compression
réversible de contexte n'y a pas d'autre représentant.

## Ressources

- Documentation — https://headroom-docs.vercel.app/docs
- Dépôt — https://github.com/headroomlabs-ai/headroom

## Voir aussi

- [[Context engineering]] — la notion : composition et budget du contexte
- [[Agent memory]] — la notion : persistance du contexte entre sessions
- [[Harnais d'agent]] — la notion : ce qui entoure le modèle dans une boucle d'agent
- [[Tokenization]] — la notion : l'unité que l'on cherche à économiser
- [[mcp-protocol]] — la notion : le protocole par lequel il expose ses outils
- [[LLM & IA générative]] — le hub du domaine
