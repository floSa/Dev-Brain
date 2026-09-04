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

<!-- AUTO:BANDEAU:START -->
> Skill/plugin MIT pour agents de code (Claude Code, Cursor, Codex, Gemini, Qwen, Kimi) imposant dix règles de sortie : action en premier, étapes numérotées, état rappelé à chaque tour, ni préambule ni récapitulatif.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Extension Markdown | open-source | dans le moteur hôte, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Un fichier `SKILL.md`, distribué comme plugin Claude Code et comme skill multi-agents, qui
reformate la sortie d'un agent de code pour un lecteur qui veut aller droit au but — la cible
annoncée étant les personnes avec un TDAH, l'usage réel étant plus large. Le contenu tient en
**dix règles** — action suivante en premier, travail multi-étapes numéroté, dernière action de
moins de deux minutes, digressions supprimées, état rappelé d'un tour à l'autre, estimations de
temps chiffrées, gains rendus visibles, ton factuel sur les erreurs, listes plafonnées à cinq
items, zéro préambule ni récapitulatif — et le mode persiste jusqu'à un « stop adhd mode ». La
valeur est dans le prompt, pas dans le logiciel : rien à exécuter, un effet fort sur la
verbosité et **nul sur la justesse**, et un contenu très mince au regard de sa popularité — à
lire en deux minutes et à adapter plutôt qu'à installer aveuglément.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Sessions longues avec un agent bavard, où le préambule et le récapitulatif coûtent plus de lecture que le travail lui-même | Phase d'apprentissage ou d'exploration : la concision imposée tronque les explications qui servent à comprendre, en particulier sur les erreurs et les compromis |
| Travail à étapes où l'on perd le fil : le rappel d'état à chaque tour est la règle la plus utile de l'ensemble | Revue d'architecture ou décision engageante, où le raisonnement compte autant que la conclusion |
| Vouloir tester une discipline de sortie sans l'écrire soi-même dans son `CLAUDE.md` | Configuration déjà personnalisée : le skill entre en conflit avec un `~/.claude/CLAUDE.md` chargé et avec les output-styles existants — vérifier ce qui gagne avant de l'activer en permanent |

## Mise en œuvre

- Installation — Claude Code : `claude plugin marketplace add ayghri/i-have-adhd` puis `claude plugin install i-have-adhd@i-have-adhd`, mode permanent avec `touch ~/.claude/.i-have-adhd-always`. Cursor : `npx skills add ayghri/i-have-adhd -a cursor -y`, plus une règle utilisateur à coller dans Settings → Rules. Codex : `codex plugin marketplace add … --ref main` puis `codex plugin add`, always-on via `~/.codex/AGENTS.md`. Gemini CLI : fichier `.toml` dans `~/.gemini/commands/`, ou `gemini extensions install`. Qwen Code : `qwen extensions install ayghri/i-have-adhd`. Kimi Code CLI : `/plugins` → Custom → URL
- Point d'entrée — le skill s'active dans la conversation et persiste jusqu'à « stop adhd mode »
- Prérequis — un agent de code supporté ; rien d'autre (l'API GitHub annonce « Python », c'est trompeur — il n'y a pas de programme)
- Exécution — dans l'agent hôte, sur le poste ; multiplateforme, c'est du markdown et de la configuration
- Coût — gratuit, MIT ; aucun coût propre, et un effet à la baisse sur les tokens de sortie

## Écosystème

### Alternatives

- Aucune page équivalente dans le brain à ce jour : la section est faible par construction, il n'existe pas d'autre skill de discipline de sortie fiché.
- Voisins par la forme (autres skills installés dans un agent), pas par la fonction : [[Graphify]], [[Spec Kit]], [[Archify]].

## Ressources

- Documentation — https://github.com/ayghri/i-have-adhd
- Dépôt — https://github.com/ayghri/i-have-adhd

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Agent skills]] — compétences packagées d'un agent
- [[Prompt engineering]] — conception de prompts
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Context engineering]] — composition et budget du contexte
