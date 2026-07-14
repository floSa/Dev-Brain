---
galaxie: dev
type: service
nom: Zapier
alias: [zapier]
pitch: "Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host."
categorie: automation/ipaas
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: ["[[Dev/Services/n8n|n8n]]", "[[Dev/Services/Activepieces|Activepieces]]", "[[Dev/Services/Windmill|Windmill]]", "[[Dev/Services/gumloop|gumloop]]"]
remplace_par: []
status: actif
tags: [low-code, orchestration, agents]
url_docs: https://help.zapier.com/
url_repo: 
---

# Zapier

## Pourquoi

**Référence historique de l'iPaaS no-code** (SaaS propriétaire) : connecte **8000+ applications** via des « **Zaps** » — un **déclencheur** puis une ou plusieurs **actions**. L'offre s'est élargie : **Tables** (base de données d'automatisation), **Interfaces** (apps/forms no-code), **Functions** (Python), **Canvas** et **agents IA**. Le plus accessible aux utilisateurs **non techniques**, au prix d'un modèle entièrement **managé** et **fermé**.

## Quand l'utiliser

- Connecter rapidement des **SaaS grand public** sans rien opérer ni coder.
- Le **plus large catalogue** d'intégrations du marché, prêt à l'emploi.
- Utilisateurs **métier / non-dev** : la prise en main est immédiate.

## Quand NE PAS l'utiliser

- Besoin de **self-host** / souveraineté des données → [[Dev/Services/n8n|n8n]] / [[Dev/Services/Activepieces|Activepieces]] / [[Dev/Services/Windmill|Windmill]].
- **Volumes élevés** : la facturation à la tâche devient vite coûteuse.
- Automatisation **IA-native** où chaque étape raisonne → [[Dev/Services/gumloop|gumloop]].

## Déploiement & coût

- **100 % managé** (SaaS), aucun self-host — d'où `hosted: managed`.
- Tarification **à la tâche** : plan gratuit (100 tâches/mois), puis Professional (~20 $/mois) et Team (~69 $/mois), Enterprise sur devis.
- Coût piloté par le **volume de tâches** et le palier de fonctionnalités, pas par l'infra.

## Pièges

- **Coût à l'échelle** : le modèle par tâche explose sur de gros volumes.
- **Lock-in** propriétaire : ni export du moteur, ni self-host.
- Logique avancée (boucles, branches complexes) moins souple que les outils code-first.

## Alternatives

- [[Dev/Services/n8n|n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Dev/Services/Activepieces|Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Dev/Services/Windmill|Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Dev/Services/gumloop|gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Liens

- [[Comparatif - Automatisation no-code]] — comparatif de la catégorie
- Doc : https://help.zapier.com/
