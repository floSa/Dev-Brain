---
role: brique
nom: OpenDataLoader PDF
alias: [opendataloader, opendataloader-pdf, open data loader pdf]
pitch: "Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA."
categorie: data/parsing
famille: paquet
licence_type: open-core
maturite: production
langage: Java
alternatives: ["[[Docling]]", "[[Unstructured]]", "[[Marker]]", "[[pdf-inspector]]"]
complements: ["[[PyMuPDF]]", "[[pdfplumber]]"]
tags: [pdf, document-parsing, layout-analysis, table-extraction, markdown-conversion, rag, accessibility]
url_docs: https://opendataloader.org/docs
url_repo: https://github.com/opendataloader-project/opendataloader-pdf
---

# OpenDataLoader PDF

<!-- AUTO:BANDEAU:START -->
> Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Java | open-core | en bibliothèque, rien à héberger | production | à jour · 2026-09-01 |
<!-- AUTO:BANDEAU:END -->

## Définition

Parseur PDF dont le mode par défaut est **déterministe et sans GPU** : analyse de mise en page
algorithmique, ordre de lecture par **XY-Cut++** pour les pages multi-colonnes, détection de
la hiérarchie de titres, des listes et des tableaux à bordures, filtrage des en-têtes, pieds
de page et filigranes. Chaque élément sort avec ses **bounding boxes**, ce qui permet de citer
la source exacte d'un passage en aval d'un RAG ; les sorties sont JSON, Markdown, HTML, texte
brut et PDF annoté. Deux propriétés le distinguent du reste de la famille : le
**déterminisme** — à PDF constant, la sortie est reproductible — et l'**accessibilité**,
puisque c'est le premier outil open-source à générer un Tagged PDF de bout en bout depuis un
PDF non balisé, en suivant la spécification Well-Tagged PDF de la PDF Association et en
validant avec veraPDF. Un **mode hybride** optionnel garde les pages simples en local et route
les pages complexes — tableaux sans bordures, scans, formules, graphiques — vers un backend IA
(Docling en pratique), qui apporte l'OCR de plus de 80 langues, les formules LaTeX et la
description d'images : il abandonne le déterminisme, et c'est un choix explicite, pas le
défaut. Frontière avec `tooling/document` : la cible ici est une **machine**, pas un lecteur
humain ; fusionner, signer ou compresser un PDF destiné à être lu relève d'une autre
catégorie.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Alimenter un index RAG avec des citations traçables : les bounding boxes renvoient à la page et à la zone d'origine | Le mode local est bien plus faible sur les tableaux que le mode hybride — 0,489 contre 0,928 dans le tableau du projet : le déterminisme se paie là |
| Traiter un gros corpus sur CPU seul, en on-prem, sans GPU ni appel à une API externe | Benchmarks auto-déclarés sur le corpus maison `opendataloader-bench` (200 PDF), chiffres du projet non reproduits ici et difficiles à croiser avec ceux des concurrents mesurés sur le même corpus |
| Exiger une sortie reproductible : audit, tests de non-régression, traçabilité réglementaire | Un appel `convert()` démarre un processus JVM : batcher tous les fichiers en un seul appel, ne jamais boucler fichier par fichier |
| Remédier en masse à l'accessibilité d'un stock de PDF non balisés — EAA, ADA, Section 508 | Java 11 ou plus requis dans tous les cas, y compris depuis Python |
| Exploiter les balises d'un PDF déjà Tagged plutôt que de re-deviner sa structure | Le mode hybride réintroduit une dépendance à un modèle et à un serveur annexe : ni déterministe, ni sans GPU selon le backend |
| | Formats non-PDF — DOCX, PPTX, XLSX, HTML, e-mails — hors périmètre |
| | Export PDF/UA-1 ou PDF/UA-2 : module payant, l'open-source s'arrête au Tagged PDF |
| | Le filtrage anti-injection de prompt annoncé sur le contenu extrait est une réduction de risque, pas une garantie : maintenir les contrôles côté application |

## Mise en œuvre

- Installation — `pip install -U opendataloader-pdf`, `npm install @opendataloader/pdf`, ou dépendance Maven `org.opendataloader:opendataloader-pdf-core` ; mode hybride via l'extra `[hybrid]`
- Point d'entrée — appel `convert()`, CLI `opendataloader-pdf` pour le traitement par lots de fichiers et de dossiers, chargeur officiel `langchain-opendataloader-pdf`
- Prérequis — Java 11 ou plus dans tous les cas, y compris depuis Python ; le mode hybride ajoute un serveur local `opendataloader-pdf-hybrid`
- Exécution — en process JVM, mono-nœud, sans service à héberger
- Coût — cœur Apache 2.0 gratuit ; export PDF/UA et éditeur d'accessibilité en add-on commercial ; les versions antérieures à la 2.0 étaient sous MPL 2.0, vérifier la licence de la version épinglée

## Écosystème

### Alternatives

- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — l'étage bas niveau, pour l'extraction brute en amont.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT. — l'étage bas niveau, pour l'extraction brute en amont.

## Ressources

- Documentation — https://opendataloader.org/docs
- Dépôt — https://github.com/opendataloader-project/opendataloader-pdf

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Stirling PDF]] — l'autre face du PDF : manipulation pour un lecteur humain, catégorie `tooling/document`
- [[OCR]] — la notion : reconnaissance optique de caractères, disponible en mode hybride seulement
- [[Chunking strategies]] — la notion : découpage de documents en aval
- [[RAG]] — la notion : génération augmentée par récupération
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
