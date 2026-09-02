---
role: hub
nom: Rules
pitch: Les contraintes qui tiennent quelle que soit la stack — outillage, structure, qualité, packaging.
---

# Rules

> Les contraintes qui tiennent quelle que soit la stack — outillage, structure, qualité, packaging.

## Ce qu'il faut comprendre

- Une règle dit ce qu'un projet **doit** faire, indépendamment des briques qu'il retient. C'est la seule famille de pages du vault qui contraint au lieu de décrire.
- Chacune porte son niveau d'exigence dans `strictness:` — `must`, `should`, `nice-to-have`. Une règle `must` n'est pas une préférence : la contredire se justifie, dans le projet, par écrit.
- Comme les patterns, aucune `categorie:` ne les range : elles sont transverses par définition, et c'est `role: rule` qui les groupe.

## Choisir

- Démarrer un projet Python → [[Rule - Toolchain Python]] et [[Rule - Structure de projet]] d'abord, ce sont elles qui figent l'arborescence et les commandes.
- Poser la barre de qualité et la CI → [[Rule - Qualité stricte]].
- Manipuler de la configuration ou des secrets → [[Rule - Config typée]].
- Livrer une démo à quelqu'un d'autre → [[Rule - Packaging démo]].

<!-- AUTO:START -->
### Rules
- [[Rule - Config typée]]
- [[Rule - Packaging démo]]
- [[Rule - Qualité stricte]]
- [[Rule - Structure de projet]]
- [[Rule - Toolchain Python]]
<!-- AUTO:END -->
