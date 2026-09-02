---
role: hub
nom: Automatisation no-code
alias: [automatisation, no-code, low-code, ipaas, workflow automation]
pitch: Enchaîner des services par un graphe plutôt que par du code — utile pour l'intégration, trompeur pour la logique métier.
domaines: [data-eng, ai-eng]
tags: [low-code, orchestration, self-hosted]
---

# Automatisation no-code

> Enchaîner des services par un graphe plutôt que par du code — utile pour l'intégration, trompeur pour la logique métier.

## Ce qu'il faut comprendre

- Ces plateformes gagnent sur un point précis : le **connecteur déjà écrit**. Brancher une boîte mail, un CRM, un webhook et une feuille de calcul prend des minutes au lieu d'une journée d'authentification et de pagination.
- Elles perdent sur tout le reste dès que le flux grossit. Un graphe ne se relit pas en diff, ne se teste pas, se versionne mal, et la logique conditionnelle y devient rapidement illisible. Le seuil de bascule vers du code est bas, et il arrive plus tôt que prévu.
- Les cinq briques se rangent sur un seul axe, et c'est celui qui compte : **combien de code la plateforme accepte-t-elle**. [[Zapier]] et [[gumloop]] n'en acceptent pas ou peu, et n'ont rien à exploiter. [[n8n]] et [[Activepieces]] acceptent des nœuds JavaScript ou Python et s'auto-hébergent. [[Windmill]] inverse le rapport : le code est premier, le graphe le compose.
- Le second axe est l'**hébergement**, et il n'est pas cosmétique : un flux no-code voit passer des identifiants de tous les systèmes qu'il connecte. Sur un SaaS, ces secrets vivent chez le fournisseur. En on-prem, c'est souvent la seule option acceptable.
- La **licence** mérite d'être lue avant l'adoption : plusieurs de ces plateformes sont *source-available* et non open-source, ce qui restreint l'usage commercial et la revente. La lire après la mise en production coûte cher.
- L'ajout d'étapes LLM est devenu l'argument de vente commun aux cinq. C'est aussi là que le no-code atteint le plus vite sa limite : un flux agentique demande des reprises, des garde-fous et de l'évaluation, que le graphe n'exprime pas.

## Choisir

- Auto-hébergé, gros catalogue de connecteurs, échappatoire vers du code → [[n8n]].
- Même besoin sous une licence plus permissive → [[Activepieces]].
- Le code d'abord, les scripts orchestrés et versionnés, un graphe par-dessus → [[Windmill]].
- Zéro infrastructure, le plus grand catalogue du marché, budget disponible → [[Zapier]].
- Des flux centrés LLM, sans rien héberger → [[gumloop]].
- Un pipeline de données à faire tourner tous les jours → un orchestrateur, pas ce domaine.
- De la logique métier durable → du code.

<!-- AUTO:START -->
### Briques
- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.
- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[Zapier]] — Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.

### Comparatifs
- [[Comparatif - Automatisation no-code]]
<!-- AUTO:END -->
