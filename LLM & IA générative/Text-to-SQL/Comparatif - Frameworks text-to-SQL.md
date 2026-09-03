---
role: comparatif
nom: Comparatif - Frameworks text-to-SQL
categorie: llm/text-to-sql
tags: [text-to-sql, rag, agents]
---

# Comparatif - Frameworks text-to-SQL

> On tranche sur : ce sur quoi le modèle raisonne — le schéma physique ou une couche sémantique métier — et sur ce qu'on livre : une brique dans une app Python, ou une UI pour une équipe.

![[Comparatif - Frameworks text-to-SQL.base]]

## Ce qui départage

- [[WrenAI]] — le seul à poser une **couche sémantique** : MDL, des fichiers versionnés qui encodent entités, relations, métriques et contrôle d'accès ligne/colonne, sur lesquels l'agent raisonne plutôt que sur le schéma brut. C'est sa valeur et son coût d'entrée — le MDL est à écrire et à maintenir, et mal modélisé il n'apporte rien.
- [[Vanna]] — la brique **à embarquer** : on l'« entraîne » sur le DDL, la doc et des paires question→SQL, agnostique de la base et du LLM — backend **Ollama** compris, donc utilisable sans aucun appel cloud. Critère décisif de cycle de vie : le dépôt OSS est **archivé depuis le 29 mars 2026**, forkable mais sans correctifs upstream.
- [[DB-GPT]] — le plus large : **multi-agent** avec son propre langage de workflow AWEL, et le seul du lot à embarquer le **fine-tuning Text2SQL** pour spécialiser un modèle sur son schéma. Le prix est un coût conceptuel élevé — AWEL, framework d'agents et pipeline à maîtriser avant d'être productif.
- [[LangChain SQL agent]] — pas un produit mais un **assemblage** : `SQLDatabase` + `SQLDatabaseToolkit` + un agent qui **boucle** — inspecter le schéma, écrire, exécuter, se corriger sur erreur. À prendre quand LangChain (ou LangGraph) est déjà le socle ; sinon c'est du câblage à maintenir, sans exemples ni couche sémantique fournis.
- [[LlamaIndex NLSQLTableQueryEngine]] — le même arbitrage dans l'autre écosystème, mais en **query engine** et non en boucle d'agent : il génère, exécute, puis **synthétise une réponse** en langage naturel. Son atout propre est `SQLTableRetrieverQueryEngine`, qui indexe les tables et récupère les pertinentes quand le schéma ne tient pas dans le prompt.
