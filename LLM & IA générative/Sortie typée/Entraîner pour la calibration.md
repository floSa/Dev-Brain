---
role: notion
nom: Entraîner pour la calibration
alias: [RLCD, règle de notation strictement propre, strictly proper scoring rule, score propre, calibration à l'entraînement, récompense calibrée]
categorie: llm/sortie-structuree
domaines: [ai-eng, ml-eng]
tags: [calibration, reinforcement-learning, structured-output, classification]
---

# Entraîner pour la calibration

## Aperçu

- Un modèle de décision vaut par ses **probabilités** : un seuil, une escalade, un tri ne tiennent que si « 0,8 » veut dire « juste 8 fois sur 10 ». Plutôt que de recaler après coup, ces modèles **visent la calibration à l'entraînement**, par une perte ou une récompense qui n'est maximisée qu'en annonçant la vraie probabilité.
- L'outil est ancien : la **règle de notation strictement propre** (score de Brier, log-vraisemblance, score sphérique). Rien de nouveau dans les formules ; ce qui est neuf, c'est de les mettre au centre de l'apprentissage d'un modèle qui décide.
- **À dater.** Les recettes ci-dessous viennent de **trois éditeurs** (Cloudflare, Convai, Liquid), sans mesure indépendante de la recette elle-même. Un quatrième, TypeSafe, nomme sa méthode (« RLCD ») sans la décrire. Ce que des tiers ont mesuré, c'est le résultat : l'erreur de calibration (ECE) de chaque modèle.

## Concepts clés

### Pourquoi la calibration ne se récompense pas sur un exemple
- Dire qu'une probabilité de 0,7 est « honnête » n'a aucun sens sur **une** décision : seul un **ensemble** de décisions annoncées à 0,7, dont environ 70 % sont justes, le dit. Une récompense « bonne ou mauvaise réponse » (préférence humaine, test automatique) ne note donc pas la confiance.
- Pire, un entraînement sur préférences apprend que l'assurance plaît : les modèles sortent **surconfiants**, effet documenté de longue date. Un objectif de calibration doit porter sur une **distribution**, pas sur un point.

### Règle de notation strictement propre
- Une règle de notation $S(q, y)$ note la distribution annoncée $q$ face à l'issue observée $y$. Elle est **strictement propre** si l'espérance de la note n'est optimale que lorsque $q$ est **la vraie distribution**. Annoncer plus sûr que la vérité fait perdre en espérance.
- Exemples : **Brier** (carré de l'écart), **log-vraisemblance** (la perte d'entropie croisée, [[Cross-entropy]]), **sphérique**. Pour une échelle ordonnée, le **score de probabilité par rang** (*ranked probability score*) compare les probabilités **cumulées**, de sorte qu'une erreur d'un niveau coûte moins qu'une erreur de trois.

### Les recettes publiées (au 2026-10-20)
- **Cloudflare, Clef** : un modèle Qwen **gelé**, une tête de schéma conjointe, des adaptateurs de bas rang (rang 256) entraînés avec elle. Perte d'**entropie croisée à lissage d'étiquettes** plus une perte de **Brier** « pour affiner la calibration », sur des jeux de données synthétiques internes qui permutent l'ordre des champs, les invites et les schémas. Puis une étape de renforcement que Cloudflare nomme RLCD : **crédit partiel aux niveaux ordinaux voisins**, récompense des enregistrements entièrement exacts, **pénalité de référence** contre la dérive de distribution.
- **Convai, Laya** : la politique annonce une distribution ; l'exploration ajoute un bruit gaussien de moyenne nulle aux logits ; la récompense est une règle strictement propre (**logarithmique plus sphérique**, plus le score de rang pour les questions ordinales) ; mises à jour de type REINFORCE avec une **base de moyenne de groupe** (style [[GRPO]]). Puis un recalage par **température**, une par type de question et nombre d'options.
- **Liquid, d1-3B et d1-omni-600M** : moyenne de poids de deux modèles de base, ajustements avec plusieurs graines et mélanges de données, puis fusion. Le blog dit que les entrées longues, le mélange des options et la correction des raccourcis dans les données ont plus compté que des techniques plus avancées. d1-omni stocke des **températures de calibration par type de question** (de 1,0 à 1,75). Liquid ne parle ni de RLCD ni de renforcement ; la fonction de perte n'est pas publiée.
- **TypeSafe, Jev** : « RLCD » est nommé, avec l'objectif de « probabilités épistémiquement honnêtes », mais ni signal de récompense, ni algorithme, ni données, ni mesure de calibration ne sont publiés (relevé au 2026-09-22). Le sigle recouvre donc trois recettes et une **homonymie** : *Reinforcement Learning from Contrastive Distillation* (Yang et Klein, 2023), une méthode d'alignement qui n'a rien à voir.

## Les maths, simplement

- **Brier** : $\text{Brier} = \dfrac{1}{n}\sum_{i=1}^{n}(p_i - y_i)^2$. Sa propriété : pour une question vraie avec probabilité $p$, la perte attendue de l'annonce $q$ est $p(1-q)^2 + (1-p)\,q^2$, minimale en $q = p$.
- **Exemple chiffré.** Vraie probabilité 0,7. Annoncer 0,7 coûte $0{,}7 \times 0{,}09 + 0{,}3 \times 0{,}49 = 0{,}21$. Annoncer 0,9 (surconfiant) coûte $0{,}7 \times 0{,}01 + 0{,}3 \times 0{,}81 = 0{,}25$. Annoncer 0,5 coûte 0,25. Seule l'annonce honnête minimise la perte.
- **Score de rang** pour $K$ niveaux : $\text{RPS} = \dfrac{1}{K-1}\sum_{k=1}^{K-1}\left(\sum_{j \le k} p_j - \sum_{j \le k} o_j\right)^2$, où $o$ vaut 1 sur le niveau observé. Un voisin proche perd moins qu'un niveau lointain : c'est le « crédit partiel » de la recette de Cloudflare.
- **Mesure** : $\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n}\,|\,\text{acc}(B_m) - \text{conf}(B_m)\,|$, écart moyen entre confiance annoncée et exactitude, par tranche de confiance. Détail et recalibrage dans [[Calibration]].

## En pratique

- **Le calibrage se vérifie à l'extérieur, et vite** : un jeu étiqueté, un diagramme de fiabilité, un ECE ; quelques heures. C'est la propriété centrale annoncée par ces modèles, et la plus facile à contrôler.
- **Recaler par type de question, sur ses données.** Le sens du biais change d'un type à l'autre : sur Jev, une étude indépendante (tickets synthétiques, 2026-09-19, corrigée le 2026-09-22) trouve les questions `choice` et `score` surconfiantes et les `noul` sous-confiantes ; la température de recalage vaut 1,30 (`choice`) et 1,92 (`score`) contre 0,66 (`noul`) après correction. Le sens du biais survit à la correction, son ampleur non. Laya annonce de même qu'il « sort surconfiant » : une température par type et nombre d'options fait passer l'ECE moyen de 0,466 à 0,081 (`laya`), d'après sa carte.
- **Hors distribution, la confiance s'effondre mal.** Sur une tâche dont la règle est absente du texte, Jev répond juste 44,7 % du temps à 0,74 de probabilité moyenne (ECE 0,325 sur cette question), et 0 message sur 30 hors périmètre est signalé, à 0,99. Conclusion de l'étude : ne pas seuiller sur le champ `confidence` brut.
- **Une probabilité n'est pas une fréquence tant que le seuil n'est pas posé sur ses données** : [[Choisir entre règle, classifieur, modèle de décision et LLM]] (règle 3).
- **Ajuster le modèle dégrade la calibration.** Laya ajusté sur sa tâche monte à 0,766 d'exactitude contre 0,362 pour les poids de base, mais son ECE avant recalage est de 0,213 (carte, lue le 2026-10-20). Un ajustement se suit avec un nouveau jeu de calibration.

### Repères datés

ECE publiés par le classement amont « Decision Index », édition 0.3.1, relevés le 2026-10-10 sur 32 benchmarks (plus bas = mieux). Fichier relu le 2026-10-20 (généré le 2026-10-16) : valeurs inchangées sauf Jev, 0,078 au lieu de 0,074. Un ECE moyen sur 32 benchmarks ne dit rien de la tâche où l'on s'apprête à seuiller.

| Modèle | ECE | Remarque |
|---|---|---|
| Clef-flash | 0,0249 | ligne du classement, qui l'a soumise n'est pas indiqué |
| Clef | 0,0395 | idem |
| d1-3B | 0,0468 | ligne « soumise par LiquidAI » (suite publique exécutée par Liquid) |
| Jev 1.13 | 0,074 | API fermée |
| d1-omni-600M | 0,1284 | « checkpoint de recherche précoce » |
| Laya (poids de base) | 0,140 | pas le checkpoint ajusté |

## Approches voisines & alternatives

- [[Calibration]] — la mesure (ECE, diagramme de fiabilité) et le recalage post-hoc (Platt, isotonique, température) ; cette page en est la version entraînée.
- [[Modèle de décision]] — l'objet dont la probabilité est la moitié du produit.
- [[RLHF and DPO]] — l'entraînement sur préférences, qui dégrade la confiance ; [[GRPO]] — l'estimateur de base de groupe que reprend la recette de Laya ; [[Reinforcement learning]].
- [[Cross-entropy]] et [[Classification metrics]] — log-vraisemblance et Brier comme métriques.
- [[Décomposer une question en signaux étroits]] — une recomposition ajustée sur étiquettes recalibre au passage.
- [[Lire un score publié]] — la grille de lecture d'un score de vitrine, qui s'applique aux ECE comme aux exactitudes.

## Pour aller plus loin

- Gneiting et Raftery, *Strictly Proper Scoring Rules, Prediction, and Estimation*, Journal of the American Statistical Association 102(477), 2007 — le cadre des règles de notation propres.
- Brier, « Verification of forecasts expressed in terms of probability », Monthly Weather Review 78(1), 1950 — l'origine du score.
- Guo, Pleiss, Sun et Weinberger, *On Calibration of Modern Neural Networks*, ICML 2017 : https://arxiv.org/abs/1706.04599 — l'ECE et le recalage par température.
- Yang, Klein et Celikyilmaz, *RLCD: Reinforcement Learning from Contrastive Distillation for Language Model Alignment*, 2023 : https://arxiv.org/abs/2307.12950 — l'homonyme, à ne pas confondre.
- Blog Cloudflare, « Clef decision models », 2026-10-01 : https://blog.cloudflare.com/clef-decision-models/ — la recette décrite en section « comment ils sont fabriqués ».
- Carte de Laya (section Training, Honest Limits) : https://huggingface.co/convaiinnovations/laya
- Blog Liquid AI, « Open d1 », 2026-10-07 : https://www.liquid.ai/blog/d1-open
- Étude indépendante de calibration de Jev (scienthoon), 2026-09-19 : https://github.com/scienthoon/jev-ood-calibration
