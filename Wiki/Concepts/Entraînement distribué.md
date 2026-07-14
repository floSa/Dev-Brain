---
galaxie: wiki
type: concept
nom: Entraînement distribué
alias: [Distributed training, DDP, DistributedDataParallel, FSDP, ZeRO, data parallelism, model parallelism, pipeline parallelism, tensor parallelism, sharding, DeepSpeed, parallélisme de données]
categorie: concept/dl
domaines: [ml-eng, mlops]
tags: [distributed-training, deep-learning, gpu, memory-optimization]
---

# Entraînement distribué

## Aperçu

- Répartir l'**entraînement** d'un réseau sur plusieurs GPU (voire plusieurs nœuds) pour aller **plus vite** (plus de débit) ou faire tenir un modèle qui **ne rentre pas** sur une seule carte.
- Deux axes orthogonaux : découper les **données** (chaque GPU voit un sous-lot, le modèle est répliqué) ou découper le **modèle** (les poids eux-mêmes sont éclatés entre GPU).

## Concepts clés

### Parallélisme de données vs de modèle
- **Data parallel (DDP)** : le modèle est **répliqué** sur chaque GPU ; chacun traite une part du batch, puis les gradients sont moyennés par **all-reduce**. Simple, efficace tant que le modèle tient sur une carte.
- **Model / tensor / pipeline parallel** : le modèle est **partitionné** — par couches (pipeline) ou à l'intérieur d'une couche (tensor). Nécessaire quand les poids dépassent la VRAM d'un GPU ; communication plus lourde.

### ZeRO & FSDP — sharding des états
- **ZeRO** (DeepSpeed) supprime la redondance du data parallel en **shardant** les états d'entraînement entre GPU : étape 1 = états de l'optimiseur, 2 = + gradients, 3 = + paramètres. On reconstruit à la volée par communication.
- **FSDP** (*Fully Sharded Data Parallel*) est l'implémentation native [[Dev/Services/PyTorch|PyTorch]], équivalente à ZeRO-3 : chaque GPU ne détient qu'un **shard** des poids et les rassemble (all-gather) juste avant de calculer la couche.

### Communication collective
- Le coût n'est plus le calcul mais l'**échange** : `all-reduce`, `all-gather`, `reduce-scatter` sur NCCL. La bande passante d'interconnexion (NVLink, InfiniBand) devient le facteur limitant à grande échelle.

## Les maths, simplement

- Mémoire d'un paramètre entraîné en précision mixte avec Adam : $2$ (poids fp16) $+ 2$ (gradient) $+ 4$ (copie maître fp32) $+ 4 + 4$ (moments $m, v$) $\approx \mathbf{16}$ octets/paramètre — d'où l'intérêt de **sharder**.
- ZeRO-3 / FSDP sur $N$ GPU ramènent cette empreinte à $\approx 16/N$ octets/paramètre, au prix d'un surcroît de communication ($\approx 1{,}5\times$ le volume du data parallel).

## En pratique

- Réflexe par défaut : **DDP** tant que le modèle tient sur un GPU — c'est le plus simple et le plus rapide. Passer à **FSDP / ZeRO** seulement quand la VRAM sature.
- Se combine avec les autres leviers mémoire : [[Mixed precision]] (poids/activations en bf16) et [[Gradient checkpointing]] (activations recalculées) sont quasi systématiques à grande échelle.
- Pièges : un **batch effectif** qui explose avec le nombre de GPU (ajuster le learning rate) ; des GPU sous-alimentés si le pipeline de données ne suit pas ; un sharding trop agressif dont la communication annule le gain.
- Surcouches qui masquent la plomberie : [[Dev/Services/PyTorch Lightning|PyTorch Lightning]], [[Dev/Services/accelerate|accelerate]], [[Dev/Services/DeepSpeed|DeepSpeed]].

## Approches voisines & alternatives

- [[Mixed precision]] — levier mémoire/débit complémentaire, presque toujours activé avec le distribué.
- [[Gradient checkpointing]] — échange du calcul contre de la mémoire d'activations, combiné à FSDP/ZeRO sur les gros modèles.
- [[Dev/Services/PyTorch|PyTorch]] — DDP et FSDP natifs (`torch.distributed`, `torch.distributed.fsdp`).
- [[Dev/Services/DeepSpeed|DeepSpeed]] — implémentation de référence de ZeRO (sharding des états, offload CPU/NVMe, 3D-parallelism).

## Pour aller plus loin

- Rajbhandari et al. (2020) — *ZeRO: Memory Optimizations Toward Training Trillion Parameter Models*.
- Zhao et al. (2023) — *PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel*.
- Shoeybi et al. (2019) — *Megatron-LM* (tensor / pipeline parallelism).
