---
role: notion
nom: Taille du cache KV par token
alias: [formule du cache KV, octets de cache par token, KV cache size, empreinte du cache KV, kappa, cache KV global, réduction du cache KV, compression du cache KV]
categorie: llm/runtime
domaines: [ai-eng, mlops, ml-eng]
tags: [inference-optimization, inference, llm, attention, gpu]
---

# Taille du cache KV par token

## Aperçu

- Le cache KV garde les clés et valeurs d'attention de chaque token déjà traité, pour ne pas les recalculer à chaque nouveau token. Sa taille **par token** (`κ`, en octets) est la seule grandeur qui compare des architectures entre elles sans dépendre de la longueur du contexte ni de la machine.
- Exemple chiffré : un modèle dense de 27 milliards de paramètres avec 16 couches d'attention, 4 têtes de clés-valeurs de 256 dimensions et un cache en bfloat16 stocke **64 Kio par token**, soit 16 Gio à 262 144 tokens. Le même modèle avec 64 couches d'attention et 24 têtes KV en stockerait 1,5 Mio par token : un facteur 48 sépare les deux.

## Concepts clés

### La formule

```
κ = 2 × L × n_kv × d_head × b      (octets par token)
KV(T) = κ × T
```

- `2` : une clé **et** une valeur par tête ; `L` : nombre de couches **qui stockent** un cache ; `n_kv` : têtes de clés-valeurs (pas les têtes de requête) ; `d_head` : dimension d'une tête ; `b` : octets par valeur (2 en bfloat16, 1 en FP8, 0,5 en FP4) ; `T` : longueur du contexte.
- Tout est multiplicatif : réduire `L`, `n_kv` ou `b` revient à multiplier les gains. `T` est le seul terme que l'utilisateur contrôle, et il n'a pas de plafond naturel.

### Les quatre leviers

| Levier | Ce qu'il change | Exemple |
|---|---|---|
| **Têtes partagées** (MQA, GQA) | `n_kv` plus petit que le nombre de têtes de requête | 24 têtes de requête, 4 têtes KV : cache ÷ 6 (GQA, Ainslie et al., 2023) |
| **Latent** ([[Multi-head Latent Attention]]) | un vecteur latent partagé au lieu d'une paire clé-valeur par tête | DeepSeek-V2 annonce 93,3 % de cache en moins face à DeepSeek 67B |
| **Couches qui stockent** ([[Architectures hybrides LLM]]) | `L` plus petit : des couches à état de taille fixe (attention linéaire), des couches qui réutilisent le cache d'une autre | 16 couches sur 64 : cache ÷ 4 ; 4 couches sur 40 qui écrivent un cache global |
| **Précision** ([[Quantization]]) | `b` plus petit : cache en FP8, en FP4 | FP8 : ÷ 2 ; FP4 (échelle comprise : 0,5625 octet par valeur) |

Une **fenêtre glissante** locale s'y ajoute parfois : son coût est borné par la taille de la fenêtre (128 tokens dans DeepSeek-V4.1-Flash), donc constant, mais non nul.

### Le terme fixe

Une couche à attention linéaire ne garde pas les tokens : chaque tête entretient une mémoire de taille fixe (une matrice 128 × 128, en float32 dans les modèles cités). La mémoire d'une conversation vaut alors `κ·T + S`. Pour le modèle de 27 Md : `S = 48 couches × 48 têtes × 128 × 128 × 4 octets = 144 Mio`, égal au cache à `T = S ÷ κ = 2 304` tokens. Contrepartie de l'état fixe : c'est un résumé avec perte, pas un enregistrement exact, et sa réutilisation par préfixe est plus délicate que celle d'un cache découpable en tranches de tokens (statut « expérimental » dans la documentation de vLLM relevée, avec des pages qui se contredisent).

### Ce que `κ` ne dit pas

- Un cache plus petit **ne dit rien de la qualité qu'il préserve**. Comparer 890 octets à 389 120 octets, c'est comparer un MoE de 552 Md de 2026 avec un modèle dense de 67 Md de 2023 ; le facteur additionne trois choses (couches, précision, structure). Pour juger un progrès d'une version à la suivante, le bon facteur est le plus petit (4), pas le plus grand (437).
- Le cache **global** ne dit pas le cache total : la fenêtre glissante locale s'ajoute, constante en `T`.
- Un cache petit ne rend pas le modèle léger : les poids restent à charger (cf. [[Dimensionner la mémoire d'un serveur LLM]]).

## Les maths, simplement

Quelques `κ` calculés avec la formule (octets par token) :

| Modèle (architecture) | `κ` | Précision | Cache à 1 M tokens |
|---|---:|---|---:|
| DeepSeek LLM 67B (GQA, 95 couches, 8 têtes KV, `d_head` 128) | 389 120 | bfloat16 | 389 Go |
| Même modèle en attention multi-tête (64 têtes KV) | 3 112 960 | bfloat16 | 3,11 To |
| Dense 27 Md, tout-attention (64 couches, 24 têtes KV) | 1 572 864 | bfloat16 | 1,6 To |
| Dense 27 Md, GQA 4 têtes, 64 couches | 262 144 | bfloat16 | 262 Go |
| Dense 27 Md hybride (16 couches, 4 têtes KV) | 65 536 | bfloat16 | 65 Go |
| Même hybride, cache FP8 | 32 768 | FP8 | 33 Go |
| MoE 396 Md hybride (15 couches, 2 têtes KV, `d_head` 256) | 30 720 | bfloat16 | 31 Go |
| DeepSeek-V4-Flash (génération précédente) | 3 514 | FP8 | 3,5 Go |
| DeepSeek-V4.1-Flash (cache global, latent, 4 couches qui écrivent) | 890 | FP4 | 0,89 Go |

- Décomposition du facteur 48 du modèle de 27 Md : GQA ÷ 6 (24 → 4 têtes), hybride ÷ 4 (64 → 16 couches), FP8 ÷ 2.
- Le facteur 437 de DeepSeek-V4.1-Flash : `389 120 ÷ 890 = 437,2`. Une reconstruction à partir des paramètres publiés (latent de 512 canaux, 2,5 entrées par token, FP4 avec échelle par bloc de 16, clés de l'indexeur de 128 canaux) donne 900 octets : l'ordre de grandeur et la structure du calcul sont bons, un détail de mise en page diffère de 1 %.
- Capacité : ce qui reste en mémoire divisé par `κ`. Avec 600 Go de reste sur un nœud de 8 GPU de 141 Go (poids de 510 Go déduits), environ 670 contextes d'un million de tokens à 890 octets, 170 à 3 514 octets, 1,5 à 389 120 octets (ordre de grandeur, activations et fragmentation ignorées).
- **Parallélisme de tenseurs** : si le nombre de GPU atteint ou dépasse le nombre de têtes KV, les têtes sont dupliquées et le cache du nœud est multiplié d'autant (cf. [[Parallélisme en inférence]]).

## En pratique

- Lire `num_hidden_layers`, `num_key_value_heads`, `head_dim` et le type de couche (`layer_types`) dans le `config.json` du modèle : trois lignes suffisent à calculer `κ`, sans lancer quoi que ce soit.
- Compter `L` comme le nombre de couches qui **stockent**, pas le nombre total de couches ; c'est l'erreur la plus fréquente sur les modèles hybrides.
- Régler le type du cache à part des poids quand le moteur le permet (`--kv-cache-dtype fp8` dans [[vLLM]]) : c'est le même ÷ 2 sur un poste, souvent sans changer de modèle. La perte de précision du cache aux longs contextes est rarement mesurée : la tester.
- Pour une charge d'agent (prompts longs, préfixes répétés), `κ` et le cache de préfixe ([[prompt-caching]]) pèsent plus dans la facture que le nombre de paramètres.

## Repères datés

- DeepSeek-V4.1-Flash : 890 octets de cache global par token, cache principal en FP4 (E2M1, échelle E4M3 par bloc de 16 canaux), 552 Md de paramètres de squelette dont 8 Md actifs au prefill et 16 Md au decode, contexte de 1 M, licence MIT ; model card relue à la source le 2026-10-20. Le rapport technique ne publie aucune évaluation de qualité à un million de tokens (section « Limites » : erreurs de sélection possibles dans des cas limites non testés). La model card affiche aussi 763 Md de paramètres dans son widget, écart non expliqué par la page. Cache de V4-Flash : 3 514 octets (document de floSa, rédigé le 2026-09-20).
- Valeurs des `κ` des autres modèles : relevés dans les `config.json` publics des 2026-09-30 et 2026-10-19 (Qwen3.8-27B, Qwen3.5-397B-A17B), recalculés.

## Approches voisines & alternatives

- [[Inference optimization]] — où le cache KV s'inscrit dans l'ensemble des techniques de serving.
- [[Contexte long]] — le coût mémoire du cache selon la longueur, et ce que valent les longueurs annoncées.
- [[Multi-head Latent Attention]] — compresser le cache par projection latente.
- [[Architectures hybrides LLM]] — moins de couches qui stockent.
- [[Flash Attention and efficient attention]] — attention économe, dont MQA et GQA.
- [[Dimensionner la mémoire d'un serveur LLM]] — du `κ` au nombre d'utilisateurs.
- [[Plafond de débit d'un GPU (roofline)]] — le cache relu à chaque pas s'ajoute aux octets lus par token.
- [[Prefill par morceaux et désagrégation prefill-decode]] — le cache est ce qui se transfère entre deux pools de GPU.

## Pour aller plus loin

- Ainslie et al. (2023) — *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*, arXiv 2305.13245 (EMNLP 2023).
- DeepSeek-AI (2024) — *DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model*, arXiv 2405.04434 (MLA, −93,3 % de cache face à DeepSeek 67B).
- Yang, Kautz, Hatamizadeh (2024) — *Gated Delta Networks: Improving Mamba2 with Delta Rule*, arXiv 2412.06464 (état de taille fixe).
- DeepSeek-AI — [model card de DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) et rapport technique *Pushing the Limits of KV Cache Compression*, figure 1(b).
- Cours de floSa : *DeepSeek-V4.1-Flash, ce que veut dire un cache KV 437 fois plus petit* (Nerdy Kings, 2026-09-18, [youtube.com/watch?v=sSuS5pLOU7U](https://www.youtube.com/watch?v=sSuS5pLOU7U)) et *Inférence d'un LLM sur GPU* (AI WITH Rithesh, [youtube.com/watch?v=lasG5MsR-gE](https://www.youtube.com/watch?v=lasG5MsR-gE), le calcul du cache de 8:47 à 9:10).
