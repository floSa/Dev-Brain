---
galaxie: wiki
type: concept
nom: STFT et spectrogramme
alias: [STFT, spectrogramme, short-time Fourier transform, mel-spectrogramme, MFCC, mel spectrogram]
categorie: concept/signal
domaines: [data-sci, ml-eng]
tags: [signal-processing, spectrogram, fourier]
---

# STFT et spectrogramme

## Aperçu

- **STFT** (Short-Time Fourier Transform) : découpe le signal en fenêtres courtes qui se chevauchent et applique une [[Transformée de Fourier]] sur chacune → le contenu fréquentiel **en fonction du temps**.
- **Spectrogramme** : $|STFT|^2$ affiché comme une image temps × fréquence. C'est la représentation de référence pour l'audio et les signaux non stationnaires.

## Concepts clés

### Fenêtre & chevauchement
- La **taille de fenêtre** est le compromis central : longue → bonne résolution fréquentielle mais mauvaise en temps ; courte → l'inverse. Le **chevauchement** (hop) lisse l'évolution temporelle. Une fenêtre d'apodisation (Hann…) limite la fuite — cf. [[Filtrage numérique]].

### Compromis temps-fréquence fixe
- Contrairement aux [[Ondelettes]], la résolution est **la même à toutes les fréquences** (fenêtre constante). C'est la limite et la simplicité de la STFT.

### Mel-spectrogramme
- Spectrogramme reprojeté sur l'**échelle mel**, qui imite la perception auditive : résolution fine en bas du spectre, grossière en haut. Standard en audio et en parole.

### MFCC
- *Mel-Frequency Cepstral Coefficients* : on prend le **log** du mel-spectrogramme puis une **DCT**, et on garde les premiers coefficients. Résultat : des features **compactes et décorrélées**, longtemps reines de la reconnaissance vocale, encore utiles comme baseline et comme features ML légères.

## Les maths, simplement

- $STFT\{x\}(m,k) = \sum_n x[n]\, w[n - mH]\, e^{-i 2\pi k n / N}$ : FFT du signal fenêtré par $w$ à la trame $m$ (décalage $H$ = hop). Spectrogramme $= |STFT|^2$.
- MFCC : $c = \mathrm{DCT}\big(\log(\mathrm{Mel}\,|STFT|^2)\big)$ — la DCT décorrèle les bandes mel.

## En pratique

- [[Dev/Services/scipy.signal|scipy.signal]] (`stft`, `spectrogram`) ; [[Dev/Services/librosa|librosa]] (`melspectrogram`, `mfcc`) pour l'audio.
- Réglages clés : `n_fft` (résolution fréquentielle), `hop_length` (résolution temporelle), choix de fenêtre.
- Beaucoup de modèles audio (CNN, transformers) prennent le **mel-spectrogramme** en entrée plutôt que la forme d'onde brute.

## Approches voisines & alternatives

- [[Transformée de Fourier]] — la brique de base (une FFT par fenêtre).
- [[Ondelettes]] — alternative temps-fréquence à résolution **adaptative**.
- [[Filtrage numérique]] — fenêtrage d'apodisation et bancs de filtres mel.
- [[Classification audio par spectrogramme]] — application directe : le mel-spectrogramme en entrée d'un CNN.
- [[Time series feature engineering]] — les features spectrales/MFCC alimentent les modèles ML.
- [[Stationarity]] — la STFT existe précisément parce que le signal n'est pas stationnaire.
- [[Traitement du signal]] — page chapeau.

## Pour aller plus loin

- Documentation `librosa` — spectrogrammes, mel, MFCC.
- Davis & Mermelstein (1980) — coefficients MFCC pour la reconnaissance vocale.
