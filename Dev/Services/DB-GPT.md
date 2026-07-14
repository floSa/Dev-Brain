---
galaxie: dev
type: service
nom: DB-GPT
alias: [dbgpt, db gpt, db-gpt, eosphoros db-gpt]
pitch: "Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Vanna|Vanna]]", "[[Dev/Services/WrenAI|WrenAI]]"]
remplace_par: []
status: actif
tags: [text-to-sql, llm, multi-agent, rag, fine-tuning]
url_docs: http://docs.dbgpt.cn
url_repo: https://github.com/eosphoros-ai/DB-GPT
---

# DB-GPT

## Pourquoi

DB-GPT est un framework open-source (MIT) pour bâtir des **agents data IA-natifs**. Au-delà du text-to-SQL, il vise l'analyse autonome : connexion à des bases et fichiers, question en langage naturel, génération de SQL puis analyse. Il s'appuie sur **AWEL** (Agentic Workflow Expression Language — langage d'expression de workflows agentiques propre au projet), du **RAG**, un système **multi-agents**, et le support multi-modèles (LLaMA, Qwen, ChatGLM… en local ou via API). Il embarque aussi une capacité de **fine-tuning Text2SQL** pour spécialiser un modèle sur son propre schéma. Très complet, écrit en Python, activement développé (v0.8+, cadence de releases soutenue).

## Quand l'utiliser

- Aller **au-delà d'une requête** : pipelines d'analyse autonomes, agents data, applications data IA-natives.
- Requêtes complexes où un **découpage multi-agent** (planification / exécution / vérification) aide.
- Volonté de **fine-tuner** un modèle Text2SQL sur son domaine plutôt que de rester en pur RAG.

## Quand NE PAS l'utiliser

- Besoin simple et rapide : la courbe d'apprentissage (AWEL + framework d'agents + pipeline) est raide → [[Dev/Services/Vanna|Vanna]].
- Équipe métier voulant une UI de BI gouvernée clé en main → [[Dev/Services/WrenAI|WrenAI]].
- Petite équipe sans temps d'appropriation de l'écosystème DB-GPT.

## Déploiement & coût

- **Self-host** Python (MIT). Déploiement mono-nœud par défaut ; un mode cluster (contrôleur + workers de modèles) existe pour distribuer le serving. LLM local ou API.
- Pas d'offre hébergée officielle : tout repose sur l'auto-hébergement.
- Le fine-tuning Text2SQL demande du GPU (une L4 24 Go suffit pour de petits modèles) ; l'inférence d'un 7B quantifié tourne sur une config modeste.

## Pièges

- **Coût conceptuel élevé** : maîtriser AWEL, le framework d'agents, le multi-model (SMMF) et le pipeline Text2SQL avant d'être productif.
- Documentation partiellement centrée sur l'écosystème d'origine (docs.dbgpt.cn) ; couverture inégale selon les modules.
- Périmètre large = surface à maintenir ; risque de sur-outiller un besoin simple.

## Alternatives

- [[Dev/Services/Vanna|Vanna]] — Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.
- [[Dev/Services/WrenAI|WrenAI]] — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.

## Liens

- [[Text-to-SQL]] — concept parent : traduire une question en langage naturel en SQL exécutable.
- [[Dev/Patterns/Comparatif - Frameworks text-to-SQL|Comparatif - Frameworks text-to-SQL]]
- Repo : https://github.com/eosphoros-ai/DB-GPT · Docs : http://docs.dbgpt.cn
