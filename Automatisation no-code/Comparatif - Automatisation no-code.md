---
role: comparatif
nom: Comparatif - Automatisation no-code
categorie: automation/no-code
tags: [low-code, orchestration, agents, mcp]
---

# Comparatif - Automatisation no-code

> On tranche sur : la licence et l'hébergement d'abord — qui a le droit de revendre, qui opère le serveur — puis qui écrit le workflow, un profil métier ou un développeur.

![[Comparatif - Automatisation no-code.base]]

## Ce qui départage

- [[n8n]] — 400+ nœuds, du **code JS/Python insérable** au milieu du visuel, des nœuds IA natifs et un self-host complet. Sa vraie frontière est juridique : *fair-code* sous **Sustainable Use License**, donc source-available et non OSI, l'usage commercial en revente ou multi-tenant restreint. Les nœuds code rendent les workflows peu portables, et le scaling au-delà du single-node passe par un *queue mode* non trivial.
- [[Activepieces]] — le seul dont le cœur est **réellement MIT**, sans restriction de revente : pièces publiées en paquets npm, DX de connecteur en TypeScript, et un virage assumé vers les agents IA et les serveurs **MCP**. Open-core — plusieurs fonctions attendues en équipe ne sont pas dans le cœur — écosystème de pièces plus restreint que n8n, et surface fonctionnelle qui bouge vite.
- [[Windmill]] — le seul **code-first** : on écrit des scripts (Python, TypeScript, Go, Bash, SQL) et la plateforme fournit autour l'orchestration, l'UI auto-générée et le scheduling, sur un moteur Rust à workers distribués. **AGPLv3** avec Enterprise commerciale : effet viral à anticiper pour tout produit propriétaire qui le ré-exposerait, et inadapté à un public non technique.
- [[Zapier]] — le catalogue, **8000+ applications**, entièrement managé et fermé : rien à opérer, prise en main immédiate pour un profil métier. Le prix est le modèle économique — facturation **à la tâche** qui explose sur le volume — doublé d'un lock-in sans self-host ni export du moteur, et d'une logique avancée moins souple que les outils code-first.
- [[gumloop]] — le seul où **chaque nœud peut porter de la logique IA** plutôt que de l'appeler en add-on : on assemble des agents métier sur un canvas, sans câbler d'appels LLM. Éditeur fondé en 2023, produit et tarifs en évolution rapide, lock-in propriétaire doublé de la dépendance aux coûts LLM sous-jacents, et l'IA partout rend les exécutions **moins déterministes** et plus dures à déboguer.
