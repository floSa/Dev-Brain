---
galaxie: dev
type: service
nom: Vanna
alias: [vanna, vanna.ai, vanna-ai]
pitch: "Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/WrenAI|WrenAI]]", "[[Dev/Services/DB-GPT|DB-GPT]]"]
remplace_par: []
status: abandonne
tags: [text-to-sql, llm, rag, agents, local-llm]
url_docs: https://vanna.ai/docs/
url_repo: https://github.com/vanna-ai/vanna
---

# Vanna

## Pourquoi

Vanna génère du SQL à partir de questions en langage naturel par **RAG** (Retrieval-Augmented Generation — génération augmentée par récupération de contexte). On l'« entraîne » sur trois matières : le **DDL** (Data Definition Language — les `CREATE TABLE` qui décrivent le schéma), de la documentation métier, et des paires question→SQL validées. À l'exécution, il récupère schéma et exemples pertinents, les injecte dans le prompt, puis demande au LLM de produire la requête. Agnostique de la base (Postgres, MySQL, Snowflake, DuckDB…) et du LLM (OpenAI, Anthropic, **Ollama en local**, Gemini, Bedrock, Mistral…). Longtemps la référence open-source du domaine (~23k étoiles). Vanna 2.0 (fin 2025) réécrit l'API autour d'un agent « user-aware » : permissions, streaming, UI web `<vanna-chat>` intégrée.

## Quand l'utiliser

- Embarquer une brique text-to-SQL **dans une app Python** custom, sans plateforme lourde.
- Cible **on-prem** avec LLM local : le backend Ollama évite tout appel cloud.
- Prototyper vite : quelques appels `train()` sur le DDL + des exemples suffisent à démarrer.

## Quand NE PAS l'utiliser

- Besoin d'un produit clé en main avec UI, gouvernance et couche sémantique métier → [[Dev/Services/WrenAI|WrenAI]].
- Exigence d'un **OSS activement maintenu** : le dépôt est archivé depuis mars 2026 (cf. Pièges) → [[Dev/Services/WrenAI|WrenAI]] ou [[Dev/Services/DB-GPT|DB-GPT]].
- Requêtes analytiques très complexes nécessitant une décomposition multi-agent → [[Dev/Services/DB-GPT|DB-GPT]].

## Déploiement & coût

- **Self-host** : bibliothèque Python (MIT) + un magasin de vecteurs pour les données d'entraînement (ChromaDB, Qdrant, pgvector…) + un LLM au choix. Tourne sur un seul nœud ; un 7B quantifié via Ollama suffit à tester en local.
- **Vanna Cloud** : version hébergée payante, seule voie désormais officiellement maintenue par l'éditeur (donc hors périmètre on-prem).

## Pièges

- **OSS archivé le 29 mars 2026** : dépôt en lecture seule, plus de correctifs upstream. Le code MIT reste forkable, mais forker = hériter de la maintenance. Décision structurante pour un produit à maintenir dans la durée.
- La qualité dépend directement de l'entraînement : DDL complet + bons exemples question/SQL. Schéma mal décrit → SQL faux.
- Pas de couche sémantique métier : Vanna voit le schéma physique, pas les définitions de métriques (contrairement à WrenAI).
- Le magasin de vecteurs devient une dépendance à opérer (persistance, sauvegarde).

## Alternatives

- [[Dev/Services/WrenAI|WrenAI]] — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.
- [[Dev/Services/DB-GPT|DB-GPT]] — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.

## Liens

- [[Text-to-SQL]] — concept parent : traduire une question en langage naturel en SQL exécutable.
- [[Dev/Patterns/Comparatif - Frameworks text-to-SQL|Comparatif - Frameworks text-to-SQL]]
- Repo : https://github.com/vanna-ai/vanna · Docs : https://vanna.ai/docs/
