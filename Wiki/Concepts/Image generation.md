---
galaxie: wiki
type: concept
nom: Image generation
alias: [text-to-image, T2I, génération d'images, Stable Diffusion, DALL-E, Midjourney, FLUX, inpainting]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [generative-model, image-generation, diffusion, multimodal]
---

# Image generation

## Aperçu

- Synthèse d'images à partir d'une **description** (text-to-image) ou d'une autre image (image-to-image, *inpainting*, *outpainting*). La sortie est une image cohérente avec le prompt.
- Idée clé : **aligner** un espace de texte et un espace d'image, puis **échantillonner** une image plausible conditionnée par le texte.

## Concepts clés

### Moteur : la diffusion latente
- L'écrasante majorité des générateurs actuels sont des [[Diffusion models|modèles de diffusion]] **latents** : débruitage itératif dans un espace compressé, conditionné par le prompt via cross-attention.

### Conditionnement texte
- Un **encodeur de texte** (CLIP, T5) produit des [[embeddings]] qui guident le débruitage. La *classifier-free guidance* dose l'**adhérence au prompt** (au prix de la diversité).

### Familles de modèles
- **Open-weight** : Stable Diffusion 3.5, FLUX.1/FLUX.2 (Black Forest Labs) — fine-tunables, auto-hébergeables. **Propriétaires** : DALL·E 3, Midjourney v7, Imagen 4 (Google). Empiriquement : FLUX/SD en photoréalisme, Midjourney en style, Imagen en **rendu de texte** dans l'image.

### Contrôle fin
- ControlNet (pose, profondeur), LoRA ([[PEFT]]) pour styles/sujets, *inpainting/outpainting* pour l'édition régionale.

## Les maths, simplement

- Objectif hérité de la diffusion **conditionnelle** : $\mathcal{L} = \mathbb{E}\big[\lVert \epsilon - \epsilon_\theta(x_t, t, c)\rVert^2\big]$, où $c$ est l'embedding du prompt — débruiter *en fonction du texte*.
- Guidance : $\hat\epsilon = \epsilon_\theta(x_t,t,\varnothing) + s\,[\epsilon_\theta(x_t,t,c) - \epsilon_\theta(x_t,t,\varnothing)]$ — l'échelle $s>1$ pousse l'image vers le prompt.

## En pratique

- **Évaluation difficile** : FID (réalisme/diversité), CLIPScore (adhérence au prompt), et de plus en plus les **préférences humaines**. Le « prompt qui marche » reste empirique.
- Arbitrages : **open-weight** (SD, FLUX) pour fine-tuner et héberger soi-même ; **API propriétaire** pour la qualité immédiate sans infra. Coût ↔ vitesse via le nombre de pas et les samplers rapides.
- Risques : biais des données, deepfakes, droits d'auteur. Le **watermarking** (SynthID) et les filtres de sécurité sont devenus standards.

## Approches voisines & alternatives

- [[Diffusion models]] — le moteur génératif sous-jacent de la quasi-totalité des générateurs d'images.
- [[Video generation]] — même socle, étendu au temps : une image animée est une vidéo très courte.
- [[Vision Language Models]] — voie inverse (image → texte, *comprendre*) vs ici (texte → image, *générer*) ; réunies dans les modèles « omni ».
- [[GANs]] — l'approche générative **historique** (jeu adversarial), supplantée par la diffusion mais encore utile en super-résolution et génération rapide.
- [[PEFT]] — LoRA adapte un générateur à un style/sujet sans tout réentraîner.
- [[Vision par ordinateur]] — la synthèse d'images est le **versant génératif** de la vision.

## Pour aller plus loin

- Rombach et al. (2022) — *Latent Diffusion Models* (Stable Diffusion).
- Ramesh et al. (2022) — *Hierarchical Text-Conditional Image Generation with CLIP Latents* (DALL·E 2).
- Esser et al. (2024) — *Scaling Rectified Flow Transformers for High-Resolution Image Synthesis* (Stable Diffusion 3).
