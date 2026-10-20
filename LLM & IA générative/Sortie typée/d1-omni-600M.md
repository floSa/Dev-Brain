---
role: brique
nom: d1-omni-600M
alias: [d1-omni, Liquid d1-omni, LiquidAI/d1-omni-600M]
pitch: "Modèle de décision expérimental à poids ouverts de Liquid AI (587 M, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel) — un état en texte avec une image ou un clip audio de 30 s en anglais donne des probabilités typées en une passe ; 2,35 Go en FP32 ; aucune latence publiée par l'éditeur ; 2 documents sur 8 triés dans l'essai d'un tiers."
categorie: llm/sortie-structuree
famille: modele
licence_type: source-available
maturite: experimental
alternatives: ["[[d1-3B]]", "[[Laya]]"]
tags: [structured-output, classification, calibration, multimodal, speech, edge-inference]
url_docs: https://huggingface.co/LiquidAI/d1-omni-600M
url_repo: 
---

# d1-omni-600M

<!-- AUTO:BANDEAU:START -->
> Modèle de décision expérimental à poids ouverts de Liquid AI (587 M, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel) — un état en texte avec une image ou un clip audio de 30 s en anglais donne des probabilités typées en une passe ; 2,35 Go en FP32 ; aucune latence publiée par l'éditeur ; 2 documents sur 8 triés dans l'essai d'un tiers.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | source-available | à charger dans un runtime | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un [[Modèle de décision|modèle de décision]] de Liquid AI, dépôt Hugging Face `LiquidAI/d1-omni-600M` créé le 2026-10-05, modifié le 2026-10-07 (lecture du 2026-10-20), « checkpoint de recherche précoce » selon l'éditeur. 587 M de paramètres : un tronc et une tête de 381 M, un encodeur de vision SigLIP2 de 94 M (12 couches) et un encodeur audio FastConformer de 112 M (17 couches). Le tronc est un **encodeur bidirectionnel** de 16 couches : chaque option reçoit un marqueur `<mask>`, une tête de décision de deux couches lit l'état caché à chacun, un softmax par question donne les probabilités. Une requête porte **une image ou un clip audio de 30 s au plus, jamais les deux** ; avec une image, l'état et la question sont coupés à 896 tokens. Contexte de 16 384 tokens. L'audio a été entraîné sur des échanges entre un locuteur anglophone et un assistant : anglais seulement. Licence : LFM Open License v1.0, comme [[d1-3B]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une **commande vocale** décidée sans étape de transcription, sur un modèle de 587 M : 8 clips sur 10 dans l'essai d'un tiers, environ 74 ms par clip sur MacBook Air M5 | Un **tri de documents photographiés** : 2 sur 8 dans le même essai, « legal notice » répondu à sept documents sur huit, avec 98 % de confiance → [[d1-3B]] |
| Un très petit modèle de décision multimodal : 2,35 Go en FP32, 1,17 Go en FP16, GGUF de 0,67 Go (Q8_0 avec audio et vision) | Une **mesure fiable** : Liquid ne publie aucune latence ni aucun score image ou audio ; « les bancs audio sont un problème ouvert » |
| Des questions **texte** à calibration par type : températures stockées dans la configuration (1,0 à 1,75) | Un **état en texte seul exigeant** : 9,45 au score complet du classement amont (9,09 dans le fichier du 2026-10-16), ECE 0,1284 → [[Laya]] ajusté ou [[Clef]] |

## Mise en œuvre

- Installation — `pip install "transformers>=5.15" torch torchvision pillow soundfile` ; poids `LiquidAI/d1-omni-600M` avec `trust_remote_code=True`, GGUF `LiquidAI/d1-omni-600M-GGUF` pour llama.cpp
- Point d'entrée — `model.system_one(état, questions, images=None, audio=None)` ; `system_one_batch` et `probabilities` pour les distributions brutes
- Prérequis — entraîné en FP32 ; **FP16** sur GPU garde les réponses (même réponse de tête sur 243 lignes texte, 214 image, 416 audio selon la carte), **éviter BF16** (réponse de tête changée sur 0,8 % des lignes texte et 1,7 % des lignes audio)
- Exécution — poste ou appareil de bord ; personne ne l'héberge, d'après l'essai d'un tiers
- Coût — gratuit sous la licence, le coût est celui de la machine

## Limites à connaître

- **Checkpoint expérimental.** « Nous ne publions pas de chiffres d'inférence pour d1-omni-600M » (carte). Un 15,8 ms pour une question en FP16 existe sur MacBook Air M5, mesuré par un tiers, et le classement amont donne 10,9 ms pour ses lignes de texte sur un autre matériel : aucune des deux valeurs n'est celle de l'éditeur ni ne se compare à l'autre.
- **Audio** : d1-omni et Clef-omni (fiche [[Clef]], 64 Go de mémoire GPU) sont les deux seuls modèles du comparatif à lire un clip ; l'audio de d1-omni est anglais seulement.
- **Essai d'un tiers : très petits effectifs.** Dix clips synthétisés avec les voix du Mac, huit documents fabriqués par l'auteur, étiquettes de l'auteur, un seul passage. Les deux erreurs vocales sont les phrases les plus vagues (« Never mind, forget what I just asked », « Something chill for the evening, maybe lo-fi »). Pistes sur l'échec des documents, toutes non testées : checkpoint précoce, encodeur de vision de 94 M qui lit mal les photos pleine taille, coupe à 896 tokens.
- **Aucune option « je ne sais pas »** et aucune explication : un modèle de décision.
- **Licence** : voir [[d1-3B]], mêmes conditions (seuil de 10 M$ de chiffre d'affaires annuel, à lire avant de livrer chez un client).

## Écosystème

### Alternatives

- [[d1-3B]] — Modèle de décision à poids ouverts de Liquid AI (3,1 Md, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel, à lire avant de livrer chez un client) — un état en texte ou en image et des questions typées donnent une probabilité par option en une passe, sans texte ; 6,25 Go en BF16, 8 ms sur RTX 4090 et 30 ms sur Apple M5 Pro selon Liquid. — 3,1 Md et l'image seule, sans audio ; 8 documents sur 8 triés dans l'essai du même tiers, et des latences publiées par matériel.
- [[Laya]] — Modèle de décision à poids ouverts de Convai Innovations (Apache-2.0), à ajuster avant usage — encodeur ModernBERT de 421 M (mmBERT de 322 M en multilingue) dont les poids de base font 0,362 sur son banc, sous la classe majoritaire (0,461), contre 0,766 pour le checkpoint ajusté ; texte seul, 512 à 1 024 tokens de contexte ; 0,84 Go en FP16, 33 ms sur Tesla T4 en multilingue. — Apache-2.0 et texte seul : 0,84 Go, à ajuster, sans image ni audio.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/LiquidAI/d1-omni-600M
- Article — « Open d1 », blog Liquid AI, 2026-10-07 : https://www.liquid.ai/blog/d1-open
- Vidéo — « Liquid AI's d1-3B Decision Model Is WILD… I Tested It Locally! », AI WITH Rithesh, 10 min 05 : https://www.youtube.com/watch?v=rFs62hHdf5E

## Voir aussi

- [[Modèle de décision]] — la variante à encodeur et marqueur par option
- [[Choisir entre règle, classifieur, modèle de décision et LLM]] — ne pas trier de documents avec un checkpoint précoce
- [[Entraîner pour la calibration]] — températures par type de question
- [[Comparatif - Modèles de décision]] — ce qui départage les quatre fiches
- [[Licences de modèles open weights]] — une licence à seuil de chiffre d'affaires
- [[Mesurer une latence]] — les 15,8 ms d'un Air M5 ne sont pas les 10,9 ms du classement
- [[llama.cpp]] — le moteur des GGUF
