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
complements: ["[[PyMuPDF]]", "[[pdfplumber]]"]
tags: [document-parsing, rag, ocr]
url_docs: https://docs.unstructured.io/
url_repo: https://github.com/Unstructured-IO/unstructured
---

# Unstructured

<!-- AUTO:BANDEAU:START -->
> Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils **ETL pour documents**, qui vise le pré-traitement RAG. Sa fonction cœur,
`partition`, détecte la nature d'un fichier — plus de soixante formats : PDF, DOCX, PPTX,
HTML, e-mails, images — et le découpe en **éléments typés** (`Title`, `NarrativeText`,
`Table`, `ListItem`, `Image`) porteurs de métadonnées : page, coordonnées, hiérarchie. S'y
ajoutent le nettoyage, le **chunking** et un catalogue de **connecteurs** d'ingestion — S3,
SharePoint, Notion — vers les bases vectorielles. Une **Platform** managée industrialise les
mêmes étapes, ce qui permet de prototyper avec la bibliothèque puis de basculer sans tout réécrire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Ingestion RAG sur un parc documentaire hétérogène — PDF, Office, mails, HTML — via une seule API | Extras et binaires système (Tesseract, Poppler, ONNX) qui alourdissent l'image Docker |
| Éléments typés et métadonnées, pour un chunking sémantique propre | Le mode `hi_res` est lent et gourmand ; le mode `fast` perd en qualité sur les PDF complexes |
| Pipeline d'ingestion avec connecteurs vers sources et bases vectorielles clés en main | Extraction des tableaux en retrait des outils spécialisés sur documents très structurés |
| Prototyper en open-source, puis basculer sur la Platform managée sans tout réécrire | Mono-nœud : la montée en charge passe par la Platform ou par un orchestrateur externe |

## Mise en œuvre

- Installation — `pip install "unstructured[pdf]"`, avec un extra par famille de format
- Point d'entrée — `partition`, puis nettoyage, chunking et connecteurs d'ingestion
- Prérequis — Tesseract (OCR), Poppler et les modèles de layout via `unstructured-inference` pour le parsing avancé
- Exécution — en process, mono-nœud ; la Platform managée industrialise les workflows d'ingestion
- Coût — gratuit, Apache-2.0 ; l'Unstructured Platform / API est facturée

## Écosystème

### Alternatives

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — l'étage bas niveau, pour l'extraction brute en amont.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT. — l'étage bas niveau, pour l'extraction brute en amont.

## Ressources

- Documentation — https://docs.unstructured.io/
- Dépôt — https://github.com/Unstructured-IO/unstructured

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
