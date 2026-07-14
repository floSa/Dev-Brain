---
galaxie: dev
type: outil
nom: Claude Video
alias: [watch, claude-video]
pitch: "Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse."
categorie: tooling/media
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
status: actif
alternatives: []
tags: [multimodal, speech, context-engineering]
url_docs: https://github.com/bradautomates/claude-video
url_repo: https://github.com/bradautomates/claude-video
---

# Claude Video

## Pourquoi

Claude Video (MIT, Python) est un skill `/watch` développé par `bradautomates` — indépendant d'Anthropic malgré le nom. Il donne à un assistant un input qu'il n'a pas nativement : une vidéo. Pipeline en un passage : `yt-dlp` télécharge la source (ou lit un fichier local), `ffmpeg` extrait des frames JPEG horodatées, la transcription vient des sous-titres natifs (`yt-dlp`) ou, à défaut, de Whisper (Groq `whisper-large-v3` ou OpenAI `whisper-1`). Le script imprime les chemins des frames avec `t=MM:SS` et le transcript aligné ; l'assistant `Read` les images en parallèle et combine ce qu'il « voit » et ce qu'il « entend ». Utile comme moteur d'extraction pour un second brain : produire une fois les artefacts bruts (images + texte), puis laisser l'agent générer autant de résumés / rapports Markdown que voulu.

## Quand l'utiliser

- Poser une question sur une vidéo (YouTube, Vimeo, TikTok, X, Twitch, Loom…) ou un fichier local (`.mp4`, `.mov`, `.mkv`, `.webm`).
- Résumer, extraire une timeline horodatée, ou zoomer sur un extrait précis (`--start`/`--end`, échantillonnage plus dense).
- Alimenter un vault Obsidian : `--out-dir <dossier du vault>` pour garder frames + transcript, puis faire écrire un rapport à l'agent.

## Quand NE PAS l'utiliser

- Vidéos longues en scan complet : la couverture de frames chute avec la durée (>10 min → frames espacées, warning). Préférer un `--start/--end` ciblé.
- Fichier local ou source sans sous-titres, sans clé Whisper : résultat *frames-only* (pas de transcript).
- Simple lecture d'un transcript déjà dispo : inutile de faire tourner le pipeline complet (`--detail transcript` suffit).

## Bases & plateformes

- Distribué en **plugin** (`bradautomates/claude-video`, skill `watch`) ; installable aussi manuellement en déposant `skills/watch/` dans `~/.claude/skills/watch/` (SKILL.md + `scripts/`). Fonctionne sur Claude Code, claude.ai (fichier `watch.skill`), Codex, etc.
- Dépendances : **`ffmpeg`+`ffprobe`** (extraction frames/audio) et **`yt-dlp`** (téléchargement + captions). Sur **Windows** : installer via `scoop install ffmpeg` ou `winget install Gyan.FFmpeg` ; **appeler `python`, pas `python3`** (le `python3` de Windows est le stub Microsoft Store).
- Config dans `~/.config/watch/.env` : `GROQ_API_KEY` / `OPENAI_API_KEY` (Whisper, optionnels), `WATCH_DETAIL`, `SETUP_COMPLETE`. Preflight idempotent : `python scripts/setup.py --check|--json`.
- Modes de détail (`WATCH_DETAIL` ou `--detail`) : `transcript` (0 frame) · `efficient` (keyframes, cap 50) · `balanced` (scene-aware, cap 100, défaut) · `token-burner` (uncapped). Cap universel **2 fps**. Frames clampées à 1998px de haut (compat `Read`).
- Sans clé Whisper : marche sur toute vidéo qui a des sous-titres (cas YouTube classique) ; sans sous-titres → *frames-only*.

## Pièges

- Coût en tokens dominé par les frames (~50-80k tokens pour 80 frames à 512px) ; le transcript est cheap. Ne pas monter `--resolution 1024` sans raison (×4 tokens).
- Le skill n'*upload jamais la vidéo* : seul l'audio extrait part vers Groq/OpenAI, et uniquement en fallback Whisper. À savoir pour les contenus sensibles.
- Nettoyage manuel : le script laisse un dossier de travail (vidéo, frames, audio, transcript). Le supprimer (`rm -rf`) si pas de suivi, ou fixer `--out-dir` pour le persister volontairement.
- Whisper coupe l'audio >25 Mo en chunks ; si des chunks échouent, transcript partiel (noté sur stderr).
- Warning « readable by other users » sur le `.env` sous Windows : artefact du check de permissions POSIX, sans effet réel sur un profil mono-utilisateur (et sans objet tant qu'aucune clé n'est stockée).

## Alternatives

- Pas d'équivalent direct fiché dans le brain. Des forks « second brain » (ex. `taoufik123-collab/claude-watch`) ajoutent directement rapport structuré + intégration Obsidian ; Claude Video, lui, ne fournit que la brique bas niveau (frames + transcript + chemin), à exploiter ensuite librement.
- Voisin fonctionnel (autre skill d'agent, but différent) : [[Dev/Outils/Graphify|Graphify]] — indexation de dépôt en knowledge graph.

## Liens

- Repo & doc : https://github.com/bradautomates/claude-video
- Skill installé localement : `~/.claude/skills/watch/`
