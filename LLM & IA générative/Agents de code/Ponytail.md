---
role: brique
nom: Ponytail
alias: [DietrichGebert/ponytail, ponytail skill]
pitch: "Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
langage: Markdown
alternatives: []
complements: ["[[Superpowers]]", "[[Skills d'Addy Osmani]]", "[[Skills de Matt Pocock]]"]
tags: [agent-skill, skills, code-assistant, agents]
url_docs: https://github.com/DietrichGebert/ponytail
url_repo: https://github.com/DietrichGebert/ponytail
---

# Ponytail

<!-- AUTO:BANDEAU:START -->
> Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **skill** : un prompt unique, `skills/ponytail/SKILL.md`, plus cinq commandes qui le prolongent. Le principe est une échelle que l'agent descend avant d'écrire une ligne : ce code doit-il exister ? existe-t-il déjà dans le dépôt ? la bibliothèque standard le fait-elle ? la plateforme native ? une dépendance déjà installée ? tient-il en une ligne ? Seulement ensuite, le minimum qui marche. L'échelle s'applique **après** avoir lu le code touché : paresseux sur la solution, jamais sur la lecture. Validation aux frontières, perte de données, sécurité et accessibilité restent hors de portée du « moins de code ». Version 4.13.0 du 2026-10-05, MIT, dernier push le 2026-10-05.

Les chiffres de gain sont ceux du projet : −54 % de code (jusqu'à −94 %), −22 % de jetons, −20 % de coût, −27 % de temps, mesurés par l'auteur sur douze tâches d'un dépôt FastAPI + React avec Claude Haiku 4.5, quatre essais. Le README précise que sur un modèle de raisonnement verbeux, le coût et la latence peuvent monter, et que le gain est nul sur du code déjà minimal.

## Les skills

| Skill ou commande | Ce qu'il fait | Quand |
|---|---|---|
| ponytail | Actif toute la session ; applique l'échelle ; trois intensités (lite, full, ultra) ou off, par `/ponytail [niveau]` | Toujours, avant d'écrire du code |
| ponytail-review | Relit un diff (non commité, indexé, branche, lien de PR) et rend une liste de ce qu'il faut supprimer | Avant de commiter ou de fusionner |
| ponytail-audit | Même revue sur tout le dépôt, pas seulement le diff | Reprise d'un dépôt, nettoyage périodique |
| ponytail-debt | Rassemble les raccourcis laissés en commentaire `ponytail:` dans un registre, pour que « plus tard » ne devienne pas « jamais » | Fin de lot, avant une revue de dette |
| ponytail-gain | Affiche le tableau de mesure du benchmark (code, coût, vitesse) | Pour juger l'effet, ou en parler |
| ponytail-help | Aide-mémoire des commandes | À tout moment |

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| L'agent sur-construit : composant maison pour ce qu'une balise native fait, classe de 120 lignes pour une fonction | Le code est déjà minimal : le gain est quasi nul d'après le projet |
| Reprise d'un dépôt à nettoyer : la revue et l'audit donnent une liste de suppressions | Le besoin est un cadre de méthode (spécification, plan, revue) → [[Superpowers]] |
| Un registre de raccourcis assumés, retrouvables | Modèle de raisonnement qui délibère longuement : le projet relève un coût en hausse sur GPT-5.5 |
| Veut une discipline à une idée, installable en une commande | Besoin d'un contrôle imposé sans exception : un skill est du contexte, pas une règle appliquée → hook ou CI |

## Mise en œuvre

- Installation — Claude Code : `/plugin marketplace add DietrichGebert/ponytail` puis `/plugin install ponytail@ponytail`. Codex : `codex plugin marketplace add DietrichGebert/ponytail` puis `codex plugin add ponytail@ponytail`. Autres agents : copier `AGENTS.md` ou installer `skills/ponytail/SKILL.md`
- Point d'entrée — `/ponytail`, puis `/ponytail-review` sur un diff
- Prérequis — un agent hôte capable de skills pour les commandes (Claude Code, Codex, Devin CLI, OpenCode, Gemini, pi, Hermes Agent, Qoder, Grok Build) ; les adaptateurs à instructions seules (Cursor, Windsurf, Cline, Copilot, Kiro, Antigravity) n'ont que la règle toujours active, sans les commandes
- Exécution — dans l'agent hôte, sur le poste ; rien à héberger, aucune configuration obligatoire
- Coût — gratuit, MIT. Le README annonce aussi une offre à venir (liste d'attente) : sans effet sur la licence du dépôt

## Écosystème

### Alternatives

- Aucune page équivalente dans le brain : aucun autre skill de sobriété du code n'y est fiché.

### Compléments

- [[Superpowers]] — Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et vérification avant d'annoncer « terminé ». — Superpowers pilote le cycle, Ponytail y retranche le superflu.
- [[Skills d'Addy Osmani]] — Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle. — son skill `code-simplification` traite aussi la simplification, après coup.
- [[Skills de Matt Pocock]] — Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue. — Ponytail agit sur ce que ces skills font écrire.

## Ressources

- Documentation — https://github.com/DietrichGebert/ponytail
- Dépôt — https://github.com/DietrichGebert/ponytail

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Quel skill pour quelle étape]] — le tableau qui réunit les skills par étape du cycle de vie
- [[Agent skills]] — le mécanisme des skills
- [[Revue, tests et définition de terminé avec un agent]] — la revue du code écrit par l'agent
