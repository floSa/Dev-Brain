---
galaxie: wiki
type: concept
nom: Traitement du signal
alias: [TdS, signal processing, DSP, traitement numérique du signal]
categorie: concept/signal
domaines: [data-sci, ml-eng]
tags: [signal-processing]
---

# Traitement du signal

## Aperçu

- Représenter, analyser et transformer des **signaux** — des suites de mesures indexées par le temps (ou l'espace) : audio, vibrations, capteurs, signaux physiologiques.
- En data/ML : c'est l'étage de **prétraitement et d'extraction de features** posé avant un modèle. Nettoyer (débruiter, détrender), puis décrire le contenu fréquentiel du signal.
- Page chapeau : oriente vers les quatre briques ci-dessous.

## Concepts clés

### Signal & échantillonnage
- Un signal continu est **échantillonné** à la fréquence $f_s$ : on n'en garde que des points $x[n]$. Tout le numérique part de là.
- **Nyquist-Shannon** : pour représenter sans perte une composante de fréquence $f$, il faut $f_s > 2f$. En dessous → **repliement** (aliasing) : des hautes fréquences se déguisent en basses, irréversiblement.

### Trois domaines d'analyse
- **Temps** : la forme d'onde brute.
- **Fréquence** : quelles fréquences composent le signal — [[Transformée de Fourier]].
- **Temps-fréquence** : comment le contenu fréquentiel évolue — [[STFT et spectrogramme]], [[Ondelettes]].

### Opérations fondamentales
- **Convolution / corrélation** : comparer ou transformer un signal par un noyau.
- **Filtrage** : garder/atténuer des bandes de fréquences — [[Filtrage numérique]].

### Les quatre briques
- [[Transformée de Fourier]] — le contenu fréquentiel global (DFT/FFT).
- [[Ondelettes]] — analyse temps-échelle multirésolution (DWT/CWT).
- [[STFT et spectrogramme]] — le spectre en fonction du temps (dont mel / MFCC).
- [[Filtrage numérique]] — concevoir des filtres (Butterworth, fenêtrage).

## Les maths, simplement

- Échantillonnage : $x[n] = x(n/f_s)$ ; la fréquence de Nyquist est $f_s/2$ — borne supérieure de ce qui est représentable.
- Résolution fréquentielle d'une analyse sur $N$ points : $\Delta f = f_s/N$ — plus de points (ou plus de durée) → spectre plus fin.

## En pratique

- Pile Python : `numpy.fft` (FFT), [[Dev/Services/scipy.signal|scipy.signal]] (filtres, spectres, fenêtres), [[Dev/Services/PyWavelets|PyWavelets]] (ondelettes), [[Dev/Services/librosa|librosa]] (audio, mel / MFCC).
- Pipeline type : **nettoyer** (détrend, filtrage passe-bas) → **analyser** (spectre, spectrogramme) → **extraire des features** → modèle ML.
- Piège récurrent : oublier l'anti-aliasing avant un sous-échantillonnage, ou la fuite spectrale faute de fenêtrage avant FFT.

## Approches voisines & alternatives

- [[Transformée de Fourier]], [[Ondelettes]], [[STFT et spectrogramme]], [[Filtrage numérique]] — les quatre briques détaillées.
- [[Autocorrelation]] — descripteur temporel, relié au spectre par Wiener-Khinchin.
- [[Stationarity]] — la stationnarité (ou son absence) décide entre Fourier global et analyse temps-fréquence.
- [[Time series feature engineering]] — les features spectrales alimentent les modèles de séries temporelles.
- [[Time series anomaly detection]] — filtrage et ondelettes servent à isoler transitoires et ruptures.

## Pour aller plus loin

- Oppenheim & Schafer — *Discrete-Time Signal Processing*.
- Steven W. Smith — *The Scientist and Engineer's Guide to Digital Signal Processing* (dspguide.com, libre).
- [[Dev/Patterns/Comparatif - Traitement du signal|Comparatif — Traitement du signal]] — les libs Python du domaine en un tableau.
