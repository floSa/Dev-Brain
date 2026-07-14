---
galaxie: wiki
type: concept
nom: Graph Neural Networks
alias: [GNN, graph neural network, réseaux de neurones sur graphes, GCN, GAT, GraphSAGE, message passing, passage de messages]
categorie: concept/dl
domaines: [ml-eng, data-sci]
tags: [gnn, deep-learning, representation-learning]
---

# Graph Neural Networks

## Aperçu

- Réseaux de neurones opérant directement sur des **graphes** (nœuds + arêtes), là où [[CNN]] et [[Transformer architectures|Transformers]] supposent une grille ou une séquence régulière.
- Principe unique : le **passage de messages** (message passing) — chaque nœud met à jour sa représentation en agrégeant celles de ses voisins, couche après couche.
- Produit des **embeddings** de nœuds, d'arêtes ou de graphe entier, exploitables pour classer, prédire des liens ou régresser une propriété du graphe.

## Concepts clés

### Message passing

- À chaque couche, pour chaque nœud : (1) **agréger** les messages des voisins (somme, moyenne, max, attention), (2) **combiner** avec son état courant via un réseau, (3) mettre à jour.
- $K$ couches → chaque nœud « voit » son voisinage à $K$ sauts. C'est la généralisation de la convolution au domaine non euclidien.
- Cadre unificateur : la plupart des GNN sont des cas particuliers du *Message Passing Neural Network* (MPNN).

### GCN, GAT, GraphSAGE

- **GCN** (Graph Convolutional Network) : agrégation = moyenne pondérée normalisée des voisins. Simple, transductif.
- **GraphSAGE** : échantillonne un sous-ensemble de voisins et apprend une fonction d'agrégation → **inductif**, passe à l'échelle et généralise à des nœuds inédits.
- **GAT** (Graph Attention Network) : pondère les voisins par **attention** apprise (cf. [[Self-attention]]) au lieu d'une normalisation fixe.

### Tâches

- **Niveau nœud** : classification de nœuds (catégoriser un utilisateur, un article).
- **Niveau arête** : prédiction de liens (recommandation, complétion de graphe de connaissances).
- **Niveau graphe** : régression / classification sur le graphe entier (propriété d'une molécule) via un *readout* (pooling global).

## Les maths, simplement

- Mise à jour générique : $h_v^{(k)} = \phi\Big(h_v^{(k-1)},\ \bigoplus_{u \in \mathcal{N}(v)} \psi(h_u^{(k-1)})\Big)$ — $\mathcal{N}(v)$ = voisins, $\bigoplus$ = agrégation permutation-invariante, $\phi,\psi$ = réseaux appris.
- Couche GCN : $H^{(k)} = \sigma\big(\tilde{D}^{-1/2}\tilde{A}\,\tilde{D}^{-1/2}\,H^{(k-1)}\,W^{(k)}\big)$ — $\tilde{A}$ = adjacence + self-loops, $\tilde{D}$ = degrés, $W$ = poids appris.
- L'agrégation doit être **invariante par permutation** des voisins (un graphe n'a pas d'ordre) — d'où somme / moyenne / max / attention plutôt qu'une concaténation ordonnée.

## En pratique

- Données : un graphe stocké dans une base de graphes ([[Dev/Services/Neo4j|Neo4j]], [[Dev/Services/Nebula Graph|Nebula Graph]]) ou des tenseurs adjacence / edge-index. Frameworks : [[Dev/Services/PyTorch Geometric|PyTorch Geometric]] (PyG), Deep Graph Library (DGL).
- **Over-smoothing** : empiler trop de couches rend tous les nœuds identiques (les représentations convergent) → rester peu profond, ou résidus / normalisation.
- **Scalabilité** : sur gros graphes, échantillonner le voisinage (GraphSAGE) ou partitionner ; le full-batch ne tient pas en mémoire.
- Quand un GNN n'apporte rien : si la structure du graphe n'est pas informative, des features tabulaires + un [[Gradient Boosting (GBDT)|GBDT]] font souvent aussi bien, pour moins cher.

## Approches voisines & alternatives

- [[CNN]] — convolution sur grille régulière ; le GNN en est la généralisation aux domaines irréguliers.
- [[Self-attention]] / [[Transformer architectures]] — un Transformer est un GNN sur graphe complet ; GAT importe l'attention dans le voisinage local.
- [[embeddings]] — les GNN produisent des embeddings de nœuds qui prolongent les méthodes type node2vec, en supervisé et inductif.
- [[Dev/Services/PyTorch Geometric|PyTorch Geometric]] — bibliothèque de référence pour écrire et entraîner des GNN sur PyTorch (message passing, GCN/GAT/GraphSAGE).
- [[Dev/Services/Neo4j|Neo4j]], [[Dev/Services/Nebula Graph|Nebula Graph]] — stockage des graphes en entrée ; complémentaires (la base sert la donnée, le GNN apprend dessus).
- [[GraphRAG]] — exploite la structure de graphe pour le retrieval ; voie symbolique là où le GNN est une voie apprise.

## Pour aller plus loin

- Kipf & Welling (2017, GCN) ; Veličković et al. (2018, GAT) ; Hamilton et al. (2017, GraphSAGE) ; Gilmer et al. (2017, MPNN).
- Bronstein et al. — *Geometric Deep Learning* (cadre unificateur grilles / graphes / groupes).
- Frameworks : PyTorch Geometric (PyG), Deep Graph Library (DGL).
- Connexions brain : [[CNN]], [[Self-attention]], [[Dev/Services/Neo4j|Neo4j]], [[Dev/Services/Nebula Graph|Nebula Graph]], [[GraphRAG]].
