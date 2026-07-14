---
galaxie: wiki
type: concept
nom: Pruning
alias: [Pruning, élagage, élagage de modèle, sparsity, sparsité, structured pruning, unstructured pruning, élagage structuré, élagage non structuré, magnitude pruning, lottery ticket]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [pruning, model-compression, deep-learning, inference-optimization]
---

# Pruning

## Aperçu

- **Élaguer** un modèle : supprimer les poids (ou des structures entières) jugés peu utiles pour obtenir un réseau plus petit et plus rapide, à perte de qualité maîtrisée.
- Repose sur la **redondance** des gros réseaux : une fraction des poids porte l'essentiel de la fonction ; le reste peut être mis à zéro, souvent sans dégradation notable après ré-ajustement.

## Concepts clés

### Structuré vs non structuré
- **Non structuré** : on met à zéro des **poids individuels** → matrices creuses très éparses, mais le gain de vitesse exige un **matériel/noyau** qui exploite la sparsité (sinon la matrice reste dense en mémoire).
- **Structuré** : on supprime des **unités entières** (neurones, canaux, têtes d'attention, couches) → modèle réellement plus petit et plus rapide sur GPU standard, mais granularité plus grossière, donc plus risquée.

### Critère d'élagage
- Le plus courant est l'amplitude : élaguer les poids de plus **faible magnitude** ($|w|$ petit). Variantes plus fines fondées sur la sensibilité de la perte (importance par gradient / second ordre).

### Élaguer puis ré-entraîner
- Recette canonique **itérative** : élaguer une fraction → *fine-tuner* pour récupérer → recommencer. Élaguer d'un coup trop fort casse le modèle.
- **Lottery Ticket Hypothesis** (Frankle & Carbin, 2019) : un sous-réseau creux, ré-initialisé à ses poids d'origine, peut atteindre la performance du réseau dense — il existe de « bons billets » cachés.

## Les maths, simplement

- Taux de sparsité $s = \frac{\#\{w_i = 0\}}{\#\{w_i\}}$. La taille mémoire utile décroît avec $s$, mais le **débit** ne suit que si le format (structuré, ou motif **N:M** type 2:4 sur Tensor Cores) est exploitable par le matériel.
- L'élagage non structuré atteint des $s$ élevés (90 %+) sur le papier ; le gain de **latence** réel dépend du support de la sparsité, d'où l'attrait du structuré.

## En pratique

- Lever d'efficience pour le déploiement, à ranger avec la [[Quantization]] et la [[Distillation]] — les trois briques de la [[Small Language Models|fabrication de petits modèles]] efficaces, souvent **enchaînées**.
- La **sparsité semi-structurée 2:4** (NVIDIA Ampere+) est le compromis pratique : 50 % de zéros dans un motif que les Tensor Cores accélèrent vraiment.
- Pièges : un élagage non structuré qui n'apporte **aucune accélération** faute de noyau creux ; oublier le *fine-tuning* de récupération ; comparer des taux de sparsité sans regarder la latence réelle.

## Approches voisines & alternatives

- [[Quantization]] — compression par baisse de **précision** des poids ; le pruning supprime des poids. Voies orthogonales, souvent combinées.
- [[Distillation]] — compression prof → élève : entraîner un petit modèle plutôt que dégrader le grand ; complémentaire.
- [[Small Language Models]] — le pruning est l'une de leurs recettes d'efficience.
- [[Inference optimization]] — le pruning s'inscrit dans l'arsenal d'accélération de l'inférence.
- [[Dev/Services/PyTorch|PyTorch]] — `torch.nn.utils.prune` (élagage par magnitude, structuré/non structuré).

## Pour aller plus loin

- Han et al. (2015) — *Learning both Weights and Connections for Efficient Neural Networks*.
- Frankle & Carbin (2019) — *The Lottery Ticket Hypothesis*.
- Mishra et al. (2021) — *Accelerating Sparse Deep Neural Networks* (sparsité 2:4).
