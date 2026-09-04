---
role: brique
nom: freebuff
alias: [Freebuff, Codebuff]
pitch: "Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-core
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[Aider]]", "[[Cline]]", "[[Continue]]", "[[pi]]"]
complements: []
tags: [code-assistant, code-generation, agents, multi-agent, cli]
url_docs: https://freebuff.com
url_repo: https://github.com/CodebuffAI/freebuff
---

# freebuff

<!-- AUTO:BANDEAU:START -->
> Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI TypeScript | open-core | en ligne de commande, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Assistant de code utilisable **sans clé API et sans paiement** : les modèles sont hébergés par
l'éditeur et le service est financé par la publicité — c'est le sujet de la fiche, et sa
contrepartie est écrite noir sur blanc par l'éditeur, qui déclare analyser les prompts et les
messages, contenu collé compris, pour personnaliser la publicité, et se réserve l'usage des
soumissions pour développer, entraîner, tester, évaluer et améliorer des modèles.
L'architecture n'est pas un modèle unique mais des **agents spécialisés** — recherche de
fichiers, implémentation, revue, recherche, automatisation navigateur, parallélisation — bâtis
sur Codebuff, le framework multi-agents maison. Traçabilité utile : le dépôt date du 2024-07-09
et c'est l'ancien `CodebuffAI/codebuff`, l'agent terminal payant de la société YC du même nom,
renommé `freebuff`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Essayer un agent de code multi-agents sans souscrire d'abonnement ni poser de clé API | Code client, code interne, contexte on-prem : les prompts partent chez un tiers qui déclare les exploiter pour le ciblage publicitaire et l'entraînement |
| Travail sur du code sans enjeu de confidentialité : projet public, exercice, prototype jetable | **LLM auto-hébergé : non.** Ni BYOK ni endpoint local pour le catalogue Freebuff. Seule ouverture, verbatim du README : le desktop peut faire tourner des agents Claude Code et Codex installés localement avec le compte fournisseur de l'utilisateur — ces modèles connectés sont séparés du catalogue inclus |
| Comparer une approche multi-agents à un agent monolithique, à coût nul | Volume soutenu : trois sessions d'une heure par jour, jusqu'à sept « gagnables » en mode limité |
| | Besoin de stabilité de version : catalogue de modèles imposé et mouvant, aucune garantie d'une version à l'autre |

## Mise en œuvre

- Installation — `npm install -g freebuff`, puis depuis le dépôt de travail : `cd ~/mon-projet` et `freebuff` ; applications desktop macOS, Windows, Linux
- Point d'entrée — CLI dans le dépôt, application desktop, accès web, exécution cloud sur GitHub, ou chat
- Prérequis — un compte Freebuff, aucune clé d'API ; non vérifié : si le CLI npm est buildé depuis ce dépôt, et s'il peut fonctionner sans le backend Freebuff
- Exécution — sur le poste ou en cloud chez l'éditeur ; les modèles, eux, tournent toujours chez lui
- Coût — nul pour l'utilisateur, et payé en données : le client est sous Apache 2.0 mais le service qui l'alimente est hébergé et propriétaire. Catalogue lu dans le README **au 2026-09-01** (susceptible de bouger) : GLM 5.3 Flash (défaut, non métré), GPT-5.6 Luna, DeepSeek V4 Flash 07/31, MiMo 2.5 (défaut en mode limité, non métré), Solar Pro 4 (essai limité dans le temps, 524K de contexte)

## Écosystème

### Alternatives

- [[Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.

## Ressources

- Documentation — https://freebuff.com (site du projet)
- Dépôt — https://github.com/CodebuffAI/freebuff

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Agent patterns]] — patrons d'architecture d'agents
- [[tool-use]] — appel d'outils par un LLM
