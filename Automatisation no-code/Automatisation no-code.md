---
role: hub
nom: Automatisation no-code
alias: [low-code, automatisation, ipaas]
pitch: Enchaîner des services par un graphe plutôt que par du code — utile pour l'intégration, trompeur pour la logique métier.
domaines: [data-eng, ai-eng]
tags: [low-code, orchestration, self-hosted]
---

# Automatisation no-code

> Enchaîner des services par un graphe plutôt que par du code — utile pour l'intégration, trompeur pour la logique métier.

## Ce qu'il faut comprendre

- Ces plateformes gagnent sur un point précis : le **connecteur déjà écrit**. Brancher une boîte mail, un CRM, un webhook et une feuille de calcul prend des minutes au lieu d'une journée d'authentification et de pagination.
- Elles perdent sur tout le reste dès que le flux grossit. Un graphe ne se relit pas en diff, ne se teste pas, se versionne mal, et la logique conditionnelle y devient rapidement illisible. Le seuil de bascule vers du code est bas, et il arrive plus tôt que prévu.
- Détail par brique : [[No-code]].

## Choisir

- Un flux d'intégration entre SaaS, à monter vite → [[No-code]], et probablement [[n8n]].
- Un pipeline de données à faire tourner tous les jours → un orchestrateur, pas ce domaine.
- De la logique métier durable → du code.

<!-- AUTO:START -->
### Sous-domaines
- [[No-code]]
<!-- AUTO:END -->
