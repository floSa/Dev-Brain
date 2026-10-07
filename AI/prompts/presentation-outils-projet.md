# Prompt — présentation des outils de gestion et de cycle de vie de projet

> Ce fichier se donne tel quel à une **nouvelle conversation**, lancée **hors du DevBrain**.
> Il contient le cadrage de floSa (ce qu'il veut) puis le catalogue des outils (ce que le brain sait).
> Catalogue généré le 2026-10-07 depuis `main`. Les pages du brain restent la source : en cas d'écart, la page gagne.

## Qui parle et comment répondre

floSa est ingénieur Data / ML / AI, profil on-prem et ESN. Réponds en **français**, phrases **courtes et claires**, sans jargon non expliqué. Pose uniquement les questions qui bloquent ; pour le reste, **tranche et dis que tu as tranché**. Si tu proposes plusieurs options, donne à chacune son **nom** et ce qu'elle fait, jamais une lettre seule. Pas de blabla.

## Ce que floSa veut

Une **présentation** (des slides) qui présente les outils d'aide à la gestion de projet et au cycle de vie d'un projet de développement assisté par agent : spécifier, cadrer l'agent, suivre le travail, vérifier et livrer, documenter, dessiner, mesurer. Elle est faite **en plusieurs fois** : une partie = un PDF, et floSa **fusionne les PDF** à la fin. Chaque partie doit donc être autonome mais garder le **même gabarit visuel** que les autres.

Ce travail se fait **hors du DevBrain**. Tu **lis** le DevBrain (dépôt `~/Projets/DevBrain`, branche `main`), tu n'y écris **rien** sans l'accord explicite de floSa. Ton travail va dans un dossier de projet à part.

## Contenu de chaque slide

- **Une à trois solutions par slide.** Pas plus. Pour chacune : le nom, **ce qu'elle permet** en mots simples, et **en quoi elle est utile**.
- **Le lien du produit sur chaque slide** : le dépôt (`url_repo`) et le site (`url_docs`). Ils sont dans le frontmatter de chaque page du catalogue ci-dessous ; les 56 pages les portent tous. Vérifie qu'ils répondent avant de les imprimer.
- **Un schéma Mermaid intégré** à la slide quand il aide à comprendre (le flux, les étapes, ce qui entre et ce qui sort). Plusieurs pages du brain en contiennent déjà : réutilise-les (surtout `BMAD - la méthode`, `BMAD - tour complet des skills`, `Cycle de vie d'un projet assisté par agent`, `Modèle C4`).
- **Le logo** de l'outil si tu peux l'obtenir proprement (depuis son dépôt ou son site). Sinon, pas de logo : ne cherche pas à le dessiner.
- **Un pied de slide** : licence, date de vérification.

Les pages du brain décrivent déjà ce que permet chaque outil. **Appuie-toi dessus**, mais ne les recopie pas aveuglément : relis-les, **vérifie à la source** (README, site officiel), et **améliore ou corrige** quand une page est fausse, périmée ou trop vague. Note chaque correction : floSa pourra en faire profiter le brain. N'invente rien. Ce que tu n'as pas pu vérifier, dis-le.

## La question du découpage, à trancher avec floSa

floSa ne sait pas encore comment ranger. Les deux options sont :

- **Domaines séparés, avec outils et skills ensemble dans chaque domaine.** Une slide « Spécifier » montre OpenSpec, Agent OS et le skill de spécification qui va avec.
- **Une partie « skills » dédiée.** Tous les skills regroupés à part.

**Ma recommandation** : des domaines séparés par étape du cycle de vie, avec les outils **et** les skills associés ; plus **une courte partie finale ou d'ouverture « Quel skill pour quelle étape »** qui les remet en tableau, à partir de la page `Quel skill pour quelle étape`. Ainsi on retrouve un skill par étape, et aussi d'un seul coup d'œil.

Le catalogue ci-dessous est **déjà rangé en 9 parties** selon cette recommandation. Propose ton propre plan si tu le trouves meilleur, mais **présente-le à floSa avant de produire quoi que ce soit**.

## Méthode, dans cet ordre

1. Lis ce fichier, puis les pages du catalogue (chemins relatifs à `~/Projets/DevBrain`).
2. Propose à floSa, **en une seule fois, sans rien produire** : le plan des parties ; le **gabarit d'une slide** (maquette d'une slide type) ; l'**outil de présentation** ; la liste des outils que tu mettrais en doublon ou que tu écarterais, avec la raison.
3. Attends son accord. Puis produis **une partie à la fois**, un PDF par partie, et dis-lui comment fusionner les PDF.
4. À chaque partie livrée : liste des liens vérifiés, des corrections trouvées, des points non vérifiés.

**Outil de présentation : propose, floSa tranche.** Il doit être **libre**, produire du **PDF**, et **dessiner Mermaid dans les slides**. Pistes : Slidev (Mermaid intégré, export PDF) ou Marp (Markdown vers PDF, Mermaid par ajout). Dis ce que tu recommandes et pourquoi.

## Suggestions de cadrage (à accepter ou refuser)

- **Une charte commune écrite d'abord** (polices, couleurs, marges, taille des titres, pied de slide), dans un seul fichier de thème partagé par toutes les parties. C'est ce qui rend la fusion des PDF propre.
- **Un fil rouge** : en tête de chaque partie, le même schéma Mermaid du cycle de vie avec l'étape courante en surbrillance. Quand les PDF sont fusionnés, le lecteur sait toujours où il en est.
- **Un gabarit de slide fixe** : « c'est quoi », « ce que ça permet », « quand le choisir », « quand l'éviter », et le lien. Une slide « comparaison » par partie quand il y a plusieurs outils concurrents (les comparatifs du brain servent de base).
- **Une slide de sommaire** et **une slide « sources »** par partie.
- **Des notes de l'orateur** par slide, courtes.
- **Un annexe « cités sans page »** : outils que le brain cite en texte simple sans page (Context7, Jira, OpenProject, Plane, awesome-claude-skills). À cadrer avec floSa : on les nomme sans les recommander.
- **Une règle de date** : toute information dépendante du temps (version, activité du dépôt, étoiles) porte sa date.

## Règles du brain à respecter dans la présentation

- On cherche des solutions **non payantes** et **déployables sur site**. On **privilégie** le libre et commercialisable. Une licence « non commerciale » reste acceptée, floSa n'a pas d'usage commercial.
- Pour chaque outil, dis **sa nature en une phrase** (agent, skill, jeu de skills, application à héberger, outil en ligne de commande, format…).
- Ne présente **ni Claude Code, ni Codex, ni Gemini CLI** comme solutions à adopter.
- Les skills de `anthropics/skills` : seuls les skills libres sont recommandés (Apache 2.0). `docx`, `pdf`, `pptx` et `xlsx` sont sous licence fermée.
- Si tu crées un dépôt git pour la présentation : identité = la config locale du dépôt, **aucun co-auteur**, petits commits, push régulier.

## Fin de tâche

Termine chaque livraison par une ligne vide, `SYNTHÈSE DE TÂCHES`, ta synthèse, puis `FIN DE TÂCHES`.

## Catalogue des outils

Chemins relatifs à `~/Projets/DevBrain`. Colonne « Licence » : valeur vérifiée à la source par le brain ; « mixte, voir la page » = le dépôt n'a pas de licence unique.

### Partie 1. Le cadre : cycle de vie d'un projet avec un agent


Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Gestion de projet — `Outils de développement/Gestion de projet/Gestion de projet.md` (hub)
- Cycle de vie d'un projet assisté par agent — `Outils de développement/Gestion de projet/Cycle de vie d'un projet assisté par agent.md` (notion)
- Vibe coding contre ingénierie agentique — `Outils de développement/Gestion de projet/Vibe coding contre ingénierie agentique.md` (notion)
- Boucle de Ralph — `Outils de développement/Gestion de projet/Boucle de Ralph.md` (notion)
- Fichiers de contexte pour agents — `Outils de développement/Gestion de projet/Fichiers de contexte pour agents.md` (notion)

### Partie 2. Cadrer et spécifier avant de coder

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| OpenSpec | Outil libre (MIT, TypeScript, paquet npm `@fission-ai/openspec`) de spécification dans le dépôt : un dossier `openspec/` garde les specs de ce qui est vrai et un dossier … | open-source | https://github.com/Fission-AI/OpenSpec | https://github.com/Fission-AI/OpenSpec/blob/main/docs/README.md | `LLM & IA générative/Agents de code/OpenSpec.md` |
| Agent OS | Jeu de commandes et de scripts shell (MIT) qui extrait les règles de code d'un projet — nommage, structure, tests, formats — dans des fichiers Markdown, puis les injecte … | open-source | https://github.com/buildermethods/agent-os | https://buildermethods.com/agent-os | `Outils de développement/Gestion de projet/Agent OS.md` |
| BMAD | Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM … | open-source | https://github.com/bmad-code-org/BMAD-METHOD | https://docs.bmad-method.org/ | `LLM & IA générative/Agents de code/BMAD.md` |
| pm-skills | Skills MIT de gestion de produit pour Claude Code et d'autres agents (69 skills, 42 commandes, 9 plugins) : découverte, PRD, histoires, sprints, lancement. | open-source | https://github.com/phuryn/pm-skills | https://github.com/phuryn/pm-skills | `LLM & IA générative/Agents de code/pm-skills.md` |
| MADR - le modèle de fiche | Modèle de fiche en Markdown (MIT ou CC0-1.0, quatre variantes) pour consigner une décision d'architecture : contexte, options envisagées, décision et conséquences, un … | open-source | https://github.com/adr/madr | https://adr.github.io/madr/ | `Outils de développement/Gestion de projet/MADR - le modèle de fiche.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Développement piloté par la spécification — `Outils de développement/Gestion de projet/Développement piloté par la spécification.md` (notion)
- PRD et user stories — `Outils de développement/Gestion de projet/PRD et user stories.md` (notion)
- ADR et design docs — `Outils de développement/Gestion de projet/ADR et design docs.md` (notion)
- BMAD - la méthode — `LLM & IA générative/Agents de code/BMAD - la méthode.md` (notion)
- BMAD - tour complet des skills — `LLM & IA générative/Agents de code/BMAD - tour complet des skills.md` (notion)

### Partie 3. Les skills qui cadrent l'agent

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| Superpowers | Jeu de 15 skills MIT pour agents de code (Claude Code, Codex, Cursor, Gemini CLI…) qui impose un cycle complet : brainstorming, plan, sous-agents, TDD, revue et … | open-source | https://github.com/obra/superpowers | https://github.com/obra/superpowers | `LLM & IA générative/Agents de code/Superpowers.md` |
| Ponytail | Skill MIT qui force l'agent de code à chercher la solution la plus simple avant d'écrire du code, avec cinq commandes de revue, d'audit et de mesure de la sur-ingénierie. | open-source | https://github.com/DietrichGebert/ponytail | https://github.com/DietrichGebert/ponytail | `LLM & IA générative/Agents de code/Ponytail.md` |
| Skills d'Addy Osmani | Jeu de 25 skills MIT pour agents de code qui couvre tout le cycle (définir, planifier, construire, vérifier, relire, livrer) avec 9 commandes et des listes de contrôle. | open-source | https://github.com/addyosmani/agent-skills | https://github.com/addyosmani/agent-skills | `LLM & IA générative/Agents de code/Skills d'Addy Osmani.md` |
| Skills de Matt Pocock | Skills MIT petits et composables pour de l'ingénierie réelle, pas du vibe coding : interrogatoire d'abord, spécification, tickets, TDD, revue. | open-source | https://github.com/mattpocock/skills | https://github.com/mattpocock/skills | `LLM & IA générative/Agents de code/Skills de Matt Pocock.md` |
| i-have-adhd | Skill/plugin MIT pour agents de code (Claude Code, Cursor, Codex, Gemini, Qwen, Kimi) imposant dix règles de sortie : action en premier, étapes numérotées, état rappelé … | open-source | https://github.com/ayghri/i-have-adhd | https://github.com/ayghri/i-have-adhd | `LLM & IA générative/Agents de code/i-have-adhd.md` |
| Skills d'Anthropic | Dépôt GitHub d'Anthropic de 19 skills d'exemple, sans licence à la racine : 14 sous Apache-2.0, 4 de documents source-available, 1 sans licence — un annuaire à lire … | mixte, voir la page | https://github.com/anthropics/skills | https://github.com/anthropics/skills | `Outils de développement/Skills d'Anthropic.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Quel skill pour quelle étape — `Outils de développement/Gestion de projet/Quel skill pour quelle étape.md` (notion)
- Agent skills — `LLM & IA générative/Agents/Agent skills.md` (notion)

### Partie 4. Découper et suivre le travail

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| Backlog.md - l'outil | Outil en ligne de commande (MIT, TypeScript) qui range les tâches d'un projet en fichiers Markdown dans le dépôt, avec critères d'acceptation, jalons et dépendances, un … | open-source | https://github.com/MrLesk/Backlog.md | https://backlog.md | `Outils de développement/Gestion de projet/Backlog.md - l'outil.md` |
| Beads | Outil en ligne de commande (MIT, Go) qui tient les tâches d'un projet comme un graphe de dépendances dans une base Dolt, pour que des agents trouvent le travail prêt, le … | open-source | https://github.com/gastownhall/beads | https://beads.gascity.com | `Outils de développement/Gestion de projet/Beads.md` |
| Kanboard | Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API … | open-source | https://github.com/kanboard/kanboard | https://docs.kanboard.org/ | `Outils de développement/Gestion de projet/Kanboard.md` |
| Redmine | Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki … | open-source | https://github.com/redmine/redmine | https://www.redmine.org/projects/redmine/wiki/Guide | `Outils de développement/Gestion de projet/Redmine.md` |
| Vikunja | Application web de gestion de tâches à héberger (AGPL-3.0 ou ultérieure, Go et Vue.js), livrée en un seul binaire ou conteneur : projets et sous-projets, tâches avec … | open-source | https://github.com/go-vikunja/vikunja | https://vikunja.io/docs/ | `Outils de développement/Gestion de projet/Vikunja.md` |
| Wekan | Application web de tableaux Kanban à héberger (MIT, JavaScript et Meteor), sur le modèle de Trello : couloirs, listes, cartes, vues tableau, calendrier et Gantt, modules … | open-source | https://github.com/wekan/wekan | https://wekan.fi | `Outils de développement/Gestion de projet/Wekan.md` |
| Vibe Kanban | Application locale (Apache-2.0, Rust) : un tableau Kanban où chaque carte lance un agent de code dans un espace de travail isolé — branche, terminal, serveur de … | open-source | https://github.com/BloopAI/vibe-kanban | https://www.vibekanban.com/docs | `Outils de développement/Gestion de projet/Vibe Kanban.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Backlog, Kanban, Scrum et Shape Up — `Outils de développement/Gestion de projet/Backlog, Kanban, Scrum et Shape Up.md` (notion)
- Comparatif - Suivi de projet auto-hébergé — `Outils de développement/Gestion de projet/Comparatif - Suivi de projet auto-hébergé.md` (comparatif)

### Partie 5. Piloter plusieurs agents et leur donner du contexte

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| Claude Squad | Application de terminal (AGPL-3.0, Go) qui gère plusieurs agents de code en parallèle, chacun dans une session tmux et un worktree git à lui, avec aperçu, diff … | open-source | https://github.com/smtg-ai/claude-squad | https://smtg-ai.github.io/claude-squad/ | `Outils de développement/Gestion de projet/Claude Squad.md` |
| Serena | Serveur MCP (GPL-3.0-or-later, Python) qui donne à un agent de code des outils au niveau du symbole — chercher, renommer, remplacer le corps d'une fonction — appuyés par … | open-source | https://github.com/oraios/serena | https://oraios.github.io/serena | `Outils de développement/Gestion de projet/Serena.md` |
| Repomix | Outil en ligne de commande (MIT, TypeScript) qui empaquette un dépôt en un seul fichier XML, Markdown, JSON ou texte pour le donner à une IA : jetons comptés, fichiers … | open-source | https://github.com/yamadashy/repomix | https://repomix.com | `Outils de développement/Gestion de projet/Repomix.md` |
| Gitingest | Outil en ligne de commande et bibliothèque Python (MIT) qui transforme un dépôt Git ou un dossier en un texte unique pour un modèle de langage, avec arborescence et … | open-source | https://github.com/coderamp-labs/gitingest | https://gitingest.com | `Outils de développement/Gestion de projet/Gitingest.md` |
| DeepWiki-Open | Application web à héberger (MIT, Python et Next.js) qui génère un wiki interactif d'un dépôt GitHub, GitLab ou Bitbucket — structure du code, documentation, diagrammes … | open-source | https://github.com/AsyncFuncAI/deepwiki-open | https://github.com/AsyncFuncAI/deepwiki-open | `Outils de développement/Gestion de projet/DeepWiki-Open.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Branches courtes et worktrees pour agents — `Outils de développement/Gestion de projet/Branches courtes et worktrees pour agents.md` (notion)

### Partie 6. Vérifier et livrer

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| PR-Agent | Outil de revue automatique de pull requests (MIT, Python), auto-hébergeable : commandes /describe, /review, /improve et /ask, en GitHub Action, en ligne de commande, en … | open-source | https://github.com/The-PR-Agent/pr-agent | https://docs.pr-agent.ai/ | `Outils de développement/Gestion de projet/PR-Agent.md` |
| pre-commit | Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque … | open-source | https://github.com/pre-commit/pre-commit | https://pre-commit.com/ | `Outils de développement/Qualité du code/pre-commit.md` |
| Lefthook | Gestionnaire de crochets git (MIT, Go) distribué en binaire unique qui lit un fichier `lefthook.yml`, lance les commandes en parallèle et choisit les fichiers à leur … | open-source | https://github.com/evilmartians/lefthook | https://lefthook.dev/ | `Outils de développement/Qualité du code/Lefthook.md` |
| Commitizen | Outil en ligne de commande Python (MIT) qui guide l'écriture de commits conventionnels, puis calcule la prochaine version SemVer et met à jour le changelog par `cz bump` … | open-source | https://github.com/commitizen-tools/commitizen | https://commitizen-tools.github.io/commitizen/ | `Outils de développement/Gestion de projet/Commitizen.md` |
| git-cliff | Outil en ligne de commande (Apache-2.0, Rust) qui génère un changelog depuis l'historique Git, par commits conventionnels ou analyseurs à expressions régulières, et … | open-source | https://github.com/orhun/git-cliff | https://git-cliff.org/docs | `Outils de développement/Gestion de projet/git-cliff.md` |
| release-please | Outil Node.js (Apache-2.0, Google) qui tient à jour une pull request de release depuis les commits conventionnels : à sa fusion, il met à jour le changelog et les … | open-source | https://github.com/googleapis/release-please | https://github.com/googleapis/release-please | `Outils de développement/Gestion de projet/release-please.md` |
| python-semantic-release | Outil en ligne de commande Python (MIT) qui lit les commits d'un dépôt, calcule la prochaine version SemVer, met à jour les fichiers de version, génère le changelog … | open-source | https://github.com/python-semantic-release/python-semantic-release | https://python-semantic-release.readthedocs.io/en/stable/ | `Outils de développement/Gestion de projet/python-semantic-release.md` |
| just | Lanceur de commandes de projet (CC0-1.0, Rust) : des recettes écrites dans un fichier `justfile`, de syntaxe inspirée de make, avec paramètres, dépendances entre … | open-source | https://github.com/casey/just | https://just.systems/man/en/ | `Outils de développement/Gestion de projet/just.md` |
| Task | Lanceur de commandes de projet (MIT, Go) qui lit un fichier `Taskfile.yml` : tâches, dépendances entre tâches, variables, vérification des fichiers sources pour ne … | open-source | https://github.com/go-task/task | https://taskfile.dev | `Outils de développement/Gestion de projet/Task.md` |
| mise | Outil en ligne de commande (MIT, Rust) qui installe les outils de développement d'un projet (Node.js, Python, Go et des centaines d'autres), fixe ses variables … | open-source | https://github.com/jdx/mise | https://mise.jdx.dev | `Outils de développement/mise.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Revue, tests et définition de terminé avec un agent — `Outils de développement/Gestion de projet/Revue, tests et définition de terminé avec un agent.md` (notion)
- Commits conventionnels, versions et changelog — `Outils de développement/Gestion de projet/Commits conventionnels, versions et changelog.md` (notion)
- Comparatif - Versions et changelog — `Outils de développement/Gestion de projet/Comparatif - Versions et changelog.md` (comparatif)

### Partie 7. Documenter et dessiner l'architecture

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| MkDocs | Outil en ligne de commande (BSD-2-Clause, Python) : génère un site statique de documentation depuis des fichiers Markdown et un seul mkdocs.yml — mais sans version … | open-source | https://github.com/mkdocs/mkdocs | https://www.mkdocs.org/ | `Outils de développement/Documentation technique/MkDocs.md` |
| mkdocstrings | Plugin MkDocs (ISC, Python) : génère la documentation d'API depuis les docstrings et le code source par une simple balise ::: dans le Markdown, avec renvois entre pages … | open-source | https://github.com/mkdocstrings/mkdocstrings | https://mkdocstrings.github.io/ | `Outils de développement/Documentation technique/mkdocstrings.md` |
| Zensical | Outil en ligne de commande (MIT, Rust et Python) : générateur de sites statiques de documentation par l'équipe de Material for MkDocs, qui lit les mkdocs.yml existants — … | open-source | https://github.com/zensical/zensical | https://zensical.org/docs/ | `Outils de développement/Documentation technique/Zensical.md` |
| Docusaurus | Outil en ligne de commande (MIT, TypeScript) : génère un site de documentation sous forme d'application React monopage, avec blog, versions de documentation, traductions … | open-source | https://github.com/facebook/docusaurus | https://docusaurus.io/ | `Outils de développement/Documentation technique/Docusaurus.md` |
| Sphinx | Outil en ligne de commande (BSD-2-Clause, Python) : générateur de documentation écrit en reStructuredText, qui sort HTML, PDF, EPUB et pages de manuel avec renvois … | open-source | https://github.com/sphinx-doc/sphinx | https://www.sphinx-doc.org/ | `Outils de développement/Documentation technique/Sphinx.md` |
| Mermaid | Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian. | open-source | https://github.com/mermaid-js/mermaid | https://mermaid.js.org/ | `Design & diagrammes/Diagrammes/Mermaid.md` |
| LikeC4 | Outil en ligne de commande (MIT, TypeScript) : décrire une architecture logicielle dans un langage de modélisation inspiré du modèle C4, puis en tirer des vues … | open-source | https://github.com/likec4/likec4 | https://likec4.dev/ | `Design & diagrammes/Diagrammes/LikeC4.md` |
| D2 | Outil en ligne de commande (MPL-2.0, Go) qui transforme un langage de description de diagrammes en SVG, PNG, PDF, GIF ou PPTX, avec thèmes, plusieurs moteurs de … | open-source | https://github.com/d2lang/d2 | https://d2lang.com | `Design & diagrammes/Diagrammes/D2.md` |
| PlantUML | Outil Java (licences au choix : GPL, LGPL, Apache, EPL ou MIT) qui dessine des diagrammes UML et plus de vingt types — séquence, classes, activité, états, Gantt, carte … | open-source | https://github.com/plantuml/plantuml | https://plantuml.com | `Design & diagrammes/Diagrammes/PlantUML.md` |
| Kroki | Serveur HTTP (MIT, Java) à héberger qui donne une seule API pour rendre une vingtaine de langages de diagrammes — PlantUML, Mermaid, D2, GraphViz, BPMN, Excalidraw … | open-source | https://github.com/yuzutech/kroki | https://docs.kroki.io/ | `Design & diagrammes/Diagrammes/Kroki.md` |
| draw.io | Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export … | open-source | https://github.com/jgraph/drawio | https://www.drawio.com/docs/ | `Design & diagrammes/Diagrammes/draw.io.md` |
| Excalidraw | Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian. | open-source | https://github.com/excalidraw/excalidraw | https://docs.excalidraw.com/ | `Design & diagrammes/Diagrammes/Excalidraw.md` |
| Archify | Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec … | open-source | https://github.com/tt-a1i/archify | https://tt-a1i.github.io/archify/ | `Design & diagrammes/Diagrammes/Archify.md` |
| FossFLOW | Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes … | open-source | https://github.com/stan-smith/FossFLOW | https://github.com/stan-smith/FossFLOW | `Design & diagrammes/Diagrammes/FossFLOW.md` |
| GitDiagram | Service web open-source (MIT, TypeScript) qui génère par LLM un diagramme d'architecture interactif d'un dépôt GitHub depuis son URL : composants liés au code, export … | open-source | https://github.com/ahmedkhaleel2004/gitdiagram | https://github.com/ahmedkhaleel2004/gitdiagram/tree/main/docs | `Design & diagrammes/Diagrammes/GitDiagram.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Diátaxis et docs-as-code — `Outils de développement/Documentation technique/Diátaxis et docs-as-code.md` (notion)
- Modèle C4 — `Outils de développement/Gestion de projet/Modèle C4.md` (notion)
- Documentation technique — `Outils de développement/Documentation technique/Documentation technique.md` (hub)
- Comparatif - Générateurs de documentation — `Outils de développement/Documentation technique/Comparatif - Générateurs de documentation.md` (comparatif)
- Diagrammes — `Design & diagrammes/Diagrammes/Diagrammes.md` (hub)
- Comparatif - Diagrammes — `Design & diagrammes/Diagrammes/Comparatif - Diagrammes.md` (comparatif)

### Partie 8. Mesurer

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| ccusage | Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour … | open-source | https://github.com/ccusage/ccusage | https://ccusage.com/ | `Outils de développement/Gestion de projet/ccusage.md` |
| Claude-Code-Usage-Monitor | Outil en ligne de commande Python (MIT) qui lit les journaux locaux de Claude Code et affiche dans le terminal, en direct, la consommation de jetons, de messages et de … | open-source | https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor | https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor | `Outils de développement/Gestion de projet/Claude-Code-Usage-Monitor.md` |
| ActivityWatch | Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le … | open-source | https://github.com/ActivityWatch/activitywatch | https://docs.activitywatch.net/ | `Outils de développement/Gestion de projet/ActivityWatch.md` |
| Kimai | Application web de suivi du temps à héberger (AGPL-3.0, PHP, Symfony) : feuilles de temps, clients et projets, tarifs, budgets, factures et API JSON, multi-utilisateur … | open-source | https://github.com/kimai/kimai | https://www.kimai.org/documentation/ | `Outils de développement/Gestion de projet/Kimai.md` |
| Apache DevLake | Plateforme à héberger (Apache-2.0, Go) qui collecte les données dispersées des outils de développement — GitHub, GitLab, Jenkins, Jira, SonarQube — et les rend en … | open-source | https://github.com/apache/devlake | https://devlake.apache.org | `Outils de développement/Gestion de projet/Apache DevLake.md` |

Pages de fond à relire pour cette partie (notions, comparatifs, hubs) :

- Mesurer un projet - DORA, coût des agents et temps passé — `Outils de développement/Gestion de projet/Mesurer un projet - DORA, coût des agents et temps passé.md` (notion)

### Partie 9. Standards et annuaires

| Outil | Ce que c'est (extrait de la page) | Licence | Dépôt | Site | Page du brain |
|---|---|---|---|---|---|
| AGENTS.md - le format | Format ouvert (MIT) d'un fichier Markdown AGENTS.md à la racine d'un dépôt, qui donne aux agents de code les commandes et les conventions du projet : aucun champ … | open-source | https://github.com/agentsmd/agents.md | https://agents.md | `Outils de développement/AGENTS.md - le format.md` |
| Agent Skills - la spécification | Spécification ouverte du format SKILL.md (dépôt Apache-2.0, documentation CC-BY-4.0, née chez Anthropic) : un dossier avec un frontmatter name et description, chargé en … | open-source | https://github.com/agentskills/agentskills | https://agentskills.io | `Outils de développement/Agent Skills - la spécification.md` |
| awesome-claude-code | Annuaire GitHub d'environ deux cents ressources pour Claude Code, rangées par thème — skills, agents, serveurs, lignes d'état, suivi de coûts, orchestration … | source-available | https://github.com/hesreallyhim/awesome-claude-code | https://github.com/hesreallyhim/awesome-claude-code | `Outils de développement/awesome-claude-code.md` |
