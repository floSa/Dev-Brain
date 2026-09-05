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

<!-- AUTO:BANDEAU:START -->
> Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Rust | open-core | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme développeur **code-first** : on écrit des scripts — Python, TypeScript, Go, Bash,
SQL — et la plateforme fournit tout autour, l'orchestration en workflows, une **UI générée**
depuis la signature du script, le scheduling et des apps internes. Le moteur est écrit en Rust
et repose sur des workers sans état qui tirent leurs jobs d'une file Postgres, ce qui lui vaut
sa réputation de rapidité et son scaling horizontal réel. C'est l'inverse exact du no-code
visuel : le code est la source, le visuel est dérivé. Windmill Labs le positionne face à
Temporal, Airplane et Retool plutôt que face aux plateformes d'automatisation grand public.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Approche **code-first** : on écrit les scripts, la plateforme fournit orchestration, UI et scheduling | L'**AGPLv3** a un effet viral : ré-exposer Windmill comme fonctionnalité d'un produit propriétaire oblige à publier ce produit en AGPL, ou à prendre une licence Enterprise |
| Besoin de performance et de scaling **distribué** — workers horizontaux, Kubernetes | Public non technique : écrire du code est le point d'entrée, pas une option |
| Bâtir des outils internes — workflows, UI et apps — sur une base auto-hébergeable unique | Plateforme large (workflows + apps + scripts) : courbe d'apprentissage réelle, et un risque de verrouillage sur son modèle |

## Mise en œuvre

- Installation — Docker ou Kubernetes pour le self-host, ou compte Windmill Cloud
- Point d'entrée — un script (Python, TypeScript, Go, Bash, SQL) ; l'UI et le workflow s'en déduisent
- Prérequis — un Postgres, qui sert de file de jobs ; des workers à dimensionner
- Exécution — self-hébergé ou managé ; architecture distribuée native, workers sans état, scaling horizontal
- Coût — gratuit sous AGPLv3 pour le cœur ; une Enterprise Edition sous licence commerciale lève la contrainte de licence et ajoute les fonctions d'équipe

## Écosystème

### Alternatives

- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Ressources

- Documentation — https://www.windmill.dev/docs/intro
- Dépôt — https://github.com/windmill-labs/windmill

## Voir aussi

- [[Automatisation no-code]] — le hub du domaine
- [[Comparatif - Automatisation no-code]] — ce qui départage les cinq plateformes du dossier
- [[Airflow]] · [[Dagster]] · [[Prefect]] · [[Temporal]] — les mondes que Windmill chevauche : orchestration de données d'un côté, exécution durable de l'autre
