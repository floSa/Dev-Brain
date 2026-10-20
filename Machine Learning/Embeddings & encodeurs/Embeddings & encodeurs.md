---
role: hub
nom: Embeddings & encodeurs
alias: [embeddings et encodeurs, calcul d'embeddings, serving d'embeddings]
pitch: Produire des vecteurs à partir de texte — choisir le modèle, puis l'outil qui le calcule ou le sert, sans dépendre d'une API externe.
domaines: [data-sci, ai-eng, mlops]
tags: [embeddings, semantic-search, retrieval, model-serving, inference]
---

# Embeddings & encodeurs

> Produire des vecteurs à partir de texte — choisir le modèle, puis l'outil qui le calcule ou le sert, sans dépendre d'une API externe.

## Ce qu'il faut comprendre

- **Ce dossier produit des vecteurs ; il ne les range pas.** Les stocker et les interroger est le métier de [[Bases de données vectorielles]] et du domaine [[Bases de données]] ; en faire un pipeline de génération augmentée est celui de [[LLM & IA générative]]. La notion de base est [[embeddings]].
- **Un outil et un modèle sont deux choix distincts.** Le modèle fixe la qualité, les langues, le contexte, la dimension et la licence des poids ; l'outil fixe où et comment le calcul tourne. Un même modèle se charge en bibliothèque ([[sentence-transformers]], [[FastEmbed]]) ou se sert derrière une API ([[Text Embeddings Inference]], [[Infinity]]).
- **Le modèle se choisit sur ses propres données.** Les classements publics servent à dresser une liste courte, pas à trancher ; ce qu'ils mesurent et ce qu'ils ne mesurent pas est dans [[Choisir un modèle d'embedding]].
- **Deux modèles donnent deux espaces incompatibles.** Changer de modèle, c'est recalculer tout l'index : le coût d'un changement fait partie du choix.
- **La licence des poids n'est pas celle du code.** Des modèles répandus sont restreints — non commercial, conditions d'usage — et il faut lire la carte de chacun, pas la licence de l'outil qui le charge.

## Choisir

- Calculer des embeddings dans un script ou un service Python, avec tout le Hub et le fine-tuning → [[sentence-transformers]].
- Les calculer sur CPU, sans PyTorch, avec un catalogue fermé de modèles convertis → [[FastEmbed]].
- Un service partagé, maintenu par Hugging Face, avec métriques et gRPC → [[Text Embeddings Inference]].
- Un service qui sert aussi ColBERT, ColPali ou CLIP, en acceptant un mainteneur unique → [[Infinity]].
- Un modèle multilingue qui produit dense, sparse et multi-vecteur, ou à contexte long et dimension réglable → [[Choisir un modèle d'embedding]] ; les modèles d'embedding ne sont pas des fiches du brain, la notion les cite en texte simple.
- Une question en texte qui doit retrouver une image, une vidéo ou un extrait audio : un embedding multimodal, après avoir lu [[Embedding multimodal et modality gap]] ; sans classement, les scores étant ceux de chaque éditeur.
- Reclasser un top-k avec un cross-encoder → [[Reranking]] et [[Comparatif - Rerankers]] (domaine [[LLM & IA générative]]). Cf. [[Comparatif - Embeddings]].

<!-- AUTO:START -->
### Notions
- [[Choisir un modèle d'embedding]] — domaines : data-sci, ai-eng
- [[Embedding multimodal et modality gap]] — domaines : ai-eng, ml-eng
- [[embeddings]] — domaines : data-sci, ai-eng

### Briques
- [[FastEmbed]] — Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut.
- [[Infinity]] — Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique.
- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026.

### Comparatifs
- [[Comparatif - Embeddings]]
<!-- AUTO:END -->
