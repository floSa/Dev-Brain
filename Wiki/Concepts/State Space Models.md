---
galaxie: wiki
type: concept
nom: State Space Models
alias: [SSM, modèles à espace d'états, Mamba, Mamba-2, Mamba-3, S4, S5, selective state space, linear-time sequence model, MIMO, discrétisation trapézoïdale]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [state-space-model, deep-learning, inference-optimization]
---

# State Space Models

## Aperçu

- Famille de modèles de séquences qui propagent l'information via un **état latent** évoluant de façon **linéaire** dans le temps, au lieu de comparer tous les tokens entre eux comme l'attention.
- Argument central : **coût linéaire** en longueur de séquence (contre quadratique pour l'attention) et **état de taille constante** à l'inférence — pas de cache KV qui enfle. **Mamba** (SSM sélectif) est l'exemple qui a rendu l'approche compétitive face au [[Transformer architectures|Transformer]].
- C'est la lignée « automatique » de l'[[Attention linéaire|attention linéaire]] : mêmes propriétés de coût, même compromis sur le rappel, vocabulaire et outillage mathématique différents (équations d'état, discrétisation).

## Concepts clés

### De l'équation d'état à la récurrence

- Hérité de l'automatique : un état continu $h(t)$ obéit à $h'(t) = A\,h(t) + B\,x(t)$, $y(t) = C\,h(t)$. **Discrétisé**, cela devient une **récurrence linéaire** sur les tokens.
- Deux vues du même modèle : forme **convolutive** (parallélisable, pour l'entraînement) et forme **récurrente** ($O(1)$ par token, pour l'inférence en flux). C'est ce double visage qui fait la force des SSM (S4).
- Le choix du **schéma de discrétisation** — comment passer du continu au discret — n'est pas un détail d'implémentation : c'est un levier de qualité, comme le montre Mamba-3 (voir plus bas).

### La sélectivité (Mamba)

- Les SSM linéaires « purs » sont invariants dans le temps → incapables de raisonnement dépendant du contenu. **Mamba** rend $B$, $C$ et le pas de discrétisation **fonction de l'entrée** : le modèle décide quoi retenir ou oublier.
- Cette sélectivité casse la forme convolutive ; elle est récupérée par un **scan parallèle** *hardware-aware* (calcul fusionné en SRAM, esprit proche de [[Flash Attention and efficient attention|Flash Attention]]).
- **Mamba-2** reformule l'opération en produits matriciels structurés (*state space duality*), ce qui la fait tourner sur les tensor cores comme une attention — le vrai déblocage pratique de la lignée.

### Mamba-3 (ICLR 2026) : trois corrections, une perspective « inference-first »

- Le papier part d'un constat pratique : les modèles linéaires publiés sacrifient des **capacités** (notamment le suivi d'état) pour de l'efficacité algorithmique, et leur linéarité théorique reste **mal exploitée par le matériel**. Trois corrections en découlent.
- **Récurrence plus expressive** — la discrétisation d'Euler ne regarde qu'une extrémité de l'intervalle (approximation d'ordre 1). Mamba-3 adopte une règle **trapézoïdale** (combinaison convexe, dépendante des données, des deux extrémités) : l'erreur locale passe de $O(\Delta t^2)$ à $O(\Delta t^3)$. Plus de fidélité par pas, à coût identique.
- **État à valeurs complexes** — une récurrence réelle ne peut pas représenter certains comptages ou automates périodiques : il lui manque la notion de **phase**. Passer aux complexes débloque des tâches de *state tracking* hors de portée des modèles linéaires réels. Le papier établit au passage un pont théorique entre SSM complexes et RoPE dépendant des données (cf. [[Positional encoding]]).
- **Formulation MIMO** (multi-entrée multi-sortie) — au lieu de canaux traités indépendamment (SISO), traiter des blocs entrée/sortie ensemble. Cela augmente l'**intensité arithmétique** au décodage (plus de calcul par octet lu, donc un GPU mieux utilisé) **sans grossir l'état** ni la latence.
- Résultats : à l'échelle 1,5 Md, +0,6 point de précision aval moyenne sur le meilleur concurrent (Gated DeltaNet), et +1,2 point de plus pour la variante MIMO — soit **+1,8 point** au total. Et surtout : **perplexité comparable à Mamba-2 avec un état deux fois plus petit**. La variante MIMO paie en vitesse d'entraînement ce qu'elle gagne en qualité.

### Le compromis face à l'attention

- Gagne sur les **contextes longs** et le **débit** à séquence longue ; perd (parfois) en **copie exacte / rappel associatif**, là où l'attention excelle. Formulation utile : le Transformer est une base de données exacte (KV-cache consultable intégralement), le SSM une **compression avec perte** à budget fixe.
- Ce compromis est de nature informationnelle, pas un défaut d'ingénierie : un état de taille bornée ne peut pas restituer un contexte illimité. D'où la convergence vers les **hybrides** — cf. [[Architectures hybrides LLM]].

## Les maths, simplement

- Récurrence discrète : $h_t = \bar{A}\,h_{t-1} + \bar{B}\,x_t$ et $y_t = C\,h_t$, où $\bar{A}, \bar{B}$ sont les versions discrétisées de $A, B$ (via le pas $\Delta$).
- Dépliée, c'est une **convolution** $y = x * \bar{K}$ avec un noyau $\bar{K} = (C\bar{B}, C\bar{A}\bar{B}, C\bar{A}^2\bar{B}, \dots)$ : entraînement parallèle en $O(L\log L)$, inférence récurrente en $O(L)$ avec mémoire $O(1)$.
- Discrétisation : Euler prend $h_{t} \approx h_{t-1} + \Delta\, f(h_{t-1})$ — la dérivée en **un** point. Le trapèze prend $h_t \approx h_{t-1} + \tfrac{\Delta}{2}\big(f(h_{t-1}) + f(h_t)\big)$ — la moyenne aux **deux** bouts, ce qui annule le terme d'erreur d'ordre suivant. Mamba-3 en fait une version pondérée et apprise.
- Intensité arithmétique : au décodage, le SSM lit un état de taille $S$ pour faire $O(S)$ opérations — ratio calcul/mémoire de $O(1)$, catastrophique pour un GPU. La formulation MIMO amortit la lecture de l'état sur plusieurs canaux, montant ce ratio sans changer $S$.

## En pratique

- Pertinent quand la **longueur de contexte** ou le **débit en streaming** dominent (audio, génomique, longs documents) ; l'écosystème (noyaux, outillage, modèles pré-entraînés) reste **moins mûr** que celui des transformeurs.
- Les modèles de prod sont **hybrides**, jamais SSM purs : Jamba (Mamba + attention + [[Mixture of Experts|MoE]]), Nemotron-3 (Mamba-2 alterné avec de l'attention), Zamba. Voir aussi RWKV (RNN linéaire d'esprit voisin).
- À l'inférence, l'état constant supprime la croissance du cache KV — un levier d'[[Inference optimization|optimisation de l'inférence]] sur les longues générations. En contrepartie, la **reprise de session** et le *prefix caching* ne fonctionnent pas comme sur un Transformer : l'état est un objet opaque, pas un cache indexé par position.
- Piège d'évaluation, systématique dans cette famille : la perplexité reste bonne pendant que le rappel exact s'effondre. Tester explicitement needle-in-a-haystack et le rappel associatif.

## Approches voisines & alternatives

- [[Attention linéaire]] — la même famille vue depuis les noyaux et la mémoire associative (règle delta, gating) ; c'est le cadre qui unifie SSM et attention linéaire.
- [[Transformer architectures]] — l'architecture dominante que les SSM cherchent à concurrencer sur le coût.
- [[Self-attention]] — mécanisme quadratique opposé : rappel exact fort, mais coût qui explose avec la longueur.
- [[Architectures hybrides LLM]] — la façon dont les SSM sont réellement déployés : minorité de couches d'attention globale pour restaurer le rappel.
- [[Flash Attention and efficient attention]] — autre voie vers l'attention efficace ; les SSM changent de mécanisme plutôt que d'optimiser l'attention.
- [[Mixture of Experts]] — levier de passage à l'échelle orthogonal, souvent combiné aux SSM dans les hybrides.
- [[Inference optimization]] — l'état de taille constante évite l'enflure du cache KV.
- [[Positional encoding]] — l'état récurrent encode la position implicitement ; Mamba-3 formalise le lien avec RoPE.
- [[Scaling laws]] — les SSM rejouent la question du compute-optimal sur une autre architecture.

## Pour aller plus loin

- Gu, Goel & Ré (2021) — *Efficiently Modeling Long Sequences with Structured State Spaces* (S4).
- Gu & Dao (2023) — *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*.
- Dao & Gu (2024) — *Transformers are SSMs* (Mamba-2, state space duality).
- Mamba-3 (ICLR 2026, arXiv 2603.15569) — *Improved Sequence Modeling using State Space Principles* (trapèze, complexes, MIMO).
- Lieber et al. (2024) — *Jamba* (hybride Mamba + attention + MoE).
