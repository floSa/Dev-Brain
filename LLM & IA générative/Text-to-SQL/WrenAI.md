---
role: brique
nom: WrenAI
alias: [wrenai, wren-ai, wren ai, wren]
pitch: "Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources."
categorie: llm/text-to-sql
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python, Rust
scaling: single-node
alternatives: ["[[Vanna]]", "[[DB-GPT]]"]
complements: []
tags: [text-to-sql, llm, agents, dashboard]
url_docs: https://docs.getwren.ai
url_repo: https://github.com/Canner/WrenAI
---

# WrenAI

<!-- AUTO:BANDEAU:START -->
> Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python, Rust | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme **GenBI** — *Generative Business Intelligence* : produire tableaux de bord,
graphiques et SQL à partir de questions en langage naturel. Sa thèse : le point dur du
text-to-SQL n'est pas la récupération du schéma, c'est que le LLM **ne comprend pas le
métier**. D'où **MDL** (Modeling Definition Language), des fichiers versionnés et
Git-friendly qui encodent modèles, colonnes, relations, vues, cubes, métriques et contrôle
d'accès ligne et colonne (RLAC/CLAC). L'agent raisonne sur cette **couche sémantique**, et non
sur le seul schéma brut. Plus de 20 sources sont connectées — BigQuery, Snowflake, Postgres,
ClickHouse, Redshift, Databricks, DuckDB. Moteur en Rust (Wren Engine), services IA en Python.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner l'accès data à une équipe métier de 10 à 20 personnes via une UI clé en main, et pas seulement une bibliothèque | La couche sémantique MDL est un investissement : elle est le cœur de la valeur, mais aussi le coût d'entrée — mal modélisée, elle n'apporte rien |
| Contexte où la sémantique métier compte : métriques calculées, définitions partagées, langage cohérent | Stack multi-services plus lourde à opérer qu'une bibliothèque : plusieurs conteneurs à superviser |
| Secteur régulé : contrôle d'accès fin RLAC/CLAC et couche sémantique auditable | Multi-licence à vérifier avant toute redistribution : cœur Apache-2.0, docs CC-BY-4.0, AGPL-3.0 réservée à d'éventuels modules futurs |

## Mise en œuvre

- Installation — stack Docker : UI, service IA, Wren Engine et magasin de vecteurs
- Point d'entrée — les fichiers MDL, versionnés dans Git, puis l'UI de questions et de tableaux de bord
- Prérequis — un LLM au choix, dont local ; les fichiers MDL à écrire et à maintenir avant tout usage sérieux
- Exécution — mono-nœud en self-host, ou Wren AI Commercial, la version hébergée et maintenue
- Coût — cœur Apache-2.0 gratuit, donc commercialisable ; l'offre hébergée est payante

## Écosystème

### Alternatives

- [[Vanna]] — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- [[DB-GPT]] — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.

## Ressources

- Documentation — https://docs.getwren.ai
- Dépôt — https://github.com/Canner/WrenAI

## Voir aussi

- [[Text-to-SQL]] — la notion du dossier
- [[Comparatif - Frameworks text-to-SQL]] — ce qui départage les frameworks du dossier
