---
role: rule
domaine: agents
applicable: agent
strictness: should
tags: [rule, agents, spec-driven, code-review, context-engineering]
---

# Rule — Projet assisté par agent

## Principe

Un projet mené avec un agent de code écrit la spécification avant le code, pose un critère de terminé que l'agent peut exécuter, vérifie avant de rendre la main et isole chaque tâche sur une branche courte.

L'agent produit vite et en volume ; sans critère exécutable, le seul signal de fin est que le travail « a l'air terminé », et l'humain devient la boucle de vérification. Ce qui ne doit jamais être violé se met dans un hook ou dans la CI, pas dans un fichier que l'agent lit comme du contexte.

## MUST

- Écrire la spécification (quoi, pourquoi, critères d'acceptation) avant le code, dans `docs/specification.md`.
- Poser avant la tâche une définition de terminé exécutable : tests, lint et types qui passent.
- Vérifier avant de rendre la main : lancer les contrôles et montrer leur sortie, sans affirmer le succès.
- Ne jamais modifier ni supprimer un test rouge pour le faire passer sans le dire.
- Travailler sur une branche courte par tâche, un worktree par agent en parallèle, et fusionner dès que la CI est verte.
- Ne pas ajouter de dépendance ni toucher à un fichier hors périmètre sans accord.

## SHOULD

- Écrire les tests depuis la spécification, sans montrer l'implémentation à l'agent qui les écrit : des tests produits après le code valident ce que le code fait, pas ce qu'il devait faire. Relire les tests avant le code.
- Relire le diff soi-même avant de fusionner, et découper la tâche quand le diff ne se lit plus en quelques minutes.
- Placer chaque consigne au bon endroit : valable à chaque session, elle va dans `AGENTS.md` ; liée à certains fichiers, dans une règle à portée de chemin ; une procédure à la demande, dans un skill ; imposée sans exception, dans un hook ou la CI.
- Écrire `AGENTS.md` à la main, court, et le construire par les échecs : une ligne par erreur de l'agent, une ligne retirée quand l'agent la respecte sans qu'on la donne. Pas de `/init` lancé en pilote automatique.
- Structurer la spécification, le plan et les tâches par un outil ([[Spec Kit]], [[OpenSpec]]) ou par de simples fichiers Markdown dans `docs/`, selon la taille du projet.
- Sur un projet de site client ou d'ESN, consigner dans `AGENTS.md` ce qui distingue le poste du client du poste standard : registre interne, pas de `pip install` direct, interdictions contractuelles.
- Tenir les secrets hors de `AGENTS.md`, des spécifications et des invites ([[Rule - Secrets hors du dépôt]]).

## NICE-TO-HAVE

- Une session de relecture à contexte vierge, qui ne voit que le diff et les critères.
- Une commande unique de vérification (`make check`) que l'agent connaît par son fichier de contexte.
- Une boucle qui relance l'agent jusqu'à ce qu'un critère passe ([[Boucle de Ralph]]), seulement si ce critère est bon et le nombre de tours plafonné.

## Pour AGENTS.md

- Spécification d'abord : `docs/specification.md` avant le code.
- Vérifier avant de rendre la main : lancer les tests, le lint et les types, et montrer leur sortie.
- Ne jamais modifier ni supprimer un test rouge pour le faire passer sans le dire.
- Une branche courte par tâche. Pas de dépendance ajoutée, pas de fichier hors périmètre sans accord.

## Exemples

### Bon

```markdown
## Terminé quand
- `uv run pytest` passe, dont le test de bout en bout de la spécification
- `uv run ruff check . && uv run mypy src` passent
- aucun fichier hors `src/ingest/` et `tests/` modifié, aucune dépendance ajoutée
- `README.md` et `docs/` à jour, diff relu par un humain
```

```bash
git worktree add ../mon-projet-tache-12 -b tache-12-ingestion
```

### Mauvais

```text
Prompt : « fais l'ingestion des fichiers, ça devrait marcher »
Fin de tâche : « Tout est terminé » (aucune sortie de test, test rouge supprimé, trois dépendances nouvelles)
```

## Exceptions

- Prototype jetable ou exploration : pas de spécification écrite, mais le code ne passe en projet qu'avec spécification et tests.
- Correction d'une ligne : la définition de terminé se réduit au test qui reproduit le bogue.
- Une seule tâche à la fois et un seul agent : le worktree supplémentaire n'apporte rien, la branche courte reste.

## Voir aussi

- [[Cycle de vie d'un projet assisté par agent]] — la carte des étapes et des points de décision humaine
- [[Développement piloté par la spécification]] — la spécification avant le code
- [[Revue, tests et définition de terminé avec un agent]] — le critère de terminé et le piège de l'agent qui teste son propre code
- [[Branches courtes et worktrees pour agents]] — une branche, une tâche, un agent
- [[Fichiers de contexte pour agents]] — ce qui va dans `AGENTS.md` et ce qui va ailleurs
- [[AGENTS.md - le format]] — la fiche du format
- [[Rule - Git et identité]], [[Rule - Tests Python avec pytest]], [[Rule - README, docs et décisions]]
- [[Spec Kit]], [[OpenSpec]] — outils de spécification
