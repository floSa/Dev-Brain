---
role: brique
nom: MinerU
alias: [mineru, opendatalab MinerU, MinerU2.5, mineru-kit]
pitch: "Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x."
categorie: data/parsing
famille: cli
licence_type: source-available
maturite: production
langage: Python
alternatives: ["[[olmOCR]]", "[[Marker]]", "[[Docling]]", "[[PaddleOCR]]"]
complements: ["[[RAGFlow]]"]
tags: [document-parsing, pdf, ocr, markdown-conversion, layout-analysis, table-extraction, vision-language, rag]
url_docs: https://opendatalab.github.io/MinerU/
url_repo: https://github.com/opendatalab/MinerU
---

# MinerU

<!-- AUTO:BANDEAU:START -->
> Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | source-available | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Extracteur de documents d'**OpenDataLab** (Shanghai AI Lab) qui rend du **Markdown, du HTML, du
LaTeX, du DOCX ou un contenu structuré** à partir de PDF — scannés compris —, d'images et de
formats Office. Depuis la version 4.0, il se règle par **quatre niveaux de qualité** : *Flash*
(extraction native et OCR rapide, sans modèle), *Basic* (petits modèles ONNX ou Torch, CPU
possible), *Standard* (par défaut, petits modèles plus un modèle vision-langage) et *Advanced*.
Le modèle vision-langage est **MinerU2.5-Pro**, de 1,2 milliard de paramètres, qui repère la
mise en page sur une image réduite puis reconnaît le contenu sur des recadrages en haute
résolution. Le traitement est **local par défaut** ; le service distant demande un `--remote`
explicite. La frontière de l'outil est double : une **licence propre**, ni Apache ni AGPL
selon la version, et une API qui a changé de forme à chaque version majeure.

*Constat du 2026-09-30 :* dernière version 4.0.10, publiée le 2026-09-29, après neuf releases
4.0.x en treize jours ; environ 80,9 k étoiles GitHub. La 4.0 (2026-09-16) casse la CLI, la
configuration (`mineru.json` remplacé par `config.yaml`), l'API et les extras de la 3.x.

## Licence — à lire avant d'adopter

Le texte actuel est la **MinerU Open Source License** : Apache 2.0 **plus trois conditions**.
Ce n'est pas un identifiant SPDX standard et elle n'est pas approuvée par l'OSI, d'où
`source-available` dans cette fiche.

- Licence commerciale distincte **obligatoire** si l'entreprise, affiliés compris, dépasse **100 millions d'utilisateurs actifs par mois** ou **20 M USD de revenu mensuel**.
- Mention **obligatoire** de MinerU, bien visible, pour tout **service en ligne** fourni à des tiers qui s'appuie dessus — y compris pour une ESN qui l'expose à ses clients.
- Non-respect de l'une ou l'autre : la licence **prend fin automatiquement**, sans préavis.
- **Historique** : AGPL-3.0 sur toutes les versions jusqu'à 3.0.6 incluse (2026-04-01), puis la licence actuelle à partir de la 3.1.0 (2026-04-17), après des allers-retours entre Apache 2.0 et AGPL en mars et avril. Épingler `mineru>=3.1`, et plutôt `>=4.0,<5`.
- **Poids** : les modèles MinerU2.5-Pro et ceux de la 4.0 sont étiquetés Apache-2.0 sur Hugging Face, l'ancien MinerU2.5-2509 reste en AGPL-3.0.

Pour un usage interne sur site, les seuils ne visent pas une entreprise ordinaire. Reste une
licence non standard, qu'un service juridique doit lire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Documents à mise en page lourde — formules, tableaux, multi-colonnes — à convertir en Markdown ou LaTeX, en local | Licence non OSI avec résiliation automatique, et AGPL sur les versions ≤ 3.0.6 : à faire valider avant tout produit ou service offert à des tiers |
| Moduler coût et qualité : CPU en Flash ou Basic, GPU ou mémoire unifiée en Standard et Advanced | Standard et Advanced demandent 16 Go de RAM et environ 8 Go de VRAM NVIDIA, ou 16 Go de mémoire unifiée sur Apple Silicon |
| Une seule entrée pour PDF, images, Word, PowerPoint, Excel, EPUB, HTML — les formats Office n'utilisent que le niveau Flash | API instable : trois versions majeures en quinze mois, 4.0 incompatible avec 3.x, Docker pour appareils non NVIDIA « en attente de mise à jour » |
| Citations stables au niveau du bloc pour relier une réponse à sa source | Modèle vision-langage : peut halluciner, comme tout VLM ; la fusion de tableaux sur plusieurs pages n'est pas disponible dans la version du modèle lue |
| Score annoncé de 95,69 sur OmniDocBench v1.6, un banc révisé par la même équipe : à recouper sur ses propres documents | Sur olmOCR-Bench, mesuré par Ai2, MinerU 2.5.4 fait 75,2 contre 82,4 pour [[olmOCR]] : le rang dépend de qui mesure → [[olmOCR]], [[Docling]] sous MIT |

## Mise en œuvre

- Installation — `uv pip install -U "mineru>=4.0,<5"` dans un environnement dédié (Python ≥ 3.10, < 3.15) ; `mineru[full]` pour le GPU NVIDIA ; Windows demande d'installer séparément le torch GPU
- Point d'entrée — commande `mineru-kit parse document.pdf -o document.md --tier standard` (sans état, toutes les pages) ; `mineru parse document.pdf --json` passe par la bibliothèque documentaire locale (10 premières pages par défaut) ; SDK Python, API V1 et interface web en complément
- Prérequis — ONNX en CPU et llama.cpp en Vulkan par défaut ; vLLM ou LMDeploy pour le débit sur GPU ; 16 Go de RAM pour Standard
- Exécution — local par défaut, mono-nœud ; routeur multi-services et Docker disponibles
- Coût — gratuit sous la MinerU Open Source License (Apache 2.0 plus conditions, cf. ci-dessus) ; aucun paiement tant que les seuils ne sont pas atteints

## Écosystème

### Alternatives

- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.

### Compléments

- [[RAGFlow]] — Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.

## Ressources

- Documentation — https://opendatalab.github.io/MinerU/
- Documentation — https://opendatalab.github.io/MinerU/reference/migration_4/
- Dépôt — https://github.com/opendatalab/MinerU
- Papier — https://arxiv.org/abs/2509.22186 (MinerU2.5, modèle découplé de parsing haute résolution, OpenDataLab, 2025)

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[OCR]] — la notion : deux étages, CTC contre attention, CER/WER, panorama des moteurs
- [[OCR classique vs modèles vision-langage pour documents]] — la notion : quand un pipeline en étages, quand un modèle vision-langage, et comment chacun échoue
- [[Vision Language Models]] — la famille de modèles dont son niveau Standard dérive
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
