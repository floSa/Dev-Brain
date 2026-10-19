---
role: notion
nom: Dimensionner la mémoire d'un serveur LLM
alias: [budget mémoire GPU, nombre d'utilisateurs maximum, capacité d'un serveur LLM, VRAM d'un serveur LLM, gpu-memory-utilization, réplication des têtes KV, dimensionnement vLLM, empreinte mémoire d'un LLM, combien d'utilisateurs sur un GPU]
categorie: llm/runtime
domaines: [ai-eng, mlops]
tags: [inference-optimization, inference, gpu, llm, model-serving]
---

# Dimensionner la mémoire d'un serveur LLM

## Aperçu

- Dimensionner un serveur LLM revient à répartir la mémoire d'un GPU entre quatre postes (poids, cache KV, état fixe, mémoire de travail) et à en déduire **combien d'utilisateurs simultanés tiennent**. Au-delà d'un utilisateur, c'est la capacité mémoire qui borne le lot avant le calcul.
- Exemple chiffré : un modèle dense de 27 milliards de paramètres en bfloat16 (50,1 Gio de poids) sur un H100 de 80 Go laisse environ 18 Gio au cache, soit **28 utilisateurs de 8 192 tokens**. Avec des poids en FP8, le même GPU en accueille environ 61 : un gigaoctet non dépensé en poids devient de la place pour le cache.

## Concepts clés

### Les quatre postes

| Poste | Dépend de | Se relit à chaque pas ? |
|---|---|---|
| **Poids** `W` | nombre de paramètres × octets par poids | oui, en entier (modèle dense) |
| **Cache KV** `κ·T` par utilisateur | longueur du contexte (cf. [[Taille du cache KV par token]]) | oui, en entier, pour chaque utilisateur |
| **État fixe** `S` par utilisateur | architecture (couches à état de taille fixe, pas de dépendance au contexte) | oui |
| **Mémoire de travail** | activations, tampons, graphes CUDA capturés | non |

Les poids sont **partagés** entre les utilisateurs du lot ; le cache et l'état ne le sont pas, sauf préfixe commun (cf. [[prompt-caching]]).

### La fraction réservée

Un moteur comme [[vLLM]] ne prend pas toute la carte : il réserve une fraction `u` de la mémoire (`--gpu-memory-utilization`, 0,92 par défaut dans la documentation stable consultée le 2026-10-20 ; une vidéo de référence disait 0,90). Ce qui reste après les poids et la mémoire de travail sert aux blocs de cache.

### Unités

Les constructeurs annoncent des **Go** (10⁹ octets) ; la mémoire utilisable et les tailles de fichiers se lisent mieux en **Gio** (2³⁰). Comparer 54 Go de poids à 80 Go de carte sans convertir fait croire qu'il reste 26 Go ; la bonne soustraction est 79,6 − 50,1 ≈ 29,5 Gio. Mélanger les deux fausse un dimensionnement d'environ 7 %.

### Le terme fixe et le terme qui grandit

Pour un modèle qui mélange des couches d'attention et des couches à état fixe (cf. [[Architectures hybrides LLM]]), la mémoire d'une conversation vaut `κ·T + S`. Les deux termes sont égaux à `T = S ÷ κ` : 2 304 tokens pour un modèle dense de 27 Md (état de 144 Mio, cache de 64 Kio par token). Au-delà, le cache domine ; en deçà, c'est l'état fixe.

### Réplication des têtes KV en parallélisme de tenseurs

Quand un modèle compte peu de têtes de clés-valeurs (2 ou 4 avec le GQA) et qu'on le coupe sur davantage de GPU que de têtes, le moteur **duplique** les têtes. Dans [[vLLM]], `QKVParallelLinear` fait `if tp_size >= total_num_kv_heads` puis `num_kv_head_replicas = tp_size // total_num_kv_heads` (code lu sur la branche principale le 2026-10-20). Avec 2 têtes KV sur 8 GPU, le cache du nœud est multiplié par 4. Voir [[Parallélisme en inférence]].

### Modèle à experts : tous les poids, quelques-uns lus

Dans un MoE, **tous les experts doivent tenir en mémoire** : l'empreinte suit les paramètres totaux, pas les paramètres actifs (cf. [[Mixture of Experts]]). Qwen3.5-397B-A17B pèse 396,3 Md de paramètres (793 Go en bfloat16, 396 Go en FP8, 223 Go à 4 bits environ) pour 16,3 Md actifs : il ne tient sur aucune carte seule, même à 4 bits.

## Les maths, simplement

```
B_max ≈ (M_GPU × u − W − M_travail) ÷ (κ·T_u + S)
```

- `M_GPU` : mémoire de la carte ; `u` : fraction réservée ; `W` : poids ; `M_travail` : mémoire de travail ; `κ·T_u` : cache d'un utilisateur de contexte `T_u` ; `S` : état fixe.
- **Cas 1, dense 27 Md sur un H100** (contextes de 8 192 tokens) : 79,6 Gio × 0,90 = 71,6 ; moins 50,1 de poids, moins environ 3,5 de mémoire de travail (hypothèse non sourcée de la vidéo) : 18 Gio. Par utilisateur : 8 192 × 64 Kio + 144 Mio = 0,64 Gio. `B_max ≈ 28`. Avec `u = 0,92` : 73,2 Gio de budget, `B_max ≈ 30`.
- **Cas 2, mêmes calculs avec des poids FP8** : le dépôt pèse 28,75 Gio (et non 25 : tenseurs laissés en 16 bits, échelles) ; il reste 39,3 Gio, soit `B_max ≈ 61`. La formule idéale `P × 1 octet` sous-estime la taille des fichiers publiés ; lire la somme des fichiers du dépôt.
- **Cas 3, MoE de 396 Md en FP8 sur 8 × H100 (640 Go)**, contextes de 32 768 tokens, cache en bfloat16 : 0,92 × 640 − 406 = 183 Go, soit 170 Gio de reste. `κ = 30 720` octets par token et `S = 180 Mio` ; le cache d'un utilisateur fait 0,94 Gio. En parallélisme de tenseurs 8 (réplication ×4) : 0,94 × 4 + 0,18 = 3,9 Gio, soit **environ 43 utilisateurs**. En parallélisme de données pour l'attention (sans réplication) : 1,1 Gio, soit **environ 150**. L'écart est d'un facteur 3,5 : le choix du mode de parallélisme se fait avant l'achat. La source donne 46 et 163 en mélangeant Go et Gio ; la marge pour les activations n'est pas retranchée.
- **La vitesse, elle, dépend du lot** (cf. [[Plafond de débit d'un GPU (roofline)]]) : 28 utilisateurs à 8 192 tokens font passer le pas de 16,3 à 21,8 ms. La capacité mémoire se calcule ; la latence acceptable fixe la limite haute.

## En pratique

- Partir de la **taille réelle des fichiers** du dépôt (somme des `safetensors`), pas de `paramètres × octets` : un écart de 0,4 % à 13 % a été mesuré selon le format.
- Quand la mémoire manque, un moteur **préempte** des requêtes et les recalcule plus tard (mode `RECOMPUTE` en V1 de vLLM) : le débit se dégrade sans erreur. Surveiller les métriques de préemption.
- Pour plus d'utilisateurs : poids quantifiés, cache KV en FP8, architecture à cache réduit, ou plus de GPU. Chaque gigaoctet retiré aux poids devient de la place au cache.
- Ne pas confondre fenêtre de contexte **annoncée** et fenêtre **payable** : combien de sessions simultanées tiennent à cette longueur ? (cf. [[Contexte long]]).
- Un outil comme [[llmfit]] répond à la version poste de travail de la question.

## Repères datés

Relevé le 2026-09-30 et le 2026-10-19 dans les cours de floSa ; les poids de dépôts changent à chaque publication.

- Qwen3.8-27B : 55,56 Go en bfloat16 (dépôt complet, 51,75 Gio), 30,87 Go en FP8 (28,75 Gio) ; relevé sur Hugging Face le 2026-09-30.
- Qwen3.5-397B-A17B : dépôt bfloat16 806,8 Go, FP8 officiel 406,2 Go, NVFP4 251,2 Go, MLX 4 bits 223,9 Go ; relevé le 2026-10-19.
- vLLM : `--gpu-memory-utilization` 0,92 par défaut (documentation stable, 2026-10-20).

## Approches voisines & alternatives

- [[Taille du cache KV par token]] — la formule du poste qui grandit.
- [[Plafond de débit d'un GPU (roofline)]] — ce que la capacité ne dit pas : la vitesse par utilisateur.
- [[Parallélisme en inférence]] — comment répartir un modèle sur plusieurs GPU, et ce que chaque mode fait au cache.
- [[Quantization]] — réduire le poste des poids.
- [[Architectures hybrides LLM]] et [[Multi-head Latent Attention]] — réduire le poste du cache.
- [[Inference optimization]] — vue d'ensemble des techniques.
- [[Coût d'un token et taux d'utilisation]] — la mémoire fixe le lot, le lot fixe le coût par token.

## Pour aller plus loin

- Kwon et al. (2023) — *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv 2309.06180 (SOSP 2023) : gaspillage de la réservation contiguë.
- Documentation vLLM — [Engine Arguments](https://docs.vllm.ai/en/stable/configuration/engine_args/) et [Optimization and Tuning](https://docs.vllm.ai/en/stable/configuration/optimization/).
- Cours de floSa, *Inférence d'un LLM sur GPU* (AI WITH Rithesh, 2026-09-28, [youtube.com/watch?v=lasG5MsR-gE](https://www.youtube.com/watch?v=lasG5MsR-gE), le calcul des 28 utilisateurs à 10:28) et *Servir un LLM à plusieurs utilisateurs* (Benoit Ferrere, cinq shorts, 2026-09-11 à 2026-10-18) : calculs refaits, scripts `recalcul-chiffres.py` et `recalcul-moe.py` exécutés.
