---
galaxie: wiki
type: concept
nom: Fuzzy matching & similarité de chaînes
alias: [fuzzy matching, similarité de chaînes, string matching, approximate string matching, distance d'édition, Levenshtein, Jaro-Winkler, record linkage, déduplication]
categorie: concept/nlp
domaines: [data-eng, data-sci]
tags: [string-matching, nlp, information-retrieval, feature-engineering]
---

# Fuzzy matching & similarité de chaînes

## Aperçu

- Mesurer à quel point deux chaînes se **ressemblent** malgré fautes, abréviations, variations d'ordre ou de casse — pour rapprocher des libellés qui ne sont pas identiques au caractère près.
- Usages : déduplication, rapprochement de référentiels (*record linkage*), normalisation de saisies, recherche tolérante aux fautes, nettoyage de données collectées.

## Concepts clés

### Distance d'édition (Levenshtein)
- Nombre minimal d'**insertions, suppressions, substitutions** pour transformer une chaîne en une autre. Damerau-Levenshtein ajoute la transposition (inversion de deux lettres voisines).
- Calculée par programmation dynamique en $O(mn)$. Capte bien les fautes de frappe ; coûteuse sur de longs textes.

### Jaro et Jaro-Winkler
- Jaro : score fondé sur le nombre de caractères communs (dans une fenêtre) et de transpositions. Conçu pour des chaînes courtes — noms, identifiants.
- Jaro-Winkler : bonifie les chaînes partageant un **préfixe commun**, adapté aux noms propres. Référence historique du record linkage.

### Similarité par tokens
- Découper en mots/tokens et comparer les ensembles, insensible à l'ordre : **token-set** et **token-sort** (popularisés par `fuzzywuzzy` / `RapidFuzz`). Robuste à « Jean Dupont » vs « Dupont, Jean ».
- Jaccard sur n-grammes de caractères : robuste aux fautes internes, base des index de *blocking*.

### Phonétique
- Soundex, Metaphone : coder une chaîne par sa **prononciation** pour rapprocher des homophones (« Smith » / « Smyth »). Surtout efficace en anglais.

### Lexical vs sémantique
- Ces mesures restent **lexicales** : « voiture » et « automobile » sont distants. Pour la proximité de **sens**, passer aux [[embeddings]] et à la similarité cosinus.

## Les maths, simplement

- Levenshtein : récurrence $d(i,j) = \min\{d(i{-}1,j){+}1,\; d(i,j{-}1){+}1,\; d(i{-}1,j{-}1){+}\mathbb{1}[a_i\neq b_j]\}$.
- Similarité normalisée : $\text{sim} = 1 - \dfrac{d(a,b)}{\max(|a|,|b|)} \in [0,1]$.
- Jaccard sur ensembles de tokens : $J(A,B) = \dfrac{|A\cap B|}{|A\cup B|}$.

## En pratique

- Le coût est quadratique par paire et explose en $O(n^2)$ paires : faire du **blocking / indexing** d'abord (regrouper les candidats par clé grossière, n-grammes, ou ANN sur [[embeddings]]), puis scorer finement dans chaque bloc.
- Choisir la mesure selon la donnée : Jaro-Winkler pour des noms, token-set pour des libellés réordonnés, Levenshtein pour des codes courts.
- Calibrer un seuil de décision sur des paires étiquetées ; au-delà, c'est un problème de [[Recherche d'information]] (rappel/précision) et d'[[Ingénierie des caractéristiques]] (la similarité devient une feature).
- Outils Python : `RapidFuzz` (rapide, successeur de `fuzzywuzzy`), `jellyfish` (Jaro-Winkler, Soundex), `recordlinkage`, `dedupe` (record linkage par apprentissage actif).

## Approches voisines & alternatives

- [[TF-IDF]], [[BM25]] — similarité lexicale pondérée au niveau document, complémentaire des distances caractère.
- [[embeddings]] — la similarité **sémantique** dense, là où le lexical échoue.
- [[Recherche d'information]] — le cadre rappel/précision pour rapprocher à grande échelle.
- [[NER et étiquetage de séquence]] — extraire les entités à apparier avant de les comparer.
- [[Traitement du langage naturel]] — page chapeau du sous-domaine.
- [[EDA automatisée & profiling]], [[Web scraping]] — déduplication et nettoyage de données collectées.

## Pour aller plus loin

- Levenshtein (1966) — *Binary codes capable of correcting deletions, insertions, and reversals*.
- Winkler (1990) — *String Comparator Metrics and Enhanced Decision Rules in the Fellegi-Sunter Model of Record Linkage*.
- Christen (2012) — *Data Matching* (record linkage, déduplication).
