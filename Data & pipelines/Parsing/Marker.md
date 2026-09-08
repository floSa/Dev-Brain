---
role: brique
nom: Marker
alias: [marker, marker-pdf, datalab-marker]
pitch: "Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte."
categorie: data/parsing
famille: paquet
licence_type: source-available
maturite: production
langage: Python
alternatives: ["[[Unstructured]]", "[[Docling]]", "[[LlamaParse]]", "[[pdf-inspector]]", "[[OpenDataLoader PDF]]"]
complements: ["[[PyMuPDF]]"]
tags: [document-parsing, pdf, ocr, markdown-conversion, rag]
url_docs: https://github.com/datalab-to/marker
url_repo: https://github.com/datalab-to/marker
---

# Marker

<!-- AUTO:BANDEAU:START -->
> Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | source-available | en bibliothèque, rien à héberger | production | à jour · 2026-07-20 |
<!-- AUTO:BANDEAU:END -->

## Définition

Marker, de datalab.to (Vik Paruchuri), convertit des PDF — et désormais de l'Office, des
images, de l'EPUB — en **Markdown, JSON, HTML ou chunks**, avec une bonne fidélité sur les
formules, les tableaux et l'ordre de lecture. C'est un **pipeline vision multi-étapes** bâti
sur la famille de modèles OCR **Surya**, du même éditeur : détection, reconnaissance, analyse
de layout. Il est optimisé pour le **débit** — des dizaines de pages par seconde sur GPU — et
l'OCR intégré lui ouvre les documents scannés. Sa vraie frontière est la licence, à deux
étages : le code d'un côté, les **poids des modèles** de l'autre, qui ne suivent pas les mêmes
règles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Convertir en lot des PDF en Markdown propre pour le RAG, en self-host avec GPU | Double licence à surveiller : code en GPL-3.0, poids en OpenRAIL-M modifiée, gratuits seulement en dessous de 2 M$ de revenus ou de financement — au-delà, licence commerciale Datalab |
| Documents riches — formules, tableaux, multi-colonnes — où la qualité de conversion compte | Le GPL peut contaminer une distribution propriétaire : bien isoler |
| Débit élevé recherché, de l'ordre de dizaines de pages par seconde sur GPU | Sans GPU, le débit s'effondre |
| Documents scannés : l'OCR Surya est intégré, rien à brancher | |

## Mise en œuvre

- Installation — `pip install marker-pdf` ; les modèles Surya se téléchargent
- Point d'entrée — conversion vers Markdown, JSON, HTML ou chunks ; l'API Datalab expose le même moteur en managé
- Prérequis — GPU fortement recommandé
- Exécution — mono-nœud par instance GPU en self-host ; l'API Datalab évite toute infra
- Coût — code GPL-3.0 gratuit ; poids OpenRAIL-M gratuits sous le seuil de 2 M$, licence commerciale Datalab au-delà ; l'API Datalab est payante

## Écosystème

### Alternatives

- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.
- [[OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.

### Compléments

- [[PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale. — l'étage bas niveau, pour l'extraction brute en amont.

## Ressources

- Documentation — https://github.com/datalab-to/marker
- Dépôt — https://github.com/datalab-to/marker

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
