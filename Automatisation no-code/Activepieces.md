---
role: brique
nom: Activepieces
alias: [activepieces]
pitch: "Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier."
categorie: automation/no-code
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[n8n]]", "[[Windmill]]", "[[Zapier]]", "[[gumloop]]"]
complements: []
tags: [low-code, orchestration, agents, mcp]
url_docs: https://www.activepieces.com/docs
url_repo: https://github.com/activepieces/activepieces
---

# Activepieces

<!-- AUTO:BANDEAU:START -->
> Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-core | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Automatisation de workflows par éditeur visuel : on relie des **pièces** — les connecteurs
maison, publiés comme paquets npm — pour brancher plus de 200 applications les unes aux autres.
Ce qui le distingue tient en deux points. D'abord la licence du cœur, **MIT**, sans restriction
de revente ni de multi-tenant, là où le voisinage joue le *fair-code* ou l'AGPL. Ensuite un
virage assumé vers l'IA : agents, et exposition comme consommation de serveurs **MCP**. La DX
de connecteur se fait en TypeScript, avec rechargement à chaud en local — écrire sa propre
pièce est un geste ordinaire, pas une extension exotique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir une base d'automatisation dont le cœur est **réellement MIT**, sans contrainte de revente | Certaines fonctions attendues en équipe — RBAC, projets, embarquement — ne sont pas dans le cœur libre mais dans l'Enterprise payante |
| Écrire ses propres connecteurs en **TypeScript**, avec rechargement à chaud | Le catalogue de pièces est plus étroit que celui des leaders du marché |
| Construire des **agents IA** ou des intégrations **MCP** dans un outil no-code auto-hébergeable | Le pivot IA/MCP fait bouger vite la surface fonctionnelle : ce qui est vrai d'une version ne l'est pas forcément de la suivante |

## Mise en œuvre

- Installation — Docker pour la Community MIT, ou compte Activepieces Cloud
- Point d'entrée — l'éditeur visuel de workflows ; les pièces se développent en TypeScript et se publient en paquets npm
- Prérequis — Docker pour le self-host ; rien pour le Cloud
- Exécution — self-hébergé ou managé, mono-nœud par défaut
- Coût — cœur gratuit sous MIT, sans limite d'usage commercial ; le coût vient des add-ons Enterprise et du Cloud

## Écosystème

### Alternatives

- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Ressources

- Documentation — https://www.activepieces.com/docs
- Dépôt — https://github.com/activepieces/activepieces

## Voir aussi

- [[Automatisation no-code]] — le hub du domaine
- [[Comparatif - Automatisation no-code]] — ce qui départage les cinq plateformes du dossier
- [[mcp-protocol]] — le protocole que cet outil expose et consomme
