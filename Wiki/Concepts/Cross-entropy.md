---
galaxie: wiki
type: concept
nom: Cross-entropy
alias: [Entropie croisée, cross entropy, log-loss, log loss, perte d'entropie croisée, negative log-likelihood, NLL]
categorie: concept/math
domaines: [data-sci, ml-eng, ai-eng]
tags: [information-theory, cross-entropy, classification]
---

# Cross-entropy

## Aperçu

- Mesure le **coût moyen d'encoder** des données issues d'une vraie loi $p$ en utilisant une loi estimée $q$. Minimale (= entropie de $p$) quand $q = p$, croît dès que $q$ s'écarte.
- C'est la **perte standard de la classification** et du pré-entraînement des modèles de langue : minimiser l'entropie croisée, c'est rapprocher la distribution prédite de la distribution réelle.

## Concepts clés

### Lien avec la vraisemblance
- Pour des étiquettes one-hot, l'entropie croisée se réduit à la **log-vraisemblance négative** (NLL) : $-\log q(\text{classe vraie})$. Minimiser l'entropie croisée ⇔ maximiser la vraisemblance (cf. [[Maximum de vraisemblance]]).

### Décomposition entropie + divergence
- $H(p,q) = H(p) + D_{KL}(p\,\|\,q)$. L'entropie $H(p)$ est **fixe** (dépend des données, pas du modèle) : optimiser l'entropie croisée revient exactement à minimiser la [[KL divergence|divergence KL]].

### Binaire, catégorielle, softmax
- **Binaire** (BCE) : sortie sigmoïde, deux classes. **Catégorielle** (CCE) : sortie softmax, $K$ classes. Le couple softmax + entropie croisée donne un gradient simple ($\hat p - y$), d'où sa domination en deep learning.

## Les maths, simplement

- $H(p,q) = -\sum_i p_i \log q_i$ ; sur un jeu de $n$ exemples et étiquettes one-hot : $-\dfrac{1}{n}\sum_i \log q_i(\text{classe}_i)$ — c'est exactement le **log-loss**.
- Cas binaire : $-\dfrac{1}{n}\sum_i \big[y_i\log\hat p_i + (1-y_i)\log(1-\hat p_i)\big]$.
- Pénalise lourdement la **confiance erronée** : prédire $\hat p \to 0$ pour la vraie classe envoie la perte vers $+\infty$.

## En pratique

- Perte par défaut en classification : `torch.nn.CrossEntropyLoss` ([[Dev/Services/PyTorch|PyTorch]], applique softmax + NLL en interne), `log_loss` côté [[Dev/Services/Scikit-Learn|sklearn.metrics]].
- Comme métrique d'évaluation, c'est le **log-loss** des [[Classification metrics]] : il note les probabilités, pas seulement la décision → exige un modèle bien calibré (cf. [[Calibration]]).
- **Label smoothing** : adoucir les cibles one-hot ($1\to 0.9$) régularise et améliore la calibration des réseaux profonds.
- Sur classes déséquilibrées, pondérer les termes par classe (focal loss, poids) pour ne pas écraser les classes rares (cf. [[Imbalanced classification]]).

## Approches voisines & alternatives

- [[Shannon entropy]] — la borne inférieure de l'entropie croisée ; l'écart au-dessus est la divergence KL.
- [[KL divergence]] — ce que l'entropie croisée minimise réellement (l'entropie de $p$ étant constante).
- [[Classification metrics]] — l'entropie croisée y figure comme **log-loss**, métrique de probabilité aux côtés de l'accuracy et du F1.
- [[Perplexity]] — son exponentielle, échelle usuelle pour les modèles de langue.
- [[Maximum de vraisemblance]] — minimiser l'entropie croisée = estimer par maximum de vraisemblance.

## Pour aller plus loin

- Goodfellow, Bengio & Courville — *Deep Learning*, chapitre sur les fonctions de coût probabilistes.
- Müller, Kornblith & Hinton (2019) — *When Does Label Smoothing Help?*.
