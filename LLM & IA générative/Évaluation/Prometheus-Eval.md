---
role: brique
nom: Prometheus-Eval
alias: [prometheus-eval, Prometheus 2, Prometheus2, M-Prometheus]
pitch: "Modèles-juges ouverts et bibliothèque Python (Apache-2.0) — Prometheus 2 en 7B et 8x7B note une réponse de 1 à 5 selon une rubrique ou choisit entre deux réponses, en local via vLLM ou par API via LiteLLM ; M-Prometheus (3B, 7B, 14B) pour le multilingue."
categorie: llm/eval
famille: modele
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[DeepEval]]"]
complements: []
tags: [llm, llm-eval, llm-as-judge, local-llm]
url_docs: https://github.com/prometheus-eval/prometheus-eval
url_repo: https://github.com/prometheus-eval/prometheus-eval
---

# Prometheus-Eval

<!-- AUTO:BANDEAU:START -->
> Modèles-juges ouverts et bibliothèque Python (Apache-2.0) — Prometheus 2 en 7B et 8x7B note une réponse de 1 à 5 selon une rubrique ou choisit entre deux réponses, en local via vLLM ou par API via LiteLLM ; M-Prometheus (3B, 7B, 14B) pour le multilingue.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Projet qui publie des **modèles entraînés pour juger** d'autres modèles, et la bibliothèque
`prometheus-eval` qui les pilote. Prometheus 2 existe en 7B et en 8x7B. Il note une réponse
de 1 à 5 selon une rubrique écrite par l'utilisateur, avec une réponse de référence
(notation absolue), ou désigne la meilleure de deux réponses (notation
relative), et renvoie un commentaire avec le verdict. Le dépôt ajoute Prometheus 2 BGB
(8x7B) et M-Prometheus (3B, 7B, 14B), tourné vers le multilingue. Le même code sait aussi
appeler un juge propriétaire comme GPT-4 par LiteLLM. Ces juges restent calibrés sur leurs
données d'entraînement : ils se valident sur un échantillon humain avant usage
(cf. [[LLM-as-judge]]).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Juger en local, sans envoyer les réponses à une API : la version 7B demande environ 16 Go de VRAM | Aucun GPU disponible : le juge passe par une API, et un cadre d'éval le fait déjà → [[DeepEval]], [[Ragas]] |
| Noter selon une rubrique sur mesure, ou départager deux réponses, avec un commentaire écrit | Il faut un cadre complet de tests en CI ou de banc d'essai, pas seulement un juge → [[Inspect AI]], [[promptfoo]] |
| Un juge figé et versionné, pour comparer des résultats dans le temps | Le projet est peu actif : dernière release en septembre 2024, dernier commit en avril 2025, bibliothèque annoncée en beta |
| Évaluer des textes non anglais (M-Prometheus) | Le 7B atteint au moins 80 % des performances du 8x7B, selon le dépôt : un juge de cette taille se valide sur un échantillon humain avant de s'y fier |

## Mise en œuvre

- Installation — `uv add prometheus-eval` ; la documentation indique `pip install prometheus-eval`, plus `vllm` pour l'inférence locale
- Point d'entrée — `PrometheusEval(model=...)`, puis `single_absolute_grade(...)` avec l'instruction, la réponse, la rubrique et une réponse de référence, qui renvoie un commentaire et une note ; notation relative en A ou B
- Prérequis — Python ≥ 3.10 ; poids téléchargés depuis HuggingFace ; ≈ 16 Go de VRAM pour le 7B
- Exécution — inférence locale sur GPU via vLLM, ou point d'accès distant (vLLM, TGI) ou API via LiteLLM
- Coût — gratuit ; dépôt et poids Prometheus 2 sous Apache-2.0 ; le coût réel est celui du GPU d'inférence

## Écosystème

### Alternatives

- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.

## Ressources

- Documentation — https://github.com/prometheus-eval/prometheus-eval
- Dépôt — https://github.com/prometheus-eval/prometheus-eval
- Papier — https://arxiv.org/abs/2405.01535 (Prometheus 2)

## Voir aussi

- [[LLM-as-judge]] — la notion parente : biais, juges spécialisés, calibration
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
