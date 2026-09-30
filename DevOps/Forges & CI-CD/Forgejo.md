---
role: brique
nom: Forgejo
alias: [forgejo]
pitch: "Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie."
categorie: devops/ci
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[GitHub Actions]]", "[[GitLab CE]]", "[[Jenkins]]"]
complements: ["[[Woodpecker CI]]", "[[Docker]]", "[[Postgres]]", "[[Keycloak]]"]
tags: [ci-cd, version-control, self-hosted]
url_docs: https://forgejo.org/docs/latest/
url_repo: https://codeberg.org/forgejo/forgejo
---

# Forgejo

<!-- AUTO:BANDEAU:START -->
> Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Forge Git auto-hébergée : dépôts, demandes de fusion, tickets, registres de paquets, et **Forgejo Actions** pour la CI. Un binaire Go, installable depuis le binaire ou en image [[Docker]] ; des paquets de distribution existent mais sont moins testés. Relevé le 2026-09-30 : **v16.0.5** (2026-09-17), environ 5 600 étoiles sur Codeberg (le dépôt d'origine). Forgejo publie une version stable tous les trois mois et une version à support long (LTS) par an, plus des correctifs de sécurité.

**Filiation.** Forgejo est né en octobre 2022 d'un fork de Gitea, quand Gitea a été repris par une société (la page de comparaison de Forgejo le dit ainsi : une lecture partisane). Depuis début 2024, les deux codes divergent et Gitea ne reprend plus les contributions de Forgejo. La gouvernance est définie par les contributeurs ; l'association à but non lucratif Codeberg e.V. (Berlin) détient les domaines et fournit les ressources ; aucune marque n'est déposée.

**Licence.** MIT jusqu'à la v8.0 incluse, **GPL v3 ou ultérieure à partir de la v9.0** (FAQ du projet). Pour un usage interne ou l'exploitation chez un client, la GPL ne gêne pas : elle n'impose rien tant que la version modifiée n'est pas redistribuée. Aucune édition payante n'est relevée.

**Gitea, la sœur.** Gitea reste sous MIT (relevé : environ 58 200 étoiles, v28.0.0 publiée le 2026-09-29), mais la société CommitGo vend une édition **Enterprise** qui ajoute SAML, journal d'audit, liste blanche d'IP, 2FA obligatoire, scan de dépendances et héritage des protections de branches. Choisir Gitea, c'est accepter cette frontière ; choisir Forgejo, c'est accepter une gouvernance associative portée par un petit noyau de mainteneurs. Gitea n'a pas de fiche ici : Forgejo en est le fork communautaire, sans partie propriétaire relevée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une forge interne légère, sur une petite machine, sans éditeur derrière | Le client exige un éditeur avec support contractuel : Gitea Enterprise ou [[GitLab CE]] avec abonnement |
| La CI décrite en YAML proche de celle de GitHub, pour ne pas réécrire les workflows existants | Des workflows GitHub complexes à reprendre tels quels : la compatibilité est partielle (voir ci-dessous) |
| Un usage interne d'ESN : la GPL ne demande rien tant qu'on ne redistribue pas un Forgejo modifié | Un parc important d'utilisateurs avec SAML et audit : à documenter avant, l'offre n'a pas été vérifiée sur ces points |
| Associer une CI à part, [[Woodpecker CI]], qui l'a comme forge officielle | Un seul outil à tout faire avec registre de conteneurs géré, sécurité avancée et approbations : [[GitLab CE]] (en partie payant) |

## Mise en œuvre

- Installation — binaire ou image Docker ; ensuite, accès à l'interface web pour la configuration et création du premier administrateur
- Point d'entrée — l'interface web ; workflows YAML versionnés dans le dépôt
- Prérequis — une base (SQLite pour un essai, [[Postgres]] pour durer : Gitea, dont Forgejo hérite, déconseille SQLite quand l'instance grossit) ; LDAP et OAuth annoncés par le projet, donc un fournisseur d'identité comme [[Keycloak]] s'y branche
- Exécution — la CI ne tourne **pas** dans le serveur : le **Forgejo Runner** (binaire, image ou paquet, licence GPL-3.0, v13.2.0 du 2026-09-18) se connecte à l'instance, choisit ses étiquettes (*labels*) et exécute les jobs ; un runner peut servir plusieurs instances, plusieurs runners une instance. La documentation avertit : « Forgejo Runner performs remote code execution » — un runner se place sur une machine isolée. Journaux gardés 365 jours, artefacts 90 jours par défaut
- Coût — gratuit ; le coût est la machine et l'équipe

## Limites à connaître

- **La compatibilité avec GitHub Actions est partielle, et le dit.** La documentation : « GitHub Actions and Forgejo Actions are not the same ». Le contexte `github` est un alias de `forgejo`. Pas de secrets ni d'OIDC pour les demandes de fusion issues de forks ; les images de conteneurs ne se mettent pas à jour toutes seules. Un chemin relatif comme `actions/checkout@v6` est résolu par `DEFAULT_ACTIONS_URL`, dont la valeur par défaut est `https://data.forgejo.org` : en réseau fermé, il faut héberger soi-même les actions ou utiliser des URL complètes.
- **Gouvernance à petite échelle.** Le financement repose sur des dons, des subventions, des bénévoles et quelques salariés détachés ; la divergence avec Gitea se creuse, ce qui complique un retour en arrière. Une migration depuis Gitea est documentée dans le guide de mise à jour.
- **Support long à surveiller.** Selon le calendrier de versions (résumé lu, non relu en source), la LTS 11.0 a pris fin le 2026-07-16 et la 15.0 tient jusqu'au 2027-07-15.
- Avis de sécurité récents de Forgejo : non vérifiés (les pages de releases de Codeberg n'ont pas pu être lues).

## Écosystème

### Alternatives

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la CI dont Forgejo Actions reprend la syntaxe, sans dépendre de GitHub.
- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes. — la forge complète et lourde, avec des fonctions gardées en éditions payantes.
- [[Jenkins]] — Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois. — un serveur d'automatisation sans forge, à brancher sur des dépôts.

### Compléments

- [[Woodpecker CI]] — CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge. — la CI qui a Forgejo parmi ses forges officielles : une alternative à Forgejo Actions, avec une étape par conteneur.
- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — l'image officielle du serveur, et le moteur des jobs du runner.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — la base conseillée dès que l'instance dépasse un essai.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — un fournisseur d'identité pour l'authentification unique, via OAuth2.

## Ressources

- Documentation — https://forgejo.org/docs/latest/
- Dépôt — https://codeberg.org/forgejo/forgejo
- Documentation — questions fréquentes (licence, gouvernance) : https://forgejo.org/faq/
- Documentation — comparaison avec Gitea : https://forgejo.org/compare-to-gitea/
- Documentation — Forgejo Actions, référence : https://forgejo.org/docs/latest/user/actions/reference/
- Documentation — installation du runner : https://forgejo.org/docs/latest/admin/actions/runner-installation/

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Comparatif - CI-CD auto-hébergé]] — le comparatif : forge intégrée ou séparée, format de pipeline, licence.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : anatomie d'un pipeline, runners, artefacts, réseau fermé.
