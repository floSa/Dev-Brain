---
role: brique
nom: Superwhisper
alias: [superwhisper]
pitch: "Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie."
categorie: media/ingestion
famille: application
domaines: [ai-eng]
licence_type: proprietary
os: "macOS, Windows, iOS"
langage: 
alternatives: []
complements: []
tags: [speech, multimodal, local-llm]
url_docs: https://superwhisper.com/docs/models/
url_repo: 
---

# Superwhisper

<!-- AUTO:BANDEAU:START -->
> Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application | propriétaire | macOS, Windows, iOS | — | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Dictée vocale système : on parle, le texte s'insère dans l'application active. La transcription
peut tourner **entièrement en local**, ce qui en fait un outil utilisable sur du contenu qu'on
ne veut pas envoyer à un tiers. Deux moteurs locaux, aucun n'est maison : **whisper.cpp** pour
la famille Whisper, **WhisperKit** (SDK Argmax) pour les modèles NVIDIA Parakeet. Le moteur de
l'éditeur, la famille S1, est côté cloud — avec Ultra Cloud, Deepgram Nova 3 / Nova 2 / Nova
Medical, et un partenariat Cohere Transcribe annoncé.

Note de rangement : la taxonomie décrit `media/ingestion` comme l'ingestion de médias pour
donner à un assistant une entrée multimodale. Superwhisper va dans l'autre sens — c'est une
**entrée utilisateur**, pas une ingestion pour agent. C'est le seul emplacement honnête de la
taxonomie fermée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Dicter du texte long — documentation, messages, notes — plus vite qu'au clavier, dans n'importe quelle application | **Poste Linux ou travail dans WSL** : il n'existe pas de version Linux |
| Transcrire du contenu confidentiel sans sortie réseau, en s'en tenant aux modèles locaux | Sous **Windows**, l'éditeur documente cinq manques : pas de FileSync, dossier applicatif non personnalisable (forcé sur `%LOCALAPPDATA%\com.superwhisper.app`), pas de « hold shift to auto-send », pas de simulation de frappes, intégrations agentiques encore « en développement » |
| Enregistrer et transcrire une réunion, y compris au palier gratuit | Matériel non Apple Silicon si l'on vise les gros modèles : l'éditeur oriente les Mac Intel anciens et les PC Windows vers un modèle moyen, et pousse les Mac Intel vers le cloud |
| | **Aucune exigence de RAM n'est publiée**, ni par modèle ni globalement, sur aucune page de l'éditeur. Les chiffres qui circulent viennent de blogs d'applications concurrentes et ne sont pas repris ici ; pour dimensionner, se référer aux tailles des poids GGML en amont, chez whisper.cpp |
| | **Aucune correspondance officielle** entre les noms commerciaux et les checkpoints OpenAI (tiny, base, small, medium, large-v3) : les tailles la suggèrent, l'éditeur ne la confirme pas |
| | **Précision en français et sur les acronymes : aucune donnée chiffrée, nulle part.** Ce qui est sourcé : l'anglais est la langue la plus forte des modèles hors ligne, et Cohere Transcribe couvre 14 langues dont le français. Les acronymes relèvent du vocabulaire personnalisé et des prompts, non documentés ni mesurés |
| | Disponibilité des modèles Parakeet **sous Windows** non vérifiée : WhisperKit est à l'origine une brique Apple/CoreML, la restriction à macOS et iOS est probable mais non confirmée |
| | Exigence de logiciel libre : c'est fermé, et le moteur de l'éditeur est cloud |
| | Donner à un **agent** la capacité de regarder une vidéo : usage différent → [[Claude Video]] |

## Mise en œuvre

- Installation — application macOS, Windows 10/11 et iOS ; **une seule licence couvre les trois**
- Point d'entrée — raccourci système de dictée ; le texte s'insère dans l'application active
- Prérequis — Apple Silicon pour les gros modèles locaux ; aucune exigence de RAM publiée par l'éditeur
- Exécution — sur le poste, hors ligne pour les modèles locaux ; 100+ langues et dialectes, traduction vers l'anglais
- Coût — freemium : 3 000 mots d'essai des fonctions Pro, puis palier gratuit à vie (dictée partout, enregistrement de réunion, petits modèles locaux illimités, prompts personnalisés). Pro à **8,49 $/mois, 84,99 $/an, ou 249,99 $ à vie**, remboursement 30 jours, Enterprise sur devis

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

Les colonnes vitesse et précision sont des notes de 1 à 10 **auto-déclarées par l'éditeur** :
ni WER, ni RTF, ni matériel de référence. Seul point confirmé sur les poids : Whisper Large V3
complet tourne bien en local via whisper.cpp, plus lent et plus précis que la distillation
turbo. Ne pas confondre **whisper.cpp**, le moteur ASR employé ici, avec llama.cpp : projets
distincts, même base ggml.

## Écosystème

### Alternatives

<!-- Aucune : les concurrents (MacWhisper, Wispr Flow, VoiceInk) ne sont pas fichés dans le brain. -->

## Ressources

- Documentation — https://superwhisper.com/docs/models/
- Site — https://superwhisper.com

## Voir aussi

- [[Médias]] — le hub du domaine
- [[Speech models]] — les modèles de parole et la transcription automatique
- [[Quantization]] — ce qui explique les paliers de 75 Mo à 3 Go
- [[Inference optimization]] — l'accélération de l'inférence
