---
role: brique
nom: ccusage
alias: [ccusage-cli, coût des agents de code, usage des jetons]
pitch: "Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session."
categorie: devtools/projet
famille: cli
licence_type: open-source
maturite: production
langage: Rust
alternatives: []
complements: ["[[ActivityWatch]]"]
tags: [project-management, metrics, agents]
url_docs: https://ccusage.com/
url_repo: https://github.com/ccusage/ccusage
---

# ccusage

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui répond à une question de coût : combien de jetons, et donc combien d'argent, ont consommé les sessions de mes agents de code ? Il ne fait que **lire les données locales** que les agents écrivent sur le disque, et les agrège par jour, semaine, mois ou session, ou par projet pour Claude Code (`--instances`). Chaque rapport sort aussi en JSON (`--json`).

Les sources prises en charge, d'après le README relu le 2026-10-07 : Claude Code, Codex, OpenCode, Amp, Droid, Codebuff, Hermes Agent, pi-agent, Goose, OpenClaw, Kilo, Kimi, Qwen, GitHub Copilot CLI, Gemini CLI, Antigravity, Grok Build CLI et ZCode, soit 18. Une commande par agent (`ccusage claude daily`) ou un rapport unifié (`ccusage daily`). Pour Claude Code, `ccusage blocks` suit les **fenêtres de facturation de cinq heures** et `ccusage statusline` fournit une ligne d'état (fonction annoncée en bêta).

Relevé le 2026-10-07 : **v20.0.26** (2026-09-27), dernier commit le même jour, licence MIT (fichier `apps/ccusage/LICENSE`, auquel le `LICENSE` de la racine renvoie). Le projet a changé d'adresse : le README et `package.json` pointent vers `github.com/ccusage/ccusage` ; l'ancienne adresse `ryoppippi/ccusage` redirige.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Voir où partent les jetons d'un agent de code, par jour, par session ou par projet | Mesurer la qualité du travail de l'agent : voir [[Agent evaluation]], ccusage ne mesure que le volume |
| Plusieurs agents en parallèle, dont des agents libres (OpenCode, Goose, pi, Qwen) : un seul rapport pour tous | Un agent qui n'écrit aucun journal local, ou une session sur une machine à laquelle l'outil n'a pas accès |
| Garder un budget : un tableau mensuel (jetons, coût estimé, par projet) suffit en solo | Un suivi d'équipe centralisé avec alertes : l'outil lit un poste, pas une flotte |
| Rapprocher le coût du résultat (voir [[Mesurer un projet - DORA, coût des agents et temps passé]]) | Le temps humain : [[ActivityWatch]] ou [[Kimai]], ccusage ignore ce que fait la personne |

## Mise en œuvre

- Installation — rien à installer : `npx ccusage@latest`, `bunx ccusage`, `pnpm dlx ccusage` ou `nix run github:ccusage/ccusage`. Un exécuteur de paquets est donc requis
- Point d'entrée — la ligne de commande : `ccusage daily`, `weekly`, `monthly`, `session`, `blocks` ; filtres `--since`, `--until`, `--last`, `--timezone`
- Prérequis — les journaux locaux de l'agent, aux emplacements par défaut ou indiqués (`--pi-path` pour pi)
- Exécution — la conversion en dollars s'appuie sur un fichier de prix issu de **LiteLLM** (embarqué dans les builds Nix, d'après le README) ; `--offline` utilise des prix mis en cache, un fichier `ccusage.json` surcharge le prix d'un modèle, `--no-cost` masque les colonnes de coût
- Coût — gratuit

## Limites à connaître

- **Un coût estimé, pas une facture.** Le chiffre vient des jetons lus et d'un barème de prix ; il se compare à la facture ou au quota réel du fournisseur, il ne les remplace pas.
- **Le projet bouge vite.** Version majeure 20, dix-huit sources, un commit le jour du relevé : la sortie peut évoluer, épingler la version dans un script qui lit la sortie JSON.
- **Il ne voit que le poste.** Rien n'est centralisé : agréger plusieurs machines ou plusieurs personnes reste à faire autour de l'outil.

## Écosystème

### Compléments

- [[ActivityWatch]] — Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le temps ; les données restent sur la machine. — le temps humain, à côté du coût des agents : les deux se mesurent à part.
- Claude-Code-Usage-Monitor (MIT) — suivi de la consommation de Claude Code en direct, avec alertes avant la limite ; cité en texte simple, sans fiche, dans [[Mesurer un projet - DORA, coût des agents et temps passé]]. Apache DevLake (mesures DORA depuis la forge et la CI) : même traitement.

## Ressources

- Documentation — https://ccusage.com/
- Dépôt — https://github.com/ccusage/ccusage

## Voir aussi

- [[Gestion de projet]] — le hub du dossier
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : DORA, coût des agents, temps passé, et les mauvaises mesures.
- [[Cycle de vie d'un projet assisté par agent]] — la notion : le coût se lit par phase du cycle.
