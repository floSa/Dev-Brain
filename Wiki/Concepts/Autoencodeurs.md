---
galaxie: wiki
type: concept
nom: Autoencodeurs
alias: [Autoencodeur, Autoencoder, Auto-encodeur, AE, VAE, Variational Autoencoder, Autoencodeur variationnel, Denoising autoencoder]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [deep-learning, unsupervised, representation-learning, dimensionality-reduction]
---

# Autoencodeurs

## Aperçu

- Réseau entraîné à **reproduire son entrée en sortie**, en la faisant passer par un goulot d'étranglement plus étroit qu'elle. L'exercice paraît absurde — copier une donnée — mais la contrainte force le réseau à ne garder que l'essentiel.
- C'est ce qu'on cherche : pas la sortie, mais le **code intermédiaire**. L'autoencodeur est un prétexte à apprendre une représentation, sans aucune étiquette. La reconstruction n'est qu'une fonction de perte gratuite.

## Concepts clés

### Encodeur, code, décodeur
- **Encodeur** $f$ : entrée → code $z$ (souvent appelé espace latent). **Décodeur** $g$ : code → reconstruction $\hat{x}$. On entraîne les deux ensemble à minimiser l'écart $x$ vs $\hat{x}$.
- Une fois entraîné, on jette souvent le décodeur : seul l'encodeur sert, comme extracteur de représentation.

### Le goulot est le régularisateur
- Sans contrainte, l'autoencodeur apprend l'**identité** — copier parfaitement, sans rien comprendre. Toute l'ingénierie consiste à l'en empêcher.
- Trois façons de contraindre : réduire la dimension du code (**sous-complet**), forcer la parcimonie (peu de neurones actifs — voir [[Sparse autoencoders]]), ou bruiter l'entrée (**denoising** : reconstruire le propre à partir du sale, ce qui interdit la copie).

### Le lien avec la PCA
- Un autoencodeur **linéaire** à perte quadratique apprend exactement le même sous-espace que la [[PCA]] — pas forcément les mêmes axes, mais le même espace engendré.
- Ce qui justifie l'objet : dès qu'on ajoute des activations non linéaires, il apprend une **variété courbe** que la PCA, linéaire par construction, ne peut pas capter. L'autoencodeur est la PCA rendue non linéaire ([[Manifold learning]]).

### VAE — le cousin génératif
- Un autoencodeur ordinaire n'est **pas génératif** : son espace latent est troué. Tirer un $z$ au hasard et le décoder produit du bruit, parce que rien n'a contraint la forme de cet espace.
- Le **VAE** encode vers une *distribution* (moyenne + variance) au lieu d'un point, et ajoute une pénalité [[KL divergence|KL]] qui rapproche l'espace latent d'une gaussienne. L'espace devient continu et échantillonnable → on peut générer.
- Différence de nature, pas de degré : AE = compresser, VAE = modéliser une distribution. Ne pas les confondre.

### La famille, et ce que chacun optimise

| Variante | La contrainte ajoutée | Ce qu'on en fait |
|---|---|---|
| **Sous-complet** | Code plus petit que l'entrée | Réduction de dimension non linéaire |
| **Denoising (DAE)** | Entrée bruitée, cible propre | Débruitage, représentations robustes |
| **Sparse (SAE)** | Peu de neurones actifs à la fois | Interprétabilité — code **plus grand** que l'entrée |
| **Variationnel (VAE)** | Latent proche d'une gaussienne (KL) | Génération, échantillonnage |
| **Contractif** | Pénalité sur la jacobienne | Robustesse aux petites perturbations |

- À noter : le **SAE est sur-complet** — son code est plus large que l'entrée. Il va à rebours de l'intuition « autoencodeur = compresser », et c'est précisément ce qui le rend utile en interprétabilité.

## Les maths, simplement

- Objectif de base : $\min_{f, g} \; \mathbb{E}_x \big[ \lVert x - g(f(x)) \rVert^2 \big]$ — reconstruire au mieux. Rien d'autre.
- Le code est $z = f(x)$, de dimension $k$. Si $k \ge \dim(x)$ et qu'aucune autre contrainte n'existe, la solution optimale est $g \circ f = \text{id}$ : le réseau triche et n'apprend rien.
- VAE — la borne inférieure de l'évidence (ELBO) : $\mathcal{L} = \underbrace{\mathbb{E}_{q(z|x)}[\log p(x|z)]}_{\text{reconstruction}} - \underbrace{D_{KL}\big(q(z|x) \,\|\, p(z)\big)}_{\text{régularise le latent}}$. Le premier terme veut copier, le second veut que le latent ressemble à $\mathcal{N}(0, I)$. Toute la tension du VAE est là.
- L'astuce de reparamétrisation, qui rend le VAE entraînable : échantillonner $z \sim \mathcal{N}(\mu, \sigma^2)$ n'est pas dérivable. On écrit $z = \mu + \sigma \odot \epsilon$ avec $\epsilon \sim \mathcal{N}(0, I)$ — le hasard passe dans $\epsilon$, et le gradient traverse $\mu$ et $\sigma$.

## En pratique

- **Sur données tabulaires, la [[PCA]] suffit presque toujours** — et elle est déterministe, instantanée, sans réglage. N'aller vers l'autoencodeur que si la non-linéarité est établie, pas par principe.
- **Détection d'anomalies** : entraîner sur du normal, puis lire l'**erreur de reconstruction** — ce que le modèle reconstruit mal est ce qu'il n'a jamais vu. Approche séduisante mais moins robuste qu'on ne croit : un autoencodeur assez large généralise et finit par bien reconstruire les anomalies aussi ([[Détection d'outliers multivariée]], [[Time series anomaly detection]]).
- **Les VAE génèrent flou.** La perte quadratique moyenne les reconstructions plausibles ; c'est structurel, pas un défaut de réglage. Pour de la génération d'images, les [[Diffusion models|modèles de diffusion]] ont gagné — mais le VAE survit **à l'intérieur** d'eux, comme compresseur vers l'espace latent (Stable Diffusion).
- **Le pré-entraînement par autoencodeur est passé de mode** : c'était l'usage historique (2006-2012), supplanté par les objectifs contrastifs et le masquage ([[Apprentissage auto-supervisé en vision]], [[embeddings]]).
- **Sa renaissance vient de l'interprétabilité** : les [[Sparse autoencoders|SAE]] appliqués aux activations de LLM sont aujourd'hui le principal usage de recherche — un retournement complet, puisqu'ils décompressent au lieu de compresser.
- Outils : [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/Keras|Keras]] (une trentaine de lignes suffisent) ; [[Dev/Services/PyOD|PyOD]] pour la variante détection d'anomalies clés en main.

## Approches voisines & alternatives

- [[PCA]] — l'équivalent linéaire, dont l'autoencodeur est la généralisation non linéaire. À essayer en premier.
- [[Réduction de dimension]] — le chapeau de la famille.
- [[Sparse autoencoders]] — la variante sur-complète, cœur de l'interprétabilité des LLM aujourd'hui.
- [[Manifold learning]] — l'autre voie non linéaire, sans réseau.
- [[t-SNE and UMAP]] — pour visualiser ; contrairement à l'autoencodeur, ils ne savent pas transformer de nouveaux points aisément.
- [[embeddings]] — les représentations apprises qui ont supplanté l'autoencodeur comme extracteur.
- [[Diffusion models]] — ont détrôné le VAE en génération, tout en l'utilisant comme compresseur latent.
- [[GANs]] — l'autre famille générative historique, adversariale plutôt que reconstructive.
- [[KL divergence]] — le terme qui régularise le latent d'un VAE.
- [[Apprentissage non supervisé]] — le cadre englobant.

## Pour aller plus loin

- Hinton & Salakhutdinov (2006) — *Reducing the Dimensionality of Data with Neural Networks* : l'article qui a relancé le domaine.
- Kingma & Welling (2013) — *Auto-Encoding Variational Bayes* : le VAE et l'astuce de reparamétrisation.
- Goodfellow, Bengio, Courville — *Deep Learning*, ch. 14 (Autoencoders).
