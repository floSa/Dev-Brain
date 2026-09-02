---
role: hub
nom: Text-to-SQL
alias: [text to sql, nl2sql, natural language to sql, texte vers SQL, requête en langage naturel]
pitch: Traduire une question en langage naturel en SQL exécutable — le point dur est le SQL sémantiquement juste, pas le SQL valide.
domaines: [ai-eng]
tags: [text-to-sql, llm, rag, agents, benchmark]
---

# Text-to-SQL

> Traduire une question en langage naturel en SQL exécutable — le point dur est le SQL sémantiquement juste, pas le SQL valide.

## Aperçu

- Traduire une question en **langage naturel** en une requête **SQL exécutable** sur une base relationnelle (aussi appelé NL2SQL — Natural Language to SQL). But : ouvrir l'accès aux données sans écrire de SQL à la main.
- Le point dur n'est pas de produire du SQL syntaxiquement correct, mais du SQL **sémantiquement juste** : bonnes tables, bonnes jointures, bonne interprétation métier de la question.

## Concepts clés

### Le schéma est le contexte
- Un LLM ne connaît pas la base cible. Il faut lui fournir le **DDL** (Data Definition Language — les `CREATE TABLE`), des descriptions de colonnes, des exemples de valeurs, parfois des paires question/SQL validées. La qualité du SQL plafonne à celle de ce contexte.
- Gros schéma → ne rentre pas dans le prompt : on **récupère d'abord les tables pertinentes** (retrieval de schéma) avant de générer.

### Deux écoles pour fournir le contexte
- **Retrieval / RAG** : récupérer schéma et exemples similaires puis les injecter dans le prompt ([[Vanna]]). Rapide à mettre en place, s'améliore en ajoutant des exemples.
- **Couche sémantique** : décrire le modèle métier (entités, relations, métriques) au-dessus du schéma physique pour que le LLM raisonne en concepts métier ([[WrenAI]] et son MDL). Plus long à poser, plus robuste sur les définitions métier partagées.

### Génération simple vs agent
- **Chaîne simple** : question → SQL en un seul passage (le NLSQLTableQueryEngine de [[LlamaIndex]], `create_sql_query_chain` de [[LangChain]]). Suffit sur schémas simples.
- **Agent** : boucle inspecter le schéma → écrire → exécuter → corriger sur erreur → re-générer. Plus robuste sur schémas complexes (SQL agent de LangChain/LangGraph, multi-agent de [[DB-GPT]]).

### Multi-candidat + sélection (l'état de l'art)
- Les meilleurs systèmes génèrent **plusieurs** SQL candidats sous des angles différents, puis un sélecteur départage (CHASE-SQL, Agentar-Scale-SQL). Le SQL d'un seul passage plafonne ; c'est le vote entre candidats qui fait gagner les derniers points.

## Les maths, simplement

- Métrique de référence : **Execution Accuracy (EX)** — le SQL prédit $\hat q$ est compté juste si son résultat d'exécution égale celui du SQL de référence $q^{*}$ (tolère un SQL différent mais sémantiquement équivalent). Sur $N$ questions : $EX = \frac{1}{N}\sum_i \mathbb{1}\big[\text{result}(\hat q_i) = \text{result}(q_i^{*})\big]$.
- Bancs d'essai : **Spider** (multi-domaine, schémas variés) et **BIRD** (données réelles, plus dur). Le SOTA sur BIRD plafonne autour de **77-82 %** d'EX, et seulement avec des architectures multi-candidat (cf. [[LLM benchmarks]]).

## En pratique

- **Exécuter en lecture seule** et borner (compte read-only, `LIMIT`, timeout) : un LLM peut générer un `DELETE` ou une requête qui écroule la base.
- Fournir de bons exemples question/SQL est le levier n°1 de qualité. Quelques exemples bien choisis valent mieux qu'un gros prompt générique.
- **Valider avant d'exécuter** (dry-run / `EXPLAIN`) et boucler sur l'erreur : le pattern agent (générer → exécuter → corriger) rattrape beaucoup d'échecs (cf. [[Agent patterns]]).
- Choisir la brique selon le besoin (cf. section suivante) : bibliothèque embarquée, plateforme à couche sémantique, ou module d'un framework déjà en place.
- Piège : croire qu'un modèle plus gros suffit. Le **contexte** (schéma + sémantique) et la **boucle de correction** pèsent plus que la taille du modèle.

## Approches voisines & alternatives

- **Frameworks dédiés** : [[Vanna]] (RAG, OSS archivé mais forkable), [[WrenAI]] (couche sémantique / GenBI), [[DB-GPT]] (multi-agent). Panorama : [[Comparatif - Frameworks text-to-SQL]].
- **Modules de frameworks généralistes** : [[LlamaIndex NLSQLTableQueryEngine]] (+ variante SQLTableRetrieverQueryEngine) et [[LangChain SQL agent]] — briques text-to-SQL internes à [[LlamaIndex]] / [[LangChain]], à privilégier quand le framework est déjà en place (des modules, pas des produits dédiés).
- **Modèles spécialisés** à héberger : SQLCoder (Defog), Arctic-Text2SQL-R1 (Snowflake), Qwen2.5-Coder — le moteur de génération, pas l'orchestration.
- **RAG** : le text-to-SQL par retrieval est un cas particulier de [[RAG]] (on récupère du schéma et des exemples au lieu de passages de texte).
- **Managé** (hors on-prem) : Snowflake Cortex Analyst, Databricks Genie — couplés à leur plateforme.

## Pour aller plus loin

- Benchmarks : Spider (Yale, 2018) et BIRD (2023) — EX comme métrique de référence.
- CHASE-SQL (Google, 2024) et Agentar-Scale-SQL (2025) — génération multi-candidat + sélection, tête du classement BIRD.
- Sujets liés : [[RAG]], [[Agent patterns]], [[LLM benchmarks]].

<!-- AUTO:START -->
### Briques
- [[DB-GPT]] — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.
- [[LangChain SQL agent]] — Module text-to-SQL de LangChain : agent qui inspecte le schéma, écrit le SQL, l'exécute et se corrige en boucle (SQLDatabaseToolkit + create_sql_agent, aujourd'hui via LangGraph) ; brique à assembler soi-même, pas un produit clé en main, à privilégier si LangChain est déjà le socle.
- [[LlamaIndex NLSQLTableQueryEngine]] — Module text-to-SQL de LlamaIndex : query engine qui introspecte le schéma, fait générer le SQL, l'exécute et synthétise la réponse ; variante SQLTableRetrieverQueryEngine pour récupérer les tables pertinentes des gros schémas ; brique intégrée, à privilégier si LlamaIndex est déjà le socle.
- [[Vanna]] — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- [[WrenAI]] — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.

### Comparatifs
- [[Comparatif - Frameworks text-to-SQL]]
<!-- AUTO:END -->
