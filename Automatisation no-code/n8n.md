---
role: brique
nom: n8n
alias: [n8n.io, n8n-io]
pitch: "Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud."
categorie: automation/no-code
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Activepieces]]", "[[Windmill]]", "[[Zapier]]", "[[gumloop]]"]
complements: []
tags: [low-code, orchestration, agents]
url_docs: https://docs.n8n.io/
url_repo: https://github.com/n8n-io/n8n
---

# n8n

## Pourquoi

**Plateforme d'automatisation de workflows** (Node.js/TypeScript) : éditeur visuel où l'on relie des **nœuds** (déclencheurs, actions, logique) pour connecter 400+ applications, avec la possibilité d'insérer du **code custom** (JS/Python) et des **nœuds IA natifs** (agents, LLM, RAG). Positionnement *fair-code* : code **source-available** sous **Sustainable Use License**, pas open-source au sens OSI (l'usage commercial en revente/multi-tenant est restreint).

## Quand l'utiliser

- Vouloir un **self-host** complet sur ses propres serveurs, avec contrôle des données.
- Workflows qui mêlent **no-code et code** : la plupart des étapes en visuel, quelques nœuds en JS/Python.
- Besoin de **nœuds IA** intégrés (agents, appels LLM) sans coder toute la tuyauterie.

## Quand NE PAS l'utiliser

- Refus de toute contrainte de licence sur la revente → préférer un cœur **MIT** : [[Activepieces]].
- Automatisation **pilotée par scripts/code** plutôt que par nœuds → [[Windmill]].
- Aucune envie d'opérer une infra, tout managé → [[Zapier]].

## Déploiement & coût

- **Self-host** gratuit (Docker, npm) ou **n8n Cloud** managé (abonnement) — d'où `hosted: both`.
- Single-node par défaut ; montée en charge possible via le **queue mode** (workers Redis), au prix d'efforts d'infra.
- Licence à lire pour tout usage **commercial où n8n est exposé à des clients** (multi-tenant) : exige une licence Enterprise.

## Pièges

- *Fair-code* ≠ open-source : la **Sustainable Use License** surprend ceux qui croient à du MIT/Apache.
- Les nœuds **code** rendent vite les workflows non portables / difficiles à versionner proprement.
- Scaling au-delà du single-node = configuration **queue mode** non triviale.

## Alternatives

- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Liens

- [[Comparatif - Automatisation no-code]] — comparatif de la catégorie
- Distinct des orchestrateurs de pipelines **data** ([[Airflow]], [[Dagster]], [[Prefect]]) : n8n automatise des **apps**, pas des DAG de données.
- Doc : https://docs.n8n.io/
