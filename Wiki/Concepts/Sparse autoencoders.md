---
galaxie: wiki
type: concept
nom: Sparse autoencoders
alias: [SAE, Sparse autoencoder, Autoencodeur parcimonieux, Autoencodeur creux, TopK SAE, JumpReLU SAE, BatchTopK, Dictionary learning]
categorie: concept/dl
domaines: [data-sci, ai-eng]
tags: [explainability, deep-learning, llm, unsupervised]
---

# Sparse autoencoders

## Aperçu

- Variante d'[[Autoencodeurs|autoencodeur]] qui va à rebours de l'intuition : son code est **plus large** que son entrée (sur-complet), mais très peu de ses unités sont actives à la fois. On ne compresse pas — on **décompresse**.
- Le but n'est pas la reconstruction mais le **démêlage** : reprendre des activations où les concepts sont entassés par [[Superposition|superposition]], et les étaler dans un espace assez grand pour qu'une direction ≈ un concept. C'est aujourd'hui l'outil central de l'[[Interprétabilité mécaniste|interprétabilité mécaniste]] des LLM.

## Concepts clés

### Pourquoi sur-complet
- Un autoencodeur classique rétrécit pour forcer l'abstraction. Ici c'est l'inverse : les activations d'un LLM contiennent **plus de concepts que de dimensions** ([[Superposition]]). Les compresser encore aggraverait le problème.
- On projette donc vers 10 à 100 fois plus de dimensions, en exigeant que presque tout soit à zéro. C'est la parcimonie, pas la dimension, qui fait office de contrainte.

### La parcimonie remplace le goulot
- Sans contrainte, un code sur-complet apprend trivialement l'identité. La parcimonie est **le seul régularisateur** : au plus $k$ unités actives par exemple.
- L'espoir sous-jacent : si chaque exemple n'active qu'une poignée de directions, ces directions ont des chances de correspondre à des notions distinctes et lisibles (**monosémantiques**).

### La tension centrale : reconstruction vs parcimonie
- Deux objectifs qui s'opposent. Plus on impose la parcimonie, moins on reconstruit fidèlement ; mieux on reconstruit, plus le code redevient dense et illisible.
- **Tout le réglage d'un SAE est ce curseur.** Il n'y a pas d'optimum objectif : trop parcimonieux → on perd de l'information et on invente des features ; pas assez → on n'a rien démêlé.

### Les variantes, et ce que chacune corrige

| Variante | Comment la parcimonie est imposée | Ce que ça change |
|---|---|---|
| **Vanilla (L1)** | Pénalité L1 sur les activations | Le classique. Défaut : le L1 **rétrécit aussi les features utiles** (*shrinkage*), ce qui biaise la reconstruction |
| **TopK** | Garder les $k$ plus fortes, forcer le reste à 0 | Parcimonie **exacte et contrôlée** — `k` se choisit, il ne se découvre pas. Pas de shrinkage |
| **BatchTopK** | TopK à l'échelle du batch | `k` variable par exemple : les entrées riches gardent plus de features |
| **JumpReLU** | Seuil appris par unité | Meilleur compromis reconstruction/parcimonie rapporté ; entraînement plus délicat |

### Interpréter ce qui sort
- Un SAE produit des **directions**, pas des concepts nommés. L'interprétation est une étape distincte : regarder les entrées qui activent le plus une direction (TopKInputs), demander à un LLM de la nommer, ou mesurer son effet causal.
- C'est le maillon faible de la chaîne — et le moins automatisable.

### Évaluer un SAE
- Pas de vérité terrain, donc pas de métrique unique. On croise : erreur de reconstruction, **parcimonie** (L0 moyen), **fidélité** (perte du modèle si l'on remplace ses activations par leur reconstruction), et **stabilité** (deux SAE entraînés sur les mêmes données trouvent-ils les mêmes features ?).
- Les *dead features* — unités jamais actives — sont le symptôme d'entraînement le plus courant à surveiller.

## Les maths, simplement

- Encodeur : $z = \text{ReLU}(W_e (x - b_d) + b_e)$, décodeur : $\hat{x} = W_d z + b_d$. Avec $\dim(z) \gg \dim(x)$ — typiquement 16× à 64×.
- Objectif vanilla : $\mathcal{L} = \underbrace{\lVert x - \hat{x} \rVert_2^2}_{\text{reconstruction}} + \underbrace{\lambda \lVert z \rVert_1}_{\text{parcimonie}}$. Le $\lambda$ **est** le curseur du compromis.
- Pourquoi le L1 pose problème : il pénalise l'**amplitude**, pas le nombre d'unités actives. Il rabote donc les features légitimes en même temps qu'il élimine les parasites — c'est le *shrinkage*, hérité du [[Régularisation|Lasso]].
- TopK contourne le souci : $z = \text{TopK}\big(W_e(x - b_d) + b_e\big)$, sans terme de pénalité. La parcimonie est structurelle, $\lVert z \rVert_0 = k$ exactement, et les amplitudes restent intactes.
- La reconstruction se lit comme une somme de features : $\hat{x} = \sum_{i \in \text{actifs}} z_i \, d_i$, où $d_i$ est la $i$-ème colonne de $W_d$ — **la direction de la feature $i$** dans l'espace du modèle. C'est cette colonne que l'on cherche à nommer.

## En pratique

- **Sujet de recherche, pas outil de production.** Utile pour comprendre un modèle, auditer un comportement, chercher une feature de sécurité. Pas pour expliquer une prédiction à un client — pour ça, [[Explicabilité des modèles|SHAP]] ou une [[Attribution par gradient|attribution]].
- **Coûteux** : entraîner un SAE demande de collecter des millions d'activations, puis un entraînement à part entière. Ce n'est pas une analyse post-hoc légère.
- **Un SAE par couche et par point d'accroche.** Les features de la couche 5 n'ont rien à voir avec celles de la couche 20. Le flux résiduel est le point d'accroche le plus courant.
- **Le doute méthodologique est réel** : rien ne garantit que les directions trouvées soient les « vraies » features du modèle plutôt qu'un artefact du SAE. Des travaux récents montrent que des SAE entraînés sur du bruit produisent des features d'apparence tout aussi interprétable. Prudence sur les conclusions.
- **Préférer TopK au L1 vanilla** en première approche : `k` se règle directement, et l'absence de shrinkage rend l'évaluation plus honnête.
- Outils : [[Dev/Services/SAELens|SAELens]] (l'écosystème dédié : entraînement, SAE pré-entraînés, analyse), [[Dev/Services/interpreto|interpreto]] (SAE parmi d'autres méthodes de dictionnaire, avec les métriques), [[Dev/Services/nnsight|nnsight]] / [[Dev/Services/TransformerLens|TransformerLens]] pour extraire les activations.

## Approches voisines & alternatives

- [[Autoencodeurs]] — le parent : même architecture, contrainte inversée (sur-complet + parcimonie au lieu de goulot).
- [[Superposition]] — le phénomène qui justifie l'existence des SAE. À lire avant.
- [[Interprétabilité mécaniste]] — le chapeau : les SAE en sont l'outil principal aujourd'hui.
- [[Probing]] — l'approche supervisée et complémentaire : chercher une direction **connue** au lieu de découvrir les inconnues.
- [[NMF]] / [[ICA]] — les autres méthodes de dictionnaire, linéaires et bien plus légères. `interpreto` les propose en alternative aux SAE.
- [[PCA]] — la décomposition de référence, mais orthogonale par construction — donc structurellement incapable de représenter des directions en superposition.
- [[Régularisation]] — d'où vient la pénalité L1, et le shrinkage qu'elle traîne.
- [[Explicabilité des modèles]] — le versant tabulaire et post-hoc.

## Pour aller plus loin

- Bricken et al. (2023) — *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning* (Anthropic).
- Gao et al. (2024) — *Scaling and evaluating sparse autoencoders* (OpenAI) : l'article des TopK SAE.
- Rajamanoharan et al. (2024) — *Jumping Ahead: Improving Reconstruction Fidelity with JumpReLU SAEs* (DeepMind).
- Templeton et al. (2024) — *Scaling Monosemanticity* (Anthropic) : les SAE passés à l'échelle sur Claude 3 Sonnet.
