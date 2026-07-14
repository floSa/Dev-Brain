---
galaxie: wiki
type: concept
nom: TF-IDF
alias: [tf-idf, term frequency-inverse document frequency, pondération tf-idf]
categorie: concept/nlp
domaines: [data-sci, ai-eng]
tags: [nlp, information-retrieval, feature-engineering]
---

# TF-IDF

## Aperçu

- Pondérer chaque terme d'un document par sa fréquence locale (**TF**) corrigée de sa rareté dans le corpus (**IDF**) : un mot fréquent dans *ce* document mais rare ailleurs est discriminant.
- Produit une représentation **sparse** du texte (sac-de-mots pondéré) — base historique de la recherche lexicale et baseline solide pour la [[Classification de texte]].

## Concepts clés

### TF — fréquence du terme
- Combien de fois un terme apparaît dans le document. Variantes : brute, logarithmique ($1+\log f$), normalisée par la longueur.

### IDF — fréquence inverse de document
- Pénalise les termes présents partout (« le », « de »). Plus un terme est rare dans le corpus, plus son IDF est élevé — donc plus il est informatif.

### Sac-de-mots & sparsité
- Le texte devient un vecteur de taille = vocabulaire, presque tout à zéro. Aucune notion d'ordre ni de sens : « banque rivière » et « rivière banque » sont identiques. C'est la limite que lèvent les [[embeddings]].

### Le prétraitement décide de tout
- Tokenisation, minuscules, stop-words, stemming / lemmatisation, n-grammes : le résultat dépend fortement de ces choix, surtout sur une langue flexionnelle comme le français.

## Les maths, simplement

- $\text{tfidf}(t, d) = \text{tf}(t,d)\cdot \text{idf}(t)$, avec $\text{idf}(t) = \log\dfrac{N}{1 + n_t}$ — $N$ le nombre de documents, $n_t$ le nombre de documents contenant $t$.
- On **normalise** ensuite chaque vecteur document en L2 : la similarité cosinus entre deux vecteurs TF-IDF mesure alors leur proximité lexicale.

## En pratique

- `TfidfVectorizer` de [[Dev/Services/Scikit-Learn|scikit-learn]] : `fit_transform` sur le corpus, sortie sparse directement consommable par une [[Régression logistique]] ou un SVM linéaire.
- Régler `ngram_range`, `min_df` / `max_df`, `sublinear_tf` ; lemmatiser ([[Dev/Services/spaCy|spaCy]]) pour le français.
- Baseline imbattable en rapport qualité/coût sur corpus petits/moyens et vocabulaire spécialisé, avant de sortir l'artillerie neuronale.
- Piège : fitter le vectorizer sur train + test → [[Data leakage]]. Fitter sur le train seul, transformer le test.

## Approches voisines & alternatives

- [[BM25]] — le raffinement de TF-IDF pour le **classement** en recherche (saturation de TF, normalisation de longueur).
- [[embeddings]] — la représentation **dense** apprise, qui capte le sens là où TF-IDF reste lexical.
- [[Recherche d'information]] — TF-IDF en est la brique de pondération historique.
- [[Classification de texte]] — TF-IDF + classifieur linéaire = le baseline de référence.
- [[Ingénierie des caractéristiques]] — TF-IDF vu comme extraction de features textuelles.
- [[Traitement du langage naturel]] — page chapeau du sous-domaine.

## Pour aller plus loin

- Spärck Jones (1972) — *A statistical interpretation of term specificity and its application in retrieval* (origine de l'IDF).
- Manning, Raghavan & Schütze — *Introduction to Information Retrieval*, ch. 6 (pondération et modèle vectoriel).
