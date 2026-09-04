---
role: brique
nom: NLTK
alias: [Natural Language Toolkit, nltk]
pitch: "Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique."
categorie: ml/nlp
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[spaCy]]"]
complements: []
tags: [nlp, tokenization, text-classification]
url_docs: https://www.nltk.org/
url_repo: https://github.com/nltk/nltk
---

# NLTK

<!-- AUTO:BANDEAU:START -->
> Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque historique de **NLP classique** en Python, née en 2001 et pensée pour
l'enseignement et la recherche. Elle couvre une large palette d'outils symboliques et
statistiques — tokenisation, stemming (Porter, Snowball), lemmatisation par WordNet, étiquetage
morphosyntaxique, parsing, classification — et surtout des dizaines de **corpus et lexiques**
téléchargeables : WordNet, stopwords, treebanks, FrameNet. Ces ressources vivent **hors du
paquet** et se récupèrent explicitement (`nltk.download`), ce qui est la première friction
rencontrée. Accompagnée du livre *NLP with Python*, son ADN reste didactique : montrer comment
les briques fonctionnent, plus que servir du débit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Apprendre ou enseigner le [[Traitement du langage naturel]] : chaque algorithme classique est montré explicitement |  |
| Accéder à des corpus et ressources prêts à l'emploi : WordNet, stopwords, treebanks, FrameNet | Support **multilingue inégal**, très centré anglais : pour le français, [[spaCy]] est souvent plus direct |
| Prototyper une baseline linguistique : stemming, n-grammes, collocations, classification naïve Bayes ([[Classification de texte]]) | Pipeline de production sous contrainte de latence : l'API objet par objet n'est pas optimisée pour le volume |
| Tâches ponctuelles de préparation : tokenisation ([[Tokenization]]), segmentation de phrases, fréquences |  |

## Mise en œuvre

- Installation — `uv add nltk`, puis les ressources séparément : `python -m nltk.downloader punkt wordnet stopwords`
- Point d'entrée — API Python objet par objet ; un `LookupError` au premier appel signale une ressource non téléchargée, pas un bug
- Prérequis — espace disque pour les corpus, gérés hors paquet
- Exécution — single-node, CPU, traitement en mémoire ; aucun modèle neuronal lourd à charger
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

## Ressources

- Documentation — https://www.nltk.org/
- Dépôt — https://github.com/nltk/nltk

## Voir aussi

- [[Traitement du langage naturel]] — la notion chapeau du dossier, dont NLTK est la référence classique
- [[Tokenization]] · [[Classification de texte]] — les tâches couvertes
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
