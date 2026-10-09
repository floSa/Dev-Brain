---
role: hub
nom: Rules
pitch: Les contraintes qui tiennent quelle que soit la stack — outillage, structure, qualité, tests, git, conteneurs, documentation, secrets, travail avec un agent.
---

# Rules

> Les contraintes qui tiennent quelle que soit la stack — outillage, structure, qualité, tests, git, conteneurs, documentation, secrets, travail avec un agent.

## Ce qu'il faut comprendre

- Une règle dit ce qu'un projet **doit** faire, indépendamment des briques qu'il retient. C'est la seule famille de pages du vault qui contraint au lieu de décrire.
- Chacune porte son niveau d'exigence dans `strictness:` — `must`, `should`, `nice-to-have`. Une règle `must` n'est pas une préférence : la contredire se justifie, dans le projet, par écrit.
- Comme les patterns, aucune `categorie:` ne les range : elles sont transverses par définition, et c'est `role: rule` qui les groupe.

## Choisir

- Démarrer un projet Python → [[Rule - Toolchain Python]] et [[Rule - Structure de projet]] d'abord, ce sont elles qui figent l'arborescence et les commandes.
- Poser la barre de qualité et la CI → [[Rule - Qualité stricte]].
- Manipuler de la configuration ou des secrets → [[Rule - Config typée]].
- Livrer une démo à quelqu'un d'autre → [[Rule - Packaging démo]].
- Écrire les tests d'un projet Python → [[Rule - Tests Python avec pytest]].
- Poser la convention de commit et automatiser les versions → [[Rule - Commits conventionnels et versions automatiques]] ; fixer l'identité et interdire le co-auteur par un hook → [[Rule - Git et identité]].
- Livrer une image de conteneur → [[Rule - Image Docker minimale]].
- Documenter un projet et consigner ses décisions → [[Rule - README, docs et décisions]].
- Travailler avec un agent de code → [[Rule - Projet assisté par agent]].
- Garder les secrets hors du dépôt → [[Rule - Secrets hors du dépôt]] (la configuration typée, elle, est dans [[Rule - Config typée]]).
- Entraîner un détecteur d'anomalies → [[Rule - Entraîner sur du normal vérifié]] ; en mesurer le résultat → [[Rule - Évaluer une anomalie par événement, pas par point]].

<!-- AUTO:START -->
### Rules
- [[Rule - Commits conventionnels et versions automatiques]]
- [[Rule - Config typée]]
- [[Rule - Entraîner sur du normal vérifié]]
- [[Rule - Git et identité]]
- [[Rule - Image Docker minimale]]
- [[Rule - Packaging démo]]
- [[Rule - Projet assisté par agent]]
- [[Rule - Qualité stricte]]
- [[Rule - README, docs et décisions]]
- [[Rule - Secrets hors du dépôt]]
- [[Rule - Structure de projet]]
- [[Rule - Tests Python avec pytest]]
- [[Rule - Toolchain Python]]
- [[Rule - Évaluer une anomalie par événement, pas par point]]
<!-- AUTO:END -->
