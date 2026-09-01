---
role: notion
nom: Harnais d'agent
alias: [harnais, harness, agent harness, scaffolding, échafaudage, agent scaffold]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm, tool-use, context-engineering]
---

# Harnais d'agent

## Aperçu

- Le **harnais** est tout ce qui entoure le modèle pour en faire un agent : la boucle d'exécution, la déclaration des outils, l'assemblage du contexte, le parsing et la validation des sorties, la reprise sur erreur, la persistance, le bac à sable.
- Il sépare trois choses trop souvent confondues sous le mot « agent » : les **poids**, l'**échafaudage**, et le **système** qui en résulte.

## Concepts clés

### La triade modèle / harnais / agent

| Couche | Ce que c'est | Ce qu'elle décide | Exemples |
|---|---|---|---|
| **Modèle** | des poids, un prédicteur de token suivant | la qualité du raisonnement et des appels d'outils proposés | GLM, Kimi, Qwen, Claude — servis par [[LM Studio]] ou [[Ollama]] |
| **Harnais** | le code autour | ce que l'agent peut faire, voit, et retente | [[OpenClaw]], [[Hermes Agent]], [[LM Studio Bionic]], [[OpenHands]] |
| **Agent** | le système en marche | le résultat observé | le couple des deux, jamais l'un seul |

Le modèle **propose**, le harnais **dispose**. Un modèle ne lit pas un fichier et n'exécute rien : il émet un texte qu'un harnais interprète comme un appel d'outil, exécute, puis réinjecte.

### Ce que le harnais apporte réellement

- **Assemblage du contexte** — quoi mettre dans la fenêtre, dans quel ordre, quoi élaguer (cf. [[Context engineering]]).
- **Déclaration des outils** — schémas, descriptions, et la manière de les présenter au modèle.
- **Parsing et validation** — transformer une sortie textuelle en action typée, refuser ce qui est malformé.
- **Reprise sur erreur** — retenter, reformuler, dégrader proprement plutôt que planter.
- **Bornage** — plafond d'itérations, budget de tokens, délai (cf. [[agent-loops]]).
- **Isolation** — exécuter le code produit sans exposer l'hôte (cf. [[Sandboxing de code généré]]).

### Même modèle, harnais différent, résultat différent

C'est le point qui justifie la notion. À modèle constant, deux harnais donnent des performances très écartées : la façon de décrire les outils, de gérer un échec d'appel ou de compresser l'historique pèse autant que le choix des poids.

Conséquence directe sur l'évaluation : **un score d'agent mesure le couple modèle + harnais**, jamais le modèle seul. Comparer deux modèles suppose de figer le harnais, et inversement — c'est la règle la plus violée dans les comparatifs publics (cf. [[Agent evaluation]], [[LLM benchmarks]]).

### Une frontière qui se déplace

Ce qui relevait du harnais migre progressivement dans le modèle : la planification explicite, la réflexion en plusieurs passes ou le formatage des appels d'outils étaient des astuces d'échafaudage avant de devenir des capacités natives ([[Reasoning models]], tool use entraîné). Le harnais se vide par le haut et se concentre sur ce que le modèle ne peut structurellement pas faire : exécuter, persister, isoler, borner.

## Les maths, simplement

- Si le harnais garantit une fiabilité $r$ par étape (appel d'outil correctement formé, exécuté, interprété), la probabilité de mener à bien une tâche de $T$ étapes vaut $\approx r^{T}$.
- Passer $r$ de $0{,}90$ à $0{,}97$ sur une tâche de 20 étapes fait passer le taux de réussite de $\approx 12\ \%$ à $\approx 54\ \%$ — sans toucher au modèle.
- Intuition : la fiabilité par étape se **compose de façon multiplicative**. C'est pourquoi le travail d'ingénierie du harnais rapporte souvent plus qu'un changement de modèle.

## En pratique

- **Choisir le harnais avant le modèle** : il fixe le périmètre d'action, la sécurité et l'ergonomie ; le modèle reste interchangeable derrière.
- **Évaluer à harnais constant.** Changer les deux à la fois rend le résultat ininterprétable.
- Le contrat entre les deux couches tient à deux choses : le **tool calling** doit être réellement supporté et activé, et la **fenêtre de contexte** doit loger prompt système, schémas d'outils et historique de travail. Voir [[Pattern - Agent sur LLM auto-hébergé]] pour le détail opérationnel.
- Piège : imputer au modèle un échec qui vient du harnais (outil mal décrit, historique tronqué, erreur avalée sans retour) — et changer de modèle pour rien.

## Approches voisines & alternatives

- [[agent-loops]] — le **cœur d'exécution** du harnais ; cette page-ci décrit l'ensemble et ses frontières.
- [[Agent patterns]] — les façons d'organiser le harnais (ReAct, plan-execute, réflexion).
- [[Tool use patterns]] / [[tool-use]] — l'interface par laquelle le modèle agit.
- [[Context engineering]] — la part du harnais qui décide du contenu de la fenêtre.
- [[Agent skills]] — des procédures chargées par le harnais à la demande.
- [[Agent evaluation]] — mesurer le couple, et savoir à qui imputer l'échec.
- [[mcp-protocol]] — standardise la fourniture d'outils au harnais.
- Alternative : **appeler le modèle directement**, sans échafaudage — suffisant pour une tâche en un coup, incapable de la moindre action.
- Harnais fichés : [[Dev/Outils/pi|pi]] (boucle, TUI et API LLM unifiée), [[Dev/Outils/Maka|Maka]] (journal append-only de chaque décision), [[Dev/Outils/t3code|t3code]] (plan de contrôle au-dessus de plusieurs harnais).

## Pour aller plus loin

- Yao et al. (2022) — *ReAct* : le premier harnais minimal explicitement décrit.
- Anthropic (2024) — *Building Effective Agents* : plaide pour le harnais le plus simple qui fonctionne.
- Liés : [[Pattern - Agent sur LLM auto-hébergé]], [[Sandboxing de code généré]], [[Small Language Models]].
