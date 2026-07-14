---
galaxie: wiki
type: concept
nom: Speculative decoding
alias: [décodage spéculatif, speculative sampling, échantillonnage spéculatif, draft model, modèle brouillon, EAGLE, Medusa]
categorie: concept/llm
domaines: [ai-eng]
tags: [inference-optimization, decoding, llm, inference]
---

# Speculative decoding

## Aperçu

- Le décodage spéculatif **accélère la génération** : un modèle rapide (brouillon) propose plusieurs tokens d'avance, que le grand modèle **vérifie en une seule passe**. Typiquement **2–3×** plus rapide.
- Propriété clé : la sortie est **distributionnellement identique** à celle du grand modèle seul — accélération **sans perte de qualité**.

## Concepts clés

### Brouillon puis vérification
- Un **drafter** (petit modèle, têtes auxiliaires, ou n-grammes) génère $k$ tokens candidats. Le **modèle cible** les évalue **en parallèle** (un seul forward), accepte le plus long préfixe cohérent et rejette le reste.
- Le gain vient du régime *memory-bound* du decode : vérifier $k$ tokens d'un coup coûte presque autant qu'en générer un, car le goulot est la lecture des poids, pas le calcul (cf. [[Inference optimization]]).

### Acceptation et correction
- Un critère d'acceptation (rejection sampling) garantit que la distribution finale est **exactement** celle du modèle cible. Le nombre de tokens acceptés par passe (*acceptance length*) détermine l'accélération réelle.

### Familles de méthodes
- **Draft model séparé** : un petit modèle de la même famille (formulation d'origine, Leviathan / Chen 2023).
- **Medusa** : des têtes de décodage supplémentaires greffées sur le modèle, pas de second modèle ; vérification en arbre.
- **EAGLE (1 → 3)** : prédiction au niveau des *features* plutôt que des tokens ; devenu le **standard de fait** (2025), meilleurs taux d'acceptation.
- **Self-speculative / n-gram / prompt lookup** : brouillon tiré du modèle lui-même ou du contexte, sans entraînement.

## Les maths, simplement

- Accélération $\approx$ *acceptance length* $\alpha$ (tokens acceptés par passe), atténuée par le surcoût du brouillon : plus $\alpha$ est élevé, plus le gain approche $\alpha$. Si le brouillon vise mal (peu accepté), le gain s'effondre, voire devient négatif.
- Acceptation par rejection sampling : accepter le token brouillon $x$ avec probabilité $\min\!\big(1,\ \tfrac{p_{\text{cible}}(x)}{q_{\text{brouillon}}(x)}\big)$, sinon rééchantillonner sur la distribution résiduelle → la distribution finale égale $p_{\text{cible}}$.

## En pratique

- Gain maximal sur les sorties **prévisibles** (code, texte structuré) où le brouillon vise juste ; faible sur du texte très entropique.
- Le brouillon doit être **bien plus rapide** que la cible et **aligné** avec elle (même famille / tokenizer).
- Activable nativement dans les runtimes : [[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]], [[Dev/Services/TGI|TGI]] et [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] supportent draft model et/ou EAGLE/Medusa.
- N'améliore **pas** le *time-to-first-token* (prefill) : c'est une optimisation du **decode**.

## Approches voisines & alternatives

- [[Inference optimization]] — le décodage spéculatif en est un cas ; partage le régime memory-bound du decode.
- [[Decoding strategies]] — le spéculatif change *la vitesse* de génération, pas le choix du token (distribution inchangée).
- Accélération **sans** spéculation : [[Inference optimization|continuous batching, KV-cache]], *Quantization* (à créer, `concept/dl`).

## Pour aller plus loin

- Leviathan et al. (2023, Google) — *Fast Inference from Transformers via Speculative Decoding*.
- Chen et al. (2023, DeepMind) — *Accelerating Large Language Model Decoding with Speculative Sampling*.
- Cai et al. (2024) — *Medusa* ; Li et al. (2024–2025) — *EAGLE / EAGLE-3*.
