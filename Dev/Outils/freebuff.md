---
galaxie: dev
type: outil
nom: freebuff
alias: [Freebuff, Codebuff]
pitch: "Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage."
categorie: llm/agent-de-code
famille: cli
domaines: [ai-eng]
licence_type: open-core
os: "Windows, macOS, Linux"
langage: TypeScript
status: actif
alternatives: ["[[Dev/Outils/Aider|Aider]]", "[[Dev/Outils/Cline|Cline]]", "[[Dev/Outils/Continue|Continue]]", "[[Dev/Outils/pi|pi]]"]
tags: [code-assistant, code-generation, agents, multi-agent, cli]
url_docs: https://freebuff.com
url_repo: https://github.com/CodebuffAI/freebuff
---

# freebuff

## Pourquoi

Assistant de code utilisable **sans clé API et sans paiement** : les modèles sont hébergés par l'éditeur et le service est financé par la publicité. Architecture non pas un modèle unique mais des **agents spécialisés** — recherche de fichiers, implémentation, revue, recherche, automatisation navigateur, parallélisation — bâtis sur Codebuff, le framework multi-agents maison. Surfaces multiples : desktop (macOS, Windows, Linux), CLI, web, cloud sur GitHub, chat.

Traçabilité utile : le dépôt date du 2024-07-09 et c'est l'ancien `CodebuffAI/codebuff`, l'agent terminal payant de la société YC du même nom, renommé `freebuff`.

Le code du dépôt est sous **Apache 2.0**, mais le service qui l'alimente est hébergé et propriétaire : d'où `licence_type: open-core` — client libre, backend modèles fermé.

## Quand l'utiliser

- Essayer un agent de code multi-agents sans souscrire d'abonnement ni poser de clé API.
- Travail sur du code sans enjeu de confidentialité : projet public, exercice, prototype jetable.
- Comparer une approche multi-agents à un agent monolithique, à coût nul.

## Quand NE PAS l'utiliser

- Code client, code interne, contexte on-prem : les prompts partent chez un tiers qui déclare les exploiter (voir Pièges).
- **LLM auto-hébergé : non.** Pas de BYOK ni d'endpoint local pour le catalogue Freebuff → [[Dev/Outils/pi|pi]] ou [[Dev/Outils/Continue|Continue]]. Seule ouverture, verbatim du README : le desktop peut faire tourner des agents Claude Code et Codex installés localement avec le compte fournisseur de l'utilisateur ; ces modèles connectés sont séparés du catalogue inclus.
- Besoin de volume soutenu : les sessions journalières sont plafonnées.
- Vouloir maîtriser son modèle et sa facture → [[Dev/Outils/Aider|Aider]].

## Installation & plateformes

- `npm install -g freebuff`, puis depuis le dépôt de travail : `cd ~/mon-projet` et `freebuff`.
- Applications desktop macOS, Windows, Linux ; accès web et exécution cloud sur GitHub.
- Catalogue de modèles inclus, lu dans le README **au 2026-09-01** (susceptible de bouger) : GLM 5.3 Flash (défaut, non métré), GPT-5.6 Luna, DeepSeek V4 Flash 07/31, MiMo 2.5 (défaut en mode limité, non métré), Solar Pro 4 (essai limité dans le temps, 524K de contexte).
- Non vérifié : si le CLI npm est buildé depuis ce dépôt, et s'il peut fonctionner sans le backend Freebuff.

## Pièges

Le « gratuit » a une contrepartie, et c'est le point central de la fiche.

- Sessions journalières plafonnées : trois sessions d'une heure par jour, jusqu'à sept « gagnables » en mode limité.
- L'éditeur annonce analyser les prompts et messages, **y compris le contenu collé**, pour personnaliser la publicité.
- L'éditeur se réserve l'usage des soumissions pour développer, entraîner, tester, évaluer et améliorer des modèles.
- Face à [[Dev/Outils/Aider|Aider]] (clé API à soi, aucune télémétrie modèle), c'est le différenciateur négatif : le code envoyé n'est pas confidentiel.
- Catalogue de modèles imposé et mouvant : pas de garantie de stabilité d'une version à l'autre.

## Alternatives

- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/pi|pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif des assistants IA de code
- [[Multi-agent systems]] — concept : systèmes à plusieurs agents coopérants
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[Agent patterns]] — concept : patrons d'architecture d'agents
- [[tool-use]] — concept : appel d'outils par un LLM
- Site : https://freebuff.com
