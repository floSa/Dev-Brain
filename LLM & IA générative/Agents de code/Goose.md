---
role: brique
nom: Goose
alias: [goose, block/goose, aaif-goose/goose]
pitch: "Agent généraliste open source (Apache-2.0, Rust, Linux Foundation) : application desktop, CLI et API, plus de 15 fournisseurs et des extensions MCP, avec Ollama pour les modèles locaux."
categorie: llm/agent-de-code
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Rust
alternatives: ["[[OpenCode]]", "[[Aider]]", "[[pi]]", "[[Qwen Code]]"]
complements: []
tags: [code-assistant, agents, mcp, tool-use, local-llm]
url_docs: https://goose-docs.ai/
url_repo: https://github.com/aaif-goose/goose
---

# Goose

<!-- AUTO:BANDEAU:START -->
> Agent généraliste open source (Apache-2.0, Rust, Linux Foundation) : application desktop, CLI et API, plus de 15 fournisseurs et des extensions MCP, avec Ollama pour les modèles locaux.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Rust | open-source | Windows, macOS, Linux | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent qui s'exécute sur le poste et ne se limite pas au code : recherche, rédaction, automatisation, analyse de données. Il se présente en application desktop native (macOS, Linux, Windows), en CLI complète et en API à intégrer ailleurs, écrit en Rust. Il parle à plus de 15 fournisseurs d'après son README (50 et plus d'après la page de configuration), et se branche à plus de 70 extensions par le Model Context Protocol. Créé par Block (dépôt `block/goose`), il a rejoint l'Agentic AI Foundation de la Linux Foundation ; le dépôt courant est `aaif-goose/goose`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent généraliste, pas seulement de code, avec une interface graphique et un CLI sur le même cœur | Un assistant centré sur le dépôt git et ses commits : [[Aider]] |
| Un modèle servi sur place : Ollama, LM Studio ou tout endpoint compatible OpenAI | Le modèle n'appelle pas d'outils : la documentation prévient que Goose en dépend fortement et fonctionne au mieux avec les modèles Claude 4 ; sans appels d'outils, il se réduit à du chat |
| Une gouvernance de fondation et une licence permissive | Un petit modèle local : la qualité des appels d'outils est le facteur limitant, à tester avant d'adopter |

## Mise en œuvre

- Installation — application desktop téléchargée depuis la page d'installation, ou CLI : `curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash`
- Point d'entrée — l'application, ou `goose configure` pour déclarer fournisseur et modèle en CLI
- Prérequis — un modèle qui sait appeler des outils : API, abonnement existant (Claude, ChatGPT, Gemini via ACP) ou serveur local (Ollama, LM Studio, Docker avec un endpoint compatible OpenAI ; fonctionnement hors ligne possible)
- Exécution — sur le poste ; v1.53.0 du 2026-10-02
- Coût — gratuit (Apache-2.0) ; la dépense est celle du modèle

## Écosystème

### Alternatives

- [[OpenCode]] — Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI.
- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.
- [[Qwen Code]] — Agent de code open source (Apache-2.0, TypeScript) pour le terminal, avec plugins d'éditeur : issu de Gemini CLI, il parle aux API OpenAI, Anthropic, Gemini et Qwen et aux modèles locaux Ollama et vLLM.

## Ressources

- Documentation — https://goose-docs.ai/
- Dépôt — https://github.com/aaif-goose/goose

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
