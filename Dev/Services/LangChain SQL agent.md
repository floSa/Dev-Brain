---
galaxie: dev
type: service
nom: LangChain SQL agent
alias: [langchain sql, langchain text-to-sql, create_sql_agent, SQLDatabaseToolkit, langgraph sql agent]
pitch: "Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle."
categorie: llm/framework-module
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LlamaIndex NLSQLTableQueryEngine|LlamaIndex NLSQLTableQueryEngine]]"]
remplace_par: []
status: actif
tags: [text-to-sql, llm, agents, tool-use]
url_docs: https://docs.langchain.com/oss/python/integrations/tools/sql_database
url_repo: https://github.com/langchain-ai/langchain
---

# LangChain SQL agent

## Pourquoi

Sous-composant text-to-SQL de [[Dev/Services/LangChain|LangChain]] — pas un produit dédié, un **assemblage** de briques du framework. On combine un wrapper `SQLDatabase` (via SQLAlchemy), un `SQLDatabaseToolkit` (outils : lister les tables, lire le schéma, exécuter, vérifier une requête) et un agent. L'agent **boucle** : inspecter le schéma → écrire le SQL → l'exécuter → se corriger sur erreur → re-générer. La voie historique `create_sql_agent` cède la place à un agent construit en **LangGraph** (graphe explicite, traçable). Une variante sans agent, `create_sql_query_chain`, génère juste le SQL en un passage.

## Quand l'utiliser

- LangChain (ou LangGraph) est **déjà le socle** de l'application : on reste dans un seul framework.
- Besoin de **contrôle total** sur la boucle agent (outils, prompts, validation) plutôt qu'un produit clé en main.
- Schéma où la boucle inspecter → corriger apporte de la robustesse.

## Quand NE PAS l'utiliser

- Recherche d'un produit dédié avec entraînement RAG et UI fournis → [[Dev/Services/Vanna|Vanna]] ou [[Dev/Services/WrenAI|WrenAI]].
- Stack déjà en LlamaIndex → son [[Dev/Services/LlamaIndex NLSQLTableQueryEngine|NLSQLTableQueryEngine]], plus direct.
- Refus de câbler soi-même la récupération d'exemples / le contexte de schéma.

## Déploiement & coût

- **Self-host** : s'exécute dans l'application Python qui embarque LangChain (MIT). Aucune infra propre ; LLM au choix, dont local (Ollama). Coût = celui du framework parent + les appels LLM.
- Un compte base **lecture seule** est indispensable (l'agent exécute du SQL généré).

## Pièges

- **Risque d'exécution** : l'agent lance du SQL produit par le LLM. Scoper les droits au strict minimum, borner (`LIMIT`, timeout).
- Assemblage à maintenir : la surface d'API LangChain bouge (migration vers LangGraph pour les agents).
- Pas de couche sémantique ni de « training » d'exemples clé en main : la qualité dépend du contexte qu'on injecte soi-même.

## Alternatives

- [[Dev/Services/LlamaIndex NLSQLTableQueryEngine|LlamaIndex NLSQLTableQueryEngine]] — Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle.

## Liens

- [[Dev/Services/LangChain|LangChain]] — framework parent dont ce module fait partie.
- [[Text-to-SQL]] — concept : traduire une question en langage naturel en SQL exécutable.
- [[Dev/Patterns/Comparatif - Frameworks text-to-SQL|Comparatif - Frameworks text-to-SQL]]
- Docs : https://docs.langchain.com/oss/python/integrations/tools/sql_database
