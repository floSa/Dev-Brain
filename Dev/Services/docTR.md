---
galaxie: dev
type: service
nom: docTR
alias: [doctr, python-doctr, Document Text Recognition, mindee docTR]
pitch: "Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [ocr, document-parsing, layout-analysis, computer-vision, deep-learning]
url_docs: https://mindee.github.io/doctr/
url_repo: https://github.com/mindee/doctr
---

# docTR

## Pourquoi

Bibliothèque d'**[[OCR]]** (Document Text Recognition) de Mindee, intégrée à l'écosystème [[Dev/Services/PyTorch|PyTorch]] (backend TensorFlow aussi disponible). Implémente le pipeline OCR **en deux étages** prêt à l'emploi : **détection de texte** (DBNet, LinkNet — localiser les mots) puis **reconnaissance** (CRNN, SAR, ViTSTR — lire les caractères), le tout avec **modèles pré-entraînés**. Une fonction (`ocr_predictor`) enchaîne les deux et restitue le texte **avec sa position** et la structure (pages, blocs, lignes, mots). C'est l'OCR open-source clé en main pour numériser des documents, sans assembler soi-même détection et reconnaissance.

## Quand l'utiliser

- Extraire le **texte de documents** (PDF, scans, photos) avec sa **position** et sa structure.
- OCR **open-source hors ligne**, sans API cloud ni coût à la page.
- Besoin de choisir le **backend** (PyTorch ou TensorFlow) ou de **fine-tuner** détection/reconnaissance sur son corpus.
- Brique d'un pipeline RAG/extraction documentaire : OCR → texte → indexation.

## Quand NE PAS l'utiliser

- Texte de **scène** très varié / multilingue (panneaux, devantures) ou manuscrit difficile → moteurs spécialisés (PaddleOCR, EasyOCR, TrOCR — voir [[OCR]]).
- **Compréhension** de document de bout en bout (questions/réponses, extraction sémantique) → un [[Vision Language Models|modèle vision-langage]].
- Simple lecture ponctuelle sans déploiement → un moteur léger type Tesseract (voir [[OCR]]).

## Déploiement & coût

- Bibliothèque Python open-source sous **Apache-2.0** (permissive), gratuite ; `uv add python-doctr` (import `doctr`). Rien à héberger.
- **Backend au choix** : installer la variante PyTorch ou TensorFlow ; modèles pré-entraînés téléchargés au premier usage.
- S'exécute CPU ou GPU ; single-node. Service d'inférence possible (API maison, ou via les produits Mindee pour l'extraction structurée).

## Pièges

- **Choix du backend explicite** à l'installation (extra PyTorch vs TensorFlow) — se tromper d'extra casse l'import des modèles.
- Qualité d'entrée déterminante : résolution, contraste, redressement ; documents penchés ou bruités dégradent la détection.
- **Ordre de lecture** en mise en page complexe (multi-colonnes, tableaux) non garanti — la [[OCR|reconstruction de structure]] reste un post-traitement.
- Couvre détection + reconnaissance, pas l'**extraction métier** (champs, tableaux structurés) — c'est le périmètre payant de Mindee.

## Liens

- [[OCR]] — le concept : deux étages (détection puis reconnaissance), CTC vs attention, CER/WER, panorama des moteurs.
- [[Détection d'objets]] / [[Segmentation]] — l'étage de détection de texte en est une variante spécialisée.
- [[Vision Language Models]] — l'alternative lecture-compréhension de bout en bout.
- [[Dev/Services/PyTorch|PyTorch]] — l'écosystème d'intégration.
- Doc : https://mindee.github.io/doctr/
