---
role: brique
nom: Qwen Code
alias: [qwen-code, QwenLM/qwen-code]
pitch: "Agent de code open source (Apache-2.0, TypeScript) pour le terminal, avec plugins d'éditeur : issu de Gemini CLI, il parle aux API OpenAI, Anthropic, Gemini et Qwen et aux modèles locaux Ollama et vLLM."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[OpenCode]]", "[[Goose]]"]
complements: []
tags: [code-assistant, code-generation, llm, agents, mcp, local-llm, terminal-ui]
url_docs: https://qwenlm.github.io/qwen-code-docs/en/users/overview
url_repo: https://github.com/QwenLM/qwen-code
---

# Qwen Code

<!-- AUTO:BANDEAU:START -->
> Agent de code open source (Apache-2.0, TypeScript) pour le terminal, avec plugins d'éditeur : issu de Gemini CLI, il parle aux API OpenAI, Anthropic, Gemini et Qwen et aux modèles locaux Ollama et vLLM.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de code qui vit dans le terminal : il lit le dépôt, édite des fichiers, lance des commandes et fait des commits à partir d'une description en langage naturel. Le README le décrit aussi en application desktop, interface web, plugin d'éditeur (VS Code, Zed, JetBrains), robot de messagerie, CLI sans interface et démon. Il est né comme dérivé de Gemini CLI v0.8.2, et son développement est indépendant depuis la version 0.1. Le dépôt est celui de l'équipe Qwen d'Alibaba (`QwenLM/qwen-code`), mais l'outil n'est pas lié à ses modèles : il accepte les protocoles OpenAI, Anthropic, Gemini et Qwen, tout fournisseur tiers compatible et les modèles locaux servis par Ollama ou vLLM, avec bascule en cours de session.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent de terminal sous licence permissive, avec les mêmes briques (MCP, commandes shell, sorties scriptables) que ses pairs | Il faut un outil qui s'installe sans Node.js : l'installeur shell ou PowerShell existe, mais la voie de repli est npm avec Node.js 22 ou plus |
| Un modèle servi sur place (Ollama, vLLM) ou un fournisseur compatible OpenAI, sans lien avec un fournisseur unique | Compter sur l'accès gratuit par OAuth : la documentation indique que ce palier est arrêté, un accès par clé d'API ou un serveur local est requis |
| Piloter l'agent en script ou depuis un démon, pas seulement en session interactive | Un assistant centré sur le dépôt git et ses commits : [[Aider]] ; un agent généraliste en application desktop : [[Goose]] |

## Mise en œuvre

- Installation — script shell (Linux, macOS), script PowerShell (Windows), Homebrew ou npm (Node.js 22 ou plus)
- Point d'entrée — la commande `qwen` ; dans la session, `/auth` configure le fournisseur et la clé
- Prérequis — un modèle joignable : API d'un fournisseur (Alibaba ModelStudio, DeepSeek, tout endpoint compatible OpenAI) ou serveur local Ollama / vLLM
- Exécution — sur le poste ; v0.24.7 du 2026-09-29, dépôt poussé le 2026-10-05, des versions nocturnes paraissent chaque jour
- Coût — gratuit (Apache-2.0) ; la dépense est celle du modèle

## Écosystème

### Alternatives

- [[OpenCode]] — Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI.
- [[Goose]] — Agent généraliste open source (Apache-2.0, Rust, Linux Foundation) : application desktop, CLI et API, plus de 15 fournisseurs et des extensions MCP, avec Ollama pour les modèles locaux.

## Ressources

- Documentation — https://qwenlm.github.io/qwen-code-docs/en/users/overview
- Dépôt — https://github.com/QwenLM/qwen-code

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
