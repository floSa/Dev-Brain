---
galaxie: dev
type: service
nom: WrenAI
alias: [wrenai, wren-ai, wren ai, wren]
pitch: "Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python, Rust
scaling: single-node
alternatives: ["[[Dev/Services/Vanna|Vanna]]", "[[Dev/Services/DB-GPT|DB-GPT]]"]
remplace_par: []
status: actif
tags: [text-to-sql, llm, agents, dashboard]
url_docs: https://docs.getwren.ai
url_repo: https://github.com/Canner/WrenAI
---

# WrenAI

## Pourquoi

WrenAI est une plateforme **GenBI** (Generative Business Intelligence — BI générative : produire tableaux de bord, graphiques et SQL à partir de questions en langage naturel). Sa thèse : le point dur du text-to-SQL n'est pas la récupération de schéma mais le fait que le LLM **ne comprend pas le métier**. D'où **MDL** (Modeling Definition Language — langage de définition de modèle) : des fichiers versionnés (Git-friendly) qui encodent modèles, colonnes, relations, vues, cubes, métriques, et contrôle d'accès ligne/colonne (RLAC/CLAC — Row/Column-Level Access Control). L'agent raisonne sur cette **couche sémantique**, pas seulement sur le schéma brut. Connecte 20+ sources (BigQuery, Snowflake, Postgres, ClickHouse, Redshift, Databricks, DuckDB…). Moteur en Rust (Wren Engine), services IA en Python.

## Quand l'utiliser

- Donner l'accès data à une **équipe** (10-20 personnes métier) via une UI clé en main, pas juste une lib.
- Contexte où la **sémantique métier** compte : métriques calculées, définitions partagées, langage cohérent.
- Secteurs régulés : contrôle d'accès fin (RLAC/CLAC) et couche sémantique auditable.

## Quand NE PAS l'utiliser

- Simple brique à embarquer dans une app Python → [[Dev/Services/Vanna|Vanna]].
- Refus de la surcharge d'une couche sémantique à modéliser (le MDL est à écrire et maintenir) → [[Dev/Services/Vanna|Vanna]].
- Besoin de fine-tuning de modèles Text2SQL ou de workflows agents très custom → [[Dev/Services/DB-GPT|DB-GPT]].

## Déploiement & coût

- **Self-host** : stack Docker (UI, service IA, Wren Engine, magasin de vecteurs). Tourne sur un seul nœud ; LLM au choix, dont local. Cœur **Apache-2.0** → commercialisable.
- **Wren AI Commercial** : version hébergée et maintenue, payante.
- Multi-licence à connaître : cœur Apache-2.0, docs CC-BY-4.0, AGPL-3.0 réservée à d'éventuels modules futurs — à surveiller en cas de redistribution.

## Pièges

- La couche sémantique MDL est un **investissement** : mal modélisée, elle n'apporte rien ; c'est le cœur de la valeur, mais aussi le coût d'entrée.
- Stack multi-services plus lourde à opérer qu'une simple bibliothèque (plusieurs conteneurs à superviser).
- Vérifier la licence des composants qu'on redistribue (le tag AGPL réservé aux modules futurs).

## Alternatives

- [[Dev/Services/Vanna|Vanna]] — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- [[Dev/Services/DB-GPT|DB-GPT]] — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.

## Liens

- [[Text-to-SQL]] — concept parent : traduire une question en langage naturel en SQL exécutable.
- [[Dev/Patterns/Comparatif - Frameworks text-to-SQL|Comparatif - Frameworks text-to-SQL]]
- Repo : https://github.com/Canner/WrenAI · Docs : https://docs.getwren.ai
