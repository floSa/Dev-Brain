---
galaxie: wiki
type: concept
nom: Classification audio par spectrogramme
alias: [classification audio, audio classification, sound classification, reconnaissance de sons, audio CNN, mel-spectrogramme CNN, acoustic scene classification, SpecAugment]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [audio-classification, spectrogram, cnn]
---

# Classification audio par spectrogramme

## Aperçu

- Classer un signal sonore (genre musical, scène acoustique, événement, espèce) en le transformant d'abord en **image temps-fréquence**, puis en le traitant comme un problème de vision.
- Recette dominante : **forme d'onde → mel-spectrogramme → CNN**. On réutilise tout l'outillage image (backbones, transfert, augmentation).

## Concepts clés

### Du son à l'image
- Le signal 1D est découpé en fenêtres et passé en [[STFT et spectrogramme|STFT]] → **mel-spectrogramme** (log-mel le plus souvent). On obtient une matrice temps × fréquence : une « image » à un canal. [[Dev/Services/librosa|librosa]] (`melspectrogram`) est l'outil de référence.

### Pourquoi un CNN
- Sur un spectrogramme, les motifs (harmoniques, transitoires, formants) sont **locaux et invariants par translation** en temps — exactement les biais inductifs du [[CNN]]. Un backbone vision ([[Architectures CNN]]) s'applique presque tel quel, l'entrée passant de 3 canaux RGB à 1 canal log-mel.

### Transfert depuis la vision
- On part rarement de zéro : [[Transfer learning vision|transfert]] d'un backbone pré-entraîné (ImageNet, ou AudioSet côté audio) puis fine-tuning. Très efficace quand les données étiquetées sont rares.

### Augmentation spécifique
- En plus de l'[[Augmentation d'images|augmentation]] classique, **SpecAugment** masque des bandes de temps et de fréquence directement sur le spectrogramme ; côté onde : time-stretch, pitch-shift, ajout de bruit. Régularise fortement.

## Les maths, simplement

- Entrée : $S \in \mathbb{R}^{F \times T}$, log-mel-spectrogramme ($F$ bandes mel, $T$ trames) — cf. [[STFT et spectrogramme]] pour $S = \log(\mathrm{Mel}\,|STFT|^2)$.
- Le CNN apprend $f_\theta(S) \to$ logits ; entraînement par [[Gradient descent|descente de gradient]] ([[Adam optimizer|Adam]]) sur l'[[Cross-entropy|entropie croisée]]. Pour du **multi-label** (plusieurs sons simultanés), sigmoïde + binary cross-entropy par classe.

## En pratique

- **Pipeline** : ré-échantillonner à un taux fixe → log-mel (`n_fft`, `hop_length`, `n_mels` cohérents sur tout le jeu) → normaliser → CNN. Fixer une **durée** (crop / pad) pour des entrées de taille constante.
- **Pièges** : classes déséquilibrées (événements rares) ; **fuite de données** si des segments du même enregistrement sont à la fois en train et en test (splitter par enregistrement, pas par segment) ; cohérence stricte des paramètres mel entre entraînement et inférence.
- **Au-delà du CNN** : les **transformers audio** (AST) prennent aussi le spectrogramme en patchs ; les modèles de parole ([[Speech models]]) traitent l'ASR / TTS, tâche distincte de la classification de sons.

## Approches voisines & alternatives

- [[STFT et spectrogramme]] — la représentation d'entrée ; tout le pré-traitement audio vit là.
- [[CNN]] / [[Architectures CNN]] — l'ossature qui consomme le spectrogramme.
- [[Classification d'images]] — la même tâche, sur des images naturelles ; on en reprend les méthodes.
- [[Speech models]] — autre branche de l'audio (reconnaissance / synthèse vocale), à ne pas confondre.
- [[Traitement du signal]] — page chapeau côté signal.

## Pour aller plus loin

- Hershey et al. (2017) — *CNN Architectures for Large-Scale Audio Classification* (AudioSet).
- Park et al. (2019) — *SpecAugment*.
- Gong et al. (2021) — *AST: Audio Spectrogram Transformer*.
