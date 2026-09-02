---
role: notion
nom: Agent skills
alias: [skill, skills, agent skill, mémoire procédurale, procedural memory, SKILL.md]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm, tool-use, context-engineering]
---

# Agent skills

## Aperçu

- Un **skill** est une procédure réutilisable donnée à un agent : des instructions rédigées, éventuellement accompagnées de scripts, de gabarits et de ressources, que l'agent charge **quand la tâche s'y prête**.
- C'est de la **mémoire procédurale** — le « comment faire », par opposition à la mémoire épisodique (« ce qui s'est passé ») et sémantique (« ce qui est vrai ») que couvre [[Agent memory]].

## Concepts clés

### Chargement conditionnel

Un skill n'est pas injecté en permanence dans le contexte. Seule sa **description** reste chargée en continu ; le corps n'est lu que si la tâche correspond. Ce mécanisme rend le coût d'un catalogue de skills à peu près indépendant de sa taille — c'est ce qui distingue un skill d'un simple bloc de prompt système.

La conséquence pratique est contre-intuitive : la **description** compte plus que le contenu. Un skill excellent jamais déclenché ne sert à rien.

### Skill, outil, serveur MCP

Trois choses souvent confondues :

| | Apporte | Forme |
|---|---|---|
| **Outil** | une capacité (appeler une API, lire un fichier) | fonction appelable |
| **Serveur [[mcp-protocol]]** | un lot d'outils exposés de façon standard | processus externe |
| **Skill** | un **savoir-faire** — quand et comment utiliser les outils | instructions + fichiers |

Un skill n'ajoute donc pas de capacité brute : il ajoute du **jugement** sur des capacités déjà présentes. D'où sa complémentarité avec MCP, qui règle le problème inverse.

### Skills auto-créés

Certains agents écrivent leurs propres skills après avoir résolu une tâche complexe, puis les raffinent à la réutilisation — c'est le principe de la boucle d'apprentissage de [[Hermes Agent]]. L'agent transforme une réussite ponctuelle en procédure rejouable.

Le gain est réel, le risque aussi : un skill erroné se **rejoue indéfiniment** et se propage aux tâches suivantes. Une procédure auto-générée mérite la même relecture qu'un commit.

## En pratique

- **Écrire la description en premier**, en pensant aux formulations réelles de l'utilisateur : c'est elle qui décide du déclenchement.
- **Un skill = une procédure.** Un skill fourre-tout ne se déclenche jamais au bon moment.
- Sortir le volumineux du corps principal (`references/`, `templates/`, scripts) et n'y laisser que la marche à suivre — même logique de budget de contexte que le chargement conditionnel.
- **Versionner les skills comme du code** : ce sont des instructions exécutées par une machine, avec les mêmes effets de bord.
- Pièges : skills tiers non audités (vecteur d'exfiltration documenté sur [[OpenClaw]]) ; descriptions qui se recouvrent et rendent le déclenchement aléatoire ; procédures figées qui survivent au changement d'API qu'elles décrivent.

## Approches voisines & alternatives

- [[Agent memory]] — la mémoire déclarative (faits, historique) ; les skills en sont le pendant procédural.
- [[mcp-protocol]] — fournit les **outils** ; les skills fournissent la **méthode** pour s'en servir.
- [[Tool use patterns]] / [[tool-use]] — l'appel d'outil lui-même, brique élémentaire qu'un skill orchestre.
- [[Context engineering]] — le chargement conditionnel est une technique de gestion du budget de contexte.
- [[Agent patterns]] — les patrons d'organisation de la boucle, dans laquelle les skills s'insèrent.
- Alternative : **tout mettre dans le prompt système** — simple et prévisible, mais le contexte sature dès que les procédures se multiplient.
- Skills fichés : [[Archify]] (génération de diagrammes), [[i-have-adhd]] (discipline de sortie), [[BMAD]] (jeu d'agents et de workflows pour le cycle de développement).

## Pour aller plus loin

- Anthropic (2025) — *Agent Skills* : format `SKILL.md` (frontmatter `name` + `description`, chargement progressif).
- Implémentations : [[OpenClaw]] (skills communautaires, en cours de remplacement par MCP), [[Hermes Agent]] (skills auto-créés et raffinés).
- Liés : [[Agent evaluation]] — mesurer si un skill se déclenche et améliore réellement le résultat.
