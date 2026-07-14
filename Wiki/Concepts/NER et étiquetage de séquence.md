---
galaxie: wiki
type: concept
nom: NER et étiquetage de séquence
alias: [NER, named entity recognition, reconnaissance d'entités nommées, étiquetage de séquence, sequence labeling, token classification, BiLSTM-CRF]
categorie: concept/nlp
domaines: [data-sci, ml-eng]
tags: [nlp, ner, sequence-labeling, supervised]
---

# NER et étiquetage de séquence

## Aperçu

- **NER** (reconnaissance d'entités nommées) : repérer et typer les mentions d'un texte — personnes, organisations, lieux, dates, montants. C'est un cas particulier d'**étiquetage de séquence** : attribuer un label à chaque token.
- Brique d'extraction d'information : anonymisation, peuplement de bases, enrichissement de [[RAG]].

## Concepts clés

### Schémas d'étiquetage IOB / BILOU
- Encoder des spans multi-tokens token par token : **IOB2** (`B`-egin, `I`-nside, `O`-utside), **BILOU** (ajoute `L`-ast, `U`-nit), plus expressif. « New York » → `B-LOC I-LOC `.

### CRF — champ aléatoire conditionnel
- Modélise les **dépendances entre labels voisins** (un `I-PER` ne suit pas un `O`), là où un classifieur token par token les ignore. Couche de sortie classique d'un tagger.

### Décodage de Viterbi
- Algorithme de **programmation dynamique** qui trouve la séquence de labels la plus probable sous les contraintes du CRF, en temps linéaire dans la longueur de la séquence.

### BiLSTM-CRF → transformeurs
- Architecture historique : embeddings → BiLSTM (contexte bidirectionnel) → CRF. Aujourd'hui : un encodeur [[Transformer architectures|transformeur]] (BERT, CamemBERT) fine-tuné en token classification, parfois coiffé d'un CRF.

### Zero-shot
- Modèles type GLiNER : extraire des types d'entités **non vus à l'entraînement**, décrits en langage naturel.

## Les maths, simplement

- CRF linéaire : $P(y\mid x) = \dfrac{1}{Z(x)}\exp\!\bigl(\sum_t \sum_k \lambda_k\, f_k(y_{t-1}, y_t, x, t)\bigr)$ — score global d'une séquence de labels $y$, normalisé par $Z(x)$. Les features $f_k$ couplent labels voisins et observations.
- Décodage : $\hat y = \arg\max_y P(y\mid x)$, résolu par **Viterbi** ; entraînement par maximum de vraisemblance (variante de l'[[Cross-entropy|entropie croisée]] sur séquences).

## En pratique

- [[Dev/Services/spaCy|spaCy]] pour un NER prêt à l'emploi et rapide ; [[Dev/Services/HuggingFace|HuggingFace]] `token-classification` (BERT / CamemBERT) pour le fine-tuning ; [[Dev/Services/pytorch-crf|pytorch-crf]] pour la couche CRF ; [[Dev/Services/GLiNER|GLiNER]] pour le zero-shot.
- Annoter en IOB / BILOU avec un outil dédié (Label Studio, Prodigy) ; la cohérence des spans est le nerf de la guerre.
- Évaluer en **F1 au niveau entité** (span exact) avec [[Dev/Services/seqeval|seqeval]], pas au niveau token : une entité partiellement correcte compte comme fausse.
- Piège : aligner les labels sur les **sous-tokens** du tokenizer (un mot peut être découpé en plusieurs) — cf. [[Tokenization]].

## Approches voisines & alternatives

- [[Construction de graphes de connaissances]] — débouché : la NER fournit les entités, à relier ensuite par extraction de relations.
- [[Classification de texte]] — la sœur : un label pour **tout** le document, pas un par token.
- [[Tokenization]] — le découpage qui conditionne l'alignement des labels.
- [[Transformer architectures]] / [[Self-attention]] — l'ossature des taggers modernes.
- [[embeddings]] — représentations de tokens en entrée du modèle.
- [[Cross-entropy]] — la perte d'apprentissage (au niveau token ou séquence).
- [[Traitement du langage naturel]] — page chapeau du sous-domaine.

## Pour aller plus loin

- Lafferty, McCallum & Pereira (2001) — *Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data*.
- Lample et al. (2016) — *Neural Architectures for Named Entity Recognition* (BiLSTM-CRF).
