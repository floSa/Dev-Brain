---
galaxie: dev
type: service
nom: spaCy
alias: [spacy, explosion spacy]
pitch: "Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/GLiNER|GLiNER]]", "[[Dev/Services/NLTK|NLTK]]"]
remplace_par: []
status: actif
tags: [nlp, ner, sequence-labeling, tokenization]
url_docs: https://spacy.io
url_repo: https://github.com/explosion/spaCy
---

# spaCy

## Pourquoi

Bibliothèque de **NLP industriel** signée Explosion : des pipelines pré-entraînés pour 70+ langues qui enchaînent tokenisation, étiquetage morphosyntaxique (POS), analyse en dépendances, lemmatisation et **NER**, sous une API stable et rapide (Cython). Pensée pour la **production** plus que la recherche : un objet `nlp` traite un texte en un appel, avec des composants remplaçables et entraînables.

## Quand l'utiliser

- Extraire entités, POS, dépendances rapidement, sans entraîner de modèle.
- NER / [[NER et étiquetage de séquence|étiquetage de séquence]] de production sur du volume (CPU efficace).
- Pré-traitement linguistique (tokenisation, lemmatisation) en amont d'un pipeline ML.
- Entraîner ou fine-tuner un pipeline custom (`spacy train`, transformeurs via `spacy-transformers`).

## Quand NE PAS l'utiliser

- NER **zero-shot** sur des types d'entités arbitraires sans données → [[Dev/Services/GLiNER|GLiNER]].
- Fine-tuner un gros transformeur de l'état de l'art pour une tâche unique → [[Dev/Services/HuggingFace|HuggingFace]].
- Tâches non linguistiques (classification tabulaire, recherche pure) → [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add spacy` + un modèle (`python -m spacy download fr_core_news_sm`).
- **Single-node** ; CPU très efficace, GPU optionnel (pipelines transformeurs). `nlp.pipe` pour le batch.
- Modèles de tailles variées (`sm` / `md` / `lg` / `trf`) : compromis vitesse / précision.

## Pièges

- Choisir la **bonne taille de modèle** et la bonne langue (`fr_core_news_*`) : un `sm` est rapide mais moins précis.
- NER limité aux **types appris** par le modèle ; pour des types custom, entraîner ou passer à [[Dev/Services/GLiNER|GLiNER]].
- Migration v2 → v3 : configuration repensée (config-driven, transformeurs) — viser la v3.

## Alternatives

- [[Dev/Services/GLiNER|GLiNER]] — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger.
- [[Dev/Services/NLTK|NLTK]] — Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique.

## Liens

- [[NER et étiquetage de séquence]] — son cas d'usage central.
- [[Tokenization]] · [[Classification de texte]] — autres tâches couvertes.
- [[Traitement du langage naturel]] — page chapeau.
- [[Dev/Services/HuggingFace|HuggingFace]] — pour le fine-tuning de transformeurs ; complément plus que substitut.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://spacy.io
