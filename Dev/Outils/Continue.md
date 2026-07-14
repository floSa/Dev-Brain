---
galaxie: dev
type: outil
nom: Continue
alias: [continue, continue.dev, continuedev]
pitch: "Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API)."
categorie: tooling/code-assistant
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript, Kotlin
status: actif
alternatives: ["[[Dev/Outils/Aider|Aider]]", "[[Dev/Outils/Cline|Cline]]"]
tags: [code-assistant, code-generation, llm, agents]
url_docs: https://docs.continue.dev/
url_repo: https://github.com/continuedev/continue
---

# Continue

## Pourquoi

Assistant IA de codage open-source (Apache 2.0) intégré à VS Code et JetBrains. Quatre usages : Chat (aide sans quitter l'éditeur), Autocomplete (suggestions en temps réel), Edit (modifications ciblées) et Agent (changements à l'échelle du dépôt). Particularité : **bring your own model** — modèle local (gratuit) ou via clé d'API, sans verrouillage fournisseur.

## Quand l'utiliser

- Rester dans son IDE (VS Code ou JetBrains) avec un assistant ouvert et configurable.
- Brancher librement le modèle voulu : local (Ollama, llama.cpp) ou API (Anthropic, OpenAI…), pour la confidentialité ou le coût.
- Besoin d'autocomplétion inline en plus du chat et de l'édition.

## Quand NE PAS l'utiliser

- Workflow 100 % terminal, agnostique de l'éditeur, avec commits git automatiques → [[Dev/Outils/Aider|Aider]].
- Agent autonome à validation pas-à-pas (Plan/Act) et intégration MCP de première classe → [[Dev/Outils/Cline|Cline]].

## Bases & plateformes

- Open-source Apache 2.0. Cœur et GUI en TypeScript ; extension JetBrains en Kotlin (désormais maintenue par la communauté).
- Extensions VS Code et JetBrains, multiplateforme. Le développement actif se déplace vers la **Continue CLI** (checks de code versionnés, exécutables en CI).

## Pièges

- Le plugin JetBrains est passé en maintenance communautaire ; l'éditeur pousse vers la CLI — surveiller la direction du produit.
- Qualité et coût dépendent entièrement du modèle branché : un modèle local faible donne des résultats médiocres.

## Alternatives

- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif des assistants IA de code
- Doc : https://docs.continue.dev/
