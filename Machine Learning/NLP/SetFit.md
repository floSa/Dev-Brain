---
role: brique
nom: SetFit
alias: [setfit, few-shot text classification]
pitch: "Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM."
categorie: ml/nlp
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[sentence-transformers]]"]
tags: [text-classification, nlp, fine-tuning]
url_docs: https://huggingface.co/docs/setfit
url_repo: https://github.com/huggingface/setfit
---

# SetFit

<!-- AUTO:BANDEAU:START -->
> Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Méthode de **classification de texte few-shot sans prompt**, signée Hugging Face. Elle procède
en deux temps : fine-tuning **contrastif** d'un [[sentence-transformers|sentence-transformer]]
sur les paires d'exemples, puis entraînement d'une **tête de classification** sur les
embeddings obtenus. Résultat : des scores compétitifs avec quelques dizaines d'exemples par
classe, sans LLM ni prompt à régler, et un modèle final petit, déterministe et bon marché à
servir. Le few-shot n'est pas pour autant sans limite : au-delà d'un certain volume d'annotations,
un fine-tuning complet reprend l'avantage.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| [[Classification de texte]] avec peu de données annotées | Beaucoup de données annotées : un fine-tuning classique d'encodeur ([[HuggingFace]]) fait alors mieux |
| Remplacer un prompt LLM zero/few-shot par un modèle léger, déterministe et bon marché à servir | Baseline ultra-simple suffisante : TF-IDF plus un modèle linéaire ([[Scikit-Learn]]) coûte moins cher |
| Itérer vite : entraînement en minutes sur CPU ou GPU modeste | Sensible au **choix du sentence-transformer de base** et à la qualité des quelques exemples fournis |
| | Multi-label ou classes déséquilibrées : la configuration demande un traitement dédié → [[Imbalanced classification]] |
| | Tâches génératives ou de raisonnement : c'est un classifieur, pas un LLM |

## Mise en œuvre

- Installation — `uv add setfit`
- Point d'entrée — API Python : `SetFitTrainer` sur quelques dizaines d'exemples par classe
- Prérequis — un modèle [[sentence-transformers]] de base, tiré du Hub [[HuggingFace]]
- Exécution — single-node ; GPU utile mais non requis, le modèle final est petit et rapide en inférence
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi — le socle que SetFit fine-tune.

## Ressources

- Documentation — https://huggingface.co/docs/setfit
- Dépôt — https://github.com/huggingface/setfit

## Voir aussi

- [[Classification de texte]] — son cas d'usage, et où sont décrites les voies concurrentes : baseline TF-IDF, fine-tuning de transformeur, prompting LLM
- [[Traitement du langage naturel]] — la notion chapeau du dossier
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
