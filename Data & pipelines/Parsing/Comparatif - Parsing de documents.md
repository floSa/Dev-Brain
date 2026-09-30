---
role: comparatif
nom: Comparatif - Parsing de documents
categorie: data/parsing
tags: [document-parsing, pdf, ocr, rag, layout-analysis]
---

# Comparatif - Parsing de documents

> On tranche sur : l'étage de la chaîne — trier, extraire du texte, lire une image, comprendre une mise en page —, puis où le calcul se fait (CPU ou GPU), sous quelle licence, et si un modèle vision-langage lit la page entière ou non.

![[Comparatif - Parsing de documents.base]]

## Ce qui départage

- [[pdf-inspector]] — l'étage de **tri**, en amont de tout le reste : classe un PDF en `TextBased`, `Scanned`, `ImageBased` ou `Mixed` en 10 à 50 ms et rend un routage OCR **page par page**, l'OCR lui-même étant opt-in au build. Les tables sont extraites par heuristique, l'API bouge encore, et ses benchmarks sont auto-déclarés.
- [[PyMuPDF]] — la **référence de vitesse** de l'écosystème Python, et le seul à donner un accès bas niveau au **modèle objet PDF** (blocs, spans, coordonnées) en plus de la manipulation : découpe, fusion, caviardage, rendu image, formulaires. **AGPL-3.0** ou licence commerciale Artifex — piège juridique en SaaS ou produit fermé.
- [[pypdf]] — le **couteau suisse** pur Python : fusion, découpe, chiffrement, formulaires, annotations, avec une extraction de texte en `plain` ou `layout`, sans dépendance et sous **BSD-3**. Son extraction est la plus lente des moteurs simples dans le banc de ses propres mainteneurs (3,5 s contre 0,1 s), le mode `layout` est expérimental, et il ne fait ni OCR ni rendu d'image.
- [[pypdfium2]] — le **moteur de Chromium** en Python : rendu de pages en image et extraction de texte aussi rapides que [[PyMuPDF]] (97 % de qualité dans le même banc), en roues précompilées, sous **Apache 2.0 ou BSD-3**. PDFium n'est pas thread-safe, l'accès à la structure PDF brute manque, et il n'analyse ni mise en page ni tableaux.
- [[pdfminer.six]] — l'**analyse de mise en page** de référence en pur Python, sous **MIT** : caractères, mots, lignes et boîtes, avec positions, selon les paramètres de `LAParams`. C'est la couche de [[pdfplumber]]. Lent (5,8 s dans le même banc), sans OCR, et aucune release depuis janvier 2026.
- [[pdfplumber]] — l'inverse : pur Python sous **MIT**, chaque objet de la page avec sa géométrie, une extraction de **tableaux** à stratégies configurables (`lines` vs `text`) et un **débogage visuel** de la page. Pas d'OCR, donc inopérant sur du scanné, et nettement plus lent que PyMuPDF sur du volume.
- [[docTR]] — l'**OCR** clé en main en deux étages, détection (DBNet, LinkNet) puis reconnaissance (CRNN, SAR, ViTSTR), avec modèles pré-entraînés et choix explicite du backend PyTorch ou TensorFlow. L'**ordre de lecture** en mise en page complexe n'est pas garanti, et l'extraction métier (champs, tableaux structurés) reste hors périmètre.
- [[Tesseract]] — l'**OCR minimal** : moteur C++ en ligne de commande, **CPU seul** et sans framework de deep learning, qui sort du texte, du hOCR, du TSV ou un **PDF cherchable**, sous Apache 2.0. Il lit des lignes de texte imprimé et rien d'autre : la doc elle-même exige 300 dpi, binarisation et redressement, et les tableaux, l'ordre de lecture et le manuscrit sont hors de portée.
- [[PaddleOCR]] — l'**OCR et le parsing de production** de Baidu : pipeline détection-reconnaissance multilingue (PP-OCRv6), **PP-StructureV3** pour tableaux, formules et mise en page, et un modèle vision-langage compact (PaddleOCR-VL), sous **Apache 2.0**, CPU ou GPU. Il faut installer PaddlePaddle ou Transformers, et les scores des modèles récents sont publiés par l'équipe elle-même.
- [[EasyOCR]] — l'**OCR en trois lignes de Python** : CRAFT puis CRNN sur plus de 80 langues, texte et boîtes, PyTorch, Apache 2.0. Ni mise en page ni tableaux, et **aucune release depuis septembre 2024** : à réserver au prototype.
- [[olmOCR]] — le **modèle vision-langage de 7 milliards de paramètres** d'Ai2, qui lit la page entière et rend du Markdown : tableaux, équations, manuscrit, ordre de lecture. Code **et poids** en Apache 2.0, mais **GPU obligatoire** (12 Go de VRAM au moins), installation fragile et dépôt sans release depuis mars 2026. Les scores de son banc sont ceux d'Ai2, et un VLM peut réécrire ce qu'il lit.
- [[MinerU]] — le **pipeline à quatre niveaux** d'OpenDataLab : du traitement natif sur CPU (Flash, Basic) jusqu'au modèle vision-langage MinerU2.5-Pro (Standard, Advanced), avec sorties Markdown, HTML et LaTeX. Sa frontière est la **licence** : Apache 2.0 plus conditions — seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel, mention obligatoire pour un service en ligne, AGPL jusqu'à la 3.0.6 —, et une 4.0 qui casse la 3.x.
- [[Docling]] — la conversion **multi-format** (PDF, DOCX, PPTX, XLSX, HTML, images) vers un `DoclingDocument` unifié, avec compréhension de layout et de tableaux par des modèles maison **exécutables sur CPU en local** — MIT, hébergé par la LF AI & Data. Premier run = téléchargement des modèles, et le gros PDF reste coûteux sans GPU.
- [[Unstructured]] — l'angle **ETL** : `partition` couvre plus de 60 formats et rend des **éléments typés** (`Title`, `Table`, `NarrativeText`) porteurs de métadonnées, avec chunking et connecteurs d'ingestion vers les bases vectorielles. Binaires système (Tesseract, Poppler, ONNX) qui alourdissent l'image Docker, mode `hi_res` lent, et tableaux en retrait des outils spécialisés.
- [[Marker]] — un pipeline **vision** multi-étapes sur la famille de modèles OCR **Surya**, optimisé pour le **débit** sur GPU. Sa vraie frontière est la **double licence** : code en GPL-3.0, mais **poids** en OpenRAIL-M modifiée, gratuits seulement en dessous de 2 M$ de revenus ou financement. Sans GPU, le débit s'effondre.
- [[LlamaParse]] — le seul **managé** et non open-source : des tiers Fast à Agentic Plus, une facturation à crédits, et aucune infra GPU ni modèle à opérer. Les documents **transitent par le cloud**, ce qui l'exclut sous contrainte de souveraineté, et le coût grimpe vite en mode agentique.
- [[OpenDataLoader PDF]] — le seul **déterministe** par défaut : analyse de layout algorithmique (XY-Cut++) sans GPU, donc sortie reproductible à PDF constant, bounding boxes pour citer la source exacte, et le premier open-source à produire un **Tagged PDF** de bout en bout. Le mode local est bien plus faible sur les tableaux — 0,489 contre 0,928 en hybride, chiffres du projet — et chaque appel démarre un processus JVM.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
