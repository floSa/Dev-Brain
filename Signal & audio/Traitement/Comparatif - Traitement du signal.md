---
role: comparatif
nom: Comparatif - Traitement du signal
categorie: signal/traitement
tags: [signal-processing, wavelet, spectrogram, fourier]
---

# Comparatif - Traitement du signal

> On tranche sur : la représentation que l'on cherche — fréquentielle, temps-échelle, ou des features audio prêtes à l'emploi — et non entre trois outils qui se remplaceraient.

![[Comparatif - Traitement du signal.base]]

## Ce qui départage

- [[scipy.signal]] — la boîte **DSP** de référence, sans dépendance lourde : conception et application de filtres FIR/IIR (Butterworth, Chebyshev, elliptique, `filtfilt` à phase nulle), analyse spectrale (`welch`, `stft`, `spectrogram`), convolution, détection de pics, ré-échantillonnage. Trois choses à savoir : la coupure se **normalise par Nyquist** ($f_s/2$), le format **SOS** (`sosfilt`) est plus stable que `(b, a)` en ordre élevé, et ses fonctions d'ondelettes sont **dépréciées ou retirées**.
- [[PyWavelets]] — exactement ce que le précédent ne fait plus : l'analyse **temps-échelle** d'un signal non stationnaire — DWT/IDWT, décomposition multiniveau, CWT, paquets d'ondelettes — et le **seuillage**, qui débruite en préservant les ruptures là où un passe-bas les lisse. Le choix de l'ondelette mère et du niveau conditionne tout, le mode de padding change les coefficients aux bords, et la CWT est redondante et coûteuse — pour compresser ou débruiter, c'est la DWT.
- [[librosa]] — l'étage **audio** de haut niveau : chargement de fichiers, STFT, mel-spectrogramme, MFCC, chromagramme, tempo et beat, HPSS, time-stretch — les features standard avant un modèle audio. Lent sur gros volumes, donc précalculer et mettre en cache ; `sr=22050` par défaut, ce qui **rééchantillonne au chargement** si on ne fixe pas `sr=None` ; et l'analyse est hors ligne, jamais temps réel.
