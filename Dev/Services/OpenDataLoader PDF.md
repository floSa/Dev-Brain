---
galaxie: dev
type: service
nom: OpenDataLoader PDF
alias: [opendataloader, opendataloader-pdf, open data loader pdf]
pitch: "Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA."
categorie: data/parsing
famille: paquet
licence_type: open-core
hosted: self
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Dev/Services/Docling|Docling]]", "[[Dev/Services/Unstructured|Unstructured]]", "[[Dev/Services/Marker|Marker]]", "[[Dev/Services/pdf-inspector|pdf-inspector]]"]
remplace_par: []
status: actif
tags: [pdf, document-parsing, layout-analysis, table-extraction, markdown-conversion, rag, accessibility]
url_docs: https://opendataloader.org/docs
url_repo: https://github.com/opendataloader-project/opendataloader-pdf
---

# OpenDataLoader PDF

## Pourquoi

Parseur PDF dont le mode par défaut est **déterministe et sans GPU** : analyse de mise en page algorithmique, ordre de lecture par XY-Cut++ pour les pages multi-colonnes, détection de la hiérarchie de titres, des listes et des tableaux à bordures, filtrage des en-têtes, pieds de page et filigranes. Chaque élément sort avec ses **bounding boxes**, ce qui permet de citer la source exacte d'un passage en aval d'un RAG. Sorties JSON, Markdown, HTML, texte brut et PDF annoté.

Deux propriétés le distinguent du reste de la famille. D'abord le **déterminisme** : à PDF constant, la sortie est reproductible — utile pour tester un pipeline, diffuser une régression ou signer un traitement. Ensuite l'**accessibilité** : c'est le premier outil open-source à générer un Tagged PDF de bout en bout depuis un PDF non balisé, en suivant la spécification Well-Tagged PDF de la PDF Association et en validant avec veraPDF.

Un **mode hybride** optionnel complète le tableau : les pages simples restent traitées en local, les pages complexes (tableaux sans bordures, scans, formules, graphiques) sont routées vers un backend IA — [[Dev/Services/Docling|Docling]] en pratique — qui apporte l'OCR (plus de 80 langues), l'extraction de formules LaTeX et la description d'images. Le mode hybride abandonne le déterminisme : c'est un choix explicite, pas le défaut.

Frontière avec `tooling/document` : ici la cible est une **machine**, pas un lecteur humain. Pour fusionner, signer ou compresser un PDF destiné à être lu, voir [[Dev/Services/Stirling PDF|Stirling PDF]].

## Quand l'utiliser

- Alimenter un index RAG avec des citations traçables : les bounding boxes permettent de renvoyer à la page et à la zone d'origine.
- Traiter un gros corpus sur CPU seul, en on-prem, sans GPU ni appel à une API externe.
- Exiger une sortie reproductible : audit, tests de non-régression sur un pipeline documentaire, traçabilité réglementaire.
- Remédier en masse à l'accessibilité d'un stock de PDF non balisés (EAA, ADA, Section 508) : l'auto-tagging est dans le périmètre Apache 2.0.
- Exploiter les balises d'un PDF déjà Tagged plutôt que de re-deviner sa structure.

## Quand NE PAS l'utiliser

- Traiter des formats non-PDF (DOCX, PPTX, XLSX, HTML, e-mails) : hors périmètre → [[Dev/Services/Docling|Docling]], [[Dev/Services/Unstructured|Unstructured]].
- Pipeline Python pur sans dépendance JVM : le cœur est en Java et chaque appel lance un processus JVM → [[Dev/Services/Marker|Marker]], [[Dev/Services/Docling|Docling]].
- Simplement savoir si un PDF a besoin d'OCR avant de le router : c'est plus léger avec [[Dev/Services/pdf-inspector|pdf-inspector]].
- Comprendre des mises en page très libres avec un modèle vision de bout en bout → [[Dev/Services/Marker|Marker]].
- Export PDF/UA-1 ou PDF/UA-2 : c'est un module payant, l'open-source s'arrête au Tagged PDF.

## Déploiement & coût

- `pip install -U opendataloader-pdf`, `npm install @opendataloader/pdf`, ou dépendance Maven `org.opendataloader:opendataloader-pdf-core`. **Java 11 ou plus requis dans tous les cas**, y compris depuis Python.
- CLI `opendataloader-pdf` pour le traitement par lots de fichiers et de dossiers. Mode hybride via `pip install "opendataloader-pdf[hybrid]"` et un serveur local `opendataloader-pdf-hybrid`.
- Chargeur officiel LangChain : paquet `langchain-opendataloader-pdf`.
- Cœur Apache 2.0, gratuit, mono-nœud, sans service à héberger. Export PDF/UA et éditeur d'accessibilité en add-on commercial. Les versions antérieures à la 2.0 étaient sous MPL 2.0 — vérifier la licence de la version épinglée.

## Pièges

- **Benchmarks auto-déclarés** : sur son propre corpus `opendataloader-bench` (200 PDF), le projet annonce le mode hybride premier au classement global à 0,907 (ordre de lecture 0,934, tableaux 0,928, titres 0,821) devant nutrient, docling et marker. Chiffres du projet, non reproduits ici — et [[Dev/Services/pdf-inspector|pdf-inspector]] revendique 0,875 sur le même corpus, ce qui invite à la prudence sur les classements croisés.
- **Le mode local est bien moins bon sur les tableaux** que le mode hybride : 0,489 contre 0,928 dans le tableau du projet. Le déterminisme se paie sur les tableaux complexes.
- Un appel `convert()` démarre un processus JVM : batcher tous les fichiers en un seul appel, ne jamais boucler fichier par fichier.
- Le mode hybride réintroduit une dépendance à un modèle et un serveur annexe ; il n'est ni déterministe ni sans GPU selon le backend retenu.
- Le filtrage anti-injection de prompt annoncé sur le contenu extrait est une réduction de risque, pas une garantie : maintenir les contrôles côté application.

## Alternatives

- [[Dev/Services/Docling|Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Dev/Services/Unstructured|Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Dev/Services/Marker|Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[Dev/Services/pdf-inspector|pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- [[Dev/Services/Stirling PDF|Stirling PDF]] — l'autre face du PDF : manipulation de documents pour un lecteur humain, catégorie `tooling/document`.
- Étage bas niveau complémentaire : [[Dev/Services/PyMuPDF|PyMuPDF]] / [[Dev/Services/pdfplumber|pdfplumber]] pour l'extraction brute.
- [[OCR]] — concept : reconnaissance optique de caractères, disponible en mode hybride seulement.
- [[Chunking strategies]] — concept : découpage de documents en aval.
- [[RAG]] — concept : génération augmentée par récupération.
- Docs : https://opendataloader.org/docs · Repo : https://github.com/opendataloader-project/opendataloader-pdf
