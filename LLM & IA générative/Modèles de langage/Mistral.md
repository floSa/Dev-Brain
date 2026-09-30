---
role: brique
nom: Mistral
alias: [Mistral AI, Mistral Small, Ministral, Ministral 3, Devstral, Magistral, Mistral Medium]
pitch: "Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Qwen]]", "[[Gemma]]", "[[gpt-oss]]"]
complements: ["[[vLLM]]", "[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]"]
tags: [llm, local-llm, reasoning, tool-use, vision-language]
url_docs: https://docs.mistral.ai/models/overview
url_repo: https://github.com/mistralai/mistral-common
---

# Mistral

<!-- AUTO:BANDEAU:START -->
> Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Les modèles de Mistral AI dont les poids sont téléchargeables sur Hugging Face (organisation `mistralai`). Ce n'est pas une famille à licence unique : la licence se lit **dépôt par dépôt**. Lue le 2026-09-30 dans les métadonnées et les fichiers des dépôts, elle vaut Apache-2.0 pour **Mistral Small 4** (119 B MoE, 6,5 B actifs, 128 experts dont 4 actifs, 256k), **Ministral 3** (3, 8 et 14 B, Base, Instruct et Reasoning, vision, 256k, 2025-10-31), **Devstral Small 2** (24 B, 2025-11-28) et Mistral Large 3 (675 B). Elle vaut « MIT modifié » pour **Mistral Medium 3.5** (128 B dense) et **Devstral 2** (123 B). Le raisonnement s'active par requête avec `reasoning_effort` (`none` ou `high`) sur Small 4, et par le prompt système sur les Ministral 3 Reasoning. Les cartes citent le français. Ministral 3 14B Instruct compte 307 732 téléchargements sur trente jours le 2026-09-30, Small 4 en compte 51 706.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le **français** compte et l'éditeur le cite sur ses cartes (Small 4, Ministral 3, Medium 3.5) | Le **chiffre d'affaires mensuel** consolidé de l'ESN ou de son employeur dépasse 20 M$ et le modèle est **Medium 3.5 ou Devstral 2** : aucun droit accordé sans licence commerciale |
| Un modèle **Apache-2.0 de 3 à 24 B** sur un GPU unique : Ministral 3 14B (24 Go en FP8 selon sa carte), Devstral Small 2 (une RTX 4090 selon sa carte) | **Mistral Small 4** sur un GPU unique : 120,9 Go de poids, hors de portée d'un GPU de 80 Go ; NVFP4 officiel de 70,8 Go → [[gpt-oss]] ou [[Gemma]] |
| Des **GGUF officiels** (Ministral 3) pour [[llama.cpp]], [[Ollama]] et [[LM Studio]] | Une fiche **Ollama** pour Small 4 : la page `mistral-small4` n'existe pas à la date de lecture |
| Un modèle de **code agentique** ouvert à taille raisonnable → Devstral Small 2 | Un **mode pensée** déjà rôdé chez l'éditeur : Magistral est listé comme déprécié côté API, ses poids restent en ligne |

## Mise en œuvre

- Installation — `uv pip install vllm` et la bibliothèque `mistral_common` (1.11 ou plus pour Small 4 d'après sa carte)
- Point d'entrée — vLLM, recommandé par la carte de Small 4, avec `--tool-call-parser mistral` et `--reasoning-parser mistral`
- Prérequis — pour Ministral 3 et Devstral 2 : le mode `mistral` du tokenizer (`--tokenizer_mode mistral`) ; pour Small 4 : un nœud multi-GPU ; aucune VRAM n'est chiffrée sur sa carte
- Exécution — Ministral 3 14B tient en 24 Go en FP8, le 3 B et le 8 B plus bas ; Devstral Small 2 sur une carte de 24 Go ; Small 4, Medium 3.5 et Large 3 sur plusieurs GPU
- Coût — gratuit en Apache-2.0 ; Medium 3.5 et Devstral 2 exigent une licence commerciale de Mistral AI au-delà du seuil

## Limites à connaître

- **Deux régimes de licence, un seul nom de famille.** Apache-2.0 : Small 4, Ministral 3, Devstral Small 2, Large 3, Magistral Small 2507 et 2509. **MIT modifié** (`license: other`, fichier `LICENSE` lu) : Medium 3.5 et Devstral 2. Plus anciens, en `license: other` dont le texte n'a pas été lu : Mistral Large 2407 et 2411, Mistral Small 2409, Ministral 8B 2410, Pixtral Large.
- **La clause du MIT modifié** : aucun droit si le chiffre d'affaires mensuel consolidé mondial de « votre société (ou de votre employeur) » dépasse 20 M$ le mois précédent. Elle vise aussi les dérivés, modifications et œuvres combinées, **y compris ceux qu'un tiers a produits**. Au-delà : licence commerciale à la discrétion de Mistral AI, ou API de l'éditeur. Une ESN de taille moyenne peut donc la dépasser, et le client aussi selon qui exerce les droits — lecture du texte, **pas un avis juridique** ; voir [[Licences de modèles open weights]].
- **Small 4 n'a pas de fichier `LICENSE`** dans son dépôt : l'Apache-2.0 figure dans le frontmatter et la carte seulement.
- **Modèles fermés** : Codestral 25.08, OCR, Embed et Moderation sont dans la catégorie « Premier » de la documentation, sans poids.
- **Ollama** : `ministral-3` (version 0.13.1 ou plus d'après la bibliothèque), `devstral-small-2` et `mistral-medium-3.5` existent ; `mistral-small4` renvoie une erreur 404.
- **Aucun score repris** : la carte de Small 4 place ses chiffres dans des images.

## Écosystème

### Alternatives

- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo. — le catalogue le plus large (petites tailles en Qwen3.5), mais une clause « Model as a Service » sur Flash-Next et le 2,4 T.
- [[Gemma]] — Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use. — Apache-2.0 sur Gemma 4 sans seuil de revenu, avec la VRAM chiffrée par l'éditeur ; français non nommé.
- [[gpt-oss]] — Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire. — Apache-2.0 sans seuil, du 20 B (16 Go) au 120 B (80 Go) ; texte seul et français non cité.

### Compléments

- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — recommandé par la carte de Small 4, avec les parseurs `mistral`.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage. — `ministral-3`, `devstral-small-2` et `mistral-medium-3.5` existent ; `mistral-small4` n'existe pas à la date de lecture.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux. — GGUF officiels de Ministral 3 ; la carte de Small 4 renvoie vers des GGUF tiers d'Unsloth.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit. — la carte de Devstral Small 2 remercie les équipes LM Studio et Ollama pour le support.

## Ressources

- Documentation — modèles : https://docs.mistral.ai/models/overview
- Dépôt — bibliothèque de tokenisation requise par vLLM : https://github.com/mistralai/mistral-common

## Voir aussi

- [[Licences de modèles open weights]] — la notion : le seuil de revenu d'un MIT modifié, parmi les clauses à lire avant de livrer
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Reasoning models]] — `reasoning_effort` et les variantes Reasoning
- [[Small Language Models]] — Ministral 3, de 3 à 14 B
