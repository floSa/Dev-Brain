---
role: brique
nom: Skills d'Anthropic
alias: [anthropics/skills, skills officiels d'Anthropic, dépôt anthropics/skills]
pitch: "Dépôt GitHub d'Anthropic de 19 skills d'exemple, sans licence à la racine : 14 sous Apache-2.0, 4 de documents source-available, 1 sans licence — un annuaire à lire, dont on ne reprend que les skills libres, pas un outil à installer en bloc."
categorie: devtools/annuaire-standard
famille: annuaire
domaines: [ai-eng]
alternatives: []
complements: ["[[Agent Skills - la spécification]]"]
tags: [agent-skill, skills, agents]
url_docs: https://github.com/anthropics/skills
url_repo: https://github.com/anthropics/skills
---

# Skills d'Anthropic

<!-- AUTO:BANDEAU:START -->
> Dépôt GitHub d'Anthropic de 19 skills d'exemple, sans licence à la racine : 14 sous Apache-2.0, 4 de documents source-available, 1 sans licence — un annuaire à lire, dont on ne reprend que les skills libres, pas un outil à installer en bloc.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Annuaire | — | rien à exécuter | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Licence, à lire en premier.** Le dépôt `anthropics/skills` n'a **pas de licence à la racine** : chaque skill porte la sienne. Relevé skill par skill le 2026-10-07 : **14 sous Apache-2.0** (fichier `LICENSE.txt` du skill), **4 réservés** (`docx`, `pdf`, `pptx`, `xlsx` : « tous droits réservés », usage régi par l'accord du lecteur avec Anthropic, que le README appelle *source-available*, pas open source), **1 sans aucune licence** (`doc-coauthoring`). Le vocabulaire du brain n'a pas de valeur « mixte » pour `licence_type` : le champ est laissé **vide**, et c'est cette section qui dit la vérité. Seuls les skills sous Apache-2.0 sont recommandés ici.

**Nature de cette page** : un annuaire de dossiers de skills, publié par l'éditeur de Claude. Rien ne s'installe d'un bloc, rien ne se déploie. Le README le dit lui-même : ces skills sont fournis « à des fins de démonstration et d'éducation », pour montrer des motifs, et le comportement obtenu dans Claude peut différer. Le format qu'ils suivent est décrit dans [[Agent Skills - la spécification]] ; le mécanisme, dans la notion [[Agent skills]].

Le dépôt, relevé le 2026-10-07 : créé le 2025-09-22, non archivé, dernier push le 2026-10-05, aucune release, environ 180 000 étoiles. Dossiers : `skills/` (19 skills), `spec/` (un renvoi vers agentskills.io), `template/` (un squelette de skill), un fichier de notices de tiers et un marché de plugins pour Claude Code.

## Les licences, skill par skill

Relevé dans le fichier `LICENSE.txt` de chaque dossier. Les noms seuls : ce que fait chaque skill est dans son `SKILL.md`.

| Licence | Skills |
|---|---|
| **Apache-2.0** — à reprendre | `academy-guide`, `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`, `discernment-nudge`, `frontend-design`, `internal-comms`, `mcp-builder`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `webapp-testing` |
| **Réservée (source-available)** — ne pas reprendre | `docx`, `pdf`, `pptx`, `xlsx` |
| **Aucune licence trouvée** — ne pas reprendre | `doc-coauthoring` |

Trois d'entre eux sont étudiés dans [[Quel skill pour quelle étape]] (`skill-creator`, `mcp-builder`, `webapp-testing`), avec la licence relevée le même jour.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Voir comment un éditeur écrit un skill avant d'écrire le sien : description, découpage en `references/`, scripts | Un skill pour une étape précise du cycle de projet → [[Quel skill pour quelle étape]], qui compare les jeux fichés |
| Reprendre un skill **sous Apache-2.0**, en gardant sa licence et ses notices | Reprendre `docx`, `pdf`, `pptx`, `xlsx` ou `doc-coauthoring` : droits réservés ou aucune licence |
| Partir du dossier `template/` pour un skill neuf | Installer le marché de plugins en bloc : le plugin `document-skills` ne contient que les quatre skills réservés, et `example-skills` contient `doc-coauthoring`, sans licence |

## Mise en œuvre

- Installation — aucune pour lire ; pour essayer, Claude Code propose d'enregistrer le dépôt comme marché de plugins (`/plugin marketplace add anthropics/skills`), puis d'installer un plugin. **Les plugins mélangent les licences** (voir plus haut) : copier à la main un dossier libre est plus sûr qu'installer un plugin.
- Point d'entrée — le dossier `skills/` du dépôt
- Prérequis — un agent qui prend en charge les skills
- Exécution — rien à exécuter ; les scripts d'un skill s'exécutent dans l'agent hôte
- Coût — gratuit à lire ; l'usage des skills réservés dépend de l'accord avec Anthropic

## Limites à connaître

- **Pas de licence racine** : un outil de conformité qui lit le dépôt comme un tout ne voit rien. La licence se lit dans chaque dossier, et change d'un skill à l'autre.
- **Des skills « de production » côtoient des exemples** : `docx`, `pdf`, `pptx` et `xlsx` sont, d'après le README, ceux qui font tourner les capacités documentaires de Claude, partagés comme référence, pas comme logiciel libre.
- **Le contenu bouge** : le skill `claude-api` reçoit des mises à jour fréquentes (trois commits entre le 2026-09-24 et le 2026-10-05). Un skill copié se périme.
- **Un skill est du code exécuté** : relire un skill avant de l'activer, même d'un éditeur connu.

## Écosystème

### Alternatives

- Aucune alternative déclarée : les jeux de skills de la communauté sont des outils à installer (rangés dans [[Agents de code]]) ; ce dépôt est un annuaire d'exemples. Deux autres annuaires existent : [[awesome-claude-code]] (une page : licence non commerciale, acceptée) et `awesome-claude-skills`, cité dans le hub du domaine sans page (aucun fichier de licence).

### Compléments

- [[Agent Skills - la spécification]] — Spécification ouverte du format SKILL.md (dépôt Apache-2.0, documentation CC-BY-4.0, née chez Anthropic) : un dossier avec un frontmatter name et description, chargé en trois temps, que 46 produits listés sur le site prennent en charge — une spécification, pas un outil, rien à installer. — le texte que ces 19 skills suivent.

## Ressources

- Documentation — https://github.com/anthropics/skills
- Dépôt — https://github.com/anthropics/skills

## Voir aussi

- [[Outils de développement]] — le hub du domaine ; les annuaires et standards de l'écosystème des agents sont rangés à part des outils (règle D-R14)
- [[Agent skills]] — la notion : ce qu'est un skill et comment il se charge
- [[Quel skill pour quelle étape]] — le choix d'un skill par étape, avec les trois skills d'Anthropic étudiés
- [[Fichiers de contexte pour agents]] — le contexte permanent d'un dépôt, à côté des skills
