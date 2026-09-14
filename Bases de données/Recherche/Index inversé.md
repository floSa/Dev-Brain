---
role: notion
nom: Index inversé
alias: [inverted index, index inverse, postings list, liste de postings]
categorie: database/recherche
domaines: [data-eng, ai-eng]
tags: [search, information-retrieval]
---

# Index inversé

## Aperçu

- Structure de données qui associe chaque **terme** à la liste des documents qui le contiennent. Le sens est « inversé » par rapport au stockage naturel, où un document contient des termes.
- C'est la structure sur laquelle repose la recherche plein texte : [[Lucene]], et donc [[Elasticsearch]], [[OpenSearch]] et [[Apache Solr]], ainsi que [[Meilisearch]] et [[Typesense]], répondent à une requête en lisant quelques listes, sans parcourir le corpus.

## Concepts clés

### Dictionnaire et postings
- Un **dictionnaire** liste tous les termes distincts du corpus. Chacun pointe vers sa **liste de postings** : les identifiants des documents où il apparaît, souvent avec la fréquence et les positions du terme.
- Trouver les documents qui contiennent un mot revient à une recherche dans le dictionnaire, puis à la lecture d'une liste. Le coût dépend du nombre de documents qui portent le terme, pas de la taille du corpus.

### Analyse : de la phrase aux termes
- Avant l'indexation, le texte passe par une **analyse** : découpage en jetons (tokenisation), normalisation de la casse et des accents, suppression éventuelle de mots vides, racinisation.
- La même analyse doit s'appliquer à la requête, sinon un terme écrit ne retrouve pas le terme indexé. C'est la première cause de « le moteur ne trouve pas mon mot ».

### Requêtes booléennes et phrases
- Un `ET` entre deux termes est l'**intersection** de leurs listes de postings ; un `OU`, leur union. Une recherche de phrase exige en plus des positions consécutives, d'où leur présence dans l'index.

### Du décompte au classement
- Les postings portent de quoi calculer un score : la fréquence du terme dans le document, le nombre de documents qui le contiennent, la longueur du document. [[BM25]] et [[TF-IDF]] s'en servent, cf. [[Recherche d'information]].

### Ajouter un document
- Un index inversé se modifie mal en place. Les moteurs de la famille Lucene écrivent des blocs d'index et les fusionnent en tâche de fond ; c'est pourquoi un document n'est visible qu'après un rafraîchissement, pas à l'`INSERT` (cf. [[Elasticsearch]]).

## Les maths, simplement

- Pour une requête à deux termes $t_1$ et $t_2$ de listes de postings de tailles $n_1$ et $n_2$, l'intersection coûte de l'ordre de $O(n_1 + n_2)$ en parcourant les deux listes triées, et moins avec des sauts. Le coût suit la **fréquence des termes**, pas la taille $N$ du corpus.
- Le terme le plus rare est donc le plus économique à lire en premier : une liste courte borne le nombre de candidats à tester.

## En pratique

- Un mot absent du dictionnaire ne renvoie rien, quelle que soit sa proximité de sens avec un mot présent : c'est la limite lexicale, que la [[Recherche sémantique]] contourne.
- Soigner l'analyse pour la langue du corpus (accents, élisions, pluriels) avant de toucher aux réglages de scoring.
- Un index inversé occupe de la place et se reconstruit, pas se corrige : concevoir le mapping ou le schéma avant d'indexer beaucoup.
- Piège de vocabulaire : « index inversé » désigne aussi, en recherche vectorielle, un partitionnement de l'espace en cellules (IVF). L'idée est la même — relier une clé à la liste de ce qu'elle contient — mais la clé y est une cellule, non un terme. Cf. [[Index ANN — internes]].

## Approches voisines & alternatives

- [[Lucene]] — la bibliothèque qui construit et interroge ces index.
- [[Recherche vectorielle approximative]] — l'autre façon de retrouver un document : par proximité de vecteurs, non par mot.
- [[Recherche sémantique]] — chercher par le sens, là où l'index inversé cherche par le mot.
- [[Hybrid retrieval]] — les deux réunis dans la même requête.
- [[bm25s]] — le classement BM25 précalculé à l'indexation en matrices creuses, sans moteur.

## Pour aller plus loin

- Manning, Raghavan, Schütze — *Introduction to Information Retrieval*, chapitre sur la construction et la compression de l'index inversé.
- [[Recherche d'information]] — la discipline générale.
