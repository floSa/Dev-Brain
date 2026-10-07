---
role: brique
nom: ActivityWatch
alias: [activitywatch, aw-qt, suivi du temps automatique]
pitch: "Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le temps ; les données restent sur la machine."
categorie: devtools/projet
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: []
complements: ["[[ccusage]]", "[[Kimai]]"]
tags: [time-tracking, privacy, self-hosted]
url_docs: https://docs.activitywatch.net/
url_repo: https://github.com/ActivityWatch/activitywatch
---

# ActivityWatch

<!-- AUTO:BANDEAU:START -->
> Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le temps ; les données restent sur la machine.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Suivi du temps **automatique**, local. L'application installe un serveur sur le poste (port 5600 par défaut) et des **watchers**, petits programmes qui lui envoient ce qu'ils observent. Deux sont actifs d'office : la fenêtre au premier plan avec son titre et le nom de l'application, et l'inactivité clavier-souris (*AFK*). D'autres s'ajoutent : onglet actif du navigateur (titre, URL), fichier édité dans un éditeur (chemin, langage, nom du projet), lecteurs multimédias. Une interface web trace l'activité, la range par catégories (règles, expressions régulières) et exporte les données.

Les données sont stockées dans une base **SQLite** dans le répertoire de données de l'utilisateur, sans envoi vers un service tiers (FAQ du projet : approche « local-first »). L'application tourne sous Windows 10 ou plus, macOS 12 ou plus, Linux (glibc 2.35 ou plus) et Android.

Relevé le 2026-10-07 : **v0.14.0** (2026-10-06), dépôt actif (dernier push le jour même), licence MPL-2.0. La version 0.14 apporte une distribution expérimentale en Tauri qui embarque `awatcher` sous Linux pour prendre en charge Wayland.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Savoir où passe réellement le temps sur son propre poste, sans rien saisir | Du temps **facturable** déclaré par projet et par client : [[Kimai]] est fait pour cela |
| Garder les données chez soi : tout reste sur la machine, exportable | Surveiller d'autres personnes : l'outil est conçu pour l'usage personnel, la collecte d'une activité de travail exige l'accord explicite de la personne |
| Rapprocher le temps passé du coût des agents ([[ccusage]]) et des tickets | Un poste Linux sous Wayland sans la distribution Tauri ou un watcher alternatif : le watcher de fenêtre ne voit alors aucune fenêtre active |
| Écrire un watcher sur mesure : une API et des exemples en Python et en Rust existent | Un suivi d'équipe centralisé : le modèle est un poste, un serveur local ; la synchronisation entre appareils a des limites documentées |

## Mise en œuvre

- Installation — installeur Windows, `.dmg` macOS (une version Apple Silicon et une Intel depuis la v0.14), archive ou paquets Linux ; le programme `aw-qt` crée une icône de barre d'état et démarre le serveur et les watchers par défaut
- Point d'entrée — l'interface web locale, et une API que les watchers et les scripts appellent
- Prérequis — un poste de bureau ; extensions de navigateur pour Chrome, Firefox et Edge
- Exécution — le serveur est `aw-server-rust` ou la version Python plus ancienne ; le démarrage à l'ouverture de session se règle à part
- Coût — gratuit (la FAQ du projet dit « completely free »)

## Limites à connaître

- **Un watcher ne voit que ce qu'il sait lire.** Le projet l'écrit : la fenêtre active n'est pas forcément celle que l'on regarde, et l'inactivité mesurée au clavier et à la souris ignore le travail fait sans eux (lecture, appel).
- **Wayland.** Le protocole n'a pas de notion de fenêtre active : dans des compositeurs comme Mutter (GNOME), le watcher de fenêtre est inopérant. Contournements : X11, un watcher alternatif, ou la distribution Tauri de la v0.14, expérimentale.
- **Le temps déduit n'est pas le temps déclaré.** Rien ne relie une fenêtre à un ticket ou à un client : pour un devis ou une facture, il faut une saisie.

## Écosystème

### Compléments

- [[ccusage]] — Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session. — le coût des agents, à côté du temps humain.
- [[Kimai]] — Application web de suivi du temps à héberger (AGPL-3.0, PHP, Symfony) : feuilles de temps, clients et projets, tarifs, budgets, factures et API JSON, multi-utilisateur avec LDAP ou SAML. — le temps déclaré et facturable : ActivityWatch le déduit, Kimai le saisit.

## Ressources

- Documentation — https://docs.activitywatch.net/en/latest/introduction.html
- Dépôt — https://github.com/ActivityWatch/activitywatch
- Documentation — FAQ : https://docs.activitywatch.net/en/latest/faq.html

## Voir aussi

- [[Gestion de projet]] — le hub du dossier
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : le temps passé, le coût des agents et les mauvaises mesures.
