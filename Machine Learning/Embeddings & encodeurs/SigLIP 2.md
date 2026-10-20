---
role: brique
nom: SigLIP 2
alias: [SigLIP2, google/siglip2, siglip2-so400m-patch14-384, SigLIP 2 So400m]
pitch: "Famille d'encodeurs image-texte de Google (Apache-2.0) — un encodeur d'image et un encodeur de texte alignés, multilingues, pour la classification d'images à zéro exemple et la recherche image-texte."
categorie: ml/embeddings
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[EmbeddingGemma 2]]", "[[Qwen3-VL-Embedding]]"]
tags: [embeddings, multimodal, vision-language, zero-shot, retrieval]
url_docs: https://huggingface.co/blog/siglip2
url_repo: https://github.com/google-research/big_vision
---

# SigLIP 2

<!-- AUTO:BANDEAU:START -->
> Famille d'encodeurs image-texte de Google (Apache-2.0) — un encodeur d'image et un encodeur de texte alignés, multilingues, pour la classification d'images à zéro exemple et la recherche image-texte.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

La deuxième génération des encodeurs **image-texte** de Google, publiée en février 2025 (arXiv 2502.14786, Tschannen et al.). Deux tours distinctes, une pour l'image et une pour le texte, entraînées pour que le vecteur d'une image et celui de sa légende soient proches ([[Apprentissage contrastif]]) : on retrouve une image par une phrase, ou on classe une image parmi des étiquettes écrites en texte, **sans exemple d'entraînement** de ces classes. Elle prolonge SigLIP (perte sigmoïde) avec des techniques déjà publiées : pré-entraînement par légendage, pertes auto-supervisées (auto-distillation, prédiction masquée) et curation des données en ligne ; le résumé annonce de meilleurs résultats en classification à zéro exemple, en recherche image-texte et comme encodeur pour des modèles vision-langage, avec une meilleure compréhension **multilingue**. Quatre tailles : B (86 M), L (303 M), So400m (400 M) et g (1 Md), en plusieurs patchs et résolutions, dont des variantes à résolution dynamique qui gardent le rapport d'aspect (« NaFlex »). Entraîné sur WebLI. Poids sur Hugging Face, chargeables avec Transformers.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| **Classer des images à zéro exemple** par des étiquettes en texte, ou retrouver une image par une phrase | Une **entrée mixte** (texte et image dans un même vecteur), de la vidéo ou de l'audio : [[Qwen3-VL-Embedding]] ou [[EmbeddingGemma 2]] |
| Un **encodeur de vision** de qualité pour un modèle vision-langage ou pour des vecteurs d'image (So400m sert de base à d'autres modèles) | Des **documents** dont il faut lire le texte : l'encodeur reconnaît des scènes, il ne lit pas une page dense ; voir [[RAG visuel - retrouver des documents sans OCR]] |
| Du **multilingue** et des modèles de petite taille (86 M) pour un poste ou un appareil | Des **requêtes longues et techniques** : la carte n'annonce aucune longueur de contexte ; [[Qwen3-VL-Embedding]] annonce 32K tokens |
| Licence **Apache-2.0** sur les cartes de modèles et dans le dépôt du code | Un index **sans écart entre modalités** : le modality gap existe aussi ici ([[Embedding multimodal et modality gap]]) |

## Mise en œuvre

- Installation — `uv add transformers torch pillow`
- Point d'entrée — `pipeline("zero-shot-image-classification", model="google/siglip2-so400m-patch14-384")` ; `AutoModel` et `AutoProcessor`, puis `model.get_image_features(**inputs)` pour les vecteurs d'image
- Prérequis — une image par appel de traitement à la résolution du modèle (384 pour So400m patch 14) ; des variantes à résolution dynamique existent pour les tailles B et So400m en patch 16
- Exécution — local ; le dépôt `big_vision` (JAX) contient le code d'entraînement
- Coût — gratuit sous Apache-2.0 ; le calcul augmente avec la taille et la résolution

## Limites à connaître

- **Pas un modèle de recherche de documents** : pour des pages, un modèle multi-vecteur ([[ColPali]]) ou un embedding multimodal récent s'en sort mieux ; ColPali part justement de SigLIP comme encodeur de vision.
- **Scores d'éditeur** : les résultats de la carte sont repris de l'article de Google ; aucun classement n'est établi ici avec [[EmbeddingGemma 2]] ou [[Qwen3-VL-Embedding]], dont les tailles et les protocoles diffèrent.
- **Deux encodeurs** : le texte et l'image ne se calculent pas dans le même modèle, ce qui rend les entrées entrelacées impossibles.

## Écosystème

### Alternatives

- [[EmbeddingGemma 2]] — Modèle d'embedding multimodal ouvert de Google DeepMind (Apache-2.0, 740 M) — texte, code, image, vidéo et audio dans un même espace de 768 dimensions et 8 192 tokens partagés, encodeurs désactivables ; scores publiés par Google seul. — un modèle unique pour cinq modalités, entrées entrelacées, au prix de 740 M de paramètres.
- [[Qwen3-VL-Embedding]] — Famille de modèles d'embedding multimodaux d'Alibaba (Apache-2.0, 2 B et 8 B) — texte, images, captures d'écran et vidéo dans un même espace, 32K tokens, dimension réglable, instructions de tâche ; pas d'audio. — entrées mixtes et contexte long, bien plus gros (2 B et 8 B).

## Ressources

- Documentation — billet Hugging Face : https://huggingface.co/blog/siglip2
- Dépôt — le code d'entraînement : https://github.com/google-research/big_vision
- Article — Tschannen et al., *SigLIP 2*, 2025 : https://arxiv.org/abs/2502.14786

## Voir aussi

- [[Embedding multimodal et modality gap]] — la notion : espace commun, écart entre modalités, limites
- [[Modèles de fondation vision]] — la famille des encodeurs de vision
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[Choisir un modèle d'embedding]] — critères de choix et limites des classements
