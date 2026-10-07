---
role: brique
nom: Agent OS
alias: [agent-os, buildermethods/agent-os, Builder Methods Agent OS]
pitch: "Jeu de commandes et de scripts shell (MIT) qui extrait les règles de code d'un projet — nommage, structure, tests, formats — dans des fichiers Markdown, puis les injecte dans le contexte de l'agent à chaque tâche pour qu'il code comme son auteur — mais il faut un agent hôte (Claude Code, Cursor…), et depuis la v3 la rédaction des spécifications est laissée au mode plan de l'agent."
categorie: devtools/projet
famille: extension
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Shell
alternatives: []
complements: []
tags: [spec-driven, context-engineering, agents]
url_docs: https://buildermethods.com/agent-os
url_repo: https://github.com/buildermethods/agent-os
---

# Agent OS

<!-- AUTO:BANDEAU:START -->
> Jeu de commandes et de scripts shell (MIT) qui extrait les règles de code d'un projet — nommage, structure, tests, formats — dans des fichiers Markdown, puis les injecte dans le contexte de l'agent à chaque tâche pour qu'il code comme son auteur — mais il faut un agent hôte (Claude Code, Cursor…), et depuis la v3 la rédaction des spécifications est laissée au mode plan de l'agent.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Shell | open-source | dans le moteur hôte, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Jeu de **commandes d'agent** et de scripts shell, créé par Brian Casel (Builder Methods), qui s'installe dans un projet. Il règle un problème précis : l'agent code correctement mais pas **à votre façon**. Les règles du projet (comment on nomme, où on range, quelle forme ont les réponses d'API, comment on teste) sont écrites une fois dans des fichiers Markdown, les **standards**, rangés dans un dossier `agent-os/standards/` par sujet. Un fichier `index.yml` les décrit pour qu'un agent sache lesquels lire.

Quatre commandes dans la v3 : `/discover-standards` fait lire le code existant à l'agent et lui fait proposer des standards à documenter ; `/inject-standards` donne à l'agent les standards utiles à la tâche, dans la conversation, dans un plan ou dans un skill en cours d'écriture ; `/shape-spec` ajoute au mode plan de l'agent des questions ciblées qui tiennent compte des standards et de la mission du produit ; `/index-standards` tient l'index à jour. Version 3.0 du 2026-01-20, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07. La v3 a **retiré** l'orchestration de l'implémentation et la rédaction de spécifications : le CHANGELOG dit que le mode plan et les modèles actuels le font mieux, et que le contenu des versions précédentes (standards, specs, documents produit) se reporte tel quel.

**Exemple concret.** Un projet FastAPI de floSa où chaque réponse d'erreur suit la même forme. Sans Agent OS, il faut le redire à chaque session. Avec : `agent-os/standards/api/response-format.md` écrit une fois (« une erreur renvoie `{"error": {"code": ..., "message": ...}}`, jamais une chaîne ; les codes viennent de `errors.py` »), `agent-os/standards/testing.md` (« pytest, un fichier de test par module, fixtures dans `conftest.py` »). Pour ajouter un point d'accès, `/inject-standards api` lit les fichiers du dossier `api/` dans la conversation ; l'agent produit alors la route, l'erreur et le test dans la forme attendue. Seul `api/response-format` est un nom pris dans la documentation de la commande ; le reste de l'exemple est inventé pour l'illustration.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les règles du projet existent dans la tête de l'équipe et l'agent les ignore : les écrire une fois, les rejouer à chaque tâche | Un fichier d'instructions suffit : pour peu de règles, [[Fichiers de contexte pour agents]] (`AGENTS.md`) est plus simple |
| Reprendre un code existant : `/discover-standards` en extrait les conventions réellement suivies | Un cadre de spécification par changement, avec archivage : [[OpenSpec]] ou [[Spec Kit]] |
| Fabriquer un skill ou un sous-agent qui embarque les règles du projet (`/inject-standards` en mode skill) | Un agent sans commandes personnalisées : les commandes sont des fichiers Markdown pour les agents qui les comprennent |
| Plusieurs projets qui partagent des règles : les profils (`config.yml`, héritage entre profils) et le script de synchronisation | Un outil qui impose des règles de style : Agent OS décrit, il ne vérifie pas ; pour contraindre, [[Ruff]] ou [[pre-commit]] |

## Mise en œuvre

- Installation — cloner le dépôt une fois, puis lancer `scripts/project-install.sh` depuis le dossier du projet ; les instructions détaillées sont sur le site
- Point d'entrée — les commandes `/discover-standards`, `/inject-standards`, `/shape-spec`, `/index-standards` dans l'agent
- Prérequis — un agent qui lit des commandes en Markdown (Claude Code, Cursor, Antigravity d'après le README) ; bash
- Exécution — sur le poste ; rien à héberger
- Coût — gratuit sous licence MIT ; le site propose une communauté payante, qui n'est pas nécessaire

## Écosystème

### Alternatives

- voisin : [[OpenSpec]] — cadre de spécification par changement ; Agent OS fixe les règles qui valent pour tous les changements.
- voisin : [[Spec Kit]] — le jeu de commandes de GitHub pour le développement piloté par la spécification.
- voisin : [[Fichiers de contexte pour agents]] — la notion : le plus simple des moyens de donner des règles à l'agent.

## Ressources

- Documentation — https://buildermethods.com/agent-os
- Dépôt — https://github.com/buildermethods/agent-os

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Développement piloté par la spécification]] — la famille d'approches
- [[Context engineering]] — composer et borner le contexte donné au modèle
- [[Outils de développement]] — le hub du domaine
