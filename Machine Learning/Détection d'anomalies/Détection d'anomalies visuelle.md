---
role: notion
nom: Détection d'anomalies visuelle
alias: [Visual anomaly detection, Inspection visuelle par IA, Détection de défauts non supervisée, Industrial anomaly detection, Contrôle qualité visuel non supervisé]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, computer-vision, industrial-inspection, unsupervised]
---

# Détection d'anomalies visuelle

## Aperçu

- Sur une ligne de production, **repérer un défaut sur une image sans avoir appris à quoi un défaut ressemble** : le modèle n'apprend que le « bon », et signale ce qui s'en écarte.
- La sortie est double : un **score** pour l'image entière (bonne ou suspecte) et une **carte d'anomalie** au pixel, qui montre où.
- Cette page pose le problème, ses entrées et sorties, et ses jeux de test. Les méthodes ont chacune leur page : [[Anomalie visuelle par banque de mémoire]], [[Anomalie visuelle par reconstruction, distillation et flux]], [[Anomalie visuelle zero-shot et few-shot]].

## Concepts clés

### Le problème : apprendre sur le bon seul

- Le cadre est le régime **semi-supervisé** de [[Types d'anomalies et régimes de supervision]] : l'entraînement ne contient que des images sans défaut ; le test mêle bon et défauts.
- La raison est industrielle. VisA l'écrit ainsi : les défauts sont rares et il est difficile d'en obtenir beaucoup d'images. L'enquête de Liu et al. (*Machine Intelligence Research*, 2024) part de la même hypothèse : la collecte d'échantillons anormaux coûte très cher en temps et en argent, donc l'entraînement ne contient que des échantillons normaux, et elle note aussi que les anomalies sont diverses et difficiles à collecter.
- Le jeu de référence, **MVTec AD** (Bergmann et al., CVPR 2019), applique exactement ce protocole : 15 catégories (10 objets, 5 textures), 5 354 images en tout dont 1 725 de test, plus de 70 types de défauts, masques pixel pour toutes les anomalies.

### Pourquoi pas un classifieur supervisé

- **Les défauts manquent**, surtout au démarrage d'une ligne, et ceux qui apparaîtront un jour ne sont pas tous connus d'avance. Un classifieur supervisé ne reconnaît que les classes de défauts qu'il a vues ; il laisse passer un défaut nouveau.
- **Le déséquilibre est extrême** : voir [[Imbalanced classification]] pour ce qu'il fait aux métriques.
- Le classifieur reste le bon outil quand les défauts sont nombreux, étiquetés et stables ; la détection d'anomalies sert quand ce n'est pas le cas, ou comme premier filet avant d'avoir de quoi entraîner. Voir aussi [[Classification d'images]] et [[Détection d'objets]].

### Entrée, sortie, et ce que « localiser » veut dire

- Une méthode produit une **carte d'anomalie** (un score par position). Dans PaDiM et PatchCore, le score de l'image est le **maximum** de cette carte ; SPADE procède en deux temps (image, puis pixel). La carte alimente donc aussi la localisation, au sens d'une segmentation grossière du défaut (voir [[Segmentation]]).
- Les métriques de la tâche sont l'AUROC image (l'image est-elle défectueuse ?), l'AUROC pixel, et **l'AU-PRO**, qui moyenne la part de chaque composante de défaut correctement retrouvée pour un taux de faux positifs plafonné à 0,3 (AU-PRO0.30). Leurs pièges (classe rare, seuil) sont dans [[Évaluer une détection d'anomalies]] ; les métriques de segmentation en général dans [[Métriques vision]].

### Une carte des méthodes

- **Banque de mémoire** : mémoriser les patchs de bon, comparer au plus proche voisin → [[Anomalie visuelle par banque de mémoire]] (SPADE, PaDiM, PatchCore).
- **Reconstruction, distillation, flux** : apprendre un réseau qui sait faire quelque chose sur le bon et échoue sur le défaut → [[Anomalie visuelle par reconstruction, distillation et flux]] (DRAEM, RD4AD, STFPM, EfficientAD, UniAD, Dinomaly, FastFlow, CFlow). Le principe de l'[[Autoencodeurs|autoencodeur]] en est l'ancêtre.
- **Zero-shot et few-shot** : réutiliser un modèle de fondation, sans image de bon ou avec très peu → [[Anomalie visuelle zero-shot et few-shot]], appuyé sur [[Modèles de fondation vision]].
- **Un cadre, deux régimes d'usage** : *une classe, un modèle* (un détecteur par pièce) ou *multi-classe*, un seul modèle pour toutes les catégories (UniAD, Dinomaly).

### Défauts sensoriels et défauts logiques

- Un défaut **sensoriel** change l'aspect : rayure, bosse, salissure. Un défaut **logique** viole une contrainte d'agencement : d'après la page de MVTec LOCO (Bergmann et al., IJCV 2022), un objet admissible présent à un endroit invalide, ou un objet requis absent. Le jeu compte 3 644 images en 5 catégories.
- La plupart des méthodes ci-dessous visent le premier cas. Dinomaly se dit conçu pour l'anomalie sensorielle, AnomalyDINO ne détecte pas les anomalies logiques (exemple : câbles échangés sur MVTec AD), EfficientAD ajoute un autoencodeur dédié. Voir [[Anomalie visuelle par reconstruction, distillation et flux]].

### La saturation de MVTec AD

- PatchCore atteint 99,1 % d'AUROC image sur MVTec AD, 99,6 % en ensemble. Le papier de Real-IAD écrit que les méthodes de pointe ont atteint la **saturation** (plus de 99 % d'AUROC) sur les jeux principaux comme MVTec. Le papier de MVTec AD 2 la mesure autrement : en AU-PRO de segmentation, MVTec AD et VisA saturent, des modèles très différents s'y séparant de moins d'un point.
- **MVTec AD 2** (Heckler-Kram et al., arXiv 2503.21622) a été construit pour y répondre : 8 scénarios, 8 004 images de 2,6 à 5 mégapixels, au moins quatre éclairages par scène (l'entraînement n'a que l'éclairage régulier), vérité terrain du test privé gardée sur un serveur d'évaluation. Les sept méthodes testées y plafonnent à 58,7 % d'AU-PRO0.30 (EfficientAD), moyenne 52,6 %, alors que quatre d'entre elles dépassent 90 % sur MVTec AD dans le même tableau.
- **VisA** (Zou et al., ECCV 2022) : 10 821 images, 12 objets dont 1 200 anormales. **Real-IAD** (Wang et al., CVPR 2024) : environ 150 000 images, 30 objets, 5 angles de prise de vue par objet. Les licences de ces jeux (la plupart non commerciales) sont dans [[Jeux de données d'anomalies]].

## Les maths, simplement

- Un détecteur calcule un score $s(x,u)$ pour chaque pixel $u$ de l'image $x$. Score d'image : $s(x)=\max_u s(x,u)$. Décision : alerte si $s(x)>\tau$ ; le seuil $\tau$ ne se règle pas sur les défauts (qu'on n'a pas), mais sur le bon — voir [[Score et seuil d'alerte]].
- AU-PRO : pour chaque seuil de score, on mesure la part de chaque composante de défaut retrouvée (le PRO) et le taux de faux positifs sur les pixels de bon ; on intègre le PRO pour un taux de faux positifs de 0 à 0,3, puis on normalise.

## En pratique

- **Un bon jeu d'images de bon d'abord.** Le détecteur ne vaut que ce que vaut son « normal » : même éclairage, même cadrage, aucun défaut caché ([[Types d'anomalies et régimes de supervision]], contamination).
- **Comparer plusieurs familles sur ses propres images** avec un seul protocole : c'est le rôle de [[anomalib]].
- **Ne pas conclure sur MVTec AD.** À 99 %, le jeu ne départage plus ; viser un jeu à éclairage variable (MVTec AD 2) ou ses propres images, et lire l'AU-PRO plutôt que l'AUROC image seule.
- **Sortir sur du matériel d'atelier** : l'export vers [[OpenVINO]] (PC industriel Intel sans GPU) est une étape de la chaîne, pas un détail.
- **Un jeu public non commercial ne sert pas à livrer** : voir [[Jeux de données d'anomalies]].

## Approches voisines & alternatives

- [[Autoencodeurs]] — apprendre à reconstruire le bon : l'ancêtre de la reconstruction.
- [[Isolation Forest]], [[One-Class SVM]] — les détecteurs classiques, sur des vecteurs de variables, pas sur des images brutes.
- [[Vision par ordinateur]] — le domaine parent.
- [[Détection hors distribution (OOD)]] — la même question posée à un classifieur d'images.
- [[Apprentissage auto-supervisé en vision]] — les features pré-entraînées sans étiquettes (DINOv2) qui servent d'extracteurs.
- [[Data drift]] — quand c'est le bon lui-même qui change (nouvelle matière, nouvel éclairage).

## Pour aller plus loin

- Bergmann, Fauser, Sattlegger, Steger (2019), *MVTec AD – A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection*, CVPR. DOI : https://doi.org/10.1109/CVPR.2019.00982
- Liu et al. (2024), *Deep Industrial Image Anomaly Detection: A Survey*, Machine Intelligence Research 21(1). arXiv : https://arxiv.org/abs/2301.11514
- Zou et al. (2022), *SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation* (VisA), ECCV. arXiv : https://arxiv.org/abs/2207.14315
- Wang et al. (2024), *Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection*, CVPR. arXiv : https://arxiv.org/abs/2403.12580
- Heckler-Kram et al., *The MVTec AD 2 Dataset: Advanced Scenarios for Unsupervised Anomaly Detection*. arXiv : https://arxiv.org/abs/2503.21622
