---
role: hub
nom: Modèles de langage
pitch: Ce qu'est un modèle de langage avant toute application — ce qu'il lit, ce qu'il produit, ce que sa taille achète.
domaines: [ai-eng, ml-eng]
tags: [tokenization, decoding, scaling-laws, small-language-model, reasoning, llm]
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
- **Choisir une famille à poids ouverts se joue sur la licence avant les classements.** [[Qwen]], [[Mistral]], [[Gemma]] et [[gpt-oss]] ne se départagent pas d'abord par leurs scores : la licence se lit **dépôt par dépôt** et change d'une génération ou d'une taille à l'autre, ce que [[Licences de modèles open weights]] explique et [[Comparatif - Modèles de langage open weights]] tranche pour une ESN qui héberge chez un client.
- Choisir un modèle est donc un arbitrage à trois branches — taille, coût d'inférence, difficulté de la tâche — et non un classement. [[llmfit]] répond à la version matérielle de la question, [[LLM benchmarks]] à sa version qualité.

## Choisir

- Comprendre un coût, une limite de fenêtre ou un comptage aberrant → [[Tokenization]].
- Des sorties trop répétitives, ou au contraire incohérentes → [[Decoding strategies]].
- Comparer deux modèles sur un corpus, hors de toute tâche → [[Perplexity]].
- Dimensionner un entraînement, ou comprendre pourquoi plus gros n'aide plus → [[Scaling laws]].
- Faire tourner en local, sur appareil contraint, ou à très bas coût → [[Small Language Models]].
- Des tâches à plusieurs étapes où la justesse prime sur la latence → [[Reasoning models]].
- Livrer un modèle à poids ouverts chez un client, ou savoir ce que sa licence permet → [[Licences de modèles open weights]], puis [[Comparatif - Modèles de langage open weights]].
- Une famille précise, sa licence lue à la source et sa VRAM → [[Qwen]] · [[Mistral]] · [[Gemma]] · [[gpt-oss]].
- Faire tourner concrètement l'un de ces modèles → [[Runtimes]] ; l'ajuster → [[Fine-tuning]].
- Une réponse plausible mais fausse, et savoir si la cause est le modèle, le contexte ou l'évaluation → [[Hallucinations des LLM]].
- Une fenêtre annoncée à plusieurs centaines de milliers de jetons : ce qu'elle coûte en mémoire et ce qu'elle vaut à l'usage → [[Contexte long]].

<!-- AUTO:START -->
### Notions
- [[Contexte long]] — domaines : ai-eng, ml-eng
- [[Decoding strategies]] — domaines : ai-eng
- [[Hallucinations des LLM]] — domaines : ai-eng
- [[Licences de modèles open weights]] — domaines : ai-eng, ml-eng
- [[Perplexity]] — domaines : ai-eng
- [[Reasoning models]] — domaines : ai-eng
- [[Scaling laws]] — domaines : ai-eng, ml-eng
- [[Small Language Models]] — domaines : ai-eng
- [[Tokenization]] — domaines : ai-eng
- [[Vision Language Models]] — domaines : ml-eng, ai-eng

### Briques
- [[Gemma]] — Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use.
- [[gpt-oss]] — Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire.
- [[Mistral]] — Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement.
- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo.

### Comparatifs
- [[Comparatif - Modèles de langage open weights]]
<!-- AUTO:END -->
