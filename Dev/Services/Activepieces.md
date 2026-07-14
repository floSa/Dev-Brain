---
galaxie: dev
type: service
nom: Activepieces
alias: [activepieces]
pitch: "Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier."
categorie: automation/workflow
licence_type: open-core
hosted: both
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/n8n|n8n]]", "[[Dev/Services/Windmill|Windmill]]", "[[Dev/Services/Zapier|Zapier]]", "[[Dev/Services/gumloop|gumloop]]"]
remplace_par: []
status: actif
tags: [low-code, orchestration, agents, mcp]
url_docs: https://www.activepieces.com/docs
url_repo: https://github.com/activepieces/activepieces
---

# Activepieces

## Pourquoi

**Automatisation de workflows open source** : éditeur visuel (TypeScript) pour connecter 200+ applications (les « **pièces** », publiées comme paquets npm), avec un fort virage **IA** — agents et exposition/consommation de **serveurs MCP**. Modèle **open-core** : la *Community Edition* est sous **MIT** (vraiment open-source, usage commercial libre) ; les fonctions *Enterprise* sont sous licence commerciale. Se positionne comme l'alternative **open-source et MIT** à Zapier.

## Quand l'utiliser

- Vouloir une base d'automatisation **réellement MIT** (pas de restriction de revente, contrairement à n8n).
- Développer ses propres connecteurs en **TypeScript** avec une bonne DX (hot reload local).
- Construire des **agents IA / intégrations MCP** dans un outil no-code self-hostable.

## Quand NE PAS l'utiliser

- Catalogue d'intégrations **plus large** ou écosystème plus mûr requis → [[Dev/Services/n8n|n8n]] ou [[Dev/Services/Zapier|Zapier]].
- Automatisation **code-first** orientée développeur → [[Dev/Services/Windmill|Windmill]].
- Tout managé sans rien opérer → [[Dev/Services/Zapier|Zapier]] / [[Dev/Services/gumloop|gumloop]].

## Déploiement & coût

- **Self-host** gratuit via Docker (Community MIT) ou **Activepieces Cloud** managé — d'où `hosted: both`.
- Single-node par défaut ; les fonctions avancées (RBAC, projets, embedding) relèvent de l'**Enterprise** payant.
- Cœur gratuit et sans limite d'usage commercial — le coût vient des add-ons Enterprise et du Cloud.

## Pièges

- **Open-core** : certaines fonctionnalités attendues en équipe ne sont pas dans le cœur MIT.
- Écosystème de pièces **plus restreint** que n8n / Zapier.
- Produit qui bouge vite (pivot IA/MCP) : surface fonctionnelle en évolution rapide.

## Alternatives

- [[Dev/Services/n8n|n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Dev/Services/Windmill|Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Dev/Services/Zapier|Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[Dev/Services/gumloop|gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Liens

- [[Comparatif - Automatisation no-code]] — comparatif de la catégorie
- Concept : [[mcp-protocol]] — Activepieces expose et consomme des serveurs MCP.
- Doc : https://www.activepieces.com/docs
