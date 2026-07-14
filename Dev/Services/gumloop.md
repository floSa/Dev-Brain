---
galaxie: dev
type: service
nom: gumloop
alias: [Gumloop, gumloop.com]
pitch: "Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host."
categorie: automation/ai-agent
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: ["[[Dev/Services/n8n|n8n]]", "[[Dev/Services/Activepieces|Activepieces]]", "[[Dev/Services/Windmill|Windmill]]", "[[Dev/Services/Zapier|Zapier]]"]
remplace_par: []
status: actif
tags: [low-code, orchestration, agents]
url_docs: https://docs.gumloop.com/
url_repo: 
---

# gumloop

## Pourquoi

**Automatisation no-code pilotée par l'IA** (SaaS propriétaire, **YC W24**) : un **canvas drag-and-drop** où l'on relie des nœuds modulaires, mais où **chaque nœud peut porter de la logique IA** (analyser du texte, décider, transformer) sans câbler manuellement d'appels LLM. Cible la construction d'**agents** métier (onboarding, rapprochement de factures, tri de tickets, mise à jour CRM) par des employés non développeurs.

## Quand l'utiliser

- Workflows où **l'IA est au cœur** de chaque étape, pas un simple add-on.
- Permettre à des **employés non-dev** de bâtir des agents IA en autonomie.
- Prototyper vite des automatisations **document/texte** lourdes en raisonnement.

## Quand NE PAS l'utiliser

- Besoin de **self-host** / contrôle des données → [[Dev/Services/n8n|n8n]] / [[Dev/Services/Activepieces|Activepieces]] / [[Dev/Services/Windmill|Windmill]].
- Très **large catalogue** d'intégrations SaaS classiques → [[Dev/Services/Zapier|Zapier]].
- Automatisation **déterministe** simple sans IA : un moteur de workflow standard suffit.

## Déploiement & coût

- **100 % managé** (SaaS), aucun self-host — d'où `hosted: managed`.
- Tarification par **crédits** / volume d'exécutions IA ; offres self-serve et Enterprise.
- Coût dominé par la **consommation IA** des nœuds (modèles appelés à chaque étape).

## Pièges

- Jeune éditeur (fondé 2023) : produit et tarifs **en évolution rapide**.
- **Lock-in** propriétaire + dépendance aux **coûts LLM** sous-jacents.
- L'IA dans chaque nœud peut rendre les exécutions **moins déterministes** et plus difficiles à déboguer.

## Alternatives

- [[Dev/Services/n8n|n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Dev/Services/Activepieces|Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Dev/Services/Windmill|Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Dev/Services/Zapier|Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.

## Liens

- [[Comparatif - Automatisation no-code]] — comparatif de la catégorie
- Concept : [[Agent patterns]] — chaque nœud gumloop encapsule un pas d'agent IA.
- Doc : https://docs.gumloop.com/
