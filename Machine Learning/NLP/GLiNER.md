---
role: brique
nom: GLiNER
alias: [gliner, generalist ner]
pitch: "Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger."
categorie: ml/nlp
famille: modele
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[spaCy]]"]
complements: []
tags: [ner, nlp, transformers]
url_docs: https://github.com/urchade/GLiNER
url_repo: https://github.com/urchade/GLiNER
---

# GLiNER

<!-- AUTO:BANDEAU:START -->
> Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Modèle de **NER zero-shot**. Au lieu d'une liste figée de types appris à l'entraînement, on lui
**décrit les entités voulues en langage naturel** — « maladie », « numéro de contrat »,
« molécule » — et il les extrait sans réentraînement. Un seul encodeur bidirectionnel compact
suffit, bien plus léger qu'un LLM sollicité par prompt pour la même tâche. La contrepartie est
que la qualité dépend directement de la **formulation des libellés** : les types se travaillent
par itérations, et le zero-shot ne bat pas un modèle entraîné quand les données annotées
existent.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire des types d'entités **custom** sans données annotées ni fine-tuning | Types d'entités stables et volumineux, avec données disponibles : un pipeline entraîné ([[spaCy]], [[HuggingFace]]) sera plus précis et plus rapide |
| Prototyper vite une extraction sur un domaine de niche : médical, juridique, technique | Qualité **variable selon le domaine** et la formulation des types — itérer sur les libellés, sans garantie de convergence |
| Alternative frugale au prompting d'un LLM pour de la NER | Projet jeune, encore en **0.x** : API et modèles mouvants, épingler la version et valider sur ses données |
| | Extraction relationnelle complexe ou raisonnement : hors du périmètre d'un encodeur de NER |

## Mise en œuvre

- Installation — `uv add gliner`
- Point d'entrée — API Python ; modèles tirés du Hub [[HuggingFace]], types d'entités passés en clair à l'appel
- Prérequis — épingler la version : le projet est en 0.x, l'API et les modèles évoluent
- Exécution — single-node ; CPU possible, GPU pour le débit ; empreinte mémoire modérée
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

## Ressources

- Dépôt — https://github.com/urchade/GLiNER

## Voir aussi

- [[NER et étiquetage de séquence]] — son terrain, par la voie zero-shot
- [[Traitement du langage naturel]] — la notion chapeau du dossier
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
