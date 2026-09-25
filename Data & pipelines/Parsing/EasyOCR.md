---
role: brique
nom: EasyOCR
alias: [easyocr, JaidedAI EasyOCR, Jaided AI]
pitch: "Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[docTR]]", "[[PaddleOCR]]", "[[Tesseract]]"]
complements: ["[[Docling]]", "[[pypdfium2]]"]
tags: [ocr, document-parsing, computer-vision, deep-learning]
url_docs: https://www.jaided.ai/easyocr/documentation/
url_repo: https://github.com/JaidedAI/EasyOCR
---

# EasyOCR

<!-- AUTO:BANDEAU:START -->
> Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python d'OCR de **Jaided AI**, conçue pour lire une image en quelques lignes :
`easyocr.Reader(['fr', 'en'])` puis `readtext`. Le pipeline est en **deux étages** — détection
du texte par **CRAFT** (DBNet en option), puis reconnaissance par un **CRNN** à décodage CTC —
et couvre plus de 80 langues, dont des écritures non latines. La sortie est une liste de
triplets (boîte, texte, confiance). C'est là que s'arrête le périmètre : **pas de tableaux, pas
de mise en page, pas de Markdown, pas de PDF cherchable**. Le manuscrit, annoncé « à venir »
dans le README, n'existe pas. Le projet est très utilisé, mais peu entretenu : sa dernière
release date de septembre 2024.

*Constat du 2026-09-30 :* dernière version 1.7.2, publiée le 2024-09-24 ; environ 30 k étoiles GitHub, dernier commit le 2025-12-05.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototyper un OCR multilingue en quelques lignes de Python, sans binaire système | Maintenance ralentie : aucune release depuis septembre 2024, un seul commit cosmétique en 2025, des centaines d'issues ouvertes |
| Lire du texte court — étiquettes, plaques, captures, photos — avec boîtes et confiance par zone | Documents structurés — tableaux, colonnes, ordre de lecture → [[Docling]] ou [[PaddleOCR]] |
| Déjà dans un environnement PyTorch : pas de second framework à installer | Corpus de PDF à volume élevé, précision de référence attendue → [[PaddleOCR]] ou [[docTR]] |
| Brique d'OCR branchée derrière [[Docling]], qui sait l'appeler | Aucune vitesse ni précision chiffrée dans la documentation officielle : la qualité se mesure sur ses propres documents, face à [[Tesseract]] ou [[PaddleOCR]] |
| | Modèles téléchargés au premier lancement dans `~/.EasyOCR` : à pré-placer en environnement sans accès réseau |

## Mise en œuvre

- Installation — `pip install easyocr` ; sous Windows, installer PyTorch et torchvision d'abord ; un Dockerfile est fourni
- Point d'entrée — `reader = easyocr.Reader(['fr', 'en'])` puis `reader.readtext('image.jpg')`
- Prérequis — PyTorch, OpenCV, Pillow, scikit-image ; modèles récupérés au premier usage
- Exécution — GPU par défaut, CPU avec `gpu=False`, mono-nœud
- Coût — gratuit, Apache-2.0 pour le code ; aucune licence explicite n'a été trouvée pour les poids téléchargés, au-delà de celle du dépôt

## Écosystème

### Alternatives

- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee, sur PyTorch — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés, et depuis la 1.1.0 analyse de mise en page, structure de tableaux et exports Markdown ; l'OCR open-source clé en main pour documents.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux.

### Compléments

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local. — l'étage de conversion structurée, qui l'accepte comme moteur OCR.
- [[pypdfium2]] — Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page. — rend la page PDF en image pour cet OCR qui lit des images.

## Ressources

- Documentation — https://www.jaided.ai/easyocr/documentation/
- Dépôt — https://github.com/JaidedAI/EasyOCR

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : quand un pipeline en étages, quand un modèle vision-langage, et comment chacun échoue
- [[PyTorch]] — l'écosystème d'intégration
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
