---
galaxie: wiki
type: concept
nom: Vision Language Models
alias: [VLM, vision-language models, modèles vision-langage, multimodal LLM, MLLM, image-text]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [vision-language, multimodal, transformers, llm]
---

# Vision Language Models

## Aperçu

- Modèles qui prennent en entrée des **images** (parfois de la vidéo) **et** du texte, raisonnent dessus et produisent du **texte** : description, VQA (questions sur image), OCR, agents qui « voient » une interface.
- Idée clé : **brancher un encodeur visuel sur un LLM** via un projecteur, pour que le LLM traite des **tokens d'image** comme des tokens de texte.

## Concepts clés

### Architecture en trois blocs
- (1) un **encodeur visuel** ([[Vision Transformers (ViT)|ViT]] type [[Modèles de fondation vision|CLIP/SigLIP]]) transforme l'image en tokens ; (2) un **projecteur** (souvent un MLP 2 couches) aligne ces tokens sur l'espace d'embedding du LLM ; (3) le **LLM** raisonne et génère le texte. C'est le schéma de **LLaVA**.

### Alignement vision ↔ langage
- Le projecteur apprend la correspondance entre l'espace **visuel** (p. ex. 1408-d) et l'espace du **LLM** (p. ex. 4096-d). Entraînement en deux temps : **pré-alignement** (paires image-légende) puis [[SFT|fine-tuning supervisé]] sur **instructions multimodales**.

### Encodeurs et compression de tokens
- **SigLIP 2** est devenu l'encodeur de référence (Qwen3-VL, Gemma 3). Une image produit **beaucoup de tokens** → compression (merger de Qwen, *token pruning*) pour tenir le budget de contexte.

### Modèles
- LLaVA (référence open-weight), Qwen-VL, GPT-4o, Gemini, Claude — la plupart des grands LLM sont aujourd'hui **nativement multimodaux**.

## Les maths, simplement

- Séquence d'entrée du LLM : $[\,\text{proj}(E_v(\text{image}))\;;\;E_t(\text{texte})\,]$ — les tokens d'image **projetés** sont concaténés aux tokens de texte, puis traités par l'[[Self-attention|attention]] habituelle.
- Le projecteur $\text{proj}: \mathbb{R}^{d_v}\!\to\!\mathbb{R}^{d_{\text{LLM}}}$ est la seule pièce qui « parle les deux langues » ; c'est lui qu'on entraîne en priorité.

## En pratique

- Usages : **VQA**, extraction de documents / OCR, description d'images, **agents GUI** (lire un écran), modération. Évaluation par benchmarks dédiés (MMMU, DocVQA…).
- Pièges : **hallucination visuelle** (décrire ce qui n'est pas là), coût en tokens des hautes résolutions, sensibilité à la qualité de l'encodeur.
- Dualité génératif : un VLM **comprend** l'image (image → texte) là où l'[[Image generation|image generation]] la **produit** (texte → image) ; les modèles « omni » réunissent les deux.

## Approches voisines & alternatives

- [[Transformer architectures]] — le LLM et l'encodeur ViT sont tous deux des Transformers.
- [[Modèles de fondation vision]] — l'encodeur visuel du VLM **est** une fondation vision (CLIP / SigLIP) branchée sur le LLM.
- [[embeddings]] — le projecteur aligne les embeddings visuels sur ceux du langage.
- [[Image generation]] — tâche **duale** : générer une image vs la comprendre.
- [[SFT]] / [[PEFT]] — l'instruction-tuning multimodal (et LoRA) adapte le LLM à la vision.
- [[Self-attention]] — le mécanisme qui mêle tokens d'image et de texte.
- [[Vision par ordinateur]] — le champ d'ensemble ; l'encodeur visuel d'un VLM (ViT) prolonge l'héritage des [[CNN]] et des [[Architectures CNN]].

## Pour aller plus loin

- Liu et al. (2023) — *Visual Instruction Tuning* (LLaVA).
- Radford et al. (2021) — *Learning Transferable Visual Models from Natural Language Supervision* (CLIP).
- Bai et al. (2025) — *Qwen2.5-VL Technical Report*.
