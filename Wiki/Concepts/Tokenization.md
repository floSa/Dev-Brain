---
galaxie: wiki
type: concept
nom: Tokenization
alias: [tokenisation, découpage en tokens, BPE, byte-pair encoding, subword tokenization]
categorie: concept/llm
domaines: [ai-eng]
tags: [tokenization, llm, nlp]
---

# Tokenization

## Aperçu

- Étape qui **convertit le texte en tokens** (unités sous-mots) que le modèle lit et génère ; chaque token est un entier indexant un **vocabulaire** fixe.
- C'est la frontière entre langage et nombres : le nombre de tokens fixe le **coût**, la **latence** et l'occupation de la **fenêtre de contexte**.

## Concepts clés

### Pourquoi des sous-mots
- Vocabulaire par mots → explosion de taille et mots inconnus (OOV) ; par caractères → séquences très longues. Le **sous-mot** est le compromis : mots fréquents en un token, mots rares découpés en morceaux.

### Algorithmes
- **BPE** (Byte-Pair Encoding) : fusionne itérativement la paire de tokens la plus fréquente jusqu'à atteindre la taille de vocabulaire visée. **WordPiece** (BERT) et **Unigram / SentencePiece** sont des variantes. Les tokenizers modernes opèrent souvent sur des **octets** (byte-level) → aucun OOV possible.

### Tokens spéciaux
- Marqueurs hors-texte : début/fin de séquence, séparateurs de rôle (system/user/assistant), padding. Le *chat template* les insère pour structurer la conversation.

### Effets concrets
- Découpage **inégal** : l'anglais coûte moins de tokens que le français, le code ou le CJK ; un même contenu n'a pas le même prix selon la langue.
- **Chiffres et espaces** mal segmentés expliquent une partie des erreurs d'arithmétique et de comptage de caractères des LLM.

## Les maths, simplement

- Un texte devient une suite $(t_1, \dots, t_N)$ de tokens, $t_i \in \mathcal{V}$ avec $|\mathcal{V}|$ la taille du vocabulaire (souvent 30 k–250 k).
- BPE part des caractères/octets et applique $M$ fusions apprises ; plus $M$ est grand, plus les séquences sont courtes mais plus le vocabulaire est lourd — arbitrage longueur de séquence ↔ taille de vocabulaire.

## En pratique

- **Compter les tokens avant d'estimer un coût** : utiliser le tokenizer du modèle (ex. `tiktoken` côté OpenAI, `tokenizers` HuggingFace) plutôt que le nombre de mots.
- Prévoir que les langues non anglaises et le code **gonflent** le compte de tokens (donc le budget de [[Context engineering|contexte]] et la facture).
- Pour le parsing strict d'une sortie, se méfier des frontières de tokens : préférer des [[Structured outputs|sorties structurées]] à un découpage manuel.
- Garder le **même tokenizer** quand on compare deux modèles sur la [[Perplexity|perplexité]] — sinon les chiffres ne sont pas comparables.

## Approches voisines & alternatives

- [[embeddings]] — une fois découpé en tokens, chaque token est projeté en vecteur dense ; tokenization et embeddings sont les deux premières couches.
- [[Decoding strategies]] — la génération produit des tokens un à un, dans ce même vocabulaire.
- [[Perplexity]] — se calcule **par token**, donc dépend directement du tokenizer.
- [[Context engineering]] — la fenêtre de contexte se mesure en tokens, pas en mots.

## Pour aller plus loin

- Sennrich et al. (2016) — *Neural Machine Translation of Rare Words with Subword Units* (BPE).
- Kudo (2018) — *Subword Regularization* / SentencePiece (modèle Unigram).
- Outils : [[Dev/Services/sentencepiece|sentencepiece]] (BPE / Unigram, indépendant de la langue), `tiktoken`, `tokenizers` (HuggingFace).
