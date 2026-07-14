---
galaxie: wiki
type: concept
nom: LoRA et QLoRA
alias: [LoRA, Low-Rank Adaptation, QLoRA, quantized LoRA, adapters LoRA, low-rank adapters]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [fine-tuning, llm]
---

# LoRA et QLoRA

## Aperçu

- **LoRA (Low-Rank Adaptation)** : figer les poids du modèle et n'entraîner que deux **petites matrices de rang faible** $B \cdot A$ injectées dans certaines couches (l'attention surtout). La méthode de fine-tuning la plus citée, cas-phare du [[PEFT]].
- Réduit massivement les **paramètres entraînables** et la **mémoire d'optimiseur** ; **QLoRA** y ajoute un modèle de base quantifié en 4 bits pour fine-tuner un très grand modèle sur un seul GPU.

## Concepts clés

### LoRA
- Au lieu de modifier une matrice de poids $W$, on apprend une mise à jour de rang faible $\Delta W = B A$ avec un **rang** $r \ll \dim$. Le modèle de base ne bouge pas ; seuls $A$ et $B$ sont appris — souvent < 1 % des paramètres.
- À l'inférence, deux régimes : **fusion** de $\Delta W$ dans $W$ (zéro surcoût de latence), ou adaptateurs gardés à part et **chargés à la volée** — multi-LoRA en serving, un adaptateur par tâche / client sur le même modèle de base.

### QLoRA
- LoRA **par-dessus un modèle de base quantifié en 4 bits** (format **NF4**), complété par la **double quantization** (quantizer aussi les constantes de quantization) et les **paged optimizers** (états d'optimiseur paginés vers la RAM CPU) → fine-tuning d'un modèle de 65B sur un seul GPU.
- Lien fort avec la [[Quantization]] : le modèle gelé est en 4 bits, les adaptateurs restent en pleine précision.

### Pourquoi ça marche
- L'adaptation à une tâche vit dans un sous-espace de **faible dimension intrinsèque** : une mise à jour de rang faible capte l'essentiel, d'où une perte minime face au full fine-tuning.

## Les maths, simplement

- Couche adaptée : $W' = W_0 + \tfrac{\alpha}{r}\, B A$, avec $W_0$ gelée, $A \in \mathbb{R}^{r \times d}$ (init aléatoire), $B \in \mathbb{R}^{d \times r}$ (**init à 0** : $\Delta W$ nul au départ) et $r \ll d$ ; $\alpha$ est le facteur d'**échelle** (scaling).
- Seuls $A$ et $B$ sont appris : $2 d r$ paramètres au lieu de $d^2$ — et l'optimiseur ne garde d'états que pour eux, d'où l'économie de mémoire.

## En pratique

- **Leviers** : le rang `r` (8–64 typiquement), `alpha` (souvent $2r$), `target_modules` (commencer par les projections d'attention, étendre aux MLP si la qualité manque), `dropout` sur l'adaptateur.
- **Rang trop bas = sous-capacité** : le modèle n'apprend pas la tâche ; monter `r` avant de conclure que LoRA ne suffit pas.
- **Quand préférer le full fine-tuning** : qualité qui plafonne malgré un rang élevé, changement de domaine profond, budget GPU non contraint. Sinon LoRA (ou QLoRA si la mémoire est serrée) est le défaut raisonnable.
- Outils : la lib **`peft`** de [[Dev/Services/HuggingFace|HuggingFace]] (+ `bitsandbytes` pour la 4-bit), exploitée par [[Dev/Services/Unsloth|Unsloth]], [[Dev/Services/Axolotl|Axolotl]], [[Dev/Services/LLaMA-Factory|LLaMA-Factory]] et [[Dev/Services/TRL|TRL]].

## Approches voisines & alternatives

- [[PEFT]] — le concept parapluie : familles d'adaptation paramétriquement efficaces (adapters, prefix / prompt tuning, (IA)³), dont LoRA est la méthode-phare.
- [[Quantization]] — la 4-bit (NF4) qui rend QLoRA possible ; sert aussi à l'inférence légère.
- [[SFT]] — l'objectif d'entraînement le plus souvent exécuté en LoRA.
- [[RLHF and DPO]] — l'alignement tourne aussi en LoRA pour rester abordable.

## Pour aller plus loin

- Hu et al. (2021) — *LoRA: Low-Rank Adaptation of Large Language Models*.
- Dettmers et al. (2023) — *QLoRA: Efficient Finetuning of Quantized LLMs*.
