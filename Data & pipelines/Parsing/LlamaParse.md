---
role: brique
nom: LlamaParse
alias: [llamaparse, llama-parse, LlamaCloud Parse]
pitch: "Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source."
categorie: data/parsing
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: Python
scaling: serverless
alternatives: ["[[Unstructured]]", "[[Docling]]", "[[Marker]]"]
complements: []
tags: [document-parsing, rag, ocr]
url_docs: https://docs.cloud.llamaindex.ai/
url_repo: 
---

# LlamaParse

<!-- AUTO:BANDEAU:START -->
> Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Service de parsing de documents de **LlamaCloud** (LlamaIndex). Il extrait les PDF complexes —
tableaux imbriqués, multi-colonnes, schémas, documents scannés — vers du **Markdown propre**,
prêt à chunker pour le RAG. La v2 expose des **tiers** — Fast, Cost-Effective, Agentic,
Agentic Plus — qui échelonnent le compromis coût/qualité, l'extraction agentique s'appuyant
sur des LLM. Rien à opérer : ni infra GPU, ni modèles. Les documents transitent par le cloud,
chiffrés en transit et au repos, avec un cache éphémère de 48 h ; un déploiement en **VPC
privé** existe en entreprise.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| PDF complexes — rapports financiers, tableaux denses, mises en page multi-colonnes — où la qualité prime | Les documents transitent par le cloud : incompatible avec une contrainte de souveraineté, hors VPC privé |
| Externaliser le parsing : ni infra GPU ni modèles à opérer | Le coût grimpe vite sur gros volumes en mode agentique |
| Pipeline RAG déjà bâti sur LlamaIndex | Dépendance à un service tiers : disponibilité, latence réseau, évolutions tarifaires |
| Volumétrie modérée, couverte par le palier gratuit mensuel ou un budget crédits | |

## Mise en œuvre

- Installation — rien à installer côté serveur ; SDK Python `pip install llama-cloud-services`, SDK TypeScript aussi
- Point d'entrée — API cloud LlamaCloud, avec intégration directe LlamaIndex
- Prérequis — un compte LlamaCloud et des crédits ; les documents doivent pouvoir sortir du réseau, hors VPC privé
- Exécution — managé uniquement, serverless ; déploiement en VPC privé possible en entreprise
- Coût — à crédits — environ 1000 crédits pour 1,25 $, à peu près 1 crédit par page en extraction simple et 3 ou plus en mode LLM — avec un palier gratuit mensuel pour démarrer

## Écosystème

### Alternatives

- [[Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.

## Ressources

- Documentation — https://docs.cloud.llamaindex.ai/

## Voir aussi

- [[Parsing]] — le hub du dossier
- [[Comparatif - Parsing de documents]] — ce qui départage les outils du dossier
