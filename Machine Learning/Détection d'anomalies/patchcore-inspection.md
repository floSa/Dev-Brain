---
role: brique
nom: patchcore-inspection
alias: [PatchCore, amazon-science/patchcore-inspection, Towards Total Recall in Industrial Anomaly Detection]
pitch: "Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[anomalib]]", "[[Dinomaly]]", "[[AnomalyCLIP]]"]
complements: []
tags: [industrial-inspection, computer-vision]
url_docs: https://github.com/amazon-science/patchcore-inspection
url_repo: https://github.com/amazon-science/patchcore-inspection
---

# patchcore-inspection

<!-- AUTO:BANDEAU:START -->
> Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Dépôt de code de l'article de Roth et al., *Towards Total Recall in Industrial Anomaly Detection* (CVPR 2022, arXiv 2106.08265). Principe de la méthode, décrit dans [[Anomalie visuelle par banque de mémoire]] : des features de patchs extraites d'un réseau pré-entraîné sur ImageNet (WideResNet50 en défaut ; le README évoque aussi d'autres backbones), regroupées en une banque de mémoire des patchs « bons », réduite par un coreset glouton approximatif ; à l'inférence, la distance d'un patch au plus proche voisin de la banque donne le score. Le dépôt livre deux scripts, `bin/run_patchcore.py` (entraîner et évaluer) et `bin/load_and_evaluate_patchcore.py` (recharger un modèle), avec des exemples shell.

Résultats annoncés par le README sur MVTec AD : baseline WR50 à 99,2 % d'AUROC image, 98,1 % d'AUROC pixel et 94,4 % de PRO ; ensemble à 99,6 %, 98,2 % et 94,9 %. Relevé le 2026-10-02 : 1 406 étoiles, aucune version publiée, dernier commit de la branche principale le 2023-03-06, dernier push enregistré par l'API le 2024-07-10 (cause non relevée), dépôt non archivé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Reproduire les chiffres de l'article avec le code de ses auteurs | Un outil maintenu, avec une CLI, des jeux de données et un export : la même méthode existe dans [[anomalib]] |
| Une baseline très forte à comparer à tout modèle neuf, sans réseau à entraîner (seule la banque se construit) | Un détecteur multi-classe en un seul modèle → [[Dinomaly]] |
| Étudier le coreset et le plus proche voisin Faiss sur du code court | Aucune image de bon sous la main → [[AnomalyCLIP]] |
| | Une mémoire et une latence maîtrisées sur un poste sans GPU : la banque grossit avec le nombre d'images de référence |

## Mise en œuvre

- Installation — dépôt à cloner ; `requirements.txt` (torch, torchvision, faiss-cpu, scikit-learn, scikit-image…) ; Python 3.8 annoncé par le README
- Point d'entrée — `env PYTHONPATH=src python bin/run_patchcore.py` ; exemples `sample_training.sh` et `sample_evaluation.sh`
- Prérequis — MVTec AD téléchargé à part ; Faiss GPU en option (commenté dans `requirements.txt`)
- Exécution — « la majorité des expériences ne dépasse pas 11 Go de mémoire GPU » (README) ; la recherche du plus proche voisin peut tourner sur CPU avec `faiss-cpu`
- Coût — gratuit, Apache-2.0

## Licence et données

- **Code** : Apache-2.0 (API GitHub et README). Le fichier `NOTICE` ne cite aucune licence de tiers.
- **Poids de backbone** : aucune mention de licence trouvée dans le dépôt pour les poids ImageNet ; leur provenance n'a pas été lue dans le code de chargement.
- **Jeu de données** : MVTec AD, CC BY-NC-SA 4.0 — non commercial, voir [[Jeux de données d'anomalies]].
- **Poids de modèles du dépôt** : six sous-dossiers de modèles existent dans `models/` (commit « Add pretrained model files », février 2023), alors que le README garde un lien placeholder (« add link »). Leur contenu n'a pas été listé.

## Limites à connaître

- **Dépôt figé** : pas de version, pas de nouvelle fonctionnalité depuis 2023. La méthode a été portée et maintenue ailleurs ([[anomalib]]).
- **Dépendances anciennes** : Python 3.8 annoncé, `torch>=1.10`, `torchvision>=0.11.1` dans `requirements.txt`.
- Les critiques de la méthode (sensibilité à l'alignement des pièces, mémoire qui croît avec le nombre d'images) sont dans [[Anomalie visuelle par banque de mémoire]].

## Écosystème

### Alternatives

- [[anomalib]] — Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0.
- [[Dinomaly]] — Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0.
- [[AnomalyCLIP]] — Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT.

## Ressources

- Dépôt — https://github.com/amazon-science/patchcore-inspection
- Article — https://arxiv.org/abs/2106.08265

## Voir aussi

- [[Anomalie visuelle par banque de mémoire]] — la notion : SPADE, PaDiM, PatchCore
- [[Détection d'anomalies visuelle]] — le cadre : apprendre sur le bon seul, sortie image et carte pixel
- [[Jeux de données d'anomalies]] — MVTec AD et sa licence
- [[Comparatif - Détection d'anomalies visuelles]] — ce qui départage les quatre outils
