---
role: brique
nom: Qwen3-Embedding
alias: [Qwen3 Embedding, Qwen3-Embedding-0.6B, Qwen3-Embedding-4B, Qwen3-Embedding-8B]
pitch: "Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche."
categorie: ml/embeddings
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[bge-m3]]"]
complements: ["[[sentence-transformers]]", "[[Text Embeddings Inference]]"]
tags: [embeddings, semantic-search, retrieval, transformers, reranking]
url_docs: https://qwenlm.github.io/blog/qwen3-embedding/
url_repo: https://github.com/QwenLM/Qwen3-Embedding
---

# Qwen3-Embedding

<!-- AUTO:BANDEAU:START -->
> Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Trois modèles d'embedding de l'équipe Qwen (Alibaba), de 0,6 B, 4 B et 8 B de paramètres,
publiés le 2025-06-03 (article arXiv 2506.05176). Ils partent d'un **modèle de langage
décodeur**, Qwen3 base, et l'affinent en encodeur : le vecteur est l'état caché du
**dernier token** (`[EOS]`), puis normalisé. Les poids n'ont pas de `lm_head` : ils ne
génèrent rien. Le pré-entraînement contrastif s'appuie sur des paires **synthétisées par
Qwen3**, puis vient un entraînement supervisé et une fusion de modèles. Dimension maximale
de 1 024, 2 560 et 4 096 selon la taille, réglable de 32 jusqu'au maximum (Matryoshka) ;
contexte de 32K tokens ; plus de 100 langues, langages de programmation compris. Côté
requête, une **instruction de tâche** (`Instruct: …\nQuery:…`) est attendue ; la carte
annonce 1 à 5 % de gain avec elle. Téléchargements du mois au 2026-09-30 : 9,74 M pour
le 0,6 B, 1,83 M pour le 4 B, 2,55 M pour le 8 B.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un **contexte long** (32K) et du multilingue avec un seul modèle | Seul le **dense** suffit et la sobriété prime : [[bge-m3]] offre en plus le sparse et le multi-vecteur |
| Une **dimension réglable** (Matryoshka) pour alléger l'index vectoriel | Un **CPU sans GPU** avec le 4 B ou le 8 B : environ 8 et 15 Go de poids en BF16 (estimation tirée du nombre de paramètres, pas de la doc) |
| Un **petit modèle** qui tient sur du CPU : le 0,6 B, environ 1,2 Go | Une chaîne qui **oublie l'instruction** côté requête : la perte annoncée est de 1 à 5 % |
| Licence **Apache-2.0** sur les poids, sans restriction d'usage annoncée | Des vecteurs **stables d'un moteur à l'autre** : dérive signalée selon la version de vLLM et le GPU |
| Le même modèle servi par [[sentence-transformers]], [[Text Embeddings Inference]], vLLM, Ollama ou llama.cpp | Un besoin **multimodal** (image, vidéo) : c'est Qwen3-VL-Embedding, une autre famille (2026-01-07) |

## Mise en œuvre

- Installation — `uv add sentence-transformers` (transformers ≥ 4.51, faute de quoi `KeyError: 'qwen3'`)
- Point d'entrée — `SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")` ; `padding_side="left"` et `attn_implementation="flash_attention_2"` recommandés par la carte
- Prérequis — l'instruction de tâche en anglais côté requête ; la carte ne donne **aucune exigence matérielle**
- Exécution — local ; [[Text Embeddings Inference]] (image en version 1.7.2 ou plus récente, tags GPU et CPU), vLLM ≥ 0.8.5, Ollama (`qwen3-embedding`, 0,6 B, 4 B, 8 B), llama.cpp avec `--pooling last` et les GGUF officiels
- Coût — gratuit, Apache-2.0 ; le calcul augmente avec la taille

## Limites à connaître

- **Classement auto-déclaré et daté.** La carte place le 8 B premier du MTEB multilingue au 5 juin 2025, à 70,58 (4 B : 69,45 ; 0,6 B : 64,33), et donne en MTEB anglais v2 75,22, 74,60 et 70,70. Ces chiffres sont ceux de l'éditeur, relevés il y a plus d'un an : le classement actuel n'a pas été relu.
- **Sorties NaN en fp16** sur certains tokens (discussions Hugging Face n° 21 et 27, sur le 8 B notamment) ; **dérive des vecteurs** selon la version de vLLM et le GPU (n° 60).
- **La dimension personnalisée** a posé problème à des utilisateurs (n° 20, « always 4096 ») : vérifier la forme du vecteur rendu.
- **Un successeur multimodal existe**, Qwen3-VL-Embedding en 2B et 8B, sans équivalent texte seul plus récent relevé chez Qwen.
- **Non relu** : la licence du dépôt de code `QwenLM/Qwen3-Embedding` (le fichier `LICENSE` n'a pas pu être lu) ; les poids sont Apache-2.0 d'après l'API du Hub.

## Écosystème

### Alternatives

- [[bge-m3]] — Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle. — le multilingue à trois sorties, plus léger, sans instruction ni dimension réglable.

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — le charge : le Hub le déclare pour cette bibliothèque.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — le sert ; la famille Qwen3 est dans ses architectures supportées.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/Qwen/Qwen3-Embedding-8B
- Article — billet de présentation : https://qwenlm.github.io/blog/qwen3-embedding/
- Dépôt — https://github.com/QwenLM/Qwen3-Embedding
- Article — *Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models* (Zhang et al., 2025) — https://arxiv.org/abs/2506.05176

## Voir aussi

- [[Choisir un modèle d'embedding]] — la notion : taille, dimension, contexte, instructions, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
