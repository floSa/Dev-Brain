---
role: brique
nom: Windmill
alias: [windmill, windmill.dev, windmill-labs]
pitch: "Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool."
categorie: automation/no-code
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Rust
scaling: distributed
alternatives: ["[[n8n]]", "[[Activepieces]]", "[[Zapier]]", "[[gumloop]]"]
complements: []
tags: [low-code, orchestration]
url_docs: https://www.windmill.dev/docs/intro
url_repo: https://github.com/windmill-labs/windmill
---

# Windmill

## Pourquoi

**Plateforme développeur code-first** (backend **Rust**, front Svelte) : transforme des **scripts** (Python, TypeScript, Go, Bash, SQL…) en **workflows**, **UIs auto-générées** et **apps internes**. Moteur d'exécution **distribué** réputé très rapide (workers sans état tirant des jobs d'une file Postgres). Open source sous **AGPLv3** (Windmill Labs), avec une **Enterprise Edition** sous licence commerciale — d'où `open-core`. Se positionne en alternative à **Temporal**, **Airplane** et **Retool**.

## Quand l'utiliser

- Approche **code-first** : on écrit des scripts, Windmill fournit l'orchestration, l'UI et le scheduling autour.
- Besoin de **performance** et de scaling **distribué** (workers horizontaux, Kubernetes).
- Bâtir des **outils internes** (workflows + UI + apps) sur une base self-hostable unique.

## Quand NE PAS l'utiliser

- Public **non-développeur** voulant du pur no-code visuel → [[n8n]] / [[Zapier]].
- Catalogue d'intégrations SaaS clé en main → [[Activepieces]] / [[Zapier]].
- Contrainte **AGPL** bloquante pour un produit propriétaire qui ré-exposerait Windmill → licence Enterprise nécessaire.

## Déploiement & coût

- **Self-host** gratuit (Docker, Kubernetes) ou **Windmill Cloud** managé — d'où `hosted: both`.
- Architecture **distribuée** native : workers sans état + file Postgres, scaling horizontal.
- **AGPLv3** : ré-exposer Windmill comme fonctionnalité d'un produit oblige à publier ce produit en AGPL ou à prendre une **licence commerciale**.

## Pièges

- **AGPLv3** : effet viral à anticiper pour tout usage embarqué dans un produit propriétaire.
- Code-first : moins adapté qu'un n8n/Zapier pour des utilisateurs **non techniques**.
- Plateforme large (workflows + apps + scripts) : courbe d'apprentissage et risque de **verrouillage**.

## Alternatives

- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Liens

- [[Comparatif - Automatisation no-code]] — comparatif de la catégorie
- Frontière avec l'orchestration **data** ([[Airflow]], [[Dagster]], [[Prefect]]) et l'exécution durable ([[Temporal]]) : Windmill chevauche les deux mondes (scripts → workflows + UIs).
- Doc : https://www.windmill.dev/docs/intro
