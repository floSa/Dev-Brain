---
galaxie: dev
type: outil
nom: Spec Kit
alias: [spec-kit, specify, specify-cli, spec-driven development, SDD]
pitch: "CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement)."
categorie: tooling/code-assistant
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
status: actif
alternatives: []
tags: [code-assistant, code-generation, agents, cli]
url_docs: https://github.com/github/spec-kit
url_repo: https://github.com/github/spec-kit
---

# Spec Kit

## Pourquoi

Spec Kit (MIT, GitHub) outille le **spec-driven development** : au lieu d'écrire du code puis de le documenter, on rédige une **spécification exécutable** qui devient la source de vérité et pilote un agent de codage IA, du cahier des charges jusqu'à l'implémentation. La CLI `specify` scaffolde le projet et installe une série de commandes slash (`/speckit.*`) que l'agent exécute étape par étape. Compatible avec 30+ agents (Copilot, Claude, Cursor, Gemini CLI…).

## Quand l'utiliser

- Cadrer un projet greenfield ou une fonctionnalité avec un cahier des charges explicite **avant** de laisser l'IA coder.
- Vouloir une trace structurée intention → plan → tâches → implémentation, révisable en équipe.
- Imposer des garde-fous : une « constitution » de principes que l'agent doit respecter.

## Quand NE PAS l'utiliser

- Complétion inline ou chat intégré à l'IDE → [[Dev/Outils/Continue|Continue]].
- Petite édition ponctuelle : le workflow SDD (6-7 étapes) est surdimensionné.

## Bases & plateformes

- MIT, écrit en Python (CLI `specify`), requiert Python 3.11+ et git ; multiplateforme (Windows, macOS, Linux).
- Installation : `uv tool install specify-cli` (ou `pipx`), puis `specify init <projet> --integration <agent>` ; `specify integration list` liste les agents supportés.
- Workflow SDD : `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`, plus les optionnelles `clarify`, `analyze`, `checklist`, `taskstoissues`.
- Maintenu par GitHub, très actif (~122k stars, releases fréquentes).

## Pièges

- Garbage-in : une spec bâclée produit un plan et un code bâclés — l'effort se déplace vers l'amont, il ne disparaît pas.
- Surcouche méthodologique : la qualité finale dépend encore de l'agent de codage sous-jacent, que Spec Kit ne remplace pas.
- Jeune et mouvant (nombreuses releases, commandes qui évoluent) : verrouiller une version dans un projet.

## Alternatives

- Pas de substitut direct dans le brain : c'est un **cadre méthodologique** (spec-driven), pas un assistant de code. Les agents qu'il pilote sont fichés à part : [[Dev/Outils/Aider|Aider]], [[Dev/Outils/Cline|Cline]], [[Dev/Outils/Continue|Continue]].

## Liens

- Repo / doc : https://github.com/github/spec-kit
