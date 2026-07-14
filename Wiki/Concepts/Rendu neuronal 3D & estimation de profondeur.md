---
galaxie: wiki
type: concept
nom: Rendu neuronal 3D & estimation de profondeur
alias: [NeRF, neural radiance fields, 3D Gaussian Splatting, 3DGS, gaussian splatting, rendu neuronal, novel view synthesis, estimation de profondeur, depth estimation, MiDaS, DPT, Depth Anything]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [neural-rendering, depth-estimation, computer-vision, deep-learning]
---

# Rendu neuronal 3D & estimation de profondeur

## Aperçu

- Deux façons de **percevoir la 3D depuis des images 2D**. (1) **Rendu neuronal** : reconstruire une scène depuis des photos multi-vues et **synthétiser de nouvelles vues** (NeRF, 3D Gaussian Splatting). (2) **Estimation de profondeur** : prédire la **distance par pixel** depuis une (ou plusieurs) image(s).
- Point commun : retrouver la **géométrie** d'une scène ; la profondeur alimente souvent la reconstruction, et inversement.

## Concepts clés

### NeRF — champ de radiance neuronal
- Un **MLP** encode la scène comme une fonction *(position 3D + direction de vue) → (couleur + densité)*. On rend une image par **intégration volumique** le long des rayons de la caméra, et on entraîne le MLP à **reconstruire** les vues d'entrée. Photoréaliste, mais **lent** (entraînement long, rendu de l'ordre de la seconde par image). Mildenhall et al., 2020.

### 3D Gaussian Splatting — représentation explicite
- La scène = **nuage de gaussiennes 3D** (position, covariance, couleur, opacité), rendu par **rasterisation différentiable** (projection des gaussiennes sur l'image). **Temps réel** (100+ FPS), entraînement en **minutes** → a largement **supplanté NeRF** en pratique (capture d'objets/scènes). Kerbl et al., SIGGRAPH 2023.

### Estimation de profondeur monoculaire
- Prédire la profondeur depuis **une seule image** — problème mal posé (échelle ambiguë). Modèles de fondation : **MiDaS / DPT** (backbone [[Vision Transformers (ViT)|ViT]]), **Depth Anything V2** (NeurIPS 2024, entraîné sur images synthétiques + pseudo-labels). Profondeur **relative** vs **métrique**. Au-delà du monoculaire : **stéréo** et *multi-view stereo* (MVS).

### Le maillon amont : les poses caméra
- NeRF et 3DGS supposent connues les **poses** des caméras, fournies par *Structure-from-Motion* (COLMAP) — souvent l'étape la plus fragile d'un pipeline 3D.

## Les maths, simplement

- Rendu volumique (NeRF) : la couleur d'un rayon $r$ est $C(r) = \int T(t)\,\sigma(t)\,c(t)\,dt$, avec la **transmittance** $T(t) = \exp\!\big(-\int_0^t \sigma(s)\,ds\big)$ — un point contribue d'autant plus qu'il est dense et peu occulté par ce qui le précède.
- 3DGS : remplace cette intégrale par un **mélange alpha** de gaussiennes 2D projetées, trié par profondeur — la même idée de composition, mais **rasterisée** donc rapide.

## En pratique

- **3DGS** pour la capture temps réel d'objets / scènes (Luma, Polycam, nerfstudio + gsplat) ; **NeRF** reste surtout en recherche et sur les cas où l'on privilégie la qualité hors-ligne.
- **Depth Anything** pour de la profondeur **prête à l'emploi** (robotique, AR, conditionnement *depth* de [[Diffusion models|ControlNet]]) ; intégré à [[Dev/Services/HuggingFace|HuggingFace]] (Transformers).
- Pièges : qualité des poses caméra (SfM), reflets / transparences mal gérés, profondeur **relative** à recaler si l'on veut des mètres.

## Approches voisines & alternatives

- [[Vision par ordinateur]] — le cadre d'ensemble ; ces tâches en sont le versant **géométrique / 3D**.
- [[Vision Transformers (ViT)]] — backbone des estimateurs de profondeur modernes (DPT, Depth Anything).
- [[Modèles de fondation vision]] — Depth Anything est une **fondation** dédiée à la profondeur ; DINOv2 fournit des features denses utiles en 3D.
- [[Diffusion models]] — génération 3D et synthèse de vues récentes s'appuient de plus en plus sur la diffusion (et le conditionnement par profondeur).

## Pour aller plus loin

- Mildenhall et al. (2020) — *NeRF: Representing Scenes as Neural Radiance Fields*.
- Kerbl et al. (2023) — *3D Gaussian Splatting for Real-Time Radiance Field Rendering* (SIGGRAPH).
- Ranftl et al. (2021) — *Vision Transformers for Dense Prediction* (DPT / MiDaS).
- Yang et al. (2024) — *Depth Anything V2* (arXiv 2406.09414).
