---
role: hub
nom: Signal & audio
alias: [signal, audio, dsp]
pitch: Analyser un signal échantillonné — le décomposer en fréquences, le filtrer, en tirer des descripteurs.
domaines: [data-sci, ml-eng]
tags: [signal-processing, wavelet, spectrogram, fourier, audio-classification]
---

# Signal & audio

> Analyser un signal échantillonné — le décomposer en fréquences, le filtrer, en tirer des descripteurs.

## Ce qu'il faut comprendre

- Un signal se lit dans deux domaines, et le choix de l'un ou de l'autre décide de tout le reste. Le **temps** dit *quand* ; la **fréquence** dit *de quoi c'est fait*. La [[Transformée de Fourier]] passe de l'un à l'autre, la [[STFT et spectrogramme]] fait le compromis entre les deux, les [[Ondelettes]] l'ajustent selon l'échelle.
- Le domaine est le **socle de l'audio** mais ne s'y limite pas : capteurs industriels, vibrations, séries de mesures physiques relèvent des mêmes outils. En revanche la modélisation d'une série *économique* ou *métier* est du ressort des séries temporelles, pas du traitement du signal.
- Deux niveaux de brique cohabitent. La **boîte à outils générique** ([[scipy.signal]], [[PyWavelets]]) fournit les transformées et les filtres, sans rien savoir de l'audio. La **bibliothèque de domaine** ([[librosa]]) ajoute les descripteurs que l'audio attend — MFCC, chroma, tempo, découpage en trames — et les valeurs par défaut qui vont avec.

## Choisir

- Filtrage, convolution, corrélation, ré-échantillonnage, transformées classiques → [[scipy.signal]], le socle.
- Analyse multi-échelle (débruitage, compression, transitoires) → [[PyWavelets]].
- Audio : extraction de descripteurs pour de la classification, du tempo, de la séparation → [[librosa]], qui s'appuie de toute façon sur SciPy.
- Les notions du domaine ([[Traitement du signal]], [[Filtrage numérique]], [[Transformée de Fourier]], [[STFT et spectrogramme]], [[Ondelettes]]) portent encore `concept/signal` : elles descendront ici au lot 4.

<!-- AUTO:START -->
### Briques
- [[librosa]] — Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.
- [[PyWavelets]] — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- [[scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

### Comparatifs
- [[Comparatif - Traitement du signal]]
<!-- AUTO:END -->
