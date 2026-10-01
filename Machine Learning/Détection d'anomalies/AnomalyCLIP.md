---
role: brique
nom: AnomalyCLIP
alias: [zqhang/AnomalyCLIP, AnomalyCLIP ICLR 2024]
pitch: "Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[anomalib]]", "[[patchcore-inspection]]", "[[Dinomaly]]"]
complements: []
tags: [industrial-inspection, computer-vision, zero-shot, vision-language]
url_docs: https://github.com/zqhang/AnomalyCLIP
url_repo: https://github.com/zqhang/AnomalyCLIP
---

# AnomalyCLIP

<!-- AUTO:BANDEAU:START -->
> Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Dépôt de l'article de Zhou, Pang, Tian, He et Chen, *AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection* (ICLR 2024, arXiv 2310.18961). Le modèle CLIP reste gelé ; seuls deux **prompts textuels génériques** s'apprennent — un pour « normal », un pour « anormal » — avec le nom de l'objet remplacé par le mot « object », pour que la notion d'anomalie ne dépende pas de la catégorie. Ils sont entraînés sur un jeu auxiliaire annoté, puis appliqués à des jeux jamais vus : c'est le sens de « zero-shot » ici, qui ne signifie pas « sans aucune donnée ». La méthode est située dans [[Anomalie visuelle zero-shot et few-shot]].

Résultats annoncés (AUROC image, entraînement sur un jeu auxiliaire) : 91,5 % (image) et 91,1 % (pixel) sur MVTec AD, 82,1 % (image) sur VisA, 97,5 % sur DAGM ; évaluation sur 17 jeux industriels et médicaux. Relevé le 2026-10-02 : 674 étoiles, dernier push le 2025-07-08, MIT, non archivé ; les points de contrôle (paramètres des prompts, 22,6 Mo par époque) sont dans le dépôt.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Démarrer un contrôle sans aucune image de bon de la nouvelle pièce, ou en avoir trop peu | Des images de bon en quantité : une méthode entraînée sur la pièce fait mieux sur MVTec AD → [[patchcore-inspection]], [[Dinomaly]] |
| Tester vite si un défaut est visible par un modèle vision-langage avant de collecter | Une latence faible sur CPU : un ViT-L/14 à 336 px est lourd → [[anomalib]] et un modèle léger |
| Un score et une carte d'anomalie sans entraîner de réseau sur la ligne | Des défauts de logique (pièce manquante, mauvais agencement) : la méthode vise les défauts d'aspect |
| | Un usage commercial des poids CLIP sans avoir lu leur statut (voir plus bas) |

## Mise en œuvre

- Installation — dépôt à cloner ; `requirements.txt` (torch 2.0.0, torchvision 0.15.1, timm 0.6.13, scikit-learn 1.2.2)
- Point d'entrée — `bash test.sh` pour l'inférence avec les points de contrôle fournis ; `train.py` pour réapprendre les prompts (15 époques, taille d'image 518 par défaut)
- Prérequis — chaque jeu à préparer, avec un JSON généré par `generate_dataset_json/` ; les poids CLIP viennent d'ailleurs que du dépôt
- Exécution — GPU : une RTX 3090 de 24 Go annoncée par le README
- Coût — gratuit pour le code

## Licence et données

- **Code** : MIT (fichier `LICENSE`, API GitHub).
- **Poids CLIP** : le dépôt `openai/CLIP` est en MIT pour le code ; la fiche de modèle de CLIP ne donne pas de licence explicite pour les poids et écrit que tout usage déployé, commercial ou non, est « hors périmètre » pour l'instant. C'est une restriction d'usage de l'éditeur, pas une clause de licence : à trancher avant une livraison chez un client.
- **Jeux de données** : MVTec AD est en CC BY-NC-SA 4.0 (non commercial) ; VisA est annoncé en CC BY 4.0 ; voir [[Jeux de données d'anomalies]].

## Limites à connaître

- **Le protocole se lit avec soin** : le résultat de 91,5 % sur MVTec AD vient d'un entraînement des prompts sur le jeu de test de VisA, pas sur MVTec AD lui-même (protocole de l'article : VisA sert à évaluer MVTec AD, et MVTec AD à évaluer les autres jeux). Il ne dit rien d'une pièce d'atelier dont l'aspect n'a rien à voir avec les jeux publics.
- **En dessous des méthodes entraînées sur le bon** quand elles ont des images : 91,5 % contre 99,6 % pour [[Dinomaly]] sur le même jeu, avec des protocoles différents.
- Dépôt de recherche, dernier push en juillet 2025, aucune version relevée.

## Écosystème

### Alternatives

- [[anomalib]] — Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0.
- [[patchcore-inspection]] — Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023.
- [[Dinomaly]] — Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0.

## Ressources

- Dépôt — https://github.com/zqhang/AnomalyCLIP
- Article — https://arxiv.org/abs/2310.18961

## Voir aussi

- [[Anomalie visuelle zero-shot et few-shot]] — la notion : WinCLIP, AnomalyCLIP, AnomalyDINO
- [[Détection d'anomalies visuelle]] — le cadre : apprendre sur le bon seul
- [[Modèles de fondation vision]] — CLIP et les modèles pré-entraînés réutilisés tels quels
- [[Jeux de données d'anomalies]] — MVTec AD, VisA et leurs licences
- [[Comparatif - Détection d'anomalies visuelles]] — ce qui départage les quatre outils
