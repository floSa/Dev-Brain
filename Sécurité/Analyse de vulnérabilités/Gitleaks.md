---
role: brique
nom: Gitleaks
alias: [gitleaks, gitleaks scanner, zricethezav gitleaks]
pitch: "Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT."
categorie: security/analyse
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Trivy]]"]
complements: ["[[GitHub Actions]]"]
tags: [secret-scanning, supply-chain, ci-cd]
url_docs: https://github.com/gitleaks/gitleaks#readme
url_repo: https://github.com/gitleaks/gitleaks
---

# Gitleaks

<!-- AUTO:BANDEAU:START -->
> Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui cherche des **secrets en dur** — mots de passe, clés d'API, jetons — dans l'historique d'un dépôt Git (`gitleaks git`, qui parcourt les correctifs de `git log -p`), dans un répertoire (`gitleaks dir`) ou sur l'entrée standard (`gitleaks stdin`). La détection est locale : des règles en TOML, chacune une expression régulière, un seuil d'entropie et des mots-clés ; il n'appelle aucun service pour savoir si le secret est encore actif, ce qui donne des faux positifs qu'une vérification en ligne aurait écartés. Relevé le 2026-09-30 : **v8.30.1** (2026-03-21), environ 29 600 étoiles, licence **MIT**. Le README annonce désormais : l'outil est « feature complete », les prochaines versions ne seront que des correctifs de sécurité, et l'auteur se concentre sur **Betterleaks**. C'est l'état de maintenance à connaître avant de l'installer dans une chaîne livrée à un client.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un binaire unique, sans réseau ni compte, pour bloquer un secret **avant le commit** (hook pre-commit) | Une vérification active des secrets trouvés (savoir lesquels sont encore valides) : aucune dans Gitleaks |
| Un audit d'un dépôt client : tout l'historique Git se parcourt, secrets supprimés compris | Des nouvelles fonctions attendues : l'auteur n'en fusionne plus, seulement des correctifs de sécurité |
| Des règles maintenables à la main dans un seul fichier TOML, avec listes d'exceptions | Une CI GitHub d'**organisation** qui ne veut pas d'une clé de licence pour l'action officielle : la licence de l'action a changé à la v2.0.0 (voir ci-dessous) |
| Un moteur éprouvé : c'est celui de la détection de secrets en pipeline de GitLab | Des secrets dans des formats binaires, des images ou un historique réécrit : aucun traitement documenté |

## Mise en œuvre

- Installation — un binaire Go unique ; images `zricethezav/gitleaks` et `ghcr.io/gitleaks/gitleaks`
- Point d'entrée — `gitleaks git`, `gitleaks dir`, `gitleaks stdin` ; `detect` et `protect` sont **dépréciés depuis la v8.19.0** ; le hook officiel exécute `gitleaks git --pre-commit --redact --staged --verbose` (variantes golang, docker ou système) ; sorties JSON, CSV, JUnit, SARIF ou gabarit Go ; code de sortie 1 en cas de fuite. Configuration par `--config`, `GITLEAKS_CONFIG`, `.gitleaks.toml` dans la cible, ou défaut intégré
- Prérequis — exceptions : commentaire `gitleaks:allow` sur la ligne, `.gitleaksignore` (empreintes), `--baseline-path` (ignorer l'existant pour ne relever que le neuf), listes d'exceptions dans le TOML. L'exemple pre-commit du README cite encore `v8.24.2` : y mettre la version courante. Un secret détecté est à considérer comme **compromis** et à faire tourner : l'effacer du dernier commit ne l'efface pas de l'historique
- Exécution — local ou CI, sans serveur ; la documentation officielle ne parle pas d'hors ligne, mais n'y décrit aucun appel réseau — à confirmer par une exécution sans accès sortant sur le poste cible
- Coût — gratuit pour le binaire. **L'action `gitleaks/gitleaks-action` est sous licence personnalisée depuis la v2.0.0** (les versions antérieures restent MIT) : sur un compte d'organisation GitHub, elle exige une clé `GITLEAKS_LICENSE`, annoncée gratuite, obtenue par formulaire ; le texte de cette licence n'a pas pu être lu ici. Appeler le binaire directement dans une étape de workflow évite la question

## Limites à connaître

- **Bruit mesuré.** Une étude indépendante de 2023 (Basak, Cox, Reaves, Williams, NC State, benchmark SecretBench, arXiv 2307.00714) mesure pour Gitleaks le meilleur rappel du lot (88 %) mais une précision de 46 %, avec des causes citées : règles génériques et entropie peu discriminante. L'étude porte sur les versions de 2023.
- **Propriété du dépôt peu claire.** Le README annonce le déplacement de l'auteur vers Betterleaks ; le site `gitleaks.io` ne le mentionne pas et présente encore un mainteneur individuel ; les fusions récentes (juin-juillet 2026) sont des mises à jour Dependabot, fusionnées par un autre compte que celui de l'auteur. Qui détient le dépôt aujourd'hui n'est établi par aucune source officielle lue.
- **Betterleaks** (MIT, environ 2 100 étoiles, v1.9.0 du 2026-09-29) se présente comme maintenu par les auteurs de Gitleaks, avec validation des secrets en option ; ses chiffres de rappel sont ceux de son auteur. Il n'a pas de fiche ici : trop récent pour le critère « éprouvé ».
- **Avis de sécurité** : aucun avis GitHub publié sur `gitleaks` ni `gitleaks-action`. Un CVE (CVE-2026-63728, injection de gabarit par des fonctions Sprig non hermétiques — `env`, `expandenv`, `getHostByName` — permettant à un gabarit de rapport malveillant d'exfiltrer l'environnement) est rapporté via Red Hat Bugzilla, versions antérieures à 8.30.1, gravité 6,3 selon un agrégateur tiers : ne pas exécuter un gabarit de rapport d'origine non fiable.
- Aucune compromission de l'action ou de l'image trouvée dans les campagnes de 2025-2026 consultées, ce qui n'est pas une preuve d'absence.

## Écosystème

### Alternatives

- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — pour la seule détection de secrets : son détecteur, décrit par sa documentation comme inspiré de Gitleaks, apporte des règles intégrées et un `trivy-secret.yaml`, sans mesure de précision documentée. TruffleHog (AGPL-3.0, vérification active) et Betterleaks (MIT, successeur annoncé) n'ont pas de fiche : le [[Comparatif - Scanners de sécurité]] dit pourquoi.

### Compléments

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — l'action `gitleaks/gitleaks-action` sous licence à clé pour les organisations ; à épingler par SHA comme toute action tierce.

## Ressources

- Documentation — https://github.com/gitleaks/gitleaks#readme
- Dépôt — https://github.com/gitleaks/gitleaks
- Dépôt — l'action GitHub et sa licence : https://github.com/gitleaks/gitleaks-action
- Dépôt — Betterleaks, le successeur annoncé : https://github.com/betterleaks/betterleaks
- Papier — Basak et al., « SecretBench » et comparaison d'outils, ESEM 2023 : https://arxiv.org/abs/2307.00714
- Documentation — la détection de secrets en pipeline GitLab : https://docs.gitlab.com/user/application_security/secret_detection/pipeline/

## Voir aussi

- [[Analyse de vulnérabilités]] — le hub du dossier
- [[Supply chain logicielle et SBOM]] — la notion : ce qu'un scanner voit et ne voit pas
- [[Comparatif - Scanners de sécurité]] — Trivy, Grype, Gitleaks, Semgrep et Dependency-Track par usage
- [[Gestion des secrets]] — la notion voisine : que faire d'un secret détecté, où le ranger ensuite
