---
role: comparatif
nom: Comparatif - Parsing de documents
categorie: data/parsing
tags: [document-parsing, pdf, ocr, rag, layout-analysis]
---

# Comparatif - Parsing de documents

> On tranche sur : l'étage de la chaîne — trier, extraire du texte, lire une image, comprendre une mise en page — puis où le calcul se fait et sous quelle licence.

![[Comparatif - Parsing de documents.base]]

## Ce qui départage

- [[pdf-inspector]] — l'étage de **tri**, en amont de tout le reste : classe un PDF en `TextBased`, `Scanned`, `ImageBased` ou `Mixed` en 10 à 50 ms et rend un routage OCR **page par page**, l'OCR lui-même étant opt-in au build. Les tables sont extraites par heuristique, l'API bouge encore, et ses benchmarks sont auto-déclarés.
- [[PyMuPDF]] — la **référence de vitesse** de l'écosystème Python, et le seul à donner un accès bas niveau au **modèle objet PDF** (blocs, spans, coordonnées) en plus de la manipulation : découpe, fusion, caviardage, rendu image, formulaires. **AGPL-3.0** ou licence commerciale Artifex — piège juridique en SaaS ou produit fermé.
- [[pdfplumber]] — l'inverse : pur Python sous **MIT**, chaque objet de la page avec sa géométrie, une extraction de **tableaux** à stratégies configurables (`lines` vs `text`) et un **débogage visuel** de la page. Pas d'OCR, donc inopérant sur du scanné, et nettement plus lent que PyMuPDF sur du volume.
- [[docTR]] — l'**OCR** clé en main en deux étages, détection (DBNet, LinkNet) puis reconnaissance (CRNN, SAR, ViTSTR), avec modèles pré-entraînés et choix explicite du backend PyTorch ou TensorFlow. L'**ordre de lecture** en mise en page complexe n'est pas garanti, et l'extraction métier (champs, tableaux structurés) reste hors périmètre.
- [[Docling]] — la conversion **multi-format** (PDF, DOCX, PPTX, XLSX, HTML, images) vers un `DoclingDocument` unifié, avec compréhension de layout et de tableaux par des modèles maison **exécutables sur CPU en local** — MIT, hébergé par la LF AI & Data. Premier run = téléchargement des modèles, et le gros PDF reste coûteux sans GPU.
- [[Unstructured]] — l'angle **ETL** : `partition` couvre plus de 60 formats et rend des **éléments typés** (`Title`, `Table`, `NarrativeText`) porteurs de métadonnées, avec chunking et connecteurs d'ingestion vers les bases vectorielles. Binaires système (Tesseract, Poppler, ONNX) qui alourdissent l'image Docker, mode `hi_res` lent, et tableaux en retrait des outils spécialisés.
- [[Marker]] — un pipeline **vision** multi-étapes sur la famille de modèles OCR **Surya**, optimisé pour le **débit** sur GPU. Sa vraie frontière est la **double licence** : code en GPL-3.0, mais **poids** en OpenRAIL-M modifiée, gratuits seulement en dessous de 2 M$ de revenus ou financement. Sans GPU, le débit s'effondre.
- [[LlamaParse]] — le seul **managé** et non open-source : des tiers Fast à Agentic Plus, une facturation à crédits, et aucune infra GPU ni modèle à opérer. Les documents **transitent par le cloud**, ce qui l'exclut sous contrainte de souveraineté, et le coût grimpe vite en mode agentique.
- [[OpenDataLoader PDF]] — le seul **déterministe** par défaut : analyse de layout algorithmique (XY-Cut++) sans GPU, donc sortie reproductible à PDF constant, bounding boxes pour citer la source exacte, et le premier open-source à produire un **Tagged PDF** de bout en bout. Le mode local est bien plus faible sur les tableaux — 0,489 contre 0,928 en hybride, chiffres du projet — et chaque appel démarre un processus JVM.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
