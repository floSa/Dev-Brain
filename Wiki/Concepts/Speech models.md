---
galaxie: wiki
type: concept
nom: Speech models
alias: [ASR, TTS, speech-to-text, text-to-speech, reconnaissance vocale, synthèse vocale, Whisper, modèles de parole, speech-to-speech]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [speech, deep-learning, multimodal]
---

# Speech models

## Aperçu

- Modèles qui relient **parole et texte** dans les deux sens : **reconnaissance** (ASR, speech → text) et **synthèse** (TTS, text → speech), plus le **speech-to-speech** direct.
- Idée clé : transformer un **signal audio continu** en représentation **discrète** exploitable par des architectures de type [[Transformer architectures|Transformer]], dans un sens comme dans l'autre.

## Concepts clés

### ASR — reconnaissance
- **Whisper** (encodeur-décodeur Transformer, ~1,5 Md de paramètres) : entraînement **supervisé massif et multilingue** → robustesse hors-domaine *sans* pré-entraînement auto-supervisé. Alternatives : wav2vec 2.0 / HuBERT (auto-supervisé), Canary, Granite Speech.

### TTS — synthèse
- Tendance : traiter l'audio comme des **tokens** via un codec neuronal, puis les générer avec un **modèle de langage** (VALL-E) ou par diffusion / flow-matching (MaskGCT). Débloque le ***zero-shot voice cloning*** à partir de quelques secondes d'exemple.

### Codec neuronal
- EnCodec, SoundStream, DAC : **compressent la forme d'onde en tokens discrets**. C'est la charnière qui permet à la parole d'emprunter l'outillage des LLM (pré-entraînement, prompting, clonage de voix).

### Speech-to-speech & temps réel
- Modèles « omni » (audio ↔ audio de bout en bout) pour la **conversation à faible latence**, sans cascade ASR → LLM → TTS.

## Les maths, simplement

- ASR : $\arg\max_{y} P(y \mid \text{audio})$ — décodage du texte le plus probable, souvent par [[Cross-entropy|entropie croisée]] séquence-à-séquence (parfois CTC).
- TTS par codec : audio $\to$ tokens via un codec, puis $P(\text{token}_t \mid \text{token}_{<t}, \text{texte})$ — un modèle **autorégressif sur tokens audio**, exactement comme un LLM sur du texte.

## En pratique

- **ASR** : surveiller le **WER** (word error rate), la robustesse au bruit / à l'accent, la latence (*streaming* vs *batch*). Whisper = défaut open-weight solide.
- **TTS** : *naturalness* (MOS), similarité de voix, latence. Attention au **consentement** et au risque de clonage vocal frauduleux (deepfake audio).
- **Multimodal** : la tokenisation audio rapproche la parole des [[Vision Language Models|modèles multimodaux]] — mêmes briques, modalité différente.

## Approches voisines & alternatives

- [[Transformer architectures]] — colonne vertébrale de l'ASR (Whisper) comme de la TTS par tokens.
- [[Tokenization]] — la tokenisation **audio** (codec neuronal) est l'analogue parole de la tokenisation texte.
- [[Vision Language Models]] — autre extension multimodale du même socle ; certains modèles « omni » couvrent texte + image + audio.

## Pour aller plus loin

- Radford et al. (2022) — *Robust Speech Recognition via Large-Scale Weak Supervision* (Whisper).
- Wang et al. (2023) — *VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers*.
- Défossez et al. (2022) — *High Fidelity Neural Audio Compression* (EnCodec).
