---
role: brique
nom: spaCy
alias: [spacy, explosion spacy]
pitch: "Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs."
categorie: ml/nlp
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[GLiNER]]", "[[NLTK]]"]
complements: ["[[HuggingFace]]"]
tags: [nlp, ner, sequence-labeling, tokenization]
url_docs: https://spacy.io
url_repo: https://github.com/explosion/spaCy
---

# spaCy

<!-- AUTO:BANDEAU:START -->
> Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-24 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de **NLP industriel** signée Explosion : des pipelines pré-entraînés pour 70+
langues qui enchaînent tokenisation, étiquetage morphosyntaxique, analyse en dépendances,
lemmatisation et **NER**, sous une API stable et rapide écrite en Cython. Un objet `nlp` traite
un texte en un appel, ses composants étant remplaçables et entraînables. La contrainte qui
structure l'usage est que son **NER est borné aux types appris** par le modèle chargé :
étendre la couverture demande d'entraîner, pas de configurer. Les modèles se déclinent en
tailles (`sm` / `md` / `lg` / `trf`), et le choix de la taille et de la langue commande
directement le compromis vitesse / précision.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire entités, POS, dépendances rapidement, sans entraîner de modèle |  |
| NER et [[NER et étiquetage de séquence]] de production sur du volume, avec un CPU efficace |  |
| Pré-traitement linguistique — tokenisation, lemmatisation — en amont d'un pipeline ML | Le NER est limité aux **types appris** par le modèle : des types custom imposent d'entraîner, ou de passer à [[GLiNER]] |
| Entraîner ou fine-tuner un pipeline custom (`spacy train`, transformeurs via `spacy-transformers`) | Tâches non linguistiques — classification tabulaire, recherche pure → [[Scikit-Learn]] |
| | Code hérité en v2 : la configuration a été repensée en v3 (config-driven, transformeurs), la migration n'est pas transparente |

## Mise en œuvre

- Installation — `uv add spacy`, puis un modèle : `python -m spacy download fr_core_news_sm`
- Point d'entrée — API Python : un objet `nlp` appelé sur le texte, `nlp.pipe` pour le batch
- Prérequis — choisir la bonne langue et la bonne taille de modèle (`sm` rapide et moins précis, jusqu'à `trf`) ; viser la v3
- Exécution — single-node ; CPU très efficace, GPU optionnel pour les pipelines transformeurs
- Coût — gratuit, MIT, rien à héberger

## Écosystème

### Alternatives

- [[GLiNER]] — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger.
- [[NLTK]] — Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique.

### Compléments

- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes — le fine-tuning de transformeurs, complément plus que substitut, branché via `spacy-transformers`.

## Ressources

- Documentation — https://spacy.io
- Dépôt — https://github.com/explosion/spaCy

## Voir aussi

- [[NER et étiquetage de séquence]] — son cas d'usage central
- [[Tokenization]] · [[Classification de texte]] — les autres tâches couvertes
- [[Traitement du langage naturel]] — la notion chapeau du dossier
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
