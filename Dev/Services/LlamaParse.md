---
galaxie: dev
type: service
nom: LlamaParse
alias: [llamaparse, llama-parse, LlamaCloud Parse]
pitch: "Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source."
categorie: data/parsing
licence_type: proprietary
hosted: managed
maturite: production
langage: Python
scaling: serverless
alternatives: ["[[Dev/Services/Unstructured|Unstructured]]", "[[Dev/Services/Docling|Docling]]", "[[Dev/Services/Marker|Marker]]"]
remplace_par: []
status: actif
tags: [document-parsing, rag, ocr]
url_docs: https://docs.cloud.llamaindex.ai/
url_repo: 
---

# LlamaParse

## Pourquoi

LlamaParse est le service de parsing de documents de **LlamaCloud** (LlamaIndex). Service **managé, non open-source**, qui extrait les PDF complexes — tableaux imbriqués, multi-colonnes, schémas, documents scannés — vers du **Markdown propre** prêt à chunker pour le RAG. La v2 expose des **tiers** (Fast, Cost-Effective, Agentic, Agentic Plus) selon le compromis coût/qualité, l'extraction « agentique » s'appuyant sur des LLM. Facturation à **crédits** ; intégration directe avec LlamaIndex.

## Quand l'utiliser

- PDF **complexes** (rapports financiers, tableaux denses, mises en page multi-colonnes) où la qualité prime.
- Externaliser le parsing : ni infra GPU ni modèles à opérer.
- Pipeline RAG déjà bâti sur LlamaIndex.
- Volumétrie modérée couverte par le palier gratuit (crédits mensuels) ou un budget crédits.

## Quand NE PAS l'utiliser

- Documents **confidentiels** interdits de cloud tiers → [[Dev/Services/Docling|Docling]] / [[Dev/Services/Unstructured|Unstructured]] en local.
- Gros volumes où le coût crédits explose → self-host [[Dev/Services/Marker|Marker]] / [[Dev/Services/Docling|Docling]].
- Simple extraction de texte d'un PDF basique → [[Dev/Services/PyMuPDF|PyMuPDF]] / [[Dev/Services/pdfplumber|pdfplumber]].

## Déploiement & coût

- **Managé uniquement** : API cloud + SDK Python & TypeScript (`pip install llama-cloud-services`). Non open-source.
- Modèle à **crédits** (≈ 1000 crédits = 1,25 $ ; ~1 crédit/page en extraction simple, 3+ en mode LLM) ; palier gratuit mensuel pour démarrer.
- Données chiffrées en transit/au repos, cache éphémère (48 h) ; déploiement **VPC privé** possible en entreprise.

## Pièges

- Dépendance à un service tiers : disponibilité, latence réseau, évolutions tarifaires.
- Le coût grimpe vite sur gros volumes en mode agentique.
- Les documents transitent par le cloud — incompatible avec certaines contraintes de souveraineté (hors VPC privé).

## Alternatives

- [[Dev/Services/Unstructured|Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Dev/Services/Docling|Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Dev/Services/Marker|Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.

## Liens

- [[Comparatif - Parsing de documents]] — comparatif de la catégorie.
- Doc : https://docs.cloud.llamaindex.ai/
