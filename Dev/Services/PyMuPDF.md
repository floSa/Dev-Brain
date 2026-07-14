---
galaxie: dev
type: service
nom: PyMuPDF
alias: [pymupdf, fitz, MuPDF]
pitch: "Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale."
categorie: data/parsing
licence_type: open-source
hosted: self
maturite: production
langage: C / Python
scaling: single-node
alternatives: ["[[Dev/Services/pdfplumber|pdfplumber]]"]
remplace_par: []
status: actif
tags: [pdf, document-parsing]
url_docs: https://pymupdf.readthedocs.io/
url_repo: https://github.com/pymupdf/PyMuPDF
---

# PyMuPDF

## Pourquoi

PyMuPDF (importé `pymupdf`, alias historique `fitz`) est le **binding Python de MuPDF**, le moteur C de rendu et d'analyse de documents d'Artifex. C'est la **référence de vitesse** de l'écosystème Python : extraction de texte, images, tableaux, annotations, champs de formulaire, métadonnées, et **rendu en image**, avec un **accès bas niveau au modèle objet PDF** (blocs, spans, coordonnées). Gère aussi XPS, EPUB, CBZ. Double licence : **AGPL-3.0** (open-source) ou **licence commerciale Artifex** pour les usages propriétaires.

## Quand l'utiliser

- Extraire vite du texte/images d'un **gros volume** de PDF (le plus rapide en Python).
- Manipuler le PDF : découper, fusionner, caviarder (redact), annoter, rendre en image, lire les formulaires.
- Accès **fin aux objets** (blocs, spans, coordonnées) pour bâtir son propre pipeline de parsing.

## Quand NE PAS l'utiliser

- Extraction de **tableaux** complexes avec réglage fin et débogage visuel → [[Dev/Services/pdfplumber|pdfplumber]].
- Conversion **structurée en Markdown** pour le RAG → [[Dev/Services/Docling|Docling]] / [[Dev/Services/Marker|Marker]].
- Contrainte AGPL incompatible avec un produit propriétaire sans budget licence → [[Dev/Services/pdfplumber|pdfplumber]] (MIT).

## Déploiement & coût

- Bibliothèque (`pip install pymupdf`), roues précompilées embarquant MuPDF ; **aucune dépendance système**.
- **AGPL-3.0** : usage open-source gratuit, mais un service réseau/SaaS déclenche l'obligation de divulgation du code ; sinon **licence commerciale Artifex** (payante).
- Single-node ; extrêmement rapide et léger.

## Pièges

- **AGPL** : piège juridique en SaaS / produit fermé — anticiper la licence commerciale.
- Double nommage de l'API (`fitz` vs `pymupdf`) selon les versions.
- Extraction de tableaux moins fine que pdfplumber sur les mises en page tordues.

## Alternatives

- [[Dev/Services/pdfplumber|pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Étage RAG complémentaire : [[Dev/Services/Docling|Docling]] / [[Dev/Services/Marker|Marker]] pour la conversion structurée.
- Doc : https://pymupdf.readthedocs.io/
