---
role: brique
nom: olmOCR
alias: [olmocr, olmOCR 2, Ai2 olmOCR, allenai olmocr]
pitch: "Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire."
categorie: data/parsing
famille: cli
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[MinerU]]", "[[Marker]]", "[[Docling]]", "[[PaddleOCR]]"]
complements: []
tags: [ocr, document-parsing, pdf, markdown-conversion, vision-language, gpu, self-hosted]
url_docs: https://github.com/allenai/olmocr
url_repo: https://github.com/allenai/olmocr
---

# olmOCR

<!-- AUTO:BANDEAU:START -->
> Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Toolkit de l'institut **Ai2** pour transformer de gros volumes de PDF en texte linéarisé. Le
cœur est un **modèle vision-langage de 7 milliards de paramètres**, olmOCR-2-7B, affiné à
partir de Qwen2.5-VL-7B-Instruct : il reçoit l'image d'une page et rend du **Markdown** avec
tableaux, équations, écriture manuscrite et ordre de lecture naturel, en ignorant en-têtes et
pieds de page. La version 2 a été entraînée par apprentissage par renforcement (GRPO) sur des
**tests unitaires binaires** appliqués à des documents synthétiques dont le HTML source est
connu. La v1 injectait dans le prompt le texte natif du PDF (« document anchoring ») ; d'après
le code du pipeline, olmOCR-2 n'en fait plus usage, ce texte ne servant que de repli quand une
page échoue. Le pipeline tourne en lot sur **GPU** via vLLM, en local, sur un serveur distant ou
en multi-nœud. C'est un VLM : il lit la page en entier, et peut donc **réécrire ou halluciner**
là où un OCR classique se trompe en bruit local.

*Constat du 2026-09-30 :* dernière release v0.4.27, publiée le 2026-03-12, dernier commit le
2026-03-25 ; olmOCR-2-7B-1025 date du 2025-10-21 ; environ 19,7 k étoiles GitHub. Aucune
release depuis six mois.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Convertir un gros corpus de PDF, scannés ou natifs, en Markdown propre, sur ses propres GPU | Pas de GPU NVIDIA récent d'au moins 12 Go de VRAM : le README est explicite, le CPU n'est pas prévu → [[Docling]] ou [[Tesseract]] |
| Code **et poids** en Apache 2.0, déploiement on-prem sans dépendance à une API | Lecture littérale exigée — archives, juridique : un VLM peut réécrire ou halluciner, et ses erreurs restent fluides ; les notes de la v0.3.0 citent déjà des hallucinations sur pages blanches, corrigées → [[Tesseract]] ou [[PaddleOCR]] |
| Coût au volume maîtrisé : moins de 200 $ par million de pages annoncés par Ai2, ou API tierces vérifiées par Ai2 | Installation fragile : environnement conda propre, `poppler-utils`, polices Microsoft, PyTorch CUDA ; le README déconseille l'ajout dans un environnement existant |
| Tableaux, équations et manuscrit traités par un seul modèle | Dépôt peu actif depuis mars 2026, version 0.x, moteur passé de SGLang à vLLM : l'API a bougé en un an |
| | Vieux scans : le sous-score « Old scans » de son propre benchmark est le plus faible, à 47,7 |

## Mise en œuvre

- Installation — paquets système (`poppler-utils`, polices Microsoft), environnement Python 3.11 propre, puis `pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128` ; `pip install olmocr` seul suffit pour viser un serveur distant
- Point d'entrée — commande `olmocr ./localworkspace --markdown --pdfs fichier.pdf` (équivalent : `python -m olmocr.pipeline`) ; entrées PDF, PNG, JPEG ; sorties Markdown et Dolma JSONL
- Prérequis — GPU NVIDIA de 12 Go de VRAM ou plus (testé sur RTX 4090, L40S, A100, H100), 30 Go de disque ; le modèle attend des images dont le grand côté fait 1288 px
- Exécution — inférence locale via vLLM, serveur vLLM distant compatible OpenAI, multi-nœud avec file de travail sur S3, image Docker
- Coût — gratuit, code Apache-2.0, poids olmOCR-2 Apache-2.0 (carte du modèle : destiné à la recherche et à l'éducation, selon les règles d'usage responsable d'Ai2) ; données d'entraînement et banc d'essai en ODC-BY ; chiffres de coût auto-déclarés par Ai2

## Écosystème

### Alternatives

- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.

## Ressources

- Documentation — https://github.com/allenai/olmocr
- Dépôt — https://github.com/allenai/olmocr
- Papier — https://arxiv.org/abs/2502.18443 (olmOCR, Poznanski et al., Ai2, 2025)
- Papier — https://arxiv.org/abs/2510.19817 (olmOCR 2 : récompenses par tests unitaires, Poznanski, Soldaini, Lo, 2025)
- Documentation — https://huggingface.co/allenai/olmOCR-2-7B-1025-FP8

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : quand un pipeline en étages, quand un modèle vision-langage, et comment chacun échoue
- [[Vision Language Models]] — la famille de modèles dont il est un dérivé spécialisé
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
