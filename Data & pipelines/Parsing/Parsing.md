---
role: hub
nom: Parsing
alias: [parsing de documents]
pitch: Extraire du contenu structuré depuis des documents — PDF, Office, scans — pour le rendre lisible par une machine.
domaines: [data-eng, ai-eng]
tags: [document-parsing, pdf, ocr, markdown-conversion]
---

# Parsing

> Extraire du contenu structuré depuis des documents — PDF, Office, scans — pour le rendre lisible par une machine.

## Ce qu'il faut comprendre

- Un PDF ne contient pas de texte structuré : il contient des instructions de dessin. Il n'y a ni paragraphe, ni tableau, ni ordre de lecture — tout cela est **reconstruit par inférence**, et c'est pourquoi deux outils donnent deux résultats sur le même fichier. C'est la difficulté centrale du domaine, pas un défaut d'implémentation.
- Le clivage qui décide de tout est **le PDF porte-t-il du texte natif ou une image**. Natif, l'extraction est déterministe et rapide ([[PyMuPDF]], [[pdfplumber]]). Scanné, il faut de l'[[OCR]] ([[docTR]]) et le résultat devient probabiliste. Un corpus réel est mixte, d'où l'intérêt de **classer avant de router** ([[pdf-inspector]]) : ne payer l'OCR que sur les pages qui en ont besoin.
- Les **tableaux** sont le point où les outils se séparent vraiment. Le texte, tout le monde le sort ; une structure de lignes et de colonnes fidèle, presque personne. C'est le critère à tester sur ses propres fichiers avant de choisir, et non à lire dans une documentation.
- Un second clivage traverse le domaine : **quelle sortie**. Un accès objet par objet, pour piloter l'extraction soi-même ([[pdfplumber]], [[PyMuPDF]]) ; ou du Markdown prêt à découper et embarquer pour un RAG ([[Marker]], [[Docling]], [[Unstructured]]). Cf. [[Chunking strategies]].
- La **licence** est ici un critère de premier rang, plus que dans le reste du brain : [[PyMuPDF]] est AGPL ou commerciale, [[Marker]] est GPL avec des poids à licence restreinte, [[LlamaParse]] n'est pas ouvert du tout. Sur un projet client, ce point se règle avant le benchmark.

## Choisir

- PDF à texte natif, priorité à la vitesse, accès bas niveau → [[PyMuPDF]] (attention à l'AGPL).
- Tableaux à extraire finement, avec débogage visuel, sous licence MIT → [[pdfplumber]].
- Manipuler des PDF (fusion, découpe, formulaires, chiffrement) en pur Python, sans dépendance, sous BSD-3 → [[pypdf]].
- Rendre des pages PDF en image ou extraire du texte très vite, sous licence permissive → [[pypdfium2]].
- Accéder à la mise en page brute d'un PDF natif — boîtes, lignes, polices — en pur Python sous MIT → [[pdfminer.six]].
- Trier un corpus mixte et ne router vers l'OCR que le nécessaire → [[pdf-inspector]].
- Scans et images, pipeline OCR clé en main → [[docTR]].
- OCR imprimé sur CPU seul, sans framework de deep learning, ou PDF cherchable à produire → [[Tesseract]].
- OCR multilingue et mise en page, tableaux ou formules dans le même outil, Apache 2.0 → [[PaddleOCR]].
- Prototype OCR Python multilingue en quelques lignes, sans exigence de maintenance → [[EasyOCR]].
- Gros corpus de PDF en Markdown par un modèle vision-langage, GPU disponible, code et poids Apache 2.0 → [[olmOCR]].
- Mise en page lourde, formules et tableaux, qualité réglable du CPU au GPU, licence non standard à faire valider → [[MinerU]].
- Documents variés (PDF, Office, HTML, e-mails) à partitionner pour un RAG → [[Unstructured]].
- Mise en page et tableaux complexes, exécution locale, Apache/MIT → [[Docling]].
- Markdown de haute qualité, GPU disponible, licence GPL acceptée → [[Marker]].
- Sortie déterministe à bounding boxes, ou PDF à baliser pour l'accessibilité, sous Apache 2.0 → [[OpenDataLoader PDF]].
- Rien à héberger, PDF complexes, budget par crédits → [[LlamaParse]].

<!-- AUTO:START -->
### Briques
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[docTR]] — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- [[EasyOCR]] — Bibliothèque OCR Python de Jaided AI, sous Apache 2.0 : détection CRAFT puis reconnaissance CRNN sur plus de 80 langues, en quelques lignes et sur PyTorch ; texte et boîtes seulement, sans mise en page ni tableaux, dernière release en septembre 2024.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[MinerU]] — Extracteur de documents d'OpenDataLab vers Markdown, HTML, LaTeX et JSON : quatre niveaux de qualité, du traitement natif sur CPU jusqu'à un modèle vision-langage de 1,2 milliard de paramètres ; licence propre (Apache 2.0 plus conditions, seuils à 100 M d'utilisateurs ou 20 M$ de revenu mensuel), version 4.0 incompatible avec la 3.x.
- [[olmOCR]] — Toolkit d'Ai2 qui convertit PDF et images en Markdown avec un modèle vision-langage de 7 milliards de paramètres affiné pour l'OCR : tableaux, équations et ordre de lecture, traitement en lot sur GPU via vLLM ; code et poids Apache 2.0, GPU obligatoire.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.
- [[PaddleOCR]] — Boîte à outils OCR et parsing de documents de Baidu (PaddlePaddle) : pipeline détection-reconnaissance PP-OCRv6 sur des dizaines de langues, PP-StructureV3 pour tableaux, formules et mise en page, et modèle vision-langage PaddleOCR-VL de 0,9 milliard de paramètres ; Apache 2.0, CPU ou GPU.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.
- [[pdfminer.six]] — Bibliothèque Python pure sous MIT qui analyse la mise en page d'un PDF (caractères, mots, lignes, boîtes via LAParams) et en extrait texte et positions ; base de pdfplumber, lecture seule, sans OCR, lente et à maintenance ralentie.
- [[pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[pypdf]] — Bibliothèque Python pure sous BSD-3 pour lire, fusionner, découper, chiffrer, annoter et remplir des PDF, avec extraction de texte (modes plain et layout) ; aucune dépendance obligatoire, ni OCR ni rendu d'image.
- [[pypdfium2]] — Binding Python de PDFium, le moteur PDF de Chromium : rendu de pages en image, extraction de texte, objets de page et CLI, en roues précompilées et sous licence permissive (Apache 2.0 ou BSD-3) ; rapide, mais PDFium n'est pas thread-safe et aucune analyse de mise en page.
- [[Tesseract]] — Moteur OCR historique en C++ sous Apache 2.0 : reconnaissance par réseau LSTM sur plus de 100 langues, sorties texte, hOCR, TSV, ALTO et PDF cherchable ; CPU seul, sans framework de deep learning, mais sensible à la qualité de l'image et sans analyse de tableaux.
- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.

### Comparatifs
- [[Comparatif - Parsing de documents]]
<!-- AUTO:END -->
