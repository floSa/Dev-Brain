---
role: brique
nom: PyTorch Geometric
alias: [PyG, pyg, torch-geometric, torch_geometric]
pitch: "Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN."
categorie: ml/graphe
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [gnn, deep-learning, gpu, representation-learning]
url_docs: https://pytorch-geometric.readthedocs.io/
url_repo: https://github.com/pyg-team/pytorch_geometric
---

# PyTorch Geometric

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de référence de deep learning sur graphes pour PyTorch — couches de message passing (GCN, GAT, GraphSAGE…), mini-batching par voisinage et datasets de graphes prêts à l'emploi pour construire et entraîner des GNN.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-20 |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque de référence pour le **deep learning sur graphes** au-dessus de [[PyTorch]].
Elle fournit la brique fondamentale des [[Graph Neural Networks]] — le **passage de messages**
(`MessagePassing`) — et des dizaines de couches prêtes à l'emploi (GCN, GAT, GraphSAGE, GIN),
un format de données graphe (`Data`, `HeteroData`) fondé sur des tenseurs `edge_index`, des
loaders qui échantillonnent le voisinage pour faire tenir de gros graphes en mémoire
(`NeighborLoader`), et un catalogue de datasets et de benchmarks. Le **mini-batching**
concatène les graphes en un seul gros graphe par blocs diagonaux : le vecteur `batch` devient
indispensable au pooling, et l'oublier produit des résultats faux **silencieusement**. Les
opérations creuses et les `scatter`/`gather` sont optimisés GPU.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Apprendre sur des données relationnelles ou en graphe : classification de nœuds, prédiction de liens, propriété de graphe | La **structure du graphe n'apporte rien** : des features tabulaires et un GBDT ([[XGBoost]]) font souvent aussi bien, pour moins cher — cf. [[Graph Neural Networks]] |
| Prototyper et entraîner un GNN — GCN, GAT, GraphSAGE — sans réimplémenter le message passing | **Installation des extensions** (`torch-scatter`, `torch-sparse`, `pyg-lib`) sensible à la version exacte de PyTorch et CUDA : source classique d'échecs, roues officielles appariées obligatoires |
| Gros graphes ne tenant pas en mémoire : échantillonnage de voisinage intégré | **Over-smoothing** : empiler trop de couches rend les nœuds indiscernables — rester peu profond, ou ajouter résidus et normalisation |
| Recherche : implémentations de référence et model zoo pour reproduire ou étendre l'état de l'art | Échantillonnage de voisinage mal réglé sur des nœuds très connectés : biais, ou explosion mémoire |
| | Données en grille ou séquence régulière : un CNN ([[torchvision]]) ou un Transformer, plutôt qu'un GNN |
| | Besoin d'un moteur de graphes **en base**, pas d'apprentissage → [[Neo4j]] |

## Mise en œuvre

- Installation — `uv add torch-geometric` ; extensions creuses optionnelles (`pyg-lib`, `torch-scatter`) à appairer avec la version PyTorch/CUDA
- Point d'entrée — API Python : `Data` / `HeteroData`, couches `MessagePassing`, loaders d'échantillonnage
- Prérequis — [[PyTorch]] installé, et une version de CUDA cohérente avec les roues des extensions
- Exécution — single-node ; suit les devices et versions de PyTorch (CUDA, ROCm, CPU)
- Coût — gratuit, MIT, rien à héberger ; le coût est celui de l'infra GPU d'entraînement

## Écosystème

### Alternatives

- Deep Graph Library (DGL) — l'alternative majeure pour les GNN, multi-backend historique (pas encore en fiche).

## Ressources

- Documentation — https://pytorch-geometric.readthedocs.io/
- Dépôt — https://github.com/pyg-team/pytorch_geometric

## Voir aussi

- [[Graph Neural Networks]] — la notion : message passing, GCN, GAT, GraphSAGE, que PyG implémente
- [[PyTorch]] — le framework sous-jacent
- [[Neo4j]] — source possible des graphes en entrée : stockage, contre apprentissage
