---
role: brique
nom: i-have-adhd
alias: [ayghri/i-have-adhd, adhd-mode]
pitch: "Skill/plugin MIT pour agents de code (Claude Code, Cursor, Codex, Gemini, Qwen, Kimi) imposant dix règles de sortie : action en premier, étapes numérotées, état rappelé à chaque tour, ni préambule ni récapitulatif."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Markdown
alternatives: []
complements: []
tags: [agent-skill, prompting, code-assistant, agents]
url_docs: https://github.com/ayghri/i-have-adhd
url_repo: https://github.com/ayghri/i-have-adhd
---

# i-have-adhd

## Pourquoi

Un fichier `SKILL.md`, distribué comme plugin Claude Code et comme skill multi-agents, qui reformate la sortie d'un agent de code pour un lecteur qui veut aller droit au but — la cible annoncée étant les personnes avec un TDAH, l'usage réel étant plus large.

Le contenu tient en **dix règles** : l'action suivante en premier ; numéroter le travail multi-étapes ; terminer par une action de moins de deux minutes ; supprimer les digressions ; rappeler l'état d'un tour à l'autre ; donner des estimations de temps chiffrées ; rendre les gains visibles ; ton factuel sur les erreurs ; listes plafonnées à cinq items ; zéro préambule, récapitulatif ou formule de politesse. Le mode persiste jusqu'à un « stop adhd mode ».

La valeur est dans le prompt, pas dans le logiciel : il n'y a pas de code à exécuter.

## Quand l'utiliser

- Sessions longues avec un agent bavard, où le préambule et le récapitulatif coûtent plus de lecture que le travail lui-même.
- Travail à étapes où l'on perd le fil : le rappel d'état à chaque tour est la règle la plus utile de l'ensemble.
- Vouloir tester une discipline de sortie sans l'écrire soi-même dans son `CLAUDE.md`.

## Quand NE PAS l'utiliser

- Phase d'apprentissage ou d'exploration : la concision imposée tronque les explications qui servent à comprendre.
- Revue d'architecture ou décision engageante, où le raisonnement compte autant que la conclusion.
- Configuration déjà personnalisée : le skill entre en conflit avec un `~/.claude/CLAUDE.md` chargé et avec les output-styles existants.

## Installation & plateformes

- Claude Code : `claude plugin marketplace add ayghri/i-have-adhd` puis `claude plugin install i-have-adhd@i-have-adhd` ; mode permanent avec `touch ~/.claude/.i-have-adhd-always`.
- Cursor : `npx skills add ayghri/i-have-adhd -a cursor -y`, plus une règle utilisateur à coller dans Settings → Rules.
- Codex : `codex plugin marketplace add … --ref main` puis `codex plugin add` ; always-on via `~/.codex/AGENTS.md`.
- Gemini CLI : fichier `.toml` dans `~/.gemini/commands/`, ou `gemini extensions install`. Qwen Code : `qwen extensions install ayghri/i-have-adhd`. Kimi Code CLI : `/plugins` → Custom → URL.
- Multiplateforme : c'est du markdown et de la configuration. L'API GitHub annonce « Python », c'est trompeur — il n'y a pas de programme.

## Pièges

- Effet fort sur la verbosité, **nul sur la justesse** : un agent concis n'est pas un agent plus juste.
- Risque de troncature d'explications utiles, en particulier sur les erreurs et les compromis.
- Conflit possible avec les instructions globales déjà en place — vérifier ce qui gagne avant de l'activer en permanent.
- Contenu très mince au regard de sa popularité : c'est un prompt, à lire en deux minutes et à adapter plutôt qu'à installer aveuglément.

## Alternatives

- Aucune page équivalente dans le brain à ce jour : la section est faible par construction, il n'existe pas d'autre skill de discipline de sortie fiché.
- Voisins par la forme (autres skills installés dans un agent), pas par la fonction : [[Graphify]], [[Spec Kit]], [[Archify]].

## Liens

- [[Comparatif - Assistants de code IA]] — comparatif de la catégorie
- [[Agent skills]] — concept : compétences packagées d'un agent
- [[Prompt engineering]] — concept : conception de prompts
- [[Harnais d'agent]] — concept : la couche qui entoure le modèle et exécute la boucle
- [[Context engineering]] — concept : composition et budget du contexte
- Repo : https://github.com/ayghri/i-have-adhd
