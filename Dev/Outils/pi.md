---
role: brique
nom: pi
alias: [pi-coding-agent, earendil-works/pi, pi-ai]
pitch: "Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux, Android (Termux)"
langage: TypeScript
alternatives: ["[[Dev/Outils/Aider|Aider]]", "[[Dev/Outils/Cline|Cline]]", "[[Dev/Outils/Continue|Continue]]", "[[Dev/Outils/freebuff|freebuff]]"]
complements: []
tags: [code-assistant, agents, local-llm, terminal-ui, tool-use]
url_docs: https://github.com/earendil-works/pi/tree/main/packages/coding-agent
url_repo: https://github.com/earendil-works/pi
---

# pi

## Pourquoi

Suite d'outils d'agent en TypeScript, MIT, livrée en cinq paquets npm : `pi-ai` (API LLM unifiée multi-fournisseurs), `pi-agent-core` (runtime, appel d'outils, gestion d'état), `pi-tui` (interface terminal à rendu différentiel), `pi-telemetry` (contrats de télémétrie neutres) et `@earendil-works/pi-coding-agent`, le CLI `pi` qui assemble le tout en assistant de codage.

La particularité par rapport aux autres CLI de codage : le **LLM auto-hébergé est un citoyen de première classe**, pas une option cachée. Le serveur routeur [[Dev/Services/llama.cpp|llama.cpp]] est supporté explicitement (`/login llama.cpp`, gestion des téléchargements et des modèles chargés via `/llama`, sélection via `/model`), et tout endpoint OpenAI-compatible ou Anthropic-compatible se déclare dans `~/.pi/agent/models.json`.

Aucun modèle économique : pas d'offre payante, pas de revente de tokens.

## Quand l'utiliser

- Faire tourner un agent de codage entièrement sur un LLM auto-hébergé, sans passer par un fournisseur cloud.
- Réutiliser la boucle d'agent ou l'API LLM unifiée comme bibliothèque dans un projet, plutôt que d'écrire la sienne.
- Travailler en terminal ou sous tmux, y compris depuis Termux sur Android.
- Basculer entre abonnement (Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot) et clés API (Anthropic, OpenAI, Azure OpenAI, Gemini, Bedrock, Mistral, Groq, DeepSeek, xAI, [[Dev/Services/OpenRouter|OpenRouter]]…) sans changer d'outil.

## Quand NE PAS l'utiliser

- Exécuter du code non fiable sans isolation : pi **n'a aucun système de permissions** (voir Pièges). Prévoir un conteneur, ou choisir un outil qui valide les actions pas à pas → [[Dev/Outils/Cline|Cline]].
- Travailler dans l'éditeur plutôt qu'en terminal → [[Dev/Outils/Continue|Continue]].
- Vouloir une gouvernance de projet claire : éditeur peu identifié, pas de page projet ni de modèle de gouvernance publié.

## Installation & plateformes

- Installation utilisateur : `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`, binaire `pi`.
- Le `npm install` + `npm run build` du README racine est le setup **contributeur**, pas l'installation utilisateur — ne pas confondre.
- Windows (notes de configuration du Terminal fournies), macOS, Linux, Termux sur Android, intégration tmux.
- Pas de site de documentation : elle vit dans le dépôt, sous `packages/coding-agent` et les guides terminal / alias shell / plateformes.

## Pièges

- **Aucun système de permissions intégré.** Le README l'écrit noir sur blanc : pi ne restreint ni le système de fichiers, ni les processus, ni le réseau, ni l'accès aux identifiants. L'isolation est à la charge de l'utilisateur.
- Support MCP non confirmé : aucune mention explicite trouvée dans la documentation. Ne pas le présumer.
- Pas d'`url_docs` stable hors dépôt : les liens de documentation suivent l'arborescence GitHub et peuvent bouger.
- Projet jeune et à éditeur peu identifié — bus factor inconnu.

## Alternatives

- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/freebuff|freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[agent-loops]] — concept : la boucle perception / action d'un agent
- [[tool-use]] — concept : appel d'outils par un LLM
- [[Sandboxing de code généré]] — concept : isoler l'exécution du code produit par un LLM
- Repo : https://github.com/earendil-works/pi
