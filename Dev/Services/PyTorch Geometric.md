---
galaxie: dev
type: service
nom: PyTorch Geometric
alias: [PyG, pyg, torch-geometric, torch_geometric]
pitch: "Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [gnn, deep-learning, gpu, representation-learning]
url_docs: https://pytorch-geometric.readthedocs.io/
url_repo: https://github.com/pyg-team/pytorch_geometric
---

# PyTorch Geometric

## Pourquoi

Bibliothèque de référence pour le **deep learning sur graphes** au-dessus de [[Dev/Services/PyTorch|PyTorch]]. Elle fournit la brique fondamentale des [[Graph Neural Networks]] — le **passage de messages** (`MessagePassing`) — et des dizaines de couches prêtes à l'emploi (GCN, GAT, GraphSAGE, GIN…), un format de données graphe (`Data`, `HeteroData`) basé sur des tenseurs `edge_index`, des **loaders** qui échantillonnent le voisinage pour faire tenir de gros graphes en mémoire (NeighborLoader), et un catalogue de datasets et de benchmarks. Opérations creuses et `scatter`/`gather` optimisés GPU : on écrit un GNN en quelques couches, on l'entraîne comme n'importe quel modèle PyTorch.

## Quand l'utiliser

- **Apprendre sur des données relationnelles / en graphe** : classification de nœuds, prédiction de liens, propriété de graphe (molécules, réseaux sociaux, recommandation).
- Prototyper et entraîner un **GNN** (GCN/GAT/GraphSAGE) sans réimplémenter le message passing.
- Gros graphes ne tenant pas en mémoire → échantillonnage de voisinage (mini-batching) intégré.
- Recherche : implémentations de référence et model zoo pour reproduire/étendre l'état de l'art.

## Quand NE PAS l'utiliser

- La **structure du graphe n'apporte rien** : des features tabulaires + un [[Dev/Services/XGBoost|GBDT]] font souvent aussi bien, pour moins cher (cf. [[Graph Neural Networks]]).
- Données en grille ou séquence régulière → [[Dev/Services/torchvision|CNN]] / Transformers, pas un GNN.
- Préférence pour l'écosystème DGL (multi-backend historique) ou besoin d'un moteur de graphes en base → [[Dev/Services/Neo4j|Neo4j]] (stockage, pas apprentissage).

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add torch-geometric`. Extensions creuses optionnelles (`pyg-lib`, `torch-scatter`) à appairer avec la version PyTorch/CUDA.
- Self-host : bibliothèque Python, rien à héberger ; coût = l'infra GPU d'entraînement.
- Suit les devices et versions de PyTorch (CUDA, ROCm, CPU).

## Pièges

- **Installation des extensions** (`torch-scatter`, `torch-sparse`, `pyg-lib`) sensible à la version exacte de PyTorch et CUDA — source classique d'échecs ; utiliser les roues officielles appariées.
- **Over-smoothing** : empiler trop de couches rend les nœuds indiscernables → rester peu profond ou ajouter résidus/normalisation.
- Le **mini-batching de graphes** concatène les graphes en un gros graphe par blocs diagonaux : penser au vecteur `batch` pour le pooling, sinon résultats faux silencieux.
- Échantillonnage de voisinage mal réglé → biais ou explosion mémoire sur nœuds très connectés (hubs).

## Alternatives

- Deep Graph Library (DGL) — alternative majeure pour les GNN, multi-backend (pas encore en fiche).

## Liens

- [[Graph Neural Networks]] — le concept (message passing, GCN/GAT/GraphSAGE) que PyG implémente.
- [[Dev/Services/PyTorch|PyTorch]] — framework sous-jacent.
- [[Dev/Services/Neo4j|Neo4j]] — source possible des graphes en entrée (stockage vs apprentissage).
- Doc : https://pytorch-geometric.readthedocs.io/
