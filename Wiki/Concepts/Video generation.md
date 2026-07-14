---
galaxie: wiki
type: concept
nom: Video generation
alias: [text-to-video, T2V, génération de vidéos, Sora, video diffusion, image-to-video]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [generative-model, video-generation, diffusion, multimodal]
---

# Video generation

## Aperçu

- Synthèse de **séquences vidéo** à partir d'un texte (text-to-video), d'une image (image-to-video) ou des deux. Le défi par rapport à l'image : la **cohérence temporelle** — mouvement plausible, objets stables d'une frame à l'autre.
- Idée clé : étendre la [[Image generation|génération d'images]] à la dimension **temporelle**, en traitant la vidéo comme un **volume spatio-temporel** à débruiter d'un bloc.

## Concepts clés

### Diffusion transformer spatio-temporelle
- Les modèles dominants (Sora) sont des [[Diffusion models|modèles de diffusion]] latents dont le débruiteur est un [[Transformer architectures|Transformer]] (DiT) opérant sur des **patchs *spacetime*** — l'attention couvre l'espace **et** le temps.

### Cohérence temporelle
- Le problème central : éviter le scintillement, le *morphing* d'objets, les incohérences physiques. Leviers : attention temporelle, conditionnement par frames de référence, passage à l'échelle.

### Durée, audio, contrôle
- Durées encore **courtes** (Sora 2 ≈ 15 s, Veo ≈ 8 s). Veo 3 génère l'**audio synchronisé** (dialogue, ambiance) dans la même passe. *Image-to-video* et contrôle de caméra pour la production.

### Modèles
- Sora 2 (OpenAI), Veo 3.1 (Google), Kling 3.0, Runway Gen-4, Seedance (ByteDance) — paysage très mouvant fin 2025, avec arrivée de l'audio natif et d'une meilleure physique.

## Les maths, simplement

- Même objectif de débruitage que la diffusion d'images, mais sur un tenseur à **axe temporel** : $x \in \mathbb{R}^{T\times H\times W\times C}$ encodé en latents spatio-temporels, puis débruité conjointement → la cohérence inter-frames émerge de l'attention sur l'axe $T$.
- Coût $\propto$ nombre de patchs *spacetime* : il **explose** avec la durée et la résolution, d'où les latents compressés et les durées limitées.

## En pratique

- Très coûteux à **entraîner et à servir** (un clip = des milliers de patchs débruités sur des dizaines de pas). Réservé à de gros acteurs ; accès surtout par **API**.
- Usages : prototypage créatif, publicité, *b-roll*. Limites : durée, cohérence longue, contrôle précis. Mêmes risques de **deepfake** que l'image (watermarking de rigueur).

## Approches voisines & alternatives

- [[Diffusion models]] — socle génératif, étendu à l'axe temporel.
- [[Image generation]] — cas dégénéré ($T=1$) ; partage les encodeurs de texte et les techniques de guidance.
- [[Transformer architectures]] — l'attention spatio-temporelle qui porte la cohérence du mouvement.

## Pour aller plus loin

- Brooks et al. (2024) — *Video generation models as world simulators* (rapport technique Sora).
- Blattmann et al. (2023) — *Stable Video Diffusion*.
- Ho et al. (2022) — *Video Diffusion Models*.
