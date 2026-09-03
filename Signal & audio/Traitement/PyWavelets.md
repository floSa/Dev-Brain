---
role: brique
nom: PyWavelets
alias: [pywt, pywavelets, wavelet transform]
pitch: "Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle."
categorie: signal/traitement
famille: paquet
licence_type: open-source
maturite: production
langage: C / Cython / Python
alternatives: ["[[scipy.signal]]"]
complements: []
tags: [signal-processing, wavelet]
url_docs: https://pywavelets.readthedocs.io/
url_repo: https://github.com/PyWavelets/pywt
---

# PyWavelets

## Pourquoi

Bibliothèque dédiée aux **transformées en ondelettes** en Python (`import pywt`). Implémente la **DWT / IDWT** (et sa version 2D pour l'image), la décomposition **multiniveau** (`wavedec` / `waverec`), la **CWT** (scalogramme), les paquets d'ondelettes et le **seuillage** pour le débruitage. Embarque une large bibliothèque d'**ondelettes mères** (Daubechies, Symlets, Coiflets, Haar, Morlet…). Cœur en C / Cython → rapide. Comble le trou laissé par scipy.signal, qui ne fait pas (plus) d'ondelettes.

## Quand l'utiliser

- Analyse **temps-échelle / multirésolution** d'un signal non stationnaire.
- **Débruitage par seuillage** des coefficients (préserve les ruptures, là où un passe-bas lisse).
- Compression, détection de singularités / transitoires (vibrations, ECG).
- Extraction de features ondelettes avant un modèle ML.

## Quand NE PAS l'utiliser

- Analyse purement **fréquentielle** (signal stationnaire) → `numpy.fft` ou [[scipy.signal]].
- **Filtrage** classique passe-bande / conception FIR-IIR → [[scipy.signal]].
- Pipeline **audio** prêt à l'emploi (mel, MFCC) → [[librosa]].

## Déploiement & coût

- Bibliothèque (`uv add pywavelets`, module `pywt`). MIT, gratuit.
- **Single-node, en mémoire** ; cœur C / Cython compilé, dépend de NumPy.
- Aucune infra.

## Pièges

- Le choix de l'**ondelette mère** et du **niveau** de décomposition conditionne tout — pas de réglage universel.
- Effets de **bord** : le mode de padding (`symmetric`, `periodization`…) change les coefficients aux extrémités.
- La **CWT** est redondante et coûteuse (analyse / visualisation) ; pour compresser ou débruiter, préférer la **DWT**.
- Reconstruire après seuillage : garder la cohérence DWT ↔ IDWT (même ondelette, même mode).

## Alternatives

- [[scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

## Liens

- [[Ondelettes]] — la notion (DWT/CWT, multirésolution, seuillage).
- [[Traitement du signal]] — page chapeau.
- [[scipy.signal]] — complément filtrage / analyse spectrale.
- [[Comparatif - Traitement du signal|Comparatif — Traitement du signal]]
- Doc : https://pywavelets.readthedocs.io/
