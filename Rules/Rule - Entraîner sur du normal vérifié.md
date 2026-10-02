---
role: rule
domaine: data-quality
applicable: anomaly-detection
strictness: must
tags: [rule, anomaly-detection, data-leakage, thresholding]
---

# Rule — Entraîner sur du normal vérifié

## Principe

Un détecteur d'anomalies n'apprend que ce qu'on lui donne comme normal : un défaut présent dans l'entraînement devient du normal, et le détecteur cesse de le voir. Le « normal » se vérifie, il ne se suppose pas.

## MUST

- Le jeu d'entraînement d'un détecteur non supervisé ou semi-supervisé ne contient que des données dont une personne qui connaît la machine ou le procédé a vérifié l'absence de défaut. Les arrêts, démarrages, interventions de maintenance, capteurs gelés et périodes précédant une panne en sont exclus, avec une marge avant et après.
- **Trois jeux disjoints** : entraînement (normal vérifié), réglage du seuil (normal vérifié, jamais vu à l'entraînement), test (avec défauts étiquetés). Un seuil réglé sur le jeu qui sert à mesurer le détecteur donne un chiffre optimiste ([[Score et seuil d'alerte]], [[Data leakage]]).
- La provenance du normal est consignée : machine, période, version des capteurs, nom de la personne qui a vérifié.
- En vision, les images de « bon » sont relues une à une avant d'entrer dans la banque ou dans l'entraînement ([[Détection d'anomalies visuelle]]).

## SHOULD

- Écrire la **contamination supposée** du jeu, et la contrôler sur un échantillon relu. Le paramètre `contamination` de scikit-learn fixe un seuil comme quantile des scores d'entraînement ; ce n'est pas une garantie sur le taux de fausses alertes d'un flux futur ([[Types d'anomalies et régimes de supervision]], [[Score et seuil d'alerte]]).
- Réexaminer le normal dès que la machine, le procédé, le capteur ou le lot de matière changent : le régime appris n'est plus le régime courant ([[Data drift]]).
- Ne pas livrer un modèle entraîné sur un jeu public de licence non commerciale : MVTec AD sert à comparer des méthodes ([[Jeux de données d'anomalies]]).
- Conditionner par régime : un modèle par régime stable, ou le régime en entrée, plutôt qu'un seul normal moyen.

## NICE-TO-HAVE

- Figer le jeu d'entraînement par empreinte et le versionner avec le modèle ([[DVC]]) : un score de demain doit pouvoir se rejouer sur le normal d'aujourd'hui.
- Mesurer la sensibilité à la contamination : ajouter volontairement quelques défauts connus à l'entraînement et voir de combien le score des défauts de test baisse.

## Exemples

### Bon

```python
normal = fenetres[(fenetres.regime == "marche") & fenetres.verifie_metier]
train, reglage = split_temporel(normal)            # deux périodes disjointes
model = IsolationForest().fit(train)
seuil = np.quantile(model.score_samples(reglage), q_bas)
# le test porte sur des défauts étiquetés, jamais sur `train` ni `reglage`
```

### Mauvais

```python
X = historique_brut                                # arrêts, pannes, capteurs gelés
model = IsolationForest(contamination=0.01).fit(X)  # le « normal » apprend les défauts
```

## Exceptions

- Défauts nombreux, étiquetés et stables : un détecteur supervisé devient possible, avec les pièges de la classe rare ([[Évaluer une détection d'anomalies]]) ; la règle vaut alors pour le jeu de réglage du seuil.
- Aucun normal vérifiable (démarrage de ligne) : les sorties du modèle sont un outil d'exploration, pas une alerte. Le dire dans le livrable.
- Un prototype zero-shot sert à juger si un défaut est visible ; il ne se livre pas sans mesure sur les défauts réels de la ligne ([[Anomalie visuelle zero-shot et few-shot]]).

## Voir aussi

- [[Types d'anomalies et régimes de supervision]] — régimes de supervision, normal propre, contamination
- [[Score et seuil d'alerte]] — du score à la décision, seuil sur du normal vérifié
- [[Pattern - Détection d'anomalies en deux étages]] — l'étage 1 qui écarte les données invalides avant l'entraînement
- [[Pattern - Inspection visuelle en ligne de production]] — constituer le « bon » avant de choisir la méthode
- [[Rule - Évaluer une anomalie par événement, pas par point]]
