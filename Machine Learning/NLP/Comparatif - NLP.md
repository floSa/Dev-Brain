---
role: comparatif
nom: Comparatif - NLP
categorie: ml/nlp
tags: [nlp, information-retrieval, ner, sequence-labeling, text-classification]
---

# Comparatif - NLP

> On tranche sur : l'étage de la chaîne texte qu'on outille — découper, étiqueter, classer, encoder, retrouver, évaluer — et, à cet étage, ce que l'outil fait que ses voisins ne font pas.

![[Comparatif - NLP.base]]

## Ce qui départage

- [[sentencepiece]] — traite la phrase comme une suite de caractères Unicode bruts, **sans pré-segmentation par espaces** : le seul applicable tel quel au japonais ou au chinois, et le seul à proposer le modèle Unigram avec sa *subword regularization*.
- [[spaCy]] — le pipeline linguistique complet et rapide (tokenisation, POS, dépendances, lemmes, NER) en un appel, sur 70+ langues et efficace en CPU ; son NER est borné aux **types appris** par le modèle.
- [[NLTK]] — l'ADN est didactique : ce sont les corpus et lexiques téléchargeables (WordNet, treebanks, FrameNet) et les algorithmes montrés explicitement, pas le débit. API objet par objet, très centrée anglais.
- [[GLiNER]] — la NER **zero-shot** : les types d'entités se décrivent en langage naturel, sans données annotées ni réentraînement, dans un encodeur compact. La qualité dépend de la formulation des libellés, et ne bat pas un modèle entraîné quand les données existent.
- [[pytorch-crf]] — juste une **couche de sortie** : la log-vraisemblance de séquence et le décodage Viterbi, pour que les labels voisins soient cohérents. Dernière release en 2019, et un gros transformeur fine-tuné rend souvent le CRF optionnel.
- [[SetFit]] — fine-tuning **contrastif** puis tête de classification : compétitif à quelques dizaines d'exemples par classe, sans prompt ni LLM, pour un modèle petit à servir. Au-delà d'un certain volume, le fine-tuning classique reprend l'avantage.
- [[sentence-transformers]] — l'étage **dense** : bi-encoders pour indexer, cross-encoders pour reranker. Les deux ne se substituent pas — un cross-encoder ne se pré-calcule pas, il ne sert que sur le top-k.
- [[RAGatouille]] — la **late-interaction** ColBERT rendue utilisable : index PLAID persisté et fine-tuning avec minage de négatifs. C'est le multi-vecteur qui généralise hors domaine, au prix d'un index volumineux ; plus aucun commit depuis mai 2025.
- [[bm25s]] — BM25 dont les scores sont **pré-calculés à l'indexation** dans des matrices creuses : la requête devient une multiplication creuse, des ordres de grandeur plus rapide. La contrepartie est qu'ajouter un document veut dire réindexer.
- [[rank-bm25]] — le même BM25 en Python pur, sans index ni dépendance : l'API la plus minimale pour un prototype. Tout en mémoire, dernière release en 2022.
- [[HuggingFace]] — pas un framework de calcul mais la **couche au-dessus** : le Hub et `transformers`/`datasets`/`PEFT`. Ce qui s'y décide n'est pas technique mais juridique — les licences des modèles sont hétérogènes, « open weights » n'est pas usage commercial libre.
- [[datasets]] — le backend **Arrow memory-mappé** : lectures *zero-copy* et mode `streaming` pour itérer sur plus grand que la RAM. Ce n'est pas un moteur de requête — pas de jointures ni de group-by.
- [[evaluate]] — les métriques **versionnées sur le Hub**, donc des scores comparables à la littérature plutôt que réimplémentés. Maintenance ralentie depuis 0.4.6, et HuggingFace pointe désormais LightEval pour les LLM.
- [[seqeval]] — score au niveau **entité** et non au niveau token, span exact et type compris : c'est la seule métrique qui reflète la qualité réelle d'un tagger, là où `sklearn` surévalue. Dernière release en octobre 2020.
- [[interpreto]] — le seul du lot à expliquer un modèle de langage déjà entraîné, attributions **et** concepts, avec le scoring des explications ; limité à HuggingFace et déclaré alpha en 0.5.0.
- [[DSPy]] — renverse le sujet : on déclare des signatures typées et un **optimiseur compile les prompts** contre une métrique. Sans jeu d'exemples ni métrique, il perd son intérêt, et la phase d'optimisation consomme beaucoup de tokens.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
