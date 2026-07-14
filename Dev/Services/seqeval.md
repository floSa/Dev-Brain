---
galaxie: dev
type: service
nom: seqeval
alias: [seq eval]
pitch: "Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger."
categorie: ml/eval
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [ner, sequence-labeling, model-evaluation, nlp]
url_docs: https://github.com/chakki-works/seqeval
url_repo: https://github.com/chakki-works/seqeval
---

# seqeval

## Pourquoi

Bibliothèque dédiée au calcul des métriques d'[[NER et étiquetage de séquence|étiquetage de séquence]]. Là où `sklearn` score **token par token** (et surévalue), seqeval score **au niveau entité** : une entité ne compte juste que si son span exact (frontières + type) est correct — la métrique qui reflète vraiment la qualité d'un tagger NER. Reconnaît les schémas IOB1/IOB2, IOE1/IOE2, IOBES et BILOU, et propose un mode `strict` compatible avec l'évaluateur historique `conlleval`. API calquée sur scikit-learn : `f1_score`, `precision_score`, `recall_score`, `classification_report`.

## Quand l'utiliser

- Évaluer un modèle de **NER** ou de chunking en **F1 au niveau entité** (le standard des papiers CoNLL).
- Obtenir un **rapport par type d'entité** (`classification_report`) — précision/rappel/F1 par classe.
- Brique d'évaluation dans une boucle d'entraînement de token classification ([[Dev/Services/HuggingFace|HuggingFace]] `Trainer`).

## Quand NE PAS l'utiliser

- Métriques au **niveau token** ou tâches de classification non séquentielles → `sklearn.metrics` ([[Dev/Services/Scikit-Learn|Scikit-Learn]]) suffit.
- Jeu de métriques **génériques et versionnées** (BLEU, ROUGE, accuracy) → [[Dev/Services/evaluate|evaluate]], qui d'ailleurs **embarque seqeval** pour sa métrique `seqeval`.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add seqeval`. Dépend de NumPy et scikit-learn.
- **Single-node**, calcul en mémoire sur des listes de listes de labels.

## Pièges

- **Peu maintenu** : dernière release 1.2.2 (oct. 2020). Stable et toujours la référence, mais ne pas attendre d'évolutions.
- Attend des **listes de listes** (une séquence de labels par phrase) ; passer une liste plate fausse le découpage en entités.
- Le **mode par défaut** diffère du mode `strict` (gestion des transitions de schéma) : fixer `mode='strict'` + `scheme=IOB2` pour des scores reproductibles et comparables à conlleval.
- Les labels doivent suivre un schéma cohérent ; un `I-` orphelin ou un préfixe inattendu est silencieusement réinterprété.

## Alternatives

Pas de substitut direct dans le brain : c'est la bibliothèque de référence pour les métriques d'étiquetage de séquence. Pour des métriques génériques, voir [[Dev/Services/evaluate|evaluate]] (qui l'enveloppe) ; pour le niveau token, `sklearn.metrics`.

## Liens

- [[NER et étiquetage de séquence]] — le concept dont seqeval calcule les métriques.
- [[Dev/Services/evaluate|evaluate]] — l'enveloppe HuggingFace qui charge seqeval comme métrique.
- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — `sklearn.metrics` pour le niveau token / la classification classique.
- [[Classification metrics]] — les concepts derrière precision / recall / F1.
- Repo : https://github.com/chakki-works/seqeval
