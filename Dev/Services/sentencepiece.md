---
galaxie: dev
type: service
nom: sentencepiece
alias: [sentence-piece, spm, google sentencepiece]
pitch: "Tokeniseur sous-mot de Google, indépendant de la langue — BPE et modèle Unigram entraînés directement sur du texte brut (Unicode/octets, sans pré-tokenisation), implémentation C++ et bindings Python."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: C++/Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [tokenization, nlp]
url_docs: https://github.com/google/sentencepiece/blob/master/README.md
url_repo: https://github.com/google/sentencepiece
---

# sentencepiece

## Pourquoi

Tokeniseur **sous-mot** de Google, conçu pour être **indépendant de la langue**. Là où la plupart des tokeniseurs supposent une pré-segmentation par espaces, SentencePiece traite la phrase comme une **suite de caractères Unicode bruts** (l'espace devient un symbole `▁`), ce qui le rend réversible et applicable au CJK ou aux langues sans séparateur de mots. Il implémente deux algorithmes d'apprentissage de vocabulaire : **BPE** et le **modèle Unigram** (sa contribution propre, avec la *subword regularization*). L'entraînement se fait directement sur du texte ; le modèle produit (`.model` + `.vocab`) est ensuite utilisé pour encoder/décoder. C'est le tokeniseur derrière de nombreux modèles (T5, ALBERT, XLNet, Llama, Mistral…).

## Quand l'utiliser

- **Entraîner un vocabulaire sous-mot** sur un corpus propre (langue, domaine, code) sans dépendre d'une pré-tokenisation.
- Modèles **multilingues** ou langues sans espaces (japonais, chinois, thaï).
- Reproduire le tokeniseur d'un modèle qui le spécifie (T5, Llama…) : charger son `.model`.
- Besoin d'un encodage **réversible** et déterministe texte ↔ ids.

## Quand NE PAS l'utiliser

- On consomme déjà un modèle [[Dev/Services/HuggingFace|HuggingFace]] : passer par `AutoTokenizer` (qui charge SentencePiece ou le tokeniseur Rust `tokenizers` à sa place) plutôt que d'appeler SentencePiece directement.
- Compter les tokens d'une API propriétaire (OpenAI…) → utiliser **tiktoken**, pas SentencePiece.
- Tokenisation linguistique (lemmes, POS, phrases) plutôt que sous-mots pour un modèle → [[Dev/Services/spaCy|spaCy]], [[Dev/Services/NLTK|NLTK]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add sentencepiece`. Rien à héberger.
- Cœur **C++** (rapide, ~50k phrases/s, empreinte mémoire faible) avec **bindings Python** (SWIG), plus une CLI et une intégration TensorFlow.
- Maintenue par Google ; modèle `.model` autonome, embarquable côté inférence sans la chaîne d'entraînement.

## Pièges

- Le vocabulaire est **figé à l'entraînement** : ré-entraîner sur un corpus représentatif, sinon beaucoup de `<unk>` ou de sur-segmentation.
- BPE vs Unigram : résultats et propriétés différents (Unigram permet la *subword regularization* à l'entraînement, pas BPE).
- Le symbole d'espace `▁` (U+2581) fait partie des tokens : oublier sa gestion casse le décodage.
- Versions du `.model` et de la lib doivent être cohérentes pour garantir le même découpage.

## Alternatives

Pas de fiche concurrente directe dans le brain. Substituts usuels hors brain : `tokenizers` (Rust, HuggingFace) pour un BPE rapide intégré, et `tiktoken` côté OpenAI. Le concept sous-jacent est traité dans [[Tokenization]].

## Liens

- [[Tokenization]] — le concept (BPE, WordPiece, Unigram, byte-level) que SentencePiece implémente.
- [[Dev/Services/HuggingFace|HuggingFace]] — `AutoTokenizer` charge un modèle SentencePiece de façon transparente.
- [[Dev/Services/spaCy|spaCy]] · [[Dev/Services/NLTK|NLTK]] — tokenisation linguistique (autre besoin).
- Doc : https://github.com/google/sentencepiece/blob/master/README.md
