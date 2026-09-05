---
role: brique
nom: LangChain SQL agent
alias: [langchain sql, langchain text-to-sql, create_sql_agent, SQLDatabaseToolkit, langgraph sql agent]
pitch: "Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle."
categorie: llm/text-to-sql
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LlamaIndex NLSQLTableQueryEngine]]"]
complements: ["[[LangChain]]"]
tags: [text-to-sql, llm, agents, tool-use]
url_docs: https://docs.langchain.com/oss/python/integrations/tools/sql_database
url_repo: https://github.com/langchain-ai/langchain
---

# LangChain SQL agent

<!-- AUTO:BANDEAU:START -->
> Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Sous-composant text-to-SQL de [[LangChain]] : pas un produit dédié, un **assemblage** de
briques du framework. On combine un wrapper `SQLDatabase` (via SQLAlchemy), un
`SQLDatabaseToolkit` — lister les tables, lire le schéma, exécuter, vérifier une requête — et
un agent. L'agent **boucle** : inspecter le schéma, écrire le SQL, l'exécuter, se corriger sur
erreur, re-générer. La voie historique `create_sql_agent` cède la place à un agent construit
en [[LangGraph]], donc à graphe explicite et traçable. Une variante sans agent,
`create_sql_query_chain`, se contente de générer le SQL en un passage.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| LangChain ou LangGraph est déjà le socle de l'application : on reste dans un seul framework | Risque d'exécution : l'agent lance du SQL produit par le LLM — droits au strict minimum, `LIMIT` et timeout à poser |
| Vouloir le contrôle total de la boucle d'agent — outils, prompts, validation — plutôt qu'un produit clé en main | Assemblage à maintenir : la surface d'API LangChain bouge, les agents ayant migré vers LangGraph |
| Schéma où la boucle inspecter → corriger apporte de la robustesse | Ni couche sémantique ni « training » d'exemples fournis : la qualité dépend entièrement du contexte qu'on injecte soi-même |

## Mise en œuvre

- Installation — aucune : le module s'exécute dans l'application Python qui embarque déjà LangChain
- Point d'entrée — `SQLDatabase` + `SQLDatabaseToolkit` + un agent LangGraph ; ou `create_sql_query_chain` pour une génération en un passage
- Prérequis — un compte base **en lecture seule**, indispensable puisque du SQL généré est exécuté ; un LLM au choix, dont local via Ollama
- Exécution — mono-nœud, dans l'application hôte
- Coût — gratuit sous MIT ; le coût est celui du framework parent, plus les appels LLM

## Écosystème

### Alternatives

- [[LlamaIndex NLSQLTableQueryEngine]] — Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle.

### Compléments

- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith. — le framework parent dont ce module fait partie : il ne s'utilise pas sans lui.

## Ressources

- Documentation — https://docs.langchain.com/oss/python/integrations/tools/sql_database
- Dépôt — https://github.com/langchain-ai/langchain

## Voir aussi

- [[Text-to-SQL]] — la notion du dossier
- [[Comparatif - Frameworks text-to-SQL]] — ce qui départage les frameworks du dossier
