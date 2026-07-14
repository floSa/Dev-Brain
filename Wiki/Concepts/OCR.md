---
galaxie: wiki
type: concept
nom: OCR
alias: [reconnaissance optique de caractères, reconnaissance de texte, text recognition, text detection, scene text, Tesseract, PaddleOCR, EasyOCR, docTR, CRNN, CTC, TrOCR, CER, WER]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [ocr, computer-vision, deep-learning]
---

# OCR

## Aperçu

- **Lire le texte présent dans une image** (scan, photo, capture) et le rendre exploitable : une chaîne de caractères, le plus souvent avec sa position.
- Deux régimes très différents : texte **de document** (propre, en lignes) et texte **de scène** (panneaux, devantures, orientations et fonds variés).

## Concepts clés

### Deux étages : détection puis reconnaissance
- **Détection de texte** : localiser les zones de texte. C'est une tâche de [[Détection d'objets|détection]] / [[Segmentation|segmentation]] spécialisée — DBNet, EAST, CRAFT gèrent le texte courbe ou incliné via des masques au pixel.
- **Reconnaissance de texte** : lire les caractères dans chaque crop détecté.

### Reconnaissance : CTC vs attention
- **CRNN + CTC** : CNN (features) → RNN (séquence) → perte **CTC** (Connectionist Temporal Classification) qui aligne sortie et image **sans annotation caractère par caractère**.
- **Seq2seq à attention / transformeur** : décodeur autorégressif (TrOCR) ; meilleur sur texte difficile, plus lourd.

### Moteurs prêts à l'emploi
- **Tesseract** (classique, LSTM depuis la v4), **EasyOCR**, **PaddleOCR**, **docTR**, **TrOCR**. Au-delà du texte brut : [[Métriques vision|analyse de mise en page]], lecture de tableaux, manuscrit (HTR).

### Vers la lecture multimodale
- Les [[Vision Language Models|modèles vision-langage]] lisent le texte d'une image **de bout en bout**, en mélangeant OCR et compréhension — la frontière OCR / extraction documentaire s'estompe.

## Les maths, simplement

- Perte CTC : marginalise sur tous les alignements $\pi$ qui se réduisent à la cible $y$ : $p(y\mid x)=\sum_{\pi\in\mathcal{B}^{-1}(y)}\prod_t p(\pi_t\mid x)$ — gère les longueurs variables et les espacements sans alignement explicite.
- Évaluation : **CER** (Character Error Rate) $= \dfrac{S+D+I}{N}$ (substitutions + délétions + insertions sur $N$ caractères, distance de Levenshtein) ; **WER** au niveau des mots.

## En pratique

- Document propre, hors ligne : **Tesseract** ou [[Dev/Services/docTR|docTR]]. Texte de scène / multilingue : **PaddleOCR**, **EasyOCR**. Manuscrit ou difficile : **TrOCR** / un VLM.
- Pipeline RAG sur PDF scannés : OCR → texte → indexation (voir [[Recherche d'information]]).
- Pièges : qualité d'image (résolution, contraste) ; ordre de lecture en multi-colonnes ; jeux de caractères et langues non latines.

## Approches voisines & alternatives

- [[Détection d'objets]] / [[Segmentation]] — l'étage de détection de texte en est une variante.
- [[Vision Language Models]] — lecture de texte de bout en bout, alternative moderne au pipeline en deux étages.
- [[Recherche d'information]] / [[Traitement du langage naturel]] — ce qui consomme le texte une fois extrait.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Shi et al. (2015) — *CRNN* · Graves et al. (2006) — *CTC*.
- Li et al. (2021) — *TrOCR* (reconnaissance par transformeur).
