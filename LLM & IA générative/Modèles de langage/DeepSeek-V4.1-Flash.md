---
role: brique
nom: DeepSeek-V4.1-Flash
alias: [DeepSeek V4.1 Flash, deepseek-flash, DeepSeek-V4.1, DeepSeek Flash, CSA2]
pitch: "Modèle de langage à poids ouverts de DeepSeek-AI (MIT, MoE de 552 B dont 8 B actifs au prefill et 16 B au décodage) — contexte de 1 M de tokens, cache KV de 890 octets par token, effort de raisonnement réglable de 1 à 100 ; checkpoint de 510 Go, donc un nœud multi-GPU."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
alternatives: ["[[gpt-oss]]", "[[Qwen]]"]
tags: [llm, local-llm, reasoning, tool-use]
url_docs: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
url_repo: 
---

# DeepSeek-V4.1-Flash

<!-- AUTO:BANDEAU:START -->
> Modèle de langage à poids ouverts de DeepSeek-AI (MIT, MoE de 552 B dont 8 B actifs au prefill et 16 B au décodage) — contexte de 1 M de tokens, cache KV de 890 octets par token, effort de raisonnement réglable de 1 à 100 ; checkpoint de 510 Go, donc un nœud multi-GPU.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Modèle de langage à poids ouverts de DeepSeek-AI, dépôt Hugging Face `deepseek-ai/DeepSeek-V4.1-Flash` créé le 2026-09-10, modifié pour la dernière fois le 2026-10-16 (lecture du 2026-10-20). **Mixture of Experts** de 552 Md de paramètres de squelette, **8 Md actifs par token pendant le traitement du prompt** et **16 Md pendant la génération** (6 experts routés sur 384, plus un partagé, d'après le rapport technique). Contexte de **1 048 576 tokens**. Son trait distinctif est le **cache KV global de 890 octets par token**, obtenu par une attention éparse compressée (CSA2), une architecture encodeur-décodeur causale et un cache en FP4 : à un million de tokens, 0,89 Go au lieu de plusieurs centaines. L'effort de raisonnement se règle **en continu de 1 à 100** ; les scores d'éditeur sont mesurés à 100. La carte déclare une entrée image et texte. Poids en FP8 : 510,3 Go mesurés sur le dépôt (88 fichiers).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un **contexte très long servi à beaucoup de sessions** : 890 octets par token, soit environ 670 contextes d'un million de tokens en parallèle sur un nœud de 1 128 Go une fois les poids chargés (estimation, hors activations) | Un **seul GPU** ou un poste : 510 Go de poids, aucune VRAM annoncée par l'éditeur → [[gpt-oss]] (20 B dans 16 Go, 120 B sur 80 Go) |
| La licence **MIT**, sans seuil ni clause d'usage : héberger, redistribuer, finetuner, livrer | Une **qualité garantie à un million de tokens** : le rapport ne publie aucune mesure à cette longueur et reconnaît des erreurs de sélection possibles |
| Un effort de raisonnement **réglable en continu** pour arbitrer coût et précision | Le **coût par tâche** prime : le mode maximal consomme jusqu'à 2,5 fois plus de tokens, sans avantage établi sur la rédaction |
| Un nœud multi-GPU déjà disponible et des agents à contexte long | Un **moteur de serving documenté** : la carte ne donne aucune commande vLLM ou SGLang, ni gabarit Jinja → [[Qwen]] |

## Mise en œuvre

- Installation — poids sur Hugging Face ; la carte ne donne ni commande vLLM ni commande SGLang : elle renvoie aux dossiers `inference` (conversion des poids et inférence locale) et `encoding` (formatage des prompts) du dépôt
- Point d'entrée — pas de gabarit de conversation Jinja : utiliser l'implémentation de référence `encoding.py`, ou les bibliothèques Rust à liaisons Python `deepseek-recipe` (https://github.com/deepseek-ai/deepseek-recipe) pour convertir Messages, Chat Completions ou Responses en prompts du modèle et relire pensée, outils et images
- Prérequis — un nœud multi-GPU : 510,3 Go de poids en FP8 ; échantillonnage recommandé `temperature=1.0`, `top_p=0.95`, `max_tokens` d'au moins 256 K
- Exécution — hors d'un centre de données, hors de portée ; l'API hébergée de DeepSeek est un service payant, citée ici en texte simple et sans page
- Coût — gratuit, MIT (fichier `LICENSE`, « Copyright (c) 2023 DeepSeek », lu le 2026-10-20)

## Limites à connaître

- **Aucune mesure indépendante à un million de tokens.** Le seul banc long du rapport est LongBench-V2 (45,2 sur le modèle de base, contre 51,5 pour V4-Pro) ; la section Limites du rapport cite des erreurs de sélection de CSA2 et une reconstruction approximative de l'état de la fenêtre glissante en cas limite.
- **Le « 437 fois » compare à DeepSeek-V1**, un modèle dense de 67 Md de 2023 en bfloat16 (389 120 octets par token). D'une version à la suivante, le facteur honnête est **4**, dont la moitié vient du passage de FP8 à FP4. Les chiffres de compression sont de l'éditeur.
- **Verbosité** : 250 M de tokens de sortie pour l'indice d'Artificial Analysis, contre une médiane de 140 M, d'où un coût par tâche (0,27 $) près de quatre fois celui de GPT-6 Luna alors que les tarifs sont du même ordre ; indice de 39 sous v4.3.2 à effort maximal, relevé le 2026-09-23. Voir [[Tarif catalogue contre coût par tâche]].
- **Comptage de paramètres** : les métadonnées Safetensors de Hugging Face affichent 763 Md, le rapport 552 Md de squelette : le décompte du dépôt n'est pas le nombre de paramètres.
- **Aucun score d'éditeur repris** : le seul score cité est celui d'un tiers, daté.

## Écosystème

### Alternatives

- [[gpt-oss]] — Modèles ouverts d'OpenAI (Apache-2.0, 20 B et 120 B MoE en MXFP4) — 131 072 tokens, raisonnement à trois niveaux, appel d'outils ; le 20 B tient dans 16 Go, le 120 B sur un GPU de 80 Go ; texte seul, format harmony obligatoire. — Apache-2.0 sur un seul GPU, là où DeepSeek demande un nœud, mais 131 072 tokens au lieu d'un million.
- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo. — un 27 B dense en Apache-2.0 sur un GPU, mais un contexte natif de 262 144 tokens et une clause de service sur les gros modèles.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
- Rapport technique (PDF, 51 pages) : https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf

## Voir aussi

- [[Licences de modèles open weights]] — la notion : MIT sans seuil, l'autre extrémité de l'échelle des clauses
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Mixture of Experts]] — pourquoi les 16 Md actifs ne réduisent pas la mémoire : tous les experts restent chargés
- [[Contexte long]] — le coût du cache KV et ce que valent les longueurs annoncées
- [[Inference optimization]] — le cache KV et le batching côté serveur
- [[Quantization]] — le cache en FP4 est de l'arithmétique, pas de l'attention
- [[Tarif catalogue contre coût par tâche]] — un tarif d'API de 0,15 $ et 0,60 $ hors pointe (relevé du 2026-09-23) qui ne dit pas la facture
- [[Effort de raisonnement et courbe coût-qualité]] — le mode maximal ne rapporte rien sur la rédaction
- [[Lire un score publié]] — « 437 fois » : contre quoi, exactement
