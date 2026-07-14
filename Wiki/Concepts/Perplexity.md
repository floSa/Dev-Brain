---
galaxie: wiki
type: concept
nom: Perplexity
alias: [perplexité, PPL]
categorie: concept/llm
domaines: [ai-eng]
tags: [perplexity, llm, model-evaluation, nlp]
---

# Perplexity

## Aperçu

- Mesure **intrinsèque** de la qualité d'un modèle de langue : à quel point il est « surpris » par un texte de référence. **Plus bas = meilleur**.
- S'interprète comme un **facteur de branchement effectif** : le nombre moyen de tokens également plausibles que le modèle hésite à choisir à chaque pas.

## Concepts clés

### Lien avec la vraisemblance
- La perplexité est l'**exponentielle de l'entropie croisée** moyenne par token, c'est-à-dire de la log-vraisemblance négative moyenne. Minimiser la perte d'entraînement, c'est minimiser la perplexité.

### Ce qu'elle dit, ce qu'elle ne dit pas
- Bon proxy pour suivre un **pré-entraînement** ou comparer des modèles sur un même corpus.
- Mais une faible perplexité **ne garantit pas** l'utilité : un modèle peu perplexe peut rester inexact, biaisé ou peu serviable. Elle ne mesure pas la qualité **en aval** (tâches réelles).

### Conditions de comparabilité
- Comparable **uniquement** à tokenizer et vocabulaire identiques, sur le **même texte**. Deux modèles aux tokenisations différentes ont des perplexités non comparables (cf. perplexité normalisée par octet/caractère pour contourner).

## Les maths, simplement

- $\mathrm{PPL} = \exp\!\Big(-\dfrac{1}{N}\sum_{i=1}^{N} \log p(t_i \mid t_{<i})\Big)$ : exponentielle de la log-vraisemblance négative moyenne sur les $N$ tokens.
- C'est exactement $\exp(H)$ où $H$ est l'entropie croisée moyenne (en nats) entre la distribution réelle et celle du modèle — d'où le lien direct avec la perte d'entraînement.

## En pratique

- Suivre la perplexité sur un **jeu de validation tenu à l'écart** pendant le pré-entraînement, et pour détecter une **dérive de domaine** (texte hors distribution → PPL qui monte).
- Ne jamais comparer des PPL issues de **tokenizers différents** sans normalisation.
- Pour juger une application LLM réelle, compléter par des évaluations **en aval** ([[LLM eval metrics]], [[LLM-as-judge]]) : la PPL seule est insuffisante.

## Approches voisines & alternatives

- [[Tokenization]] — la perplexité se calcule par token, donc dépend du tokenizer choisi.
- [[Decoding strategies]] — exploite la distribution dont la perplexité mesure la qualité.
- [[Cross-entropy]] — la perplexité en est l'exponentielle ; même information, autre échelle.
- [[Shannon entropy]] — l'entropie dont la perplexité est l'exponentielle ; facteur de branchement effectif.
- Alternative pour évaluer un LLM applicatif : métriques **extrinsèques** (exactitude sur tâche, jugement humain ou LLM-juge) plutôt qu'intrinsèques.

## Pour aller plus loin

- Jurafsky & Martin — *Speech and Language Processing*, chapitre modèles de langue (définition de la perplexité).
- Documentation `evaluate` / HuggingFace sur le calcul de la perplexité d'un modèle causal.
