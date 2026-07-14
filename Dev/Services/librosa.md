---
galaxie: dev
type: service
nom: librosa
alias: [librosa audio, audio features, MIR]
pitch: "Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/scipy.signal|scipy.signal]]"]
remplace_par: []
status: actif
tags: [signal-processing, spectrogram, feature-engineering]
url_docs: https://librosa.org/doc/
url_repo: https://github.com/librosa/librosa
---

# librosa

## Pourquoi

Bibliothèque de référence pour l'**analyse audio et musicale** en Python. Charge des fichiers son et fournit, sous une API simple, les représentations clés : **STFT**, **mel-spectrogramme**, **MFCC**, chromagramme, plus l'estimation de **tempo / beat**, de **hauteur** (pitch), la séparation **harmonique / percussive** (HPSS) et le time-stretch / pitch-shift. C'est l'étage d'**extraction de features** standard avant un modèle audio (CNN, transformers).

## Quand l'utiliser

- Charger et rééchantillonner de l'audio, calculer mel-spectrogrammes / MFCC.
- Produire des features pour de la **classification audio**, du MIR (music information retrieval), de la parole.
- Beat tracking, estimation de tempo, onset detection, séparation HPSS.
- Prototyper rapidement un pipeline audio → ML.

## Quand NE PAS l'utiliser

- **DSP générique** non audio (filtres, capteurs) → [[Dev/Services/scipy.signal|scipy.signal]].
- Analyse par **ondelettes** → [[Dev/Services/PyWavelets|PyWavelets]].
- **Reconnaissance vocale** (ASR) ou TTS de bout en bout → modèles dédiés ([[Dev/Services/HuggingFace|HuggingFace]] : Whisper, wav2vec2).
- Traitement audio **temps réel / faible latence** → librosa vise l'analyse hors ligne (NumPy, CPU).

## Déploiement & coût

- Bibliothèque (`uv add librosa`). Licence ISC, gratuit.
- **Single-node, en mémoire** ; Python pur au-dessus de NumPy / SciPy (+ soundfile / audioread pour l'I/O).
- Aucune infra ; CPU uniquement (pas d'accélération GPU).

## Pièges

- **Lent sur gros volumes** (Python / NumPy) : pour l'entraînement à l'échelle, précalculer et mettre en cache les spectrogrammes.
- `sr=22050` par défaut : librosa **rééchantillonne** au chargement — fixer `sr=None` (ou explicite) pour ne pas dégrader le signal.
- Amplitudes : penser `power_to_db` / `amplitude_to_db` pour des mel-spectrogrammes exploitables.
- I/O : certains formats compressés exigent `ffmpeg` (via audioread).

## Alternatives

- [[Dev/Services/scipy.signal|scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

## Liens

- [[STFT et spectrogramme]] — mel-spectrogramme et MFCC, son terrain principal.
- [[Traitement du signal]] — page chapeau.
- [[Dev/Services/scipy.signal|scipy.signal]] — DSP bas niveau sous-jacent.
- [[Dev/Patterns/Comparatif - Traitement du signal|Comparatif — Traitement du signal]]
- Doc : https://librosa.org/doc/
