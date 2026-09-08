---
role: brique
nom: CausalImpact
alias: [tfcausalimpact, tfp-causalimpact, pycausalimpact]
pitch: "Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle."
categorie: stats/causal
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [causal-inference, bayesian, timeseries]
url_docs: https://google.github.io/CausalImpact/CausalImpact.html
url_repo: https://github.com/WillianFuks/tfcausalimpact
---

# CausalImpact

<!-- AUTO:BANDEAU:START -->
> Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2025-01-13 |
<!-- AUTO:BANDEAU:END -->

## Définition

Estime l'effet causal d'une intervention datée — lancement, campagne, changement de prix —
quand aucun essai randomisé n'est disponible. À partir de la série de réponse et d'un jeu
de **séries de contrôle non affectées**, un modèle bayésien de séries temporelles
structurelles (BSTS) prédit le **contrefactuel**, ce qu'aurait été la métrique sans
intervention, puis mesure l'écart cumulé avec son intervalle de crédibilité. Méthode
introduite chez Google (Brodersen et al.) ; côté Python, elle est portée par deux paquets
concurrents d'API différente, `tfcausalimpact` (communauté) et `tfp-causalimpact` (Google).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Mesurer l'impact d'un événement ponctuel et daté sur une métrique suivie dans le temps, sans groupe tiré au sort | Écosystème Python **fragmenté** : `tfcausalimpact` contre `tfp-causalimpact`, API différentes, aucun officiellement supporté — choisir et épingler |
| Disposer de séries de contrôle corrélées et non touchées par l'intervention — autres marchés, produits, régions | Hypothèse forte : les contrôles doivent rester non affectés sur **toute** la période post, sinon le contrefactuel est biaisé |
| Vouloir un effet estimé avec intervalle de crédibilité, pas un simple avant/après | Sensible au choix de la fenêtre pré-intervention et aux priors de tendance et de saisonnalité |
| | Données en panel avec groupe traité et groupe témoin observés : le cadre classique [[Diff-in-Diff]] est plus simple et plus transparent |
| | Sans bon contrôle non contaminé, ou sans date d'intervention nette : aucun outil ne sauve un design faible |

## Mise en œuvre

- Installation — `uv add tfcausalimpact` ; l'implémentation de référence reste un package R
- Point d'entrée — import Python, `CausalImpact(data, pre_period, post_period)`, puis `summary()` et `plot()`
- Prérequis — TensorFlow Probability comme backend ; des séries de contrôle crédibles comme prérequis méthodologique
- Exécution — dans le process appelant, CPU, mono-nœud ; ajustement BSTS plus coûteux qu'une régression
- Coût — gratuit, Apache-2.0, aucune limite d'usage

## Écosystème

### Alternatives

- Aucune outillée dans le brain : côté méthode, l'approche concurrente est [[Diff-in-Diff]], couvert côté bibliothèques par [[statsmodels]].

## Ressources

- Documentation — https://google.github.io/CausalImpact/CausalImpact.html
- Dépôt — https://github.com/WillianFuks/tfcausalimpact

## Voir aussi

- [[Inférence causale]] · [[Diff-in-Diff]] · [[Inférence bayésienne]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
