---
role: hub
nom: Théorie de l'information
alias: [information theory, entropie, divergences, transport optimal]
pitch: Mesurer l'incertitude d'une loi et l'écart entre deux lois — d'où viennent la perte de la classification et la plupart des critères de comparaison de distributions.
domaines: [data-sci, ml-eng, ai-eng]
tags: [information-theory, entropy, cross-entropy, kl-divergence, mutual-information, optimal-transport]
---

# Théorie de l'information

> Mesurer l'incertitude d'une loi et l'écart entre deux lois — d'où viennent la perte de la classification et la plupart des critères de comparaison de distributions.

## Ce qu'il faut comprendre

- **Tout part d'une seule quantité.** [[Shannon entropy]] mesure l'incertitude moyenne d'une distribution ; [[Cross-entropy]], [[KL divergence]] et [[Mutual information]] s'écrivent toutes à partir d'elle. Lire l'entropie en premier fait tomber les trois autres.
- **La page à retenir pour le travail quotidien est [[Cross-entropy]]** : c'est la perte de toute classification et du pré-entraînement des modèles de langue. Sur des étiquettes one-hot elle se réduit à la log-vraisemblance négative — entraîner par entropie croisée et entraîner par [[Maximum de vraisemblance]] sont le même geste.
- **[[KL divergence]] est la mesure de référence, et elle a deux défauts qui expliquent tout le reste du dossier.** Elle est **asymétrique** — $D(p\|q) \ne D(q\|p)$, et le choix du sens change ce que le modèle fait — et elle **explose à $+\infty$** dès que les supports ne se recouvrent pas. [[Jensen-Shannon divergence]] corrige les deux, au prix d'une borne. [[Optimal transport]] et [[Wasserstein distance]] corrigent le second autrement, en tenant compte de la **distance entre les points** au lieu de comparer les masses point par point : c'est ce qui les rend informatives sur des supports disjoints.
- **[[Optimal transport]] est rangé ici bien qu'il soit un programme linéaire**, et c'est un arbitrage assumé : ce que la page produit est une mesure d'écart entre distributions, et c'est par là qu'on la cherche. Sa valeur optimale *est* la [[Wasserstein distance]] — les séparer aurait mis dans deux dossiers une page et le nombre qu'elle calcule.
- **[[Mutual information]] n'est pas une corrélation.** Elle capte toute forme de dépendance, linéaire ou non, et vaut zéro si et seulement si les variables sont indépendantes — d'où son intérêt en sélection de variables, et sa difficulté d'estimation en dimension.

## Choisir

- Une perte pour de la classification → [[Cross-entropy]].
- Comparer deux distributions dont les supports se recouvrent → [[KL divergence]].
- Les comparer symétriquement, ou les clusteriser → [[Jensen-Shannon divergence]].
- Les comparer quand les supports sont disjoints ou décalés → [[Wasserstein distance]], et [[Optimal transport]] pour le mécanisme.
- Mesurer une dépendance non linéaire entre deux variables → [[Mutual information]].
- Comprendre d'où sortent toutes ces formules → [[Shannon entropy]].
- Tester si un écart observé est significatif sur un échantillon → [[Tests d'hypothèse]], au domaine [[Statistiques & inférence]] : ce dossier définit l'écart, il ne le teste pas.

<!-- AUTO:START -->
### Notions
- [[Cross-entropy]] — domaines : data-sci, ml-eng, ai-eng
- [[Jensen-Shannon divergence]] — domaines : data-sci, ml-eng
- [[KL divergence]] — domaines : data-sci, ml-eng
- [[Mutual information]] — domaines : data-sci, ml-eng
- [[Optimal transport]] — domaines : data-sci, ml-eng
- [[Shannon entropy]] — domaines : data-sci, ml-eng
- [[Wasserstein distance]] — domaines : data-sci, ml-eng
<!-- AUTO:END -->
