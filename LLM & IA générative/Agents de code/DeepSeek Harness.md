---
role: brique
nom: DeepSeek Harness
alias: [dsh, DeepSeek Harness (dsh), deepseek-harness, "@deepseek-ai/dsh", Cordis, DeepSeek Harness et Cordis]
pitch: "Application locale de harnais d'agent de code de DeepSeek AI (MIT, préversion développeur) — chaque brique (modèle, outils, sessions, bac à sable, boucle) est un plugin du framework Cordis ; fonctionne avec un modèle DeepSeek ou tout fournisseur compatible ; son bac à sable ne confine que les fichiers et un plugin installé tourne hors de lui."
categorie: llm/agent-de-code
famille: application
licence_type: open-source
hosted: [self]
maturite: experimental
langage: TypeScript
scaling: single-node
alternatives: ["[[pi]]"]
complements: []
tags: [agents, code-assistant, sandbox, self-hosted]
url_docs: https://deepseek-harness.github.io/deepseek-harness/
url_repo: https://github.com/deepseek-ai/deepseek-harness
---

# DeepSeek Harness

<!-- AUTO:BANDEAU:START -->
> Application locale de harnais d'agent de code de DeepSeek AI (MIT, préversion développeur) — chaque brique (modèle, outils, sessions, bac à sable, boucle) est un plugin du framework Cordis ; fonctionne avec un modèle DeepSeek ou tout fournisseur compatible ; son bac à sable ne confine que les fichiers et un plugin installé tourne hors de lui.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | self-hébergé · mono-nœud | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application locale de **harnais d'agent** (la commande `dsh`) : l'environnement qui entoure un modèle pour en faire un agent de code, avec fichiers, shell, recherche, planification, sous-agents et permissions. Son parti pris est une architecture **« tout est plugin »** : l'adaptateur de modèle, le registre d'outils, le journal de session, le bac à sable et la boucle d'agent sont des plugins de **Cordis**, un méta-framework TypeScript (contexte de services, injection de dépendances, événements typés, effets réversibles) maintenu depuis 2022 par l'organisation `cordiverse` ; DeepSeek en embarque une copie. Interfaces : application web locale (`127.0.0.1:3080`), application de bureau, exécuteur sans interface, serveur SDK et serveur ACP. Cordis n'a pas de fiche à part : il est décrit ici.

Relevé le 2026-10-20 : licence **MIT** lue dans les fichiers `LICENSE` de `deepseek-ai/deepseek-harness` (copyright 2026 DeepSeek) et de `cordiverse/cordis` ; dépôt créé le 2026-08-13, poussé le 2026-10-17 ; paquet npm `@deepseek-ai/dsh` en 0.2.1-rc.2 (tag `latest`, 2026-10-17), 38 versions publiées en deux mois ; Cordis en v4.0.0-rc.11 (2026-10-14). Le README parle de **« developer preview »**, annonce des changements incompatibles et renvoie à un avis de sécurité.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Construire **son propre agent** : remplacer l'adaptateur de modèle, les outils, la politique de permission, l'interface | Un agent de code prêt à l'emploi, sans configuration : c'est une **préversion** qui change chaque semaine → [[Aider]], [[OpenCode]] |
| Brancher **n'importe quel fournisseur** : DeepSeek, des fournisseurs livrés dans le catalogue, ou une API personnalisée (relais, passerelle d'entreprise, serveur auto-hébergé) | Du code sensible sur une machine **non jetable** : l'éditeur recommande lui-même une machine virtuelle ou un conteneur jetable |
| Un **journal de session** en ajout seul, d'où chaque requête envoyée au modèle peut être reconstituée | Installer des **plugins de la communauté** hors d'un environnement isolé : un plugin installé s'exécute dans le processus hôte, hors du bac à sable de l'espace de travail |
| Un cadre MIT pour étudier ou prototyper une architecture d'agent par plugins | Un cadre stable pour une équipe : pas d'audit de sécurité, pas de garantie de compatibilité, pas de gestion centralisée des politiques publiée |
| Deux réglages indépendants et lisibles : mode du bac à sable et politique d'approbation | Un confinement du réseau et des processus : le bac à sable ne gouverne **que les effets sur les fichiers** |

## Mise en œuvre

- Installation — `npx @deepseek-ai/dsh web` (Node.js 22.19 ou plus, ou 24 ou plus, d'après le manifeste racine du dépôt ; le paquet publié ne déclare pas de champ `engines`) ; ou depuis les sources avec `pnpm install`, `pnpm run build`, `pnpm dsh web`
- Point d'entrée — l'interface web sur `http://127.0.0.1:3080` ; quatre modes : Standard (agent complet), PTC (outils exposés par un SDK de code), Minimal (shell persistant et éditeur de remplacement) et Créateur (conçu pour créer des préréglages et des plugins) ; clé d'API à saisir dans *Settings → Models*, stockée en écriture seule dans `$DSH_HOME/.credentials.yaml`
- Prérequis — Node.js, et un modèle : le logiciel est gratuit, l'usage d'un modèle hébergé ne l'est pas ; une API personnalisée (OpenAI Chat Completions, OpenAI Responses ou Anthropic Messages) permet un serveur local, donc un usage sur site sans appel externe
- Exécution — local, un processus Node.js ; permissions par préréglages : `workspace-write` avec approbation (`ask`) par défaut, ou `danger-full-access` sans approbation ; bac à sable local par bwrap et Landlock (Linux), Seatbelt (macOS) ou jeton restreint et ACL (Windows, application **partielle**)
- Coût — gratuit, MIT ; la télémétrie de session et de produit suit `DSH_TELEMETRY_MODE` (`FULL`, `FEEDBACK_ONLY`, `DISABLED`) : une note de conception archivée le 2026-09-04 en fait le consentement positif, la base partagée n'envoyant qu'après un retour explicite ; fixer `DISABLED` sur un site isolé

## Limites à connaître

- **« Tout est plugin » ne veut pas dire « sans noyau ».** Les paquets du produit sont des plugins ; le noyau de Cordis, le chargeur et le lanceur restent fixes (la documentation ne liste pas ce qui n'est pas remplaçable : c'est une lecture). La boucle d'agent est remplaçable en principe ; un seul plugin de boucle est livré, hors le profil `sdk-minimal`.
- **Un plugin installé s'exécute dans le processus hôte, hors du bac à sable.** La documentation du gestionnaire de plugins écrit que le code d'un bundle installé « s'exécute dans le processus, hors du bac à sable de l'espace de travail » ; installer un plugin équivaut donc, pour le système, à un accès shell. Le bac à sable de code généré (`node:vm`) « isole les variables globales mais n'est pas une frontière de sécurité ». Aucune signature de plugin ni liste d'autorisations déclarées n'est décrite dans les pages lues.
- **Le bac à sable ne gouverne que les fichiers.** Le réseau et la visibilité des processus sont hors de son vocabulaire (« Network and process visibility are outside this vocabulary »). Un des préréglages livrés, `danger-full-access` avec `never`, n'a ni confinement ni approbation. L'avis `SAFETY.md` : projet « expérimental », « sans audit de sécurité », à ne pas traiter comme sûr ni prêt pour la production ; recommandation d'une VM ou d'un conteneur jetable.
- **Le flux du mode Créateur a changé.** La démonstration de la vidéo d'origine (un plugin d'horloge généré, approuvé puis modifié) ne correspond plus à la documentation du 2026-09-16 : le mode Créateur installe des bundles persistants par l'outil `plugin_manager`.
- **Pas de comparaison à modèle égal.** Aucune mesure ne fait varier le harnais en gardant le modèle : le critère décisif n'est pas testé. Aucune mesure indépendante de qualité sur de vraies tâches de code n'a été trouvée. La démonstration de la vidéo montre une horloge d'en-tête, pas une tâche de programmation.
- **Une frontière externe manque.** Un runtime à politique comme [[OpenShell]] ou [[sandbox-runtime]] est le genre de couche que l'éditeur n'apporte pas ; l'association n'a pas été testée.

## Écosystème

### Alternatives

- [[pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés. — la boîte à outils la plus proche par l'esprit : un harnais minimal à assembler, sans architecture à plugins ni application web, en CLI.
- voisin : [[OpenCode]] — agent de code en terminal, prêt à l'emploi, là où Harness est un cadre à composer.

## Ressources

- Documentation — https://deepseek-harness.github.io/deepseek-harness/
- Dépôt — https://github.com/deepseek-ai/deepseek-harness
- Article — papier de Cordis, « A Programming Paradigm for Spatiotemporal Composability », arXiv 2608.25512 (2026-08-26) : https://arxiv.org/abs/2608.25512

## Voir aussi

- [[Harnais d'agent]] — la notion : le modèle propose, le harnais dispose ; Harness en est un exemple à plugins
- [[Garde-fous hors modèle]] — ce que couvre un bac à sable limité aux fichiers, et ce qu'un plugin dans le processus hôte laisse à découvert
- [[Isolation par politique déclarative]] — la frontière que Harness n'apporte pas
- [[Comparatif - Isolation d'exécution d'un agent]] — son bac à sable face aux autres, sans classement
- [[Context engineering]] — la gestion du contexte est l'un des plugins
- [[Agents de code]] — le hub du dossier
