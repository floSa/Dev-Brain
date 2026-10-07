---
role: brique
nom: PR-Agent
alias: [pr-agent, The-PR-Agent/pr-agent, qodo-ai/pr-agent, Qodo Merge open source]
pitch: "Outil de revue automatique de pull requests (MIT, Python), auto-hébergeable : commandes /describe, /review, /improve et /ask, en GitHub Action, en ligne de commande, en conteneur ou en webhook, pour GitHub, GitLab, Bitbucket, Azure DevOps et Gitea — mais le modèle est à fournir (clé d'API ou modèle local par LiteLLM), et le projet est un héritage de Qodo tenu par la communauté, distinct de l'offre commerciale de Qodo."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: beta
langage: Python
alternatives: []
complements: []
tags: [code-review, llm, self-hosted]
url_docs: https://docs.pr-agent.ai/
url_repo: https://github.com/The-PR-Agent/pr-agent
---

# PR-Agent

<!-- AUTO:BANDEAU:START -->
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de revue de code qui lit une pull request et répond par des commentaires, avec un seul appel de modèle par commande : `/describe` rédige la description, `/review` relit le changement, `/improve` propose des corrections, `/ask` répond à une question sur le diff. Il se lance en GitHub Action (voie recommandée par le README), en ligne de commande (`pip install "pr-agent[github]"` puis `pr-agent --pr_url <url> review`), en conteneur Docker ou en webhook, pour GitHub, GitLab, Bitbucket, Azure DevOps et Gitea. Le modèle est celui qu'on lui donne : OpenAI, Anthropic, Gemini, DeepSeek, Mistral et tout fournisseur joignable par LiteLLM, dont Ollama. Les grandes pull requests passent par une stratégie de compression du diff. Licence MIT lue dans le dépôt ; version 0.47.0 du 2026-10-02, dépôt poussé le 2026-10-07.

**D'où il vient.** PR-Agent a été écrit par Qodo. D'après le README, Qodo l'a donné à la communauté : le dépôt est passé de `qodo-ai/pr-agent` à `The-PR-Agent/pr-agent`, la documentation à `docs.pr-agent.ai`, et il cherche une fondation d'accueil. Il n'est **pas** l'offre commerciale de Qodo (le service hébergé « Qodo Merge » est devenu Qodo, une plateforme de revue propriétaire), que ce brain ne fiche pas (règle 15). Le nom d'organisation et l'espace Docker Hub ont changé : les images depuis la 0.34.2 sont sous `pragent/pr-agent`, et l'ancien `codiumai/pr-agent` est figé à la v0.31.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une première relecture automatique des pull requests d'une petite équipe ou d'un projet solo, avant la revue humaine (cf. [[Revue, tests et définition de terminé avec un agent]]) | Un remplaçant de la revue humaine : l'outil lit un diff avec un appel de modèle, sans exécuter le code ni les tests |
| Un modèle local par [[Ollama]] via LiteLLM, pour que le diff ne quitte pas le réseau interne | Une forge qui n'est pas dans la liste : le README donne GitHub, GitLab, Bitbucket, Azure DevOps et Gitea ; ce brain n'a pas vérifié [[Forgejo]], dérivé de Gitea |
| Des invites personnalisables par fichier de configuration (`configuration.toml`) pour les catégories de revue | La commande `/help_docs` : désactivée depuis la v0.36.1, le temps de corriger une exposition d'identifiants (issue 2445 du dépôt) |
| Le lancer en CI sur le poste ou en conteneur, sur n'importe quelle forge prise en charge | Un projet qui doit sa continuité à un éditeur : le dépôt est tenu par la communauté, avec un premier mainteneur externe |

## Mise en œuvre

- Installation — GitHub Action (`uses: the-pr-agent/pr-agent@main`, avec `OPENAI_KEY` et `GITHUB_TOKEN`), ou `pip install "pr-agent[github]"` (extras par forge, `pr-agent[all]` pour toutes), ou l'image `pragent/pr-agent`
- Point d'entrée — `pr-agent --pr_url <url de la pull request> review` en local ; en CI, les événements `pull_request` ouverts ou mis à jour
- Prérequis — un modèle joignable : clé d'API d'un fournisseur ou serveur local par LiteLLM ; un jeton de la forge
- Exécution — action de CI, conteneur ou webhook auto-hébergé ; avec une clé OpenAI, la confidentialité du diff est celle d'OpenAI (le README renvoie à sa politique)
- Coût — gratuit sous licence MIT ; la dépense est celle du modèle, nulle en local

## Écosystème

### Alternatives

- voisin : [[Ollama]] — le serveur de modèles locaux que PR-Agent atteint par LiteLLM ; il garde le diff sur le réseau interne.
- voisin : Kodus — autre revue de code par IA, cité en texte simple, non fiché dans le brain. Les offres propriétaires de revue, dont Qodo, sont hors du périmètre (règle 15).

## Ressources

- Documentation — https://docs.pr-agent.ai/
- Dépôt — https://github.com/The-PR-Agent/pr-agent

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Revue, tests et définition de terminé avec un agent]] — ce que la revue d'un agent doit établir avant « terminé »
- [[pre-commit]] — les contrôles avant le commit, en amont de la revue de pull request
- [[Outils de développement]] — le hub du domaine
