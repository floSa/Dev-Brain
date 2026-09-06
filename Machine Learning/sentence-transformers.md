---
role: brique
nom: sentence-transformers
alias: [sbert, sentence transformers, sentence-bert]
pitch: "Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi."
categorie: ml/embeddings
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[HuggingFace]]", "[[SetFit]]", "[[txtai]]"]
tags: [embeddings, semantic-search, retrieval, reranking, nlp]
url_docs: https://www.sbert.net
url_repo: https://github.com/huggingface/sentence-transformers
---

# sentence-transformers

<!-- AUTO:BANDEAU:START -->
> Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Le framework de référence pour produire des **embeddings de phrases** (SBERT). Il charge des
centaines de modèles pré-entraînés et encode du texte — ou des images — en vecteurs denses
comparables au cosinus, en quelques lignes. Il fournit deux familles qui ne se substituent
pas : les **bi-encoders**, dont les vecteurs se pré-calculent et s'indexent, et les
**cross-encoders**, qui notent une paire requête-document sans rien pouvoir pré-calculer, et
ne servent donc que sur le top-k d'un [[Reranking|re-ranking]]. Deux contraintes commandent
l'usage : normaliser les vecteurs, et indexer puis requêter avec le **même modèle** — deux
modèles donnent deux espaces incompatibles. Maintenu par Hugging Face.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Produire des [[embeddings]] de phrases ou de documents : recherche sémantique, [[RAG]], clustering, déduplication | Recherche purement **lexicale** sur mots exacts → [[rank-bm25]], ou un moteur comme [[Elasticsearch]] |
| Étage **dense** d'un pipeline de [[Recherche d'information]] | Un **cross-encoder ne se pré-calcule pas** : le réserver au top-k, jamais à l'indexation |
| [[Reranking]] avec un cross-encoder — BGE-reranker, mxbai | Le modèle doit être **adapté à la langue et au domaine** : un multilingue générique dégrade sur un corpus spécialisé |
| Fine-tuner un encodeur sur son domaine, par perte contrastive (`MultipleNegativesRankingLoss`) | Embeddings **managés** par API : c'est une alternative d'infrastructure hors brain — OpenAI, Cohere, Voyage |
| | Génération de texte : c'est de l'encodage, pas un LLM génératif |

## Mise en œuvre

- Installation — `uv add sentence-transformers`
- Point d'entrée — API Python : `SentenceTransformer(...).encode(...)` pour les bi-encoders, `CrossEncoder` pour le re-ranking
- Prérequis — un modèle du Hub adapté à la langue et au domaine ; le même de bout en bout, indexation et requête
- Exécution — single-node ; GPU recommandé pour encoder du volume, CPU possible sur petits jeux
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- Aucun substitut direct dans le brain : c'est la voie open-source de référence pour les embeddings locaux.
- Embeddings managés par API — OpenAI, Cohere, Voyage : une alternative d'infrastructure, pas de bibliothèque (pas encore en fiche).

### Compléments

- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes — le socle de modèles et le Hub d'où viennent les encodeurs.
- [[SetFit]] — Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM — bâti dessus, pour la classification few-shot.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI. — l'index et les workflows qui se montent au-dessus des embeddings produits

## Ressources

- Documentation — https://www.sbert.net
- Dépôt — https://github.com/huggingface/sentence-transformers

## Voir aussi

- [[embeddings]] — la notion : ce qu'il produit
- [[Recherche d'information]] · [[Reranking]] · [[RAG]] — ses usages
- [[PyTorch]] — le framework de calcul sous-jacent
- [[Comparatif - NLP]] — ce qui départage les outils de la chaîne texte
