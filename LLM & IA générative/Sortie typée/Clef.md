---
role: brique
nom: Clef
alias: [Clef-flash, Clef-omni, Cloudflare Clef, Cloudflare/clef]
pitch: "Famille de modèles de décision de Cloudflare à poids ouverts (Apache-2.0) — Clef 27 Md, Clef-flash 9 Md et Clef-omni 30 Md MoE : un état et des questions typées donnent une probabilité par option en une passe, sans texte ; entrée texte, image et vidéo (audio pour Clef-omni) ; 54,7, 18,8 et 70,5 Go en BF16, donc un GPU de serveur."
categorie: llm/sortie-structuree
famille: modele
licence_type: open-source
maturite: beta
alternatives: ["[[d1-3B]]", "[[Laya]]"]
tags: [structured-output, classification, calibration, multimodal, llm]
url_docs: https://huggingface.co/Cloudflare/clef
url_repo: 
---

# Clef

<!-- AUTO:BANDEAU:START -->
> Famille de modèles de décision de Cloudflare à poids ouverts (Apache-2.0) — Clef 27 Md, Clef-flash 9 Md et Clef-omni 30 Md MoE : un état et des questions typées donnent une probabilité par option en une passe, sans texte ; entrée texte, image et vidéo (audio pour Clef-omni) ; 54,7, 18,8 et 70,5 Go en BF16, donc un GPU de serveur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Trois modèles de décision à poids ouverts de Cloudflare, dépôts Hugging Face `Cloudflare/clef` et `Cloudflare/clef-flash` créés le 2026-09-30, `Cloudflare/clef-omni` le 2026-10-09, modifiés le 2026-10-19 (lecture du 2026-10-20). Un [[Modèle de décision|modèle de décision]] : à partir d'un état et de questions typées (`noul`, `choice`, `score`), il rend une probabilité par option de chaque question, en une passe avant, sans écrire un token. **Clef** : 27,36 Md de paramètres, post-entraîné de Qwen3.8-27B. **Clef-flash** : 9,41 Md, de Qwen3.5-9B. **Clef-omni** : 35,26 Md au total, de Qwen3-Omni-30B-A3B (MoE, 3 Md actifs), avec **audio** en plus. Le modèle Qwen est **gelé** ; une tête de schéma conjointe note toutes les options de toutes les questions ensemble, avec des adaptateurs de bas rang (rang 256). Les cartes disent l'API « entièrement compatible avec Jev et SystemOne ».

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un modèle de décision à **poids ouverts en Apache-2.0** (fichier `LICENSE` lu dans les trois dépôts), livrable chez un client sans seuil | Un **poste sans GPU de serveur** : 54,7 Go (Clef) et 18,8 Go (Clef-flash) en BF16, 64 Go de mémoire GPU pour Clef-omni selon sa carte → [[d1-3B]] (6,25 Go) ou [[Laya]] (0,84 Go) |
| Le **même schéma que Jev** (`/v1/systemone`) pour changer de fournisseur par l'URL, la clé et le champ `model` | Un **seuil de confiance repris d'un autre modèle** : la formule de `confidence` n'est pas publiée, un seuil se règle sur ses données |
| **Image et vidéo** en entrée (audio pour Clef-omni), dans une seule passe | Un **raisonnement à connaissances** : sur GPQA Diamond, BBH et MMLU-Pro, Clef perd de 17 à 30 points contre Jev dans la carte |
| La **calibration** la meilleure du classement amont (ECE 0,0249 pour Clef-flash et 0,0395 pour Clef, relevés le 2026-10-10) | Une **mesure indépendante par tâche** : le classement note des moyennes sur 37 benchmarks, pas la tâche visée |

## Mise en œuvre

- Installation — poids sur Hugging Face (`Cloudflare/clef`, `clef-flash`, `clef-omni`) avec leur code `joint_schema_model.py` ; `snapshot_download` puis `load_release_model`
- Point d'entrée — serveur SGLang (image `lmsysorg/sglang:dev-clef`, recette de la carte pour H200, B200 et B300), qui répond en `POST /v1/systemone` ; ou en Python `encode_record` puis `systemone(model, processor, requête)`, avec `images` et `videos` dans la requête
- Prérequis — testé avec `torch` 2.11 et `transformers` 5.10.2 sur un H200 ; Clef-omni demande environ 64 Go de mémoire GPU en BF16 selon sa carte ; `encode_record` borne l'entrée à 16 384 tokens par défaut
- Exécution — local sur GPU de serveur, ou service Workers AI de Cloudflare (payant, cité ici en texte simple, sans page) : 0,24 $, 0,038 $ et 0,15 $ par million de tokens d'entrée pour Clef, Clef-flash et Clef-omni, sortie non facturée, relevés le 2026-10-20 ; contexte de 65 536, 24 576 et 64 000 tokens selon la même documentation
- Coût — gratuit, Apache-2.0 ; le coût est celui de la machine

## Limites à connaître

- **Scores de qualité auto-rapportés.** Le billet de Cloudflare présente 10 benchmarks sur 41 de la carte ; Clef bat Jev sur 26 lignes sur 41 et perd de 17 à 30 points sur trois bancs de raisonnement. Le classement amont « Decision Index » (édition 0.3.1, 2026-10-10) donne, au **score complet**, 53,08 pour Clef et 47,61 pour Clef-flash, contre 61,71 et 56,15 au score public : le score public surestime d'environ 9 points, comme pour les autres modèles ouverts testés.
- **Le checkpoint évalué est-il celui qu'on télécharge ?** Question ouverte : un seul dépôt, un seul commit de poids (2026-09-30), mais la carte parle d'une « exécution interne » sans identifier le checkpoint. Aucun contrôle équivalent à celui du piège de [[Laya]] n'est publié.
- **`confidence` sans formule publiée** : ni la probabilité maximale ni un moins l'entropie normalisée d'après les chiffres de la carte. Un seuil réglé sur Jev ne se transpose pas.
- **Contexte de Clef-flash divergent** le même jour : 24 576 tokens sur la page Workers AI (2026-10-20), 65 536 selon OpenRouter (2026-10-10).
- **Latences non comparables.** 209,3 ms (Clef) et 38,8 ms (Clef-flash) par la carte de Cloudflare, matériel non précisé ; 102,1 et 53,4 ms au classement amont, une RTX PRO 6000 décrite pour le protocole. Voir [[Comparatif - Modèles de décision]].
- **Le service de fine-tuning de Cloudflare** (apprentissage par renforcement, avec des ingénieurs déployés chez le client, libre-service « plus tard ») n'a ni prix ni date : à citer, pas à planifier.

## Écosystème

### Alternatives

- [[d1-3B]] — Modèle de décision à poids ouverts de Liquid AI (3,1 Md, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel, à lire avant de livrer chez un client) — un état en texte ou en image et des questions typées donnent une probabilité par option en une passe, sans texte ; 6,25 Go en BF16, 8 ms sur RTX 4090 et 30 ms sur Apple M5 Pro selon Liquid. — local sur un poste de 6,25 Go et une image dans l'état, mais une licence à seuil de 10 M$ de chiffre d'affaires et un classement amont plus bas (40,08 contre 53,08 au score complet, relevé du 2026-10-10).
- [[Laya]] — Modèle de décision à poids ouverts de Convai Innovations (Apache-2.0), à ajuster avant usage — encodeur ModernBERT de 421 M (mmBERT de 322 M en multilingue) dont les poids de base font 0,362 sur son banc, sous la classe majoritaire (0,461), contre 0,766 pour le checkpoint ajusté ; texte seul, 512 à 1 024 tokens de contexte ; 0,84 Go en FP16, 33 ms sur Tesla T4 en multilingue. — un encodeur de 421 M en Apache-2.0 qui tient sur CPU, mais à ajuster : poids de base à 4,43 au score complet du classement amont, texte seul.

## Ressources

- Documentation — carte de Clef : https://huggingface.co/Cloudflare/clef
- Documentation — cartes de Clef-flash et Clef-omni : https://huggingface.co/Cloudflare/clef-flash · https://huggingface.co/Cloudflare/clef-omni
- Article — « Clef decision models », blog Cloudflare, 2026-10-01 : https://blog.cloudflare.com/clef-decision-models/
- Documentation — Workers AI : https://developers.cloudflare.com/workers-ai/models/clef/

## Voir aussi

- [[Modèle de décision]] — ce qu'est un modèle de décision, et les trois types de questions
- [[Entraîner pour la calibration]] — la recette de Cloudflare (entropie croisée à lissage d'étiquettes, Brier, étape de renforcement) et les ECE publiés
- [[Choisir entre règle, classifieur, modèle de décision et LLM]] — quand le prendre, et quand garder le `if`
- [[Décomposer une question en signaux étroits]] — la façon de lui poser la question
- [[Comparatif - Modèles de décision]] — ce qui départage les quatre fiches
- [[Licences de modèles open weights]] — le fichier `LICENSE` lu dans le dépôt
- [[Qwen]] — la famille sur laquelle Clef est post-entraîné
- [[SGLang]] — le moteur qui sert Clef
