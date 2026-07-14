---
galaxie: dev
type: service
nom: pdfplumber
alias: [pdfplumber, jsvine-pdfplumber]
pitch: "Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT."
categorie: data/parsing
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/PyMuPDF|PyMuPDF]]"]
remplace_par: []
status: actif
tags: [pdf, table-extraction, document-parsing]
url_docs: https://github.com/jsvine/pdfplumber
url_repo: https://github.com/jsvine/pdfplumber
---

# pdfplumber

## Pourquoi

pdfplumber (Jeremy Singer-Vine, **MIT**) est bâti sur **pdfminer.six** et expose, pour chaque page, un **accès détaillé à chaque objet** (caractères, lignes, rectangles, courbes) avec ses coordonnées. Au-dessus, des méthodes de haut niveau extraient texte et surtout **tableaux**, avec des stratégies de détection configurables (lignes explicites vs alignement de texte) et un **débogage visuel** (rendu de la page avec les objets / tableaux détectés). Pur Python, idéal pour les **PDF natifs** (non scannés).

## Quand l'utiliser

- Extraction de **tableaux** de PDF natifs avec réglage fin (stratégies, tolérances).
- Contrôle précis sur la **position des objets** (coordonnées, géométrie).
- **Débogage visuel** pour comprendre une mise en page récalcitrante.
- Pur Python, sans binaire système ni contrainte de licence (**MIT**).

## Quand NE PAS l'utiliser

- **Vitesse brute** sur gros volumes → [[Dev/Services/PyMuPDF|PyMuPDF]] (nettement plus rapide).
- PDF **scannés** (images) : pas d'OCR intégré → [[Dev/Services/Marker|Marker]] / [[Dev/Services/Unstructured|Unstructured]].
- Conversion **structurée en Markdown** pour le RAG → [[Dev/Services/Docling|Docling]] / [[Dev/Services/Marker|Marker]].

## Déploiement & coût

- Bibliothèque (`pip install pdfplumber`), **MIT**, pur Python (dépend de pdfminer.six) ; aucune dépendance système.
- Single-node ; léger, mais plus lent que PyMuPDF.

## Pièges

- **Pas d'OCR** : inopérant sur PDF scannés.
- Plus **lent** que PyMuPDF sur gros volumes.
- L'extraction de tableaux demande souvent du **tuning** (stratégies `lines` / `text`, tolérances).

## Alternatives

- [[Dev/Services/PyMuPDF|PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Étage RAG complémentaire : [[Dev/Services/Docling|Docling]] / [[Dev/Services/Unstructured|Unstructured]] pour le pipeline d'ingestion.
- Fondation : pdfminer.six (parsing PDF bas niveau, MIT).
- Doc : https://github.com/jsvine/pdfplumber
