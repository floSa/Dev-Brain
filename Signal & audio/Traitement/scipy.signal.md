---
role: brique
nom: scipy.signal
alias: [scipy, scipy signal, scipy.fft]
pitch: "Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy."
categorie: signal/traitement
famille: paquet
licence_type: open-source
maturite: production
langage: C / Fortran / Python
alternatives: ["[[PyWavelets]]", "[[librosa]]"]
complements: []
tags: [signal-processing, digital-filter, fourier, spectrogram]
url_docs: https://docs.scipy.org/doc/scipy/reference/signal.html
url_repo: https://github.com/scipy/scipy
---

# scipy.signal

<!-- AUTO:BANDEAU:START -->
> Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C / Fortran / Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-21 |
<!-- AUTO:BANDEAU:END -->

## Définition

Sous-module de SciPy dédié au traitement du signal numérique, bâti sur les `ndarray`
de NumPy. Il couvre la conception et l'application de filtres FIR/IIR — Butterworth,
Chebyshev, elliptique, `filtfilt` à phase nulle —, l'analyse spectrale (`periodogram`,
`welch`, `stft`, `spectrogram`), la convolution et la corrélation, la détection de pics,
le ré-échantillonnage et les fenêtres d'apodisation. Deux conventions structurent tout
usage : la fréquence de coupure se **normalise par la fréquence de Nyquist** ($f_s/2$),
erreur classique de `butter`, et le format **SOS** (`sosfilt`) est numériquement plus
stable que le couple `(b, a)` dès que l'ordre du filtre monte. Ses fonctions d'ondelettes
(`cwt`, `ricker`) sont dépréciées ou retirées : le module ne couvre plus le temps-échelle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Filtrer un signal (passe-bas, passe-haut, passe-bande) ou concevoir un FIR ou un IIR | Simple FFT sans traitement autour : `numpy.fft` et `scipy.fft` couvrent déjà le besoin → [[numpy]] |
| Estimer un spectre ou un spectrogramme (Welch, STFT) | Signal trop court : `filtfilt` double l'ordre effectif et exige des bords assez longs pour absorber les transitoires |
| Convolution, corrélation, détection de pics, ré-échantillonnage | |
| Prétraiter des signaux de capteurs ou des séries physiques avant un modèle ML | |

## Mise en œuvre

- Installation — `uv add scipy` ; le module est livré avec SciPy, il ne s'installe pas seul
- Point d'entrée — import Python, `from scipy import signal`
- Prérequis — NumPy ; cœur compilé en C, Fortran et Cython, appuyé sur BLAS/LAPACK
- Exécution — dans le process appelant, CPU, en mémoire ; rien à héberger
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[PyWavelets]] — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- [[librosa]] — Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.

## Ressources

- Documentation — https://docs.scipy.org/doc/scipy/reference/signal.html
- Dépôt — https://github.com/scipy/scipy

## Voir aussi

- [[Traitement du signal]] — la notion du dossier
- [[Filtrage numérique]] — FIR/IIR, Butterworth, fenêtrage : le cœur du module
- [[Transformée de Fourier]] — la notion derrière `periodogram` et `welch`
- [[STFT et spectrogramme]] — la notion derrière `stft` et `spectrogram`
- [[Comparatif - Traitement du signal]] — ce qui départage les outils du dossier
