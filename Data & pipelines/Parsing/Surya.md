---
role: brique
nom: Surya
alias: [surya-ocr, Surya OCR, datalab-to/surya, Surya 2]
pitch: "Boîte à outils OCR de Datalab à base d'un modèle vision-langage de 650 millions de paramètres : texte, mise en page avec ordre de lecture et tableaux d'une page en plus de 90 langues ; code Apache-2.0, poids sous OpenRAIL-M modifiée (gratuit sous 5 M$ de revenu ou de financement), servi par vLLM ou llama.cpp."
categorie: data/parsing
famille: paquet
licence_type: source-available
maturite: beta
langage: Python
alternatives: ["[[olmOCR]]", "[[PaddleOCR]]", "[[Indra OCR]]"]
tags: [ocr, document-parsing, layout-analysis, vision-language, self-hosted]
url_docs: https://github.com/datalab-to/surya
url_repo: https://github.com/datalab-to/surya
---

# Surya

<!-- AUTO:BANDEAU:START -->
> Boîte à outils OCR de Datalab à base d'un modèle vision-langage de 650 millions de paramètres : texte, mise en page avec ordre de lecture et tableaux d'une page en plus de 90 langues ; code Apache-2.0, poids sous OpenRAIL-M modifiée (gratuit sous 5 M$ de revenu ou de financement), servi par vLLM ou llama.cpp.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | source-available | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Bibliothèque Python et outils en ligne de commande d'OCR de l'éditeur Datalab : code sous Apache-2.0, poids sous une licence OpenRAIL-M modifiée, gratuite pour un usage personnel ou de recherche et sous 5 M$ de revenu ou de financement (fichiers `LICENSE` et `MODEL_LICENSE` du dépôt, lus le 2026-10-20).** Depuis la version 2, un seul modèle vision-langage de 650 millions de paramètres fait la mise en page avec ordre de lecture, l'OCR et la reconnaissance de tableaux (une génération par page) ; des modèles plus petits restent à part pour la détection de lignes de texte et la détection d'erreurs d'OCR. Le modèle est servi par un serveur que la bibliothèque lance à la demande : vLLM sur GPU NVIDIA (Docker), llama.cpp sur CPU ou Apple Silicon. C'est le moteur sur lequel [[Marker]] est bâti. Dernière version 0.22.1, publiée le 2026-07-20 ; dernier push le 2026-09-11 (relevé du 2026-10-20).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une **mise en page avec ordre de lecture** et des tableaux par un seul modèle, en 90 langues et plus, sur ses propres machines → [[OCR vision-langage en une passe avec grounding]] | Une société de plus de 5 M$ de revenu ou de financement, ou un produit concurrent de Datalab : les poids exigent une licence commerciale |
| Un code Apache-2.0 à intégrer, avec une sortie structurée (blocs, HTML, polygones, confiance par bloc) | Une migration depuis la v1 sans temps pour réécrire : les schémas de sortie ont changé (`text_lines` devient `blocks`, plus de `top_k`, cellules de tableau sans `is_header` ni `colspan`) |
| Un serveur local sur Apple Silicon ou CPU via llama.cpp | Aucun serveur d'inférence à gérer : le gestionnaire lance un conteneur vLLM ou un `llama-server` → [[Indra OCR]] ou [[Tesseract]] |
| Un banc de comparaison avec LightOnOCR-3 ou [[olmOCR]] | Des scores indépendants : le 83,3 % sur olmOCR-bench est annoncé par l'éditeur |

## Mise en œuvre

- Installation — `pip install surya-ocr` (Python 3.10 ou plus, PyTorch, transformers) ; backend d'inférence à part : Docker et NVIDIA Container Toolkit pour vLLM, ou le binaire `llama-server` de llama.cpp (`brew install llama.cpp` sur macOS)
- Point d'entrée — `surya_ocr DATA_PATH` (blocs en JSON), `surya_layout`, `surya_detect`, `surya_gui` (application Streamlit) ; en Python, `SuryaInferenceManager` partagé par `RecognitionPredictor`, `LayoutPredictor` et `TableRecPredictor` ; `--keep_server` laisse le serveur actif entre deux commandes
- Prérequis — un GPU NVIDIA pour vLLM, ou un CPU ou un Mac pour llama.cpp (plus lent) ; la variable `SURYA_INFERENCE_URL` pointe vers un serveur existant
- Exécution — local ou serveur distant compatible OpenAI ; débit réglé par le backend (`--max-num-seqs` pour vLLM, `SURYA_INFERENCE_PARALLEL`) et par la résolution de rendu (de 192 à 96 dpi pour gagner en débit)
- Coût — code gratuit ; poids gratuits dans les limites de `MODEL_LICENSE` ; offre gérée et licence commerciale payantes chez Datalab, citées ici en texte simple

## Limites à connaître

- **Licence des poids** : trois cas excluent l'usage commercial (plus de 5 M$ de revenu l'an passé, plus de 5 M$ levés, produit concurrent de Datalab) ; les deux premiers ne valent pas pour un usage personnel ou de recherche. Le cas d'un consultant qui traite des documents pour le compte d'un client n'est pas tranché par le texte.
- **Scores de l'éditeur, auto-rapportés** (README du 2026-10-20) : 83,3 % sur olmOCR-bench (« le meilleur sous 3 milliards de paramètres »), environ 5 pages par seconde sur une RTX 5090 ; non reproduits par un tiers à notre connaissance.
- **Version 0.x** : le passage à la v2 a changé l'architecture (un VLM à la place de plusieurs réseaux) et les schémas de sortie ; à épingler.
- **Pas de test local** dans les sources du cours de floSa : seule l'existence de l'OCR de Datalab y est citée, comme alternative.

## Écosystème

### Alternatives

- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[Indra OCR]] — OCR de Datalab pour processeur seul : un paquet de petits réseaux ONNX (reconnaisseur latin d'environ 1,25 million de paramètres, 76 Mo au total) qui lit PDF et images en Markdown ou JSON avec boîtes, étiquettes de blocs et ordre de lecture ; code Apache-2.0, poids OpenRAIL-M modifiée (gratuit sous 20 M$ de revenu ou de financement), sans PyTorch ni GPU.
- voisin : [[Marker]] — le convertisseur PDF vers Markdown de Datalab, bâti sur Surya.

## Ressources

- Documentation — https://github.com/datalab-to/surya
- Dépôt — https://github.com/datalab-to/surya
- Documentation — https://github.com/datalab-to/surya/blob/master/MODEL_LICENSE (licence des poids)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR vision-langage en une passe avec grounding]] — la notion : un modèle donne texte, mise en page et boîtes
- [[Évaluer un OCR]] — la notion : lire un score d'éditeur, bancs à vérité terrain
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : le choix entre familles
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
