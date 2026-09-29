---
role: brique
nom: Inspect AI
alias: [inspect-ai, inspect_ai, Inspect, UK AISI Inspect]
pitch: "Framework d'évaluation de LLM et d'agents (MIT, UK AI Security Institute et Meridian Labs) — des tâches composées d'un dataset, d'un solver et d'un scorer (texte ou noté par un modèle), 200+ évaluations prêtes à lancer, sandbox pour le code non fiable, visualiseur web et extension VS Code."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[DeepEval]]", "[[promptfoo]]"]
complements: []
tags: [llm, llm-eval, llm-as-judge, agents, benchmark]
url_docs: https://inspect.aisi.org.uk/
url_repo: https://github.com/UKGovernmentBEIS/inspect_ai
---

# Inspect AI

<!-- AUTO:BANDEAU:START -->
> Framework d'évaluation de LLM et d'agents (MIT, UK AI Security Institute et Meridian Labs) — des tâches composées d'un dataset, d'un solver et d'un scorer (texte ou noté par un modèle), 200+ évaluations prêtes à lancer, sandbox pour le code non fiable, visualiseur web et extension VS Code.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework Python d'évaluation de modèles de langage, créé par l'AI Security Institute
britannique et développé avec Meridian Labs. Une évaluation y est une **tâche** qui assemble
trois briques : un *dataset* d'échantillons (une entrée, une cible ou une consigne de
notation), un *solver* qui produit la réponse — un simple appel au modèle ou un agent
complet avec outils —, et un *scorer* qui la note. Les scorers fournis vont de la
correspondance de texte à la notation par un autre modèle (`model_graded_qa`,
`model_graded_fact`), c'est-à-dire du [[LLM-as-judge]]. Le cadre couvre aussi l'évaluation
d'agents, y compris des agents externes comme Claude Code ou Codex CLI, et exécute le code
généré par un modèle dans un *sandbox* (Docker, Kubernetes, Modal, Proxmox, Vagrant).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Évaluer des **agents** qui appellent des outils, avec du code non fiable isolé dans un sandbox | Traiter l'éval comme des assertions pytest dans la CI, avec un large catalogue de métriques → [[DeepEval]] |
| Lancer un des 200+ bancs d'essai déjà écrits sur n'importe quel modèle, sans les réimplémenter | Comparer prompts et modèles dans un fichier YAML déclaratif, avec du red-teaming → [[promptfoo]] |
| Écrire ses propres évaluations avec des briques réutilisables : datasets, solvers, scorers | Métriques propres au RAG (précision et rappel du contexte, fidélité) → [[Ragas]] |
| Rester sur du local : inférence HuggingFace, vLLM ou SGLang, visualiseur web et extension VS Code | Le versionnage est en 0.x et les versions se succèdent vite : épingler la version, sans quoi une mise à jour peut casser une évaluation |

## Mise en œuvre

- Installation — `uv add inspect-ai` ; la documentation indique `pip install inspect-ai`
- Point d'entrée — une tâche Python lancée par la commande `inspect eval <fichier.py> --model <fournisseur/modèle>`
- Prérequis — Python ≥ 3.10 ; l'accès à un modèle, soit le paquet du fournisseur et sa clé d'API, soit une inférence locale ; un moteur de conteneurs pour le sandbox
- Exécution — en local, mono-machine ; plus de 20 fournisseurs de modèles pris en charge
- Coût — gratuit, MIT ; le coût réel est en tokens du modèle évalué et, si un scorer noté par un modèle est utilisé, du modèle juge

## Écosystème

### Alternatives

- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Ressources

- Documentation — https://inspect.aisi.org.uk/
- Dépôt — https://github.com/UKGovernmentBEIS/inspect_ai

## Voir aussi

- [[LLM-as-judge]] — ce que font ses scorers notés par un modèle, avec leurs biais
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
