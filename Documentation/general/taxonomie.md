---
galaxie: meta
nom: taxonomie
type: gouvernance
created: 2026-06-04
modified: 2026-06-11
tags: [meta, gouvernance, taxonomie]
---

# Taxonomie — catégories autorisées

Valeurs autorisées pour le champ `categorie:` du frontmatter. Une page dont la catégorie n'est pas dans cette liste n'est pas valide. Catégorie manquante → **demander avant d'inventer**.

## Services Dev (`Dev/Services/`) — `categorie: <domaine>/<sous-domaine>`

```
database/{relational, document, keyvalue, vector, timeseries, graph, warehouse, columnar, search, wide-column, driver}
framework/{backend, frontend, fullstack, mobile, orm}
ui/{data-app, ml-demo}
language/{general, runtime}
devops/{ci, iac, container, orchestration}
llm/{api, local, framework, framework-module, eval, embeddings, finetuning, observability, guardrails}
ml/{tracking, training, serving, hyperopt, orchestration, framework,
    feature-store, monitoring, annotation, optimization, quantization, eval}
data/{orchestration, parsing, ingestion, format, quality,
      transformation, streaming, lakehouse, versioning, scraping}
automation/{workflow, ipaas, ai-agent}
compute/distributed
auth
storage
observability/{log, metric, trace}
tooling/{lint, format, build, test, package, data, viz, stats, notebook, migration, db-admin, optim, api, code-assistant, media, diagram, design}
```

- `database/driver` — pilote / adaptateur bas niveau d'accès à une base (DB-API 2.0, wrapper libpq) : psycopg2, asyncpg, psycopg 3. Distinct de `framework/orm` (mapping objet) : le driver transporte le SQL, il n'abstrait pas le schéma.
- `data/scraping` — récupération de données depuis des pages web : clients HTTP furtifs (empreinte TLS), navigateurs headless, contournement d'anti-bot, parsing HTML. Distinct de `data/ingestion` (connecteurs ELT vers des sources structurées / API).
- `automation/*` — automatisation no-code / orchestration de workflows applicatifs : connecter des applications et services via déclencheurs et actions, généralement par éditeur visuel de nœuds. **Distinct de `data/orchestration`** (Airflow, Dagster, Prefect…) qui orchestre des pipelines de **données** (DAG, dépendances, backfills) en code. Sous-domaines :
  - `automation/workflow` — moteurs d'automatisation de workflows self-hostables, orientés intégration d'apps et tâches techniques (n8n, Activepieces, Windmill).
  - `automation/ipaas` — plateformes SaaS d'intégration entre applications (iPaaS), entièrement managées (Zapier).
  - `automation/ai-agent` — automatisation no-code dont chaque étape peut porter de la logique IA / agents (gumloop).
- `tooling/optim` — recherche opérationnelle / programmation mathématique : modélisation et résolution de problèmes d'optimisation (LP, MIP, optimisation convexe) via des solveurs ; modeleurs Python (PuLP, Pyomo, CVXPY) et bindings de solveurs. Distinct de `ml/optimization` (compression / optimisation de modèles ML) et de `tooling/stats` (modélisation statistique).
- `ml/eval` — bibliothèques de calcul de métriques et de validation de modèles ML (accuracy, F1, BLEU, ROUGE, exact match…) : HuggingFace `evaluate`, jeux de métriques réutilisables. Distinct de `llm/eval` (évaluation de systèmes LLM/RAG/agents — faithfulness, scoring par juge) et du concept transverse `model-evaluation` (le tag).
- `llm/framework-module` — **sous-composant notable d'un gros framework LLM** (LangChain, LlamaIndex…) qui mérite sa page dédiée parce que le framework parent est trop vaste pour le mettre en avant : p. ex. le SQL agent de LangChain, le NLSQLTableQueryEngine de LlamaIndex. Ce n'est **pas** une brique déployable seule (elle s'utilise via son framework parent, qu'elle référence dans ses liens), d'où la distinction avec `llm/framework` — et l'exclusion des comparatifs de frameworks. Fiche `type: service`, `licence_type`/`langage` hérités du parent.

## Outils Dev (`Dev/Outils/`) — `categorie: tooling/<famille>`

Outils techniques que l'on **utilise** (clients GUI, CLI, utilitaires) — par opposition aux services que l'on **déploie** (`Dev/Services/`). Même galaxie `dev` : tout ce qui est technique vit dans Dev.

- `db-admin` — clients GUI et outils d'administration de bases (DBeaver, pgAdmin, Compass…)
- `api` — clients d'API : composer, envoyer et tester des requêtes HTTP/REST/GraphQL/gRPC, gérer collections et environnements (Postman, Bruno, Insomnia…). Distinct de `tooling/test` (frameworks de test de code, type pytest).
- `code-assistant` — assistants IA de codage intégrés à l'éditeur ou au terminal : complétion, chat, édition multi-fichiers, mode agent (Continue, Aider, Cline…). Distinct des frameworks d'apps LLM (`llm/framework`) : ce sont des outils que l'on utilise, pas des briques que l'on déploie.
- `media` — ingestion / traitement de médias (vidéo, audio, image) pour donner à un assistant IA un input multimodal : téléchargement, extraction de frames, transcription (claude-video/`watch`…). Distinct de `code-assistant` (assistance au codage) et de `data/*` (données structurées / ELT).
- `diagram` — outils de création de **diagrammes et schémas** (flowcharts, UML, réseau, isométrique, whiteboard) : éditeurs GUI (draw.io, FossFLOW, Excalidraw) comme approches diagram-as-code (Mermaid). Distinct de `tooling/viz` (visualisation de **données**) : ici on dessine des schémas, pas des graphiques de données.
- `design` — outils de **design d'interface et de prototypage** UI/UX (Figma, Penpot) : maquettes, prototypes interactifs, systèmes de composants. Distinct de `diagram` (schémas techniques) : ici on conçoit des interfaces produit.

## Concepts Wiki (`Wiki/Concepts/`) — `categorie: concept/<sous-domaine>`

```
concept/{data, ai, ml, dl, rl, ts, nlp, signal, stats, math, devops, llm}
```

- `dl` — deep learning (architectures, attention, génératif)
- `rl` — reinforcement learning
- `ts` — séries temporelles & forecasting
- `nlp` — traitement du langage naturel (TF-IDF, NER, recherche d'information)
- `signal` — traitement du signal (Fourier, ondelettes, spectrogrammes)

> Dérivé du réservoir Wiki v1 + spec brain-v2 (§5.2 : `concept/data`). À valider / étendre.

## Skills Wiki (`Wiki/Outils/`) — `categorie: skill/<famille>`

> Réservé aux **skills / extensions** liés à la pratique perso (Claude Code, Obsidian, MCP). Les **outils techniques** (clients GUI, CLI, BDD, frameworks) ne sont PAS ici — ils vivent dans `Dev/` (cf. *Outils Dev* ci-dessus). Section vide en v2 tant qu'aucun skill n'est documenté.

```
skill/{documents, dev-flow, code-quality, knowledge, data, meta}
```

- `documents` — manipulation PDF, XLSX, DOCX, PPTX
- `dev-flow` — bootstrap, init, package mgmt, API SDK, GitHub
- `code-quality` — review, security, lint, refactor
- `knowledge` — Obsidian, scraping, ingestion de contenu
- `data` — accès DB, query, exploration (skills / connecteurs)
- `meta` — skills sur les skills (creator, eval, debug)

## Champ `domaines:`

Vocabulaire des grandes thématiques transverses → cf. [[themes]] (`data-sci`, `data-eng`, `mlops`, `ml-eng`, `ai-eng`).
