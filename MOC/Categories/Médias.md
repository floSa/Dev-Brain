---
type: moc
nom: Médias
galaxie: dev
indexe: media/*
---

# Médias

<!-- AUTO:START -->
Briques techniques de la catégorie `media/*`.

- [[Claude Video]] — Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.
- [[OpenCut]] — Éditeur de montage vidéo open-source (MIT), alternative déclarée à CapCut : cœur Rust, frontend TypeScript/Next.js, médias traités en local. Réécriture en cours — serveur MCP, mode headless et plugins sont annoncés, pas livrés.
- [[SmartTube]] — Client YouTube alternatif pour Android TV et box (MIT, Java) : lecture sans publicité, SponsorBlock, sans Google Services. Distribué hors magasin par APK à installer soi-même.
- [[Superwhisper]] — Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie.
<!-- AUTO:END -->

## Notes

