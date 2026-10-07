---
role: brique
nom: Claude-Code-Usage-Monitor
alias: [claude-monitor, ccmonitor, cmonitor, Maciek-roboblog/Claude-Code-Usage-Monitor]
pitch: "Outil en ligne de commande Python (MIT) qui lit les journaux locaux de Claude Code et affiche dans le terminal, en direct, la consommation de jetons, de messages et de coût sur la fenêtre de cinq heures, avec prévision et alertes avant la limite, état exportable en JSON et entrepôt local facultatif — mais il ne suit que Claude Code, là où ccusage couvre dix-huit agents."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[ccusage]]"]
complements: []
tags: [project-management, agents]
url_docs: https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
url_repo: https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
---

# Claude-Code-Usage-Monitor

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande Python (MIT) qui lit les journaux locaux de Claude Code et affiche dans le terminal, en direct, la consommation de jetons, de messages et de coût sur la fenêtre de cinq heures, avec prévision et alertes avant la limite, état exportable en JSON et entrepôt local facultatif — mais il ne suit que Claude Code, là où ccusage couvre dix-huit agents.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande (`claude-monitor`, alias `cmonitor` et `ccmonitor`) qui sert de **tableau de bord de consommation** pour un agent de code précis, Claude Code. Il lit les journaux de session de la machine et montre, en direct dans le terminal (interface Rich), trois mesures sur la **fenêtre de cinq heures** d'une session : jetons, nombre de messages et **coût**, la plus utile pour une longue session. Son plan par défaut, « Custom », apprend vos limites sur les sessions des 192 dernières heures (huit jours) pour prévoir le rythme et alerter avant d'atteindre la limite.

La version 4.0.0 (2026-06-27) en fait un « compagnon d'exploitation » : la commande `--statusline` capte les limites officielles de Claude Code, avec repli sur des estimations locales étiquetées (`official`, `local_estimate`, `experimental`, `unknown`) ; `--once`, `--compact` et `--write-state` produisent un instantané lisible par un autre programme ; un **entrepôt local facultatif** garde l'historique au-delà du nettoyage de trente jours opéré par Claude, par projet, modèle et jour, avec rapports CSV et JSON. Le README se dit « privacy-first » : tout est lu et gardé sur la machine. Licence MIT lue dans le dépôt, dépôt poussé le 2026-07-05, Python 3.9 ou plus.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Surveiller en direct la fenêtre de cinq heures d'un abonnement Claude Code, avec alerte avant la limite | Mesurer plusieurs agents (Codex, OpenCode, Goose…) sur un même tableau : [[ccusage]] |
| Exporter l'état de consommation en JSON vers une barre d'état ou un script | Mesurer le temps passé par un humain : [[ActivityWatch]] |
| Garder localement l'historique de consommation au-delà de trente jours | Mesurer la livraison d'une équipe (DORA) : [[Apache DevLake]] |
| Un outil qui n'envoie rien hors de la machine | Des chiffres exacts de facturation : les estimations locales sont étiquetées comme telles |

## Mise en œuvre

- Installation — `uv tool install claude-monitor` (recommandé par le README), `pipx install claude-monitor`, `pip install claude-monitor`, ou depuis les sources
- Point d'entrée — `claude-monitor` dans un terminal ; `--statusline` pour l'intégration à la ligne d'état de Claude Code
- Prérequis — Python 3.9 ou plus, et des journaux de session Claude Code sur la machine (`CLAUDE_CONFIG_DIR` ou `--data-paths` pour d'autres dossiers)
- Exécution — sur le poste ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[ccusage]] — Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session. — là où Claude-Code-Usage-Monitor suit en direct un seul agent avec alertes, ccusage rend des rapports sur dix-huit.

## Ressources

- Documentation — https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
- Dépôt — https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : DORA, coût des agents, temps passé, et les mauvaises mesures
- [[Cycle de vie d'un projet assisté par agent]] — le coût se lit par phase du cycle
- [[Outils de développement]] — le hub du domaine
