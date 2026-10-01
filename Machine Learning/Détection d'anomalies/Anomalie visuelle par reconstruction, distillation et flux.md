---
role: notion
nom: Anomalie visuelle par reconstruction, distillation et flux
alias: [DRAEM, RD4AD, Reverse Distillation, STFPM, EfficientAD, UniAD, FastFlow, CFlow, CFlow-AD, Détection d'anomalies multi-classe, Anomalie visuelle par réseau appris]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, computer-vision, industrial-inspection, normalizing-flow, deep-learning]
---

# Anomalie visuelle par reconstruction, distillation et flux

## Aperçu

- Seconde grande famille de détecteurs d'anomalies sur images, face à la [[Anomalie visuelle par banque de mémoire|banque de mémoire]] : au lieu de **mémoriser** le bon, on **entraîne un réseau** à faire une tâche sur le bon (le reconstruire, imiter un enseignant, estimer sa densité), et on repère les endroits où il échoue.
- Trois mécanismes : la **reconstruction** (DRAEM, UniAD, Dinomaly), la **distillation** enseignant-élève (RD4AD, STFPM, EfficientAD), les **flux normalisants** (FastFlow, CFlow-AD). Tous partent de features pré-entraînées, sauf cas noté.
- Le gain par rapport à la mémoire est la latence à l'inférence : pas de recherche de voisins. Le coût est un entraînement, et un réglage de ce que le réseau peut « trop bien » généraliser. Cadre dans [[Détection d'anomalies visuelle]].

## Concepts clés

### Reconstruction

- **Idée** : un réseau entraîné sur le bon reconstruit mal ce qui n'est pas du bon ; l'écart entre l'entrée et la reconstruction est le score. C'est le principe de l'[[Autoencodeurs|autoencodeur]].
- **Limite connue, citée par plusieurs papiers** : le réseau généralise trop. DRAEM : « les autoencodeurs sur-généralisent aux anomalies » ; RD4AD : les modèles profonds généralisent si bien que même les régions anormales sont bien restaurées ; UniAD parle d'un « raccourci d'identité » (*identical shortcut*), où le réseau recopie l'entrée.
- **DRAEM** (Zavrtanik et al., ICCV 2021) : un sous-réseau de reconstruction et un sous-réseau discriminatif entraînés ensemble sur des anomalies **simulées** (masque de bruit de Perlin rempli de textures d'un autre jeu). Les auteurs précisent que la simulation vise des apparences « juste hors distribution », pas des défauts réalistes. 98,0 % d'AUROC image sur MVTec AD.
- **UniAD** (You et al., NeurIPS 2022) : reconstruction de features par un décodeur à requêtes par couche, attention masquée et *feature jittering* pour éviter le raccourci d'identité. 96,5 % d'AUROC image, 96,8 % pixel sur MVTec AD en cadre unifié.
- **Dinomaly** (Guo et al., CVPR 2025) : reconstruction de features par un Transformer pur, encodeur DINOv2 à registres gelé (ViT-B/14), goulot bruité (Dropout), attention linéaire, reconstruction « lâche » (couches regroupées par sommes). 99,6 % d'AUROC image, 98,4 % pixel, 94,8 % d'AU-PRO sur MVTec AD en multi-classe. Brique : [[Dinomaly]].

### Distillation enseignant-élève

- **Idée** : un enseignant pré-entraîné extrait des features ; un élève, entraîné sur le bon seul, apprend à les imiter. Sur un défaut, l'élève n'a jamais appris à imiter : l'écart entre les deux est le score.
- **STFPM** (Wang et al., BMVC 2021) : élève de même architecture que l'enseignant, appariement des pyramides de features. 95,5 % d'AUROC image sur MVTec AD.
- **RD4AD, ou distillation inverse** (Deng et Li, CVPR 2022) : l'élève ne reçoit pas l'image mais l'*embedding* « une classe » de l'enseignant, et doit restaurer ses représentations multi-échelles, des abstraites vers les bas niveaux. 98,5 % d'AUROC image, 97,8 % pixel, 93,9 % de PRO ; 0,31 s par image sur un CPU Intel i7.
- **EfficientAD** (Batzner et al., WACV 2024) : extracteur léger (PDN) distillé depuis un réseau pré-entraîné, avec une perte « *hard feature loss* » ; un autoencodeur dédié aux anomalies **logiques**. Latence de 2,2 ms (version S) et 4,5 ms (version M) sur un GPU RTX A6000 à lot de 1 ; 98,8 et 99,1 % d'AUROC image sur MVTec AD.

### Flux normalisants

- **Idée** : un flux est une transformation inversible qui envoie les features du bon vers une loi simple (gaussienne) en gardant une densité calculable. Un patch de faible vraisemblance est suspect.
- **FastFlow** (Yu et al., arXiv 2021, aucune venue relevée) : flux 2D branché sur un extracteur (ResNet, ViT) ; 99,4 % d'AUROC image sur MVTec AD, avec CaiT-M48 comme extracteur (99,3 % avec Wide-ResNet50-2).
- **CFlow-AD** (Gudovskiy et al., WACV 2022) : décodeurs à flux normalisants **conditionnels** multi-échelles ; 98,26 % d'AUROC image, 98,62 % pixel, 94,60 % d'AU-PRO sur MVTec AD.

### Multi-classe contre une classe, un modèle

- Le cadre historique : **un modèle par catégorie** (par pièce). UniAD le juge coûteux en mémoire et pose la tâche **unifiée** : un seul modèle entraîné sur les normaux de plusieurs catégories, sans étiquette de classe ni à l'entraînement ni à l'inférence.
- En unifié, beaucoup de méthodes chutent : DRAEM perd environ 10 points d'après UniAD ; Dinomaly attribue la baisse à la correspondance identité (la copie de l'entrée) et la reformule en sur-généralisation du décodeur. Dans le tableau de Dinomaly, RD4AD est à 94,6 % en multi-classe, contre 98,5 % dans son propre papier.
- Intérêt pratique : **un modèle à maintenir** pour toutes les références d'une ligne, quand les références changent souvent.

### Coût d'un Transformer

- Dinomaly mesure, sur RTX 3090 à lot de 16 : 153,6 images par seconde en ViT-S, 58,1 en ViT-B, 24,2 en ViT-L ; AUROC image de 99,26, 99,60 et 99,77 %. Les auteurs reconnaissent dans leur annexe le coût de calcul des ViT.
- Les latences ne sont pas comparables d'un papier à l'autre : GPU, lot et résolution diffèrent (2,2 ms pour EfficientAD sur A6000 à lot de 1 ; 0,31 s pour RD4AD sur CPU).

### Quand les chiffres de MVTec AD ne tiennent plus

- Sur MVTec AD 2, le papier évalue sept méthodes dont RD (l'implémentation *Reverse Distillation Revisited*, pas le code original), EfficientAD et MSFlow. En AU-PRO0.30 de segmentation : EfficientAD 58,7 %, RD 53,0 %, MSFlow 52,7 %, contre 93,5, 93,9 et 91,2 % sur MVTec AD.
- Sous éclairage non vu à l'entraînement (AU-PRO0.05, test privé mixte), RD perd 1,4 point et MSFlow 12,4 : la robustesse varie fortement d'une méthode à l'autre. Dinomaly et UniAD n'y sont pas évalués.
- **Anomalies sensorielles et logiques.** Dinomaly se dit conçu pour l'anomalie « sensorielle » (aspect), pas sémantique. MVTec LOCO (Bergmann et al., IJCV 2022) définit la **logique** : un objet admissible présent au mauvais endroit, ou un objet requis absent. EfficientAD ajoute un autoencodeur pour elle ; sur LOCO, EfficientAD-M atteint 90,7 % d'AUROC image contre 80,3 % pour PatchCore dans le même tableau.

## Les maths, simplement

- Reconstruction : $s(x,u)=\lVert \phi(x)_u-\hat\phi(x)_u\rVert$ — écart entre la feature d'entrée et sa reconstruction à la position $u$ ; ou $1-\cos(\cdot,\cdot)$ pour Dinomaly (perte cosinus globale, avec *hard mining* qui réduit le gradient des points déjà bien reconstruits).
- Distillation : $s(x,u)=\sum_\ell \lVert T_\ell(x)_u-S_\ell(x)_u\rVert^2$ — écart entre les features de l'enseignant $T$ et de l'élève $S$, couche $\ell$ par couche.
- Flux : $\log p(z)=\log p_0(f(z))+\log\left|\det \tfrac{\partial f}{\partial z}\right|$ — la densité d'une feature se calcule exactement par changement de variable ; $-\log p$ sert de score.

## En pratique

- **Choisir le mécanisme selon la contrainte** : latence très basse → distillation légère (EfficientAD) ; un modèle pour toutes les références → multi-classe (UniAD, Dinomaly) ; meilleur score sur les jeux publics → Dinomaly, avec son coût de ViT.
- **Mesurer la latence soi-même**, sur le matériel visé et la résolution des images d'atelier : les chiffres publiés ne se transposent pas. Pour la sortie en production, un export vers [[OpenVINO]] se prépare avec [[anomalib]].
- **Un score élevé sur MVTec AD ne vaut pas robustesse** à l'éclairage ou aux défauts logiques ([[Détection d'anomalies visuelle]]).
- **Valider le bon** : le réseau apprend ce qu'on lui montre ; un défaut dans l'entraînement se reconstruit ou s'imite comme du normal.

## Approches voisines & alternatives

- [[Anomalie visuelle par banque de mémoire]] — mémoriser plutôt qu'entraîner : aucune optimisation, mais recherche de voisins à l'inférence.
- [[Anomalie visuelle zero-shot et few-shot]] — sans entraînement sur la pièce.
- [[Autoencodeurs]] — la reconstruction en général, hors images industrielles.
- [[Vision Transformers (ViT)]] — l'architecture de Dinomaly et son coût.
- [[Modèles de fondation vision]] — DINOv2 et les encodeurs gelés.
- [[Isolation Forest]] — côté tabulaire : même question, sans pixels.

## Pour aller plus loin

- Zavrtanik et al. (2021), *DRAEM — A discriminatively trained reconstruction embedding for surface anomaly detection*, ICCV. arXiv : https://arxiv.org/abs/2108.07610
- Deng, Li (2022), *Anomaly Detection via Reverse Distillation from One-Class Embedding*, CVPR. arXiv : https://arxiv.org/abs/2201.10703
- Wang et al. (2021), *Student-Teacher Feature Pyramid Matching for Anomaly Detection*, BMVC. arXiv : https://arxiv.org/abs/2103.04257
- Batzner et al. (2024), *EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies*, WACV. arXiv : https://arxiv.org/abs/2303.14535
- You et al. (2022), *A Unified Model for Multi-class Anomaly Detection*, NeurIPS. arXiv : https://arxiv.org/abs/2206.03687
- Guo et al. (2025), *Dinomaly: The Less Is More Philosophy in Multi-Class Unsupervised Anomaly Detection*, CVPR. arXiv : https://arxiv.org/abs/2405.14325
- Yu et al., *FastFlow: Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows*. arXiv : https://arxiv.org/abs/2111.07677
- Gudovskiy et al. (2022), *CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows*, WACV. arXiv : https://arxiv.org/abs/2107.12571
- Bergmann et al. (2022), *Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization*, IJCV. DOI : https://doi.org/10.1007/s11263-022-01578-9
