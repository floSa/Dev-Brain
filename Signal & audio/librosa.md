---
role: brique
nom: librosa
alias: [librosa audio, audio features, MIR]
pitch: "Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio."
categorie: signal/audio
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[scipy.signal]]"]
complements: []
tags: [signal-processing, spectrogram, feature-engineering]
url_docs: https://librosa.org/doc/
url_repo: https://github.com/librosa/librosa
---

# librosa

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'analyse audio et musicale en Python — chargement, STFT, mel-spectrogramme et MFCC, estimation de tempo et de hauteur, séparation harmonique/percussive ; la référence pour extraire des features audio.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'analyse audio et musicale en Python. Elle charge des fichiers son et
fournit sous une API uniforme les représentations standard du domaine — STFT,
mel-spectrogramme, MFCC, chromagramme — plus l'estimation de tempo et de beat, la
détection d'onsets, l'estimation de hauteur, la séparation harmonique/percussive (HPSS),
le time-stretch et le pitch-shift. C'est l'étage d'extraction de features en amont d'un
modèle audio. Deux comportements par défaut piègent tout pipeline qui les ignore :
`sr=22050` est la fréquence d'échantillonnage par défaut, donc un chargement
**rééchantillonne** le signal tant qu'on ne fixe pas `sr=None` ; et les amplitudes
brutes ne sont exploitables qu'une fois passées en décibels par `power_to_db` ou
`amplitude_to_db`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charger et rééchantillonner de l'audio, calculer mel-spectrogrammes et MFCC | Reconnaissance vocale ou synthèse de parole de bout en bout → [[HuggingFace]] et ses modèles dédiés (Whisper, wav2vec2) |
| Produire des features pour de la classification audio, du MIR ou de la parole | Traitement temps réel ou à faible latence : l'analyse est hors ligne, en NumPy et sur CPU |
| Beat tracking, estimation de tempo, détection d'onsets, séparation HPSS | Gros volumes à l'entraînement : lent en Python et NumPy — précalculer et mettre en cache les spectrogrammes plutôt que les recalculer par époque |
| Prototyper un pipeline audio vers un modèle ML | |

## Mise en œuvre

- Installation — `uv add librosa`
- Point d'entrée — import Python, `import librosa`
- Prérequis — NumPy et SciPy ; `soundfile` ou `audioread` pour l'I/O, et `ffmpeg` pour certains formats compressés
- Exécution — dans le process appelant, CPU uniquement, en mémoire ; aucune accélération GPU
- Coût — gratuit, licence ISC, aucune limite d'usage

## Écosystème

### Alternatives

- [[scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

## Ressources

- Documentation — https://librosa.org/doc/
- Dépôt — https://github.com/librosa/librosa

## Voir aussi

- [[Signal & audio]] — le hub du domaine
- [[STFT et spectrogramme]] — la notion : mel-spectrogramme et MFCC, son terrain principal
- [[Traitement du signal]] — la notion voisine, côté DSP
- [[Comparatif - Traitement du signal]] — ce qui départage les outils du dossier
