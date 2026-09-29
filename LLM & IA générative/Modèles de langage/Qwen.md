---
role: brique
nom: Qwen
alias: [Qwen3.8, Qwen3.6, Qwen3.5, Qwen3.8-27B, Qwen3 LLM, Tongyi Qianwen]
pitch: "Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Mistral]]", "[[Gemma]]", "[[gpt-oss]]"]
complements: ["[[vLLM]]", "[[SGLang]]", "[[Ollama]]", "[[llama.cpp]]", "[[Unsloth]]", "[[LLaMA-Factory]]", "[[Qwen3-Embedding]]"]
tags: [llm, local-llm, reasoning, tool-use, vision-language]
url_docs: https://huggingface.co/Qwen/Qwen3.8-27B
url_repo: https://github.com/QwenLM/Qwen3.8
---

# Qwen

<!-- AUTO:BANDEAU:START -->
> Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Famille de modèles de langage de l'équipe Qwen d'Alibaba, publiée en poids ouverts sur Hugging Face (organisation `Qwen`). La génération lue le 2026-09-30 est **Qwen3.8**, en trois modèles : un **27 B dense** à entrée image et vidéo (dépôt créé le 2026-08-05, Apache-2.0), **Flash-Next** (MoE de 125 B dont 6 B actifs, 2026-08-24) et un MoE de **2,4 T** dont 95 B actifs (2026-08-08). Ces deux derniers ne sont **plus** sous Apache-2.0 : ils portent des licences propres à clause « Model as a Service » (voir *Limites*). Contexte natif de 262 144 tokens, extensible à 1 M avec YaRN, statique donc susceptible de dégrader les textes courts. Le mode pensée est actif par défaut et se règle par requête (`reasoning_effort`). Les petites tailles (0,8 à 9 B) n'existent que dans **Qwen3.5**, tout Apache-2.0. Le 27 B compte 7 038 259 téléchargements sur trente jours et 16 635 mentions « j'aime » le 2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un modèle **Apache-2.0** hébergeable, redistribuable, finetunable et livrable sans condition : le 27 B de Qwen3.8 et toute la génération Qwen3.5 et 3.6 | Le modèle visé est **Flash-Next ou le 2,4 T** et l'endpoint est exposé à un client : clause « Model as a Service » de la Qwen Community License 1.0 → [[gpt-oss]] ou [[Gemma]], sous Apache-2.0 |
| Un modèle **dense multimodal** (texte, image, vidéo) sur un seul GPU : FP8 officiel de 30,9 Go | Le **français** doit être garanti par l'éditeur : la carte du 27 B ne liste aucune langue → [[Mistral]], dont les cartes citent le français |
| Le **mode pensée** et l'**appel d'outils** réglables par requête, avec des parseurs vLLM dédiés | Une **VRAM exigée** par l'éditeur : aucune carte Qwen3.8 n'en annonce |
| De **petites tailles** pour un poste ou un nœud modeste (0,8 à 9 B) → Qwen3.5 | Un GGUF **officiel** : les conversions llama.cpp de la génération viennent de tiers ou de `ggml-org` |

## Mise en œuvre

- Installation — `uv pip install vllm` (la recette vLLM du 27 B demande la version 0.17 ou plus, lue via un résumé), ou `ollama pull qwen3.8:27b`
- Point d'entrée — `vllm serve Qwen/Qwen3.8-27B` ; les cartes Qwen3.5 et 3.6 donnent `--reasoning-parser qwen3` et `--tool-call-parser qwen3_coder`, celle du 27 B ne donne pas de commande de service hors contexte long
- Prérequis — un GPU : le dépôt pèse 55,6 Go en BF16 et 30,9 Go en FP8 (quantification officielle) ; aucune VRAM n'est annoncée par l'éditeur
- Exécution — un nœud GPU pour le 27 B ; Flash-Next (185,6 Go en FP8) et le 2,4 T (2,5 To) dépassent un nœud modeste
- Coût — gratuit, Apache-2.0 pour le 27 B ; licence Qwen Community License 1.0 pour Flash-Next, Qwen3.8-Max License pour le 2,4 T

## Limites à connaître

- **Trois modèles, trois licences** dans une même génération, lues dans le fichier `LICENSE` de chaque dépôt le 2026-09-30 : 27 B en Apache-2.0 ; Flash-Next en **Qwen Community License 1.0** ; 2,4 T en **Qwen3.8-Max License**. Un identifiant de famille ne dit donc pas la licence : lire celle du dépôt.
- **Qwen Community License 1.0** : usage, hébergement, finetuning et vente permis, sous deux conditions. Afficher le nom du modèle si un produit dépasse 100 M d'utilisateurs actifs mensuels ou 20 M$ de revenu mensuel. Et obtenir une **licence séparée de Qwen** pour tout usage commercial si le licencié ou ses affiliés exercent une activité « Model as a Service » — donner à un tiers accès à l'inférence ou au fine-tuning, par API ou endpoint hébergé, avec un contrôle réel sur les entrées, paramètres ou données d'entraînement. L'usage interne qui n'expose ni le modèle ni ses sorties à un tiers est exclu. La Max License reprend ces conditions, avec un seuil de 50 M$ de revenu sur douze mois pour la clause de service.
- **Pour une ESN** : avec le 27 B, tout est permis. Avec Flash-Next, héberger un endpoint pour un client peut relever de la clause de service : lecture du texte, **pas un avis juridique** — voir [[Licences de modèles open weights]].
- **Le français n'est pas nommé** sur les cartes Qwen3.8 lues. Seule la carte de Qwen3.5-9B annonce « 201 langues et dialectes ». Non mesuré ici.
- **Les GGUF** de Qwen3.8 ne sont pas publiés par l'éditeur : le dépôt `ggml-org/Qwen3.8-27B-GGUF` (Apache-2.0) est une conversion automatique. Le dernier GGUF publié par l'organisation `Qwen` est `Qwen3-Coder-Next-GGUF` (2026-02-02).
- **Aucun score repris** : les tableaux de la carte utilisent un harnais d'agent de code propre à l'éditeur et des cellules HTML non recoupées.

## Écosystème

### Alternatives

- [[Mistral]] — Modèles ouverts de Mistral AI — Small 4 (119 B MoE), Ministral 3 (3, 8, 14 B) et Devstral Small 2 en Apache-2.0 ; Medium 3.5 et Devstral 2 sous MIT modifié, exclu au-delà de 20 M$ de revenu mensuel ; 256k tokens, français cité, outils et raisonnement. — le français cité et des tailles de 3 à 24 B en Apache-2.0, mais un MIT modifié plafonné à 20 M$ de revenu mensuel sur Medium 3.5.
- [[Gemma]] — Modèles de langage ouverts de Google DeepMind — Gemma 4 (E2B à 31 B, dont un MoE de 26 B) en Apache-2.0, dépôts sans accès sur demande ; 128K à 256K tokens, image et audio, appel de fonctions et mode pensée ; la génération précédente reste sous Gemma Terms of Use. — Apache-2.0 sur toute la génération 4 et un QAT 4 bits officiel, là où Qwen mêle Apache-2.0 et licences propres dans une génération.
- [[gpt-oss]] — Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire. — Apache-2.0 sans seuil, sur un GPU de 80 Go ou dans 16 Go, mais texte seul et sans langue citée.

### Compléments

- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — sert le 27 B ; les cartes de Qwen3.5 et 3.6 donnent les parseurs `qwen3` et `qwen3_coder`.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS. — cité avec vLLM par la carte du 27 B, qui donne la commande de contexte long pour SGLang.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage. — la bibliothèque propose `qwen3.8`, tag `27b`.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux. — conversion GGUF du 27 B par `ggml-org`, non publiée par l'éditeur ; le README de Qwen3.8 cite llama.cpp.
- [[Unsloth]] — Fine-tuning de LLM ~2× plus rapide avec 70-80 % de VRAM en moins via des kernels Triton sur mesure — LoRA/QLoRA et GRPO sur un seul GPU grand public, sans perte de précision. — cité par le README du dépôt Qwen3.8.
- [[LLaMA-Factory]] — Plateforme unifiée de fine-tuning de 100+ LLM/VLM — SFT, DPO, PPO, KTO en LoRA/QLoRA, pilotable en CLI, YAML ou interface web (LLaMA Board), zéro code requis. — cité par le README du dépôt Qwen3.8.
- [[Qwen3-Embedding]] — Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche. — le modèle d'embedding de la même équipe, pour le RAG autour du modèle de génération.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/Qwen/Qwen3.8-27B
- Dépôt — https://github.com/QwenLM/Qwen3.8

## Voir aussi

- [[Licences de modèles open weights]] — la notion : licences OSI contre licences d'éditeur, et ce qu'elles permettent avant de livrer
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Reasoning models]] — ce que le mode pensée dépense à l'inférence
- [[Vision Language Models]] — le 27 B branche un encodeur visuel sur un LLM
- [[Small Language Models]] — les petites tailles de Qwen3.5
- [[Contexte long]] — le coût du cache KV et ce que valent les longueurs annoncées
- [[Quantification des LLM - GGUF, AWQ, GPTQ]] — formats quantifiés, matériel et pièges pour servir ce modèle
