---
galaxie: wiki
type: concept
nom: Diffusion models
alias: [DDPM, denoising diffusion, score-based models, latent diffusion, modèles de diffusion, diffusion]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [generative-model, diffusion, deep-learning]
---

# Diffusion models

## Aperçu

- Famille de **modèles génératifs** qui apprennent à **inverser un bruitage** : on détruit progressivement une donnée en y ajoutant du bruit gaussien (*forward*), puis un réseau apprend à **débruiter pas à pas** (*reverse*) pour échantillonner de nouvelles données.
- Idée clé : transformer la génération — un problème dur — en une **suite de petits débruitages**, chacun facile et stable à apprendre. C'est ce qui a détrôné les [[GANs|GAN]] (entraînement instable) sur l'image et la vidéo.

## Concepts clés

### Processus forward / reverse
- **Forward** : chaîne de Markov *fixe* qui ajoute du bruit en $T$ étapes jusqu'au bruit pur. **Reverse** : le réseau prédit le bruit (ou le *score*) à retirer à chaque étape (DDPM, Ho et al. 2020).

### Score et débruitage
- Apprendre à débruiter revient à estimer le **gradient de la log-densité** (le *score*) — d'où l'équivalence avec les *score-based models* / SDE (Song et al.).

### Diffusion latente
- Diffuser non pas dans l'espace **pixel** mais dans un **espace latent** compressé par un autoencodeur → coût divisé. C'est la base de Stable Diffusion. Le débruiteur fut un **U-Net**, de plus en plus un [[Transformer architectures|Transformer]] (DiT, backbone de SD3 et Sora).

### Conditionnement et guidance
- On conditionne par un **texte** (via les [[embeddings]] d'un encodeur type CLIP/T5) injecté par cross-attention. La **classifier-free guidance** amplifie l'effet du prompt au prix de la diversité.

## Les maths, simplement

- Forward : $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1-\bar\alpha_t}\,\epsilon$, avec $\epsilon \sim \mathcal{N}(0, I)$ — interpolation bruitée entre la donnée $x_0$ et le bruit pur.
- Perte : $\mathcal{L} = \mathbb{E}_{t,x_0,\epsilon}\big[\lVert \epsilon - \epsilon_\theta(x_t, t)\rVert^2\big]$ — le réseau **prédit le bruit injecté**. Dérivée d'une borne variationnelle (ELBO), elle se réduit à une simple **MSE de débruitage** ; maximiser l'ELBO revient à minimiser une [[KL divergence]] entre trajectoires forward et reverse.

## En pratique

- Échantillonner = itérer le débruiteur **20 à 1000 fois** → coûteux. Les samplers rapides (DDIM, DPM-Solver) et la [[Distillation]] (consistency models, variantes *turbo*) ramènent à quelques pas.
- Domine l'[[Image generation|image]] et la [[Video generation|vidéo]] ; concurrence les modèles **autorégressifs** (génération par tokens) et les anciens **[[GANs|GAN]]** (moins divers, instables).
- Qualité ↔ vitesse ↔ fidélité au prompt se règlent par le **nombre de pas** et l'**échelle de guidance** ; la [[Quantization]] allège le déploiement des gros débruiteurs.

## Approches voisines & alternatives

- [[Image generation]] — principale application : la diffusion est le moteur de la plupart des générateurs d'images.
- [[Video generation]] — extension spatio-temporelle de la diffusion (diffusion transformer sur patchs *spacetime*).
- [[Transformer architectures]] — backbone moderne du débruiteur (DiT), en remplacement du U-Net.
- [[KL divergence]] — la borne variationnelle qui justifie l'objectif de débruitage.
- [[Distillation]] — réduit le nombre de pas d'échantillonnage (consistency / turbo).
- [[GANs]] — la famille générative que la diffusion a supplantée sur l'image (jeu adversarial unique vs débruitage itératif) ; encore utilisée en super-résolution et comme perte adversariale dans la distillation *turbo*.

## Pour aller plus loin

- Ho, Jain & Abbeel (2020) — *Denoising Diffusion Probabilistic Models* (DDPM).
- Song et al. (2021) — *Score-Based Generative Modeling through SDEs*.
- Rombach et al. (2022) — *High-Resolution Image Synthesis with Latent Diffusion Models* (Stable Diffusion).
- Peebles & Xie (2023) — *Scalable Diffusion Models with Transformers* (DiT).
