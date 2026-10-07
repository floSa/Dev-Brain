---
role: brique
nom: AGENTS.md - le format
alias: [agentsmd, agentsmd/agents.md, format AGENTS.md]
pitch: "Format ouvert (MIT) d'un fichier Markdown AGENTS.md à la racine d'un dépôt, qui donne aux agents de code les commandes et les conventions du projet : aucun champ obligatoire, le fichier le plus proche du code l'emporte — une spécification, pas un outil, rien à installer."
categorie: devtools/annuaire-standard
famille: specification
domaines: [ai-eng]
licence_type: open-source
alternatives: []
complements: ["[[Agent Skills - la spécification]]"]
tags: [agents, context-engineering, code-assistant]
url_docs: https://agents.md
url_repo: https://github.com/agentsmd/agents.md
---

# AGENTS.md - le format

<!-- AUTO:BANDEAU:START -->
> Format ouvert (MIT) d'un fichier Markdown AGENTS.md à la racine d'un dépôt, qui donne aux agents de code les commandes et les conventions du projet : aucun champ obligatoire, le fichier le plus proche du code l'emporte — une spécification, pas un outil, rien à installer.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification | open-source | rien à exécuter | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **format** de fichier, pas un logiciel. Le site le présente comme « un format simple et ouvert pour guider les agents de code » : un « README pour les agents », c'est-à-dire un endroit prévisible où mettre ce qu'un humain apprendrait en rejoignant l'équipe (commandes de build et de test, style de code, consignes de pull request). Le dépôt `agentsmd/agents.md` ne contient pas de bibliothèque : il contient le site qui explique le format (Next.js), un exemple de fichier, et la charte technique du projet.

Ce que dit le format, relevé sur le site le 2026-10-07 :

- **Aucun champ obligatoire.** C'est du Markdown ordinaire ; les titres sont libres, l'agent lit le texte.
- **Sections courantes** : vue d'ensemble du projet, commandes de build et de test, style de code, instructions de test, sécurité.
- **Imbrication.** Un `AGENTS.md` peut vivre dans un sous-paquet (monorepo) ; l'agent lit le fichier **le plus proche** dans l'arborescence, qui l'emporte. Le message de l'utilisateur dans le chat prime sur tous les fichiers.
- **Les commandes de test listées sont exécutées** par l'agent qui tente de corriger un échec : elles doivent être justes.
- **Compatibilité ascendante** par lien symbolique, si un outil attend un autre nom de fichier.

Le site énumère plus de vingt-cinq outils compatibles (parmi lesquels Codex, Cursor, Aider, GitHub Copilot, Jules, Zed, Warp, Gemini CLI). Gouvernance, d'après le site : le format est « désormais sous la tutelle de l'Agentic AI Foundation, au sein de la Linux Foundation », né d'une collaboration entre OpenAI, Amp, Google, Cursor et Factory.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un dépôt est manipulé par **plusieurs** agents de code : un seul fichier au lieu d'un par outil | Une consigne ne doit **jamais** être violée : un fichier est lu comme du contexte, pas appliqué → un hook ou la CI, voir [[Fichiers de contexte pour agents]] |
| Écrire une fois les commandes exactes de build, de test et de lint que l'agent ne peut pas deviner | Une procédure longue et occasionnelle : elle appartient à un skill, chargé à la demande → [[Agent Skills - la spécification]] |
| Un monorepo, où chaque sous-paquet a ses propres règles | Chercher un outil qui génère ou valide le fichier : le format n'en fournit aucun |

## Mise en œuvre

- Installation — aucune : un fichier `AGENTS.md` commité dans le dépôt
- Point d'entrée — le site https://agents.md et l'exemple de son README
- Prérequis — un agent qui lit ce nom de fichier ; la liste des outils est sur le site, et chaque outil documente sa propre prise en charge
- Exécution — rien à exécuter
- Coût — gratuit, MIT

## Licence et gouvernance

- **MIT** (fichier `LICENSE` du dépôt, relevé le 2026-10-07) ; dépôt non archivé, dernier push le 2026-09-10, environ 24 800 étoiles, **aucune release publiée** : le format n'a pas de numéro de version.
- **Gouvernance** : Agentic AI Foundation (Linux Foundation) d'après le site ; le dépôt porte un `Technical_Charter.pdf`, dont le contenu n'a pas été lu pour cette fiche.

## Limites à connaître

- **Pas de schéma ni de validateur** : rien ne signale un fichier trop long, contradictoire ou périmé. Les mesures sur l'efficacité réelle de ces fichiers sont dans [[Fichiers de contexte pour agents]].
- **Un format, pas une garantie de lecture** : chaque outil décide s'il lit `AGENTS.md`, seul ou à côté de son propre fichier, et dans quel ordre. Vérifier dans la documentation de l'outil utilisé.
- **Toujours chargé** : le contenu pèse sur chaque session. C'est la différence avec un skill, dont seul le résumé reste en contexte.

## Écosystème

### Alternatives

- Aucune alternative déclarée : les fichiers propres à chaque outil (`CLAUDE.md`, `.cursor/rules/`, `.clinerules/`, `CONVENTIONS.md`) sont comparés dans la notion [[Fichiers de contexte pour agents]], pas fichés ici.

### Compléments

- [[Agent Skills - la spécification]] — Spécification ouverte du format SKILL.md (dépôt Apache-2.0, documentation CC-BY-4.0, née chez Anthropic) : un dossier avec un frontmatter name et description, chargé en trois temps, que 46 produits listés sur le site prennent en charge — une spécification, pas un outil, rien à installer. — `AGENTS.md` est le contexte toujours chargé ; un skill est la procédure chargée à la demande.

## Ressources

- Documentation — https://agents.md
- Dépôt — https://github.com/agentsmd/agents.md

## Voir aussi

- [[Outils de développement]] — le hub du domaine ; les annuaires et standards de l'écosystème des agents sont rangés à part des outils (règle D-R14)
- [[Fichiers de contexte pour agents]] — la notion : que mettre dans un fichier de contexte, où placer quoi, les pièges
- [[Agent skills]] — la notion du mécanisme voisin, les procédures chargées à la demande
- [[Context engineering]] — la discipline dont ce fichier est un outil
