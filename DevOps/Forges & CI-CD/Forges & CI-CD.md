---
role: hub
nom: Forges & CI-CD
alias: [forge git, ci-cd, ci/cd, forges et ci]
pitch: Héberger le code et exécuter ce qui le construit, le teste et le livre — la forge, le serveur de CI, et le déploiement depuis Git.
domaines: [mlops, infra-ops]
tags: [ci-cd, version-control, self-hosted]
---

# Forges & CI-CD

> Héberger le code et exécuter ce qui le construit, le teste et le livre — la forge, le serveur de CI, et le déploiement depuis Git.

## Ce qu'il faut comprendre

- **Trois rôles, que certains outils cumulent.** La **forge** héberge les dépôts et la revue de code ([[GitLab CE]], [[Forgejo]], GitHub). Le **serveur de CI** exécute les pipelines ([[Jenkins]], [[Woodpecker CI]]). La **livraison** déploie ce que la CI a construit ([[Argo CD]] sur un cluster). [[GitHub Actions]], [[GitLab CE]] et [[Forgejo]] réunissent forge et CI ; [[Jenkins]] et [[Woodpecker CI]] s'appuient sur une forge existante.
- **Sur site, la licence se lit avant le reste.** Seuls [[Jenkins]] (MIT), [[Woodpecker CI]] (Apache-2.0) et [[Forgejo]] (GPL-3.0-or-later depuis la v9) sont entièrement libres. [[GitLab CE]] est open-core : cœur MIT, dossier `ee/` propriétaire, approbations obligatoires et SAST avancé en éditions payantes. [[GitHub Actions]] sur site suppose GitHub Enterprise Server, propriétaire.
- **Le runner est la surface de risque**, pas le serveur : il exécute du code avec les secrets du projet. [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] dit comment l'isoler, où mettre cache et artefacts, et quoi faire en réseau fermé.
- **Une forge et une CI séparées se choisissent ensemble** : [[Forgejo]] avec [[Woodpecker CI]] est l'attelage le plus léger ; [[GitLab CE]] porte tout dans un outil, au prix de 8 vCPU et 16 Go de RAM ; [[Jenkins]] reste le choix d'un existant ou de cibles que les conteneurs ne couvrent pas.
- **Hors fiches** : Gitea, Drone, Concourse, Tekton, Buildbot, SourceHut — le comparatif dit pourquoi ; Harbor, registre d'images, est prévu au bloc suivant.

## Choisir

- Une forge et une CI internes, légères, pour une petite équipe → [[Forgejo]] et [[Woodpecker CI]].
- Un seul outil pour dépôts, revue, CI et registre de conteneurs, avec un client qui connaît GitLab → [[GitLab CE]].
- Une CI qui existe déjà, des agents Windows ou du matériel à piloter → [[Jenkins]].
- Le code peut rester chez GitHub mais les builds doivent rester dans le réseau → [[GitHub Actions]] avec des runners auto-hébergés.
- Déployer sur Kubernetes depuis Git → [[Argo CD]].
- Comparer les cinq sur la forge, le format, l'exécution, le SSO et la licence → [[Comparatif - CI-CD auto-hébergé]].

<!-- AUTO:START -->
### Notions
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — domaines : infra-ops, mlops

### Briques
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé).
- [[Forgejo]] — Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie.
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.
- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes.
- [[Jenkins]] — Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois.
- [[Woodpecker CI]] — CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge.

### Comparatifs
- [[Comparatif - CI-CD auto-hébergé]]
<!-- AUTO:END -->
