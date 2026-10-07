---
role: brique
nom: Superpowers
alias: [obra/superpowers, superpowers skills]
pitch: "Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et vérification avant d'annoncer « terminé »."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
langage: Markdown
alternatives: ["[[Skills d'Addy Osmani]]", "[[Skills de Matt Pocock]]"]
complements: ["[[Ponytail]]"]
tags: [agent-skill, skills, code-assistant, agents]
url_docs: https://github.com/obra/superpowers
url_repo: https://github.com/obra/superpowers
---

# Superpowers

<!-- AUTO:BANDEAU:START -->
> Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et vérification avant d'annoncer « terminé ».

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **jeu de skills** : quinze dossiers `SKILL.md`, plus un petit script de démarrage, que l'agent hôte charge quand la tâche s'y prête. Le dépôt se présente comme « une méthodologie complète de développement » : dès que l'agent voit qu'on construit quelque chose, il ne code pas, il interroge. Il tire une spécification de la conversation, la montre par morceaux lisibles, puis écrit un plan assez détaillé pour un exécutant sans contexte, et enfin déroule le plan tâche par tâche. Le dépôt annonce des sessions autonomes de plusieurs heures. Les skills sont **obligatoires, pas facultatifs** : l'agent consulte la liste avant chaque tâche. Auteur : Jesse Vincent (Prime Radiant), licence MIT, version 6.4.2 du 2026-09-25, dernier push le 2026-10-06.

## Les skills

Ordre du cycle. « Quand » dit à quelle étape le skill se déclenche ; il s'active seul, sans commande.

| Skill | Ce qu'il fait | Quand |
|---|---|---|
| using-superpowers | Présente le système de skills ; injecté au démarrage de la session (et après compaction) pour que l'agent cherche un skill avant toute tâche | Début de session |
| brainstorming | Affine l'idée par questions, explore des variantes, présente le design par sections à valider, sauvegarde le document de design | Avant d'écrire du code |
| using-git-worktrees | Crée un espace de travail isolé sur une nouvelle branche, lance l'installation, vérifie que les tests passent au départ | Après validation du design |
| writing-plans | Découpe le travail en tâches de 2 à 5 minutes, avec chemins exacts, code complet et étapes de vérification | Avec un design validé |
| subagent-driven-development | Un sous-agent neuf par tâche, relecture à deux niveaux : conformité à la spécification, puis qualité du code | Plan prêt, mode le plus rigoureux |
| executing-plans | Exécute le plan dans la session courante, avec une seule revue de la branche à la fin | Plan prêt, mode le moins cher |
| dispatching-parallel-agents | Lance des sous-agents concurrents sur des tâches indépendantes | Plusieurs tâches sans dépendance |
| test-driven-development | Cycle RED-GREEN-REFACTOR : test qui échoue, code minimal, test qui passe ; supprime le code écrit avant le test ; fournit un guide d'anti-patrons de test | Pendant l'implémentation |
| requesting-code-review | Relit le travail contre le plan, classe les défauts par gravité ; un défaut critique bloque la suite | Entre deux tâches |
| receiving-code-review | Cadre la façon de répondre aux retours de revue | À la réception d'une revue |
| systematic-debugging | Cause racine en quatre phases, avec traçage de la cause, défense en profondeur et attente sur condition | Test rouge, comportement inattendu |
| verification-before-completion | Exige de vérifier que le correctif tient avant de le déclarer | Avant d'annoncer « terminé » |
| finishing-a-development-branch | Vérifie les tests, propose fusion, PR, garde ou abandon, nettoie le worktree | Tâches finies |
| writing-skills | Guide la création d'un skill, avec méthode de test | Écrire ses propres skills |
| diagnosing-superpowers | Lit la transcription d'une session ratée, rapporte les faits avec preuves ligne à ligne, peut préparer un paquet expurgé pour un rapport de bogue | Un skill se déclenche à tort ou jamais |

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir une méthode complète, déjà enchaînée, sans la composer soi-même | Composer ses propres briques une à une, avec peu de règles imposées → [[Skills de Matt Pocock]] |
| Projet neuf ou fonctionnalité large : le brainstorming et le plan évitent de coder à côté | Petite correction : le cycle brainstorming, plan, revue est surdimensionné |
| Tâches longues confiées à des sous-agents, avec revue après chaque tâche | Besoin d'une couverture large (sécurité, observabilité, API, performance) → [[Skills d'Addy Osmani]] |
| Culture test d'abord : le TDD est imposé, pas suggéré | Code déjà écrit sans tests, à ne pas jeter : le skill supprime le code écrit avant le test |

## Mise en œuvre

- Installation — Claude Code : `/plugin install superpowers@claude-plugins-official`. Chaque agent a sa commande (Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode, Pi, Qwen Code, Hermes Agent…) ; installer séparément pour chacun
- Point d'entrée — rien à lancer : les skills se déclenchent seuls, `brainstorming` d'abord quand on décrit un projet
- Prérequis — un agent hôte supporté, accès à GitHub ou à une place de marché de plugins
- Exécution — dans l'agent hôte, sur le poste ; rien à héberger
- Coût — gratuit, MIT ; les sous-agents et les revues multiplient les appels au modèle, donc la facture de l'agent hôte

## Écosystème

### Alternatives

- [[Skills d'Addy Osmani]] — Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle.
- [[Skills de Matt Pocock]] — Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue.
- voisin : [[BMAD]] — jeu d'agents agiles qui couvre du brief aux stories ; plus lourd, avec des rôles nommés.
- voisin : [[Spec Kit]] — la spécification exécutable seule, sans le reste du cycle.
- voisin : [[i-have-adhd]] — règles de forme de la sortie, aucune méthode.

### Compléments

- [[Ponytail]] — Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie. — freine ce que le plan détaillé de Superpowers tend à produire.

## Ressources

- Documentation — https://github.com/obra/superpowers
- Dépôt — https://github.com/obra/superpowers
- Article — https://blog.fsck.com/2025/10/09/superpowers/

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Quel skill pour quelle étape]] — le tableau qui réunit les skills par étape du cycle de vie
- [[Agent skills]] — le mécanisme des skills
- [[Cycle de vie d'un projet assisté par agent]] — le cycle que ces skills outillent
