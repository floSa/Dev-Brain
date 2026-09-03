---
role: hub
nom: Traitement
alias: [traitement numérique du signal, DSP, transformées]
pitch: Décomposer un signal échantillonné en fréquences et le filtrer — les transformées, ce qu'elles coûtent, et les deux boîtes à outils qui les implémentent.
domaines: [data-sci, ml-eng]
tags: [signal-processing, fourier, spectrogram, wavelet, digital-filter]
---

# Traitement

> Décomposer un signal échantillonné en fréquences et le filtrer — les transformées, ce qu'elles coûtent, et les deux boîtes à outils qui les implémentent.

## Ce qu'il faut comprendre

- **Un signal se lit dans deux domaines, et le choix décide de tout le reste.** Le temps dit *quand*, la fréquence dit *de quoi c'est fait*. [[Transformée de Fourier]] passe de l'un à l'autre — et perd complètement le *quand* : elle dit quelles fréquences sont présentes, jamais à quel instant.
- **Les deux pages suivantes ne sont que deux façons de récupérer ce *quand*.** [[STFT et spectrogramme]] découpe le signal en fenêtres et transforme chacune : la résolution temps / fréquence devient un réglage — fenêtre courte, on situe bien mais on distingue mal les fréquences ; fenêtre longue, l'inverse. [[Ondelettes]] fait varier ce compromis **avec l'échelle** : fin en temps sur les hautes fréquences, fin en fréquence sur les basses. C'est le bon outil pour un transitoire, une rupture, un signal non stationnaire.
- **[[Filtrage numérique]] est l'autre geste du dossier**, et il est orthogonal aux transformées : on ne décrit pas le signal, on lui retire quelque chose. Le choix FIR / IIR est le seul arbitrage structurant — le FIR est stable et à phase linéaire mais coûte des coefficients, l'IIR atteint la même sélectivité pour bien moins de calcul au prix de la phase et d'un risque d'instabilité.
- **[[Traitement du signal]] est la page chapeau** : échantillonnage, Shannon-Nyquist, repliement de spectre. À lire d'abord si le vocabulaire n'est pas acquis — un signal mal échantillonné ne se rattrape par aucun traitement en aval.
- **Deux niveaux de brique, et le second n'est pas un remplaçant du premier.** [[scipy.signal]] est la boîte générique — filtres, spectres, convolution, ré-échantillonnage — et ne sait rien de l'audio. [[PyWavelets]] est le seul à porter les ondelettes. [[librosa]], qui reste au niveau du domaine, s'appuie de toute façon sur SciPy et n'ajoute que ce que l'audio attend.

## Choisir

- Savoir quelles fréquences composent un signal stationnaire → [[Transformée de Fourier]].
- Savoir *quand* chaque fréquence apparaît → [[STFT et spectrogramme]].
- Un signal non stationnaire, un transitoire, une rupture → [[Ondelettes]], et [[PyWavelets]] pour le calculer.
- Retirer du bruit, borner une bande, ré-échantillonner → [[Filtrage numérique]], et [[scipy.signal]] pour le calculer.
- Le vocabulaire de base, l'échantillonnage, le repliement → [[Traitement du signal]].
- Des descripteurs audio — MFCC, chroma, tempo → [[librosa]], au niveau du domaine.
- Modéliser une série économique ou métier plutôt qu'un signal physique → [[Séries temporelles]], au domaine [[Machine Learning]].

<!-- AUTO:START -->
### Notions
- [[Filtrage numérique]] — domaines : data-sci, ml-eng
- [[Ondelettes]] — domaines : data-sci, ml-eng
- [[STFT et spectrogramme]] — domaines : data-sci, ml-eng
- [[Traitement du signal]] — domaines : data-sci, ml-eng
- [[Transformée de Fourier]] — domaines : data-sci, ml-eng

### Briques
- [[PyWavelets]] — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- [[scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.
<!-- AUTO:END -->
