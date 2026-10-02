---
role: notion
nom: Normalisation et initialisation des réseaux
alias: [Normalisation des réseaux, initialisation des poids, BatchNorm, batch normalization, LayerNorm, layer normalization, GroupNorm, group normalization, RMSNorm, pré-norme, post-norme, pre-LN, post-LN, Xavier, Glorot, initialisation de He, Kaiming, internal covariate shift, QK-norm]
categorie: ml/apprentissage-profond
domaines: [ml-eng]
tags: [deep-learning, mixed-precision, optimization]
---

# Normalisation et initialisation des réseaux

## Aperçu

- Deux réponses au même problème : garder l'**échelle des signaux** (activations en avant, gradients en arrière) dans une plage où l'entraînement reste possible, d'une couche à l'autre. L'**initialisation** règle cette échelle au pas 0 ; la **normalisation** la maintient pendant tout l'entraînement.
- Quatre normalisations dominent : **BatchNorm** (Ioffe et Szegedy, 2015), **LayerNorm** (Ba et al., 2016), **GroupNorm** (Wu et He, 2018), **RMSNorm** (Zhang et Sennrich, 2019). Elles diffèrent par **ce sur quoi elles calculent leurs statistiques**, et donc par ce qu'elles supposent du lot.
- Un grand modèle de langage ouvert comme LLaMA prend RMSNorm, placée **avant** chaque sous-couche. Mais la littérature reste en désaccord sur le placement de la norme et sur la raison pour laquelle BatchNorm marche (voir plus bas).

## Concepts clés

### Pourquoi l'échelle des signaux compte
- Dans un réseau profond, la variance d'une activation est multipliée par un facteur à chaque couche. Un facteur moyen supérieur à 1 fait **exploser** le signal, inférieur à 1 le fait **disparaître** ; il en va de même, en sens inverse, des gradients de la [[Rétropropagation et différentiation automatique|passe arrière]].
- Glorot et Bengio (2010) en tirent deux conditions, sous l'hypothèse d'un régime **linéaire** à l'initialisation et de poids indépendants : conserver la variance en avant, $n_i\,\mathrm{Var}[W^i] = 1$, et en arrière, $n_{i+1}\,\mathrm{Var}[W^i] = 1$.

### Initialisation de Xavier (Glorot)
- Compromis entre les deux conditions : $\mathrm{Var}[W^i] = 2/(n_i + n_{i+1})$. En version uniforme : $W \sim U\!\left[-\sqrt{6}/\sqrt{n_j + n_{j+1}},\; +\sqrt{6}/\sqrt{n_j + n_{j+1}}\right]$.
- Le papier compare à l'initialisation « standard » $U[-1/\sqrt{n}, 1/\sqrt{n}]$, qui donne $n\,\mathrm{Var}[W] = 1/3$. Il note aussi que la sigmoïde logistique est mal adaptée aux réseaux profonds.

### Initialisation de He (Kaiming)
- Xavier suppose des activations linéaires. Pour une **ReLU**, qui annule la moitié du signal, He et al. (2015) obtiennent $\tfrac{1}{2}\, n_l\, \mathrm{Var}[w_l] = 1$, soit une gaussienne centrée d'écart-type $\sqrt{2/n_l}$ ($n_l$ : nombre de connexions entrantes), biais à 0.
- Résultat mesuré dans le papier : sur un modèle à 22 couches, les deux initialisations convergent (He plus tôt), sans écart net de précision ; à **30 couches**, Xavier **cale complètement**.

### BatchNorm
- Chaque canal est normalisé par la moyenne et la variance **du mini-lot**, puis remis à l'échelle par deux paramètres appris : $y = \gamma\,\hat x + \beta$, avec $\hat x = (x - \mu_B)/\sqrt{\sigma_B^2 + \varepsilon}$.
- À l'inférence, le papier utilise les statistiques de **population** (variance non biaisée) ; les bibliothèques en pratique les estiment par moyenne glissante pendant l'entraînement.
- Résultat annoncé : sur un modèle de type Inception, la même précision avec 14 fois moins de pas d'entraînement, des taux d'apprentissage bien plus élevés (×5, puis ×30), un effet de régularisation qui dispense parfois de Dropout. Un ensemble de réseaux normalisés atteint 4,9 % d'erreur top-5 en validation sur ImageNet.
- **Limite constante** : les statistiques viennent du lot. Wu et He montrent qu'avec ResNet-50 sur ImageNet, l'erreur de BatchNorm passe de 23,6 % (32 images par GPU) à 34,7 % (2 images), tandis que GroupNorm reste autour de 24,1 %.

### LayerNorm
- Les statistiques sont calculées sur **toutes les unités d'une couche, pour un seul exemple** : même calcul en entraînement et en test, utilisable avec un lot de taille 1, adapté aux réseaux récurrents et aux séquences de longueur variable.
- Limite écrite par les auteurs : sur les réseaux convolutifs, BatchNorm fait mieux, d'après des expériences qu'ils qualifient de préliminaires.

### GroupNorm
- Les canaux sont divisés en $G$ groupes (32 par défaut), les statistiques calculées par groupe et par exemple. $G = 1$ redonne LayerNorm, $G = C$ la normalisation d'instance.
- À taille de lot normale, elle fait 0,5 point **moins bien** que BatchNorm ; à lot de 2, son erreur est 10,6 points plus basse. Elle sert quand le lot est contraint par la mémoire (détection, segmentation, vidéo).

### RMSNorm
- Pas de recentrage : $\bar a_i = a_i / \mathrm{RMS}(a)\cdot g_i$, avec $\mathrm{RMS}(a) = \sqrt{\tfrac{1}{n}\sum_i a_i^2}$. Hypothèse de Zhang et Sennrich : l'invariance au recentrage de LayerNorm est **superflue** ; garder l'invariance à l'échelle suffit.
- Gain annoncé : performance comparable à LayerNorm, temps d'exécution réduit de 7 à 64 % selon les modèles et les implémentations. Sa variante partielle, qui estime le RMS sur une fraction des entrées (6,25 %), n'a pas montré de gain de vitesse constant en pratique.
- LLaMA (Touvron et al., 2023) la prend avec une **pré-normalisation** de chaque sous-couche, d'après le papier.

### Pré-norme contre post-norme
- **Post-LN** (Transformer d'origine) : la norme est placée *après* l'addition résiduelle. **Pre-LN** : la norme est placée *à l'intérieur* de la branche résiduelle, avant l'attention ou le MLP.
- Xiong et al. (2020), par une analyse en champ moyen **à l'initialisation** : avec Post-LN, les gradients près de la sortie sont grands, ce qui rend l'entraînement instable sans **warm-up** du taux d'apprentissage ; avec Pre-LN, les gradients restent bien conduits, et le warm-up peut être retiré sans perte de qualité notable sur les tâches testées.
- **Les sources ne vont pas dans le même sens sur la qualité finale.** Nguyen et Salazar (2019) trouvent que PreNorm permet d'entraîner sans warm-up, mais qu'en traduction à haute ressource (WMT14 En-De) il **dégrade** la performance. Wang et al. (DeepNet, 2022) écrivent que Pre-LN a des gradients plus forts dans les couches basses, ce qui dégraderait la performance face à Post-LN ; ils proposent DeepNorm, avec lequel ils annoncent un entraînement jusqu'à 1 000 couches.

### Interaction avec la précision mixte
- Micikevicius et al. (2017) : les grandes réductions (sommes sur un vecteur) se font en **FP32**, notamment dans les couches de normalisation (accumulation des statistiques) et dans softmax ; ces couches lisent et écrivent du FP16 mais calculent en FP32.
- La doc PyTorch (autocast, v2.14) liste `layer_norm`, `group_norm`, `softmax` parmi les opérations exécutées en **float32** ; `batch_norm` et `rms_norm` n'y figurent pas, et la doc précise qu'une opération non listée est supposée stable en float16. Détails dans [[Mixed precision]].

### Travaux récents et variantes
- **QK-norm** : normaliser les requêtes et les clés de l'attention. Henry et al. (2020) : normalisation $\ell_2$ de $Q$ et $K$ suivie d'un gain appris. Dehghani et al. (2023, ViT-22B) : divergence observée vers 8 milliards de paramètres, attribuée à de très grandes valeurs de logits d'attention, corrigée par une LayerNorm sur $Q$ et $K$.
- **Peri-LN** (Kim et al., ICML 2025) : normalisation avant **et** après chaque module, plus normalisation des embeddings. Les auteurs citent Gemma et OLMo comme l'adoptant, sans l'analyser ; leurs expériences, jusqu'à 3,2 milliards de paramètres, donnent une variance plus équilibrée et moins de pics que Pre-LN.
- **Se passer de la normalisation** : Zhu et al. (2025) remplacent la norme par *Dynamic Tanh*, $\gamma\tanh(\alpha x) + \beta$ ; sur LLaMA de 7 à 70 milliards de paramètres, la perte finale est la même à un centième près. Limites écrites par les auteurs : elle peine à remplacer BatchNorm dans un ResNet, et une fois le code bien compilé, elle n'apporte aucun gain de vitesse.
- Deux préprints de février 2026, lus par leur résumé seulement : *SiameseNorm* (un flux de type Pre-Norm et un de type Post-Norm partageant les blocs) et *TaperNorm* (une normalisation qui s'efface progressivement en une application linéaire).

## Les maths, simplement

- Pour $y = Wx$ avec $n$ entrées indépendantes, de moyenne nulle, de variance $\sigma_x^2$, et des poids indépendants de variance $\sigma_W^2$ : $\mathrm{Var}[y] = n\,\sigma_W^2\,\sigma_x^2$. Garder la variance revient à $n\,\sigma_W^2 = 1$, condition de Glorot.
- Une ReLU met à zéro la moitié des valeurs d'une entrée symétrique : le second moment de sa sortie vaut la moitié de la variance de son entrée, d'où le facteur 2 de He : $\sigma_W^2 = 2/n$.
- Normaliser revient à imposer $\mathrm{Var} = 1$ par construction : $\hat x = (x - \mu)/\sqrt{\sigma^2 + \varepsilon}$. Ce qui change d'une méthode à l'autre est l'**ensemble** sur lequel $\mu$ et $\sigma^2$ sont calculés (lot, couche, groupe de canaux) ; RMSNorm laisse tomber $\mu$.

## En pratique

- **Réseau convolutif, lot de taille raisonnable** : BatchNorm. **Lot petit** (détection, segmentation, vidéo) : GroupNorm.
- **Transformeur, séquences** : LayerNorm ou RMSNorm, en pré-norme ; RMSNorm si la vitesse compte et que la qualité reste comparable.
- **ReLU et dérivées** : initialisation de He ; **tanh ou sigmoïde** : Xavier. Les bibliothèques posent ces valeurs par défaut ; les contrôler quand une couche non standard est ajoutée.
- BatchNorm a deux comportements : `train()` utilise les statistiques du lot, `eval()` celles de population. Oublier de repasser en `eval()` fausse les prédictions (le mode ne coupe pas les gradients ; voir [[Rétropropagation et différentiation automatique]]).
- Divergence tardive d'un grand transformeur : examiner les logits d'attention (QK-norm) et le placement de la norme avant de baisser le taux d'apprentissage.
- Précision mixte : garder les normalisations et softmax en fp32, ce qu'`autocast` fait déjà pour `layer_norm` et `group_norm`.

## Approches voisines & alternatives

- [[Mixed precision]] — les normalisations sont parmi les opérations à garder en fp32.
- [[Rétropropagation et différentiation automatique]] — le problème des gradients qui disparaissent ou explosent, dont ces techniques sont les remèdes en amont.
- [[Maximal Update Parametrization]] — règle d'initialisation et de pas par couche en fonction de la largeur ; traite l'échelle des signaux à un autre niveau que la normalisation.
- [[Adam optimizer]] — autre mécanisme d'adaptation d'échelle, côté optimiseur : il met à l'échelle les **pas** par paramètre, la normalisation met à l'échelle les **activations**.
- [[Learning rate schedules]] — le warm-up que Post-LN impose et que Pre-LN permet de retirer.
- [[Régularisation]] — BatchNorm a un effet de régularisation qui dispense parfois de Dropout.
- [[Self-attention]] et [[Transformer architectures]] — où se placent les normes et où QK-norm s'applique.
- [[Perceptron et MLP]] — le cadre où Xavier et He se dérivent.
- [[Apprentissage contrastif]] — la perte contrastive, dont les sorties sont normalisées $\ell_2$ avant de calculer des similarités cosinus.
- [[PyTorch]] — `nn.BatchNorm2d`, `nn.LayerNorm`, `nn.GroupNorm`, `nn.RMSNorm`, et initialisations dans `torch.nn.init`.

## Pour aller plus loin

- Ioffe & Szegedy (2015) — [*Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*](https://arxiv.org/abs/1502.03167).
- Santurkar, Tsipras, Ilyas & Madry (2018) — [*How Does Batch Normalization Help Optimization?*](https://arxiv.org/abs/1805.11604) : les auteurs avancent que la stabilité de distribution des entrées de couche y est pour peu, et que BatchNorm lisse le paysage d'optimisation (perte et gradients plus lipschitziens) ; leur expérience injecte du bruit après BatchNorm sans perdre le gain. **Désaccord direct avec Ioffe et Szegedy** sur le mécanisme, laissé tel quel.
- Ba, Kiros & Hinton (2016) — [*Layer Normalization*](https://arxiv.org/abs/1607.06450).
- Wu & He (2018) — [*Group Normalization*](https://arxiv.org/abs/1803.08494).
- Zhang & Sennrich (2019) — [*Root Mean Square Layer Normalization*](https://arxiv.org/abs/1910.07467).
- Glorot & Bengio (2010) — [*Understanding the difficulty of training deep feedforward neural networks*](https://proceedings.mlr.press/v9/glorot10a.html), AISTATS.
- He, Zhang, Ren & Sun (2015) — [*Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification*](https://arxiv.org/abs/1502.01852).
- Xiong et al. (2020) — [*On Layer Normalization in the Transformer Architecture*](https://arxiv.org/abs/2002.04745).
- Nguyen & Salazar (2019) — [*Transformers without Tears: Improving the Normalization of Self-Attention*](https://arxiv.org/abs/1910.05895) ; Wang et al. (2022) — [*DeepNet*](https://arxiv.org/abs/2203.00555).
- Touvron et al. (2023) — [*LLaMA*](https://arxiv.org/abs/2302.13971) ; Micikevicius et al. (2017) — [*Mixed Precision Training*](https://arxiv.org/abs/1710.03740).
- Henry et al. (2020) — [*Query-Key Normalization for Transformers*](https://arxiv.org/abs/2010.04245) ; Dehghani et al. (2023) — [*Scaling Vision Transformers to 22 Billion Parameters*](https://arxiv.org/abs/2302.05442).
- Kim et al. (2025) — [*Peri-LN*](https://arxiv.org/abs/2502.02732) ; Zhu et al. (2025) — [*Transformers without Normalization*](https://arxiv.org/abs/2503.10622).
