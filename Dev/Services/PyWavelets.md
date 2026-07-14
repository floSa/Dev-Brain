---
galaxie: dev
type: service
nom: PyWavelets
alias: [pywt, pywavelets, wavelet transform]
pitch: "Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: C / Cython / Python
scaling: single-node
alternatives: ["[[Dev/Services/scipy.signal|scipy.signal]]"]
remplace_par: []
status: actif
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

- Analyse purement **fréquentielle** (signal stationnaire) → `numpy.fft` ou [[Dev/Services/scipy.signal|scipy.signal]].
- **Filtrage** classique passe-bande / conception FIR-IIR → [[Dev/Services/scipy.signal|scipy.signal]].
- Pipeline **audio** prêt à l'emploi (mel, MFCC) → [[Dev/Services/librosa|librosa]].

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

- [[Dev/Services/scipy.signal|scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

## Liens

- [[Ondelettes]] — la notion (DWT/CWT, multirésolution, seuillage).
- [[Traitement du signal]] — page chapeau.
- [[Dev/Services/scipy.signal|scipy.signal]] — complément filtrage / analyse spectrale.
- [[Dev/Patterns/Comparatif - Traitement du signal|Comparatif — Traitement du signal]]
- Doc : https://pywavelets.readthedocs.io/
