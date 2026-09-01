---
galaxie: meta
nom: taxonomie
type: gouvernance
created: 2026-06-04
modified: 2026-09-02
tags: [meta, gouvernance, taxonomie]
---

# Taxonomie — deux axes de rangement

Une page de `Dev/` est rangée sur **deux axes indépendants**, tous deux à vocabulaire fermé :

| Axe | Question à laquelle il répond | Valeurs |
|-----|-------------------------------|---------|
| `categorie:` | **De quoi ça parle** — le domaine, le sujet | cf. sections *Services Dev* / *Outils Dev* ci-dessous |
| `famille:` | **Ce que c'est** — la nature de la chose | 9 valeurs, cf. section *Axe `famille:`* |

`famille:` porte la **NATURE**, `categorie:` porte le **DOMAINE**. Les deux sont contrôlés par
`AI/scripts/check_brain.py` : une valeur hors liste échoue en dur.

**`type:` cesse de porter la nature.** Le champ reste — il désigne le gabarit de frontmatter et
la galaxie d'accueil (`service`, `outil`, `concept`, `pattern`, `rule`) — mais il ne dit rien de
ce qu'est l'objet : il est posé par le dossier d'accueil (`Dev/Services/` vs `Dev/Outils/`), pas
par une question sur l'objet. Le croisement le prouve : sur les 336 fiches Dev, 57 relèvent des
familles `application`, `cli` ou `extension` — 34 en `type: outil`, 23 en `type: service`, sans
discriminant (Marimo, notebook à interface, est `type: service` ; DBeaver, client à interface,
est `type: outil` — même nature, types opposés ; symétriquement, 11 des 13 `saas` sont
`type: service`). Ne pas raisonner sur `type:` pour savoir ce qu'est une brique : lire `famille:`.

## Axe `famille:` — la nature de la brique (9 valeurs fermées)

Énumération fermée, lue par `check_brain.py` dans ce bloc de code et **là seulement** :

```famille
paquet
plateforme
application
cli
saas
extension
specification
modele
annuaire
```

Le champ est attendu sur `type: service` et `type: outil`, et interdit sur les autres gabarits
(`concept`, `pattern`, `rule` : ceux-là ne documentent pas une brique). `check_brain` refuse en
dur toute valeur hors de ce bloc [R14] mais **accepte un champ vide** : c'est le seul signal
prévu pour « l'arbre n'a pas tranché, à arbitrer ». Une famille inventée est une faute, un champ
vide est une question ouverte.

### Arbre de décision — ORDRE STRICT, première réponse positive gagne

La famille ne se **choisit** pas, elle se **dérive**. On descend les neuf questions dans l'ordre
et on s'arrête à la première réponse « oui ». Aucune question n'appelle un jugement de valeur :
toutes portent sur un fait vérifiable dans le dépôt amont ou dans la fiche.

| # | Question fermée | Si oui |
|---|-----------------|--------|
| F1 | La page décrit-elle une liste de ressources externes plutôt qu'un logiciel ? | `annuaire` |
| F2 | Est-ce une norme, un format ou un protocole, sans implémentation de référence unique ? | `specification` |
| F3 | Le livrable téléchargé est-il un jeu de poids entraînés ? | `modele` |
| F4 | Faut-il un logiciel hôte tiers (IDE, navigateur, agent, SGBD) pour l'exécuter ? | `extension` |
| F5 | L'auto-hébergement est-il impossible (compte chez un tiers obligatoire) ? | `saas` |
| F6 | Un autre **programme**, et pas seulement un humain, en est-il le consommateur nominal (port, API réseau) ? | `plateforme` |
| F7 | Le point d'entrée nominal est-il une interface graphique ? | `application` |
| F8 | S'invoque-t-il en commande shell sans être importé dans du code ? | `cli` |
| F9 | Aucun des précédents | `paquet` |

Si deux branches semblent convenir, ce n'est pas à l'arbitrage de trancher : c'est une **règle de
départage** ci-dessous. Si aucune ne tranche, laisser le champ **vide** et demander — ne pas
forcer une valeur.

### Six règles de départage

Sans elles, l'arbre laisse 35 fiches en suspens sur 336 ; avec elles, aucune.

| # | Règle | Cas qu'elle résout |
|---|-------|--------------------|
| R1 | Si le code est publié et déployable, la famille est `plateforme`, jamais `saas`, même si l'éditeur pousse son offre managée. | Comet, Neptune, Weights & Biases, LangSmith, E2B |
| R2 | Un moteur exécutable en embarqué **et** en serveur est `paquet` si l'installation par défaut ne lance aucun processus. | DuckDB, SQLite, Chroma, LanceDB |
| R3 | La famille suit le **point d'entrée documenté en premier** (README amont, à défaut la fiche). | Uvicorn (`cli`), Ray (`paquet`), pi (`cli`), Mermaid (`extension`), LM Studio (`application`), TensorRT (`paquet`), Web-Check (`application`) |
| R4 | `specification` seulement si la page ne documente **aucune** implémentation de référence. | Gymnasium → `paquet` ; ADBC, Parquet, Avro, Iceberg → `specification` |
| R5 | Le tri se fait sur ce dont l'objet **a besoin pour tourner**, pas sur ce à quoi il ressemble. | TransformerLens, SAELens, nnsight, sentence-transformers → `paquet` |
| R6 | Une sortie destinée à une **machine** et une sortie destinée à un **humain** ne rangent pas pareil (vaut surtout pour `categorie:`, cité ici pour mémoire). | Stirling PDF vs docTR |

### Les 9 valeurs, définition et frontière

| Famille | Définition | Frontière |
|---------|-----------|-----------|
| `paquet` | S'installe dans un projet et s'importe dans du code. | Distinct de `cli` parce que le point d'entrée est un `import`, pas une commande. Distinct de `extension` parce que l'hôte est un projet, pas un logiciel. |
| `plateforme` | Se déploie et tourne en processus qu'un autre **programme** appelle. | Distinct de `application` parce que le consommateur nominal n'est pas un humain. Distinct de `saas` parce qu'elle est auto-hébergeable (R1). |
| `application` | S'utilise par une interface faite pour un humain. | Distinct de `plateforme` parce qu'aucune API réseau n'y est un point d'entrée documenté. |
| `cli` | S'invoque en commande shell sans être importé. | Distinct de `paquet` par le point d'entrée documenté en premier (R3) : `axolotl train` contre `import trl`. |
| `saas` | Compte chez un tiers obligatoire, aucun auto-hébergement. | Distinct de `plateforme` parce que le code n'est pas déployable (R1) — une offre managée à côté d'un dépôt ouvert ne suffit pas. |
| `extension` | Ne s'exécute qu'à l'intérieur d'un hôte tiers. | Distinct de `paquet` parce que l'hôte est un **logiciel** (IDE, navigateur, agent de code, SGBD), pas un projet : `pgvector` sans Postgres et `jupysql` sans Jupyter n'exécutent rien. |
| `specification` | Norme, format ou protocole sans implémentation de référence. | Distinct de `paquet` parce qu'il existe plusieurs implémentations et aucune canonique (R4). |
| `modele` | Le livrable est un jeu de poids entraînés. | Distinct de `paquet` parce qu'on charge des poids, on n'écrit pas d'algorithme : `timm` (collection de backbones) est un `paquet`, `segment-anything` (code + poids officiels) un `modele`. |
| `annuaire` | Liste de ressources externes, pas un logiciel. | Distinct de tout le reste parce que rien ne s'installe, rien ne se déploie, il n'y a pas de version à suivre. |

### `famille: annuaire` n'exonère pas du domaine

Un annuaire n'a pas de domaine évident : `public-apis` liste 1 700 API de 52 secteurs. La règle est
néanmoins : **`categorie:` reste obligatoire, et vaut le domaine du sujet listé**, pas celui de la
forme « annuaire ». Quand l'annuaire couvre plusieurs domaines, il prend celui de l'**intention de
recherche** qui le fait ouvrir, et cet arbitrage s'écrit en clair dans le corps de la fiche.

Motif du refus de l'exonération : `categorie:` est un champ requis contrôlé (`check_brain`), et
`build_mocs.py` groupe par `categorie:` — une page sans catégorie sort des MOC et viole aussitôt
R7 (toute page atteignable depuis un MOC). Une exonération pour 2 pages sur 336 serait une
exception que personne ne retient, au prix d'une page injoignable.

## Axe `categorie:` — le domaine

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

## Outils Dev (`Dev/Outils/`) — `categorie: tooling/<sous-domaine>`

Outils techniques que l'on **utilise** (clients GUI, CLI, utilitaires) — par opposition aux services que l'on **déploie** (`Dev/Services/`). Même galaxie `dev` : tout ce qui est technique vit dans Dev.

> **Portée du champ `categorie:` pour un Outil.** Le sous-domaine est le plus souvent `tooling/<sous-domaine>`, mais pas obligatoirement : un outil dont le domaine existe déjà par ailleurs prend ce domaine (Sniffnet en `network/analysis`, osint4all en `security/osint`). La règle est le **domaine du sujet**, pas le dossier.
>
> **Attention.** La **nature** de l'objet — on l'utilise, on le déploie, on l'importe — ne se lit ni dans `categorie:` ni dans `type:` : elle se lit dans `famille:` (cf. section *Axe `famille:`*). `type: outil` ne dit que le gabarit et le dossier ; il ne présume ni d'une interface graphique ni d'une commande shell.

- `db-admin` — clients GUI et outils d'administration de bases (DBeaver, pgAdmin, Compass…)
- `api` — clients d'API : composer, envoyer et tester des requêtes HTTP/REST/GraphQL/gRPC, gérer collections et environnements (Postman, Bruno, Insomnia…). Distinct de `tooling/test` (frameworks de test de code, type pytest).
- `code-assistant` — assistants IA de codage intégrés à l'éditeur ou au terminal : complétion, chat, édition multi-fichiers, mode agent (Continue, Aider, Cline…). Distinct des frameworks d'apps LLM (`llm/framework`) : ce sont des outils que l'on utilise, pas des briques que l'on déploie.
- `media` — ingestion / traitement de médias (vidéo, audio, image) pour donner à un assistant IA un input multimodal : téléchargement, extraction de frames, transcription (claude-video/`watch`…). Distinct de `code-assistant` (assistance au codage) et de `data/*` (données structurées / ELT).
- `diagram` — outils de création de **diagrammes et schémas** (flowcharts, UML, réseau, isométrique, whiteboard) : éditeurs GUI (draw.io, FossFLOW, Excalidraw) comme approches diagram-as-code (Mermaid). Distinct de `tooling/viz` (visualisation de **données**) : ici on dessine des schémas, pas des graphiques de données.
- `design` — outils de **design d'interface et de prototypage** UI/UX (Figma, Penpot) : maquettes, prototypes interactifs, systèmes de composants. Distinct de `diagram` (schémas techniques) : ici on conçoit des interfaces produit.
- `document`, `video`, `capture`, `llm` — cf. définitions en section *Services Dev* ci-dessus : les mêmes sous-domaines servent aux deux natures (Stirling PDF est un service que l'on déploie, OpenCut un outil que l'on utilise, tous deux dans un domaine `tooling/*`).

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

## Skills Wiki (`Wiki/Outils/`) — `categorie: skill/<sous-domaine>`

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
