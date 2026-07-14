---
galaxie: dev
type: service
nom: SetFit
alias: [setfit, few-shot text classification]
pitch: "Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [text-classification, nlp, fine-tuning]
url_docs: https://huggingface.co/docs/setfit
url_repo: https://github.com/huggingface/setfit
---

# SetFit

## Pourquoi

Méthode de **classification de texte few-shot sans prompt**, signée Hugging Face. En deux temps : fine-tuning **contrastif** d'un [[Dev/Services/sentence-transformers|sentence-transformer]] sur les paires d'exemples, puis entraînement d'une **tête de classification** sur les embeddings obtenus. Résultat : des scores compétitifs avec **quelques dizaines d'exemples par classe**, sans LLM ni prompt à régler, pour un modèle petit et rapide à servir.

## Quand l'utiliser

- [[Classification de texte]] avec **peu de données annotées** (few-shot).
- Remplacer un prompt LLM zero/few-shot par un modèle **léger, déterministe et bon marché** à servir.
- Itérer vite : entraînement en minutes sur CPU / GPU modeste.

## Quand NE PAS l'utiliser

- **Beaucoup** de données annotées → un fine-tuning classique d'encodeur ([[Dev/Services/HuggingFace|HuggingFace]]) peut faire mieux.
- Baseline ultra-simple suffisant → TF-IDF + linéaire ([[Dev/Services/Scikit-Learn|Scikit-Learn]]).
- Tâches génératives ou de raisonnement → un LLM.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add setfit`.
- **Single-node** ; s'appuie sur [[Dev/Services/sentence-transformers|sentence-transformers]] / [[Dev/Services/HuggingFace|HuggingFace]]. GPU utile mais non requis.
- Modèle final petit → inférence rapide et peu coûteuse.

## Pièges

- Sensible au **choix du sentence-transformer** de base et à la qualité des quelques exemples.
- Few-shot ≠ magie : au-delà d'un certain volume, un fine-tuning complet reprend l'avantage.
- Multi-label et déséquilibre demandent une configuration adaptée → [[Imbalanced classification]].

## Alternatives

Pas de substitut direct dans le brain. Les voies concurrentes pour la classification de texte (baseline TF-IDF, fine-tuning de transformeur, prompting LLM) sont décrites dans le concept [[Classification de texte]].

## Liens

- [[Classification de texte]] — son cas d'usage (few-shot).
- [[Dev/Services/sentence-transformers|sentence-transformers]] — le socle qu'il fine-tune.
- [[Dev/Services/HuggingFace|HuggingFace]] — exécution et alternative full-fine-tune.
- [[Traitement du langage naturel]] — page chapeau.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://huggingface.co/docs/setfit
