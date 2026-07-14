---
galaxie: dev
type: outil
nom: Aider
alias: [aider]
pitch: "Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur."
categorie: tooling/code-assistant
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
status: actif
alternatives: ["[[Dev/Outils/Continue|Continue]]", "[[Dev/Outils/Cline|Cline]]"]
tags: [code-assistant, code-generation, llm, version-control]
url_docs: https://aider.chat/docs/
url_repo: https://github.com/Aider-AI/aider
---

# Aider

## Pourquoi

Pair-programmeur IA qui vit dans le terminal (Apache 2.0, Python). Il relie un LLM au dépôt git local : édition de fichiers, création et refactor pilotés par le chat, **commit git automatique** de chaque changement (faciles à suivre et annuler). Construit une carte (repo map) de toute la base de code pour bien travailler sur les gros projets. Agnostique de l'éditeur : aucun plugin requis.

## Quand l'utiliser

- Travailler depuis le terminal, sans dépendre d'un IDE ni d'un plugin.
- Vouloir un historique git propre : un commit atomique par édition de l'IA.
- Refactors et changements multi-fichiers sur un dépôt existant, avec repo map pour le contexte.

## Quand NE PAS l'utiliser

- Assistant intégré à l'IDE avec autocomplétion inline → [[Dev/Outils/Continue|Continue]].
- Agent autonome dans VS Code avec modes Plan/Act et MCP → [[Dev/Outils/Cline|Cline]].

## Bases & plateformes

- Open-source Apache 2.0, écrit en Python (requiert Python 3.9+ et git).
- Multiplateforme (Windows, macOS, Linux). Se connecte à presque tous les LLM (Claude, GPT, DeepSeek, modèles locaux…).

## Pièges

- Tout passe par git : un dépôt non initialisé ou sale complique le suivi des commits automatiques.
- Pas d'interface graphique : la prise en main suppose l'aisance en ligne de commande.
- Le coût d'API peut grimper sur de gros dépôts à cause de la repo map envoyée en contexte.

## Alternatives

- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif des assistants IA de code
- Doc : https://aider.chat/docs/
