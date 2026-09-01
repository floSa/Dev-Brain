---
galaxie: dev
type: outil
nom: Superwhisper
alias: [superwhisper]
pitch: "Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie."
categorie: tooling/media
famille: application
domaines: [ai-eng]
licence_type: proprietary
os: "macOS, Windows, iOS"
langage: 
status: actif
alternatives: []
tags: [speech, multimodal, local-llm]
url_docs: https://superwhisper.com/docs/models/
url_repo: 
---

# Superwhisper

## Pourquoi

Dictée vocale système : on parle, le texte s'insère dans l'application active. La transcription peut tourner **entièrement en local**, ce qui en fait un outil utilisable sur du contenu qu'on ne veut pas envoyer à un tiers.

Deux moteurs locaux, aucun n'est maison : **whisper.cpp** pour les modèles de la famille Whisper, **WhisperKit** (SDK Argmax) pour les modèles NVIDIA Parakeet. Le moteur propriétaire de l'éditeur, la famille S1, est côté cloud — avec Ultra Cloud, Deepgram Nova 3 / Nova 2 / Nova Medical, et un partenariat Cohere Transcribe annoncé.

Note de rangement : la taxonomie décrit `tooling/media` comme l'ingestion de médias pour donner à un assistant un input multimodal. Superwhisper va dans l'autre sens — c'est une **entrée utilisateur**, pas une ingestion pour agent. C'est le seul emplacement honnête de la taxonomie fermée.

## Quand l'utiliser

- Dicter du texte long (documentation, messages, notes) plus vite qu'au clavier, dans n'importe quelle application.
- Transcrire du contenu confidentiel sans sortie réseau, en s'en tenant aux modèles locaux.
- Enregistrer et transcrire une réunion, y compris au palier gratuit.

## Quand NE PAS l'utiliser

- **Poste Linux ou travail dans WSL** : il n'existe pas de version Linux. Et sous Windows, l'éditeur documente lui-même cinq manques — pas de FileSync, dossier applicatif non personnalisable (forcé sur `%LOCALAPPDATA%\com.superwhisper.app`), pas de « hold shift to auto-send », pas de simulation de frappes, intégrations agentiques (Claude Code, Codex, OpenCode, Pi) encore « en développement ».
- Sur du matériel non Apple Silicon si l'on vise les gros modèles : l'éditeur oriente les Mac Intel anciens et les PC Windows vers un modèle de taille moyenne, et pousse les Mac Intel vers le cloud.
- Exigence de logiciel libre : c'est propriétaire et closed-source.
- Donner à un agent la capacité de regarder une vidéo — usage différent → [[Dev/Outils/Claude Video|Claude Video]].

## Installation & plateformes

- Application macOS, Windows 10/11 et iOS ; **une seule licence couvre les trois**.
- Freemium : 3 000 mots d'essai des fonctions Pro, puis palier gratuit à vie (dictée dans toute application, enregistrement de réunion, usage illimité des petits modèles locaux, prompts personnalisés).
- Pro : **8,49 $/mois, 84,99 $/an, ou 249,99 $ à vie**. Remboursement 30 jours. Offre Enterprise sur devis.
- Fonctionnement hors ligne revendiqué, 100+ langues et dialectes, traduction vers l'anglais.

### Modèles locaux disponibles

| Modèle | Moteur | Langues | Disque | Vitesse | Précision | Palier |
|---|---|---|---|---|---|---|
| Ultra | whisper.cpp | toutes | 3 Go | 6 | 10 | Pro |
| Ultra V3 Turbo | whisper.cpp | toutes | 1,6 Go | 8 | 8 | Pro |
| Ultra V3 Turbo (Chinese) | whisper.cpp | chinois | 1,6 Go | 8 | 8 | Pro |
| Pro | whisper.cpp | toutes | 1,5 Go | 7 | 8 | Pro |
| Pro (English) | whisper.cpp | anglais | 1,5 Go | 7 | 8 | Pro |
| Standard | whisper.cpp | toutes | 500 Mo | 8 | 5 | Gratuit |
| Standard (English) | whisper.cpp | anglais | 500 Mo | 8 | 5 | Gratuit |
| Nano | whisper.cpp | toutes | 150 Mo | 9 | 3 | Gratuit |
| Nano (English) | whisper.cpp | anglais | 150 Mo | 9 | 3 | Gratuit |
| Fast | whisper.cpp | toutes | 75 Mo | 10 | 1 | Gratuit |
| Fast (English) | whisper.cpp | anglais | 75 Mo | 10 | 1 | Gratuit |
| Parakeet | WhisperKit | anglais | 476 Mo | 10 | 8 | Pro |
| Parakeet Multilanguage | WhisperKit | multi | 494 Mo | 10 | 8 | Pro |

Les colonnes vitesse et précision sont des notes de 1 à 10 **auto-déclarées par l'éditeur** : ni WER, ni RTF, ni matériel de référence.

## Pièges

- **Aucune exigence de RAM n'est publiée**, ni par modèle ni globalement, sur aucune page de l'éditeur. Les chiffres du type « 1 Go pour tiny, 10 Go pour large » qui circulent proviennent de blogs d'applications concurrentes : ils ne sont pas repris ici. Pour dimensionner, se référer aux tailles des poids GGML en amont, chez whisper.cpp.
- **Aucune correspondance officielle** entre les noms commerciaux et les checkpoints OpenAI (tiny, base, small, medium, large-v3). Les tailles la suggèrent, l'éditeur ne la confirme pas. Seul point confirmé : les poids complets de Whisper Large V3 tournent en local via whisper.cpp, plus lents et plus précis que la distillation turbo.
- **Précision en français et sur les acronymes : aucune donnée chiffrée, nulle part.** Ce qui est sourcé : l'anglais est la langue la plus forte des modèles hors ligne, et Cohere Transcribe couvre 14 langues dont le français. Le traitement des acronymes relève du vocabulaire personnalisé et des prompts de l'application, non documentés ni mesurés.
- Disponibilité des modèles Parakeet **sous Windows** non vérifiée : WhisperKit est à l'origine une brique Apple/CoreML, la restriction à macOS et iOS est probable mais non confirmée.
- Ne pas confondre **whisper.cpp** (le moteur ASR utilisé ici) avec llama.cpp : projets distincts, même base ggml.

## Alternatives

- Aucune page du brain n'est une vraie alternative : les concurrents (MacWhisper, Wispr Flow, VoiceInk…) ne sont pas fichés.
- Voisin fonctionnel, usage différent : [[Dev/Outils/Claude Video|Claude Video]] — Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.

## Liens

- [[Speech models]] — concept : modèles de parole et transcription automatique
- [[Quantization]] — concept : ce qui explique les paliers de 75 Mo à 3 Go
- [[Inference optimization]] — concept : accélération de l'inférence
- Docs modèles : https://superwhisper.com/docs/models/ · Site : https://superwhisper.com
