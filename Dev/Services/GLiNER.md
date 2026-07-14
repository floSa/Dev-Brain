---
galaxie: dev
type: service
nom: GLiNER
alias: [gliner, generalist ner]
pitch: "Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/spaCy|spaCy]]"]
remplace_par: []
status: actif
tags: [ner, nlp, transformers]
url_docs: https://github.com/urchade/GLiNER
url_repo: https://github.com/urchade/GLiNER
---

# GLiNER

## Pourquoi

Modèle de **NER zero-shot** : au lieu d'une liste figée de types appris, on lui **décrit les entités voulues en langage naturel** (« maladie », « numéro de contrat », « molécule ») et il les extrait, sans réentraînement. Un seul modèle compact (encodeur bidirectionnel), bien plus léger qu'un LLM, pour une extraction flexible.

## Quand l'utiliser

- Extraire des **types d'entités custom** sans données annotées ni fine-tuning.
- Prototyper vite une extraction sur un domaine de niche (médical, juridique, technique).
- Alternative frugale au prompting d'un LLM pour de la NER.

## Quand NE PAS l'utiliser

- Types d'entités **stables et volumineux** avec données dispo → un pipeline entraîné ([[Dev/Services/spaCy|spaCy]], [[Dev/Services/HuggingFace|HuggingFace]]) sera plus précis et plus rapide.
- Pipeline linguistique complet (POS, dépendances, lemmes) → [[Dev/Services/spaCy|spaCy]].
- Extraction relationnelle complexe / raisonnement → un LLM.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add gliner`, modèles sur le Hub.
- **Single-node** ; CPU possible, GPU pour le débit. Empreinte modérée.
- Encore en **0.x** (API et modèles évoluent) — épingler la version.

## Pièges

- Qualité **variable selon le domaine** et la formulation des types — itérer sur les libellés.
- Projet jeune (0.x) : API mouvante, valider sur ses données.
- Le zero-shot ne bat pas un modèle bien entraîné quand les données existent.

## Alternatives

- [[Dev/Services/spaCy|spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

## Liens

- [[NER et étiquetage de séquence]] — son terrain (la voie zero-shot).
- [[Traitement du langage naturel]] — page chapeau.
- [[Dev/Services/HuggingFace|HuggingFace]] — modèles et exécution.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Repo : https://github.com/urchade/GLiNER
