---
role: brique
nom: Gemma
alias: [Gemma 4, Gemma 3, Google Gemma, Gemma-4-31B-it]
pitch: "Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Qwen]]", "[[Mistral]]", "[[gpt-oss]]"]
complements: ["[[vLLM]]", "[[SGLang]]", "[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[Unsloth]]", "[[TRL]]"]
tags: [llm, local-llm, reasoning, tool-use, vision-language]
url_docs: https://ai.google.dev/gemma/docs
url_repo: https://github.com/google-deepmind/gemma
---

# Gemma

<!-- AUTO:BANDEAU:START -->
> Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Les modèles de langage ouverts de Google DeepMind. La génération lue le 2026-09-30 est **Gemma 4**, dont la page des versions de Google date la sortie du 31 mars 2026 (les dépôts Hugging Face sont créés du 2 au 11 mars, le 12 B le 2026-05-23). Cinq tailles : **E2B** et **E4B** (contexte 128K, image et audio), **12 B** (256K, image et audio), **26 B A4B** (MoE de 25,2 B dont 3,8 B actifs, 256K, image) et **31 B dense** (256K, image). Elle est publiée sous **Apache-2.0**, sans accès sur demande : c'est un changement par rapport à Gemma 1 à 3, soumis aux Gemma Terms of Use. Appel de fonctions natif, mode pensée configurable, prise en charge annoncée de plus de 35 langues (entraînement sur plus de 140). Le 31 B compte 9 904 107 téléchargements sur trente jours et 3 976 mentions « j'aime » le 2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une licence **Apache-2.0** sans seuil ni politique d'usage incorporée : héberger, redistribuer, finetuner, livrer | La génération visée est **Gemma 3 ou antérieure** : Gemma Terms of Use, dépôts à accès manuel, politique d'usage incorporée → Gemma 4, ou [[Qwen]] en Apache-2.0 |
| Un **QAT officiel en 4 bits** : le 31 B pèse 17,65 Go en GGUF q4_0, le 26 B A4B 14,44 Go, le 12 B 6,98 Go | De l'**audio** avec un gros modèle : il n'est pris en charge que par E2B, E4B et le 12 B |
| De l'**audio en entrée** sur un petit modèle (E2B, E4B, 12 B, 30 s au plus) | Le **français nommé** par l'éditeur : la carte dit « 35+ langues » sans le citer → [[Mistral]] |
| Un **MoE à 3,8 B actifs sur 25,2 B** (26 B A4B) : 14,44 Go en GGUF q4_0 officiel | Un **4 bits** sur le 26 B A4B avec vLLM : la recette le déconseille et propose l'int8 par canal |

## Mise en œuvre

- Installation — `uv pip install vllm`, ou `ollama pull gemma4` (tags `e2b`, `e4b`, `12b`, `26b`, `31b`), ou `llama-cli -hf ggml-org/gemma-4-E2B-it-GGUF`
- Point d'entrée — `vllm serve google/gemma-4-31B-it` avec `--tool-call-parser gemma4` et `--reasoning-parser gemma4` (recette vLLM)
- Prérequis — la VRAM chiffrée par l'éditeur, poids seuls avec 20 % de marge, hors cache KV : 31 B, 69,9 Go en BF16, 34,9 Go en SFP8, 17,5 Go en Q4_0 ; 26 B A4B, 57,7 / 28,8 / 14,4 Go ; 12 B, 26,7 / 13,4 / 6,7 Go ; E4B, 17,9 / 8,9 / 4,5 Go ; E2B, 11,4 / 5,7 / 2,9 Go
- Exécution — un GPU de 80 Go en BF16 pour le 31 B et le 26 B A4B (recette vLLM), ou 17,5 Go de poids en Q4_0 pour le 31 B, cache KV en plus
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Deux régimes de licence selon la génération.** Gemma 4 : Apache-2.0, `license: apache-2.0` dans les métadonnées, lien vers la page « Gemma 4 license » de Google qui redirige vers le texte Apache standard ; aucun fichier `LICENSE` dans les dépôts. Gemma 3 : `license: gemma`, accès manuel. Les Gemma Terms of Use (modifiées le 1er avril 2026) renvoient pour Gemma 4 à sa propre licence.
- **Ce que les Gemma Terms imposaient et que Gemma 4 n'impose plus** : la politique d'usage interdit incorporée par référence, la répercussion des restrictions dans tout accord de distribution, le droit de Google de restreindre l'usage « à distance ou autrement », et la résiliation avec suppression des copies. La page de la politique d'usage existe toujours ; aucun texte lu ne dit qu'elle s'applique encore à Gemma 4.
- **Date de sortie ambiguë** : page des versions de Google, 31 mars 2026 ; billet de blog, 2 avril 2026 ; dépôts créés plus tôt.
- **Le français n'est pas nommé** sur la carte : « plus de 35 langues » et un score MMLU multilingue.
- **Aucun chiffre de benchmark repris** : la carte en publie pour le 31 B, le 26 B A4B et le 12 B ; non recoupés hors de la carte.

## Écosystème

### Alternatives

- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo. — un catalogue plus large, mais trois licences dans la génération Qwen3.8.
- [[Mistral]] — Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement. — le français cité par l'éditeur, mais un MIT modifié à 20 M$ de revenu mensuel sur Medium 3.5.
- [[gpt-oss]] — Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire. — deux modèles Apache-2.0 sans seuil, mais texte seul et sans mise à jour depuis août 2025.

### Compléments

- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — recette dédiée, parseurs `gemma4`.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS. — cité par la page des modèles de la documentation Gemma.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage. — `gemma4` : tags `e2b`, `e4b`, `12b`, `26b`, `31b`.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux. — GGUF q4_0 QAT publiés par Google, et `ggml-org/gemma-4-E2B-it-GGUF` cité par la documentation.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit. — cité par la page des modèles de la documentation Gemma.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision. — cité par la documentation Gemma.
- [[TRL]] — Bibliothèque de post-training de Hugging Face — trainers prêts à l'emploi (SFT, reward modeling, DPO, GRPO, PPO) au-dessus de Transformers ; la brique de référence pour fine-tuner et aligner un LLM par code. — la documentation Gemma décrit un finetuning complet avec Hugging Face TRL.

## Ressources

- Documentation — https://ai.google.dev/gemma/docs
- Dépôt — https://github.com/google-deepmind/gemma

## Voir aussi

- [[Licences de modèles open weights]] — la notion : pourquoi la génération du modèle change la licence, avec Gemma en exemple
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Small Language Models]] — E2B, E4B et le 12 B
- [[Vision Language Models]] — l'image en entrée pour toutes les tailles
- [[Reasoning models]] — le mode pensée configurable
