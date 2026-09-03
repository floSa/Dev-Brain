---
role: notion
nom: Small Language Models
alias: [SLM, petits modèles de langage, small language model, modèles compacts, edge LLM, on-device LLM]
categorie: llm/modele
domaines: [ai-eng]
tags: [small-language-model, scaling-laws, llm, local-llm]
---

# Small Language Models

## Aperçu

- Les SLM sont des modèles de langage **compacts** (≈ 0,1 à ~10 B paramètres) pensés pour tourner à **bas coût**, en **local** ou sur **edge / appareil**, avec une latence faible.
- Leur pari : un petit modèle **sur-entraîné** sur beaucoup de données de qualité (et bien post-entraîné) suffit pour une tâche ciblée, sans le coût d'un modèle frontière.

## Concepts clés

### Pourquoi ça marche
- **Sur-entraînement** (inference-optimal, cf. [[Scaling laws]]) : entraîner bien au-delà de 20 tokens/param compense la petite taille.
- **Données de qualité** : curation soignée et **donnée synthétique** (approche « textbooks », famille Phi).
- **Distillation** depuis un grand modèle et **post-training** soigné (SFT, préférences) transfèrent des capacités.

### Ce qu'on y gagne
- Coût et énergie réduits, **latence** faible, **confidentialité** (données qui ne quittent pas l'appareil), fonctionnement **hors-ligne**, fine-tuning abordable.

### Ce qu'on y perd
- Moins de **connaissances** encyclopédiques, raisonnement complexe plus fragile, fenêtre de contexte souvent plus courte. À réserver à des tâches **cadrées**.

### Exemples de familles
- Phi (Microsoft), Gemma (Google), Qwen (petites tailles), Llama 3.2 1B/3B, SmolLM (Hugging Face). Souvent **quantizés** (GGUF, AWQ) pour l'edge.

## Les maths, simplement

- Levier mémoire : un modèle de $N$ paramètres en précision $p$ octets occupe $\approx N \times p$ octets de poids (ex. 3 B en 4-bit $\approx$ 1,5 Go) → tient sur un laptop ou un mobile. La [[Inference optimization|quantization]] divise d'autant l'empreinte.
- Choix d'échelle : à budget d'inférence fixe, on préfère le couple $(N\downarrow,\ D\uparrow)$ — petit modèle, beaucoup de tokens — plutôt que le point compute-optimal de [[Scaling laws]].

## En pratique

- Exécuter en local : [[Ollama]] (le plus simple), [[llama.cpp]] (CPU / GPU grand public, GGUF), [[vLLM]] (serving à débit si plusieurs requêtes).
- Spécialiser par **fine-tuning léger** ([[PEFT]]) plutôt que d'attendre la polyvalence d'un grand modèle.
- Construire un **petit jeu d'éval** sur la tâche cible : un SLM bien choisi peut égaler un grand modèle sur un périmètre étroit, pas en général.
- Combiner avec un routage : SLM par défaut, escalade vers un grand modèle sur les cas durs (*routing and cascading*, à créer).

## Approches voisines & alternatives

- [[Scaling laws]] — les SLM appliquent la logique **inference-optimal** (sur-entraînement).
- [[PEFT]] — fine-tuning abordable pour spécialiser un SLM.
- [[Distillation]] — fabrique un petit modèle à partir d'un grand.
- [[Quantization]] — réduit encore l'empreinte pour l'edge.
- [[Reasoning models]] — pari inverse : dépenser plus à l'inférence plutôt que viser le compact.
- Runtimes locaux : [[Ollama]], [[llama.cpp]], [[LM Studio]].
- Modèle spécialisé pour l'edge : [[needle]] — 45 M paramètres en 2 bits, dédié à l'appel d'outils et à l'extraction structurée.
- Choix du modèle selon la machine : [[llmfit]] — classe les modèles par tenue en mémoire, vitesse estimée, qualité et contexte, sur le matériel réellement disponible.

## Pour aller plus loin

- Gunasekar et al. (2023) — *Textbooks Are All You Need* (Phi).
- Rapports techniques Gemma, Qwen, Llama 3.2, SmolLM.
