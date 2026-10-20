---
role: comparatif
nom: Comparatif - Embeddings
categorie: ml/embeddings
tags: [embeddings, semantic-search]
---

# Comparatif - Embeddings

> On tranche sur : la nature de la brique d'abord — bibliothèque en process ou serveur partagé —, puis ce qu'elle sait servir (dense, sparse, multi-vecteur, images) et sur quel matériel. Un outil charge un modèle d'embedding ; le modèle, lui, se choisit à part.

![[Comparatif - Embeddings.base]]

## Ce qui départage

**Les outils qui calculent ou servent des embeddings.**

- [[sentence-transformers]] — le **généraliste** : tout modèle du Hub, l'entraînement et le fine-tuning, le dense, le sparse, le multi-vecteur (depuis la 6.0) et les cross-encoders. Il tourne en process, sur PyTorch, sans batching dynamique ni service ; Apache-2.0, 22,7 M de téléchargements PyPI sur trente jours. À prendre tant qu'aucun service partagé n'est nécessaire.
- [[FastEmbed]] — la voie **légère** : ONNX Runtime sans PyTorch, CPU par défaut, dense, sparse, late-interaction et rerankers. Le prix est un **catalogue fermé** (les modèles convertis par Qdrant, sans BGE-M3) et des licences de modèles à filtrer, certains étant CC-BY-NC ou sous licence Gemma. Naturel avec [[Qdrant]].
- [[Text Embeddings Inference]] — le **serveur** de référence, maintenu par Hugging Face : batching par tokens, images CPU et GPU, HTTP, gRPC et `/v1/embeddings`, métriques, hors-ligne documenté, Apache-2.0 depuis la v1.2.1. Il ne sert que ses architectures, sans ColBERT, ColPali ni CLIP, et sans quantification.
- [[Infinity]] — le serveur à **couverture plus large** : ColBERT, ColPali, CLIP, CLAP, plusieurs modèles par instance, AMD et Inferentia. Il est **moins sûr dans la durée** (mainteneur unique, une version en douze mois) et sa télémétrie est active par défaut.

**Les modèles d'embedding** (bge-m3, Qwen3-Embedding, EmbeddingGemma, SigLIP 2 et les autres) ne sont pas des briques du brain : un outil ci-dessus en charge un, et le brain ne décrit que des outils. Les critères de choix sont dans [[Choisir un modèle d'embedding]], et le cas texte-image dans [[Embedding multimodal et modality gap]].

**Pas de fiche ici** (hors brain ou par le plafond de la capture) : FlagEmbedding (bibliothèque du BAAI : les trois sorties de BGE-M3, le fine-tuning et l'évaluation ; c'est la voie documentée pour les trois sorties, MIT), Model2Vec (embeddings statiques, MIT : environ 82 à 95 % de la qualité d'un petit transformer selon l'éditeur, pour un débit sans commune mesure sur CPU) et nomic-embed-text (Apache-2.0, préfixes obligatoires). Choisir entre modèles : [[Choisir un modèle d'embedding]].

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Embeddings & encodeurs]] — le hub du dossier.
- [[Choisir un modèle d'embedding]] — la notion : critères de choix et limites de MTEB.
