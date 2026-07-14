---
galaxie: wiki
type: concept
nom: Decoding strategies
alias: [stratégies de décodage, décodage, sampling, greedy, top-k, top-p, nucleus sampling, beam search, température]
categorie: concept/llm
domaines: [ai-eng]
tags: [decoding, llm, nlp]
---

# Decoding strategies

## Aperçu

- À chaque pas, le modèle produit une **distribution de probabilité** sur le prochain token ; la stratégie de décodage **choisit** ce token à partir de cette distribution.
- Même modèle, même prompt : le décodage seul fait basculer la sortie du **déterministe et plat** au **varié et créatif** (ou incohérent).

## Concepts clés

### Déterministe : greedy et beam search
- **Greedy** : prendre l'argmax à chaque pas. Rapide, reproductible, mais myope et répétitif.
- **Beam search** : garder les $b$ meilleures séquences partielles. Meilleur pour la traduction ; sur du texte ouvert, tend vers des réponses fades et génériques.

### Échantillonnage : température, top-k, top-p
- **Température** $T$ : aplatit ($T>1$) ou pique ($T<1$) la distribution avant tirage.
- **Top-k** : ne tirer que parmi les $k$ tokens les plus probables.
- **Top-p (nucleus)** : ne garder que le plus petit ensemble de tokens dont la masse cumulée atteint $p$ — taille de candidat **adaptative** au contexte.

### Pénalités
- *Repetition / frequency / presence penalty* : abaisser la probabilité des tokens déjà émis pour casser les boucles.

### Décodage contraint
- Masquer à chaque pas les tokens interdits par une grammaire / un schéma → sortie **garantie valide** : c'est le [[Constrained decoding|décodage contraint]], moteur des [[Structured outputs|sorties structurées]].

## Les maths, simplement

- Softmax à température : $p_i = \dfrac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$, où $z_i$ est le logit du token $i$. $T \to 0$ → greedy ; $T \to \infty$ → uniforme.
- Top-p : choisir le plus petit ensemble $\mathcal{S}$ tel que $\sum_{i \in \mathcal{S}} p_i \ge p$, puis renormaliser et tirer dans $\mathcal{S}$.

## En pratique

- **Tâches factuelles / code / extraction** → température basse (voire greedy) pour la stabilité et la reproductibilité.
- **Créatif / brainstorming** → température modérée + top-p (~0,9) ; combiner les deux plutôt que pousser la seule température.
- Fixer une **seed** quand on veut des résultats reproductibles malgré l'échantillonnage.
- Pour une sortie machine-parseable, préférer le **décodage contraint** ([[Structured outputs]]) à un post-traitement fragile.

## Approches voisines & alternatives

- [[Tokenization]] — le décodage choisit des tokens dans le vocabulaire issu de la tokenisation.
- [[Perplexity]] — mesure la qualité de la distribution prédite ; le décodage, lui, exploite cette distribution.
- [[Structured outputs]] — applique un décodage **contraint** par un schéma.
- [[Constrained decoding]] — le mécanisme détaillé (compilation en automate, masquage, *token healing*) et ses bibliothèques ([[Dev/Services/Outlines|Outlines]], [[Dev/Services/Guidance|Guidance]]).
- [[Server-Sent Events & streaming LLM]] — le décodage token par token **alimente** le flux streamé au client.
- *Speculative decoding* (à créer) — accélère la génération sans changer la distribution cible.

## Pour aller plus loin

- Holtzman et al. (2020) — *The Curious Case of Neural Text Degeneration* (introduit le nucleus sampling).
- Documentation des paramètres `temperature`, `top_p`, `top_k`, pénalités des API LLM.
