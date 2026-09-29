---
role: brique
nom: ARES
alias: [ares, ares-ai, Automated RAG Evaluation System]
pitch: "Framework d'évaluation de RAG (Apache-2.0, Stanford) — génère des données synthétiques, affine de petits juges LM pour la pertinence du contexte, la fidélité et la pertinence de la réponse, puis corrige leurs scores par prediction-powered inference avec quelques centaines d'annotations humaines ; NAACL 2024."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[RAGChecker]]"]
complements: []
tags: [llm, llm-eval, rag-eval, llm-as-judge, rag]
url_docs: https://github.com/stanford-futuredata/ARES
url_repo: https://github.com/stanford-futuredata/ARES
---

# ARES

<!-- AUTO:BANDEAU:START -->
> Framework d'évaluation de RAG (Apache-2.0, Stanford) — génère des données synthétiques, affine de petits juges LM pour la pertinence du contexte, la fidélité et la pertinence de la réponse, puis corrige leurs scores par prediction-powered inference avec quelques centaines d'annotations humaines ; NAACL 2024.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'évaluation de systèmes [[RAG]] présenté dans *ARES: An Automated Evaluation
Framework for Retrieval-Augmented Generation Systems* (Saad-Falcon, Khattab, Potts,
Zaharia, NAACL 2024, arXiv:2311.09476). Là où [[Ragas]] fait juger chaque réponse par un LLM
généraliste, ARES **entraîne** ses juges : il génère des requêtes synthétiques à partir des
documents, affine de **petits modèles de langue** pour noter trois axes — pertinence du
contexte, fidélité de la réponse, pertinence de la réponse — puis applique la **prediction-
powered inference (PPI)** : un petit lot d'annotations humaines corrige le biais des juges et
donne un **intervalle de confiance** sur le score. Le papier annonce qu'il suffit de « quelques
centaines » d'annotations humaines à l'évaluation ; le README demande au moins 50 exemples annotés, plusieurs centaines idéalement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un score RAG avec un **intervalle de confiance** statistique, pas un chiffre isolé | Aucune annotation humaine disponible, aucun moyen d'en produire : le calibrage exige au moins 50 exemples annotés, plusieurs centaines idéalement → [[Ragas]], sans référence |
| Évaluer un **domaine spécialisé** où un juge généraliste est peu fiable : les juges sont affinés sur le corpus | Une boucle de dev rapide : entraîner des juges avant de mesurer est plus lourd qu'un appel de métrique → [[DeepEval]] |
| Comparer des systèmes RAG sur les mêmes trois axes, avec la robustesse annoncée face aux changements de domaine | Diagnostiquer **où** ça casse, retriever ou générateur, claim par claim → [[RAGChecker]] |
| Rester **hors ligne** : le README indique un fonctionnement par API OpenAI ou en local via vLLM | Besoin d'une brique maintenue activement : dernière release PyPI en juillet 2024, dernier commit du dépôt en mars 2025 |

## Mise en œuvre

- Installation — `uv add ares-ai`
- Point d'entrée — un jeu de requêtes, passages et réponses du système évalué, plus un petit lot annoté à la main ; le framework génère les données synthétiques, affine les juges puis calcule scores et intervalles par PPI
- Prérequis — un jeu de validation annoté à la main (au moins 50 triplets requête-document-réponse, plusieurs centaines idéalement) ; les besoins matériels de l'affinage ne sont pas chiffrés dans le README
- Exécution — mono-nœud ; modèles via API OpenAI ou en local par vLLM
- Coût — gratuit sous Apache-2.0 ; le coût réel est l'annotation humaine, l'affinage des juges et les tokens de génération synthétique

## Écosystème

### Alternatives

- [[RAGChecker]] — Framework de diagnostic de RAG (Apache-2.0, Amazon Science) — extrait des claims de la réponse et les vérifie par entailment pour séparer les fautes du retriever (claim recall, context precision) de celles du générateur (fidélité, hallucination, sensibilité au bruit) ; juges via LiteLLM.

voisin : [[Ragas]] — l'approche sans référence par LLM généraliste, quand ARES entraîne ses juges et exige des annotations ; [[DeepEval]] et [[TruLens]] — même famille de métriques RAG, sans calibrage statistique.

## Ressources

- Documentation — https://github.com/stanford-futuredata/ARES
- Dépôt — https://github.com/stanford-futuredata/ARES
- Article — https://arxiv.org/abs/2311.09476

## Voir aussi

- [[RAG eval]] — la notion qu'il met en œuvre
- [[LLM-as-judge]] — le mécanisme, ici avec des juges affinés
- [[LLM eval metrics]] — la notion du dossier
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
