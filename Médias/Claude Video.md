---
role: brique
nom: Claude Video
alias: [watch, claude-video]
pitch: "Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse."
categorie: media/ingestion
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Python
alternatives: []
complements: []
tags: [multimodal, speech, context-engineering]
url_docs: https://github.com/bradautomates/claude-video
url_repo: https://github.com/bradautomates/claude-video
---

# Claude Video

<!-- AUTO:BANDEAU:START -->
> Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Extension Python | open-source | dans le moteur hôte, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Skill `/watch` développé par `bradautomates` — indépendant d'Anthropic malgré le nom. Il donne
à un assistant un type d'entrée qu'il n'a pas nativement : une vidéo. Le pipeline tient en un
passage — `yt-dlp` télécharge la source ou lit un fichier local, `ffmpeg` en extrait des frames
JPEG horodatées, et la transcription vient des sous-titres natifs ou, à défaut, de Whisper
(Groq `whisper-large-v3` ou OpenAI `whisper-1`). Le script imprime les chemins des frames avec
leur `t=MM:SS` et le transcript aligné ; l'assistant lit les images en parallèle et combine ce
qu'il « voit » et ce qu'il « entend ». Il ne produit **aucun résumé** : il produit les
artefacts bruts, à partir desquels l'agent écrit ensuite ce qu'on lui demande.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Poser une question sur une vidéo en ligne (YouTube, Vimeo, TikTok, X, Twitch, Loom) ou un fichier local | Scan complet d'une vidéo **longue** : la couverture de frames chute avec la durée (au-delà de 10 min, frames espacées et avertissement) — cibler par `--start` / `--end` |
| Résumer, extraire une timeline horodatée, ou zoomer sur un extrait précis par échantillonnage plus dense | Source sans sous-titres et sans clé Whisper : le résultat est *frames-only*, sans transcript |
| Alimenter un vault : `--out-dir` garde frames et transcript, l'agent écrit le rapport ensuite | Simple lecture d'un transcript déjà disponible : `--detail transcript` suffit, le pipeline complet est inutile |
| | Le coût en tokens est dominé par les frames — de l'ordre de 50 à 80 k tokens pour 80 frames à 512 px ; monter `--resolution 1024` quadruple la note |
| | Contenu sensible : la vidéo n'est jamais téléversée, mais l'**audio extrait** part chez Groq ou OpenAI dès que le repli Whisper se déclenche |
| | Le dossier de travail (vidéo, frames, audio, transcript) n'est pas nettoyé : le supprimer, ou fixer `--out-dir` pour le persister volontairement |
| | Whisper découpe l'audio au-delà de 25 Mo ; si des morceaux échouent, le transcript est partiel — signalé sur stderr seulement |

## Mise en œuvre

- Installation — plugin `bradautomates/claude-video`, ou dépôt manuel de `skills/watch/` dans `~/.claude/skills/watch/`
- Point d'entrée — la commande `/watch` d'un agent ; fonctionne sur Claude Code, claude.ai (fichier `watch.skill`), Codex
- Prérequis — `ffmpeg` et `ffprobe` pour les frames et l'audio, `yt-dlp` pour le téléchargement et les sous-titres. Sous **Windows** : installer par `scoop install ffmpeg` ou `winget install Gyan.FFmpeg`, et appeler `python`, jamais `python3` (le `python3` de Windows est le stub du Microsoft Store)
- Exécution — sur le poste, dans le processus de l'agent. Configuration dans `~/.config/watch/.env` : `GROQ_API_KEY` / `OPENAI_API_KEY` (Whisper, optionnels), `WATCH_DETAIL`, `SETUP_COMPLETE` ; preflight idempotent par `python scripts/setup.py --check|--json`. Quatre modes de détail — `transcript` (0 frame), `efficient` (keyframes, plafond 50), `balanced` (scene-aware, plafond 100, défaut), `token-burner` (sans plafond) — avec un plafond universel de 2 fps et des frames bornées à 1998 px de haut. L'avertissement « readable by other users » sur le `.env` sous Windows est un artefact du contrôle de permissions POSIX, sans effet sur un profil mono-utilisateur
- Coût — gratuit, MIT ; le coût réel est en tokens, et en appels Whisper si le repli se déclenche

## Écosystème

### Alternatives

<!-- Aucune : pas d'équivalent fiché dans le brain. Des forks « second brain » (par exemple `taoufik123-collab/claude-watch`) ajoutent rapport structuré et intégration Obsidian ; ce skill ne fournit que la brique bas niveau — frames, transcript, chemins — à exploiter ensuite librement. -->

## Ressources

- Dépôt — https://github.com/bradautomates/claude-video
- Documentation — le `README.md` du dépôt ; il n'existe pas de site séparé

## Voir aussi

- [[Médias]] — le hub du domaine
- [[Graphify]] — un autre skill d'agent, but différent : indexation de dépôt en graphe de connaissances
- [[Superwhisper]] — le sens inverse : transcrire la voix de l'utilisateur, pas donner une vidéo à un agent
