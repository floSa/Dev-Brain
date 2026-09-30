---
role: brique
nom: Infinity
alias: [infinity-emb, michaelfeil infinity, Infinity embeddings]
pitch: "Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique."
categorie: ml/embeddings
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Text Embeddings Inference]]", "[[sentence-transformers]]", "[[FastEmbed]]"]
complements: []
tags: [embeddings, model-serving, inference, semantic-search, reranking, self-hosted]
url_docs: https://michaelfeil.eu/infinity/
url_repo: https://github.com/michaelfeil/infinity
---

# Infinity

<!-- AUTO:BANDEAU:START -->
> Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un serveur REST en Python (FastAPI) pour servir des embeddings de texte, des rerankers, de
la classification, et aussi **CLIP, CLAP et ColPali** : l'étendue est ce qui le distingue
de [[Text Embeddings Inference]]. Plusieurs modèles peuvent tourner dans une même instance,
derrière une clé d'API, avec un batching dynamique. Le moteur se choisit : PyTorch, optimum
(ONNX, TensorRT) ou CTranslate2 pour BERT, sur CUDA, ROCm, CPU, AWS Inferentia ou MPS ;
une quantification int8 et fp8 existe, marquée expérimentale. ColBERT sort en embeddings de
token encodés en base64 ; ColPali n'est pris qu'en modèles fusionnés, pas en adaptateurs
LoRA. Le dépôt est celui d'une seule personne : **une version en douze mois** (0.0.77, le
2025-08-22), un dernier commit le 2026-03-24, environ 2 950 étoiles le 2026-09-30, et des
tickets ouverts sur des dépendances qui ont bougé (optimum 2.0, transformers 5).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Servir **ColBERT, ColPali, CLIP ou CLAP**, que [[Text Embeddings Inference]] n'annonce pas | Un support dans la durée : mainteneur unique, une release en douze mois → [[Text Embeddings Inference]] |
| **Plusieurs modèles** sur une même instance, derrière une clé d'API | Une compatibilité stricte avec l'API OpenAI : un ticket ouvert (#541) signale des écarts |
| Backend **AMD, Inferentia**, ou CPU en ONNX int8 | Un environnement sur transformers 5 : non supporté à ce jour (#657) |
| Licence MIT, image Docker prête | La télémétrie ne peut pas être coupée : elle est **active par défaut** (arguments CLI, OS, GPU et processeur) |
| Pouvoir **figer l'image et la version** | Un simple encodage en batch : [[sentence-transformers]] en process |

## Mise en œuvre

- Installation — `uv add "infinity-emb[all]"` (extras `torch`, `optimum`, `ct2`, `server`) ; ou l'image `michaelf34/infinity`
- Point d'entrée — serveur : `docker run --gpus all -p $port:$port -v $volume:/app/.cache michaelf34/infinity:latest v2 --model-id $model --port $port`, API de type OpenAI
- Prérequis — un modèle au format supporté ; le README teste sous Python 3.11 ; **`INFINITY_ANONYMOUS_USAGE_STATS=0` ou `DO_NOT_TRACK=1`** pour couper la télémétrie, à poser systématiquement en on-prem
- Exécution — un processus ; hors-ligne par un répertoire monté et `--model-id /models/…`
- Coût — gratuit, MIT

## Limites à connaître

- **Comparatif de débit daté.** Le seul que l'auteur publie oppose Infinity 0.0.25 à TEI 0.6 : les versions ne sont plus celles d'aujourd'hui, et la ligne PyTorch sur CPU y est marquée « needs revision ». À ne pas reprendre comme mesure.
- **Adoption déclarée par l'auteur.** Baseten, RunPod, SAP AI Core sont cités au README ; aucun de ces usages n'a été vérifié. Mesures relevées : 5 574 téléchargements PyPI sur le dernier mois, environ 912 000 tirages Docker Hub.
- **Dérive de dépendances.** `optimum.bettertransformer` a disparu d'optimum 2.0 (tickets #649 et #656) : un environnement neuf peut casser.

## Écosystème

### Alternatives

- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — le serveur de référence, maintenu par Hugging Face ; sans ColBERT ni CLIP.
- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — la voie en process, sans serveur.
- [[FastEmbed]] — Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut. — le calcul en bibliothèque, sans service.

## Ressources

- Documentation — https://michaelfeil.eu/infinity/
- Dépôt — https://github.com/michaelfeil/infinity
- Documentation — la télémétrie : https://github.com/michaelfeil/infinity/blob/main/docs/docs/telemetry.md

## Voir aussi

- [[Choisir un modèle d'embedding]] — la notion : quel modèle servir, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[Serving]] — le domaine du serving de modèles, dont ce serveur est le cas spécialisé aux embeddings
