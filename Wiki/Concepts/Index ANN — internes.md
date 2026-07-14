---
galaxie: wiki
type: concept
nom: Index ANN — internes
alias: [ANN, index ANN, HNSW, IVF, PQ, product quantization, approximate nearest neighbor, recherche ANN]
categorie: concept/data
domaines: [data-eng, ai-eng]
tags: [ann, vector-db, embeddings]
---

# Index ANN — internes

## Aperçu

- Comment les index de recherche vectorielle trouvent les plus proches voisins **sans** comparer la requête à tous les vecteurs : ils échangent un peu de **rappel** contre beaucoup de **vitesse** et de **mémoire**.
- Trois familles, souvent combinées : **HNSW** (graphe), **IVF** (partitionnement), **PQ** (compression). C'est ce qui tourne sous [[Dev/Services/Faiss|Faiss]], [[Dev/Services/hnswlib|hnswlib]], [[Dev/Services/ScaNN|ScaNN]] et les [[Bases de données vectorielles|bases vectorielles]].

## Concepts clés

### HNSW — graphe navigable hiérarchique
- Un graphe multi-couches : les couches hautes, clairsemées, servent d'« autoroutes » ; les basses, denses, affinent localement.
- Recherche par *greedy* : descendre couche par couche vers le voisin le plus proche, à partir d'un point d'entrée.
- Réglages : `M` (degré du graphe, mémoire), `ef_construction` (qualité de construction), `ef` (effort à la requête → rappel vs latence).
- Profil : rappel/latence excellents, **construction incrémentale**, mais **forte RAM** (tout le graphe en mémoire) et peu compressible. Défaut courant.

### IVF — index inversé (partitionnement)
- Un *k-means* partitionne l'espace en **cellules** (centroïdes) ; chaque vecteur est rangé dans sa cellule.
- À la requête, on ne sonde que les `nprobe` cellules les plus proches du vecteur requête au lieu de tout l'espace.
- Réglages : nombre de cellules (`nlist`) et `nprobe` (cellules sondées → rappel vs vitesse). Nécessite un `train()` sur un échantillon représentatif.
- Profil : construction rapide et bonne montée en charge sur gros volumes ; rappel sensible aux vecteurs proches d'une frontière de cellule.

### PQ — quantification de produit (compression)
- Découpe chaque vecteur en *m* sous-vecteurs ; chaque sous-vecteur est remplacé par l'**id du centroïde** le plus proche d'un petit codebook appris.
- Un vecteur devient *m* codes d'un octet → compression massive de la RAM ; les distances s'approximent via des tables précalculées.
- Coût : c'est une approximation **avec perte** → rappel dégradé, souvent rattrapé par un *re-ranking* exact sur les meilleurs candidats.
- Variante : **OPQ** (rotation apprise avant PQ) ; la **quantification anisotrope** de [[Dev/Services/ScaNN|ScaNN]] préserve les composantes qui comptent pour le produit scalaire.

### Combinaisons
- En pratique on **empile** : `IVF+PQ` (partitionner *puis* compresser) pour des milliards de vecteurs en RAM contrainte ; `HNSW` posé sur les centroïdes IVF pour accélérer le choix des cellules.
- Le bon index dépend du budget : RAM disponible, volume, rappel cible, latence acceptable.

## Les maths, simplement

- **Rappel\@k** = (nb de vrais $k$ plus proches retrouvés) / $k$. C'est la métrique qu'on sacrifie pour la vitesse ; tous les réglages (`ef`, `nprobe`) l'arbitrent contre la latence.
- Mémoire PQ : un vecteur de dimension $d$ en `float32` coûte $4d$ octets ; en PQ à $m$ sous-quantizers d'un octet, $m$ octets. Pour $d=768, m=96$ → 3072 → 96 octets, soit ≈ **32×** moins. Les codebooks ont $2^{8}=256$ centroïdes par sous-espace.
- IVF : sonder $\text{nprobe}$ cellules sur $\text{nlist}$ ramène le coût de recherche à ≈ $\frac{\text{nprobe}}{\text{nlist}}$ de la force brute — d'où le compromis rappel/vitesse réglé par `nprobe`.
- HNSW : recherche en ≈ $O(\log n)$ sauts grâce à la hiérarchie, au prix d'une mémoire en $O(n \cdot M)$ pour les arêtes.

## En pratique

- Choisir l'index par contrainte dominante : **HNSW** si la RAM suffit et qu'on vise le meilleur rappel/latence ; **IVF** si construction rapide et gros volume ; **PQ** (souvent `IVF+PQ`) si la RAM est le mur.
- IVF et PQ exigent un `train()` sur un échantillon **représentatif** ; un échantillon biaisé dégrade durablement le rappel.
- Mesurer le rappel sur un jeu de requêtes réel avant de figer les hyperparamètres : `ef` / `nprobe` trop bas font chuter le rappel **silencieusement** (aucune erreur, juste de mauvais voisins).
- Avec compression, ajouter un **re-ranking exact** sur les top candidats pour récupérer le rappel perdu par PQ.
- Pour quelques milliers de vecteurs, un index plat (exact) [[Dev/Services/Faiss|Faiss]] ou même du NumPy suffit : pas besoin d'ANN. L'ANN se justifie au-delà de ~$10^5$–$10^6$ vecteurs.

## Approches voisines & alternatives

- [[Bases de données vectorielles]] — le concept englobant ; ces index sont son moteur de recherche.
- [[Dev/Services/Faiss|Faiss]] — la boîte à outils de référence (HNSW, IVF, PQ, OPQ, GPU).
- [[Dev/Services/hnswlib|hnswlib]] — HNSW « nu », minimal et incrémental.
- [[Dev/Services/ScaNN|ScaNN]] — quantification anisotrope, état de l'art sur le produit scalaire.
- [[embeddings]] — les vecteurs que ces index organisent et recherchent.
- Alternative : k-NN **exact** (force brute / `IndexFlat`) — rappel parfait, viable seulement à petit volume.

## Pour aller plus loin

- Comparatif des moteurs qui exposent ces index : [[Comparatif - Bases vectorielles]].
- Familles non couvertes ici : LSH (hachage sensible à la localité), arbres (Annoy) — historiquement importantes, aujourd'hui dominées par HNSW/IVF/PQ sur la plupart des charges.
