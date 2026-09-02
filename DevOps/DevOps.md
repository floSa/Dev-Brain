---
role: hub
nom: DevOps
alias: [devops, ci, cd]
pitch: Déployer et faire tourner ce qui a été fabriqué — packager en image, et l'exécuter à chaque commit.
domaines: [mlops, infra-ops]
tags: [container, ci-cd, deployment-strategy]
---

# DevOps

> Déployer et faire tourner ce qui a été fabriqué — packager en image, et l'exécuter à chaque commit.

## Ce qu'il faut comprendre

- La frontière avec [[Outils de développement]] est nette et vaut d'être tenue : **fabriquer** un logiciel (écrire, tester, linter) est là-bas ; le **déployer** est ici. C'est la distinction que porte la taxonomie entre `devtools/*` et `devops/*`.
- Les deux briques du domaine sont les deux faces d'un même geste. [[Docker]] fixe **ce qui tourne** : une image reproductible, dépendances système comprises. [[GitHub Actions]] fixe **quand ça tourne** : à chaque poussée, chaque tag, chaque nuit.
- Pour un projet data, l'image est ce qui rend un modèle transportable — la version de Python, celle de CUDA, les bibliothèques natives que `pip` ne gère pas. C'est aussi ce qui explique le poids des images ML, et pourquoi le multi-stage et le cache de couches y comptent plus qu'ailleurs.
- L'usage de [[Docker]] en **test** mérite d'être connu à part : [[testcontainers]] démarre une vraie base ou un vrai broker le temps d'un test, ce qui supprime une catégorie entière de mocks.
- Le domaine est volontairement pauvre : la spécialité de ce brain est l'**on-prem**, et Kubernetes, Terraform, Ansible n'y ont pas encore de fiche. C'est un manque connu, pas un choix.

## Choisir

- Packager une application ou un modèle avec son environnement → [[Docker]].
- Lancer les tests, construire l'image et publier à chaque commit → [[GitHub Actions]].
- Des dépendances jetables pendant un test → [[testcontainers]], au-dessus de Docker.

<!-- AUTO:START -->
### Briques
- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre.
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.
<!-- AUTO:END -->
