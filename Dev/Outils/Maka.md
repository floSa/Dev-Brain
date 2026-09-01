---
galaxie: dev
type: outil
nom: Maka
alias: [apache-maka, maka]
pitch: "Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine."
categorie: tooling/code-assistant
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "macOS (Apple Silicon), Windows (preview)"
langage: TypeScript
status: en-eval
alternatives: ["[[Dev/Services/OpenHands|OpenHands]]", "[[Dev/Outils/t3code|t3code]]"]
tags: [audit-log, agents, tool-use, ai-security, code-assistant]
url_docs: https://incubator.apache.org/projects/maka.html
url_repo: https://github.com/apache/maka
---

# Maka

## Pourquoi

Espace de travail d'agent **local-first** dont le parti pris est la traçabilité. Chaque message du modèle, chaque appel d'outil, chaque résultat d'outil, chaque décision de permission et chaque fin de tour est écrit dans un **journal append-only** (event sourcing) stocké sur la machine. La session n'est pas un historique de chat : c'est une suite d'événements rejouable et vérifiable après coup.

Les outils qui franchissent la frontière du sandbox exigent une approbation explicite. Un seul « Runtime Host » exécute les agents. Les connexions modèle peuvent viser le cloud, des modèles locaux ou des passerelles compatibles — le journal, lui, reste local.

Projet en **incubation à l'Apache Software Foundation**. Apache-2.0, écrit en TypeScript sur Electron.

## Quand l'utiliser

- Contexte où il faut pouvoir prouver ce qu'un agent a fait, et avec quelle autorisation : audit, conformité, revue d'incident.
- Rejouer une session d'agent pour comprendre une décision, plutôt que relire un historique de conversation.
- Vouloir une gouvernance de projet identifiée (ASF) plutôt qu'un dépôt personnel.

## Quand NE PAS l'utiliser

- **Sous Linux : impossible aujourd'hui.** Linux n'est pas encore supporté, la cible principale est macOS Apple Silicon, Windows n'existe qu'en preview non signée, et les Mac Intel ne sont pas supportés. C'est le point bloquant pour un poste WSL2 ou Linux.
- En production : **aucune release Apache officielle n'a encore été publiée**, et le projet annonce lui-même des formats de données et des commandes CLI susceptibles de changer.
- Pour isoler du code non fiable : Maka n'est pas un fournisseur de bacs à sable jetables — la frontière de sandbox n'y est qu'un mécanisme interne. Pour cet usage → [[Dev/Services/E2B|E2B]] ou [[Dev/Services/Daytona|Daytona]].
- Pour éditer du code au fil de l'eau dans l'éditeur → [[Dev/Outils/Cline|Cline]], [[Dev/Outils/Continue|Continue]].

## Installation & plateformes

- Builds nightly desktop depuis les GitHub Releases, paquet CLI sur npm, ou build depuis les sources (`npm ci` puis `npm run dev`).
- Pas de formule brew, pas d'image Docker, pas de binaire officiel signé.
- Documentation : dossier `docs/` et `ARCHITECTURE.md` du dépôt, plus la page de statut d'incubation ASF. Pas de site dédié.

## Pièges

- Linux absent, Windows instable : la portabilité annoncée n'est pas encore là.
- L'application de chat est expérimentale ; le cœur utile est le runtime et son journal.
- Incubation ASF : le statut ne garantit ni release, ni pérennité, ni compatibilité ascendante.
- `status: en-eval` ici plutôt que `actif` — le dépôt bouge tous les jours, mais rien n'est publié.

## Alternatives

- [[Dev/Services/OpenHands|OpenHands]] — Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé.
- [[Dev/Outils/t3code|t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — concept : isoler l'exécution du code produit par un LLM
- [[agent-loops]] — concept : la boucle perception / action d'un agent
- [[Tool use patterns]] — concept : patrons d'appel d'outils
- Repo : https://github.com/apache/maka · Incubation : https://incubator.apache.org/projects/maka.html
