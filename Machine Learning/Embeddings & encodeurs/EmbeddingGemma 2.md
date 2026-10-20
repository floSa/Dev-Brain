---
role: brique
nom: EmbeddingGemma 2
alias: [EmbeddingGemma2, embeddinggemma-2, google/embeddinggemma-2, EmbeddingGemma v2]
pitch: "Modèle d'embedding multimodal ouvert de Google DeepMind (Apache-2.0, 740 M) — texte, code, image, vidéo et audio dans un même espace de 768 dimensions et 8 192 tokens partagés, encodeurs désactivables ; scores publiés par Google seul."
categorie: ml/embeddings
famille: modele
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Qwen3-VL-Embedding]]", "[[SigLIP 2]]"]
tags: [embeddings, multimodal, semantic-search, retrieval, embedded]
url_docs: https://huggingface.co/google/embeddinggemma-2
url_repo: https://huggingface.co/google/embeddinggemma-2
---

# EmbeddingGemma 2

<!-- AUTO:BANDEAU:START -->
> Modèle d'embedding multimodal ouvert de Google DeepMind (Apache-2.0, 740 M) — texte, code, image, vidéo et audio dans un même espace de 768 dimensions et 8 192 tokens partagés, encodeurs désactivables ; scores publiés par Google seul.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un modèle à poids ouverts de Google DeepMind qui projette du **texte (code compris), des images, de la vidéo et de l'audio**, seuls ou **entrelacés**, dans **un seul espace de 768 dimensions** ([[Embedding multimodal et modality gap]]). 740 M de paramètres en tout : un modèle texte de 270 M (130 M de transformeur et 140 M de table de vocabulaire, bâti sur l'architecture de Gemma 4), un encodeur de vision de 170 M et un encodeur audio de 300 M. Les deux encodeurs se **désactivent** au chargement : 270 M en texte seul, 440 M avec l'image, 570 M avec l'audio, 740 M pour tout. Contexte de 8 192 tokens **partagés** entre les modalités (par défaut : 280 tokens par image, 140 par image de vidéo, 25 par seconde d'audio, soit environ 29 images, 58 images de vidéo ou 327 secondes d'audio seuls). Dimension tronquable à 512, 256 ou 128 (Matryoshka), avec renormalisation. Publié par Google le 2026-10-06 ; la carte Hugging Face compte 167 750 téléchargements sur trente jours à la lecture du 2026-10-20.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| **Un seul modèle ouvert** pour du texte, des images, de la vidéo et de l'audio, sans maintenir une conversion par modalité | Seul le **texte** compte et le français prime : [[bge-m3]] ou [[Qwen3-Embedding]] sont mieux documentés en texte ; le score MTEB multilingue annoncé (61,36) est de peu supérieur à celui de la v1 (61,15) |
| **Matériel modeste** : les encodeurs inutiles se désactivent, 270 M en texte seul ; Google chiffre 567 Mo de mémoire active en multimodal sur un téléphone | Un **classement indépendant** : aucun score ne vient d'un tiers, il n'y a pas de rapport technique, et les tailles diffèrent de celles de [[Qwen3-VL-Embedding]] (2 B et 8 B) |
| Un **index léger** : 768 dimensions, tronquables à 256 avec une perte annoncée faible | Les **128 dimensions en multimodal** : MMEB v2 global de 59,01 à 768 dimensions et 45,65 à 128, selon Google |
| Licence **Apache-2.0** sur la carte | Un **contexte long** : 8 192 tokens partagés entre toutes les modalités |

## Mise en œuvre

- Installation — `uv add sentence-transformers transformers`
- Point d'entrée — `SentenceTransformer("google/embeddinggemma-2")` ; `model.encode(texte, prompt_name="SearchQuery")` pour une requête, `prompt_name="Document"` pour un document ; un dictionnaire `{"text": ..., "image": [...], "video": ...}` pour une entrée entrelacée, avec des marqueurs `<|image|>`, `<|video|>`, `<|audio|>` dans le texte
- Prérequis — **bfloat16 ou float32, jamais float16** : la plage d'activation dépasse celle du float16, le modèle renvoie des NaN ou des vecteurs dégradés sans lever d'erreur ; préfixes de tâche pour le texte seulement (`task: search result | query: …` côté requête, `title: … | text: …` côté document), les images, la vidéo et l'audio sans préfixe
- Exécution — local ; Google vise les appareils et les ordinateurs portables ; la génération de la réponse reste à héberger à part
- Coût — gratuit sous Apache-2.0 ; le coût est celui du calcul

## Limites à connaître

- **Scores d'un seul éditeur.** MTEB multilingue v2 61,36, MTEB code 78,68 (68,76 pour la v1), MMEB v2 global 59,01 (image 57,28, documents visuels 67,84, vidéo 50,67), audio MSEB 69,54 : tous publiés par Google sur la carte. Qwen publie 77,8 pour Qwen3-VL-Embedding-8B sur MMEB-V2, mais les protocoles ne sont pas prouvés identiques et les tailles diffèrent : **aucune conclusion de classement**.
- **Dérive à la troncature** : sauter la renormalisation après une troncature dégrade le classement sans erreur ; requête et corpus partagent la même dimension.
- **Licence : à lire deux fois.** La carte et son en-tête disent Apache-2.0, et la page de licence liée (« Gemma 4 license ») est le texte de l'Apache 2.0 ; le dépôt Hugging Face ne contient pas de fichier de licence séparé, et la page de licence ne nomme pas EmbeddingGemma 2. La politique d'usage interdit de Gemma est liée depuis cette page : son articulation avec l'Apache-2.0 n'est pas expliquée.
- **Maturité** : sorti il y a moins de quinze jours à la lecture du 2026-10-20, sans évaluation indépendante trouvée.
- **Un embedding ne restitue pas le texte d'une image** : pour citer, il faut un OCR ou un modèle de lecture en aval.

## Écosystème

### Alternatives

- [[Qwen3-VL-Embedding]] — Famille de modèles d'embedding multimodaux d'Alibaba (Apache-2.0, 2 B et 8 B) — texte, images, captures d'écran et vidéo dans un même espace, 32K tokens, dimension réglable, instructions de tâche ; pas d'audio. — l'autre modèle multimodal ouvert à contexte long, plus gros (2 B et 8 B), sans l'audio.
- [[SigLIP 2]] — Famille d'encodeurs image-texte de Google (Apache-2.0) — un encodeur d'image et un encodeur de texte alignés, multilingues, pour la classification d'images à zéro exemple et la recherche image-texte. — image et texte seulement, sans vidéo ni audio ; deux encodeurs plutôt qu'un modèle texte partagé.
- voisin : [[bge-m3]] et [[Qwen3-Embedding]] — les modèles texte ouverts du dossier, à prendre quand aucune autre modalité n'est en jeu.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/google/embeddinggemma-2
- Article — annonce de Google, 2026-10-06 : https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2
- Vidéo — « C'est quoi le RAG multimodal ? Et l'intérêt derrière ? », Benoit Ferrere, 2 min 29 : https://www.youtube.com/watch?v=FbHEm1wgjEE

## Voir aussi

- [[Embedding multimodal et modality gap]] — la notion : espace commun, écart entre modalités, limites
- [[Choisir un modèle d'embedding]] — critères de choix et limites des classements
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[Licences de modèles open weights]] — lire la licence de la version qu'on déploie
