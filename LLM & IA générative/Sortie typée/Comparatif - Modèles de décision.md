---
role: comparatif
nom: Comparatif - Modèles de décision
categorie: llm/sortie-structuree
tags: [structured-output, classification, calibration]
---

# Comparatif - Modèles de décision

> On tranche sur : la licence (Apache-2.0 sans seuil, ou seuil de chiffre d'affaires), ce que le modèle lit (texte, image, vidéo, audio), la mémoire des poids, et le **score complet daté**, jamais le score de vitrine. Les latences se lisent **par matériel**, une ligne chacune, et ne se comparent pas entre elles.

![[Comparatif - Modèles de décision.base]]

## Les critères côte à côte

Relevé le 2026-10-20 sur les cartes Hugging Face, les fichiers `LICENSE` et la documentation Cloudflare ; scores et ECE du classement amont « Decision Index » (édition 0.3.1, relevé du 2026-10-10 dans un document de synthèse, puis fichier généré le 2026-10-16). Les six rendent les mêmes trois types de réponse (`noul`, `choice`, `score`) avec une probabilité par option et `output_tokens = 0` ; ce qui diffère, c'est la définition de `confidence` et ce qu'on fait des probabilités.

| Modèle | Licence | Taille | Entrées | Contexte | Mémoire des poids |
|---|---|---|---|---|---|
| [[Clef]] | Apache-2.0 | 27,36 Md | texte, JSON, image, vidéo | 65 536 | 54,7 Go (BF16) |
| [[Clef]] (Clef-flash) | Apache-2.0 | 9,41 Md | texte, JSON, image, vidéo | 24 576 (65 536 selon OpenRouter le 2026-10-10) | 18,8 Go (BF16) |
| [[Clef]] (Clef-omni) | Apache-2.0 | 35,26 Md (30 Md MoE, 3 Md actifs) | + audio | 64 000 | 70,5 Go (BF16) |
| [[Laya]] | Apache-2.0 | 421 M (322 M en multilingue) | texte, e-mail, JSON | 512 ou 1 024 (8 192 en multilingue avec `max_len`) | 0,84 Go (FP16) |
| [[d1-3B]] | LFM Open License v1.0 : gratuit sous 10 M$ de chiffre d'affaires annuel | 3,12 Md | texte, JSON, image | 32 768 | 6,25 Go (BF16) |
| [[d1-omni-600M]] | idem | 587 M | texte, JSON, avec une image **ou** un clip audio de 30 s | 16 384 (896 avec une image) | 2,35 Go (FP32), 1,17 Go (FP16) |

Mémoire : paramètres × octets par paramètre, lue sur le fichier pour d1-3B ; 8 bits et 4 bits divisent par 2 et par 4, avant le cache de contexte (16 Kio par token pour d1-3B).

### Score daté et calibration

Le **score complet** note des tests privés ; le score public surestime d'environ 9 points les modèles ouverts testés, pas Jev. Citer le complet. Jev (API fermée, sans fiche) sert de repère. Les ECE sont ceux du 2026-10-10 ; le fichier du 2026-10-16 donne 0,078 pour Jev et laisse les autres inchangés.

| Modèle | Score complet 2026-10-10 | Score complet 2026-10-16 | Score public | ECE (plus bas = mieux) | Provenance de la ligne |
|---|---|---|---|---|---|
| Jev 1.13 (repère) | 60,11 | 60,11 | 57,96 | 0,074 | API appelée par les mainteneurs |
| Clef | 53,08 | 53,08 | 61,71 | 0,0395 | qui l'a soumise n'est pas indiqué |
| Clef-flash | 47,61 | 47,61 | 56,15 | 0,0249 | idem |
| Clef-omni | 49,32 | 48,28 | 56,54 | 0,0403 | exécuté par Cloudflare, sans soumission |
| d1-3B | 40,08 | 38,9 | 48,99 | 0,0468 | « soumis par LiquidAI » (suite publique), tests privés par les mainteneurs |
| d1-omni-600M | 9,45 | 9,09 | 17,90 | 0,1284 | idem |
| Laya (poids de base) | 4,43 | 4,43 | 6,19 | 0,140 | exécuté par les mainteneurs ; couverture de 0,76, **pas le checkpoint ajusté** (0,766 contre 0,362 sur le banc de l'éditeur) |

Le classement bouge vite : au fichier du 2026-10-16, des modèles qui ne sont pas fichés ici le dépassent (voir plus bas, Perplexity Decider).

### Latences par matériel

**Aucune ligne ne se compare à une autre** : le matériel, la précision, le protocole et le nombre de questions changent. Le même d1-3B répond en 8 ms, 30 ms ou 78 ms selon la machine. Voir [[Mesurer une latence]].

| Matériel (qui mesure) | Modèle | Latence | Protocole |
|---|---|---|---|
| RTX 4090 (Liquid) | d1-3B | 8 ms | une question, bf16, CUDA graphs, médiane de 20 passes ; 16 ms sans graphes |
| AMD MI325X (Liquid) | d1-3B | 9 ms | idem |
| Jetson AGX Thor, AGX Orin 64 Go, Orin Nano (Liquid) | d1-3B | 16, 26 et 50 ms | idem, une question à la fois |
| Apple M5 Pro (Liquid) | d1-3B | 30 ms (41 ms pour trois questions) | idem |
| MacBook Air M5, PyTorch sur GPU Apple (un tiers) | d1-3B | 78 ms ; 2 649 ms pour un état de 4 897 tokens | une mesure, 50 tokens |
| MacBook Air M5, FP16 (un tiers) | d1-omni-600M | 15,8 ms ; 74 ms par clip audio (médiane de 10) | une mesure ; l'éditeur ne publie rien |
| Tesla T4 (carte de Laya) | Laya | 39,5 ms (anglais), 32,8 ms (multilingue) ; 72,3 ms pour dix questions groupées | une question, T4 |
| Apple Neural Engine d'un M5 Pro, CoreML (un tiers) | Laya | 3,7 ms | post X, essai unique, portage communautaire |
| CPU d'un M2 (banc indépendant) | Laya | 375 à 660 ms par appel de cinq questions | banc tiers |
| 1 × RTX PRO 6000 (classement amont, `latency-v1`) | Clef · Clef-flash · d1-3B · d1-omni · Laya | 102,1 · 53,4 · 16,1 · 10,9 · 5,8 ms (médiane) | un client séquentiel, 750 lignes ; Laya par noyaux fusionnés et graphes CUDA (19,8 ms en chemin standard) |
| Pile Cloudflare, GPU non précisés (Cloudflare, 2026-10-01) | Clef · Clef-flash | 209,3 · 38,8 ms (médiane) | calcul seul, matériel non précisé |

Jev, API hébergée, sans fiche : 524,1 ms de médiane au classement amont, **aller-retour réseau compris**, donc non comparable aux lignes sur carte.

## Ce qui départage

- [[Clef]] — **Apache-2.0** sans seuil, **image, vidéo** et audio (Clef-omni) dans le même schéma que Jev, et la meilleure calibration du classement (ECE 0,0249 et 0,0395) ; mais de 18,8 à 70,5 Go de poids, donc un GPU de serveur, et des scores de qualité d'abord auto-rapportés par Cloudflare.
- [[d1-3B]] — le modèle qui **tient sur un poste** (6,25 Go) et lit une image, avec des latences publiées par matériel ; sous une **licence à seuil de 10 M$ de chiffre d'affaires annuel**, à lire avant toute livraison à un client, et 40,08 au score complet contre 53,08 pour Clef.
- [[d1-omni-600M]] — le plus petit modèle qui **lit l'audio** (587 M) ; checkpoint expérimental, aucune latence publiée, 9,45 au score complet, 2 documents sur 8 triés dans l'essai d'un tiers : à réserver à des essais.
- [[Laya]] — le plus léger (0,84 Go), **Apache-2.0**, CPU, navigateur et NPU ; mais **à ajuster** : 0,362 en zéro exemple contre 0,766 ajusté, texte seul, et « sort surconfiant ».

**Pas de fiche ici**, faute de licence lue, de poids ouverts ou d'évaluation :

- Jev (TypeSafe) — API fermée et payante (0,042 $ le million de tokens d'entrée, relevé du 2026-10-10), sans poids ; citée en repère.
- GLiDE (Fastino) — « poids bientôt » dans le classement amont ; rien à lire.
- GLiNER2.5-Decide (Fastino) — dépôt `fastino/GLiNER2.5-Decide`, `license: apache-2.0` sur la carte au 2026-10-20, 9,24 au score complet du fichier du 2026-10-16 ; non évalué ici, fichier de licence non lu.
- Perplexity Decider — dépôts `perplexity-ai/pplx-decider-*` sur Hugging Face ; la v1.2 de 27 Md est à 65,55 au score complet du fichier du 2026-10-16, au-dessus de Jev ; licence non lue, donc pas de page.
- Microsoft-Decision-1 — listé sur OpenRouter le 2026-10-10 d'après le document de synthèse ; non lu.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Sortie typée]] — le hub du dossier.
- [[Modèle de décision]] — la notion : l'objet, les trois types de questions, ce que ce n'est pas.
- [[Choisir entre règle, classifieur, modèle de décision et LLM]] — avant de choisir un modèle, savoir si la règle suffit.
- [[Licences de modèles open weights]] — la licence se lit au dépôt, un seuil de chiffre d'affaires change la livraison.
- [[Comparatif - Garde-fous pour LLM]] — le comparatif voisin : filtrer les entrées et les sorties d'un LLM ; un modèle de décision peut tenir ce rôle, sans le générer.
