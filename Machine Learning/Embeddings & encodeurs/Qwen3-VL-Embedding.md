---
role: brique
nom: Qwen3-VL-Embedding
alias: [Qwen3 VL Embedding, Qwen3-VL-Embedding-2B, Qwen3-VL-Embedding-8B, Qwen3-VL-Reranker]
pitch: "Famille de modèles d'embedding multimodaux d'Alibaba (Apache-2.0, 2 B et 8 B) — texte, images, captures d'écran et vidéo dans un même espace, 32K tokens, dimension réglable, instructions de tâche ; pas d'audio."
categorie: ml/embeddings
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[EmbeddingGemma 2]]", "[[SigLIP 2]]"]
tags: [embeddings, multimodal, vision-language, retrieval, reranking]
url_docs: https://qwen.ai/blog?id=qwen3-vl-embedding
url_repo: https://github.com/QwenLM/Qwen3-VL-Embedding
---

# Qwen3-VL-Embedding

<!-- AUTO:BANDEAU:START -->
> Famille de modèles d'embedding multimodaux d'Alibaba (Apache-2.0, 2 B et 8 B) — texte, images, captures d'écran et vidéo dans un même espace, 32K tokens, dimension réglable, instructions de tâche ; pas d'audio.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Deux modèles d'embedding de l'équipe Qwen (Alibaba), de **2 B et 8 B** de paramètres, bâtis sur le modèle vision-langage Qwen3-VL et publiés le 2026-01-07 (rapport technique arXiv 2601.04720). Ils acceptent du **texte, des images, des captures d'écran, de la vidéo et des entrées mixtes** (texte et image, texte et vidéo) et les placent dans un même espace ([[Embedding multimodal et modality gap]]). Architecture « deux tours » : le vecteur est l'état caché du dernier token (`[EOS]`) de la dernière couche. Contexte de 32K tokens ; dimension maximale de 2 048 (2 B) et de 4 096 (8 B), réglable par Matryoshka (de 64 à 2 048 pour le 2 B) ; plus de 30 langues (33 listées, français compris) ; instructions de tâche attendues côté requête (gain annoncé de 1 à 5 %). Le dépôt publie aussi un **reranker** multimodal de mêmes tailles (Qwen3-VL-Reranker, architecture « une tour », score par paire requête-document). Téléchargements sur trente jours au 2026-10-20 : 0,81 M pour le 2 B, 1,41 M pour le 8 B.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des **documents visuels** (pages, captures, schémas) et du texte dans un **même index**, avec un contexte long | Un besoin d'**audio** : aucune entrée audio ; voir [[EmbeddingGemma 2]] |
| **Deux tailles** : 2 B pour un poste ou un petit GPU, 8 B quand la qualité prime | Un **matériel sans GPU** : 2 B et 8 B de paramètres ; la carte renvoie au rapport technique pour les exigences matérielles |
| Une **dimension réglable** pour alléger l'index (Matryoshka) et une **quantification** des vecteurs de sortie | Les **comparaisons avec d'autres modèles** : scores publiés par Qwen (MMEB-V2 global 73,2 pour le 2 B et 77,8 pour le 8 B), protocoles et tailles différents |
| La paire **embedding puis reranker** du même éditeur, dans le même dépôt | Un environnement **ancien** : le chargement par le dépôt exige transformers ≥ 4.57 et qwen-vl-utils ≥ 0.0.14 |
| Licence **Apache-2.0** sur les cartes et dans le dépôt (fichier LICENSE) | |

## Mise en œuvre

- Installation — `uv add sentence-transformers` (carte du modèle : `SentenceTransformer`, `model.encode`) ; ou le dépôt, qui fournit `Qwen3VLEmbedder` (transformers ≥ 4.57, qwen-vl-utils ≥ 0.0.14) ; un exemple vLLM figure dans la carte
- Point d'entrée — `model.encode([{"text": …, "image": …}])` ; instruction par défaut « Represent the user's input. », personnalisable par le paramètre `prompt`
- Prérequis — l'instruction de tâche en anglais de préférence ; `flash_attention_2` recommandé pour la vitesse et la mémoire
- Exécution — local ; modèles sur Hugging Face et ModelScope
- Coût — gratuit sous Apache-2.0 ; le calcul augmente avec la taille

## Limites à connaître

- **Scores d'un seul éditeur** (MMEB-V2, MMTEB) : relevés sur la carte du modèle, avec des concurrents réévalués par Qwen. **Aucune conclusion de classement** avec [[EmbeddingGemma 2]] (740 M, 59,01 de MMEB v2 selon Google) : tailles différentes, protocoles non prouvés identiques.
- **Gros modèles** : 2 B et 8 B contre 740 M pour EmbeddingGemma 2 ; le 8 B demande un GPU.
- **Un embedding ne restitue pas le texte d'une image** : pour citer, un OCR ou un modèle de lecture.
- **Stabilité entre moteurs** : comme pour [[Qwen3-Embedding]], vérifier que le même texte donne le même vecteur dans le moteur de service avant de réindexer.

## Écosystème

### Alternatives

- [[EmbeddingGemma 2]] — Modèle d'embedding multimodal ouvert de Google DeepMind (Apache-2.0, 740 M) — texte, code, image, vidéo et audio dans un même espace de 768 dimensions et 8 192 tokens partagés, encodeurs désactivables ; scores publiés par Google seul. — plus petit, avec l'audio, sur 8 192 tokens partagés et sans reranker associé.
- [[SigLIP 2]] — Famille d'encodeurs image-texte de Google (Apache-2.0) — un encodeur d'image et un encodeur de texte alignés, multilingues, pour la classification d'images à zéro exemple et la recherche image-texte. — image et texte seulement, deux encodeurs, sans entrée mixte ni contexte long.
- voisin : [[Qwen3-Embedding]] — la famille texte de la même équipe, à prendre quand aucune image n'est en jeu.

## Ressources

- Documentation — carte du modèle 8 B : https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B
- Dépôt — https://github.com/QwenLM/Qwen3-VL-Embedding
- Article — rapport technique, arXiv 2601.04720 : https://arxiv.org/abs/2601.04720

## Voir aussi

- [[Embedding multimodal et modality gap]] — la notion : espace commun, écart entre modalités, limites
- [[Choisir un modèle d'embedding]] — critères de choix et limites des classements
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[RAG visuel - retrouver des documents sans OCR]] — l'usage sur des pages de documents
