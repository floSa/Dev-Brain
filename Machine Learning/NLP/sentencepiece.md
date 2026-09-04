---
role: brique
nom: sentencepiece
alias: [sentence-piece, spm, google sentencepiece]
pitch: "Tokeniseur sous-mot de Google, indépendant de la langue — BPE et modèle Unigram entraînés directement sur du texte brut (Unicode/octets, sans pré-tokenisation), implémentation C++ et bindings Python."
categorie: ml/nlp
famille: paquet
licence_type: open-source
maturite: production
langage: C++/Python
alternatives: []
complements: []
tags: [tokenization, nlp]
url_docs: https://github.com/google/sentencepiece/blob/master/README.md
url_repo: https://github.com/google/sentencepiece
---

# sentencepiece

<!-- AUTO:BANDEAU:START -->
> Tokeniseur sous-mot de Google, indépendant de la langue — BPE et modèle Unigram entraînés directement sur du texte brut (Unicode/octets, sans pré-tokenisation), implémentation C++ et bindings Python.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++/Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Tokeniseur **sous-mot** de Google, conçu pour être indépendant de la langue. Là où la plupart
des tokeniseurs supposent une pré-segmentation par espaces, SentencePiece traite la phrase
comme une **suite de caractères Unicode bruts** — l'espace devient le symbole `▁` (U+2581),
lui-même un token à part entière —, ce qui le rend réversible et applicable au japonais, au
chinois ou au thaï. Il implémente deux algorithmes d'apprentissage de vocabulaire : **BPE** et
le **modèle Unigram**, sa contribution propre, seul à offrir la *subword regularization*. Le
vocabulaire est **figé à l'entraînement** : le modèle produit (`.model` + `.vocab`) sert
ensuite à encoder et décoder, et c'est le tokeniseur derrière T5, ALBERT, XLNet, Llama ou
Mistral.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Entraîner un vocabulaire sous-mot sur un corpus propre — langue, domaine, code — sans dépendre d'une pré-tokenisation | Le vocabulaire est **figé à l'entraînement** : un corpus non représentatif donne beaucoup de `<unk>` ou de la sur-segmentation, et il faut ré-entraîner |
| Modèles multilingues, ou langues sans séparateur de mots : japonais, chinois, thaï | Un modèle [[HuggingFace]] déjà consommé via `AutoTokenizer` charge SentencePiece de façon transparente — l'appeler en direct duplique la chaîne |
| Reproduire le tokeniseur d'un modèle qui le spécifie (T5, Llama) en chargeant son `.model` | Compter les tokens d'une API propriétaire (OpenAI) : ce n'est pas le même vocabulaire → tiktoken, hors brain |
| Besoin d'un encodage **réversible** et déterministe texte ↔ ids |  |
| | Le symbole d'espace `▁` fait partie des tokens : l'oublier casse le décodage |
| | Versions du `.model` et de la bibliothèque à tenir cohérentes, sous peine de découpage différent |

## Mise en œuvre

- Installation — `uv add sentencepiece`
- Point d'entrée — bindings Python (SWIG), CLI d'entraînement, ou bibliothèque C++ ; intégration TensorFlow disponible
- Prérequis — un corpus d'entraînement représentatif ; le `.model` produit est autonome et embarquable côté inférence, sans la chaîne d'entraînement
- Exécution — cœur C++ rapide, de l'ordre de 50 k phrases/s, empreinte mémoire faible ; single-node
- Coût — gratuit, Apache-2.0, rien à héberger ; maintenu par Google

## Écosystème

### Alternatives

- `tokenizers` — le BPE rapide en Rust de HuggingFace, intégré à la chaîne `transformers` (pas encore en fiche).
- `tiktoken` — le tokeniseur des modèles OpenAI, pour compter les tokens d'une API propriétaire (pas encore en fiche).

## Ressources

- Documentation — https://github.com/google/sentencepiece/blob/master/README.md
- Dépôt — https://github.com/google/sentencepiece

## Voir aussi

- [[Tokenization]] — la notion : BPE, WordPiece, Unigram, byte-level, que SentencePiece implémente
- [[HuggingFace]] — son `AutoTokenizer` charge un modèle SentencePiece de façon transparente
- [[Traitement du langage naturel]] — la notion chapeau du dossier
- [[Comparatif - NLP]] — ce qui départage les outils du dossier
