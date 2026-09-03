---
role: hub
nom: Modèles de langage
pitch: Ce qu'est un modèle de langage avant toute application — ce qu'il lit, ce qu'il produit, ce que sa taille achète.
domaines: [ai-eng, ml-eng]
tags: [tokenization, decoding, scaling-laws, small-language-model, reasoning]
---

# Modèles de langage

> Ce qu'est un modèle de langage avant toute application — ce qu'il lit, ce qu'il produit, ce que sa taille achète.

## Ce qu'il faut comprendre

- Ce dossier est le seul du domaine qui **ne construit rien**. Les autres servent le modèle, l'ajustent ou l'assemblent ; ici on décrit l'objet. C'est là qu'on va quand un comportement surprend et qu'aucune couche applicative ne l'explique.
- **Un modèle ne voit que des tokens**, et une bonne part des surprises d'usage vient de là : [[Tokenization]] explique pourquoi un modèle compte mal les lettres d'un mot, pourquoi une facture n'est pas proportionnelle au nombre de mots, et pourquoi la même phrase coûte plus cher dans une langue que dans une autre.
- **À modèle et prompt constants, le décodage seul change la sortie** — du plat et déterministe au varié et incohérent. [[Decoding strategies]] est le réglage le moins cher du domaine, et le plus souvent oublié.
- La qualité **intrinsèque** se mesure par la [[Perplexity]] : utile pour comparer deux modèles sur un corpus, inutile pour juger une application. L'éval d'un produit est extrinsèque et vit dans [[Évaluation]].
- **Les lois d'échelle décident de l'économie du domaine.** [[Scaling laws]] dit ce que paramètres, données et compute achètent, et permet de prédire un grand entraînement depuis de petits. Les deux classes de modèles nées de ce compromis tirent dans des directions opposées : [[Small Language Models]] sur-entraîne petit pour tenir en local et à bas coût, [[Reasoning models]] dépense au contraire davantage **au moment de répondre**.
- **Un modèle de fondation ne se limite pas au texte, et c'est le même objet qu'on décrit.** [[Vision Language Models]] branche un encodeur visuel sur un LLM par un projecteur : l'image devient des tokens, et tout ce que dit ce dossier — tokenisation, décodage, lois d'échelle — continue de s'appliquer. Ce qu'on fait ensuite des pixels eux-mêmes (détecter, segmenter, suivre) est de l'autre côté, dans [[Vision]].
- Choisir un modèle est donc un arbitrage à trois branches — taille, coût d'inférence, difficulté de la tâche — et non un classement. [[llmfit]] répond à la version matérielle de la question, [[LLM benchmarks]] à sa version qualité.

## Choisir

- Comprendre un coût, une limite de fenêtre ou un comptage aberrant → [[Tokenization]].
- Des sorties trop répétitives, ou au contraire incohérentes → [[Decoding strategies]].
- Comparer deux modèles sur un corpus, hors de toute tâche → [[Perplexity]].
- Dimensionner un entraînement, ou comprendre pourquoi plus gros n'aide plus → [[Scaling laws]].
- Faire tourner en local, sur appareil contraint, ou à très bas coût → [[Small Language Models]].
- Des tâches à plusieurs étapes où la justesse prime sur la latence → [[Reasoning models]].
- Faire tourner concrètement l'un de ces modèles → [[Runtimes]] ; l'ajuster → [[Fine-tuning]].

<!-- AUTO:START -->
### Notions
- [[Decoding strategies]] — domaines : ai-eng
- [[Perplexity]] — domaines : ai-eng
- [[Reasoning models]] — domaines : ai-eng
- [[Scaling laws]] — domaines : ai-eng, ml-eng
- [[Small Language Models]] — domaines : ai-eng
- [[Tokenization]] — domaines : ai-eng
- [[Vision Language Models]] — domaines : ml-eng, ai-eng
<!-- AUTO:END -->
