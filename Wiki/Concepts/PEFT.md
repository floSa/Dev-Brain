---
galaxie: wiki
type: concept
nom: PEFT
alias: [parameter-efficient fine-tuning, fine-tuning paramétriquement efficace, adapters]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [fine-tuning, llm]
---

# PEFT

## Aperçu

- **Fine-tuning paramétriquement efficace** : adapter un grand modèle en n'entraînant qu'une **petite fraction** de paramètres, les poids de base restant **gelés**.
- Rend le fine-tuning ([[SFT]], [[RLHF and DPO]]) accessible sur un seul GPU : moins de mémoire, artefacts légers (quelques Mo), et plusieurs adaptateurs interchangeables sur un même modèle.

## Concepts clés

### LoRA et QLoRA — la méthode-phare
- **[[LoRA et QLoRA]]** : apprendre une **mise à jour de rang faible** $\Delta W = B A$ sur un modèle gelé ; QLoRA la combine avec un modèle de base quantifié en 4 bits ([[Quantization]]). La famille PEFT dominante en pratique — détails, maths et leviers sur la page dédiée.

### Autres familles
- **Adapters** (couches insérées), **prefix / prompt tuning** (vecteurs entraînables ajoutés en entrée), **(IA)³**. LoRA domine en pratique par son rapport simplicité / qualité.

### Pourquoi ça marche
- L'adaptation à une tâche vit dans un sous-espace de **faible dimension intrinsèque** : une mise à jour de rang faible suffit à capter l'essentiel, d'où une perte minime face au full fine-tuning.

## Les maths, simplement

- Idée commune à toutes les familles : remplacer l'apprentissage des $d^2$ poids d'une matrice par un **petit nombre de paramètres additionnels** (rang faible, vecteurs préfixes, couches insérées), le reste étant gelé.
- Le cas LoRA ($\Delta W = \tfrac{\alpha}{r} B A$, $2dr$ paramètres au lieu de $d^2$) est détaillé dans [[LoRA et QLoRA]].

## En pratique

- **Défaut raisonnable** pour tout fine-tuning de LLM : [[LoRA et QLoRA|LoRA]] (ou QLoRA si la mémoire est serrée). Le full fine-tuning n'est justifié que si la qualité plafonne. Leviers de réglage ($r$, $\alpha$, couches ciblées) sur la page dédiée.
- Garder un **adaptateur par tâche / client** et les charger à la volée sur le même modèle de base — économie de stockage et de déploiement.
- Outils : la lib **`peft`** de [[Dev/Services/HuggingFace|HuggingFace]] (+ `bitsandbytes` pour la 4-bit), sur [[Dev/Services/PyTorch|PyTorch]] ; pilotée par [[Dev/Services/TRL|TRL]], [[Dev/Services/Axolotl|Axolotl]] et [[Dev/Services/LLaMA-Factory|LLaMA-Factory]], et accélérée par [[Dev/Services/Unsloth|Unsloth]].
- PEFT est le **comment** ; [[SFT]] et [[RLHF and DPO]] sont le **quoi** qu'on entraîne avec.

## Approches voisines & alternatives

- [[SFT]] — l'objectif d'entraînement le plus courant exécuté en PEFT.
- [[RLHF and DPO]] — l'alignement se fait aussi en LoRA pour rester abordable.
- [[RL for LLMs]] — le RL de post-training (RLHF, GRPO) tourne aussi en LoRA pour rester accessible.
- [[LoRA et QLoRA]] — la méthode PEFT la plus citée : adaptation de rang faible, avec ou sans base quantifiée 4 bits.
- [[Quantization]] — la 4-bit qui rend QLoRA possible ; sert aussi à l'inférence légère.
- [[Dev/Services/HuggingFace|HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes.

## Pour aller plus loin

- [[LoRA et QLoRA]] — la page dédiée porte les références fondatrices (Hu et al. 2021, Dettmers et al. 2023).
- Houlsby et al. (2019) — *Parameter-Efficient Transfer Learning for NLP* (adapters).
- Documentation de la bibliothèque `peft` (HuggingFace).
