---
role: brique
nom: Bruno
alias: [bruno, usebruno]
pitch: "Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud."
categorie: devtools/client-api
famille: application
domaines: [data-eng, ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: JavaScript (Electron)
alternatives: ["[[Postman]]"]
complements: []
tags: [api-client, version-control]
url_docs: https://docs.usebruno.com/
url_repo: https://github.com/usebruno/bruno
---

# Bruno

<!-- AUTO:BANDEAU:START -->
> Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript (Electron) | open-source | Windows, macOS, Linux | — | à jour · 2026-08-20 |
<!-- AUTO:BANDEAU:END -->

## Définition

Client d'API pensé pour le dépôt git : une collection n'est pas une entrée de base, c'est un
dossier de fichiers texte posés sur le disque, écrits dans **Bru**, un langage de balisage
qui lui est propre. Requêtes, environnements et assertions se lisent, se diffent, se
branchent et se relisent en revue de code comme n'importe quelle source. Rien ne part vers
un serveur : ni compte, ni synchronisation, ni espace partagé. Les requêtes se scriptent en
JavaScript avec des assertions de style Chai, et une CLI rejoue les collections en
intégration continue.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Versionner les collections dans le dépôt du projet : diff lisible, branche, revue de code | Le format `.bru` n'est pas un standard : l'import/export Postman ou OpenAPI existe, mais reste imparfait |
| Travailler entièrement hors-ligne, sans compte ni envoi vers un cloud tiers | Ni mocks, ni monitoring, ni doc publiée, ni catalogue : la couche « plateforme » n'existe pas |
| Scripter les requêtes en JavaScript, avec assertions Chai et import de paquets npm | |
| Rejouer les collections en intégration continue par la CLI | |

## Mise en œuvre

- Installation — binaire, ou gestionnaire de paquets : Homebrew, Chocolatey, Scoop, Snap, Flatpak, Apt
- Point d'entrée — application de bureau ; les collections sont des fichiers `.bru` sur le disque ; CLI pour la CI
- Prérequis — Windows, macOS ou Linux ; application Electron, aucun service tiers à joindre
- Exécution — sur le poste, tout est local : aucun compte, aucune synchronisation
- Coût — gratuit sous licence MIT ; une offre commerciale ajoute support et fonctions d'entreprise sans fermer le cœur

## Écosystème

### Alternatives

- [[Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.

## Ressources

- Documentation — https://docs.usebruno.com/
- Dépôt — https://github.com/usebruno/bruno

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Clients d'API]] — ce qui départage les clients du dossier
