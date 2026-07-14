---
galaxie: dev
type: service
nom: scipy.signal
alias: [scipy, scipy signal, scipy.fft]
pitch: "Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: C / Fortran / Python
scaling: single-node
alternatives: ["[[Dev/Services/PyWavelets|PyWavelets]]", "[[Dev/Services/librosa|librosa]]"]
remplace_par: []
status: actif
tags: [signal-processing, digital-filter, fourier, spectrogram]
url_docs: https://docs.scipy.org/doc/scipy/reference/signal.html
url_repo: https://github.com/scipy/scipy
---

# scipy.signal

## Pourquoi

Sous-module de **SciPy** dédié au traitement du signal numérique, bâti sur les `ndarray` de [[Dev/Services/numpy|numpy]]. Couvre la **conception et l'application de filtres** (FIR/IIR — Butterworth, Chebyshev, elliptique ; `filtfilt` à phase nulle), l'**analyse spectrale** (`periodogram`, `welch`, `stft`, `spectrogram`), la **convolution / corrélation**, la **détection de pics**, le **ré-échantillonnage** et les **fenêtres d'apodisation**. La boîte à outils DSP de référence en Python scientifique, sans dépendance lourde.

## Quand l'utiliser

- Filtrer un signal (passe-bas / haut / bande), concevoir un FIR ou un IIR.
- Estimer un spectre ou un spectrogramme (Welch, STFT).
- Convolution, corrélation, détection de pics, ré-échantillonnage.
- Prétraiter des signaux de capteurs / séries physiques avant un modèle ML.

## Quand NE PAS l'utiliser

- Analyse **temps-échelle par ondelettes** → [[Dev/Services/PyWavelets|PyWavelets]] (SciPy a retiré ses fonctions d'ondelettes).
- Pipeline **audio / musique** de haut niveau (mel, MFCC, tempo, chargement de fichiers) → [[Dev/Services/librosa|librosa]].
- Simple **FFT** sans traitement → `numpy.fft` / `scipy.fft` suffit.

## Déploiement & coût

- Bibliothèque (`uv add scipy`) ; le module fait partie de SciPy. BSD-3-Clause, gratuit.
- **Single-node, en mémoire** ; cœur compilé en C / Fortran / Cython, s'appuie sur BLAS/LAPACK.
- Aucune infra : tourne partout où NumPy tourne.

## Pièges

- **Normaliser la coupure par la fréquence de Nyquist** ($f_s/2$) — erreur classique de `butter`.
- Préférer le format **SOS** (`sosfilt`) au format `(b, a)` pour la stabilité numérique des filtres d'ordre élevé.
- `filtfilt` double l'ordre effectif et exige des bords assez longs (gestion des transitoires).
- Ondelettes : `scipy.signal.cwt` / `ricker` sont **dépréciés / retirés** → passer à [[Dev/Services/PyWavelets|PyWavelets]].

## Alternatives

- [[Dev/Services/PyWavelets|PyWavelets]] — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- [[Dev/Services/librosa|librosa]] — Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.

## Liens

- [[Filtrage numérique]] — FIR/IIR, Butterworth, fenêtrage : le cœur du module.
- [[Transformée de Fourier]] — `periodogram` / `welch` pour l'estimation spectrale.
- [[STFT et spectrogramme]] — `stft` / `spectrogram`.
- [[Traitement du signal]] — page chapeau.
- [[Dev/Services/numpy|numpy]] — socle `ndarray` sur lequel il opère.
- [[Dev/Patterns/Comparatif - Traitement du signal|Comparatif — Traitement du signal]]
- Doc : https://docs.scipy.org/doc/scipy/reference/signal.html
