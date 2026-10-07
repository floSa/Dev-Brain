---
role: hub
nom: Agents de code
alias: [assistants de code, agents de codage]
pitch: Les agents qui lisent et modifient un dépôt — dans le terminal, dans l'éditeur, ou au-dessus des deux.
domaines: [ai-eng]
tags: [code-assistant, code-generation, agents, agent-skill, mcp]
---

# Agents de code

> Les agents qui lisent et modifient un dépôt — dans le terminal, dans l'éditeur, ou au-dessus des deux.

## Ce qu'il faut comprendre

- Ce dossier contient des **agents déjà écrits**, à installer et à utiliser. Les bibliothèques pour en écrire un sont dans [[Agents]] ; la distinction est celle entre un produit et une brique, et c'est elle qui range chaque fiche ici ou là.
- Trois formes coexistent, et le choix se fait sur le **point d'insertion dans le poste de travail**, pas sur les capacités annoncées : dans le terminal, à côté de git ([[Aider]], [[pi]], [[freebuff]], [[OpenCode]], [[Goose]], [[Qwen Code]]) ; dans l'éditeur, avec le contexte de l'IDE ([[Cline]], [[Continue]], [[Zoo Code]], [[Kilo Code]], ce dernier aussi en CLI) ; au-dessus des CLI déjà installées, comme plan de contrôle ([[t3code]], [[Maka]]).
- La couche qui compte le plus au quotidien n'est pas le modèle mais le **harnais** : quels fichiers sont lus, quels outils sont exposés, quel contexte est rechargé à chaque tour, et quelle action demande une confirmation. Cf. [[Harnais d'agent]] et [[Context engineering]] — à modèle égal, deux harnais donnent des résultats sans rapport.
- Cette famille a produit un objet propre, le **skill** : une compétence packagée qui étend ou contraint le comportement de l'agent, installée dans le dépôt ou dans l'outil. [[Agent skills]] en décrit le mécanisme ; [[BMAD]] en fait un processus complet (brief → PRD → architecture → stories), [[Spec Kit]] en fait une spécification exécutable, [[i-have-adhd]] ne contraint que le format de sortie. Ce sont trois usages du même levier, du plus lourd au plus léger.
- Le **contexte du dépôt** est le point dur, et deux réponses s'opposent : laisser l'agent chercher (grep, lecture à la demande) ou lui donner une carte préalable — c'est ce que fait [[Graphify]] en transformant le dépôt en graphe interrogeable. La seconde coûte une étape d'indexation et fait gagner sur les gros dépôts.
- La **mémoire entre sessions** est le manque le plus visible de ces outils : chaque session repart de zéro. [[ai-memory]] y répond par un serveur MCP qui consolide les sessions en wiki versionné, et permet de reprendre sous un agent une tâche entamée sous un autre. Cf. [[Agent memory]].
- **Un agent qui exécute du code exécute du code**, y compris ce qu'il a lui-même écrit. [[Sandboxing de code généré]] n'est pas une précaution optionnelle sur un dépôt de travail ; c'est aussi pour cette raison que [[Maka]] journalise chaque appel d'outil et chaque décision de permission en append-only, et que [[swarm-forge]] isole chaque agent dans son propre worktree git.
- La comparaison de ces outils par **benchmark** est à lire avec méfiance : [[Code and math benchmarks]] mesure des tâches fermées et vérifiables, ce qui ne dit presque rien de la tenue sur un dépôt réel, avec son historique, ses conventions et ses tests lents.
- **La méthode autour de l'agent n'est pas ici.** Cycle de vie du projet, spécification, fichiers de contexte, revue, boucle de Ralph, worktrees : ces pages sont des méthodes, rangées dans [[Gestion de projet]] ; ce dossier garde les agents eux-mêmes.
- **Libre seulement.** Ce dossier ne range que des agents sous licence libre vérifiée dans le dépôt. Écartés le 2026-10-04, cités ici en texte simple : Crush (Charm, licence FSL-1.1-MIT, donc source-available ; successeur du dépôt Go `opencode-ai/opencode`, archivé) ; Roo Code (Apache-2.0 mais extension fermée le 2026-05-15, dépôt archivé ; son fork actif Zoo Code a sa fiche) ; Kimi CLI (dépôt archivé) ; Plandex (dernier push en 2025-10). Voisins déjà au brain, rangés ailleurs : [[OpenHands]], [[Hermes Agent]], [[OpenClaw]].
- Deux points de vigilance sur les fiches de ce dossier, et ils ne sont pas techniques : le **modèle économique** ([[freebuff]] finance des modèles hébergés par la publicité et exploite les prompts pour le ciblage) et la **licence** ([[swarm-forge]] n'en déclare aucune, [[BMAD]] porte une clause de marque).

## Choisir

- Éditer un dépôt en langage naturel depuis le terminal, avec commits automatiques → [[Aider]].
- Un agent autonome dans VS Code, avec validation pas-à-pas et MCP → [[Cline]].
- Un assistant multi-éditeurs (VS Code, JetBrains) avec le modèle de mon choix → [[Continue]].
- Un agent de terminal libre avec n'importe quel fournisseur, ou un serveur local → [[OpenCode]].
- Un agent généraliste (code, recherche, automatisation) en desktop et en CLI → [[Goose]].
- Un agent de terminal avec des modèles Qwen ou un serveur local (Ollama, vLLM) → [[Qwen Code]].
- Un agent à modes (Code, Architect, Debug) dans VS Code, dans la lignée de Roo Code → [[Zoo Code]].
- Le même agent dans VS Code, JetBrains et le terminal, avec clé propre ou modèle local → [[Kilo Code]].
- Piloter plusieurs CLI d'agents déjà installées depuis une seule interface → [[t3code]].
- Un journal rejouable de tout ce que l'agent a fait sur ma machine → [[Maka]].
- Une boîte à outils TypeScript pour bâtir mon propre agent de code → [[pi]].
- Imposer un processus de spécification avant l'implémentation → [[Spec Kit]], ou [[BMAD]] pour un cycle complet à rôles nommés.
- Ne changer que la forme des réponses de l'agent → [[i-have-adhd]].
- Donner à l'agent la structure du dépôt avant qu'il ne cherche → [[Graphify]].
- Retrouver le contexte d'une session à l'autre, ou d'un agent à l'autre → [[ai-memory]].
- Faire travailler plusieurs agents en parallèle sur des worktrees isolés → [[swarm-forge]], licence non déclarée.
- Un agent gratuit sans clé API, en acceptant l'exploitation des prompts → [[freebuff]].
- Écrire moi-même la boucle d'agent → [[Agents]], pas ce dossier.

<!-- AUTO:START -->
### Briques
- [[ai-memory]] — Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.
- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story.
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.
- [[Goose]] — Agent généraliste open source (Apache-2.0, Rust, Linux Foundation) : application desktop, CLI et API, plus de 15 fournisseurs et des extensions MCP, avec Ollama pour les modèles locaux.
- [[Graphify]] — Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.
- [[i-have-adhd]] — Skill/plugin MIT pour agents de code (Claude Code, Cursor, Codex, Gemini, Qwen, Kimi) imposant dix règles de sortie : action en premier, étapes numérotées, état rappelé à chaque tour, ni préambule ni récapitulatif.
- [[Kilo Code]] — Agent de code open source (MIT, TypeScript) pour VS Code, JetBrains et le terminal, bâti sur le code d'OpenCode : agents Code, Plan, Ask et Debug, plus de 30 fournisseurs par clé propre et les serveurs locaux Ollama et LM Studio.
- [[Maka]] — Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.
- [[OpenCode]] — Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI.
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.
- [[Qwen Code]] — Agent de code open source (Apache-2.0, TypeScript) pour le terminal, avec plugins d'éditeur : issu de Gemini CLI, il parle aux API OpenAI, Anthropic, Gemini et Qwen et aux modèles locaux Ollama et vLLM.
- [[Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).
- [[swarm-forge]] — Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée.
- [[t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.
- [[Zoo Code]] — Extension VS Code open source (Apache-2.0, TypeScript), suite communautaire de Roo Code : modes Code, Architect, Ask, Debug et personnalisés, serveurs MCP, et le fournisseur de modèles de son choix dont Ollama et LM Studio.

### Comparatifs
- [[Comparatif - Assistants de code IA]]
<!-- AUTO:END -->
