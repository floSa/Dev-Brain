---
galaxie: dev
type: service
nom: CausalImpact
alias: [tfcausalimpact, tfp-causalimpact, pycausalimpact]
pitch: "Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [causal-inference, bayesian, timeseries]
url_docs: https://google.github.io/CausalImpact/CausalImpact.html
url_repo: https://github.com/WillianFuks/tfcausalimpact
---

# CausalImpact

## Pourquoi

Estime l'**effet causal d'une intervention** (lancement, campagne, changement de prix) quand on ne dispose pas d'un essai randomisé. À partir de la série de réponse et d'un jeu de **séries de contrôle** non affectées par l'intervention, un modèle bayésien de **séries temporelles structurelles** (BSTS) prédit le **contrefactuel** — ce qu'aurait été la métrique sans intervention — puis mesure l'écart cumulé avec son incertitude. Méthode introduite chez Google (Brodersen et al.) ; portée en Python via `tfcausalimpact` (communauté) et `tfp-causalimpact` (Google, TensorFlow Probability).

## Quand l'utiliser

- Mesurer l'impact d'un événement ponctuel et daté sur une métrique suivie dans le temps, sans groupe témoin tiré au sort.
- On dispose de séries de contrôle corrélées et **non touchées** par l'intervention (autres marchés, produits, régions).
- Besoin d'un effet estimé **avec intervalle de crédibilité**, pas d'un simple avant/après.

## Quand NE PAS l'utiliser

- Données en panel avec groupe traité et groupe témoin observés : le cadre classique [[Wiki/Concepts/Diff-in-Diff|Diff-in-Diff]] est plus simple et plus transparent.
- Pas de bon contrôle non contaminé → le contrefactuel n'est pas crédible, aucun outil ne sauve un design faible.
- Effet diffus sans date d'intervention nette → relève d'une modélisation causale dédiée.

## Déploiement & coût

- `uv add tfcausalimpact` (backend TensorFlow Probability) ; l'original de référence est un package R.
- Single-node ; ajustement BSTS plus coûteux qu'une régression, raisonnable sur des séries usuelles.
- Apache-2.0, gratuit.

## Pièges

- Écosystème Python **fragmenté** : `tfcausalimpact` (communauté, le plus utilisé) vs `tfp-causalimpact` (Google, non « officiellement supporté ») — choisir et épingler, l'API diffère.
- Hypothèse forte : les contrôles doivent rester non affectés par l'intervention sur toute la période post — sinon le contrefactuel est biaisé.
- Sensible au choix de la fenêtre pré-intervention et des priors du modèle de tendance/saisonnalité.

## Alternatives

- Pas d'alternative outillée dans le brain. Approche concurrente côté méthode : [[Wiki/Concepts/Diff-in-Diff|Diff-in-Diff]] (design à groupe témoin), couvert côté libs par [[Dev/Services/statsmodels|statsmodels]].

## Liens

- Concepts implémentés : [[Wiki/Concepts/Inférence causale|Inférence causale]], [[Wiki/Concepts/Diff-in-Diff|Diff-in-Diff]], [[Wiki/Concepts/Inférence bayésienne|Inférence bayésienne]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://google.github.io/CausalImpact/CausalImpact.html
