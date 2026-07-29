---
galaxie: wiki
type: concept
nom: Attention Residuals
alias: [AttnRes, Block AttnRes, résiduels par attention, attention sur la profondeur, depth-wise attention, dilution PreNorm]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [attention, transformers, deep-learning]
---

# Attention Residuals

## Aperçu

- Proposition de l'équipe Kimi (Moonshot AI, mars 2026) qui remplace la **connexion résiduelle** d'un [[Transformer architectures|Transformer]] — l'addition $h + f(h)$, inchangée depuis ResNet en 2015 — par une **attention softmax apprise sur les sorties de toutes les couches précédentes**.
- Formulation qui éclaire l'idée : le résiduel classique est un **RNN de la profondeur** (accumulation à poids fixes, un pas par couche) ; AttnRes en fait une **attention de la profondeur** (pondération apprise et dépendante de l'entrée). Le même geste que l'attention a fait subir aux RNN sur l'axe séquence, appliqué à l'axe couches.
- Résultat annoncé : **1,25× d'avantage compute** (le modèle égale une baseline 25 % plus grosse), pour +3,8 % de coût d'entraînement et +1,9 % de latence d'inférence.

## Concepts clés

### Le problème : la dilution PreNorm

- En *Pre-LayerNorm* — le standard actuel (cf. [[Transformer architectures]]) — le flux résiduel **accumule toutes les sorties de couches à poids unitaires**. Rien ne borne cette somme : la norme de l'état caché croît avec la profondeur.
- Conséquence mécanique : la contribution **relative** de chaque nouvelle couche décroît à mesure qu'on monte. Une couche tardive ajoute un terme de norme $\approx 1$ à un état de norme $\approx \sqrt{L}$ — elle est structurellement diluée avant même d'avoir appris quoi que ce soit.
- Symptôme observable : les normes de gradient sont très inégales selon la profondeur. Sur un Transformer standard, elles s'étalent de 0,15 (couche 1) à 1,0 (couche 8) ; l'entraînement ne répartit pas son signal uniformément.

### Le mécanisme : une pseudo-requête par couche

- Chaque couche porte un **vecteur de paramètres appris qui joue le rôle d'une requête** — d'où « pseudo-requête » : elle n'est pas produite par l'entrée comme un $Q$ classique, c'est un paramètre du modèle.
- Cette pseudo-requête est confrontée aux sorties des couches précédentes, un softmax en tire des **poids qui somment à 1**, et l'état d'entrée de la couche devient cette combinaison pondérée au lieu d'une somme brute.
- Deux propriétés en découlent :
  - **Bornage** — un softmax somme à 1, donc la norme de l'état ne peut plus enfler avec la profondeur. La dilution disparaît par construction.
  - **Sélectivité dépendante du contenu** — une couche peut décider de lire surtout la couche 3 sur un exemple et surtout la couche 11 sur un autre. Les ablations du papier confirment que ce choix dépend bien du contenu et n'est pas dégénéré.
- Coût en paramètres : $O(d)$ par couche — négligeable. Le coût réel est en **mémoire** : il faut conserver les sorties de toutes les couches précédentes.

### Block AttnRes : rendre la chose finançable

- La version complète mémorise $L$ représentations par position, soit $O(Ld)$ — insoutenable à l'échelle, surtout en entraînement distribué où ces tenseurs circulent entre GPU.
- **Block AttnRes** partitionne les couches en $N$ blocs et n'attend qu'au niveau des blocs : $O(Ld) \rightarrow O(Nd)$. Sur un modèle de 48 couches découpé en 8 blocs, cela divise par **~6** le nombre de représentations conservées, en gardant l'essentiel du gain.
- La mise en œuvre repose sur un pipeline de communication par cache et un calcul en deux phases — c'est ce qui rend le surcoût acceptable en pratique (< 4 % à l'entraînement).

### Ce que ça donne

- Validation à l'échelle réelle : intégré dans **Kimi Linear** (48 Md de paramètres totaux, 3 Md activés — un [[Mixture of Experts|MoE]] [[Architectures hybrides LLM|hybride]]), pré-entraîné sur 1,4 T tokens.
- Gains sur benchmarks : GPQA-Diamond +7,5 points (36,9 → 44,4), MATH +3,6 (53,5 → 57,1), HumanEval +3,1 (59,1 → 62,2), C-Eval +2,9 (79,6 → 82,5). Amélioration sur **toutes** les tâches évaluées.
- Normes de gradient stabilisées entre 0,82 et 0,97 sur toute la profondeur — à comparer à l'étalement 0,15-1,0 de la baseline.
- Les expériences de [[Scaling laws|loi d'échelle]] montrent un gain **constant** selon la taille de modèle : ce n'est pas un artefact d'un point de fonctionnement.

## Les maths, simplement

- Résiduel classique, déplié : $h_L = h_0 + \sum_{\ell=1}^{L} f_\ell(h_{\ell-1})$. Tous les termes ont le **même poids 1**, et si les contributions sont approximativement décorrélées, $\lVert h_L \rVert$ croît en $\Theta(\sqrt{L})$ — c'est exactement la dilution.
- AttnRes : $h_\ell = \sum_{j < \ell} a_{\ell j} \, h_j$ avec $a_{\ell j} = \text{softmax}_j\big(\langle q_\ell, h_j \rangle\big)$, où $q_\ell$ est la pseudo-requête apprise de la couche $\ell$. Puisque $\sum_j a_{\ell j} = 1$, l'état est une **moyenne convexe** : sa norme reste dans l'enveloppe de celles des couches précédentes.
- Vu comme une matrice $A$ triangulaire inférieure de mélange en profondeur : le résiduel standard, c'est $A$ **figée à 1**. AttnRes rend $A$ apprise et dépendante de l'entrée. Block AttnRes en impose une structure **par blocs**, donc de rang réduit.

## En pratique

- Modification d'**architecture de pré-entraînement** : rien à activer sur un modèle déjà entraîné. La portée pratique immédiate est de savoir **lire** une fiche de modèle et comprendre pourquoi il gagne à taille égale.
- Le rapport bénéfice/coût est inhabituellement bon (1,25× de compute pour ~4 % de surcoût), mais l'annonce vient d'une seule équipe sur un seul modèle : à traiter comme un résultat prometteur et non comme un acquis, en attendant des réplications indépendantes.
- Pour qui entraîne : le point de vigilance est la **mémoire d'activations** et le trafic inter-GPU, pas le calcul. Ne pas envisager la variante complète au-delà de quelques milliards de paramètres — Block AttnRes est la version utilisable.
- Une implémentation de référence PyTorch existe (dépôt `MoonshotAI/Attention-Residuals`, plus une réimplémentation communautaire).

## Approches voisines & alternatives

- [[Transformer architectures]] — AttnRes remplace une brique de base du bloc : le résiduel et son interaction avec la normalisation Pre-LN.
- [[Self-attention]] — le même mécanisme, appliqué à l'axe **profondeur** au lieu de l'axe séquence.
- [[Attention linéaire]] — même mouvement conceptuel (substituer de l'attention apprise à un mécanisme figé), sur l'autre axe ; les deux cohabitent dans Kimi Linear.
- [[Architectures hybrides LLM]] — le modèle de validation d'AttnRes en est un.
- [[Loss landscape and saddle points]] — l'argument central est un argument de conditionnement et de propagation du gradient en profondeur.
- [[Learning rate schedules]] — même famille de problème (stabiliser l'entraînement profond), levier différent : l'optimiseur au lieu de l'architecture.
- [[Scaling laws]] — le gain est présenté comme un déplacement de la courbe compute ↔ qualité.
- Alternatives sur le même problème : **DenseNet / dense connections** (concaténer au lieu de pondérer), **résiduels pondérés appris** (poids scalaire par couche, sans dépendance à l'entrée), **normalisation du flux résiduel** (post-LN, DeepNorm).

## Pour aller plus loin

- Kimi Team, Moonshot AI (2026) — *Attention Residuals* (arXiv 2603.15031 — papier de référence).
- He et al. (2015) — *Deep Residual Learning* (le résiduel que ce travail remet en question).
- Xiong et al. (2020) — *On Layer Normalization in the Transformer Architecture* (l'origine du choix Pre-LN et de sa dilution).
- Dépôt `MoonshotAI/Attention-Residuals` — implémentation officielle.
