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

- Un signal se lit dans deux domaines, et le choix de l'un ou de l'autre décide de tout le reste. Le **temps** dit *quand* ; la **fréquence** dit *de quoi c'est fait*. La [[Transformée de Fourier]] passe de l'un à l'autre, la [[STFT et spectrogramme]] fait le compromis entre les deux, les [[Ondelettes]] l'ajustent selon l'échelle. Ces pages, et les deux boîtes à outils qui les implémentent, sont dans [[Traitement]] — le seul sous-dossier du domaine.
- Le domaine est le **socle de l'audio** mais ne s'y limite pas : capteurs industriels, vibrations, séries de mesures physiques relèvent des mêmes outils. En revanche la modélisation d'une série *économique* ou *métier* est du ressort des séries temporelles, pas du traitement du signal.
- Deux niveaux de brique cohabitent, et c'est ce que le découpage en dossiers montre : la **boîte à outils générique** ([[scipy.signal]], [[PyWavelets]]) est dans [[Traitement]] avec les notions qu'elle calcule, parce qu'elle ne sait rien de l'audio ; la **bibliothèque de domaine** ([[librosa]]) reste au niveau du domaine — elle ajoute les descripteurs que l'audio attend, MFCC, chroma, tempo, découpage en trames, et les valeurs par défaut qui vont avec. `signal/audio` n'a qu'elle : pas de dossier, et c'est le seuil qui le décide, pas un arbitrage.

## Choisir

- Filtrage, convolution, corrélation, ré-échantillonnage, transformées classiques → [[scipy.signal]], le socle, dans [[Traitement]].
- Analyse multi-échelle (débruitage, compression, transitoires) → [[PyWavelets]].
- Audio : extraction de descripteurs pour de la classification, du tempo, de la séparation → [[librosa]], qui s'appuie de toute façon sur SciPy.
- Toutes les notions du domaine → [[Traitement]].

<!-- AUTO:START -->
### Sous-domaines
- [[Traitement]]

### Briques
- [[librosa]] — Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.

### Comparatifs
- [[Comparatif - Traitement du signal]]
<!-- AUTO:END -->
