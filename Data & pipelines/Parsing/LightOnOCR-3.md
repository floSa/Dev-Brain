---
role: brique
nom: LightOnOCR-3
alias: [LightOnOCR 3, LightOnOCR-3-0.8B, LightOnOCR-3-1B, LightOnOCR-3-4B, lightonai/LightOnOCR-3-4B, LightOn OCR]
pitch: "Famille de trois modèles d'OCR à poids ouverts de LightOn (0,8B, 1B, 4B, Apache-2.0) : un seul modèle vision-langage lit la page en une génération et rend le Markdown ou, en mode grounding, l'étiquette et la boîte de chaque bloc, la description des images et les graphiques en tableaux ; servi par vLLM, scores auto-rapportés."
categorie: data/parsing
famille: modele
licence_type: open-source
maturite: beta
alternatives: ["[[olmOCR]]", "[[PaddleOCR]]", "[[MinerU]]", "[[Surya]]"]
tags: [ocr, document-parsing, vision-language, layout-analysis, gpu, self-hosted]
url_docs: https://github.com/lightonai/LightOnOCR
url_repo: https://github.com/lightonai/LightOnOCR
---

# LightOnOCR-3

<!-- AUTO:BANDEAU:START -->
> Famille de trois modèles d'OCR à poids ouverts de LightOn (0,8B, 1B, 4B, Apache-2.0) : un seul modèle vision-langage lit la page en une génération et rend le Markdown ou, en mode grounding, l'étiquette et la boîte de chaque bloc, la description des images et les graphiques en tableaux ; servi par vLLM, scores auto-rapportés.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Famille de trois modèles d'OCR à poids ouverts de la société française LightOn, sous Apache-2.0 sur les trois tailles** (champ `license` de chaque carte Hugging Face et fichier `LICENSE` du dépôt, lus le 2026-10-20). Un modèle vision-langage reçoit l'image d'une page et rend du Markdown (invite vide) ou, avec l'invite `grounding`, une étiquette et une boîte pour chaque bloc, une description pour les images et un tableau de données pour les graphiques. Trois tailles : **0,8B** (852 985 920 paramètres, base Qwen3.5), **1B** (1 005 647 872, architecture de LightOnOCR-2, remplaçant direct de la v2) et **4B** (4 539 265 536, base Qwen3.5). Les cartes datent des 6 et 7 octobre 2026, modifiées pour la dernière fois le 2026-10-09 ; dernier commit du dépôt client le 2026-10-08.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une **seule chaîne** à héberger : texte, mise en page, tableaux, formules et graphiques dans le même appel → [[OCR vision-langage en une passe avec grounding]] | Pas de GPU NVIDIA ni de Mac à mémoire unifiée : le dépôt documente vLLM, un serveur → [[Indra OCR]] ou [[Tesseract]] sur CPU |
| Des **boîtes englobantes** par bloc pour citer la source d'une réponse, et des graphiques à convertir en données | Télécopies, scans anciens, manuscrits à lire sans relecture : l'échec des trois tailles sur une page de télécopie est mesuré ; un modèle de 35 milliards reste devant sur les vieux scans selon les tableaux de LightOn |
| Poids **Apache-2.0** sur les trois tailles, usage commercial permis, confidentialité du local | Lecture littérale exigée : un modèle vision-langage peut réécrire ce qu'il lit (cf. [[OCR classique vs modèles vision-langage pour documents]]) |
| Une migration depuis LightOnOCR-2 : la taille 1B garde l'architecture, l'invite vide et la résolution de 1540 px | Un lot de milliers de pages sur un portable : 52 s par page pour le 4B sur MacBook Air M5, environ le double sur pages denses |
| Un banc à reproduire : LightOn publie ses scripts (`benchmarks/`) | Dépendre de scores indépendants : aucune mesure de tiers n'était trouvée le 2026-10-10 |

## Mise en œuvre

- Installation — `uv sync --extra vllm` dans le dépôt `lightonai/LightOnOCR` (client, CLI et visionneuse) ; l'extra épingle vLLM 0.30.0 avec transformers 5.16.1 (transformers 5.17 casse les modèles 1B sur vLLM 0.30.0, vLLM 0.27.1 fait boucler tous les modèles, d'après le README)
- Point d'entrée — `vllm serve lightonai/LightOnOCR-3-1B ...` puis `lightonocr paper.pdf --mode grounding` (sortie par page : image, Markdown, JSON des blocs en grounding) ; un appel est un message utilisateur avec l'image, plus le mot `grounding` pour le mode ancré
- Prérequis — GPU compatible vLLM ; pages à 2048 px pour 0,8B et 4B, 1540 px pour le 1B ; température 0,1 recommandée, pas le décodage glouton ; sur Mac Apple Silicon, un banc tiers a utilisé MLX et mlx-vlm en bfloat16 (conversions communautaires, non évaluées)
- Exécution — local : serveur vLLM compatible OpenAI sur un port interne, requêtes en parallèle (le CLI garde 64 pages en vol) ; poids : 1,71 Go (0,8B), 2,01 Go (1B), 9,08 Go (4B) en bfloat16
- Coût — gratuit, code et poids Apache-2.0 ; GPU ou machine à mémoire unifiée à fournir

## Limites à connaître

- **Scores auto-rapportés.** Relevés par LightOn le 2026-10-08 : olmOCR-Bench 86,3 (4B), 85,5 (0,8B), 84,5 (1B) ; ParseBench 75,1, 74,6, 71,4 ; fr-bench-pdf2md 74,1, 70,5, 69,6. Le choix des concurrents affichés est celui de l'éditeur, qui dit qu'un écart d'un point est dans le bruit du format de sortie (cf. [[Lire un score publié]]).
- **Banc local d'un testeur** (vidéo AI WITH Rithesh, 2026-10-10, MacBook Air M5 24 Go, MLX, bfloat16, 1540 px, décodage glouton, quatre pages fabriquées, un graphique) : CER 0,30 / 0,25 / 0,30 %, toutes les erreurs sur la télécopie ; F1 de boîtes à IoU 0,5 de 0,938 / 0,926 / 0,947 ; seul le 4B lit exactement les six barres du graphique ; 10,07 / 11,09 / 52,15 s par page, 2,8 / 7,9 / 10,5 Go de mémoire de pointe. Ce n'est pas un classement (cf. [[Évaluer un OCR]]).
- **Pas de grounding hors v3.** LightOnOCR-1 et -2 font de l'OCR seul.
- **Étiquette `aside_text`** (texte tourné en marge) jamais produite par les trois tailles sur le banc local, bien qu'elle soit dans la liste.
- **Le 1B** a une pointe de mémoire anormale sur MacBook Air M5 (7,9 Go, quatre fois ses poids) : non expliquée.
- **Non vérifié** : le comportement sur documents français hors banc de LightOn, la qualité des versions quantisées, le comportement soutenu sur un lot long.

## Écosystème

### Alternatives

- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.
- [[Surya]] — Boîte à outils OCR de Datalab à base d'un modèle vision-langage de 650 millions de paramètres : texte, mise en page avec ordre de lecture et tableaux d'une page en plus de 90 langues ; code Apache-2.0, poids sous OpenRAIL-M modifiée (gratuit sous 5 M$ de revenu ou de financement), servi par vLLM ou llama.cpp.

## Ressources

- Documentation — https://huggingface.co/lightonai/LightOnOCR-3-4B (cartes des trois tailles : `-4B`, `-1B`, `-0.8B`)
- Dépôt — https://github.com/lightonai/LightOnOCR
- Article — https://huggingface.co/blog/lightonai/lightonocr-3 (LightOn, 2026-10-08, éditeur)
- Papier — https://arxiv.org/abs/2601.14251 (LightOnOCR-2, janvier 2026, la lignée précédente)
- Vidéo — https://www.youtube.com/watch?v=sPPmHJZCl_s (AI WITH Rithesh, 2026-10-10, test local sur MacBook Air M5)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR vision-langage en une passe avec grounding]] — la notion : une génération donne texte, étiquette et boîte
- [[Évaluer un OCR]] — la notion : CER, F1 de boîtes, graphique, banc à vérité terrain
- [[Cascade OCR et contrôle arithmétique des factures]] — la notion : le gros modèle d'une cascade, et le contrôle des totaux
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : quand un pipeline, quand un modèle vision-langage
- [[Plafond de débit d'un GPU (roofline)]] — la notion : pourquoi 52 s contre 10 s suit le rapport des poids
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
