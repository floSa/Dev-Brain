---
role: brique
nom: pytorch-crf
alias: [torchcrf, pytorch crf, conditional random field pytorch]
pitch: "Couche CRF (champ aléatoire conditionnel) pour PyTorch — modélise les dépendances entre labels voisins et décode par Viterbi ; brique de sortie classique d'un tagger d'étiquetage de séquence."
categorie: ml/nlp
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [sequence-labeling, ner, deep-learning]
url_docs: https://pytorch-crf.readthedocs.io
url_repo: https://github.com/kmkurn/pytorch-crf
---

# pytorch-crf

<!-- AUTO:BANDEAU:START -->
> Couche CRF (champ aléatoire conditionnel) pour PyTorch — modélise les dépendances entre labels voisins et décode par Viterbi ; brique de sortie classique d'un tagger d'étiquetage de séquence.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont ancien · 2019-02-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation minimale et canonique d'une **couche CRF** — champ aléatoire conditionnel
linéaire — pour [[PyTorch]]. Posée en sortie d'un modèle de séquence, BiLSTM ou transformeur,
elle calcule la **log-vraisemblance** des séquences de labels et **décode** la meilleure par
Viterbi, de sorte que les labels prédits respectent les contraintes de transition : un `I-PER`
ne suit pas un `O`. C'est une brique de sortie, rien de plus — pas un tagger. Le projet est
**dormant** : dernière release en 2019, sans évolution depuis, même s'il fonctionne avec les
PyTorch récents.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Ajouter une tête CRF à un tagger d'[[NER et étiquetage de séquence]] : NER, POS, chunking | Projet **dormant** depuis 2019 : aucune évolution, compatibilité à valider soi-même à chaque montée de version PyTorch |
| Les **dépendances entre labels voisins** comptent et un softmax token par token produit des séquences incohérentes | Un gros transformeur fine-tuné rend souvent le CRF **optionnel** : mesurer le gain réel avant de l'ajouter → [[HuggingFace]] |
| | Masquage des séquences de longueur variable à gérer soigneusement — padding et `mask` sont à la charge de l'appelant |
| | Tâche sans structure séquentielle, comme la classification de document : une tête linéaire simple suffit |

## Mise en œuvre

- Installation — `uv add pytorch-crf`
- Point d'entrée — s'utilise comme un `nn.Module` [[PyTorch]], posé en sortie du modèle de séquence
- Prérequis — gérer le `mask` des séquences paddées ; aucune ressource externe
- Exécution — single-node ; suit le device du modèle PyTorch, CPU ou GPU
- Coût — gratuit, MIT, rien à héberger

## Écosystème

### Alternatives

- Se passer de CRF — une tête de token-classification sur transformeur ([[HuggingFace]]) rend souvent la couche superflue ; c'est la voie concurrente réelle, aucune fiche du brain n'occupe le même créneau.

## Ressources

- Documentation — https://pytorch-crf.readthedocs.io
- Dépôt — https://github.com/kmkurn/pytorch-crf

## Voir aussi

- [[NER et étiquetage de séquence]] — la notion où CRF et Viterbi sont décrits
- [[PyTorch]] — le framework hôte
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
