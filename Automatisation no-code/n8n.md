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

<!-- AUTO:BANDEAU:START -->
> Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme TypeScript | source-available | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'automatisation de workflows en Node.js : un éditeur visuel où l'on relie des
**nœuds** — déclencheurs, actions, logique — pour connecter plus de 400 applications, avec deux
particularités. On peut insérer du **code** JavaScript ou Python au milieu du visuel, ce qui
rattrape tout ce que le no-code ne sait pas exprimer ; et les **nœuds IA** sont natifs, agents
et appels LLM compris, sans câbler la tuyauterie. Le positionnement est *fair-code* : le code
est lisible et modifiable, mais la licence n'est pas OSI (cf. *Écarter si*) — c'est la
distinction que le nom « open source » masque le plus souvent sur cet outil.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un self-host complet sur ses propres serveurs, avec contrôle des données | La **Sustainable Use License** est source-available, pas open-source au sens OSI : l'usage commercial en revente ou multi-tenant est restreint et exige une licence Enterprise |
| Workflows qui mêlent no-code et code : la plupart des étapes en visuel, quelques nœuds en JS ou Python | Les nœuds **code** rendent les workflows peu portables et difficiles à versionner proprement |
| Besoin de **nœuds IA** intégrés — agents, appels LLM — sans écrire la tuyauterie | Monter au-delà du mono-nœud passe par le **queue mode** (workers Redis) : ce n'est pas une case à cocher |

## Mise en œuvre

- Installation — Docker ou npm pour le self-host, ou compte n8n Cloud
- Point d'entrée — l'éditeur visuel de nœuds ; les nœuds code acceptent du JavaScript ou du Python
- Prérequis — Docker ou Node.js pour le self-host ; Redis en plus si l'on active le queue mode
- Exécution — self-hébergé ou managé, mono-nœud par défaut, distribué en queue mode
- Coût — self-host gratuit, n8n Cloud sur abonnement. La licence est à lire pour tout usage commercial où n8n est exposé à des clients

## Écosystème

### Alternatives

- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Ressources

- Documentation — https://docs.n8n.io/
- Dépôt — https://github.com/n8n-io/n8n

## Voir aussi

- [[Automatisation no-code]] — le hub du domaine
- [[Comparatif - Automatisation no-code]] — ce qui départage les cinq plateformes du dossier
- [[Airflow]] · [[Dagster]] · [[Prefect]] — la frontière à ne pas franchir : ces trois-là orchestrent des DAG de **données**, n8n automatise des **applications**
