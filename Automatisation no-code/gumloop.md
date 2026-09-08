---
role: brique
nom: gumloop
alias: [Gumloop, gumloop.com]
pitch: "Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host."
categorie: automation/no-code
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[n8n]]", "[[Activepieces]]", "[[Windmill]]", "[[Zapier]]"]
complements: []
tags: [low-code, orchestration, agents]
url_docs: https://docs.gumloop.com/
url_repo: 
---

# gumloop

<!-- AUTO:BANDEAU:START -->
> Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Automatisation no-code où l'IA n'est pas un nœud parmi d'autres : sur un **canvas
drag-and-drop**, **chaque nœud peut porter de la logique IA** — analyser un texte, décider,
transformer — sans qu'on câble un seul appel LLM. La cible affichée est la construction
d'agents métier par des employés non développeurs : onboarding, rapprochement de factures, tri
de tickets, mise à jour de CRM. C'est ce déplacement du LLM depuis l'add-on vers le matériau de
base qui définit l'outil, et c'est aussi ce qui explique ses limites d'exploitation. Éditeur
fondé en 2023, passé par Y Combinator (W24).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Workflows où l'IA est **au cœur** de chaque étape, pas un simple add-on | L'IA dans chaque nœud rend les exécutions **moins déterministes** et nettement plus difficiles à déboguer |
| Permettre à des employés non développeurs de bâtir des agents IA en autonomie | Jeune éditeur : produit et tarifs en évolution rapide, rien n'est stabilisé |
| Prototyper vite des automatisations document ou texte, lourdes en raisonnement | Lock-in propriétaire doublé d'une dépendance aux **coûts LLM** sous-jacents, qui pilotent la facture |
| | Automatisation déterministe simple, sans IA : un moteur de workflow ordinaire fait le travail pour moins cher |

## Mise en œuvre

- Installation — aucune : un compte suffit
- Point d'entrée — le canvas drag-and-drop de nœuds
- Prérequis — aucun ; pas de self-host à prévoir, ni possible
- Exécution — 100 % managé, serverless
- Coût — par **crédits** et volume d'exécutions IA, en offres self-serve et Enterprise ; la facture est dominée par la consommation des modèles appelés à chaque étape

## Écosystème

### Alternatives

- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.

## Ressources

- Documentation — https://docs.gumloop.com/

## Voir aussi

- [[Automatisation no-code]] — le hub du domaine
- [[Comparatif - Automatisation no-code]] — ce qui départage les cinq plateformes du dossier
- [[Agent patterns]] — chaque nœud gumloop encapsule un pas d'agent
