---
galaxie: wiki
type: concept
nom: Scaling laws
alias: [lois d'échelle, loi d'échelle, scaling law, Chinchilla, Kaplan, compute-optimal]
categorie: concept/llm
domaines: [ai-eng, ml-eng]
tags: [scaling-laws, llm, deep-learning]
---

# Scaling laws

## Aperçu

- Les lois d'échelle décrivent comment la **perte** d'un modèle décroît, de façon prévisible (loi de puissance), quand on augmente trois ressources : **paramètres** $N$, **données** $D$, **compute** $C$.
- Conséquence pratique : on peut **prédire** la performance d'un grand entraînement à partir de petits, et **allouer** un budget de compute de façon optimale.

## Concepts clés

### Loi de puissance
- La perte suit approximativement $L(X) \approx L_\infty + (X_0 / X)^{\alpha}$ : des **rendements décroissants** mais réguliers et extrapolables. Pas de seuil magique, une droite sur échelle log-log.

### Kaplan (2020) vs Chinchilla (2022)
- **Kaplan et al. (OpenAI, 2020)** : à compute fixe, privilégier la **taille du modèle**. A conduit à des modèles très gros mais **sous-entraînés** (ex. GPT-3 175B).
- **Hoffmann et al. (DeepMind, 2022, « Chinchilla »)** : modèle et données doivent croître **ensemble**. Ratio compute-optimal $\approx$ **20 tokens par paramètre**. Chinchilla 70B (1,4 T tokens) bat Gopher 280B.

### Compute-optimal vs inference-optimal
- Le point Chinchilla minimise la perte **à coût d'entraînement donné**. Mais si le modèle est **beaucoup servi**, on l'entraîne **au-delà** de l'optimum (plus de tokens, modèle plus petit) pour réduire le coût d'**inférence** → c'est la logique des [[Small Language Models]].

### Au-delà de la perte
- La perte (proxy de la [[Perplexity|perplexité]]) s'extrapole bien ; les **capacités en aval** émergent de façon moins régulière. Et la donnée de qualité est **finie** — d'où la donnée synthétique et le décalage vers le *test-time compute* ([[Reasoning models]]).

## Les maths, simplement

- Coût d'entraînement d'un transformeur dense : $C \approx 6\,N\,D$ FLOPs. Sous ce budget, Chinchilla trouve $N_{\text{opt}} \propto C^{0.5}$ et $D_{\text{opt}} \propto C^{0.5}$ → **doubler le compute** ⇒ doubler **à la fois** taille et données.
- D'où la règle de poche $D \approx 20\,N$ au point compute-optimal.

## En pratique

- Dimensionner un entraînement : fixer le budget compute, en déduire $(N, D)$ compute-optimaux plutôt que de gonfler $N$ seul.
- Pour un modèle destiné à être **massivement servi**, dépasser 20 tokens/param est rationnel (amortir l'inférence sur les requêtes).
- Lire les lois d'échelle comme un **outil de planification et d'extrapolation**, pas comme une garantie de capacité précise.

## Approches voisines & alternatives

- [[Small Language Models]] — exploitent le régime **inference-optimal** (sur-entraînement) pour de petits modèles performants.
- [[Reasoning models]] — déplacent une partie de l'effort vers le **test-time compute** quand le pré-entraînement plafonne.
- [[Perplexity]] — la « perte » des lois d'échelle est l'entropie croisée dont la perplexité est l'exponentielle.
- [[Transformer architectures]] — l'estimation $C \approx 6ND$ suppose un transformeur dense.
- [[Mixture of Experts]] — casse précisément cette hypothèse : capacité découplée du calcul, donc un autre régime d'échelle.

## Pour aller plus loin

- Kaplan et al. (2020) — *Scaling Laws for Neural Language Models*.
- Hoffmann et al. (2022) — *Training Compute-Optimal Large Language Models* (Chinchilla).
