---
role: brique
nom: Maka
alias: [apache-maka, maka]
pitch: "Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine."
categorie: llm/agent-de-code
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "macOS (Apple Silicon), Windows (preview)"
langage: TypeScript
alternatives: ["[[OpenHands]]", "[[t3code]]"]
complements: []
tags: [audit-log, agents, tool-use, ai-security, code-assistant]
url_docs: https://incubator.apache.org/projects/maka.html
url_repo: https://github.com/apache/maka
---

# Maka

<!-- AUTO:BANDEAU:START -->
> Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | macOS (Apple Silicon), Windows (preview) | — | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Espace de travail d'agent **local-first** dont le parti pris est la traçabilité. Chaque message
du modèle, chaque appel d'outil, chaque résultat d'outil, chaque décision de permission et chaque
fin de tour est écrit dans un **journal append-only** (event sourcing) stocké sur la machine :
une session n'est pas un historique de chat, c'est une suite d'événements rejouable et
vérifiable après coup. Les outils qui franchissent la frontière du sandbox exigent une
approbation explicite, et un seul « Runtime Host » exécute les agents. Les connexions modèle
peuvent viser le cloud, des modèles locaux ou des passerelles compatibles — le journal, lui,
reste local. L'application de chat est expérimentale : le cœur utile est le runtime et son
journal.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Contexte où il faut pouvoir prouver ce qu'un agent a fait, et avec quelle autorisation : audit, conformité, revue d'incident | **Poste Linux ou WSL2 : impossible aujourd'hui.** Linux n'est pas supporté, la cible principale est macOS Apple Silicon, Windows n'existe qu'en preview non signée, et les Mac Intel ne sont pas supportés |
| Rejouer une session d'agent pour comprendre une décision, plutôt que relire un historique de conversation | Production : aucune release Apache officielle n'a encore été publiée, le dépôt bouge tous les jours, et le projet annonce lui-même des formats de données et des commandes CLI susceptibles de changer — l'incubation ASF ne garantit ni release, ni pérennité, ni compatibilité ascendante |
| Vouloir une gouvernance de projet identifiée (ASF) plutôt qu'un dépôt personnel | Isoler du code non fiable : Maka n'est pas un fournisseur de bacs à sable jetables, la frontière de sandbox n'y est qu'un mécanisme interne → [[E2B]] ou [[Daytona]] |

## Mise en œuvre

- Installation — builds nightly desktop depuis les GitHub Releases, paquet CLI sur npm, ou build depuis les sources (`npm ci` puis `npm run dev`) ; pas de formule brew, pas d'image Docker, pas de binaire officiel signé
- Point d'entrée — application desktop Electron, plus une CLI ; le journal append-only est écrit sur la machine
- Prérequis — macOS Apple Silicon (cible principale) ou Windows en preview ; un accès modèle, cloud, local ou par passerelle
- Exécution — sur le poste ; un seul « Runtime Host » exécute les agents
- Coût — gratuit, Apache-2.0 ; la dépense réelle est celle du modèle branché

## Écosystème

### Alternatives

- [[OpenHands]] — Agent de développement autonome open-source (ex-OpenDevin, All Hands AI, MIT) — écrit du code, exécute des commandes shell et navigue le web pour réaliser des tâches d'ingénierie de bout en bout ; self-host ou OpenHands Cloud managé.
- [[t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.

## Ressources

- Documentation — https://incubator.apache.org/projects/maka.html (page de statut d'incubation ASF ; pas de site dédié — `docs/` et `ARCHITECTURE.md` vivent dans le dépôt)
- Dépôt — https://github.com/apache/maka

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
