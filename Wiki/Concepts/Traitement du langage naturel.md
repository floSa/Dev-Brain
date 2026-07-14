---
galaxie: wiki
type: concept
nom: Traitement du langage naturel
alias: [NLP, natural language processing, TALN, TAL, traitement automatique du langage]
categorie: concept/nlp
domaines: [data-sci, ml-eng, ai-eng]
tags: [nlp]
---

# Traitement du langage naturel

## Aperçu

- Représenter, analyser et exploiter du **texte** en langage humain : rechercher, extraire de l'information, classer.
- En data/ML : transformer du texte non structuré en entrées exploitables, du sac-de-mots aux représentations neuronales.
- Page chapeau : oriente vers les cinq briques ci-dessous.

## Concepts clés

### Du symbole au vecteur
- Le texte est discret et symbolique ; tout pipeline commence par le **découper** ([[Tokenization]]), puis le **représenter** : sparse ([[TF-IDF]]) ou dense ([[embeddings]]).

### Deux grandes familles de tâches
- **Au niveau document** : un label global → [[Classification de texte]] (sentiment, thème, spam).
- **Au niveau token** : un label par mot → [[NER et étiquetage de séquence|étiquetage de séquence]] (entités nommées, parties du discours).

### Retrouver l'information
- [[Recherche d'information]] : classer des documents par pertinence — lexical ([[TF-IDF]], [[BM25]]), dense ([[embeddings]]), hybride. Fonde le retrieval du [[RAG]].

### Baseline → embeddings → LLM
- Trajectoire typique de sophistication : un baseline lexical (TF-IDF + classifieur linéaire) d'abord, des embeddings / transformeurs ensuite, un LLM en dernier recours. Mesurer le gain à chaque palier.

### Les cinq briques
- [[TF-IDF]] — pondération sparse des termes (baseline lexical).
- [[BM25]] — la fonction de classement lexicale de référence.
- [[Recherche d'information]] — lexical / dense / hybride + re-ranking.
- [[NER et étiquetage de séquence]] — extraire et typer (IOB/BILOU, CRF, Viterbi).
- [[Classification de texte]] — catégoriser un document (baseline → embeddings → LLM).

## Les maths, simplement

- Représentation sparse : un document devient un vecteur de taille = vocabulaire, pondéré $\text{tf}\times\text{idf}$ ; proximité mesurée par cosinus.
- Représentation dense : un encodeur appris $f : \text{texte} \to \mathbb{R}^d$ place les sens proches côte à côte — cf. [[embeddings]].

## En pratique

- Pile Python : [[Dev/Services/Scikit-Learn|scikit-learn]] (TF-IDF + classifieurs), [[Dev/Services/NLTK|NLTK]] (NLP classique / pédagogique, corpus), [[Dev/Services/spaCy|spaCy]] (tokenisation, NER, lemmatisation), [[Dev/Services/HuggingFace|HuggingFace]] / [[Dev/Services/sentence-transformers|sentence-transformers]] (transformeurs, embeddings), [[Dev/Services/rank-bm25|rank-bm25]] (lexical), [[Dev/Services/GLiNER|GLiNER]] / [[Dev/Services/SetFit|SetFit]] (zero / few-shot).
- Pipeline type : **nettoyer / tokeniser** → **représenter** (sparse ou dense) → **tâche** (classer, étiqueter, rechercher) → **évaluer** (F1, NDCG).
- Pour le français : lemmatiser (flexion riche), choisir des modèles adaptés (CamemBERT, embeddings multilingues).
- Pièges récurrents : [[Data leakage]] en fittant le vectorizer sur train + test ; ignorer le déséquilibre des classes → [[Imbalanced classification]].

## Approches voisines & alternatives

- [[TF-IDF]], [[BM25]], [[Recherche d'information]], [[NER et étiquetage de séquence]], [[Classification de texte]] — les cinq briques détaillées.
- [[Tokenization]] — le prétraitement commun à toutes.
- [[embeddings]] — la représentation dense, pivot des approches modernes.
- [[RAG]] / [[Hybrid retrieval]] / [[Reranking]] — le prolongement « IA générative » de la recherche d'information.
- [[Transformer architectures]] — l'architecture qui sous-tend le NLP neuronal actuel.

## Pour aller plus loin

- Jurafsky & Martin — *Speech and Language Processing* (référence libre, 3e édition en ligne).
- Manning, Raghavan & Schütze — *Introduction to Information Retrieval* (versant recherche).
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]] — les libs Python du domaine en un tableau.
