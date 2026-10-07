---
role: brique
nom: pm-skills
alias: [phuryn/pm-skills, PM Skills Marketplace]
pitch: "Skills MIT de gestion de produit pour Claude Code et d'autres agents (69 skills, 42 commandes, 9 plugins) : découverte, PRD, histoires, sprints, lancement."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
langage: Markdown
alternatives: []
complements: ["[[Skills d'Addy Osmani]]"]
tags: [agent-skill, skills, project-management, agents]
url_docs: https://github.com/phuryn/pm-skills
url_repo: https://github.com/phuryn/pm-skills
---

# pm-skills

<!-- AUTO:BANDEAU:START -->
> Skills MIT de gestion de produit pour Claude Code et d'autres agents (69 skills, 42 commandes, 9 plugins) : découverte, PRD, histoires, sprints, lancement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Une **place de marché de plugins** pour agents, côté **produit** et non côté code : soixante-neuf skills et quarante-deux commandes en neuf plugins, par Paweł Huryn (lettre The Product Compass). Chaque skill encode un cadre connu (découverte continue de Teresa Torres, évaluation des hypothèses, cadres de priorisation) et déroule l'analyse pas à pas. Une **commande** (`/discover`, `/write-prd`) enchaîne plusieurs skills ; `/discover` chaîne par exemple brainstorm-ideas, identify-assumptions, prioritize-assumptions, brainstorm-experiments. Conçu pour Claude Code et Cowork ; les skills seuls marchent ailleurs, les commandes sont propres à Claude. Version 2.1.0 du 2026-07-03, MIT, dernier push le 2026-09-14. Le dépôt se décrit comme comptant « plus de 100 » skills, le README en compte 69 : le README fait foi ici.

## Les skills

Seuls les plugins utiles à la conduite d'un projet de développement sont détaillés. Les cinq autres (stratégie produit, étude de marché, analyse de données, mise sur le marché, croissance) et `pm-toolkit` (relecture de CV, NDA, politique de confidentialité, correction de texte) servent un chef de produit, pas un développeur.

| Étape | Skill | Ce qu'il fait |
|---|---|---|
| Cadrer | opportunity-solution-tree | Arbre résultat, opportunités, solutions, expériences (Teresa Torres) |
| Cadrer | identify-assumptions-existing / -new | Repère les hypothèses risquées (valeur, utilisabilité, viabilité, faisabilité ; huit catégories pour un produit neuf) |
| Cadrer | prioritize-assumptions | Matrice impact × risque, avec expériences suggérées |
| Cadrer | interview-script, summarize-interview | Script d'entretien client, puis synthèse d'une transcription |
| Cadrer | brainstorm-ideas / -experiments | Idéation et conception d'expériences, produit existant ou neuf |
| Spécifier | create-prd | Gabarit de PRD en huit sections |
| Spécifier | user-stories | Histoires d'utilisateur selon les 3 C et les critères INVEST |
| Spécifier | job-stories | « Quand [situation], je veux [motivation], pour [résultat] » |
| Spécifier | wwas | Éléments de backlog au format Pourquoi, Quoi, Acceptation |
| Planifier | prioritize-features | Priorise un backlog selon impact, effort, risque et alignement |
| Planifier | prioritization-frameworks | Guide de neuf cadres : Opportunity Score, ICE, RICE, MoSCoW, Kano… |
| Planifier | outcome-roadmap | Transforme une liste de fonctionnalités en feuille de route par résultats |
| Planifier | sprint-plan | Planification de sprint : capacité, choix des histoires, risques |
| Planifier | brainstorm-okrs | Objectifs et résultats clés d'équipe |
| Planifier | stakeholder-map | Grille pouvoir × intérêt et plan de communication |
| Vérifier | pre-mortem | Analyse de risques avant lancement (tigres, tigres de papier, éléphants) |
| Vérifier | strategy-red-team | Test adverse d'un plan : hypothèses porteuses, ce qui les ferait échouer, par coût de test |
| Vérifier | test-scenarios | Scénarios de test depuis des histoires : chemins nominaux, cas limites, erreurs |
| Vérifier | shipping-artifacts, intended-vs-implemented | Plugin `pm-ai-shipping` : documente une application écrite par IA, puis cherche l'écart entre l'intention documentée et le code |
| Livrer | release-notes | Notes de version pour utilisateurs, depuis tickets, PRD ou changelog |
| Après | retro | Animation d'une rétrospective de sprint |
| Divers | summarize-meeting, dummy-dataset | Compte rendu de réunion en décisions et actions ; jeux de données factices en CSV, JSON, SQL ou Python |

Commandes de `pm-ai-shipping` : `/ship-check` (paquet de livraison complet), `/document-app`, `/derive-tests`, `/security-audit-static`, `/performance-audit-static`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cadrer **quoi** construire avant de spécifier : discovery, hypothèses, PRD, histoires | Le besoin est déjà clair et le goulot est l'implémentation → [[Superpowers]], [[Skills de Matt Pocock]] |
| Rôle de chef de produit ou de PO en plus du développement, en ESN ou en petite équipe | Projet solo où un PRD d'une page suffit : neuf plugins, c'est trop |
| Reprendre une application écrite à la volée : `pm-ai-shipping` rétro-documente et audite | Audit de sécurité probant : l'audit est **statique**, sans exécution du code |
| Réutiliser les cadres de priorisation et de rétrospective sans les redécouvrir | Utiliser autre chose que Claude Code : les commandes ne s'exécutent pas ailleurs, seuls les skills passent |

## Mise en œuvre

- Installation — Claude Code : `claude plugin marketplace add phuryn/pm-skills`, puis `claude plugin install pm-execution@pm-skills` (un par plugin). Codex : `codex plugin marketplace add phuryn/pm-skills`. Autres agents : copier les dossiers `skills/*` dans le répertoire de skills de l'agent (Gemini CLI, OpenCode, Cursor, Kiro)
- Point d'entrée — `/discover`, `/write-prd`, `/sprint`, `/ship-check`
- Prérequis — un agent hôte ; installer des plugins entiers plutôt qu'un skill isolé, car un workflow en utilise plusieurs
- Exécution — dans l'agent hôte, sur le poste ; rien à héberger
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- Aucune page équivalente dans le brain : aucun autre jeu de skills de gestion de produit n'y est fiché. Les méthodes correspondantes sont écrites dans [[PRD et user stories]] et [[Backlog, Kanban, Scrum et Shape Up]].

### Compléments

- [[Skills d'Addy Osmani]] — Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle. — prend la suite : le PRD de `create-prd` nourrit `spec-driven-development`.

## Ressources

- Documentation — https://github.com/phuryn/pm-skills
- Dépôt — https://github.com/phuryn/pm-skills

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Quel skill pour quelle étape]] — le tableau qui réunit les skills par étape du cycle de vie
- [[Agent skills]] — le mécanisme des skills
- [[PRD et user stories]] — la méthode derrière `create-prd` et `user-stories`
