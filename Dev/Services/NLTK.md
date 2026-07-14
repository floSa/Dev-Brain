---
galaxie: dev
type: service
nom: NLTK
alias: [Natural Language Toolkit, nltk]
pitch: "Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/spaCy|spaCy]]"]
remplace_par: []
status: actif
tags: [nlp, tokenization, text-classification]
url_docs: https://www.nltk.org/
url_repo: https://github.com/nltk/nltk
---

# NLTK

## Pourquoi

La bibliothèque historique de **NLP classique** en Python (depuis 2001), pensée pour l'**enseignement et la recherche**. Couvre une large palette d'outils symboliques et statistiques : tokenisation, stemming (Porter, Snowball), lemmatisation (WordNet), étiquetage morphosyntaxique, parsing, classification, et surtout des dizaines de **corpus et lexiques** téléchargeables (`nltk.download`). Accompagnée du livre *NLP with Python* — son ADN reste didactique : montrer comment les briques fonctionnent, plus que servir en production.

## Quand l'utiliser

- Apprendre / enseigner le [[Traitement du langage naturel]] : voir chaque algorithme classique explicitement.
- Accéder à des **corpus et ressources** prêts à l'emploi (WordNet, stopwords, treebanks, FrameNet).
- Prototyper une baseline linguistique (stemming, n-grammes, collocations, [[Classification de texte|classification]] naïve Bayes).
- Tâches ponctuelles de préparation : [[Tokenization|tokenisation]], segmentation de phrases, fréquences.

## Quand NE PAS l'utiliser

- NLP **industriel** rapide et multilingue (pipelines pré-entraînés, [[NER et étiquetage de séquence|NER]], dépendances) → [[Dev/Services/spaCy|spaCy]].
- État de l'art par transformeurs (fine-tuning, embeddings contextuels) → [[Dev/Services/HuggingFace|HuggingFace]].
- Pipeline de production sous contrainte de latence : l'API objet par objet de NLTK n'est pas optimisée pour le débit.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add nltk` + téléchargement des ressources (`python -m nltk.downloader ...`).
- **Single-node**, CPU, traitement en mémoire ; pas de modèle neuronal lourd à charger.
- Ressources (corpus, modèles) gérées hors paquet, à télécharger explicitement.

## Pièges

- Oublier `nltk.download('punkt' / 'wordnet' / 'stopwords'...)` → `LookupError` au premier appel : les ressources ne sont pas embarquées.
- Support **multilingue** inégal : très centré anglais ; pour le français, spaCy est souvent plus direct.
- API verbeuse et lente sur du volume — c'est un outil d'apprentissage et de prototypage, pas un moteur de production.

## Alternatives

- [[Dev/Services/spaCy|spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

## Liens

- [[Traitement du langage naturel]] — page chapeau ; NLTK en est la référence classique/pédagogique.
- [[Tokenization]] · [[Classification de texte]] — tâches couvertes.
- [[Dev/Services/spaCy|spaCy]] — la suite industrielle quand on passe du cours à la production.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://www.nltk.org/
