---
role: notion
nom: Multi-Token Prediction
alias: [MTP, prédiction multi-tokens, MTP heads, têtes MTP, MTP-1, self-speculative decoding]
categorie: llm/runtime
domaines: [ml-eng, ai-eng]
tags: [decoding, transformers, inference-optimization, llm]
---

# Multi-Token Prediction

## Aperçu

- Au lieu d'entraîner un modèle à ne prédire que le **token suivant**, on lui greffe des **têtes auxiliaires** qui prédisent les tokens $t+2$, $t+3$, … depuis le même état caché. La perte totale additionne toutes ces prédictions.
- Double bénéfice, et c'est ce qui rend le concept intéressant : un **signal d'entraînement plus dense** (le modèle est forcé de planifier plus loin qu'un token) et, gratuitement, un **brouillon interne** réutilisable pour du [[Speculative decoding|décodage spéculatif]] sans second modèle.
- Devenu standard côté poids ouverts depuis DeepSeek-V3, où MTP donne un taux d'acceptation supérieur à **80 %** et environ **1,8×** de débit de génération.

## Concepts clés

### Le signal d'entraînement : forcer l'anticipation

- Un objectif purement *next-token* laisse le modèle optimiser localement : il suffit d'être bon sur le mot d'après. Prédire $t+2$ et $t+3$ depuis le même état oblige la représentation à **encoder plus de futur** qu'elle n'en a strictement besoin.
- L'effet est mesurable sur la qualité du modèle de base, indépendamment de toute accélération : c'est un objectif auxiliaire de type régularisation par tâche supplémentaire. C'est pourquoi MTP est décrit comme une technique d'**entraînement** avant d'être une technique d'inférence.
- Les têtes MTP sont **jetables** : on peut les retirer après entraînement et servir le modèle en next-token classique, en conservant le bénéfice de représentation.

### Deux façons de câbler les têtes

- **Têtes parallèles indépendantes** (formulation Meta d'origine, Gloeckle et al. 2024) : $k$ têtes lisent le même état caché et prédisent chacune une position. Simple, mais les prédictions ignorent leurs dépendances mutuelles — un brouillon incohérent.
- **Têtes séquentielles** (DeepSeek-V3) : chaque module MTP reçoit l'état **et** le token prédit à l'étape précédente. La chaîne causale est préservée à l'intérieur du brouillon, ce qui monte nettement le taux d'acceptation. C'est le choix qui a fait école.
- Le nombre de têtes utilisées à l'inférence est un réglage : « **MTP-1** » (une seule tête, un token d'avance) est la configuration de production de référence — c'est la baseline contre laquelle se mesurent les frameworks spéculatifs plus ambitieux.

### Du brouillon à l'accélération

- À l'inférence, les têtes MTP jouent le rôle de **drafter** : elles proposent $k$ tokens, le corps du modèle les vérifie en une passe, et l'on accepte le plus long préfixe cohérent (cf. [[Speculative decoding]] pour le critère d'acceptation).
- C'est du **self-speculative decoding** : pas de second modèle à charger, à aligner ou à maintenir. Le brouillon est par construction « de la même famille » que la cible, ce qui explique les taux d'acceptation élevés.
- Attention à la confusion fréquente : MTP **n'émet pas** plusieurs tokens par pas de façon inconditionnelle. La génération reste autorégressive et vérifiée ; ce qui change, c'est le nombre de tokens validés par passe.

## Les maths, simplement

- Objectif d'entraînement : $\mathcal{L} = \mathcal{L}_1 + \lambda \sum_{j=2}^{k} \mathcal{L}_j$, où $\mathcal{L}_j$ est l'[[Cross-entropy|entropie croisée]] sur le token à l'offset $j$ et $\lambda$ pondère les têtes auxiliaires (typiquement $\lambda < 1$, décroissant avec $j$).
- Accélération attendue : si $p$ est le taux d'acceptation par token de brouillon et $k$ la profondeur proposée, le nombre moyen de tokens validés par passe vaut $\mathbb{E}[\alpha] = \sum_{i=1}^{k} p^i$ (préfixe géométrique). À $p = 0{,}8$ et $k = 1$, cela donne $\approx 1{,}8$ — exactement le chiffre observé sur V3.
- Lecture : le gain est **borné par $p$**, non par $k$. Ajouter des têtes ne sert à rien si l'acceptation s'effondre au-delà de la première ; d'où l'intérêt des têtes séquentielles, qui maintiennent $p$ plus haut sur les positions lointaines.

## En pratique

- Côté **utilisateur d'un modèle**, MTP n'est pas un réglage : soit les têtes sont dans les poids publiés, soit non. Vérifier dans la carte du modèle (`num_nextn_predict_layers` chez DeepSeek) et dans le runtime que le chemin MTP est activé — sinon le gain de débit est simplement perdu.
- Côté **entraînement**, c'est un des ajouts au meilleur rapport bénéfice/complexité d'un pré-entraînement moderne, mais il coûte de la mémoire (têtes supplémentaires + activations) et complique le sharding. Supporté nativement par Megatron-Core / Megatron-Bridge.
- Le gain se cumule mal avec un contexte très entropique : sur du texte créatif, l'acceptation chute et l'on retombe sur du next-token avec un surcoût de vérification.
- Ne pas confondre MTP avec les modèles de diffusion textuelle, qui émettent réellement plusieurs tokens en parallèle sans vérification autorégressive — mécanisme et garanties différents.

## Approches voisines & alternatives

- [[Speculative decoding]] — le cadre dans lequel MTP s'insère à l'inférence ; MTP en est la variante « brouillon interne » (et la baseline MTP-1 des frameworks récents comme DSpark).
- [[Decoding strategies]] — MTP ne change pas *quel* token est choisi, seulement le rythme de validation.
- [[Transformer architectures]] — les têtes MTP sont un ajout architectural greffé sur la pile de couches.
- [[Inference optimization]] — MTP est un levier de débit du **decode**, sans effet sur le *time-to-first-token*.
- [[Cross-entropy]] — la perte additionnée sur les offsets futurs.
- [[Scaling laws]] — MTP améliore la qualité à compute donné : c'est un déplacement de la frontière, pas seulement une accélération.
- Alternatives comme drafter : **EAGLE-3** (prédiction au niveau des features, souvent supérieure), **Medusa** (têtes en arbre), **draft model séparé** (plus flexible, plus lourd à opérer).

## Pour aller plus loin

- Gloeckle et al. (2024, Meta) — *Better & Faster Large Language Models via Multi-token Prediction* (formulation d'origine, têtes parallèles).
- DeepSeek-AI (2024) — *DeepSeek-V3 Technical Report* (arXiv 2412.19437 — têtes séquentielles, acceptation > 80 %, ~1,8×).
- NVIDIA — *Multi-Token Prediction*, documentation Megatron-Bridge (mise en œuvre à l'entraînement).
- Raschka (2026) — *LLM Architecture Gallery : MTP* (comparaison des câblages entre modèles récents).
