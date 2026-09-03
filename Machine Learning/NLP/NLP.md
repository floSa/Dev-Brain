---
role: hub
nom: NLP
alias: [traitement automatique du langage, TAL]
pitch: Les bibliothèques dont l'entrée est du texte sans génération — découper, étiqueter, classer, extraire, retrouver.
domaines: [ml-eng, data-sci]
tags: [nlp, ner, sequence-labeling, text-classification, information-retrieval, tokenization, string-matching]
---

# NLP

> Les bibliothèques dont l'entrée est du texte sans génération — découper, étiqueter, classer, extraire, retrouver.

## Ce qu'il faut comprendre

- **La confusion à lever d'abord : ce dossier n'est pas [[LLM & IA générative]].** Un LLM *génère* du texte et se pilote par un prompt ; ce qui est ici *analyse* du texte et se pilote par un modèle entraîné sur une tâche fermée. La distinction n'est pas académique, elle est économique : classer un million de documents avec [[spaCy]] coûte quelques minutes de CPU, le faire avec un LLM coûte une facture. Le réflexe « un LLM fera l'affaire » est souvent vrai en qualité et faux en coût, en latence et en reproductibilité.
- **[[Traitement du langage naturel]] pose le cadre**, et la chaîne classique reste utile même à l'ère des LLM : segmenter, étiqueter, extraire, indexer. Chaque étape a ses métriques, ses erreurs typiques et ses modèles légers.
- **Tout commence par la tokenisation, et c'est là que se jouent les surprises** — un modèle ne voit jamais des mots. Le découpage sous-mot est un modèle entraîné, pas une règle : il conditionne la taille du vocabulaire, la longueur des séquences et donc le coût.
- **L'étiquetage de séquence est le cœur de l'extraction structurée** : [[NER et étiquetage de séquence]]. Deux faits pratiques dominent — l'évaluation se fait à l'entité et non au token, sinon les chiffres sont faux, et une couche de dépendance entre labels voisins améliore encore les modèles récents.
- **La classification de texte est le problème le plus courant et le plus mal outillé** : [[Classification de texte]]. La question utile n'est pas « quel modèle » mais « combien d'exemples annotés ai-je » — quelques dizaines suffisent aux approches few-shot, quelques milliers justifient un fine-tuning classique.
- **La recherche d'information est un domaine à part entière, et le lexical n'est pas mort.** [[Recherche d'information]] pose le cadre, [[TF-IDF]] et [[BM25]] restent la base solide — [[BM25]] est encore la moitié gagnante de tout retrieval hybride, y compris dans un pipeline RAG moderne. Les moteurs et les bases vectorielles sont ailleurs : [[Recherche]] et [[Vectoriel]].
- **Le rapprochement approximatif de chaînes est un besoin transverse**, souvent confondu avec du NLP sémantique alors qu'il n'en est pas : [[Fuzzy matching & similarité de chaînes]] — déduplication de référentiels, réconciliation de noms, appariement de libellés.
- Enfin, la passerelle vers le reste : représenter un texte par un vecteur relève des [[embeddings]], et l'outillage est au niveau du domaine avec [[sentence-transformers]].

## Choisir

- Un pipeline NLP industriel — tokenisation, POS, dépendances, NER — rapide et multilingue → [[spaCy]].
- Extraire des entités dont les types ne sont pas connus à l'avance, sans réentraîner → [[GLiNER]].
- Classer du texte avec quelques dizaines d'exemples seulement → [[SetFit]].
- Ajouter une couche CRF à un tagger PyTorch → [[pytorch-crf]].
- Entraîner ou réutiliser un tokeniseur sous-mot indépendant de la langue → [[sentencepiece]].
- Enseigner, prototyper, ou accéder aux corpus et algorithmes classiques → [[NLTK]].
- Mesurer un modèle d'étiquetage au niveau entité → [[seqeval]]. Cf. [[Comparatif - NLP]].
- Générer, résumer, dialoguer, ou extraire par prompt → [[LLM & IA générative]], pas ce dossier.

<!-- AUTO:START -->
### Notions
- [[BM25]] — domaines : ai-eng, data-sci
- [[Classification de texte]] — domaines : data-sci, ml-eng
- [[Fuzzy matching & similarité de chaînes]] — domaines : data-eng, data-sci
- [[NER et étiquetage de séquence]] — domaines : data-sci, ml-eng
- [[Recherche d'information]] — domaines : ai-eng, data-sci
- [[TF-IDF]] — domaines : data-sci, ai-eng
- [[Traitement du langage naturel]] — domaines : data-sci, ml-eng, ai-eng

### Briques
- [[GLiNER]] — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger.
- [[NLTK]] — Bibliothèque NLP classique et pédagogique en Python — tokenisation, stemming, POS, corpus et algorithmes de référence, riche pour l'enseignement et le prototypage linguistique.
- [[pytorch-crf]] — Couche CRF (champ aléatoire conditionnel) pour PyTorch — modélise les dépendances entre labels voisins et décode par Viterbi ; brique de sortie classique d'un tagger d'étiquetage de séquence.
- [[sentencepiece]] — Tokeniseur sous-mot de Google, indépendant de la langue — BPE et modèle Unigram entraînés directement sur du texte brut (Unicode/octets, sans pré-tokenisation), implémentation C++ et bindings Python.
- [[SetFit]] — Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM.
- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs.

### Comparatifs
- [[Comparatif - NLP]]
<!-- AUTO:END -->

## Notes
