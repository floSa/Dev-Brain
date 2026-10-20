---
role: brique
nom: Indra OCR
alias: [indra-ocr, Indra, datalab-to/indra, indra OCR 1M]
pitch: "OCR de Datalab pour processeur seul : un paquet de petits réseaux ONNX (reconnaisseur latin d'environ 1,25 million de paramètres, 76 Mo au total) qui lit PDF et images en Markdown ou JSON avec boîtes, étiquettes de blocs et ordre de lecture ; code Apache-2.0, poids OpenRAIL-M modifiée (gratuit sous 20 M$ de revenu ou de financement), sans PyTorch ni GPU."
categorie: data/parsing
famille: paquet
licence_type: source-available
maturite: beta
langage: Python
alternatives: ["[[Tesseract]]", "[[PaddleOCR]]", "[[docTR]]", "[[Surya]]"]
tags: [ocr, document-parsing, pdf, layout-analysis, edge-inference, self-hosted]
url_docs: https://github.com/datalab-to/indra
url_repo: https://github.com/datalab-to/indra
---

# Indra OCR

<!-- AUTO:BANDEAU:START -->
> OCR de Datalab pour processeur seul : un paquet de petits réseaux ONNX (reconnaisseur latin d'environ 1,25 million de paramètres, 76 Mo au total) qui lit PDF et images en Markdown ou JSON avec boîtes, étiquettes de blocs et ordre de lecture ; code Apache-2.0, poids OpenRAIL-M modifiée (gratuit sous 20 M$ de revenu ou de financement), sans PyTorch ni GPU.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Paquet | source-available | en ligne de commande, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Outil en ligne de commande et bibliothèque Python d'OCR pour processeur seul, de l'éditeur Datalab : code sous Apache-2.0, poids sous une licence OpenRAIL-M modifiée, gratuite pour un usage personnel ou de recherche et sous 20 M$ de revenu ou de financement, mais pas pour un produit concurrent de Datalab.** Ce n'est pas un seul modèle : un paquet de réseaux ONNX (détection de lignes, reconnaissance latine, CJK, de droite à gauche et autres écritures, classeur d'écriture, ordre de lecture, orientation), dont le reconnaisseur latin compte environ 1,25 million de paramètres et dont l'ensemble pèse 76 Mo par défaut. Il rend du Markdown, du texte ou du JSON (boîtes, étiquettes, confiance par ligne, ordre de lecture). Sur un PDF numérique, il **lit la couche de texte** quand elle passe ses contrôles et ne fait l'OCR que du reste. Relevé le 2026-10-20 : version 1.1.2 (PyPI le 2026-10-20), annoncé le 2026-10-13 en version 0.3.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un gros volume d'imprimé propre, de formulaires, de pages tournées, sur machines **sans GPU** (indexation, recherche, RAG) | Manuscrit, reçus, tableaux à cellules fusionnées ou à texte sur plusieurs lignes, scans anciens : l'éditeur lui-même renvoie vers son offre payante → [[LightOnOCR-3]], [[olmOCR]] |
| Une **première passe** rapide avant un gros modèle sur les seules pages douteuses → [[Cascade OCR et contrôle arithmétique des factures]] | Une livraison à un client ou un produit dans une société de plus de 20 M$ de revenu ou de financement : les poids ne sont pas libres (le cas d'un consultant qui traite des documents pour un client n'est pas tranché par les textes, à faire valider) |
| Une installation en une ligne, sans PyTorch, sur Linux ou Mac Apple Silicon | Une écriture hors des quatre recognizers : le texte d'une image reste faux, seule la couche d'un PDF numérique passe → [[Couche de texte d'un PDF contre OCR]] |
| Des boîtes de lignes et de blocs, une étiquette et un ordre de lecture sans GPU | Un paquet jeune, qui bouge vite : six versions en une semaine, journal des modifications à relire avant tout usage |

## Mise en œuvre

- Installation — `pip install indra-ocr` (Python 3.10 ou plus ; ONNX Runtime, OpenCV et pypdfium2, sans PyTorch) ; le premier lancement télécharge environ 76 Mo de modèles depuis Hugging Face, puis les met en cache ; `INDRA_OCR_MODEL_DIR` pour un dossier local, hors ligne
- Point d'entrée — `indra-ocr paper.pdf` (Markdown sur la sortie standard), `indra-ocr *.pdf --out results/`, `--format json` pour lignes, boîtes et confiances, `--mode auto|ocr|text`, `--math` pour les formules ; `indra-ocr-viewer` ouvre une visionneuse locale ; en Python, `indra_ocr.load(threads=4)` puis `conv.convert("paper.pdf")`
- Prérequis — CPU seul ; Linux x86_64 et aarch64, macOS Apple Silicon (testé sur Python 3.10 à 3.13)
- Exécution — local : un processus mono-fil par cœur (`--cores` pour limiter), une page par tâche ; aucun service à héberger
- Coût — code gratuit sous Apache-2.0 ; poids gratuits sous OpenRAIL-M modifiée dans les limites de la licence (usage commercial exclu au-delà de 20 M$ de revenu ou de financement levé, ou face à Datalab) ; licence commerciale et service géré payants chez Datalab, cités ici en texte simple

## Limites à connaître

- **Licence des poids, lue le 2026-10-20** (fichier `LICENSE` du dépôt Hugging Face) : trois cas indépendants excluent l'usage commercial : plus de 20 M$ de revenu l'an passé, plus de 20 M$ levés en capital ou en dette, ou un produit ou service concurrent de Datalab. Les deux premiers ne valent pas pour un usage personnel ou de recherche. Le code, lui, est sous Apache-2.0.
- **Chiffres de l'éditeur, auto-rapportés, relevés le 2026-10-20** (version 1.1) : score global de 66,7 sur OmniParseBench (71,4 avec `--math`), contre 58,4 pour PP-StructureV3 ; environ 44 pages par seconde sur 32 cœurs x86 et environ 210 ms par page sur 4 cœurs. **OmniParseBench est un benchmark de l'éditeur**, créé le 2026-10-09 ; moteur et juge sont du même éditeur ; aucune reproduction tierce trouvée au 2026-10-15. Sans `--math`, PP-StructureV3 lit mieux le texte brut.
- **Test local d'un tiers sur la version 0.3.2** (vidéo AI WITH Rithesh, 2026-10-15, MacBook Air M5 24 Go, 23 pages fabriquées, 20 lignes manuscrites) : 64 ms par page isolée, 25,2 pages/s sur 10 cœurs ; CER de 0 à 3,3 % sur imprimé propre et pages tournées (Tesseract : 31,4 à 83,9 % sur trois des quatre pages) ; **40,7 % sur un ticket** (l'ordre, pas la reconnaissance), 49,6 % sur le manuscrit, 88,1 % sur du kannada en image, une équation sur quatre ; nombres de tableaux justes à 100 % mais forme défaite (9 lignes lues pour 5). La version 1.1 a changé les modèles depuis (manuscrit annoncé à 25,2 % de tests réussis contre 8,3 % en 0.3) : ces mesures sont à refaire.
- **Le « 1 million de paramètres » est le reconnaisseur latin**, non le paquet ; avec les modèles par défaut le total est de 7,3 millions de paramètres d'après le README de la 1.1.
- **Lignes peu sûres** : une ligne reconnue avec une confiance moyenne sous 0,5 garde sa boîte et perd son texte (journal de la 0.3.0) : un tri par confiance doit compter les lignes vides. La calibration de la confiance n'est démontrée nulle part.
- **Limites déclarées** (README du 2026-10-20) : tableaux complexes, manuscrit, scans dégradés (29,5 % de tests réussis), écritures hors liste, formules sans `--math`, pages très larges, dessins techniques.
- **Données d'entraînement non documentées** : l'éventuel recouvrement avec des jeux publics (IAM) n'est pas exclu.

## Écosystème

### Alternatives

- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee, sur PyTorch — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés, et depuis la 1.1.0 analyse de mise en page, structure de tableaux et exports Markdown ; l'OCR open-source clé en main pour documents.
- [[Surya]] — Boîte à outils OCR de Datalab à base d'un modèle vision-langage de 650 millions de paramètres : texte, mise en page avec ordre de lecture et tableaux d'une page en plus de 90 langues ; code Apache-2.0, poids sous OpenRAIL-M modifiée (gratuit sous 5 M$ de revenu ou de financement), servi par vLLM ou llama.cpp.

## Ressources

- Documentation — https://github.com/datalab-to/indra
- Dépôt — https://github.com/datalab-to/indra
- Article — https://www.datalab.to/blog/indra-ocr (Datalab, 2026-10-13, éditeur)
- Documentation — https://huggingface.co/datalab-to/indra-ocr (fiche du modèle et `LICENSE` des poids)
- Vidéo — https://www.youtube.com/watch?v=wXvJeofdAFQ (AI WITH Rithesh, 2026-10-15, test local sur MacBook Air M5)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Couche de texte d'un PDF contre OCR]] — la notion : quand lire la couche, quand reconnaître l'image
- [[Cascade OCR et contrôle arithmétique des factures]] — la notion : Indra d'abord, un gros modèle ensuite
- [[Évaluer un OCR]] — la notion : CER, benchmark de l'éditeur, banc à vérité terrain
- [[OCR]] — la notion : deux étages, CTC contre attention (le reconnaisseur d'Indra est de type CTC)
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : le choix entre familles
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
