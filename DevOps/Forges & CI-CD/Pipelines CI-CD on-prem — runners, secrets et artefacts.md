---
role: notion
nom: Pipelines CI-CD on-prem — runners, secrets et artefacts
alias: [Pipelines CI/CD on-prem : runners, secrets et artefacts, ci on-prem, runner ci, runners auto-hébergés, pipeline ci-cd on-prem]
categorie: devops/ci
domaines: [infra-ops, mlops]
tags: [ci-cd, self-hosted, container, supply-chain, reproducibility]
---

# Pipelines CI-CD on-prem — runners, secrets et artefacts

## Aperçu

- Un pipeline de CI/CD est une suite d'étapes qu'un **serveur** déclenche sur un événement du dépôt et qu'un **runner** exécute. Sur site, les deux sont à héberger, et c'est le runner, pas le serveur, qui concentre les risques : il exécute du code que quelqu'un a écrit, avec les secrets du projet.
- Quatre questions structurent un pipeline on-prem : **où tourne l'exécution** (et avec quelle isolation), **d'où viennent les dépendances** (surtout en réseau fermé), **où vont les résultats** (cache, artefacts, images), **ce qui est scanné** avant de livrer. Les outils changent ([[GitLab CE]], [[Forgejo]], [[Jenkins]], [[Woodpecker CI]], [[GitHub Actions]]) ; les questions restent.
- Pour la spécificité des modèles (données, entraînement, évaluation en CI), voir [[CI-CD pour le ML]] : cette page ne le répète pas.

## Concepts clés

### Anatomie d'un pipeline

- **Déclencheur** : poussée, demande de fusion, tag, planification, lancement manuel. Le déclencheur décide du niveau de confiance : une demande de fusion venant d'un fork n'a pas le même droit qu'une poussée sur la branche par défaut.
- **Étapes** : récupérer le code, installer les dépendances, vérifier, construire, tester, scanner, publier. Les cinq moteurs fichés les décrivent en YAML (`.github/workflows`, `.gitlab-ci.yml`, `.woodpecker/*.yaml`, workflows Forgejo) sauf [[Jenkins]], dont le `Jenkinsfile` est du Groovy.
- **Une étape par conteneur, ou un job sur une machine.** [[Woodpecker CI]] exécute **chaque étape dans son propre conteneur** ; GitLab Runner, Forgejo Runner et les runners GitHub exécutent un **job** dans un conteneur ou directement sur l'hôte selon la configuration ; un agent [[Jenkins]] exécute sur sa machine ou dans un pod.
- **Du résultat à la livraison** : la CI construit et publie ; un outil de déploiement ([[Argo CD]] sur un cluster) tire ensuite depuis Git, plutôt que la CI ne pousse. La CI ne doit pas garder les clés du cluster si l'on peut l'éviter.

### Runners : éphémères en conteneur ou machines permanentes

- **Permanent** : une machine qui garde son état entre les jobs. Avantage : caches chauds, rapidité. Inconvénient : tout ce que laisse un job (fichiers, images, variables, dépôt local) est visible du suivant. La documentation de GitLab Runner le dit pour le cache de dépôt en mode `fetch` sur des runners partagés : un utilisateur peut y déposer du code malveillant qui s'exécutera dans le pipeline d'un autre, y compris par des sous-modules restés accessibles après suppression.
- **Éphémère** : un environnement neuf par job, détruit après. Forgejo le pousse jusqu'au bout : en mode éphémère, « Forgejo will assign a runner at most one job before removing it » — un jeton de runner volé ne sert pas deux fois. GitLab recommande des machines virtuelles éphémères pour les opérations privilégiées, et le plugin Kubernetes de [[Jenkins]] crée **un pod par build**.
- **L'hôte est le pire cas.** Forgejo : exécuter un job directement sur l'hôte expose le fichier d'état du runner, que l'attaquant peut voler pour se faire passer pour lui. GitLab : l'exécuteur `shell` est dit à haut risque. Le mode privilégié d'un conteneur, à l'inverse, efface la frontière : « a user running a CI/CD job could gain full root access to the runner's host system ».
- **Construire des images dans la CI pose le même problème.** Donner le socket [[Docker]] au job équivaut à donner la machine ; chercher un constructeur sans démon ou un runner éphémère dédié aux builds d'images.
- **Portée d'enregistrement.** Forgejo distingue runners de dépôt, d'organisation et globaux, du plus restreint au plus exposé : un runner global exécute les jobs de n'importe quel dépôt de l'instance.
- **Où tourner sur Kubernetes.** GitLab (exécuteur Kubernetes), Jenkins (plugin Kubernetes), Woodpecker (moteur Kubernetes) et GitHub (Actions Runner Controller) savent créer des pods de job. Un runner qui vit dans le cluster a les droits de ce cluster : isoler dans un espace de noms, limiter les comptes de service.

### Isolation : le risque d'un runner partagé

- Un runner **partagé** entre des projets de confiance différente est le vecteur d'attaque type : le code d'une demande de fusion s'exécute avec l'accès du runner. Les protections sont en couches : runner par équipe ou par sensibilité ; approbation avant d'exécuter les demandes de fusion de forks (Forgejo note qu'elle n'est demandée qu'une fois : les suivantes partent seules) ; protection de la branche où vivent les workflows ; méfiance envers `pull_request_target`, qui donne accès aux secrets tout en exécutant le code de la branche cible.
- **Isoler le réseau** : les runners dans un segment qui ne voit ni le cœur du réseau ni les autres runners (recommandation de GitLab). Forgejo : passer le réseau d'un conteneur de job en mode `host` expose les services locaux qui comptent sur un reverse proxy.
- **Patcher, sans relâche.** Le serveur de CI est lui-même une cible : [[GitLab CE]] a publié des correctifs critiques le 2026-09-10 et le 2026-09-23 ; les avis sur les plugins de [[Jenkins]] tombent presque chaque mois.

### Secrets

- Le principe : un secret n'est jamais dans le dépôt, et une étape n'en reçoit que ce dont elle a besoin. La **gestion** (coffre, chiffrement versionné, rotation) est dans [[Gestion des secrets]], avec [[SOPS]] et [[OpenBao]] ; cette page ne la répète pas.
- Ce qui est propre à la CI : les secrets des **variables** du moteur sont exposés à tout job qui tourne dans l'environnement ; sur un runner compromis, ils sont volés, « including but not limited to the `CI_JOB_TOKEN` » (GitLab). D'où le jeton à durée de vie courte et à portée minimale, et la déclaration des droits (le `permissions:` du jeton GitHub).
- Un secret passé à un shell ne se met pas entre guillemets doubles sous Jenkins : Groovy l'interpole et le secret apparaît dans la liste des processus.
- Un détecteur de secrets ([[Gitleaks]]) dans le pipeline attrape ceux qui sont déjà dans l'historique.

### Cache et artefacts

- **Cache** : ce que l'on retélécharge sinon (paquets, couches). Il est **au mieux** : GitLab précise que la mise en cache est une optimisation, pas une garantie, et que des projets différents ne partagent pas le cache. **Artefact** : un résultat à passer d'une étape à l'autre ou à garder, avec une expiration (30 jours par défaut chez GitLab).
- **Le cache est un vecteur d'empoisonnement.** GitHub le nomme *cache poisoning* : un déclencheur peu fiable (demande de fusion, commentaire) peut y écrire ce qu'un pipeline de confiance restaurera ensuite. Sa parade : seuls `push`, `workflow_dispatch` et `schedule` écrivent dans le cache de la branche par défaut, les autres lisent seulement. Le cache GitHub : 10 Go par dépôt, expiré après 7 jours sans accès.
- **Plusieurs runners sans disque commun** : le cache se met sur un stockage objet compatible S3 (GitLab le documente), soit [[MinIO]], [[SeaweedFS]], [[Garage]] ou [[Ceph]] chez soi.
- **Les données d'un pipeline ML** ne passent pas par l'artefact de CI : c'est le travail de [[DVC]] et du stockage objet, pas de la CI.

### Registre d'images interne

- La CI **publie** des images ; il faut donc un endroit où les mettre. [[GitLab CE]] en livre un (le registre de conteneurs est en Free, à activer par l'administrateur). Sans forge qui en fournit un, il faut un registre à part : Harbor et ses scanners sont à traiter dans le bloc suivant.
- Un registre local peut aussi servir de **miroir** : l'image officielle de Distribution fait office de cache de tirage (*pull-through*) avec une durée de conservation (`ttl`), réglée côté démon par `registry-mirrors`. Limites documentées : un seul registre amont à la fois, et le démon Docker ne connaît que des miroirs de Docker Hub.

### Miroir des dépendances en réseau fermé

- Un réseau fermé n'atteint ni PyPI, ni npm, ni Docker Hub. Il faut un **miroir interne** de chaque source, alimenté depuis une zone ouverte, et des outils pointés dessus : avec [[uv]], un `default-index` dans `pyproject.toml` ou la variable `UV_DEFAULT_INDEX`, et des identifiants par index (`UV_INDEX_<NOM>_USERNAME`).
- **Confusion de dépendances** : uv traite l'index par défaut comme le plus faible et s'arrête au premier index qui a le paquet ; avec plusieurs index, l'ordre décide. Ne pas laisser l'ordre au hasard.
- Les **actions** des CI imitant GitHub sont des dépendances comme les autres : Forgejo les résout par défaut depuis `data.forgejo.org`. En réseau fermé, les héberger soi-même ou écrire des URL complètes vers un dépôt interne.
- Les bases de vulnérabilités des scanners (voir plus bas) sont aussi des dépendances à miroiter : [[Trivy]] et [[Grype]] fonctionnent hors ligne avec une base importée à la main.

### Reproductibilité

- Une CI reproductible **verrouille** : un `uv.lock` ([[uv]]), des images Docker épinglées, des actions épinglées par SHA et non par un tag mobile — la compromission de `tj-actions/changed-files` en mars 2025 a montré ce que coûte un tag réécrit, et la fiche de [[GitHub Actions]] donne la suite.
- Un build qui ne marche que sur la machine du runner n'est pas reproductible : les étapes en **conteneur** (Woodpecker, exécuteurs Docker) le rendent plus probable que des outils installés sur un agent permanent.

### Scanner dans le pipeline

- Quatre contrôles, chacun une étape : **vulnérabilités** des dépendances et de l'image ([[Trivy]], [[Grype]], suivi long terme par [[Dependency-Track]]), **secrets** ([[Gitleaks]]), **analyse statique** du code ([[Semgrep]]), **lint** ([[Ruff]]). Le détail de chacun est dans sa fiche.
- **Un scanner est une dépendance du pipeline.** Les tags de l'action `trivy-action` ont été réécrits en mars 2026 : un scanner exécuté avec les secrets du workflow est une cible ; épingler par SHA, ou appeler le binaire.
- Tests Python : [[pytest]] ; données en CI : [[DVC]].

## En pratique

- **Petite équipe, une forge à choisir** : [[Forgejo]] avec [[Woodpecker CI]] pour l'empreinte la plus faible ; [[GitLab CE]] si le client veut tout dans un outil et peut porter 8 vCPU et 16 Go ; [[Jenkins]] s'il existe déjà, ou pour des cibles que les conteneurs ne couvrent pas.
- **Quand rester sur [[GitHub Actions]] avec des runners auto-hébergés** : quand le code a le droit d'être sur GitHub mais que les builds ne doivent pas sortir du réseau (accès à des machines d'atelier, données sensibles en entrée). Les runners sont gratuits côté plateforme (à revérifier : un frais avait été annoncé puis reporté) ; GitHub Enterprise Server, lui, exige des runners auto-hébergés et un stockage blob externe. Ne convient pas si le client interdit tout hébergement chez GitHub.
- **Le minimum à mettre en place** : runners éphémères ou dédiés par projet ; aucun mode privilégié ; réseau cloisonné ; jetons courts ; actions et images épinglées ; miroir des dépendances ; un scan avant la publication ; serveur mis à jour à chaque correctif.
- **Pièges** : un runner global « pour aller plus vite » ; le socket Docker monté dans un job ; un cache partagé entre branches non fiables ; le serveur de CI exposé sur Internet sans patch.

## Approches voisines & alternatives

- **Le GitOps** déplace la livraison hors de la CI : [[Argo CD]] tire depuis Git. Voir [[Du Compose à Kubernetes — quand changer d'échelle]].
- **Les orchestrateurs de données** ([[Airflow]] et cousins) ne sont pas des CI : ils planifient des traitements, pas des builds.
- **CI spécialisées pour le ML** : voir [[CI-CD pour le ML]].
- **Autres moteurs** sans fiche : Tekton (sur Kubernetes), Concourse, Buildbot, Drone ; le comparatif dit pourquoi : [[Comparatif - CI-CD auto-hébergé]].
- Voir aussi : [[Harbor]], [[Zot]], [[Comparatif - Registres d'images]].
