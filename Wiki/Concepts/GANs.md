---
galaxie: wiki
type: concept
nom: GANs
alias: [GAN, generative adversarial network, génération adversariale, réseau antagoniste génératif, DCGAN, StyleGAN, WGAN, CycleGAN, pix2pix]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [gan, generative-model, image-generation, deep-learning]
---

# GANs

## Aperçu

- Deux réseaux en **jeu adversarial** : un **générateur** $G$ fabrique des images à partir de bruit, un **discriminateur** $D$ tente de distinguer le vrai du faux. À l'équilibre, $G$ produit du réaliste et $D$ ne fait mieux que le hasard.
- Idée clé (Goodfellow et al., 2014) : remplacer une vraisemblance explicite par une **compétition** — $G$ apprend en cherchant à **tromper** $D$. Longtemps l'état de l'art en image, aujourd'hui supplanté par la [[Diffusion models|diffusion]] sur la génération générale.

## Concepts clés

### Le jeu min-max
- $G$ et $D$ s'entraînent **en opposition** : $D$ maximise sa capacité à classer vrai/faux, $G$ minimise cette même capacité. Pas de cible fixe : chacun poursuit une frontière qui bouge.

### Instabilité & mode collapse
- Équilibre **fragile** : oscillations, gradients qui s'évanouissent, et surtout **mode collapse** (G ne produit qu'une poignée de modes, perdant la diversité). Remèdes : **WGAN** (distance de **Wasserstein** / transport optimal au lieu de la divergence de Jensen-Shannon), *gradient penalty*, *spectral normalization*, règles d'apprentissage à deux échelles de temps.

### Familles marquantes
- **DCGAN** (convolutif, recette stable de base), **StyleGAN** (Karras et al. — visages photoréalistes, contrôle du style par couche), **Conditional GAN** (génération conditionnée par une classe / une entrée), **pix2pix** et **CycleGAN** (traduction image→image, appariée ou non), **ESRGAN** (super-résolution).

### Génération en une passe
- Contrairement à la diffusion (échantillonnage **itératif**), un GAN génère en **un seul forward** → très rapide. D'où sa persistance en super-résolution, génération temps réel, et comme **perte adversariale** dans la distillation de modèles de diffusion (modèles *turbo*, GigaGAN).

## Les maths, simplement

- Objectif original : $\min_G \max_D \; \mathbb{E}_{x}[\log D(x)] + \mathbb{E}_{z}[\log(1 - D(G(z)))]$. À $D$ optimal, $G$ minimise la [[Jensen-Shannon divergence|divergence de Jensen-Shannon]] entre données réelles et générées — d'où les gradients qui s'effondrent quand les deux distributions ne se recouvrent pas.
- **WGAN** : $\min_G \max_{D\,\in\,1\text{-Lip}} \; \mathbb{E}_x[D(x)] - \mathbb{E}_z[D(G(z))]$ — la distance de Wasserstein donne un gradient utile même sans recouvrement (d'où la contrainte 1-Lipschitz).

## En pratique

- Largement **supplanté par la [[Diffusion models|diffusion]]** pour le text-to-image général : plus stable à entraîner, plus divers, meilleure couverture des modes.
- Reste pertinent là où la **vitesse** compte (génération 1-passe, super-résolution temps réel) et sur des domaines spécialisés (visages : StyleGAN).
- Évaluation : **FID** (réalisme + diversité) et Inception Score ; surveiller le *mode collapse* à l'œil sur des échantillons.

## Approches voisines & alternatives

- [[Diffusion models]] — la famille qui a **détrôné** les GAN sur l'image : débruitage itératif stable vs jeu adversarial unique mais instable.
- [[Image generation]] — l'application principale ; les générateurs actuels sont surtout des modèles de diffusion, les GAN y interviennent en super-résolution / accélération.
- [[Jensen-Shannon divergence]] — ce que minimise le GAN original ; sa faiblesse motive le passage au transport optimal (WGAN).
- [[Vision par ordinateur]] — la génération adversariale est l'un des versants **génératifs** de la vision.

## Pour aller plus loin

- Goodfellow et al. (2014) — *Generative Adversarial Nets*.
- Radford et al. (2015) — *DCGAN* · Arjovsky et al. (2017) — *Wasserstein GAN*.
- Karras et al. (2019) — *A Style-Based Generator Architecture for GANs* (StyleGAN).
