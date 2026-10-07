---
role: notion
nom: Vibe coding contre ingénierie agentique
alias: [vibe coding, agentic engineering, ingénierie agentique, vibe engineering]
categorie: devtools/projet
domaines: [ai-eng, ml-eng]
tags: [project-management, agents, code-assistant, code-generation]
---

# Vibe coding contre ingénierie agentique

## Aperçu

- **Vibe coding** : produire du logiciel par prompts en acceptant le code sans le lire. Terme lancé par Andrej Karpathy, février 2025, pour des projets jetables.
- **Ingénierie agentique** : piloter des agents de code avec la même exigence de qualité qu'un code écrit à la main — spécification, tests, relecture, responsabilité du résultat.
- La différence ne tient pas à l'outil mais à ce que l'humain **continue de comprendre et de vérifier**.

## Concepts clés

### L'origine : un message de février 2025

Le 2 février 2025, Karpathy écrit sur X : « There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. » Il décrit ensuite le geste : dicter à l'éditeur, « Accept All » sans lire les diffs, recopier les messages d'erreur sans commentaire, contourner un bogue que le modèle n'arrive pas à corriger. Et il borne lui-même l'usage : « It's not too bad for throwaway weekend projects. »

Le terme est parfois étendu à tout développement avec agent ; le message d'origine décrit un mode d'abandon du contrôle, pour des projets jetables.

### Le terme qui lui succède

Dans un message du 4 février 2026, Karpathy revient sur l'anniversaire. À l'époque, les modèles ne servaient qu'à des « throwaway projects, demos and explorations ». Désormais, programmer par agents devient « a default workflow for professionals, except with more oversight and scrutiny », et il propose **agentic engineering** : « agentic » parce qu'on n'écrit plus le code directement 99 % du temps mais qu'on orchestre des agents et supervise ; « engineering » pour souligner qu'il y a un art, une science et une expertise qui s'apprennent. Dès octobre 2025, Simon Willison avait proposé **vibe engineering** pour le même contraste : des professionnels qui utilisent les LLM tout en restant responsables d'un code maintenable.

### Ce que disent les mesures

- **Productivité** : METR (juillet 2025), essai randomisé : 16 développeurs expérimentés de gros dépôts open source, 246 tâches. Avec les outils d'IA, les tâches ont pris **19 % de temps en plus**, alors que les développeurs prévoyaient un gain de 24 % et croyaient, après coup, avoir gagné 20 %. Limites écrites par les auteurs : échantillon réduit, un moment précis des outils, aucune prétention à représenter la plupart des développeurs ni à exclure de meilleurs usages. Résultat à ne pas généraliser, mais l'écart entre perception et mesure est le point à retenir.
- **Sécurité** : Veracode (juillet 2025), rapport d'éditeur : 80 tâches, plus de 100 modèles, analyse statique ; le code produit contient une faille de la liste OWASP Top 10 dans 45 % des cas, avec 38 à 45 % d'échecs en Python et plus de 70 % en Java. Les modèles plus gros ne font pas significativement mieux. Rapport d'un vendeur d'outils de sécurité, à lire comme un ordre de grandeur. Plus ancien, plus rigoureux sur le plan académique : Pearce et al. (2021) trouvent environ 40 % de programmes vulnérables sur 1 689 générés par Copilot, sur des scénarios CWE choisis ; l'outil testé a changé depuis.
- **Équipe** : le rapport DORA 2025 (près de 5 000 répondants) conclut que l'IA est un **amplificateur** : elle magnifie les forces des organisations performantes et les dysfonctionnements des autres.

## En pratique

### Quand reprendre la main : signaux concrets

- L'agent corrige un bogue en en créant un autre, ou propose « de contourner » plutôt que de comprendre la cause.
- Le diff n'est plus relisible en quelques minutes ; plus personne ne sait expliquer ce qu'il fait.
- Les mêmes corrections sont redites plus de deux fois dans la session (contexte pollué : repartir d'une session vierge avec un meilleur énoncé).
- Les tests passent mais l'agent a modifié les tests ou les a écrits après le code ([[Revue, tests et définition de terminé avec un agent]]).
- Le code touche à des secrets, de l'authentification, des droits, une base de production, un automate.
- Une dépendance ou une API apparaît sans que personne l'ait choisie.

### Contexte on-prem industriel ou ESN

- Le vibe coding reste légitime pour un prototype jetable, un script d'exploration de données, une maquette de tableau de bord jetée après la démo.
- Il ne l'est pas pour du code qui tournera chez un client, près d'un procédé ou sur un réseau isolé : maintenance sur plusieurs années par d'autres équipes, recette formelle, audit de sécurité, parfois responsabilité contractuelle.
- Contraintes fréquentes : pas d'accès à un service d'agent en ligne, d'où des agents pilotés par des modèles locaux ([[OpenCode]], [[Aider]], [[Cline]]), moins capables, donc des portes plus rapprochées.
- Les dépendances ajoutées par un agent passent par la revue de licences et de sécurité du client comme les autres.

### Ce qu'on garde de l'ingénierie classique

Willison liste les pratiques que les LLM « récompensent » : tests automatisés, plan préalable, documentation, bon usage de git, CI et lint, culture de la revue, QA manuelle. Aucune n'est nouvelle. Voir [[Cycle de vie d'un projet assisté par agent]] pour leur place dans le cycle.

## Approches voisines & alternatives

- [[Cycle de vie d'un projet assisté par agent]] — le cadre dans lequel l'ingénierie agentique place ses portes de décision.
- [[Revue, tests et définition de terminé avec un agent]] — la vérification, le contrepoids direct du vibe coding.
- [[Développement piloté par la spécification]] — la réponse méthodologique : spécifier d'abord ([[Spec Kit]], [[BMAD]]).
- [[Fichiers de contexte pour agents]] — encoder les conventions pour que l'agent n'improvise pas.
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — savoir si l'agent fait réellement gagner du temps.
- [[Prompt engineering]] et [[Context engineering]] — la compétence centrale côté agent.
- [[Agent patterns]] — les boucles dans lesquelles l'agent travaille.
- Alternative : **ne pas utiliser d'agent** sur le code critique ; choix légitime, à comparer avec la mesure plutôt qu'avec une impression.

## Pour aller plus loin

- Karpathy (2 février 2025) — message d'origine sur X, texte vérifié via https://x.com/karpathy/status/1886192184808149383 (page X fermée au robot ; texte lu par l'API de miroir fxtwitter).
- Karpathy (4 février 2026) — rétrospective et proposition « agentic engineering » : https://x.com/karpathy/status/2019137879310836075 (même remarque pour la lecture).
- Willison (7 octobre 2025) — *Vibe engineering* : https://simonwillison.net/2025/Oct/7/vibe-engineering/
- Becker, Rush, Barnes, Rein, METR (10 juillet 2025) — *Early-2025 AI experienced OS dev study* : https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Veracode (30 juillet 2025) — *2025 GenAI Code Security Report* (communiqué) : https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- Pearce, Ahmad, Tan, Dolan-Gavitt, Karri (2021) — *Asleep at the Keyboard?* : https://arxiv.org/abs/2108.09293
- DORA / Google (2025) — *State of AI-assisted Software Development* : https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
