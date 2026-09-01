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
llm/{api, local, framework, framework-module, app, context, eval, embeddings, finetuning, observability, guardrails}
ml/{tracking, training, serving, hyperopt, orchestration, framework,
    feature-store, monitoring, annotation, optimization, quantization, eval}
data/{orchestration, parsing, ingestion, format, quality,
      transformation, streaming, lakehouse, versioning, scraping}
automation/{workflow, ipaas, ai-agent}
compute/{distributed, sandbox, serverless}
auth
storage
network/{analysis, transfer}
security/{recon, osint}
observability/{log, metric, trace, infra}
tooling/{lint, format, build, test, package, data, viz, stats, notebook, migration, db-admin,
        optim, api, code-assistant, media, diagram, design, document, video, capture, llm}
```

- `database/driver` — pilote / adaptateur bas niveau d'accès à une base (DB-API 2.0, wrapper libpq) : psycopg2, asyncpg, psycopg 3. Distinct de `framework/orm` (mapping objet) : le driver transporte le SQL, il n'abstrait pas le schéma.
- `data/scraping` — récupération de données depuis des pages web : clients HTTP furtifs (empreinte TLS), navigateurs headless, contournement d'anti-bot, parsing HTML. Distinct de `data/ingestion` (connecteurs ELT vers des sources structurées / API).
- `automation/*` — automatisation no-code / orchestration de workflows applicatifs : connecter des applications et services via déclencheurs et actions, généralement par éditeur visuel de nœuds. **Distinct de `data/orchestration`** (Airflow, Dagster, Prefect…) qui orchestre des pipelines de **données** (DAG, dépendances, backfills) en code. Sous-domaines :
  - `automation/workflow` — moteurs d'automatisation de workflows self-hostables, orientés intégration d'apps et tâches techniques (n8n, Activepieces, Windmill).
  - `automation/ipaas` — plateformes SaaS d'intégration entre applications (iPaaS), entièrement managées (Zapier).
  - `automation/ai-agent` — automatisation no-code dont chaque étape peut porter de la logique IA / agents (gumloop).
- `compute/sandbox` — bacs à sable d'exécution de code **non fiable** (typiquement généré par un LLM) : isolation forte (microVM, kernel dédié), création et destruction à la demande, cycle de vie court. Distinct de `devops/container` (packaging et déploiement d'applications de confiance) et de `compute/distributed` (calcul réparti sur plusieurs nœuds).
- `compute/serverless` — plateformes de calcul à la demande facturées à l'usage, sans serveur à provisionner (scale-to-zero, démarrage à froid rapide, GPU inclus le cas échéant).
- `tooling/optim` — recherche opérationnelle / programmation mathématique : modélisation et résolution de problèmes d'optimisation (LP, MIP, optimisation convexe) via des solveurs ; modeleurs Python (PuLP, Pyomo, CVXPY) et bindings de solveurs. Distinct de `ml/optimization` (compression / optimisation de modèles ML) et de `tooling/stats` (modélisation statistique).
- `ml/eval` — bibliothèques de calcul de métriques et de validation de modèles ML (accuracy, F1, BLEU, ROUGE, exact match…) : HuggingFace `evaluate`, jeux de métriques réutilisables. Distinct de `llm/eval` (évaluation de systèmes LLM/RAG/agents — faithfulness, scoring par juge) et du concept transverse `model-evaluation` (le tag).
- `llm/framework-module` — **sous-composant notable d'un gros framework LLM** (LangChain, LlamaIndex…) qui mérite sa page dédiée parce que le framework parent est trop vaste pour le mettre en avant : p. ex. le SQL agent de LangChain, le NLSQLTableQueryEngine de LlamaIndex. Ce n'est **pas** une brique déployable seule (elle s'utilise via son framework parent, qu'elle référence dans ses liens), d'où la distinction avec `llm/framework` — et l'exclusion des comparatifs de frameworks. Fiche `type: service`, `licence_type`/`langage` hérités du parent.

- `llm/app` — **application LLM prête à déployer**, utilisable telle quelle par un utilisateur final (chat, classe virtuelle, assistant métier). Distinct de `llm/framework` (briques et SDK avec lesquels on *construit* une application) : ici on installe et on s'en sert, on n'assemble pas.
- `llm/context` — gestion et **compression du contexte** envoyé au modèle : réduction du nombre de tokens en entrée, élagage, réécriture, réinjection à la demande du contenu intégral. Distinct de `llm/observability` (mesurer ce qui est envoyé) et de `ml/optimization` (alléger le modèle, pas le prompt).
- `network/*` — **réseau** : ce qui circule entre machines, indépendamment de l'applicatif. Sous-domaines :
  - `network/analysis` — observation et analyse du trafic (qui parle à qui, ports, protocoles, volumes, alertes). Distinct de `observability/*` qui instrumente des applications *depuis l'intérieur*.
  - `network/transfer` — transfert de fichiers de machine à machine (chiffrement, relais, reprise).
- `security/*` — **sécurité et renseignement**, du point de vue de l'analyste. Distinct du tag `ai-security` (surface d'attaque des systèmes LLM). Sous-domaines :
  - `security/recon` — reconnaissance d'une cible **depuis l'extérieur**, sans accès privilégié : DNS, TLS, en-têtes, technologies détectées, empreinte réseau.
  - `security/osint` — renseignement en sources ouvertes : outils et **annuaires** de recherche en sources publiques.
- `observability/infra` — supervision de **machines et de conteneurs** : CPU, mémoire, disque, réseau, état des conteneurs, alertes. Distinct de `observability/{log, metric, trace}` qui portent la télémétrie *applicative*, et de `ml/monitoring` (dérive de modèle).
- `tooling/document` — manipulation de **documents et de PDF** en tant que fichiers : fusion, découpe, rotation, conversion de format, OCR, signature, compression. Distinct de `data/parsing` (extraire du contenu structuré *pour une machine*, typiquement pour du RAG) : ici on produit un document pour un humain.
- `tooling/video` — outils **vidéo** : montage et production (timeline, découpe, export), encodage, clients de lecture. Distinct de `tooling/media` (ingestion de médias comme *input* pour un assistant IA) et de `ui/*`.
- `tooling/capture` — **capture de contenu** externe vers un format texte réutilisable : page web ou document converti en Markdown pour des notes, de la documentation ou un prompt. Distinct de `data/scraping` (extraction *programmatique* et à l'échelle) : ici c'est un geste manuel, à l'unité.
- `tooling/llm` — utilitaires locaux **autour** des LLM : dimensionnement matériel ↔ modèle, choix et gestion de modèles, inspection. Distinct de `llm/local` (les runtimes d'inférence eux-mêmes, type Ollama ou llama.cpp) : ici on outille la décision, on ne sert pas le modèle.

## Outils Dev (`Dev/Outils/`) — `categorie: tooling/<famille>`

Outils techniques que l'on **utilise** (clients GUI, CLI, utilitaires) — par opposition aux services que l'on **déploie** (`Dev/Services/`). Même galaxie `dev` : tout ce qui est technique vit dans Dev.

> **Portée du champ `categorie:` pour un Outil.** La famille est le plus souvent `tooling/<famille>`, mais pas obligatoirement : un outil dont le domaine existe déjà par ailleurs prend ce domaine (Sniffnet en `network/analysis`, osint4all en `security/osint`). La règle est le **domaine du sujet**, pas le dossier. Ce qui distingue `Dev/Outils/` de `Dev/Services/` est la **nature** — on l'utilise vs on le déploie — et cela se lit dans `type:`, pas dans `categorie:`.

- `db-admin` — clients GUI et outils d'administration de bases (DBeaver, pgAdmin, Compass…)
- `api` — clients d'API : composer, envoyer et tester des requêtes HTTP/REST/GraphQL/gRPC, gérer collections et environnements (Postman, Bruno, Insomnia…). Distinct de `tooling/test` (frameworks de test de code, type pytest).
- `code-assistant` — assistants IA de codage intégrés à l'éditeur ou au terminal : complétion, chat, édition multi-fichiers, mode agent (Continue, Aider, Cline…). Distinct des frameworks d'apps LLM (`llm/framework`) : ce sont des outils que l'on utilise, pas des briques que l'on déploie.
- `media` — ingestion / traitement de médias (vidéo, audio, image) pour donner à un assistant IA un input multimodal : téléchargement, extraction de frames, transcription (claude-video/`watch`…). Distinct de `code-assistant` (assistance au codage) et de `data/*` (données structurées / ELT).
- `diagram` — outils de création de **diagrammes et schémas** (flowcharts, UML, réseau, isométrique, whiteboard) : éditeurs GUI (draw.io, FossFLOW, Excalidraw) comme approches diagram-as-code (Mermaid). Distinct de `tooling/viz` (visualisation de **données**) : ici on dessine des schémas, pas des graphiques de données.
- `design` — outils de **design d'interface et de prototypage** UI/UX (Figma, Penpot) : maquettes, prototypes interactifs, systèmes de composants. Distinct de `diagram` (schémas techniques) : ici on conçoit des interfaces produit.
- `document`, `video`, `capture`, `llm` — cf. définitions en section *Services Dev* ci-dessus : les mêmes familles servent aux deux natures (Stirling PDF est un service que l'on déploie, OpenCut un outil que l'on utilise, tous deux dans un domaine `tooling/*`).

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
