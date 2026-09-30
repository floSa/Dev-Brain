---
role: notion
nom: OCR classique vs modèles vision-langage pour documents
alias: [OCR vs VLM, OCR classique ou VLM, pipeline OCR vs VLM, OCR end-to-end, VLM pour l'OCR]
categorie: data/parsing
domaines: [data-eng, ai-eng]
tags: [ocr, document-parsing, vision-language, layout-analysis, benchmark]
---

# OCR classique vs modèles vision-langage pour documents

## Aperçu

- Deux façons de faire lire une page à une machine. Le **pipeline en étages** localise le texte, puis lit chaque région, et confie l'ordre de lecture et les tableaux à des modules à part. Le **modèle vision-langage** (VLM) reçoit l'image de la page et écrit le Markdown en un passage.
- Le choix ne se joue pas sur une précision moyenne, mais sur ce qu'on exige : **fidélité littérale**, tableaux et formules, volume, matériel, contrainte de souveraineté. Les sources lues en 2026 ne donnent pas de vainqueur général.

## Concepts clés

### Le pipeline en étages
- [[Tesseract]], [[docTR]], [[EasyOCR]] et la partie OCR de [[PaddleOCR]] suivent le schéma de [[OCR]] : **détection** du texte, puis **reconnaissance** de chaque crop. Mise en page, ordre de lecture et tableaux relèvent de modules séparés, comme dans [[Docling]] ou PP-StructureV3.
- Une erreur y est **locale** : un caractère faux, un mot coupé. Le reste de la page n'est pas touché.
- Le pré-traitement pèse lourd. La doc de Tesseract exige au moins 300 dpi et recommande binarisation, suppression du bruit et redressement ; une page penchée dégrade nettement la segmentation de lignes.

### Le VLM « page → Markdown »
- [[olmOCR]] en est l'exemple le plus net : un VLM de 7 milliards de paramètres qui rend du Markdown avec tableaux, équations et ordre de lecture. Sa version 2 est entraînée par apprentissage par renforcement, avec pour récompenses des **tests unitaires binaires** (Poznanski, Soldaini, Lo, 2025).
- Gain : tableaux, formules, colonnes multiples et manuscrit traités par un seul modèle. Coût : un **GPU**, et une sortie générée plutôt que lue.

### Les hybrides
- [[PaddleOCR]] (PaddleOCR-VL) et [[MinerU]] (niveaux Standard et Advanced) **découplent** : une détection de mise en page d'abord, puis un petit VLM sur chaque région, en résolution native pour MinerU. Le pari est de garder la mise en page hors du modèle génératif, pour limiter latence et hallucination ; la source qui le défend est celle de l'équipe qui a construit PaddleOCR-VL.
- [[pdf-inspector]] joue le rôle inverse, en amont : décider page par page si l'OCR est nécessaire.

### Comment chaque famille échoue
- **Pipeline** : bruit local, ordre de lecture et tableaux fragiles, scans dégradés, écritures hors des données d'entraînement.
- **VLM** : réécriture et hallucination, **fluides donc difficiles à repérer**. Lee et al. (2026) mesurent, sur 15 systèmes, une dégradation sous perturbation de la page qui va jusqu'à 6,9 points de WER pour les VLM généralistes, de 0,1 à 3,4 points pour les VLM spécialisés en OCR, et de moins de 0,8 point sur l'anglais pour l'OCR classique. Gardella et al. (2026) relèvent, sur des documents historiques, des normalisations d'orthographe, du texte ajouté sans région d'image correspondante et des substitutions sémantiques, **avec peu d'effet sur le CER**.
- **En production**, avec des VLM servis par API : boucles de répétition jusqu'à épuisement du budget de tokens et arrêts par les filtres de « récitation » des fournisseurs (He, LlamaIndex, 2026). Les parades sont des plafonds de tokens, un changement de température au retry et un modèle de repli.

## Les maths, simplement

- **CER** : $\mathrm{CER} = \dfrac{S + D + I}{N}$, substitutions, suppressions et insertions sur $N$ caractères de référence ; le **WER** est le même calcul sur les mots. Détail dans [[OCR]].
- **Distance d'édition normalisée** : $\dfrac{\mathrm{ED}(a, b)}{\max(|a|, |b|)}$, la mesure de texte d'OmniDocBench, à côté de CDM pour les formules.
- **TEDS**, pour les tableaux : $\mathrm{TEDS}(T_a, T_b) = 1 - \dfrac{\mathrm{EditDist}(T_a, T_b)}{\max(|T_a|, |T_b|)}$, une distance d'édition **entre arbres** HTML, qui capte les décalages de cellules que le CER ignore (Zhong et al., 2019).
- **Tests unitaires binaires** (olmOCR-Bench) : chaque test vérifie une propriété — un texte présent, un ordre de lecture, une cellule de tableau — et rend vrai ou faux ; aucune distance à une transcription unique.
- Quand l'analyse de page échoue, le CER n'est plus défini. Le **Character Error Vector** (Bourne et al., 2026) sépare l'erreur de découpage de page, l'erreur d'OCR et leur interaction.

## En pratique

- **Fidélité littérale exigée** — archives, juridique, pièces à citer : partir d'un OCR classique, ou mesurer un VLM sur ses propres pages avant de s'y fier. Sur des journaux d'archives dégradés, les pipelines classiques battent les modèles de bout en bout (Bourne et al., 2026).
- **Tableaux, formules, colonnes, manuscrit de page entière** : un VLM ou un hybride. Sur des manuscrits, les VLM font mieux que [[Tesseract]] à l'échelle de la page et à peu près autant à celle de la ligne (Farazi et al., 2026).
- **Pas de GPU** : [[Tesseract]], [[Docling]] ou les niveaux Flash et Basic de [[MinerU]] ; [[olmOCR]] est exclu.
- **Volume** : un VLM auto-hébergé se compte en GPU — Ai2 annonce moins de 200 $ par million de pages pour olmOCR, chiffre auto-déclaré. Un billet de blog propose Tesseract d'abord et un repli sur VLM sous 70 % de confiance ; ses coûts sont calculés par l'auteur, pas mesurés.
- **Toujours mesurer sur ses documents.** Le rang d'un outil dépend de qui tient le banc : sur olmOCR-Bench, publié par Ai2, olmOCR fait 82,4 et MinerU 2.5.4 fait 75,2 ; MinerU annonce de son côté 95,69 sur OmniDocBench v1.6, révisé par sa propre équipe.
- **Licences** : [[olmOCR]] et [[PaddleOCR]] sont en Apache 2.0, [[MinerU]] a une licence à conditions, [[Marker]] des poids restreints. Cela se règle avant le benchmark.

## Approches voisines & alternatives

- [[OCR]] — la notion de base : deux étages, CTC contre attention, CER et WER.
- [[Vision Language Models]] — la famille des modèles, sans le cadre documentaire.
- [[Parsing]] et [[Comparatif - Parsing de documents]] — les outils, et ce qui les départage.
- [[Marker]] — un pipeline vision multi-étapes entre les deux familles, à poids sous licence restreinte.
- Texte déjà natif dans le PDF : [[PyMuPDF]], [[pdfplumber]], [[pypdfium2]] — pas d'OCR du tout, ce qui est la première question à se poser.

## Pour aller plus loin

- Poznanski, Soldaini, Lo (2025) — *olmOCR 2: Unit Test Rewards for Document OCR* — https://arxiv.org/abs/2510.19817
- Ouyang et al. (CVPR 2025) — *OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations* — https://arxiv.org/abs/2412.07626
- Cui et al. (2025) — *PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model* — https://arxiv.org/abs/2510.14528
- Lee et al. (2026) — *Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models* — https://arxiv.org/abs/2607.21617
- Gardella et al. (2026) — *When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents* — https://arxiv.org/abs/2607.24077
- Bourne, Simbeye, Nockels (2026) — *The Character Error Vector: Decomposable errors for page-level OCR evaluation* — https://arxiv.org/abs/2604.06160
- Farazi et al. (2026) — *When Do VLMs Help Arabic Manuscript OCR? A Cross-Dataset Study* — https://arxiv.org/abs/2608.22366
- Zhong, ShafieiBavani, Jimeno Yepes (2019) — *Image-based table recognition: data, model, and evaluation* — https://arxiv.org/abs/1911.10683
- He (LlamaIndex, 2026-04-08) — *Engineering Insights: Failure Modes That Break VLM-Powered OCR in Production* — https://www.llamaindex.ai/blog/engineering-insights-failure-modes-that-break-vlm-powered-ocr-in-production
- Anhaia (2026-05-04) — *Vision Models for OCR: When They Beat Tesseract and When They Don't* — https://dev.to/gabrielanhaia/vision-models-for-ocr-when-they-beat-tesseract-and-when-they-dont-54a6

> Désaccord entre les sources, non tranché : Gardella et al. trouvent les VLM meilleurs que l'OCR classique en CER et en WER sur des images d'archives, quand Lee et al. et Bourne et al. trouvent l'OCR classique plus fidèle ou plus robuste, sur des pages synthétiques perturbées et des journaux dégradés. Les jeux de données diffèrent, aucune comparaison directe n'existe. Non trouvé : une mesure de la reproductibilité d'un même VLM d'une exécution à l'autre, et un comparatif de Tesseract et d'olmOCR sur le même banc.
