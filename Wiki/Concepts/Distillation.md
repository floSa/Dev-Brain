---
galaxie: wiki
type: concept
nom: Distillation
alias: [Knowledge distillation, distillation de connaissances, teacher-student, distillation prof-élève, soft labels, dark knowledge]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [model-compression, deep-learning, small-language-model, synthetic-data, fine-tuning]
---

# Distillation

## Aperçu

- Technique de **compression** où un petit modèle **élève** apprend à imiter un grand modèle **professeur**, en s'entraînant sur ses **sorties** plutôt que sur les seules étiquettes dures.
- Idée clé : les **probabilités douces** du professeur (et non juste la classe gagnante) portent une information riche — les similarités entre classes, la « *dark knowledge* » — qu'un petit modèle capte mal s'il apprend seul.

## Concepts clés

### Cibles douces et température
- On « adoucit » les logits du professeur par une **température** $T>1$ : la distribution devient moins piquée et révèle la structure relative entre classes. L'élève apprend à reproduire cette distribution.

### Variantes
- **Response-based** : imiter les logits / probabilités de sortie (le cas canonique).
- **Feature-based** : aligner aussi les **représentations intermédiaires** (DistilBERT, TinyBERT).
- **Sequence-level (LLM)** : entraîner l'élève sur des **générations** du professeur — la distillation devient de la [[Synthetic data generation|génération de données synthétiques]].

### Distillation et données synthétiques
- Pour les LLM, distiller revient souvent à faire produire au grand modèle un corpus d'instructions/réponses, puis à y faire un [[SFT|fine-tuning supervisé]] de l'élève (self-instruct, distillation de raisonnement).

## Les maths, simplement

- Perte combinée : $\mathcal{L} = \alpha\,\underbrace{\text{CE}(y, p_\text{élève})}_{\text{étiquettes dures}} + (1-\alpha)\,T^2\,\underbrace{\text{KL}\!\big(p^T_\text{prof}\,\|\,p^T_\text{élève}\big)}_{\text{cibles douces}}$.
- Le terme de droite est une [[KL divergence]] entre distributions adoucies à température $T$ (le facteur $T^2$ rééquilibre l'échelle des gradients) ; le terme de gauche est la [[Cross-entropy|cross-entropie]] habituelle.

## En pratique

- Suppose un **accès au professeur** : logits/représentations (boîte blanche) ou au moins ses générations (boîte noire). Distiller un modèle **propriétaire fermé** peut violer ses conditions d'utilisation — vérifier la licence.
- Se **cumule** avec la [[Quantization]] : on distille d'abord vers un élève plus petit, puis on quantize pour le déploiement.
- Produit des [[Small Language Models|petits modèles]] efficaces (DistilBERT, gammes « distill » de Gemma/Llama) ; alternative ou complément au [[PEFT]] quand on veut **réduire la taille** et pas seulement le coût d'adaptation.

## Approches voisines & alternatives

- [[Quantization]] — autre voie de compression : on baisse la **précision** au lieu de réduire la **taille** du modèle ; souvent combinées.
- [[Pruning]] — compression par **suppression** de poids/structures ; complémentaire de la distillation prof → élève.
- [[Small Language Models]] — la distillation est l'une des recettes pour les obtenir.
- [[Synthetic data generation]] — la distillation au niveau séquence en est un cas (apprendre des générations du professeur).
- [[PEFT]] — réduit le **coût d'adaptation** (LoRA) sans changer la taille ; complémentaire.
- [[Cross-entropy]] / [[KL divergence]] — les pertes qui mesurent l'écart élève↔professeur.

## Pour aller plus loin

- Hinton, Vinyals & Dean (2015) — *Distilling the Knowledge in a Neural Network*.
- Sanh et al. (2019) — *DistilBERT, a distilled version of BERT*.
- Gou et al. (2021) — *Knowledge Distillation: A Survey*.
