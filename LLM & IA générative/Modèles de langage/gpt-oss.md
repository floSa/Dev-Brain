---
role: brique
nom: gpt-oss
alias: [gpt-oss-20b, gpt-oss-120b, OpenAI gpt-oss, GPT OSS]
pitch: "Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Qwen]]", "[[Mistral]]", "[[Gemma]]"]
complements: ["[[vLLM]]", "[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]"]
tags: [llm, local-llm, reasoning, tool-use]
url_docs: https://huggingface.co/openai/gpt-oss-120b
url_repo: https://github.com/openai/gpt-oss
---

# gpt-oss

<!-- AUTO:BANDEAU:START -->
> Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Les deux modèles à poids ouverts d'OpenAI, dépôts Hugging Face créés le 2025-08-04 (dernière modification le 2025-08-26). **gpt-oss-120b** : 117 B de paramètres dont 5,1 B actifs, environ 65 Go. **gpt-oss-20b** : 21 B dont 3,6 B actifs, 13,8 Go. Les poids des experts sont post-entraînés en **MXFP4** : c'est le format natif, pas une quantification ajoutée. Contexte de 131 072 positions. Le niveau de raisonnement (low, medium, high) se règle dans le prompt système (« Reasoning: high »), la chaîne de pensée est exposée, l'appel d'outils est natif, et le modèle prend en charge la navigation web et l'exécution Python dans son format de conversation **harmony**, obligatoire. Texte seul. Aucune génération plus récente n'a été trouvée le 2026-09-30 : la liste des modèles de l'organisation `openai` ne montre, après août 2025, que des modèles de sécurité et de filtrage. Le 20 B compte 6 750 574 téléchargements sur trente jours et 5 109 mentions « j'aime » le 2026-09-30, le 120 B 4 453 393 et 5 332.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une licence **Apache-2.0** et une politique d'usage d'une phrase (respecter les lois applicables) : héberger, redistribuer, finetuner, livrer | Le **français** doit être garanti : la carte ne mentionne aucune langue → [[Mistral]] |
| Un modèle de **raisonnement** sur un GPU de 80 Go (120 B) ou dans 16 Go de mémoire (20 B), sans conversion | De l'**image ou de l'audio** en entrée : texte seul → [[Gemma]] ou [[Qwen]] |
| Un support **Ollama**, **LM Studio** (cités par le README du dépôt) et **llama.cpp** (GGUF publié par `ggml-org`, Apache-2.0) | Un modèle **récent** : aucune mise à jour des poids depuis 2025-08-26 |
| Des **outils** et un raisonnement réglables sans changer de modèle | Un **format de conversation libre** : harmony est obligatoire, le modèle est à servir par un moteur qui l'applique |

## Mise en œuvre

- Installation — `uv pip install --pre vllm==0.10.1+gptoss` d'après le README du dépôt (une version plus récente de vLLM peut l'avoir intégré, non vérifié), ou `ollama pull gpt-oss:20b`
- Point d'entrée — `vllm serve openai/gpt-oss-20b`, serveur compatible OpenAI
- Prérequis — un GPU : 80 Go pour le 120 B, 16 Go pour le 20 B, chiffres de l'éditeur sur la carte
- Exécution — un seul GPU par modèle ; le support de vLLM pour l'architecture `GptOssForCausalLM` figure dans sa documentation des modèles pris en charge
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Licence** : fichier `LICENSE` en Apache-2.0 standard ; fichier `USAGE_POLICY` d'une phrase (respecter les lois applicables), absent des métadonnées de licence. Aucun seuil de revenu ou d'utilisateurs, aucune interdiction d'entraîner d'autres modèles avec les sorties : lecture des fichiers le 2026-09-30.
- **Le français n'est pas cité** sur la carte, qui ne mentionne aucune langue ni la multimodalité.
- **Date de sortie** : la date du 5 août 2025 donnée par l'éditeur n'a pas pu être relue (la page d'annonce renvoie 403) ; seules les dates de dépôt sont relevées.
- **Le dernier tag GitHub** est v0.0.9 (2025-09-29) : le dépôt est un support de référence, peu actif.
- **Aucun score repris** : aucun n'a été relu à la source.

## Écosystème

### Alternatives

- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo. — image et vidéo en entrée et un 27 B dense en Apache-2.0, mais des licences propres sur les gros modèles.
- [[Mistral]] — Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement. — le français cité et des modèles de 3 à 24 B en Apache-2.0, mais un MIT modifié sur Medium 3.5.
- [[Gemma]] — Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use. — image et audio en entrée, Apache-2.0 depuis Gemma 4, et des tailles de 2 à 31 B.

### Compléments

- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — le README du dépôt donne `vllm serve openai/gpt-oss-20b` et une version dédiée `0.10.1+gptoss`.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage. — tags `gpt-oss:20b` et `gpt-oss:120b`, cités par le README du dépôt.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux. — GGUF `ggml-org/gpt-oss-120b-GGUF` (Apache-2.0).
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit. — cité par le README du dépôt et par la carte.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/openai/gpt-oss-120b
- Dépôt — https://github.com/openai/gpt-oss

## Voir aussi

- [[Licences de modèles open weights]] — la notion : une licence sans seuil ni clause d'usage, l'autre extrémité de l'échelle
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Reasoning models]] — trois niveaux de raisonnement dans le prompt système
