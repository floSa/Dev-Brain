---
role: brique
nom: Skills de Matt Pocock
alias: [mattpocock/skills, Skills For Real Engineers, mattpocock-skills]
pitch: "Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
langage: Markdown
alternatives: ["[[Superpowers]]", "[[Skills d'Addy Osmani]]"]
complements: ["[[Ponytail]]"]
tags: [agent-skill, skills, code-assistant, agents]
url_docs: https://github.com/mattpocock/skills
url_repo: https://github.com/mattpocock/skills
---

# Skills de Matt Pocock

<!-- AUTO:BANDEAU:START -->
> Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **jeu de skills**, dépôt `mattpocock/skills`, sous-titré « Skills For Real Engineers » : les skills que Matt Pocock (Total TypeScript) dit utiliser chaque jour. Le parti pris est écrit dans le README : les méthodes qui possèdent le processus (GSD, BMAD, Spec Kit) retirent le contrôle et rendent les bogues du processus difficiles à corriger ; ici, chaque skill est **petit, adaptable, composable**, et marche avec n'importe quel modèle. Trente et un skills hors dossier `in-progress`, rangés en `engineering`, `productivity` et `misc`. Deux familles : les skills **invoqués par l'utilisateur** (`/grill-me`, orchestrent) et ceux que le **modèle** peut invoquer seul (disciplines réutilisables) ; un skill d'orchestration peut appeler des skills de discipline, jamais un autre skill d'orchestration. Version 1.3.1 du 2026-10-04, MIT, dernier push le 2026-10-07.

## Les skills

Les quatre échecs que le README attaque, dans l'ordre : l'agent n'a pas fait ce qu'on voulait (interrogatoire), il est trop bavard (langage commun), le code ne marche pas (boucles de retour, TDD), le code devient une boule de boue (conception).

| Étape | Skill | Ce qu'il fait | Qui l'appelle |
|---|---|---|---|
| Orientation | ask-matt | Dit quel skill ou quel enchaînement convient à la situation | Utilisateur |
| Orientation | setup-matt-pocock-skills | Une fois par dépôt : tracker de tickets, étiquettes de tri, emplacement des documents | Utilisateur |
| Cadrer | grill-me | Interrogatoire sans relâche sur un plan, jusqu'à résoudre chaque branche | Utilisateur |
| Cadrer | grill-with-docs | Même interrogatoire, qui construit aussi le modèle de domaine : glossaire `GLOSSARY.md` et ADR tenus à jour | Utilisateur |
| Cadrer | grilling | Primitive d'entretien réutilisée par `grill-me`, `triage`, `wayfinder`… | Modèle |
| Cadrer | domain-modeling | Affûte le modèle de domaine : termes contre glossaire, cas limites, ADR | Modèle |
| Cadrer | research | Enquête sur des sources primaires, résultats cités dans un fichier Markdown du dépôt, en agent d'arrière-plan | Modèle |
| Cadrer | to-questionnaire | Transforme une décision qu'on ne peut pas prendre seul en questionnaire pour la bonne personne | Utilisateur |
| Spécifier | to-spec | Convertit la conversation en spécification publiée dans le tracker, sans nouvel entretien | Utilisateur |
| Planifier | to-tickets | Découpe un plan en tickets en balle traçante, avec leurs dépendances | Utilisateur |
| Planifier | wayfinder | Pour un chantier plus gros qu'une session : carte partagée de tickets de décision, résolus un à un | Utilisateur |
| Planifier | triage | Fait passer les tickets par une machine à états de rôles de tri | Utilisateur |
| Construire | implement | Réalise une spécification ou un lot de tickets, en TDD, clôt par `/code-review` avant le commit | Utilisateur |
| Construire | implement-spec | Implémente toute une spécification sur une branche d'intégration, des sous-agents en parallèle sur les tickets prêts | Utilisateur |
| Construire | tdd | Boucle rouge, vert, refactor, une tranche verticale à la fois | Modèle |
| Construire | prototype | Prototype jetable pour répondre à une question de conception (un fichier HTML, ou plusieurs variantes d'interface) | Modèle |
| Construire | codebase-design | Vocabulaire et discipline des modules profonds : beaucoup de comportement derrière une petite interface | Modèle |
| Vérifier | diagnosing-bugs | Boucle de diagnostic : un retour qui passe au rouge sur ce bogue, minimiser, hypothèse, instrumenter, corriger, test de régression | Modèle |
| Relire | code-review | Revue du diff sur deux axes, normes du dépôt et conformité à la spécification, par deux sous-agents séparés | Modèle |
| Relire | improve-codebase-architecture | Cherche des occasions d'approfondir les modules, en rapport HTML, puis interroge sur celle qu'on retient | Utilisateur |
| Livrer | pr | Forme du corps d'une pull request : résumé visuel, preuves avant et après, risque de fusion | Modèle |
| Livrer | wizard | Génère un assistant bash interactif pour les étapes que seul un humain peut faire (identifiants, tableau de bord tiers, bascule) | Modèle |
| Après | retro | Propose des améliorations de l'environnement de l'agent (navigation, contrôles, normes), par gravité | Utilisateur |
| Reprise | handoff | Condense la conversation en document de passation pour un autre agent | Utilisateur |
| Reprise | wait-what | Reformule un message mal compris, avec le contexte manquant, dans le vocabulaire du glossaire | Utilisateur |
| Rédaction | writing-for-agents | Écrire pour des agents : skills, `AGENTS.md` / `CLAUDE.md`, tout document atteint par un pointeur | Modèle |
| Apprendre | teach | Enseigne une compétence sur plusieurs sessions, le dossier courant servant d'espace d'enseignement | Utilisateur |
| Dépôt (misc) | setup-pre-commit | Installe Husky, lint-staged (Prettier), typage et tests au commit : chaîne JavaScript | — |
| Dépôt (misc) | git-guardrails-claude-code | Pose des hooks Claude Code qui bloquent les commandes git destructrices (push, reset --hard, clean, branch -D) | — |
| Dépôt (misc) | migrate-to-shoehorn | Remplace les assertions `as` dans les tests TypeScript par `@total-typescript/shoehorn` | — |
| Dépôt (misc) | scaffold-exercises | Crée des squelettes d'exercices de cours qui passent le lint de l'auteur | — |

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Garder la main sur le processus : chaque skill fait une chose, on enchaîne soi-même | Vouloir un cycle complet qui s'enchaîne seul → [[Superpowers]] |
| Le point faible est l'écart entre ce qu'on veut et ce que l'agent comprend : `grill-me` et `grill-with-docs` | Couverture large (sécurité, observabilité, performance web) → [[Skills d'Addy Osmani]] |
| Travailler avec un tracker de tickets (GitHub, GitLab, fichiers locaux) : spécification et tickets y sont publiés | Projet Python hors TypeScript : `setup-pre-commit`, `migrate-to-shoehorn` et `scaffold-exercises` ciblent l'écosystème de l'auteur, et `setup-pre-commit` installe Husky, pas [[pre-commit]] |
| Aimer lire et modifier les skills : l'installateur copie des fichiers modifiables | Vouloir un contrôle sans exception : `git-guardrails-claude-code` bloque aussi `git push` ; à retirer d'un flux qui pousse par petits commits |

## Mise en œuvre

- Installation — Claude Code : `claude plugins install mattpocock-skills` (bundle géré, en lecture seule). Autres agents ou skills modifiables : `npx skills@latest add mattpocock/skills`. Ne pas installer les deux : chaque skill serait en double
- Point d'entrée — `/setup-matt-pocock-skills` une fois par dépôt, puis `/grill-me` ou `/grill-with-docs` avant tout changement
- Prérequis — un agent hôte ; Node pour l'installateur `npx`
- Exécution — dans l'agent hôte, sur le poste ; rien à héberger
- Coût — gratuit, MIT ; l'auteur tient une lettre d'information. Le plugin du marketplace d'Anthropic peut avoir quelques jours de retard sur le dépôt

## Écosystème

### Alternatives

- [[Superpowers]] — Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et vérification avant d'annoncer « terminé ».
- [[Skills d'Addy Osmani]] — Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle.
- voisin : [[Spec Kit]] — le README le cite comme exemple de méthode qui possède le processus.
- voisin : [[BMAD]] — idem ; ici, aucun rôle d'agent imposé.
- voisin : [[i-have-adhd]] — règles de forme de la sortie, à côté de `writing-for-agents`.

### Compléments

- [[Ponytail]] — Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie. — retranche le code superflu que `implement` produit.

## Ressources

- Documentation — https://github.com/mattpocock/skills
- Dépôt — https://github.com/mattpocock/skills

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Quel skill pour quelle étape]] — le tableau qui réunit les skills par étape du cycle de vie
- [[Agent skills]] — le mécanisme des skills
- [[ADR et design docs]] — `grill-with-docs` tient les ADR à jour
- [[Développement piloté par la spécification]] — `to-spec` et `to-tickets` en sont une version légère
