---
role: brique
nom: Tesseract
alias: [tesseract-ocr, Tesseract OCR, pytesseract]
pitch: "Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux."
categorie: data/parsing
famille: cli
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[docTR]]", "[[PaddleOCR]]", "[[EasyOCR]]"]
complements: ["[[PyMuPDF]]", "[[Docling]]", "[[Unstructured]]"]
tags: [ocr, document-parsing, pdf]
url_docs: https://tesseract-ocr.github.io/tessdoc/
url_repo: https://github.com/tesseract-ocr/tesseract
---

# Tesseract

<!-- AUTO:BANDEAU:START -->
> Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI C++ | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de reconnaissance de caractères écrit en **C++**, maintenu depuis plus de dix ans et
présent dans les paquets de toutes les distributions Linux. Depuis la 4.0, la reconnaissance
repose sur un **réseau LSTM** appliqué ligne par ligne ; l'ancien moteur à base de formes
n'est disponible qu'avec le dépôt de modèles historique `tessdata`. Il s'invoque d'abord en
**commande shell** (`tesseract image sortie`), une API C/C++ existant à côté, et restitue du
texte, du hOCR, du TSV (position mot par mot), de l'ALTO, du PAGE XML ou un **PDF cherchable**.
Les langues se chargent par fichiers `.traineddata`. Il ne fait que **lire des lignes de
texte** : ni tableaux structurés, ni ordre de lecture en mise en page complexe, ni Markdown.
La doc elle-même conditionne la qualité à l'image d'entrée — 300 dpi au moins, binarisation,
redressement.

*Constat du 2026-09-30 :* dernière version 5.5.3, publiée le 2026-07-24, une version de maintenance (correctifs mémoire et sécurité sur la lecture des `traineddata`) ; environ 76,8 k étoiles GitHub, dernier commit le 2026-09-28.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| OCR de texte imprimé propre, sur CPU seul, sans dépendance à PyTorch ou à PaddlePaddle | Scan dégradé, penché ou bruité sans pré-traitement : la segmentation de lignes se dégrade nettement, la doc recommande de redresser et binariser |
| Produire un **PDF cherchable** ou du hOCR / ALTO à partir de scans | Tableaux, formules, mise en page multi-colonnes à restituer → [[Docling]] |
| Empreinte minimale, installation par le gestionnaire de paquets, licence permissive | Texte de scène, écritures non latines difficiles ou meilleure précision attendue → [[PaddleOCR]] ou [[docTR]] |
| Brique d'OCR branchée derrière un autre outil — [[PyMuPDF]], [[Docling]], [[Unstructured]] savent l'appeler | Manuscrit : la doc dit que le résultat sera médiocre, le moteur étant conçu pour l'imprimé |
| | Pas de GPU exploitable : le calcul est limité au CPU, par threads OpenMP |

## Mise en œuvre

- Installation — `apt install tesseract-ocr` plus un paquet par langue (`tesseract-ocr-fra`), `brew install tesseract` sur macOS, installeur tiers sous Windows ; wrapper Python `pytesseract` (paquet séparé, Apache 2.0)
- Point d'entrée — commande `tesseract <image> <sortie> -l fra+eng`, avec `--psm` pour le mode de segmentation de page ; API C/C++ `libtesseract`
- Prérequis — bibliothèque Leptonica ; fichiers `traineddata` au choix : `tessdata_fast` (défaut des distributions), `tessdata_best` (plus précis, seul utilisable pour le fine-tuning), `tessdata` (historique)
- Exécution — CPU seul, mono-nœud, multithread OpenMP
- Coût — gratuit, Apache-2.0, y compris les modèles `tessdata_best`

## Écosystème

### Alternatives

- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[EasyOCR]] — Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024.

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — son OCR intégré s'appuie sur Tesseract, à installer à part.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local. — l'un des moteurs OCR que Docling sait brancher, en ligne de commande ou via tesserocr.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG. — l'OCR dont son parsing avancé dépend comme binaire système.

## Ressources

- Documentation — https://tesseract-ocr.github.io/tessdoc/
- Documentation — https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
- Documentation — https://tesseract-ocr.github.io/tessdoc/Data-Files.html
- Dépôt — https://github.com/tesseract-ocr/tesseract

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
