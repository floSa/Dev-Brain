---
role: brique
nom: Laya
alias: [Laya decision model, laya-typed-decisions, laya-multilingual, convaiinnovations/laya, Convai Laya]
pitch: "Modèle de décision à poids ouverts de Convai Innovations (Apache-2.0), à ajuster avant usage — encodeur ModernBERT de 421 M (mmBERT de 322 M en multilingue) dont les poids de base font 0,362 sur son banc, sous la classe majoritaire (0,461), contre 0,766 pour le checkpoint ajusté ; texte seul, 512 à 1 024 tokens de contexte ; 0,84 Go en FP16, 33 ms sur Tesla T4 en multilingue."
categorie: llm/sortie-structuree
famille: modele
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Clef]]", "[[d1-3B]]", "[[d1-omni-600M]]"]
tags: [structured-output, classification, calibration, text-classification, edge-inference]
url_docs: https://huggingface.co/convaiinnovations/laya
url_repo: https://github.com/NandhaKishorM/laya
---

# Laya

<!-- AUTO:BANDEAU:START -->
> Modèle de décision à poids ouverts de Convai Innovations (Apache-2.0), à ajuster avant usage — encodeur ModernBERT de 421 M (mmBERT de 322 M en multilingue) dont les poids de base font 0,362 sur son banc, sous la classe majoritaire (0,461), contre 0,766 pour le checkpoint ajusté ; texte seul, 512 à 1 024 tokens de contexte ; 0,84 Go en FP16, 33 ms sur Tesla T4 en multilingue.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un [[Modèle de décision|modèle de décision]] **à ajuster** de Convai Innovations (Nandakishor M), trois checkpoints Hugging Face créés les 18 et 19 septembre 2026, modifiés pour la dernière fois le 2026-10-03 ; dépôt GitHub `NandhaKishorM/laya` poussé le 2026-10-19 (lecture du 2026-10-20). C'est un **encodeur bidirectionnel**, pas un LLM : ModernBERT-large (395 M) plus une tête de décision de deux couches, soit 421 M de paramètres pour `laya` (anglais) et `laya-typed-decisions` ; mmBERT-base (322 M) pour `laya-multilingual`, annoncé sur plus de 100 langues. Chaque option est notée à son propre marqueur `[MASK]`, un softmax par question donne les probabilités, et toutes les questions d'un appel sont traitées en une passe. Un **routeur** (`Router`) choisit le checkpoint selon la langue. Le chiffre de vitrine de 0,766 appartient au checkpoint **ajusté** sur le jeu d'entraînement de son banc, pas aux poids de base.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un **petit modèle à ajuster** sur ses propres décisions étiquetées : 0,84 Go en FP16 (0,42 Go en 8 bits), notebook Kaggle 2 × T4 (environ 4 à 5 h pour quatre époques sur ~30 000 questions, README du dépôt) et script Apple Silicon | Un modèle **prêt à l'emploi en zéro exemple** : poids de base à 0,362 sur son banc, sous la classe majoritaire (0,461) ; 4,43 au score complet du classement amont → [[Clef]] ou [[d1-3B]] |
| **CPU, navigateur ou NPU** : portages communautaires (ONNX 8 bits de 524 Mo en WebAssembly, CoreML sur Apple Neural Engine, MLX) et répertoires de SDK Go, Rust, Java, .NET, TypeScript dans le dépôt | Une **image** ou un **audio** en entrée : texte seul → [[d1-3B]], [[d1-omni-600M]] |
| **Apache-2.0** vérifiée au dépôt GitHub (fichier `LICENSE`) et sur la carte, sans seuil de chiffre d'affaires | Une question à **beaucoup d'options** (50 et plus) ou à **échelle ordinale** : Banking77 à 0,425 par défaut contre 0,870 pour Jev, SST-5 à 0,372 |
| Plus de **100 langues** avec `laya-multilingual` | Des **probabilités fiables sans recalage** : le modèle « sort surconfiant », température à ajuster par type de question |

## Mise en œuvre

- Installation — `pip install laya` (Python 3.10 ou plus) ; extras `laya[serve]` (serveur HTTP), `laya[mcp]`, `laya[langchain]`, `laya[onnx]`, `laya[fast]` (noyaux TileLang)
- Point d'entrée — `Router().predict(état, questions)` ; `model="multilingual"` et `max_len=8192` pour les longs documents ; l'ajustement par le notebook Kaggle ou le script Apple Silicon du dépôt
- Prérequis — contexte de 512 tokens (anglais) ou 1 024 (multilingue et `typed-decisions`) par défaut, 8 192 en multilingue avec `max_len=8192` ; plus de 50 options dans une question : relever `head_max_len`
- Exécution — poste, CPU, navigateur ; aucune API éditeur
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Le piège du score de vitrine.** `laya-typed-decisions` fait 0,766 sur le banc `typed-decisions` (400 cas, 2 000 décisions) parce qu'il a été ajusté sur le jeu d'entraînement de ce banc ; `laya` (poids de base) fait 0,362, au-dessus du hasard (0,318) mais **sous la classe majoritaire** (0,461). L'éditeur publie les deux et l'écrit ; reste qu'un score cité sans l'autre trompe. Transposé à une autre tâche, le checkpoint ajusté redevient un modèle de base. Voir [[Lire un score publié]].
- **Ajuster dégrade la calibration.** Carte lue le 2026-10-20 : checkpoint ajusté, Brier 0,062 mais ECE 0,213 avant recalage. Une température par type de question et nombre d'options fait passer l'ECE moyen de 0,466 à 0,081 pour `laya`, d'après la carte ; le classement amont (édition 0.3.1, 2026-10-10) note le **checkpoint de base** : 4,43 au score complet, couverture de 0,76 (24 % du poids de l'indice, des épreuves interactives, non exécuté), ECE 0,140.
- **Points faibles listés par l'éditeur** : `noul` peut suivre le libellé de ses options plutôt que l'état (un « non » confiant sur une entrée nettement positive) ; `action.act_probability` ne porte aucun signal exploitable ; l'échelle ordinale est la primitive la plus faible. Se rabattre sur un `choice` à deux options.
- **Latences par matériel, jamais comparables entre elles.** Sur Tesla T4 (carte) : `laya` 39,5 ms et `laya-multilingual` 32,8 ms pour une question, 72,3 ms pour dix questions groupées en multilingue. Posts de tiers, essais uniques : 3,7 ms sur Apple Neural Engine d'un M5 Pro (CoreML), 12,3 ms sur un M3 Max (MLX, FP16), 375 à 660 ms par appel de cinq questions sur le CPU d'un M2. Le classement amont note 5,8 ms de médiane pour Laya, par un chemin à noyaux fusionnés et graphes CUDA (19,8 ms en chemin standard) : la valeur est propre au protocole.
- **Banc indépendant** (751 états, 9 suites, `instax-dutta/sysone-bench`) : Jev gagne six suites, Laya deux (AG News, MNLI), une égalité ; Laya en local sur CPU d'un M2, Jev par API.
- **Le comparatif à 140 étiquettes d'un acteur du secteur** (anth.us) : moteur contre moteur, Jev 0,768 et Laya 0,722 ; après ajustement, Laya 0,896. Auteur intéressé, protocole décrit.

## Écosystème

### Alternatives

- [[Clef]] — Famille de modèles de décision de Cloudflare à poids ouverts (Apache-2.0) — Clef 27 Md, Clef-flash 9 Md et Clef-omni 30 Md MoE : un état et des questions typées donnent une probabilité par option en une passe, sans texte ; entrée texte, image et vidéo (audio pour Clef-omni) ; 54,7, 18,8 et 70,5 Go en BF16, donc un GPU de serveur. — prêt à l'emploi en zéro exemple, avec image et vidéo, mais 18,8 à 54,7 Go de poids sur un GPU de serveur.
- [[d1-3B]] — Modèle de décision à poids ouverts de Liquid AI (3,1 Md, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel, à lire avant de livrer chez un client) — un état en texte ou en image et des questions typées donnent une probabilité par option en une passe, sans texte ; 6,25 Go en BF16, 8 ms sur RTX 4090 et 30 ms sur Apple M5 Pro selon Liquid. — prêt à l'emploi avec l'image, 6,25 Go, mais sous la LFM Open License (seuil de 10 M$ de chiffre d'affaires) et sans recette d'ajustement publiée.
- [[d1-omni-600M]] — Modèle de décision expérimental à poids ouverts de Liquid AI (587 M, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel) — un état en texte avec une image ou un clip audio de 30 s en anglais donne des probabilités typées en une passe ; 2,35 Go en FP32 ; aucune latence publiée par l'éditeur ; 2 documents sur 8 triés dans l'essai d'un tiers. — l'audio en entrée sur 587 M, mais expérimental, anglais seulement et sous la LFM Open License.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/convaiinnovations/laya
- Dépôt : https://github.com/NandhaKishorM/laya
- Tutoriel — ajustement sur 2 × T4 (Kaggle) : https://github.com/NandhaKishorM/laya/blob/main/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb
- Vidéo — « Laya », AI WITH Rithesh, 9 min 08 : https://www.youtube.com/watch?v=7O3TaHf9cmg

## Voir aussi

- [[Modèle de décision]] — la variante à encodeur et marqueur par option
- [[Choisir entre règle, classifieur, modèle de décision et LLM]] — Laya ajusté comme classifieur à coût nul par appel
- [[Entraîner pour la calibration]] — la récompense par règle de notation strictement propre et le recalage par température
- [[Lire un score publié]] — 0,766 contre 0,362 : quel checkpoint, quel jeu
- [[Comparatif - Modèles de décision]] — ce qui départage les quatre fiches
- [[Licences de modèles open weights]] — Apache-2.0 lue dans le fichier du dépôt
- [[Mesurer une latence]] — un modèle, des matériels très différents, de 3,7 ms à 660 ms
- [[Fine-tuning]] — ajuster un modèle sur ses propres décisions
