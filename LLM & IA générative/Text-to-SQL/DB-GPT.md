---
role: brique
nom: DB-GPT
alias: [dbgpt, db gpt, db-gpt, eosphoros db-gpt]
pitch: "Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python."
categorie: llm/text-to-sql
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Vanna]]", "[[WrenAI]]"]
complements: []
tags: [text-to-sql, llm, multi-agent, rag, fine-tuning]
url_docs: http://docs.dbgpt.cn
url_repo: https://github.com/eosphoros-ai/DB-GPT
---

# DB-GPT

<!-- AUTO:BANDEAU:START -->
> Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · mono-nœud | production | à jour · 2026-08-26 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework pour bâtir des **agents data IA-natifs**. Au-delà du text-to-SQL, il vise l'analyse
autonome : connexion à des bases et à des fichiers, question en langage naturel, génération de
SQL, puis analyse du résultat. Il repose sur **AWEL** (Agentic Workflow Expression Language),
un langage d'expression de workflows agentiques propre au projet, sur du RAG, sur un système
**multi-agents** et sur le support multi-modèles (LLaMA, Qwen, ChatGLM, en local ou via API).
Il est le seul de son dossier à embarquer une capacité de **fine-tuning Text2SQL**, pour
spécialiser un modèle sur son propre schéma. Développement actif, cadence de releases soutenue
(v0.8+).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Aller au-delà d'une requête : pipelines d'analyse autonomes, agents data, applications data IA-natives | Coût conceptuel élevé — AWEL, framework d'agents, multi-modèle SMMF et pipeline Text2SQL sont à maîtriser avant d'être productif ; une petite équipe sans temps d'appropriation n'y arrivera pas |
| Requêtes complexes où un découpage multi-agent — planification, exécution, vérification — aide | Documentation partiellement centrée sur l'écosystème d'origine (`docs.dbgpt.cn`), à couverture inégale selon les modules |
| Vouloir fine-tuner un modèle Text2SQL sur son domaine plutôt que de rester en pur RAG | Périmètre large, donc surface à maintenir : risque réel de sur-outiller un besoin simple |

## Mise en œuvre

- Installation — self-host Python ; il n'existe aucune offre hébergée officielle
- Point d'entrée — workflows AWEL, système multi-agents, connexions aux bases et aux fichiers
- Prérequis — un LLM local ou via API ; du GPU pour le fine-tuning Text2SQL, une L4 24 Go suffisant pour de petits modèles, l'inférence d'un 7B quantifié tenant sur une config modeste
- Exécution — mono-nœud par défaut ; un mode cluster (contrôleur et workers de modèles) distribue le serving
- Coût — gratuit sous MIT ; tout repose sur l'auto-hébergement

## Écosystème

### Alternatives

- [[Vanna]] — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- [[WrenAI]] — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.

## Ressources

- Documentation — http://docs.dbgpt.cn
- Dépôt — https://github.com/eosphoros-ai/DB-GPT

## Voir aussi

- [[Text-to-SQL]] — la notion du dossier
- [[Comparatif - Frameworks text-to-SQL]] — ce qui départage les frameworks du dossier
