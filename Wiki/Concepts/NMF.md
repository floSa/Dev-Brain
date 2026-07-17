---
galaxie: wiki
type: concept
nom: NMF
alias: [Non-negative Matrix Factorization, Factorisation en matrices non négatives, Factorisation non négative, NNMF, Semi-NMF, Convex NMF]
categorie: concept/ml
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis, unsupervised]
---

# NMF

## Aperçu

- Décomposition d'une matrice **positive** en produit de deux matrices **positives** : $V \approx W H$. Une seule contrainte ajoutée par rapport aux autres factorisations — l'interdiction du négatif — et elle change tout.
- Cette contrainte produit une **représentation par parties additives** : on ne peut qu'ajouter des morceaux, jamais en soustraire. Là où la [[PCA]] décrit un visage comme « un visage moyen moins ceci plus cela », la NMF le décrit comme « un nez + une bouche + des yeux ». C'est ce qui la rend interprétable là où la PCA ne l'est pas.

## Concepts clés

### Pourquoi la positivité change tout
- La [[PCA]] et la [[SVD]] produisent des composantes à coefficients de signe quelconque. Résultat : les parties se compensent, et « −0,3 × composante 2 » n'a le plus souvent aucun sens physique.
- Beaucoup de données réelles sont **positives par nature** : comptages de mots, intensités de pixels, spectres, quantités vendues, activations ReLU. Un coefficient négatif y est physiquement absurde.
- En interdisant le négatif, la NMF force chaque composante à être un **constituant** de la donnée, pas une direction de variation. L'additivité est ce qui la rend lisible.

### Ce qu'elle perd au passage
- **Aucune orthogonalité, aucun ordre.** Comme l'[[ICA]] et contrairement à la PCA : pas de « première composante », pas de variance expliquée pour classer.
- **Aucune unicité** : le problème est non convexe, il n'existe pas de solution fermée. Deux exécutions depuis des initialisations différentes donnent des décompositions différentes — toutes légitimes.
- **La reconstruction est moins bonne** qu'une SVD de même rang. C'est mathématiquement inévitable : on optimise sous contrainte. On échange de la précision contre du sens.

### Le choix de la divergence
- **Frobenius** (moindres carrés) — le défaut. Suppose un bruit gaussien. Convient aux intensités, aux spectres.
- **Kullback-Leibler** — adaptée aux **comptages** (un mot apparaît 3 fois, pas −1,7 fois). C'est le bon choix sur du texte, et elle relie la NMF au *topic modeling* probabiliste.
- **Itakura-Saito** — pour l'audio (spectrogrammes de puissance), invariante d'échelle.
- Ce choix n'est pas cosmétique : il encode l'hypothèse sur le bruit des données.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_components` | Nombre de parties cherchées | **Le seul choix qui compte, et il n'a pas de critère objectif.** À fixer par le métier ou par erreur de reconstruction vs interprétabilité |
| `init` | Initialisation | `nndsvd` (déterministe, bon pour la parcimonie) plutôt que `random` — reproductible |
| `beta_loss` | La divergence | `frobenius` (bruit gaussien), `kullback-leibler` (comptages), `itakura-saito` (audio) |
| `alpha_W` / `alpha_H` | Pénalité de régularisation (cf. [[Régularisation]]) | ↑ = décomposition plus parcimonieuse, donc plus lisible |
| `l1_ratio` | Dosage L1 / L2 | Vers L1 = parties plus creuses et plus nettes |
| `max_iter` | Itérations | 200 par défaut, souvent insuffisant — l'avertissement de non-convergence est fréquent |

## Les maths, simplement

- Le problème : $\min_{W \ge 0, \; H \ge 0} \; \lVert V - WH \rVert_F^2$, avec $V \in \mathbb{R}^{n \times m}_{+}$, $W \in \mathbb{R}^{n \times k}_{+}$, $H \in \mathbb{R}^{k \times m}_{+}$ et $k \ll \min(n, m)$.
- Lecture des facteurs : $W$ = les **parties** (le dictionnaire, $k$ composantes), $H$ = les **poids** de chaque partie dans chaque observation. Chaque donnée se reconstruit comme $v_j \approx \sum_{i=1}^{k} W_i \, H_{ij}$ — une somme pondérée **positive** de parties.
- Le problème est **non convexe conjointement en $(W, H)$**, mais convexe en chacune séparément. D'où les algorithmes alternés : fixer $W$, optimiser $H$, inverser, répéter. On converge vers un optimum **local** — ce qui explique la non-unicité.
- Règles multiplicatives de Lee & Seung, l'algorithme historique : $H \leftarrow H \odot \dfrac{W^\top V}{W^\top W H}$ et $W \leftarrow W \odot \dfrac{V H^\top}{W H H^\top}$. Élégance de la mise à jour : partant de facteurs positifs, elle ne multiplie que par des quantités positives — **la positivité est préservée gratuitement**, sans projection ni contrainte explicite.
- Avec la divergence KL, la NMF devient formellement équivalente à un modèle de sujets probabiliste (pLSA).

## En pratique

- **Ne s'applique qu'à des données positives.** Sur des données centrées ou signées, elle n'a pas de sens — utiliser [[PCA]], [[SVD]] ou [[ICA]]. La variante **Semi-NMF** relâche la contrainte sur $W$ si nécessaire.
- **Choisir `beta_loss` selon la nature du bruit** : `kullback-leibler` sur des comptages, `frobenius` sur des intensités. C'est le réglage le plus souvent laissé au défaut à tort.
- **`init='nndsvd'` plutôt que `random`** : déterministe et reproductible. Sinon, fixer `random_state` — la non-unicité fait croire à un bug.
- **`n_components` n'a pas de bonne réponse.** Il n'y a pas de coude d'inertie ni de variance expliquée. Trancher par l'interprétabilité des parties obtenues, ce qui est un jugement, pas un calcul.
- **Terrain naturel** : topic modeling sur du [[TF-IDF]] (une baseline honnête, souvent suffisante), décomposition de spectrogrammes ([[STFT et spectrogramme]]), imagerie, systèmes de recommandation (la factorisation de matrices y est reine, [[Systèmes de recommandation]]).
- **Usage en interprétabilité** : [[Dev/Services/interpreto|interpreto]] la propose comme méthode de dictionnaire sur les activations, à côté des [[Sparse autoencoders|SAE]] et de l'[[ICA]]. Elle y est particulièrement légitime — les activations post-ReLU sont **positives par construction**, et NMF est instantanée là où un SAE demande un entraînement complet. La baseline à battre avant de sortir l'artillerie.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.decomposition.NMF]] (et `MiniBatchNMF` à grande échelle).

## Approches voisines & alternatives

- [[PCA]] — le contraste de référence : directions signées et orthogonales, meilleure reconstruction, mais composantes rarement interprétables.
- [[SVD]] — la factorisation sans contrainte dont la NMF est la version contrainte ; reconstruction optimale à rang donné.
- [[ICA]] — l'autre décomposition « à part » : indépendance au lieu de positivité, sources au lieu de parties.
- [[Matrix decompositions]] — la famille algébrique.
- [[Réduction de dimension]] — le chapeau.
- [[Sparse autoencoders]] — le pendant non linéaire et appris, pour démêler des activations. NMF en est la baseline linéaire.
- [[Clustering]] — la NMF à contrainte forte s'y ramène (Convex NMF ≈ [[K-Means]]).
- [[TF-IDF]] — l'entrée type pour le topic modeling.
- [[Systèmes de recommandation]] — la factorisation de matrices y est la méthode historique.

## Pour aller plus loin

- Lee & Seung (1999) — *Learning the parts of objects by non-negative matrix factorization* (Nature) : l'article fondateur, et l'exemple des visages décomposés en parties.
- Lee & Seung (2001) — *Algorithms for Non-negative Matrix Factorization* : les règles multiplicatives.
- Documentation scikit-learn — *Decomposing signals in components*, où la comparaison PCA / ICA / NMF sur le jeu de visages est visuelle.
