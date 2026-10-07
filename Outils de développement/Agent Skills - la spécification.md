---
role: brique
nom: Agent Skills - la spécification
alias: [agentskills.io, agentskills, spécification SKILL.md]
pitch: "Spécification ouverte du format SKILL.md (dépôt Apache-2.0, documentation CC-BY-4.0, née chez Anthropic) : un dossier avec un frontmatter name et description, chargé en trois temps, que 46 produits listés sur le site prennent en charge — une spécification, pas un outil, rien à installer."
categorie: devtools/annuaire-standard
famille: specification
domaines: [ai-eng]
licence_type: open-source
alternatives: []
complements: ["[[AGENTS.md - le format]]", "[[Skills d'Anthropic]]"]
tags: [agent-skill, skills, agents, context-engineering]
url_docs: https://agentskills.io
url_repo: https://github.com/agentskills/agentskills
---

# Agent Skills - la spécification

<!-- AUTO:BANDEAU:START -->
> Spécification ouverte du format SKILL.md (dépôt Apache-2.0, documentation CC-BY-4.0, née chez Anthropic) : un dossier avec un frontmatter name et description, chargé en trois temps, que 46 produits listés sur le site prennent en charge — une spécification, pas un outil, rien à installer.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification | open-source | rien à exécuter | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un **format** de dossier, pas un logiciel. Le texte de référence du format `SKILL.md` : un skill est un dossier qui contient au minimum un fichier `SKILL.md`, composé d'un frontmatter YAML et d'un corps en Markdown, et qui peut embarquer des scripts, des références et des ressources. Le mécanisme, ses usages et ses pièges sont dans la notion [[Agent skills]] ; cette fiche ne décrit que le **texte normatif** : ce que le format impose, qui le tient, qui le lit.

Le dépôt `agentskills/agentskills` porte la documentation du site agentskills.io et `skills-ref`, une bibliothèque de référence pour valider un skill (`skills-ref validate ./mon-skill`). Le README dit que le format « a été développé à l'origine par Anthropic, publié comme standard ouvert, et adopté par un nombre croissant de produits » ; il est ouvert aux contributions de l'écosystème.

Ce que fixe la spécification, relevé sur agentskills.io le 2026-10-07 :

- **Arborescence** : `SKILL.md` obligatoire ; `scripts/`, `references/` et `assets/` facultatifs, par convention.
- **Frontmatter** : `name` (obligatoire, 1 à 64 caractères, minuscules, chiffres et tirets, ni tiret au début ou à la fin, ni deux tirets de suite, **égal au nom du dossier parent**) et `description` (obligatoire, 1 à 1 024 caractères : ce que fait le skill **et** quand l'utiliser). Facultatifs : `license` (un nom court ou le nom d'un fichier de licence embarqué), `compatibility` (jusqu'à 500 caractères : produit visé, paquets système, accès réseau), `metadata` (table de chaînes) et `allowed-tools` (liste d'outils pré-approuvés séparés par des espaces, marqué **expérimental** : la prise en charge varie selon les implémentations).
- **Chargement progressif**, en trois niveaux : métadonnées (nom et description, de l'ordre de 100 jetons par skill, chargées au démarrage), instructions (le corps, **moins de 5 000 jetons** recommandés, chargé à l'activation), ressources (chargées au besoin). Le fichier principal devrait rester sous 500 lignes ; les renvois vers d'autres fichiers ne descendent pas à plus d'un niveau.
- **Le corps est libre** : aucune restriction de format ; des sections sont recommandées (étapes, exemples d'entrées et de sorties, cas limites).

Le site liste **46 produits** compatibles au 2026-10-07, dont Claude et Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, VS Code, OpenCode, OpenHands, Goose et pi.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Écrire un skill qui doit tourner sur **plusieurs** agents sans le réécrire | Donner à l'agent le contexte permanent du projet (commandes, conventions) → [[AGENTS.md - le format]] |
| Vérifier qu'un skill respecte le format avant de le partager (`skills-ref validate`) | Chercher des skills prêts à l'emploi : la spécification n'en contient aucun → [[Skills d'Anthropic]], [[Quel skill pour quelle étape]] |
| Savoir ce qu'un client peut supposer d'un skill : champs, limites, chargement | Compter sur `allowed-tools` pour restreindre un agent : le champ est expérimental |

## Mise en œuvre

- Installation — aucune pour le format ; `skills-ref` (dépôt `agentskills/agentskills`, dossier `skills-ref`) pour valider
- Point d'entrée — https://agentskills.io/specification
- Prérequis — un agent qui prend en charge les skills ; chaque produit documente son propre emplacement de skills et son installation (liens « Setup instructions » du Client Showcase)
- Exécution — rien à exécuter ; les scripts d'un skill s'exécutent dans l'agent hôte, avec ses droits
- Coût — gratuit

## Licence et gouvernance

- **Apache-2.0** pour le code du dépôt (fichier `LICENSE`, relevé le 2026-10-07), **CC-BY-4.0** pour la documentation, d'après le README. Dépôt non archivé, dernier push le 2026-08-09, environ 26 000 étoiles, aucune release publiée.
- **Gouvernance** : développé à l'origine par Anthropic ; le README et le site disent « standard ouvert » ouvert aux contributions, sans nommer de fondation. Aucune structure de gouvernance indépendante n'a été relevée, à la différence d'AGENTS.md.
- Le dépôt `anthropics/skills` garde un dossier `spec/` dont l'unique fichier annonce que la spécification « se trouve désormais » sur agentskills.io.

## Limites à connaître

- **Le format ne dit rien du déclenchement** : la description décide si l'agent charge le skill, et la spécification ne dit pas comment un client la compare à la tâche. Un skill excellent peut ne jamais se déclencher.
- **La licence est un simple champ texte** : `license` n'est pas contrôlé. Dans `anthropics/skills`, la valeur varie d'un skill à l'autre, jusqu'à « Proprietary » : lire la licence de **chaque** skill avant de le reprendre (voir [[Skills d'Anthropic]]).
- **Un skill est du code exécuté par une machine** : un skill tiers non relu est un risque ; la spécification ne prévoit aucune signature.

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucun autre format de skill n'est fiché dans le brain. Les formats propres à un outil (extensions d'un agent, plugins) sont comparés dans la notion [[Agent skills]].

### Compléments

- [[AGENTS.md - le format]] — Format ouvert (MIT) d'un fichier Markdown AGENTS.md à la racine d'un dépôt, qui donne aux agents de code les commandes et les conventions du projet : aucun champ obligatoire, le fichier le plus proche du code l'emporte — une spécification, pas un outil, rien à installer. — le contexte toujours chargé ; un skill est la procédure chargée à la demande.
- [[Skills d'Anthropic]] — Dépôt GitHub d'Anthropic de 19 skills d'exemple, sans licence à la racine : 14 sous Apache-2.0, 4 de documents source-available, 1 sans licence — un annuaire à lire, dont on ne reprend que les skills libres, pas un outil à installer en bloc. — le dépôt officiel d'exemples qui suit ce format.

## Ressources

- Documentation — https://agentskills.io
- Dépôt — https://github.com/agentskills/agentskills

## Voir aussi

- [[Outils de développement]] — le hub du domaine ; les annuaires et standards de l'écosystème des agents sont rangés à part des outils (règle D-R14)
- [[Agent skills]] — la notion : ce qu'est un skill, chargement conditionnel, skill contre outil contre serveur MCP
- [[Quel skill pour quelle étape]] — le tableau qui réunit les jeux de skills fichés et dit lequel prendre à chaque étape
