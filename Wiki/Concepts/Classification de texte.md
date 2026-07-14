---
galaxie: wiki
type: concept
nom: Classification de texte
alias: [text classification, classification de documents, catégorisation de texte, analyse de sentiment]
categorie: concept/nlp
domaines: [data-sci, ml-eng]
tags: [nlp, text-classification, classification, supervised, class-imbalance]
---

# Classification de texte

## Aperçu

- Assigner une ou plusieurs **catégories** à un document : sentiment, thème, intention, spam, langue. La tâche NLP supervisée la plus courante.
- Trois niveaux de sophistication selon les données et le budget : baseline lexical → embeddings → LLM.

## Concepts clés

### Trois paliers
- **Baseline** : [[TF-IDF]] + classifieur linéaire ([[Régression logistique]], SVM). Rapide, robuste, interprétable.
- **Embeddings** : encoder le texte ([[embeddings]] de phrases), puis classifier ; ou fine-tuner un encodeur transformeur (BERT). Capte le sens.
- **LLM** : zero / few-shot par prompt, ou fine-tuning léger ([[Dev/Services/SetFit|SetFit]] pour le few-shot frugal). Souple, fort en faibles données.

### Mono- vs multi-label
- Une classe exclusive (softmax) vs plusieurs simultanées (sigmoïdes indépendantes + seuil).

### Déséquilibre des classes
- Fréquent (spam, fraude, défaut) : rééchantillonnage (SMOTE), pondération de la perte → [[Imbalanced classification]].

### Évaluation
- Pas l'accuracy seule en cas de déséquilibre : précision / rappel / F1 par classe, macro vs micro → [[Classification metrics]].

## Les maths, simplement

- Perte standard : **entropie croisée** ([[Cross-entropy]]), $-\sum_c y_c \log \hat p_c$ entre la classe vraie et la distribution prédite $\hat p$.
- Baseline complet : pipeline $\text{texte} \xrightarrow{\text{TF-IDF}} \mathbf{x} \xrightarrow{\text{logistique}} \hat p$.

## En pratique

- Commencer par le baseline TF-IDF + [[Régression logistique|régression logistique]] : souvent 90 % du résultat pour 10 % de l'effort, et un étalon pour juger les approches lourdes.
- Monter en gamme seulement si le baseline plafonne : embeddings / BERT, puis LLM.
- Soigner la **stratification** du split et éviter le [[Data leakage]] (fit du vectorizer sur le train seul).
- Few-shot frugal : [[Dev/Services/SetFit|SetFit]] (fine-tuning contrastif de [[Dev/Services/sentence-transformers|sentence-transformers]]) bat souvent le prompt LLM à coût bien moindre.

## Approches voisines & alternatives

- [[TF-IDF]] — le baseline de features.
- [[embeddings]] — représentations denses pour la voie neuronale.
- [[NER et étiquetage de séquence]] — la sœur : étiqueter les tokens plutôt que le document entier.
- [[Classification metrics]] — comment l'évaluer correctement.
- [[Imbalanced classification]] — quand les classes sont déséquilibrées.
- [[Régression logistique]] / [[Random Forest]] — classifieurs du baseline.
- [[SFT|Fine-tuning]] — adapter un LLM ou un encodeur à la tâche.
- [[Traitement du langage naturel]] — page chapeau du sous-domaine.

## Pour aller plus loin

- Joulin et al. (2016) — *Bag of Tricks for Efficient Text Classification* (fastText, baseline linéaire fort).
- Tunstall et al. (2022) — *Efficient Few-Shot Learning Without Prompts* (SetFit).
