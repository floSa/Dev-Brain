---
role: comparatif
nom: Comparatif - Embeddings
categorie: ml/embeddings
tags: [embeddings, semantic-search]
---

# Comparatif - Embeddings

> On tranche sur : la nature de la brique d'abord — bibliothèque en process, serveur partagé ou jeu de poids —, puis, pour un outil, ce qu'il sait servir (dense, sparse, multi-vecteur, images) et sur quel matériel, et, pour un modèle, la licence des poids, le contexte, la dimension réglable et les langues. Les outils et les modèles ne se substituent pas : un outil charge un modèle.

![[Comparatif - Embeddings.base]]

## Ce qui départage

**Les outils qui calculent ou servent des embeddings.**

- [[sentence-transformers]] — le **généraliste** : tout modèle du Hub, l'entraînement et le fine-tuning, le dense, le sparse, le multi-vecteur (depuis la 6.0) et les cross-encoders. Il tourne en process, sur PyTorch, sans batching dynamique ni service ; Apache-2.0, 22,7 M de téléchargements PyPI sur trente jours. À prendre tant qu'aucun service partagé n'est nécessaire.
- [[FastEmbed]] — la voie **légère** : ONNX Runtime sans PyTorch, CPU par défaut, dense, sparse, late-interaction et rerankers. Le prix est un **catalogue fermé** (les modèles convertis par Qdrant, sans BGE-M3) et des licences de modèles à filtrer, certains étant CC-BY-NC ou sous licence Gemma. Naturel avec [[Qdrant]].
- [[Text Embeddings Inference]] — le **serveur** de référence, maintenu par Hugging Face : batching par tokens, images CPU et GPU, HTTP, gRPC et `/v1/embeddings`, métriques, hors-ligne documenté, Apache-2.0 depuis la v1.2.1. Il ne sert que ses architectures, sans ColBERT, ColPali ni CLIP, et sans quantification.
- [[Infinity]] — le serveur à **couverture plus large** : ColBERT, ColPali, CLIP, CLAP, plusieurs modèles par instance, AMD et Inferentia. Il est **moins sûr dans la durée** (mainteneur unique, une version en douze mois) et sa télémétrie est active par défaut.

**Les modèles.**

- [[bge-m3]] — le **multilingue à trois sorties** : dense, sparse et multi-vecteur d'un seul calcul, 8 192 tokens, MIT, 568 M. Pas de Matryoshka documenté ; les trois sorties exigent FlagEmbedding, le serveur TEI ne documentant que le dense.
- [[Qwen3-Embedding]] — la **famille à contexte long et dimension réglable** : 32K tokens, de 0,6 B à 8 B, Apache-2.0, instructions de tâche à poser. Dense seulement, dérivée d'un décodeur ; le 0,6 B tient sur CPU, le 8 B veut un GPU.

**Pas de fiche ici**, par le plafond de la capture : FlagEmbedding (bibliothèque du BAAI : les trois sorties de BGE-M3, le fine-tuning et l'évaluation ; c'est la voie documentée pour les trois sorties, MIT), Model2Vec (embeddings statiques, MIT : environ 82 à 95 % de la qualité d'un petit transformer selon l'éditeur, pour un débit sans commune mesure sur CPU) et nomic-embed-text (Apache-2.0, préfixes obligatoires). Choisir entre modèles : [[Choisir un modèle d'embedding]].

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Embeddings & encodeurs]] — le hub du dossier.
- [[Choisir un modèle d'embedding]] — la notion : critères de choix et limites de MTEB.
