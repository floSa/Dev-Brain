---
role: brique
nom: Jenkins
alias: [jenkins ci, jenkinsfile]
pitch: "Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois."
categorie: devops/ci
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[GitHub Actions]]", "[[GitLab CE]]", "[[Forgejo]]", "[[Woodpecker CI]]"]
complements: ["[[Docker]]", "[[Kubernetes]]"]
tags: [ci-cd, self-hosted]
url_docs: https://www.jenkins.io/doc/
url_repo: https://github.com/jenkinsci/jenkins
---

# Jenkins

<!-- AUTO:BANDEAU:START -->
> Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur d'automatisation open source, sans forge : il se branche sur des dépôts hébergés ailleurs (GitLab, Forgejo, GitHub, Bitbucket) et exécute des pipelines. Un **contrôleur** orchestre, des **agents** exécutent. Relevé le 2026-09-30 : LTS **2.580.1**, weekly **2.584** (2026-09-29), environ 26 600 étoiles, Java 21 ou plus requis pour le serveur. Une version LTS est choisie tous les 12 semaines, avec des versions de correctifs toutes les 4 semaines.

- **Pipeline.** Un `Jenkinsfile` versionné avec le code, en deux syntaxes : **déclarative** (structurée, introduite avec Pipeline 2.5) et **scriptée** (Groovy, presque tout le langage). La documentation le range en bonne pratique : un Jenkinsfile dans le dépôt, pas un job défini dans l'interface web.
- **Plugins.** Plus de 2 000 sur le catalogue officiel : agents, forges, authentification, notifications. C'est la force et la dette du projet : presque tout passe par un plugin, donc par un code tiers qui suit son propre cycle de sécurité.
- **Agents éphémères.** Le plugin Kubernetes lance chaque build dans un pod dédié qui disparaît à la fin, sans que Jenkins tourne lui-même dans le cluster ; il est installé sur 13,4 % des contrôleurs.
- **CloudBees** vend une distribution commerciale bâtie sur le cœur de Jenkins (haute disponibilité, droits fins, support). Lue seulement dans un billet de l'éditeur : à valider avant de citer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le client a déjà Jenkins, des Jenkinsfile et des plugins métier : migrer coûte plus que l'exploiter | Une installation neuve sans équipe pour la tenir : la dette de plugins demande un suivi régulier |
| Des cibles hétérogènes : agents Windows, machines physiques, bancs d'essai matériel, tout ce qu'un conteneur ne couvre pas | Des pipelines simples qu'une CI intégrée à la forge ([[GitLab CE]], [[Forgejo]]) couvrirait sans serveur à part |
| Une CI séparée de la forge, pour en brancher plusieurs | Une CI qui doit tenir dans 100 Mo de RAM : [[Woodpecker CI]] |
| Des pipelines en code avec des bibliothèques partagées | Un besoin de démarrer vite : le Groovy et les plugins ont une courbe d'apprentissage |

## Mise en œuvre

- Installation — paquet Linux ou image [[Docker]] ; Java 21 ou plus
- Point d'entrée — l'interface web et le `Jenkinsfile` du dépôt
- Prérequis — 256 Mo de RAM et 1 Go de disque au strict minimum ; pour une petite équipe, 4 Go ou plus de RAM et 50 Go ou plus de disque. L'authentification unique passe par des plugins : OIDC (`oic-auth`, score de santé 100 %), SAML, LDAP — ce sont des plugins, donc soumis au même cycle de sécurité que les autres
- Exécution — contrôleur plus agents ; des agents permanents sur des machines, ou éphémères dans [[Kubernetes]]
- Coût — gratuit ; le coût est l'exploitation et la veille sur les avis de sécurité

## Limites à connaître

- **La dette de sécurité des plugins est réelle et mesurable.** La page des avis de sécurité liste, pour 2026, 9 avis dont 8 touchent des plugins ; certains en corrigent 13 à 18 à la fois (2026-09-02, 2026-09-16, 2026-08-05). En 2025 : 12 avis, dont 10 sur des plugins. Un plugin sans mainteneur porte le bandeau « up for adoption » : il ne recevra plus de correctif. Ces comptes viennent d'un résumé de la page, pas d'un dénombrement ligne à ligne.
- **Les secrets.** La documentation recommande l'aide `credentials()` de la syntaxe déclarative, et des guillemets simples autour des commandes shell : des guillemets doubles font interpoler le secret par Groovy et l'exposent dans la liste des processus.
- **Plugins de SSO = plugins.** Une faille dans le plugin d'authentification est une faille d'accès au contrôleur : un plugin LDAP figure dans l'avis du 2026-05-27 (à relire dans l'avis).

## Écosystème

### Alternatives

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — une CI sans serveur à tenir, mais chez GitHub ou sur GitHub Enterprise Server.
- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes. — la forge avec CI intégrée, qui remplace serveur de CI et dépôts d'un coup.
- [[Forgejo]] — Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie. — une forge légère avec sa CI, à la place de Jenkins plus un dépôt séparé.
- [[Woodpecker CI]] — CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge. — une CI légère, une étape par conteneur, sans plugins à patcher.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — l'image officielle du contrôleur, et les conteneurs de build des agents.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — le plugin Kubernetes y lance un pod éphémère par build.

## Ressources

- Documentation — https://www.jenkins.io/doc/
- Dépôt — https://github.com/jenkinsci/jenkins
- Article — avis de sécurité : https://www.jenkins.io/security/advisories/
- Documentation — Jenkinsfile : https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
- Documentation — plugin Kubernetes : https://plugins.jenkins.io/kubernetes/

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Comparatif - CI-CD auto-hébergé]] — le comparatif : forge intégrée ou séparée, format de pipeline, licence.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : anatomie d'un pipeline, runners, artefacts, réseau fermé.
