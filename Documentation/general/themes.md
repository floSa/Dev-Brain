---
galaxie: meta
nom: themes
type: gouvernance
created: 2026-06-04
modified: 2026-09-02
tags: [meta, gouvernance, themes]
---

# Thèmes — grandes thématiques & MOC

Vocabulaire du champ `domaines:` (frontmatter des Concepts Wiki, et tri transverse). Cinq thèmes calés sur le profil de l'utilisateur. Chaque thème porte, à terme, une **MOC** — page-index qui agrège ses pages clés.

| Code (`domaines:`) | Thème | Couvre | MOC |
|--------------------|-------|--------|-----|
| `data-sci` | Data Science | exploration, modélisation, viz, stats | _(à créer)_ |
| `data-eng` | Data Engineering | pipelines, ELT, qualité, streaming | _(à créer)_ |
| `mlops` | MLOps | déploiement modèle, monitoring, infra ML | _(à créer)_ |
| `ml-eng` | ML Engineering | entraînement scalable, optimisation | _(à créer)_ |
| `ai-eng` | AI Engineering | apps LLM, RAG, agents, MCP | _(à créer)_ |
| `infra-ops` | Infrastructure & Ops | réseau, supervision de machines, self-hosting, sécurité opérationnelle | _(à créer)_ |

Une page peut porter plusieurs domaines. Exemple : les bases vectorielles relèvent de `[data-eng, ai-eng]`.

> `infra-ops` (ajouté le 2026-09-02) couvre ce qui fait tourner et surveiller les machines, par opposition aux cinq
> thèmes data/ML/AI qui portent le métier. Motif de l'ajout : aucun des cinq n'accueillait honnêtement un moniteur
> de trafic réseau ou un hub de supervision serveur. Limite connue : certains outils du poste de travail
> (montage vidéo, client de streaming) ne relèvent d'aucun thème, même après cet ajout — ils portent
> `domaines: []` en attendant l'audit de taxonomie (cf. `AI/ameliorations-devbrain.md`).
