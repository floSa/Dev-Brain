---
role: brique
nom: seqeval
alias: [seq eval]
pitch: "Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger."
categorie: ml/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[evaluate]]"]
tags: [ner, sequence-labeling, model-evaluation, nlp]
url_docs: https://github.com/chakki-works/seqeval
url_repo: https://github.com/chakki-works/seqeval
---

# seqeval

<!-- AUTO:BANDEAU:START -->
> Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Le calcul des métriques d'[[NER et étiquetage de séquence|étiquetage de séquence]] **au niveau entité**. Là où `sklearn` score token par token — et surévalue —, seqeval ne compte une entité juste que si son span exact, frontières et type, est correct : c'est la métrique qui reflète la qualité réelle d'un tagger, et le standard des papiers CoNLL. Il reconnaît les schémas IOB1, IOB2, IOE1, IOE2, IOBES et BILOU, et propose un mode `strict` compatible avec l'évaluateur historique `conlleval`. Son API est calquée sur scikit-learn (`f1_score`, `precision_score`, `recall_score`, `classification_report`), ce qui masque deux exigences de format : il attend des **listes de listes** — une séquence de labels par phrase —, une liste plate faussant silencieusement le découpage en entités ; et les labels doivent suivre un schéma cohérent, un `I-` orphelin ou un préfixe inattendu étant réinterprété sans avertir.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Évaluer un modèle de NER ou de chunking en F1 au niveau entité | Métriques au **niveau token**, ou tâches de classification non séquentielles : `sklearn.metrics` suffit → [[Scikit-Learn]] |
| Obtenir un rapport par type d'entité : précision, rappel et F1 par classe (`classification_report`) | Jeu de métriques génériques et versionnées — BLEU, ROUGE, accuracy → [[evaluate]], qui d'ailleurs embarque seqeval pour sa métrique `seqeval` |
| Brique d'évaluation dans une boucle d'entraînement de token classification | |

## Mise en œuvre

- Installation — `uv add seqeval` ; dernière release 1.2.2 (oct. 2020), stable et toujours la référence, mais sans évolution à attendre
- Point d'entrée — import Python, API calquée sur `sklearn.metrics` ; fixer `mode='strict'` et `scheme=IOB2` pour des scores reproductibles et comparables à conlleval, le mode par défaut traitant les transitions de schéma autrement
- Prérequis — NumPy et scikit-learn
- Exécution — single-node, en mémoire, sur des listes de listes de labels
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- Pas de substitut direct dans le brain : c'est la bibliothèque de référence des métriques d'étiquetage de séquence. Pour le niveau token, `sklearn.metrics` ; pour des métriques génériques, l'enveloppe HuggingFace qui la charge.

### Compléments

- [[evaluate]] — Bibliothèque HuggingFace de métriques d'évaluation ML prêtes à l'emploi — accuracy, F1, BLEU, ROUGE, exact match… chargées depuis le Hub via une API unique load/compute, comparables d'un projet à l'autre. — l'enveloppe qui charge seqeval comme métrique.

## Ressources

- Documentation — https://github.com/chakki-works/seqeval
- Dépôt — https://github.com/chakki-works/seqeval

## Voir aussi

- [[Évaluation de modèles]] — le hub du domaine
- [[NER et étiquetage de séquence]] — le concept dont seqeval calcule les métriques
- [[Classification metrics]] — les concepts derrière precision, recall et F1
