---
role: brique
nom: LlamaIndex NLSQLTableQueryEngine
alias: [nlsqltablequeryengine, llamaindex text-to-sql, llamaindex sql, SQLTableRetrieverQueryEngine, llamaindex nl2sql]
pitch: "Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle."
categorie: llm/text-to-sql
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LangChain SQL agent]]"]
complements: ["[[LlamaIndex]]"]
tags: [text-to-sql, llm, rag, retrieval]
url_docs: https://developers.llamaindex.ai/python/examples/index_structs/struct_indices/sqlindexdemo/
url_repo: https://github.com/run-llama/llama_index
---

# LlamaIndex NLSQLTableQueryEngine

<!-- AUTO:BANDEAU:START -->
> Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Sous-composant text-to-SQL de [[LlamaIndex]] : pas un produit dédié, un **query engine**
intégré au framework. On lui passe un objet `SQLDatabase` (via SQLAlchemy) et des noms de
tables ; il introspecte le schéma, fait générer le SQL par le LLM, l'exécute, puis
**synthétise une réponse en langage naturel** à partir du résultat — et non un simple tableau.
Pour un schéma trop gros pour tenir dans le prompt, la variante
`SQLTableRetrieverQueryEngine` indexe les tables (ObjectIndex et embeddings) et récupère
d'abord les tables pertinentes avant de générer. C'est le text-to-SQL « batteries incluses »
de LlamaIndex, aligné sur son moteur d'indexation et de retrieval.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| LlamaIndex est déjà le socle de l'application — RAG documentaire, agents data : on branche le SQL dans le même framework | Risque d'exécution : le query engine lance du SQL produit par le LLM — scoper les droits, borner les résultats |
| Gros schéma : `SQLTableRetrieverQueryEngine` traite le cas où toutes les tables ne rentrent pas dans le prompt | Sur gros schéma sans la variante retriever, le prompt explose : il faut passer à `SQLTableRetrieverQueryEngine` |
| Vouloir une réponse en langage naturel synthétisée, et pas seulement le tableau de résultats | Aucune couche sémantique métier : le moteur voit le schéma physique, et la qualité dépend des descriptions de tables et de colonnes fournies |
| | C'est un query engine, pas une boucle d'agent : ni correction itérative, ni multi-outils |

## Mise en œuvre

- Installation — aucune : le module s'exécute dans l'application Python qui embarque déjà LlamaIndex
- Point d'entrée — un objet `SQLDatabase` et des noms de tables ; `SQLTableRetrieverQueryEngine` pour les gros schémas
- Prérequis — un compte base **en lecture seule**, le moteur exécutant du SQL généré ; un LLM au choix, dont local via Ollama ; un magasin d'embeddings si l'on passe par la variante retriever
- Exécution — mono-nœud, dans l'application hôte
- Coût — gratuit sous MIT ; aucune infra propre au-delà de celle de LlamaIndex

## Écosystème

### Alternatives

- [[LangChain SQL agent]] — Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle.

### Compléments

- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances. — le framework parent dont ce module fait partie : il ne s'utilise pas sans lui.

## Ressources

- Documentation — https://developers.llamaindex.ai/python/examples/index_structs/struct_indices/sqlindexdemo/
- Dépôt — https://github.com/run-llama/llama_index

## Voir aussi

- [[Text-to-SQL]] — la notion du dossier
- [[Comparatif - Frameworks text-to-SQL]] — ce qui départage les frameworks du dossier
