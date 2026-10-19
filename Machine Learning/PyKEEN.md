---
role: brique
nom: PyKEEN
alias: [pykeen, PyKEEN 1.0, knowledge graph embeddings library]
pitch: "Bibliothèque Python (MIT) pour entraîner et comparer des plongements de graphes de connaissances — 40 modèles dont TransE et RotatE, 37 jeux de données, optimisation d'hyperparamètres avec Optuna ; dernière release en avril 2025."
categorie: ml/graphe
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [link-prediction, knowledge-graph, embeddings]
url_docs: https://pykeen.readthedocs.io/
url_repo: https://github.com/pykeen/pykeen
---

# PyKEEN

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python (MIT) pour entraîner et comparer des plongements de graphes de connaissances — 40 modèles dont TransE et RotatE, 37 jeux de données, optimisation d'hyperparamètres avec Optuna ; dernière release en avril 2025.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python pour **entraîner et évaluer des plongements de graphes de connaissances** : à partir de triplets (tête, relation, queue), elle apprend un vecteur par entité et par relation, puis classe les faits manquants les plus plausibles (prédiction de liens). Le README annonce 40 modèles (dont TransE et RotatE), 37 jeux de données et 5 jeux inductifs, 15 fonctions de perte, 5 évaluateurs et 40 métriques, et 8 outils de suivi d'expériences (TensorBoard, MLflow, Weights & Biases). La fonction `pipeline()` entraîne et évalue un modèle désigné par son nom ; l'optimisation d'hyperparamètres passe par Optuna. L'article de référence est Ali et al., *PyKEEN 1.0*, JMLR 22, 2021. Relevé le 2026-10-19 : version **1.11.1** (2025-04-24) sur PyPI, mais un dépôt actif (dernier push le 2026-10-18), licence MIT, environ 2 000 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Compléter un graphe de connaissances ou classer des candidats pour une requête `(tête, relation, ?)` | Des attributs numériques ou textuels qui comptent : un réseau de neurones sur graphe ([[PyTorch Geometric]]) ou un modèle de langage s'y prête mieux |
| Comparer plusieurs modèles de la famille TransE sur ses propres données, avec un protocole d'évaluation commun | Une justification des propositions : un plongement donne un score, pas une raison |
| Reproduire ou étendre des résultats publiés : la bibliothèque sert de référence de comparaison | Un graphe sans relations variées ou très petit : peu de signal à apprendre |
| Brancher le suivi d'expériences (MLflow, Weights & Biases, TensorBoard) sur l'entraînement | Une version de Python ancienne : le README annonce Python 3.11 ou plus (PyPI : 3.10 ou plus) |

## Mise en œuvre

- Installation — `uv add pykeen`
- Point d'entrée — `pykeen.pipeline.pipeline(model="TransE", dataset="Nations")`, qui rend un résultat avec le modèle entraîné et son évaluation
- Prérequis — Python 3.11 ou plus d'après le README (PyPI déclare 3.10 ou plus) ; un GPU facultatif : `pykeen.env()` rapporte les informations CUDA
- Exécution — en bibliothèque, rien à héberger
- Coût — gratuit, MIT

## Limites à connaître

- **Les scores des articles ne se transposent pas tels quels.** Voir la notion : le résultat dépend de l'ensemble architecture, perte, entraînement et traitement des relations inverses, et l'évaluation agrégée peut surestimer la performance. Mesurer sur son propre graphe, contre une base simple.
- **Dernière release datée d'avril 2025**, tandis que le dépôt reçoit des commits : les correctifs récents sont sur la branche de développement. Épingler la version publiée ou un commit.
- **Entités inconnues.** Un composant ajouté après l'entraînement n'a pas de vecteur ; il faut réentraîner ou prévoir une stratégie pour les entités nouvelles.

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucune autre brique du brain n'entraîne de plongements de graphes de connaissances.
- [[PyTorch Geometric]] — voisin : la bibliothèque de réseaux de neurones sur graphes, quand les attributs des nœuds comptent autant que les relations.

## Ressources

- Documentation — https://pykeen.readthedocs.io/
- Dépôt — https://github.com/pykeen/pykeen

## Voir aussi

- [[Plongements de graphe et prédiction de liens]] — la notion : TransE et sa famille, évaluation, pièges
- [[Graphe de connaissances]] — la page d'entrée du sujet
- [[Ontologies et RDF]] — le hub du sous-domaine RDF, où le graphe se construit et se valide
