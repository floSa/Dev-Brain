---
role: brique
nom: OpenCode
alias: [opencode, anomalyco/opencode, sst/opencode]
pitch: "Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[Aider]]", "[[pi]]", "[[Goose]]"]
complements: []
tags: [code-assistant, code-generation, llm, agents, local-llm, terminal-ui]
url_docs: https://opencode.ai/docs/
url_repo: https://github.com/anomalyco/opencode
---

# OpenCode

<!-- AUTO:BANDEAU:START -->
> Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de code qui s'exécute dans le terminal, avec une interface texte (TUI) : on lui décrit une tâche, il lit le dépôt, édite des fichiers et lance des commandes. Une application desktop (bêta, macOS, Windows, Linux) existe à côté. Il ne dépend d'aucun modèle : les fournisseurs passent par le AI SDK et Models.dev, soit plus de 75 d'après la documentation, abonnements (ChatGPT Plus/Pro, GitHub Copilot, Claude Pro/Max) comme clés d'API.

**Trois projets ont porté ce nom — c'est le piège de cette fiche.**

| Dépôt | État | Ce que c'est |
|---|---|---|
| `anomalyco/opencode` (ex `sst/opencode`, le lien ancien redirige) | actif, MIT, v1.18.34 du 2026-09-30 | **Celui de cette fiche.** TypeScript |
| `opencode-ai/opencode` | **archivé** (dernier push 2025-09-18, v0.0.55), MIT | Agent en Go. Son README annonce que le projet « a continué sous le nom Crush » |
| `charmbracelet/crush` | actif, licence **FSL-1.1-MIT** | Le successeur du précédent. Source-available, donc **sans fiche** ici (cf. [[Agents de code]]) |

Le terminal d'`anomalyco` n'est donc pas le Crush de Charm, malgré le nom : les deux projets ont divergé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent de terminal libre qui ne lie à aucun fournisseur, y compris un modèle servi sur place | Le terminal n'est pas le poste de travail voulu : l'intégration éditeur est le cas d'usage de [[Cline]] ou de [[Continue]] |
| Brancher un modèle auto-hébergé (Ollama, llama.cpp, LM Studio, vLLM) via un endpoint compatible OpenAI | Besoin d'un contrôle fin du réseau et des fichiers : à vérifier dans la documentation des permissions avant de l'exposer sur un dépôt client |
| Réutiliser des abonnements existants plutôt que payer des clés d'API | Projet très actif (releases quasi quotidiennes) : verrouiller une version en production |

## Mise en œuvre

- Installation — script `curl -fsSL https://opencode.ai/install | bash`, ou `npm i -g opencode-ai`, Homebrew, Scoop, Chocolatey, pacman, mise, Nix ; application desktop en bêta (`.dmg`, `.exe`, `.deb`, `.rpm`, `.AppImage`)
- Point d'entrée — commande `opencode` dans le dépôt ; `/connect` pour enregistrer un fournisseur, `/models` pour choisir le modèle
- Prérequis — un accès à un modèle : abonnement, clé d'API ou serveur local
- Modèle local — déclarer un fournisseur `@ai-sdk/openai-compatible` avec son `baseURL` dans `opencode.json`
- Exécution — sur le poste, en terminal ; l'éditeur propose en plus ses offres hébergées (OpenCode Zen et Go, modèles sélectionnés), facultatives
- Coût — le logiciel est gratuit (MIT) ; la dépense est celle du modèle, nulle en local

## Écosystème

### Alternatives

- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.
- [[Goose]] — Agent généraliste open source (Apache-2.0, Rust, Linux Foundation) : application desktop, CLI et API, plus de 15 fournisseurs et des extensions MCP, avec Ollama pour les modèles locaux.

### Compléments

- voisin : [[t3code]] — pilote OpenCode parmi les CLI qu'il supporte.

## Ressources

- Documentation — https://opencode.ai/docs/
- Dépôt — https://github.com/anomalyco/opencode

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
