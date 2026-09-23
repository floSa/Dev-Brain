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
- Le domaine se lit en deux gestes. **Ce qui tourne, et où** : une image reproductible, puis son exécution sur une machine ou sur un cluster — c'est le sous-domaine [[Conteneurs & orchestration]], de [[Docker]] à [[Kubernetes]]. **Quand ça tourne** : à chaque poussée, chaque tag, chaque nuit — [[GitHub Actions]] construit et teste, [[Argo CD]] déploie depuis Git sur un cluster — sous-domaine [[Forges & CI-CD]]. Sur site, la forge et la CI sont à héberger : [[GitLab CE]], [[Forgejo]], [[Jenkins]], [[Woodpecker CI]].
- Pour un projet data, l'image est ce qui rend un modèle transportable — la version de Python, celle de CUDA, les bibliothèques natives que `pip` ne gère pas. C'est aussi ce qui explique le poids des images ML, et pourquoi le multi-stage et le cache de couches y comptent plus qu'ailleurs.
- L'usage de [[Docker]] en **test** mérite d'être connu à part : [[testcontainers]] démarre une vraie base ou un vrai broker le temps d'un test, ce qui supprime une catégorie entière de mocks.
- Le domaine reste incomplet, et le dit : la spécialité de ce brain est l'**on-prem**, et Terraform, Ansible et un registre d'images (Harbor, prévu au bloc suivant) n'y ont pas encore de fiche. Les reverse proxies et le TLS sont dans [[Reverse proxies]] (domaine Web & API), parce qu'ils exposent une application avant de la déployer. C'est un manque connu, pas un choix.

## Choisir

- Packager une application ou un modèle avec son environnement → [[Docker]] ; l'exécuter, de la machine unique au cluster → [[Conteneurs & orchestration]].
- Lancer les tests, construire l'image et publier à chaque commit → [[GitHub Actions]].
- Déployer sur un cluster Kubernetes depuis un dépôt Git, avec la trace de chaque changement → [[Argo CD]].
- Une forge Git et une CI internes, quand le code n'a pas le droit d'aller chez GitHub → [[Comparatif - CI-CD auto-hébergé]] : [[GitLab CE]] (tout-en-un, lourd, une partie payante), [[Forgejo]] (légère) avec [[Woodpecker CI]], ou [[Jenkins]] (le plus souple, le plus exposé). Les règles d'un pipeline sur site : [[Pipelines CI-CD on-prem — runners, secrets et artefacts]].
- Des dépendances jetables pendant un test → [[testcontainers]], au-dessus de Docker.

<!-- AUTO:START -->
### Sous-domaines
- [[Conteneurs & orchestration]] · [[Forges & CI-CD]]
<!-- AUTO:END -->
