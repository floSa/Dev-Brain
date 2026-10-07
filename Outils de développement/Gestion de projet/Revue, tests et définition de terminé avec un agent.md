---
role: notion
nom: Revue, tests et définition de terminé avec un agent
alias: [definition of done, DoD, définition de terminé, revue de code d'agent, tests d'abord, test-first avec agent, vérification de code généré]
categorie: devtools/projet
domaines: [ai-eng, ml-eng, mlops]
tags: [project-management, testing, agents, code-assistant, git-hooks]
---

# Revue, tests et définition de terminé avec un agent

## Aperçu

- Un agent s'arrête quand le travail « a l'air terminé ». Sans critère exécutable, c'est le seul signal disponible, et l'humain devient la boucle de vérification.
- Une **définition de terminé** écrite avant la tâche, des **tests qui ne viennent pas du code qu'ils jugent** et une **revue humaine d'un diff de taille raisonnable** forment le garde-fou minimal.
- Le piège central : les tests écrits par l'agent *après* son code valident ce que le code fait, pas ce qu'il devait faire.

## Concepts clés

### Définition de terminé

Une liste courte, vérifiable par machine autant que possible, posée **avant** de lancer l'agent :

- les tests cités dans la spécification passent ;
- le linter, le formateur et le typage passent ([[Ruff]], [[mypy]]) ;
- aucun fichier hors périmètre modifié, aucune dépendance ajoutée sans accord ;
- la documentation et le changelog touchés par le changement sont à jour ;
- un humain a relu le diff.

La documentation de Claude Code donne la même consigne : donner à l'agent un contrôle qu'il peut exécuter (tests, build, linter, capture d'écran) et lui demander de montrer la sortie plutôt que d'affirmer le succès. Son verdict sur l'écart de confiance : « If you can't verify it, don't ship it. »

### Tests d'abord

Écrire (ou faire écrire, puis relire) les tests **avant** l'implémentation, depuis la spécification ([[Développement piloté par la spécification]]).

- Cas nominal, cas limites, au moins un échec attendu.
- Pour un bogue : un test qui échoue et reproduit le symptôme, puis la correction.
- [[pytest]] pour le socle ; [[Hypothesis]] pour énoncer des propriétés plutôt que des exemples, ce qui réduit la dépendance aux cas imaginés par l'agent ; [[testcontainers]] pour tester contre une vraie base ou un vrai broker plutôt que contre un faux écrit par l'agent.

### Le piège : l'agent teste son propre code

Quand le même modèle écrit le code puis les tests, un défaut du code se retrouve dans les tests, qui l'entérinent. Konstantinou, Tambon et Papadakis (juillet 2026) mesurent cette « propagation d'erreur » : des tests générés indépendamment détectent 25 % des fautes, contre 14 % pour des tests générés après un code fautif. Ce résultat porte sur leur protocole et leurs modèles ; il n'établit pas un taux universel, mais le mécanisme est plausible et facile à vérifier chez soi.

Les benchmarks d'agents en montrent un cousin : UTBoost (ACL 2025) trouve 36 instances de SWE-bench aux tests insuffisants et 345 correctifs faussement validés, ce qui change 18 classements sur la variante Lite. Un test qui passe est une preuve faible quand le test est faible.

Parades :

- **Tests depuis la spécification**, sans montrer l'implémentation à l'agent qui les écrit.
- **Deux sessions** : l'une écrit les tests, l'autre le code ; ou une session de relecture à contexte vierge, qui ne voit que le diff et les critères (pratique documentée par Anthropic).
- **Relire les tests en premier**, avant le code. S'ils sont faux, le reste ne vaut rien.
- Tester des **propriétés** ([[Hypothesis]]) et des cas **aberrants choisis par un humain**.
- Une suite qui ne détecte pas une faute injectée volontairement ne protège pas ; essayer.

### Revue de ce que l'agent a écrit

- **Taille du diff** : la relecture humaine perd en attention à mesure que le diff grossit (jugement, pas une mesure) ; viser des diffs qu'une personne lit en quelques minutes, et découper la tâche sinon. Le rapport DORA 2025 rattache l'écart entre vitesse individuelle et stabilité d'équipe au déplacement de la charge vers la revue et les tests ; l'instruction de découpage est une conséquence raisonnable, pas un chiffre du rapport.
- **Que chercher** : fichiers modifiés hors périmètre, tests affaiblis ou supprimés, exceptions avalées, dépendances nouvelles, secrets, valeurs codées en dur, API inventées.
- **Revue par un second agent** : utile en complément, jamais à la place. Un relecteur prié de trouver des défauts en trouve même sur un code sain ; il faut lui demander de ne signaler que ce qui touche la justesse ou les exigences.

## En pratique

- **Automatiser ce qui l'est** : [[pre-commit]] pour formatage, lint et typage avant chaque commit ; une CI identique en miroir ([[Forges & CI-CD]]). L'agent ne décide pas de passer outre : le hook refuse.
- **Un hook de fin de tour** ou une commande unique de vérification (`make check`, `uv run pytest && ruff check && mypy`) que l'agent connaît par son fichier de contexte ([[Fichiers de contexte pour agents]]).
- **Solo** : relire le diff soi-même reste obligatoire ; la discipline est de ne pas fusionner dans la minute.
- **On-prem ou ESN** : la définition de terminé s'aligne sur la recette contractuelle du client ; l'ajouter à la spécification évite que l'agent la découvre en fin de parcours. Tests d'intégration contre de vraies briques via [[testcontainers]] quand l'environnement cible est connu.
- **Pièges** : tests qui reproduisent l'implémentation ligne à ligne ; couverture élevée prise pour une preuve de justesse ; « tout est vert » après que l'agent a modifié le test rouge ; relecture rapide d'un gros diff par fatigue de revue.

## Approches voisines & alternatives

- [[Cycle de vie d'un projet assisté par agent]] — l'étape « vérifier » et la porte « terminé » dans le cycle.
- [[Vibe coding contre ingénierie agentique]] — l'absence de cette discipline, et les chiffres de risque.
- [[Développement piloté par la spécification]] — la source des tests et du critère de terminé.
- [[Boucle de Ralph]] — itérer jusqu'à ce qu'un critère passe ; ne vaut que si le critère est bon.
- [[Branches courtes et worktrees pour agents]] — de petites unités de changement, donc des diffs relisibles.
- [[Agent evaluation]] — évaluer l'agent lui-même (jeux de tâches, juges) ; ici, on vérifie un livrable, pas l'agent.
- [[pytest]], [[Hypothesis]], [[testcontainers]] — les trois niveaux de test cités.
- [[pre-commit]], [[Ruff]], [[mypy]] — les contrôles automatiques de la définition de terminé.
- [[Agent patterns]] — le patron « Reflexion / self-critique » (l'agent juge sa propre sortie) en est la version sans indépendance, donc la plus exposée au piège ci-dessus.

## Pour aller plus loin

- Anthropic (2025-2026) — *Best practices for Claude Code* : vérification exécutable, relecteur à contexte vierge, schéma auteur/relecteur, « trust-then-verify gap ». https://code.claude.com/docs/en/best-practices
- Konstantinou, Tambon, Papadakis (2026) — *On the risk of coding before testing: An empirical study on LLM-based test generation workflow*, arXiv 2607.05139. https://arxiv.org/abs/2607.05139
- Yu, Zhu, He, Kang (2025) — *UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench*, ACL 2025. https://arxiv.org/abs/2506.09289
- DORA / Google (2025) — *State of AI-assisted Software Development* (l'IA comme amplificateur ; chiffres détaillés non relus à la source). https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
- Willison (2025) — *Vibe engineering* : tests automatisés, CI, culture de la revue. https://simonwillison.net/2025/Oct/7/vibe-engineering/
