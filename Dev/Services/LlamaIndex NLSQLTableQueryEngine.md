---
galaxie: dev
type: service
nom: LlamaIndex NLSQLTableQueryEngine
alias: [nlsqltablequeryengine, llamaindex text-to-sql, llamaindex sql, SQLTableRetrieverQueryEngine, llamaindex nl2sql]
pitch: "Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle."
categorie: llm/framework-module
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LangChain SQL agent|LangChain SQL agent]]"]
remplace_par: []
status: actif
tags: [text-to-sql, llm, rag, retrieval]
url_docs: https://developers.llamaindex.ai/python/examples/index_structs/struct_indices/sqlindexdemo/
url_repo: https://github.com/run-llama/llama_index
---

# LlamaIndex NLSQLTableQueryEngine

## Pourquoi

Sous-composant text-to-SQL de [[Dev/Services/LlamaIndex|LlamaIndex]] — pas un produit dédié, un **query engine** intégré au framework. On lui passe un objet `SQLDatabase` (via SQLAlchemy) et des noms de tables ; il introspecte le schéma, fait générer le SQL par le LLM, l'exécute, puis **synthétise une réponse** en langage naturel à partir du résultat. Pour un schéma trop gros pour tenir dans le prompt, sa variante `SQLTableRetrieverQueryEngine` indexe les tables (ObjectIndex + embeddings) et **récupère d'abord les tables pertinentes** avant de générer. C'est le text-to-SQL « batteries incluses » de LlamaIndex, aligné sur son moteur d'indexation et de retrieval.

## Quand l'utiliser

- LlamaIndex est **déjà le socle** de l'application (RAG documentaire, agents data) : on branche le SQL dans le même framework.
- Gros schéma : la variante `SQLTableRetrieverQueryEngine` gère le cas où toutes les tables ne rentrent pas dans le prompt.
- Besoin d'une **réponse en langage naturel** synthétisée (pas juste le tableau de résultats).

## Quand NE PAS l'utiliser

- Recherche d'un produit dédié avec UI et entraînement d'exemples clé en main → [[Dev/Services/Vanna|Vanna]] ou [[Dev/Services/WrenAI|WrenAI]].
- Stack déjà en LangChain → son [[Dev/Services/LangChain SQL agent|SQL agent]], même logique dans l'autre écosystème.
- Besoin d'une boucle agent riche (correction itérative, multi-outils) plus poussée que le query engine.

## Déploiement & coût

- **Self-host** : s'exécute dans l'application Python qui embarque LlamaIndex (MIT). Pas d'infra propre ; LLM au choix, dont local (Ollama). La variante retriever ajoute un magasin d'embeddings pour l'index des tables.
- Compte base **lecture seule** requis (le moteur exécute le SQL généré).

## Pièges

- **Risque d'exécution** : le query engine lance du SQL produit par le LLM. Scoper les droits, borner les résultats.
- Sur gros schéma sans la variante retriever, le prompt explose : passer à `SQLTableRetrieverQueryEngine`.
- Pas de couche sémantique métier : le moteur voit le schéma physique. La qualité dépend des descriptions de tables/colonnes fournies.

## Alternatives

- [[Dev/Services/LangChain SQL agent|LangChain SQL agent]] — Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle.

## Liens

- [[Dev/Services/LlamaIndex|LlamaIndex]] — framework parent dont ce module fait partie.
- [[Text-to-SQL]] — concept : traduire une question en langage naturel en SQL exécutable.
- [[Dev/Patterns/Comparatif - Frameworks text-to-SQL|Comparatif - Frameworks text-to-SQL]]
- Docs : https://developers.llamaindex.ai/python/examples/index_structs/struct_indices/sqlindexdemo/
