---
role: brique
nom: anomalib
alias: [Anomalib, open-edge-platform/anomalib, openvinotoolkit/anomalib]
pitch: "Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[patchcore-inspection]]", "[[Dinomaly]]", "[[AnomalyCLIP]]"]
complements: []
tags: [industrial-inspection, computer-vision, edge-inference]
url_docs: https://anomalib.readthedocs.io/en/latest/
url_repo: https://github.com/open-edge-platform/anomalib
---

# anomalib

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python (Intel, Open Edge Platform) de détection d'anomalies visuelles — une trentaine de modèles d'images (PatchCore, PaDiM, STFPM, EfficientAD, FastFlow, CFlow, DRAEM, Dinomaly, WinCLIP…) sous PyTorch Lightning, CLI et API Python, jeux MVTec AD, VisA ou dossier maison, export ONNX et OpenVINO ; Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils qui range sous une même interface les méthodes de détection d'anomalies sur images. Chaque modèle est un module PyTorch Lightning ; l'entraînement, l'évaluation, la prédiction et l'export passent par un `Engine` en Python ou par la ligne de commande (`anomalib train --model Patchcore --data anomalib.data.MVTecAD`). La liste des modèles lue sur la branche principale le 2026-10-02 compte une trentaine de noms, dont PatchCore, PaDiM, STFPM, EfficientAd, Fastflow, Cflow, Draem, Dinomaly, WinClip et AnomalyDINO, plus deux modèles vidéo (AI-VAD, FUVAS). Les jeux de données pris en charge vont de MVTec AD, MVTec AD 2, VisA et MVTec LOCO à Real-IAD, plus un lecteur de **dossier maison** (`folder`) pour des images d'atelier. Intérêt central : essayer plusieurs familles de méthodes (voir [[Anomalie visuelle par banque de mémoire]], [[Anomalie visuelle par reconstruction, distillation et flux]], [[Anomalie visuelle zero-shot et few-shot]]) sur ses propres images avec un seul protocole, puis exporter celle qui tient la latence.

Relevé le 2026-10-02 : dernière version `lib/v2.6.2` du 2026-09-11 (cadence : 2.5.0 le 2026-05-29, 2.6.0 le 2026-07-25), dernier commit le jour même, 6 212 étoiles, dépôt non archivé. Le dépôt est un monorepo (étiquettes préfixées `lib/`). Les auteurs déclarés dans `pyproject.toml` sont « Intel OpenVINO ».

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer PatchCore, EfficientAD, FastFlow ou Dinomaly sur ses propres images, même découpage, mêmes métriques | Reproduire à l'identique les chiffres d'un papier : le code de l'auteur reste la référence → [[patchcore-inspection]], [[Dinomaly]] |
| Sortir un modèle vers **OpenVINO** (FP16, ou INT8 par NNCF) pour un PC industriel Intel sans GPU : `ExportType.OPENVINO` | Un seul modèle, une seule dépendance, sans Lightning ni CLI : le dépôt de la méthode suffit |
| Un jeu d'images d'atelier maison, lu par le lecteur `folder` sans passer par un jeu public | Du zero-shot appris par prompts à la manière d’AnomalyCLIP : le dépôt de la méthode reste le point d’entrée → [[AnomalyCLIP]] |
| Un projet qui veut une CLI et des fichiers de configuration plutôt qu'un script par méthode | Un modèle qui ne figure pas dans la liste (UniAD n'y a pas été trouvé le 2026-10-02) |

## Mise en œuvre

- Installation — `uv pip install anomalib` ; variante GPU `uv pip install "anomalib[cu130]"` ; extras `openvino`, `clip`, `vlm`, `cpu`, `rocm`, `xpu`
- Point d'entrée — la CLI `anomalib` (`train`, `predict`, `export`) ou `Engine` en Python ; `Engine.export(model, ExportType.OPENVINO, ...)` accepte aussi `ONNX` et `TORCH`, avec `compression_type` (FP16, INT8_PTQ, INT8_ACQ) pour OpenVINO seulement
- Prérequis — Python 3.10 ou plus ; PyTorch 2.6 ou plus ; Lightning ; timm pour les backbones, dont les poids pré-entraînés sont téléchargés au premier usage (`pre_trained=True` par défaut)
- Exécution — bibliothèque en mémoire ; CPU possible pour l'inférence, GPU pour entraîner les méthodes à réseau
- Coût — gratuit, Apache-2.0 ; les jeux de données ont chacun leur licence

## Licence et données

- **Code** : Apache-2.0 (API GitHub). La version 2.6.2 refuse de charger des tableaux au format pickle ou HDF, qui peuvent exécuter du code à la désérialisation (notes de version).
- **Jeux de données** : le chargeur de MVTec AD porte, dans son code, la mention CC BY-NC-SA 4.0 et télécharge le jeu automatiquement : jeu **non commercial**, qui sert à comparer des méthodes, pas à entraîner un modèle livré à un client. Le chargeur de VisA porte la même mention, alors que la page du jeu annonce CC BY 4.0 (écart non tranché, voir [[Jeux de données d'anomalies]]). La licence des autres jeux n'a pas été relevée.
- **Poids** : les backbones viennent de timm. Leur provenance et leur licence n'ont pas été relevées ; à lire avant une livraison chez un client.

## Limites à connaître

- **Le comparatif intégré n'est pas une garantie de reproduction** : une méthode portée dans la bibliothèque peut s'écarter du code de l'auteur. La documentation de Dinomaly dans anomalib indique une licence MIT pour l'implémentation d'origine, alors que le dépôt d'origine est en Apache-2.0 ; la mention n'a pas été tranchée.
- **Version à épingler** : le dépôt contraint `torch` pour des CVE (CVE-2025-32434, CVE-2025-3001) et exclut deux versions de Lightning (2.6.2 et 2.6.3) dans `pyproject.toml`.

## Écosystème

### Alternatives

- [[patchcore-inspection]] — Implémentation de référence d'Amazon Science de PatchCore (CVPR 2022) — banque de mémoire de patchs d'un WideResNet50, réduite par coreset, puis plus proche voisin (Faiss) au test ; scripts d'entraînement et d'évaluation sur MVTec AD, 99,6 % d'AUROC image annoncés pour l'ensemble ; Apache-2.0, dernier commit de la branche principale en mars 2023.
- [[Dinomaly]] — Code de Dinomaly (CVPR 2025) — détection d'anomalies visuelles multi-classe avec un seul modèle pour toutes les catégories : encodeur DINOv2 à registres gelé, goulot bruité, décodeur à attention linéaire ; 99,6 % d'AUROC image annoncés sur MVTec AD, 98,7 % sur VisA, 89,3 % sur Real-IAD ; points de contrôle fournis, Apache-2.0.
- [[AnomalyCLIP]] — Code d'AnomalyCLIP (ICLR 2024) — détection d'anomalies visuelles zero-shot : CLIP ViT-L/14@336px gelé, deux prompts apprenables indépendants de l'objet (normal, anormal), entraînés sur un jeu auxiliaire puis testés sur des catégories jamais vues ; 91,5 % d'AUROC image annoncés sur MVTec AD ; code sous licence MIT.

## Ressources

- Documentation — https://anomalib.readthedocs.io/en/latest/
- Dépôt — https://github.com/open-edge-platform/anomalib

## Voir aussi

- [[Détection d'anomalies visuelle]] — la notion : ce que la bibliothèque outille
- [[Anomalie visuelle par banque de mémoire]] — PatchCore et PaDiM, ses modèles les plus courants
- [[Anomalie visuelle par reconstruction, distillation et flux]] — STFPM, EfficientAD, FastFlow, Dinomaly
- [[Anomalie visuelle zero-shot et few-shot]] — WinCLIP, AnomalyDINO
- [[OpenVINO]] — le runtime vers lequel exporter pour un poste industriel Intel
- [[Jeux de données d'anomalies]] — MVTec AD, VisA, Real-IAD et leurs licences
- [[Comparatif - Détection d'anomalies visuelles]] — ce qui départage les quatre outils
