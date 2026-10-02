---
role: brique
nom: Dinomaly
alias: [guojiajeremy/Dinomaly, Dinomaly CVPR 2025]
pitch: "Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[anomalib]]", "[[patchcore-inspection]]", "[[AnomalyCLIP]]"]
complements: []
tags: [industrial-inspection, computer-vision, self-supervised]
url_docs: https://github.com/guojiajeremy/Dinomaly
url_repo: https://github.com/guojiajeremy/Dinomaly
---

# Dinomaly

<!-- AUTO:BANDEAU:START -->
> Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Dépôt de l'article de Guo et al., *Dinomaly: The Less Is More Philosophy in Multi-Class Unsupervised Anomaly Detection* (CVPR 2025, arXiv 2405.14325). La méthode est décrite dans [[Anomalie visuelle par reconstruction, distillation et flux]]. Un encodeur DINOv2 avec registres (ViT-B/14 par défaut, **gelé**) fournit les features ; un goulot MLP avec Dropout (le « bruit »), puis un décodeur de huit blocs Transformer à attention linéaire, reconstruisent ces features ; la perte est un cosinus global avec *hard mining* (les points déjà bien reconstruits voient leur gradient réduit à un dixième). Le cadre est **multi-classe** : un seul modèle pour toutes les catégories d'un jeu, plutôt qu'un modèle par pièce. Les scripts `*_uni.py` du dépôt sont les versions unifiées, les `*_sep.py` des versions par classe.

Résultats annoncés (image AUROC, configuration par défaut ViT-B) : 99,6 % sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD. Avec ViT-L, le README annonce 99,8, 98,7 et 90,1 % ; l'article mesure 275,3 M de paramètres pour ViT-L contre 148,0 M pour ViT-B, et 413,5 G de MACs contre 104,7 G. Relevé le 2026-10-02 : 529 étoiles, dernier push le 2026-09-17, aucune version publiée, branche par défaut `master`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un seul modèle à maintenir pour toutes les références d'une ligne (cadre multi-classe) | Une latence faible sur CPU : les auteurs reconnaissent le coût de calcul des ViT face aux CNN |
| Viser l'état de l'art sur MVTec AD, VisA ou Real-IAD, avec des points de contrôle de départ | Un chemin d'export et de CLI prêt à l'emploi → [[anomalib]] qui l'intègre depuis la version 2.1.0 |
| Des poids d'encodeur DINOv2 annoncés sous Apache-2.0 (voir plus bas) | Un jeu d'apprentissage sans image de bon → [[AnomalyCLIP]] |
| | Une méthode éprouvée depuis 2022, sans réseau à entraîner → [[patchcore-inspection]] |

## Mise en œuvre

- Installation — dépôt à cloner ; `requirements.txt` fige torch 1.12.0 (CUDA 11.3), torchvision 0.13.0, timm 0.9.12 ; Python 3.8.12 annoncé
- Point d'entrée — scripts `dinomaly_mvtec_uni.py` et équivalents VisA et Real-IAD ; 10 000 itérations dans le script MVTec
- Prérequis — MVTec AD à décompresser à côté du dépôt, VisA à prétraiter par script, Real-IAD sur demande aux auteurs ; l'encodeur se télécharge depuis `dl.fbaipublicfiles.com`
- Exécution — GPU : le README recommande une RTX 3090 de 24 Go ; aucune VRAM minimale mesurée
- Coût — gratuit ; trois points de contrôle ViT-B (MVTec AD, VisA, Real-IAD) sur Google Drive

## Licence et données

- **Code** : Apache-2.0 (API GitHub, fichier `LICENSE`, README). Le README demande de citer l'œuvre dans les travaux, produits et brevets : c'est une demande, pas une clause de la licence.
- **Backbone DINOv2** : le README du dépôt DINOv2 écrit que le code et les poids sont sous Apache-2.0. Les modèles d'autres familles listés dans le même README sont, eux, non commerciaux (Cell-DINO, XRay-DINO) : ils ne sont pas utilisés ici.
- **Jeux de données** : MVTec AD est en CC BY-NC-SA 4.0, non commercial ; VisA est annoncé en CC BY 4.0 par sa page ; Real-IAD en CC BY-NC-SA 4.0 d'après Hugging Face. Voir [[Jeux de données d'anomalies]]. Des poids entraînés sur un jeu non commercial sont à lire avec la même prudence.
- Dans la documentation d'[[anomalib]], la page de Dinomaly indique « MIT License » pour l'implémentation d'origine, ce qui contredit le dépôt ; non tranché.

## Limites à connaître

- **Anomalies sensorielles, pas sémantiques** : les auteurs écrivent que la méthode vise les premières (défauts d'aspect), pas les anomalies logiques d'agencement.
- **Dépôt de recherche** : versions de bibliothèques anciennes (torch 1.12), pas de version publiée ; une branche tierce (« cnlab ») propose DINOv3-Large pour des versions plus récentes de Python et PyTorch.
- Le chiffre de MVTec AD est **saturé** : à 99,6 %, il ne départage plus les méthodes ; voir [[Détection d'anomalies visuelle]].

## Écosystème

### Alternatives

- [[anomalib]] — Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0.
- [[patchcore-inspection]] — Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023.
- [[AnomalyCLIP]] — Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT.

## Ressources

- Dépôt — https://github.com/guojiajeremy/Dinomaly
- Article — https://arxiv.org/abs/2405.14325

## Voir aussi

- [[Anomalie visuelle par reconstruction, distillation et flux]] — la notion : reconstruction, distillation, flux
- [[Détection d'anomalies visuelle]] — le cadre, et la saturation de MVTec AD
- [[Modèles de fondation vision]] — DINOv2, l'encodeur gelé
- [[Jeux de données d'anomalies]] — MVTec AD, VisA, Real-IAD et leurs licences
- [[Comparatif - Détection d'anomalies visuelles]] — ce qui départage les quatre outils
