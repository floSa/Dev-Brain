---
role: brique
nom: docTR
alias: [doctr, python-doctr, Document Text Recognition, mindee docTR]
pitch: "Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [ocr, document-parsing, layout-analysis, computer-vision, deep-learning]
url_docs: https://mindee.github.io/doctr/
url_repo: https://github.com/mindee/doctr
---

# docTR

<!-- AUTO:BANDEAU:START -->
> Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'OCR de Mindee qui implémente le pipeline **en deux étages**, prêt à l'emploi :
**détection de texte** — DBNet, LinkNet — pour localiser les mots, puis **reconnaissance** —
CRNN, SAR, ViTSTR — pour lire les caractères, avec des modèles pré-entraînés de chaque côté.
Une seule fonction, `ocr_predictor`, enchaîne les deux et restitue le texte **avec sa
position** et sa structure : pages, blocs, lignes, mots. Le backend se choisit explicitement à
l'installation, PyTorch ou TensorFlow, et les deux étages se fine-tunent sur un corpus propre.
Elle s'arrête à la lecture : l'extraction métier — champs, tableaux structurés — n'est pas
dans son périmètre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire le texte de documents — PDF, scans, photos — avec sa position et sa structure | Ordre de lecture non garanti en mise en page complexe (multi-colonnes, tableaux) : la reconstruction de structure reste un post-traitement |
| OCR open-source hors ligne, sans API cloud ni coût à la page | Ne couvre pas l'extraction métier — champs, tableaux structurés — qui est le périmètre payant de Mindee |
| Choisir le backend, PyTorch ou TensorFlow, ou fine-tuner détection et reconnaissance sur son corpus | Texte de scène très varié, multilingue ou manuscrit difficile : les moteurs spécialisés valent mieux, voir [[OCR]] |
| Brique d'un pipeline RAG ou d'extraction documentaire : OCR, puis texte, puis indexation | Compréhension de document de bout en bout — questions-réponses, extraction sémantique → [[Vision Language Models]] |
| | Le choix du backend est explicite à l'installation : se tromper d'extra casse l'import des modèles |
| | Qualité d'entrée déterminante : résolution, contraste, redressement — un document penché ou bruité dégrade la détection |

## Mise en œuvre

- Installation — `uv add python-doctr` avec l'extra du backend voulu ; import `doctr`
- Point d'entrée — `ocr_predictor`, qui enchaîne détection et reconnaissance
- Prérequis — PyTorch ou TensorFlow selon l'extra choisi ; modèles pré-entraînés téléchargés au premier usage
- Exécution — CPU ou GPU, mono-nœud, rien à héberger
- Coût — gratuit, Apache-2.0 ; l'extraction structurée est le périmètre payant de Mindee

## Écosystème

### Alternatives

- Aucune dans le brain : les moteurs OCR concurrents — PaddleOCR, EasyOCR, TrOCR, Tesseract — sont hors périmètre.

## Ressources

- Documentation — https://mindee.github.io/doctr/
- Dépôt — https://github.com/mindee/doctr

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[Détection d'objets]] · [[Segmentation]] — l'étage de détection de texte en est une variante spécialisée
- [[PyTorch]] — l'écosystème d'intégration
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
