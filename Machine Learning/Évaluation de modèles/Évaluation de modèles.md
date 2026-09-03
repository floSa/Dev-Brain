---
role: hub
nom: Évaluation de modèles
alias: [évaluation ML, mesure de performance]
pitch: Obtenir un chiffre honnête, puis choisir celui qui décrit vraiment le coût des erreurs — le protocole avant la métrique.
domaines: [data-sci, ml-eng]
tags: [model-evaluation, classification, regression, ranking, calibration, resampling]
---

# Évaluation de modèles

> Obtenir un chiffre honnête, puis choisir celui qui décrit vraiment le coût des erreurs — le protocole avant la métrique.

## Ce qu'il faut comprendre

- **Ce dossier range l'endroit où la plupart des projets échouent**, et il échoue rarement sur l'algorithme. Un modèle qui affiche 0,97 en validation et déçoit en production n'a pas un problème de modèle : il a un problème de mesure. Deux questions se posent dans cet ordre, et l'inverser est la faute la plus commune — *ce chiffre est-il honnête ?* puis seulement *ce chiffre décrit-il ce qui m'intéresse ?*
- **Le protocole vient avant la métrique.** [[Compromis biais-variance]] dit pourquoi une erreur d'entraînement basse ne prouve rien ; [[Validation croisée]] est le protocole qui donne un chiffre stable sans gaspiller de données ; [[Data leakage]] est la façon la plus courante de le rendre faux sans s'en apercevoir, et elle laisse une signature reconnaissable — des performances trop belles pour être vraies. Une métrique parfaite calculée sur un protocole qui fuit ne vaut rien.
- **Choisir la métrique est un acte métier, pas un choix technique** : elle encode le coût relatif des erreurs, et ce coût n'est pas dans les données. [[Classification metrics]] pour une décision à seuil fixé, [[Regression metrics]] pour une cible continue — quadratique ou absolu selon qu'on veut ou non punir les gros écarts —, [[Ranking metrics]] quand seul l'ordre compte, ce qui est le cas de la recherche, de la recommandation et du retriever d'un RAG.
- **Une courbe dit ce qu'une métrique à seuil ne peut pas dire.** [[ROC-AUC & courbe PR]] évalue sur tous les seuils à la fois, et la seconde courbe est la bonne dès que le positif est rare — l'AUC-ROC reste flatteuse là où la précision-rappel s'effondre.
- **Ordonner et chiffrer ne sont pas la même compétence** : un modèle peut très bien classer et produire des probabilités fausses. [[Calibration]] est la vérification à faire dès qu'un score devient une décision chiffrée — un seuil, un coût, une priorisation. C'est le contrôle le plus souvent omis du dossier.
- **Le déséquilibre des classes casse les métriques avant de casser les modèles** : [[Imbalanced classification]], rangé dans [[Tabulaire]] parce que son traitement est un travail de pipeline, pose le problème que ce dossier mesure.
- **Ce dossier mesure un modèle donné ; il ne le borne pas a priori.** C'est la frontière avec [[Théorie de l'apprentissage]], qui répond à « de quoi la généralisation dépend-elle » avec des bornes trop lâches pour dimensionner quoi que ce soit. Et il ne mesure pas non plus une *application* LLM, qui relève de [[Évaluation]] dans [[LLM & IA générative]] — juger une réponse par un juge n'a rien à voir avec compter des vrais positifs.

## Choisir

- Un score de validation qu'on soupçonne trop beau → [[Data leakage]] d'abord, [[Validation croisée]] ensuite.
- Un protocole d'estimation qui ne gaspille pas les données → [[Validation croisée]] ; sur une série indexée par le temps, [[Walk-forward CV]] à la place.
- Un classifieur à seuil fixé, à comparer à une vérité terrain → [[Classification metrics]].
- Le même classifieur sans figer de seuil, ou avec un positif rare → [[ROC-AUC & courbe PR]].
- Une cible continue → [[Regression metrics]].
- Un système qui produit un ordre plutôt qu'une valeur → [[Ranking metrics]].
- Un score qu'on va transformer en euros, en priorité ou en alerte → [[Calibration]].
- Calculer une métrique standard sans la réimplémenter → [[evaluate]] ; scorer un étiquetage de séquence au niveau entité → [[seqeval]].
- Comparer des centaines de configurations plutôt qu'une → [[Optimisation d'hyperparamètres]] et [[Suivi d'expériences]].

<!-- AUTO:START -->
### Notions
- [[Calibration]] — domaines : data-sci, ml-eng
- [[Classification metrics]] — domaines : data-sci, ml-eng
- [[Compromis biais-variance]] — domaines : data-sci, ml-eng
- [[Data leakage]] — domaines : data-sci, ml-eng
- [[Ranking metrics]] — domaines : data-sci, ml-eng
- [[Regression metrics]] — domaines : data-sci, ml-eng
- [[ROC-AUC & courbe PR|ROC-AUC / courbe PR]] — domaines : data-sci, ml-eng
- [[Validation croisée]] — domaines : data-sci, ml-eng

### Briques
- [[evaluate]] — Bibliothèque HuggingFace de métriques d'évaluation ML prêtes à l'emploi — accuracy, F1, BLEU, ROUGE, exact match… chargées depuis le Hub via une API unique load/compute, comparables d'un projet à l'autre.
- [[seqeval]] — Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger.
<!-- AUTO:END -->

## Notes
