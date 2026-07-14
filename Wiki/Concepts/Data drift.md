---
galaxie: wiki
type: concept
nom: Data drift
alias: [dérive de données, distribution shift, drift, dérive de distribution]
categorie: concept/ml
domaines: [mlops, data-sci]
tags: [data-drift, concept-drift, model-monitoring]
---

# Data drift

## Aperçu

- La distribution des données en production s'écarte de celle vue à l'entraînement → le modèle se dégrade **silencieusement** : il continue d'émettre des prédictions, mais elles deviennent fausses.
- Enjeu central du monitoring ML : un modèle n'est pas figé une fois déployé, le monde sous-jacent bouge (saisonnalité, nouveaux comportements, changement de capteur, de marché).

## Concepts clés

### Covariate shift (data drift au sens strict)
- La distribution des entrées change : `P(X)` se déplace, mais la relation entrée→cible `P(y|X)` reste stable.
- Ex. une part croissante de trafic mobile sur un modèle entraîné surtout sur du desktop.

### Concept drift
- La **relation** elle-même se déforme : `P(y|X)` change. Mêmes entrées, cible différente.
- Ex. après un changement réglementaire, le même profil client ne présente plus le même risque de défaut.

### Label shift (prior shift)
- La distribution de la cible change : `P(y)` se déplace (ex. taux de fraude qui explose), même si `P(X|y)` reste stable.

### Dynamique temporelle
- **Soudain** (rupture : panne de capteur, déploiement amont), **graduel** (glissement lent), **récurrent/saisonnier** (à ne pas confondre avec une vraie dérive).

## Les maths, simplement

- Comparer une distribution de **référence** `P_ref` (le train, ou une période prod saine) à la distribution **courante** `P_cur` sur une fenêtre récente.
- **PSI** (Population Stability Index), par binning : $PSI = \sum_i (q_i - p_i)\,\ln\frac{q_i}{p_i}$, où $p_i, q_i$ sont les proportions du bin $i$ en référence et en courant. Repères usuels : $<0{,}1$ stable, $0{,}1$–$0{,}25$ à surveiller, $>0{,}25$ dérive marquée.
- Tests par variable : Kolmogorov-Smirnov (numérique), khi-deux (catégoriel) — attention au sur-déclenchement sur gros volumes.
- Écart entre distributions : [[KL divergence]] (asymétrique), [[Jensen-Shannon divergence]] (symétrique, bornée), [[Wasserstein distance]] (métrique, sensible à l'ampleur du déplacement).

## En pratique

- Fixer une **fenêtre de référence** et la comparer à des fenêtres glissantes ; surveiller les **features** (input drift) **et** les **prédictions/scores** (output drift).
- Suivre la **performance réelle** dès que les labels arrivent — souvent **retardés** : sans labels, le drift des inputs/scores sert de proxy d'alerte précoce.
- Réagir, ne pas sur-réagir : alerte → investigation → ré-entraînement ciblé ou rollback. Un drift saisonnier connu n'est pas un incident.
- Tracer les métriques de drift et de perf dans le suivi d'expériences ([[Dev/Services/MLflow|MLflow]]) pour relier dérive observée et version de modèle.
- Outillage spécialisé : [[Dev/Services/Evidently|Evidently]] (en fiche), NannyML, WhyLabs.

## Approches voisines & alternatives

- [[Data leakage]] — autre cause d'écart train↔prod, mais côté conception/évaluation (information du futur dans le train), pas dérive temporelle en production.
- [[KL divergence]], [[Jensen-Shannon divergence]], [[Wasserstein distance]] — mesures quantifiant l'écart entre référence et courant.
- [[Monitoring de modèle en production]] — le cadre opérationnel qui surveille le drift parmi d'autres signaux (perf, données, infra).
- [[Calibration]] — la fiabilité des probabilités prédites se dégrade typiquement avec le drift.
- [[Dev/Services/MLflow|MLflow]] — tracking / registre où journaliser drift et performance pour le monitoring.
- [[Dev/Services/Evidently|Evidently]] — outillage de détection de drift et de monitoring (PSI, KS, 20+ méthodes, rapports et dashboards).
- [[Dev/Services/River|River]] — apprentissage en ligne qui s'adapte à la dérive en continu (détecteurs ADWIN / Page-Hinkley intégrés), plutôt que de la détecter pour ré-entraîner en batch.

## Pour aller plus loin

- Gama et al. (2014) — *A Survey on Concept Drift Adaptation*.
- Documentation Evidently / NannyML — détection de drift et estimation de performance sans labels.
