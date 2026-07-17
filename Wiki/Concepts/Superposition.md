---
galaxie: wiki
type: concept
nom: Superposition
alias: [Superposition hypothesis, Hypothèse de superposition, Polysémanticité, Polysemanticity, Neurones polysémantiques]
categorie: concept/dl
domaines: [data-sci, ai-eng]
tags: [explainability, deep-learning, llm]
---

# Superposition

## Aperçu

- Hypothèse centrale de l'[[Interprétabilité mécaniste|interprétabilité mécaniste]] : un réseau encode **plus de features qu'il n'a de neurones**, en les rangeant dans des directions non orthogonales qui se chevauchent.
- Conséquence directe et gênante : un neurone donné s'active pour plusieurs notions sans rapport — il est **polysémantique**. C'est pourquoi lire les neurones un par un ne mène nulle part, et c'est le problème que les [[Sparse autoencoders|SAE]] tentent de résoudre.

## Concepts clés

### Le constat qui a lancé le sujet
- On aimerait qu'un neurone = un concept. En pratique, on trouve un neurone qui répond à la fois aux « citations académiques », aux « dialogues en coréen » et aux « verbes en -ing ». Rien de commun entre les trois.
- Longtemps pris pour un artefact ou du bruit d'entraînement. La superposition en donne une explication : ce n'est pas un défaut, c'est une **stratégie de compression** que le réseau apprend délibérément.

### Pourquoi le réseau s'y résout
- Le monde a bien plus de features utiles qu'un modèle n'a de dimensions. Un LLM peut avoir besoin de représenter des millions de notions dans quelques milliers de dimensions par couche.
- Il ne peut pas leur donner à chacune une direction orthogonale — il n'y en a pas assez. Il les entasse donc dans des directions **presque** orthogonales, en acceptant un peu d'interférence.

### Le troc : parcimonie contre interférence
- Ce qui rend l'entassement viable, c'est que les features réelles sont **parcimonieuses** : à un instant donné, très peu sont actives. Deux features qui ne s'activent jamais ensemble peuvent partager une région de l'espace sans se gêner.
- Le réseau échange donc de la **capacité** contre du **bruit**. Il préfère représenter 10 000 features avec un peu d'interférence que 1 000 proprement — et c'est un bon calcul tant que la parcimonie tient.

### Ce que la géométrie impose
- En dimension $n$, on ne peut placer que $n$ vecteurs strictement orthogonaux. Mais on peut en placer un nombre **exponentiel** en $n$ qui soient *presque* orthogonaux (lemme de Johnson-Lindenstrauss). C'est le fondement mathématique du phénomène.
- Les travaux d'Anthropic sur les *toy models* montrent que le réseau organise ces directions en structures géométriques régulières (digones, triangles, pentagones, tétraèdres) selon le degré de parcimonie — la superposition n'est pas un entassement au hasard.

### Pourquoi c'est un problème pratique
- Toute tentative de lire un modèle **neurone par neurone** est vouée à l'échec : la base des neurones n'est pas la base des concepts. On lit dans le mauvais repère.
- D'où la stratégie des [[Sparse autoencoders|SAE]] : projeter les activations dans un espace **beaucoup plus grand** et parcimonieux, pour espérer y retrouver une direction par concept. On décompresse ce que le réseau avait compressé.

## Les maths, simplement

- Le modèle jouet : le réseau doit encoder $m$ features dans $n$ dimensions avec $m \gg n$, via $h = Wx$ puis reconstruire $\hat{x} = \text{ReLU}(W^\top h + b)$. Le résultat dépend entièrement de la parcimonie de $x$.
- Si $x$ est **dense** (beaucoup de features actives ensemble) : le réseau renonce, ne garde que les $n$ features les plus importantes et jette le reste. Pas de superposition — c'est une PCA déguisée.
- Si $x$ est **parcimonieux** : il encode les $m$ features dans des directions non orthogonales. L'interférence entre deux features $i$ et $j$ vaut $w_i^\top w_j \ne 0$, mais elle ne coûte que si les deux s'activent en même temps — ce qui est rare par hypothèse.
- Johnson-Lindenstrauss, le résultat qui autorise tout ça : dans $\mathbb{R}^n$, on peut placer $m = e^{O(\epsilon^2 n)}$ vecteurs dont les produits scalaires deux à deux sont tous $\le \epsilon$. Le nombre de directions « presque orthogonales » croît **exponentiellement** avec la dimension, là où le nombre de directions strictement orthogonales n'en offre que $n$.

## En pratique

- **C'est une hypothèse, pas un théorème.** Solidement étayée sur des modèles jouets et cohérente avec ce qu'on observe sur de vrais LLM, mais elle reste un cadre d'interprétation. Le domaine bouge vite ; s'en méfier comme d'une vérité acquise.
- **La conséquence méthodologique est ferme** : ne pas chercher à interpréter des neurones isolés. Chercher des **directions** dans l'espace d'activations ([[Sparse autoencoders]], [[Probing]]).
- **Elle explique pourquoi les modèles surdimensionnés sont plus lisibles** : plus de dimensions = moins de pression à entasser = moins de superposition. Un vrai argument, à mettre en face du coût.
- Elle éclaire aussi la **distillation** et le **pruning** : si l'information est entassée dans des directions presque orthogonales, on comprend qu'un modèle puisse être élagué sans s'effondrer — la redondance apparente n'en est pas ([[Pruning]], [[Distillation]]).
- Pas d'outil dédié : la superposition est le **cadre théorique**, l'outillage est côté [[Sparse autoencoders|SAE]] ([[Dev/Services/SAELens|SAELens]], [[Dev/Services/interpreto|interpreto]]).

## Approches voisines & alternatives

- [[Interprétabilité mécaniste]] — le chapeau : la superposition en est l'obstacle fondateur.
- [[Sparse autoencoders]] — la réponse pratique : décompresser vers un espace sur-complet et parcimonieux.
- [[Probing]] — l'approche complémentaire : chercher une direction connue plutôt que découvrir les directions inconnues.
- [[embeddings]] — le même phénomène côté représentations : des directions porteuses de sens dans un espace dense.
- [[Réduction de dimension]] — la superposition est de la compression apprise ; le lemme de Johnson-Lindenstrauss y est aussi le résultat clé.
- [[Pruning]] / [[Distillation]] — ce que la superposition explique : pourquoi tant de paramètres semblent redondants sans l'être.
- [[Explicabilité des modèles]] — le versant tabulaire et post-hoc, où le problème ne se pose pas.

## Pour aller plus loin

- Elhage et al. (2022) — *Toy Models of Superposition* (Anthropic, Transformer Circuits) : l'article fondateur, avec les structures géométriques.
- Olah et al. (2020) — *Zoom In: An Introduction to Circuits* (Distill) : l'origine du constat de polysémanticité.
- Bricken et al. (2023) — *Towards Monosemanticity* (Anthropic) : la démonstration que les SAE démêlent effectivement la superposition.
