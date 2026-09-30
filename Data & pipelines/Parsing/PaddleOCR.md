---
role: brique
nom: PaddleOCR
alias: [paddleocr, PaddlePaddle OCR, PP-OCR, PP-OCRv5, PP-OCRv6, PP-StructureV3, PaddleOCR-VL]
pitch: "Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[docTR]]", "[[Tesseract]]", "[[EasyOCR]]", "[[olmOCR]]", "[[MinerU]]"]
complements: []
tags: [ocr, document-parsing, layout-analysis, table-extraction, computer-vision, deep-learning]
url_docs: https://www.paddleocr.ai/latest/en/index.html
url_repo: https://github.com/PaddlePaddle/PaddleOCR
---

# PaddleOCR

<!-- AUTO:BANDEAU:START -->
> Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils de **Baidu**, bâtie sur son framework PaddlePaddle, qui couvre trois étages. Le
**pipeline OCR** enchaîne des modules optionnels — orientation du document, redressement,
orientation des lignes — puis une **détection** et une **reconnaissance** obligatoires ; le
modèle par défaut, PP-OCRv6, existe en trois tailles, de 1,5 à 34,5 millions de paramètres.
**PP-StructureV3** ajoute l'analyse de mise en page, les tableaux avec ou sans bordures, les
formules et les sceaux, avec des sorties JSON, Markdown et Word. **PaddleOCR-VL** est un modèle
vision-langage d'environ 0,9 milliard de paramètres qui lit chaque région détectée ; il ne
s'emploie qu'avec son pipeline complet, la doc prévenant que le modèle seul produit du texte
halluciné. Les chiffres de PaddleOCR-VL et de PP-OCRv6 sont publiés par l'équipe Paddle
elle-même.

*Constat du 2026-09-30 :* dernière version 3.7.0, publiée le 2026-06-11 (une release toutes les deux à quatre semaines) ; environ 90,4 k étoiles GitHub, dernier push le 2026-09-16.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| OCR de production sur de nombreuses langues — le modèle unifié couvre le chinois, l'anglais, le japonais et 46 langues latines — avec CPU, GPU, XPU ou NPU | Dépendance lourde : PaddlePaddle à installer à part (ou Transformers ≥ 5.10), plus `paddlex` |
| Tableaux, formules et mise en page dans le même outil que l'OCR, sous Apache 2.0, sans service cloud | Le modèle par défaut de PP-StructureV3 est gourmand et lent sur du matériel modeste |
| Parsing de documents par modèle vision-langage compact, exécutable en local | PaddleOCR-VL : GPU NVIDIA de capacité ≥ 7.0 (≥ 8.0 sous vLLM ou SGLang) ; les scores sont auto-déclarés |
| Choisir le moteur d'inférence (Paddle, Transformers) selon l'infrastructure | Manuscrit faible : environ 58 % de précision sur PP-OCRv5_server_rec, en chinois comme en anglais |
| | Besoin d'un OCR minimal, sans framework de deep learning → [[Tesseract]] ; prototype Python en trois lignes → [[EasyOCR]] ; écosystème PyTorch et fine-tuning → [[docTR]] |
| | PDF limité aux 10 premières pages par défaut : à relever explicitement |

## Mise en œuvre

- Installation — `pip install paddleocr`, qui tire `paddlex[ocr-core]` ; extras `paddleocr[doc-parser]` et `paddleocr[all]` ; PaddlePaddle ≥ 3.0 à installer séparément avec le backend Paddle
- Point d'entrée — `PaddleOCR(...).predict("image.png")` en Python ; CLI `paddleocr ocr -i image.png` ; moteur d'inférence au choix : `paddle`, `paddle_static`, `paddle_dynamic` ou `transformers`
- Prérequis — Python 3.8 ou plus pour le cœur (3.9 pour les extras) ; PaddlePaddle ou Transformers ; modèles téléchargés au premier usage
- Exécution — CPU, GPU, XPU ou NPU, mono-nœud ; service via vLLM, SGLang ou FastDeploy pour PaddleOCR-VL
- Coût — gratuit, Apache-2.0 pour le code et pour les modèles lus (PaddleOCR-VL, PP-OCRv5)

## Écosystème

### Alternatives

- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux.
- [[EasyOCR]] — Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024.
- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.
- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.

## Ressources

- Documentation — https://www.paddleocr.ai/latest/en/index.html
- Documentation — https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html
- Documentation — https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html
- Papier — https://arxiv.org/abs/2510.14528 (PaddleOCR-VL, Baidu, 2025)
- Dépôt — https://github.com/PaddlePaddle/PaddleOCR

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
