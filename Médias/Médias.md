---
role: hub
nom: Médias
alias: [medias, media, video, audio]
pitch: Produire, consommer et donner à lire des médias — de la dictée vocale au montage vidéo, jusqu'à la vidéo qu'un agent regarde.
domaines: [ai-eng]
tags: [video-editing, media-player, speech, multimodal]
---

# Médias

> Produire, consommer et donner à lire des médias — de la dictée vocale au montage vidéo, jusqu'à la vidéo qu'un agent regarde.

## Ce qu'il faut comprendre

- Le domaine est un petit ensemble d'**applications de bout en bout**, pas une pile technique. Aucune de ces briques ne s'importe dans un pipeline : on les installe et on les utilise.
- Deux usages s'y croisent, et c'est le second qui intéresse un profil data. **Consommer ou produire** un média ([[OpenCut]], [[SmartTube]]) est de l'outillage personnel. **Faire entrer un média dans une chaîne de traitement** ([[Superwhisper]] pour la parole, [[Claude Video]] pour la vidéo) est de l'ingestion multimodale : le média devient du texte, donc de la donnée exploitable.
- La transcription **locale** est le point technique du domaine. Whisper tournant sur la machine, la parole devient une entrée utilisable sans qu'aucun audio ne sorte — ce qui la rend acceptable là où l'API ne l'est pas.

## Choisir

- Dicter du texte plutôt que le taper, sans envoyer l'audio ailleurs → [[Superwhisper]].
- Donner à un agent la capacité de regarder une vidéo et d'en parler → [[Claude Video]].
- Monter une vidéo sans dépendre d'un éditeur propriétaire → [[OpenCut]].
- Regarder YouTube sur une box Android TV, sans publicité ni services Google → [[SmartTube]].

<!-- AUTO:START -->
### Briques
- [[Claude Video]] — Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.
- [[OpenCut]] — Éditeur de montage vidéo open-source (MIT), alternative déclarée à CapCut : cœur Rust, frontend TypeScript/Next.js, médias traités en local. Réécriture en cours — serveur MCP, mode headless et plugins sont annoncés, pas livrés.
- [[SmartTube]] — Client YouTube alternatif pour Android TV et box (MIT, Java) : lecture sans publicité, SponsorBlock, sans Google Services. Distribué hors magasin par APK à installer soi-même.
- [[Superwhisper]] — Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie.
<!-- AUTO:END -->
