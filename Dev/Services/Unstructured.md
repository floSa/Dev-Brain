---
role: brique
nom: Unstructured
alias: [unstructured, unstructured-io]
pitch: "Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG."
categorie: data/parsing
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Docling]]", "[[LlamaParse]]", "[[Marker]]", "[[OpenDataLoader PDF]]"]
complements: []
tags: [document-parsing, rag, ocr]
url_docs: https://docs.unstructured.io/
url_repo: https://github.com/Unstructured-IO/unstructured
---

# Unstructured

## Pourquoi

Unstructured est une boîte à outils **ETL open-source (Apache-2.0)** pour transformer des documents hétérogènes en données exploitables par un LLM. Sa fonction cœur, `partition`, détecte la nature d'un fichier (plus de 60 formats : PDF, DOCX, PPTX, HTML, e-mails, images…) et le découpe en **éléments typés** (`Title`, `NarrativeText`, `Table`, `ListItem`, `Image`…) porteurs de métadonnées (page, coordonnées, hiérarchie). S'y ajoutent nettoyage, **chunking** et un catalogue de **connecteurs** d'ingestion (S3, SharePoint, Notion…) vers les bases vectorielles. Le tout vise le pré-traitement RAG. Une **Platform** managée (payante) industrialise les mêmes étapes.

## Quand l'utiliser

- Ingestion RAG sur un parc documentaire **hétérogène** (PDF, Office, mails, HTML) via une seule API.
- Besoin d'éléments **typés + métadonnées** pour un chunking sémantique propre.
- Pipeline d'ingestion avec connecteurs vers sources et bases vectorielles clés en main.
- Prototyper en open-source, puis basculer sur la Platform managée sans tout réécrire.

## Quand NE PAS l'utiliser

- Un seul PDF et juste le texte brut, le plus vite possible → [[PyMuPDF]] / [[pdfplumber]].
- Conversion fidèle d'un PDF complexe en Markdown (mise en page, formules) → [[Marker]] / [[Docling]].
- Refus de gérer l'infra (modèles, OCR, binaires) → service managé [[LlamaParse]].

## Déploiement & coût

- Bibliothèque Python (`pip install "unstructured[pdf]"` ; extras par format). Apache-2.0, gratuite.
- Le parsing avancé tire des **dépendances lourdes** : Tesseract (OCR), Poppler, modèles de détection de layout via `unstructured-inference`.
- Managé : **Unstructured Platform / API** (facturée), workflows d'ingestion clés en main.
- Single-node ; la montée en charge passe par la Platform ou un orchestrateur externe.

## Pièges

- Extras et binaires système (Tesseract, Poppler, ONNX) **alourdissent l'image Docker**.
- Le mode `hi_res` (layout par modèle) est lent et gourmand ; `fast` perd en qualité sur les PDF complexes.
- Extraction des tableaux en retrait des outils spécialisés sur documents très structurés.

## Alternatives

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Étage bas niveau complémentaire : [[PyMuPDF]] / [[pdfplumber]] pour l'extraction brute.
- Doc : https://docs.unstructured.io/
