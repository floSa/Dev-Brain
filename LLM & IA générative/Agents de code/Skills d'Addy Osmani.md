---
role: brique
nom: Skills d'Addy Osmani
alias: [agent-skills, addyosmani/agent-skills, Addy Osmani agent skills]
pitch: "Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
langage: Markdown
alternatives: ["[[Superpowers]]", "[[Skills de Matt Pocock]]"]
complements: ["[[Ponytail]]", "[[pm-skills]]"]
tags: [agent-skill, skills, code-assistant, agents]
url_docs: https://github.com/addyosmani/agent-skills
url_repo: https://github.com/addyosmani/agent-skills
---

# Skills d'Addy Osmani

<!-- AUTO:BANDEAU:START -->
> Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **jeu de skills**, dépôt `addyosmani/agent-skills` : vingt-cinq dossiers `SKILL.md`, dont vingt-quatre skills de cycle de vie et un skill d'orientation (`using-agent-skills`), plus 9 commandes, 4 personas d'agent (relecteur, ingénieur de test, auditeur de sécurité, auditeur de performance web) et des listes de contrôle de référence. Chaque skill suit le même plan : aperçu, conditions de déclenchement, étapes, portes de vérification, et un tableau des « rationalisations » que l'agent se donne pour sauter une étape. Le fil est DEFINE, PLAN, BUILD, VERIFY, REVIEW, SHIP. Les skills se déclenchent aussi seuls selon la tâche. Version 0.6.12 du 2026-10-03, MIT, dernier push le 2026-10-03.

## Les skills

| Étape | Skill | Ce qu'il fait |
|---|---|---|
| Orientation | using-agent-skills | Associe le travail entrant au bon skill, fixe les règles communes |
| Définir | interview-me | Interrogatoire, une question à la fois, jusqu'à environ 95 % de confiance sur ce que veut vraiment l'utilisateur |
| Définir | idea-refine | Pensée divergente puis convergente : d'une idée floue à une proposition concrète |
| Définir | spec-driven-development | Rédige un PRD (objectifs, commandes, structure, style, tests, limites) avant tout code |
| Définir | constraint-driven-development | Écrit `CONSTRAINTS.md` (barre de qualité, seuils par défaut), place chaque contrôle selon son coût, détecte l'agent qui désactive un contrôle ou saute un test |
| Planifier | planning-and-task-breakdown | Découpe la spécification en tâches vérifiables avec critères d'acceptation et ordre de dépendance |
| Construire | incremental-implementation | Tranches verticales minces : implémenter, tester, vérifier, commiter ; drapeaux de fonctionnalité, retour arrière facile |
| Construire | test-driven-development | Red-Green-Refactor, pyramide de tests 80/15/5, tailles de tests |
| Construire | context-engineering | Donner à l'agent la bonne information au bon moment : fichiers de règles, paquets de contexte, MCP |
| Construire | source-driven-development | Appuie chaque choix de framework sur la documentation officielle, cite, signale le non vérifié |
| Construire | doubt-driven-development | Revue adverse en contexte neuf de chaque décision non triviale, au fil de l'eau |
| Construire | frontend-ui-engineering | Composants, système de design, état, adaptatif, accessibilité WCAG 2.1 AA |
| Construire | api-and-interface-design | Contrat d'abord, loi de Hyrum, sémantique d'erreur, validation aux frontières |
| Vérifier | browser-testing-with-devtools | Données d'exécution réelles via le MCP Chrome DevTools : DOM, console, réseau, profil |
| Vérifier | debugging-and-error-recovery | Cinq temps : reproduire, localiser, réduire, corriger, protéger ; règle d'arrêt de la ligne |
| Relire | code-review-and-quality | Revue sur cinq axes, taille de changement d'environ 100 lignes, niveaux de gravité |
| Relire | code-simplification | Réduire la complexité en préservant le comportement exact (clôture de Chesterton, règle des 500) |
| Relire | security-and-hardening | Prévention OWASP Top 10, authentification, secrets, audit des dépendances |
| Relire | performance-optimization | Mesurer d'abord : Core Web Vitals, profilage, analyse de bundle |
| Livrer | git-workflow-and-versioning | Développement sur tronc, commits atomiques, le commit comme point de sauvegarde |
| Livrer | ci-cd-and-automation | Contrôles décalés vers la gauche, pipelines à portes de qualité, retours d'échec |
| Livrer | deprecation-and-migration | Le code est un passif ; dépréciation imposée ou conseillée, migration, retrait du code zombie |
| Livrer | documentation-and-adrs | Décisions d'architecture (ADR), documentation d'API, commentaires : documenter le pourquoi |
| Livrer | observability-and-instrumentation | Journaux structurés, métriques RED, traçage OpenTelemetry, alertes sur symptômes |
| Livrer | shipping-and-launch | Liste de contrôle avant lancement, déploiement par paliers, retour arrière, supervision |

Commandes : `/spec`, `/plan`, `/build` (et `/build auto`, qui génère le plan puis implémente tout en une passe approuvée, chaque tâche testée et commitée à part), `/test`, `/constraints`, `/review`, `/webperf`, `/code-simplify`, `/ship`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un catalogue large, qui va jusqu'à la sécurité, l'observabilité, l'API et la performance | Vouloir un cycle imposé tout fait, sans choisir → [[Superpowers]] |
| Choisir un skill par étape, sans adopter une méthode entière | Préférer quelques skills courts et modifiables à un catalogue de vingt-cinq → [[Skills de Matt Pocock]] |
| Projet web : frontend, performance web et tests navigateur sont couverts | Projet de données ou de ML : rien de spécifique aux jeux de données, aux modèles ni aux pipelines |
| Une commande par étape du cycle (`/spec` à `/ship`) | Installer un seul skill : l'installation par skill ne copie pas le dossier commun `references/`, signalé comme limite connue |

## Mise en œuvre

- Installation — `npx skills add addyosmani/agent-skills` (CLI ouvert, plus de 70 agents) ; un seul skill : `--skill code-review-and-quality`. Claude Code : `/plugin marketplace add addyosmani/agent-skills` puis `/plugin install agent-skills@addy-agent-skills`
- Point d'entrée — les commandes `/spec` à `/ship`, ou le déclenchement automatique d'un skill
- Prérequis — un agent hôte ; Node pour l'installateur `npx`. Le marketplace de Claude Code clone en SSH : passer par l'URL HTTPS sans clé GitHub
- Exécution — dans l'agent hôte, sur le poste ; rien à héberger
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[Superpowers]] — Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et vérification avant d'annoncer « terminé ».
- [[Skills de Matt Pocock]] — Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue.
- voisin : [[Spec Kit]] — la spécification exécutable en commandes, là où `spec-driven-development` n'est qu'un skill.
- voisin : [[BMAD]] — des rôles agiles nommés, plus lourd ; ici, des skills sans rôles.

### Compléments

- [[Ponytail]] — Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie. — retranche le superflu que `incremental-implementation` laisse passer.
- [[pm-skills]] — Skills MIT de gestion de produit pour Claude Code et d'autres agents (69 skills, 42 commandes, 9 plugins) : découverte, PRD, histoires, sprints, lancement. — amont du `spec-driven-development` : décider quoi construire.

## Ressources

- Documentation — https://github.com/addyosmani/agent-skills
- Dépôt — https://github.com/addyosmani/agent-skills

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Quel skill pour quelle étape]] — le tableau qui réunit les skills par étape du cycle de vie
- [[Agent skills]] — le mécanisme des skills
- [[Context engineering]] — le skill `context-engineering` en est la version pratique
- [[ADR et design docs]] — le skill `documentation-and-adrs` y répond
