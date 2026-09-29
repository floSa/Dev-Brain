---
role: brique
nom: RAGChecker
alias: [ragchecker, RAG Checker, ragchecker-amazon]
pitch: "Framework de diagnostic de RAG (Apache-2.0, Amazon Science) — extrait des claims de la réponse et les vérifie par entailment pour séparer les fautes du retriever (claim recall, context precision) de celles du générateur (fidélité, hallucination, sensibilité au bruit) ; juges via LiteLLM."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[ARES]]"]
complements: []
tags: [llm, llm-eval, rag-eval, llm-as-judge, rag]
url_docs: https://github.com/amazon-science/RAGChecker
url_repo: https://github.com/amazon-science/RAGChecker
---

# RAGChecker

<!-- AUTO:BANDEAU:START -->
> Framework de diagnostic de RAG (Apache-2.0, Amazon Science) — extrait des claims de la réponse et les vérifie par entailment pour séparer les fautes du retriever (claim recall, context precision) de celles du générateur (fidélité, hallucination, sensibilité au bruit) ; juges via LiteLLM.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de **diagnostic** de systèmes [[RAG]], décrit dans *RAGChecker: A Fine-grained
Framework for Diagnosing Retrieval-Augmented Generation* (Ru et al., 2024, arXiv:2408.08067 ;
présenté à la piste Datasets & Benchmarks de NeurIPS 2024). Un modèle extrait les **claims**
de la réponse générée et de la réponse de référence, un second vérifie chacun par
**entailment** contre le contexte récupéré. Les métriques en tombent à trois niveaux :
globales (précision, rappel, F1), du **retriever** (claim recall, context precision) et du
**générateur** (context utilization, sensibilité au bruit relevant et irrelevant,
hallucination, self-knowledge, fidélité). L'objet est d'**attribuer** une erreur à un étage,
pas seulement de noter la réponse. Les auteurs annoncent, dans l'abstract, de meilleures
corrélations avec les jugements humains que les autres métriques. Le dépôt a publié en
décembre 2024 un jeu de référence de 4 000 questions sur 10 domaines, et propose une
intégration à [[LlamaIndex]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Savoir si la faute vient du **retriever** ou du **générateur** avant de toucher au pipeline : [[Reranking]], [[Chunking strategies]], prompt | Un score global rapide, sans référence, pour une boucle de dev → [[Ragas]] |
| Un diagnostic **au niveau claim** : ce que la réponse affirme sans que le contexte le soutienne, et ce que le contexte contenait sans que la réponse le reprenne | Pas de **réponse de référence** : la seule annotation requise par requête est la réponse attendue (`gt_answer`), donc un golden set est nécessaire |
| Comparer deux configurations de RAG métrique par métrique, pas sur un chiffre agrégé | Des intervalles de confiance statistiques sont exigés → [[ARES]] |
| Faire tourner l'extraction et la vérification sur un modèle au choix : tout modèle compatible LiteLLM | Une brique suivie de près : dernière release PyPI (0.1.9) en septembre 2024, dernier commit du dépôt en décembre 2024 |

## Mise en œuvre

- Installation — `uv add ragchecker`
- Point d'entrée — un jeu de questions, réponses de référence, réponses générées et contextes récupérés en entrée ; l'extracteur puis le vérificateur de claims produisent les métriques
- Prérequis — un modèle pour l'extraction de claims et la vérification, joignable par LiteLLM ; le dépôt donne en exemple Llama 3.1 70B sur AWS Bedrock
- Exécution — mono-nœud ; les appels au modèle juge sont la charge dominante
- Coût — gratuit sous Apache-2.0 ; le coût réel est en tokens du modèle extracteur et vérificateur, sur chaque claim de chaque réponse

## Écosystème

### Alternatives

- [[ARES]] — Framework d'évaluation de RAG (Apache-2.0, Stanford) — génère des données synthétiques, affine de petits juges LM pour la pertinence du contexte, la fidélité et la pertinence de la réponse, puis corrige leurs scores par prediction-powered inference avec quelques centaines d'annotations humaines ; NAACL 2024.

voisin : [[Ragas]] — métriques sans référence par LLM généraliste, plus rapide à démarrer, moins fin pour attribuer une faute ; [[DeepEval]] et [[TruLens]] — même famille de métriques RAG, à l'échelle de la réponse plutôt que du claim.

## Ressources

- Documentation — https://github.com/amazon-science/RAGChecker
- Dépôt — https://github.com/amazon-science/RAGChecker
- Article — https://arxiv.org/abs/2408.08067

## Voir aussi

- [[RAG eval]] — la notion qu'il met en œuvre
- [[LLM-as-judge]] — le mécanisme : un modèle extrait et vérifie les claims
- [[Ranking metrics]] — les métriques d'ordre du retriever, quand un golden set de passages existe
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
