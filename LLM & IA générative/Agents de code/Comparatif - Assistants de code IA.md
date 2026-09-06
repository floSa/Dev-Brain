---
role: comparatif
nom: Comparatif - Assistants de code IA
categorie: llm/agent-de-code
tags: [code-assistant, agents, code-generation]
---

# Comparatif - Assistants de code IA

> On tranche sur : ce que la brique fait dans la chaîne — écrire le code, dire à l'agent quoi écrire, superviser plusieurs agents, ou leur fournir le contexte — puis, pour celles qui écrivent, où l'on travaille et à qui part le code.

![[Comparatif - Assistants de code IA.base]]

## Ce qui départage

- [[Aider]] — le pair-programmeur du **terminal**, agnostique de l'éditeur : chaque édition devient un **commit git atomique**, donc annulable une par une, et une *repo map* de toute la base sert de contexte. Tout passe par git — un dépôt non initialisé ou sale complique le suivi — et cette repo map fait grimper la facture sur un gros dépôt.
- [[Cline]] — l'agent autonome dans l'IDE, avec la boucle **Plan/Act** : il raisonne d'abord sur une stratégie, puis exécute avec approbation à chaque étape. C'est aussi le seul du lot dont le support **MCP est de première classe** (marketplace, stdio/SSE) — ce qui élargit d'autant la surface d'exécution à vérifier.
- [[Continue]] — le seul à faire de l'**autocomplétion inline** en plus du chat, de l'édition et de l'agent, dans VS Code comme dans JetBrains, avec *bring your own model* — local ou API. Réserve à surveiller : le plugin JetBrains est passé en maintenance communautaire, l'éditeur poussant vers la CLI.
- [[pi]] — le seul CLI de codage dont le **LLM auto-hébergé est un citoyen de première classe** : `/login llama.cpp`, gestion des modèles chargés, tout endpoint OpenAI- ou Anthropic-compatible déclarable. Contrepartie écrite noir sur blanc dans son README : **aucun système de permissions** — ni fichiers, ni processus, ni réseau. L'isolation est à la charge de l'utilisateur.
- [[freebuff]] — l'inverse exact de pi sur le même axe : **ni clé API ni paiement**, les modèles étant hébergés par l'éditeur et le service financé par la publicité. Le prix est le sujet de la fiche — prompts et contenu collé analysés pour le ciblage, soumissions réutilisables pour l'entraînement, sessions journalières plafonnées. À écarter dès qu'il s'agit de code client.
- [[Spec Kit]] — n'écrit pas de code : il impose le **spec-driven development**, une spécification exécutable qui devient la source de vérité et pilote l'agent, plus une « constitution » de principes à respecter. L'effort se déplace vers l'amont sans disparaître — une spec bâclée produit un code bâclé.
- [[BMAD]] — même étage que Spec Kit, mais découpé en **rôles agiles nommés** (analyst, PM, architect, dev, UX, scrum master, test architect) et en **stories** isolées chacune dans un chat neuf. Il pilote, il ne code pas. Churn important : v4 et v6 sont incompatibles, verrouiller une version.
- [[i-have-adhd]] — un fichier `SKILL.md`, rien à exécuter : dix règles qui reformatent la **sortie** de l'agent — action d'abord, état rappelé à chaque tour, ni préambule ni récapitulatif. Effet fort sur la verbosité, **nul sur la justesse**.
- [[t3code]] — un **plan de contrôle**, pas un assistant : il ne parle à aucun LLM et pilote des CLI déjà installées (Claude Code, Codex, Cursor, OpenCode, Grok), depuis un desktop, un navigateur ou un téléphone. Qualité, coût et confidentialité restent entièrement ceux de la CLI sous-jacente.
- [[swarm-forge]] — orchestre plusieurs agents en parallèle sur **tmux**, chacun dans son propre **git worktree**, avec des handoffs asynchrones et une porte d'audit qui interdit de resoumettre un handoff inchangé. Bloquant en contexte professionnel : le dépôt **ne déclare aucune licence**, donc n'accorde aucun droit d'usage.
- [[Maka]] — l'axe est la **traçabilité** : chaque message, appel d'outil et décision de permission part dans un journal **append-only** rejouable, local. Deux bornes dures : **Linux n'est pas supporté**, et aucune release Apache n'est encore publiée.
- [[Graphify]] — ne code pas, il **cartographie** : le dépôt indexé en knowledge graph (Tree-sitter, communautés Leiden, *god nodes*), que l'assistant lit avant de grep. Le graphe est un artefact à régénérer — périmé, il induit l'assistant en erreur.
- [[ai-memory]] — l'autre fournisseur de contexte, mais dans le temps plutôt que dans l'espace : un serveur MCP qui consolide les sessions en **wiki markdown versionné par git**, ce qui permet de quitter une CLI au milieu d'une tâche et de reprendre sous une autre. Windows natif expérimental, WSL2 recommandé.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
