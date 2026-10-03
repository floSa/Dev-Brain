---
role: notion
nom: LSTM et réseaux récurrents
alias: [LSTM, Long Short-Term Memory, RNN, réseaux récurrents, réseau de neurones récurrent, recurrent neural network, GRU, Gated Recurrent Unit, BiLSTM, LSTM bidirectionnel, BPTT, rétropropagation à travers le temps, xLSTM, cellule LSTM, forget gate]
categorie: ml/apprentissage-profond
domaines: [ml-eng, data-sci]
tags: [lstm, deep-learning, timeseries]
---

# LSTM et réseaux récurrents

## Aperçu

- Un **réseau récurrent** (RNN) lit une séquence **pas à pas** et résume ce qu'il a vu dans un **état caché** réinjecté au pas suivant. Un même jeu de poids sert à chaque pas : la longueur de la séquence n'est pas figée par l'architecture.
- Le RNN simple apprend mal les dépendances longues : le gradient s'évanouit ou explose le long du temps. Le **LSTM** (Hochreiter et Schmidhuber, 1997) et le **GRU** (Cho et al., 2014) y répondent par des **portes** qui décident ce que l'état garde, écrit ou lit.
- Dans ce vault, c'est la brique de séquence derrière deux familles de pages : la durée de vie résiduelle ([[RUL par apprentissage profond]]) et les anomalies multivariées ([[Anomalies multivariées par apprentissage profond]]). Face aux Transformers et aux modèles à espace d'états, c'est le choix sobre : léger, lisible en flux, sans grosse infrastructure.
- **Rangement.** Arbre D1→D14 : l'objet n'appelle aucun grand modèle de langage (D1 non) ; il entraîne un modèle d'apprentissage (D2 oui) → `ml/*`. Dans `ml/*`, c'est un **réseau comme objet**, pas un régime d'apprentissage ni une tâche : `ml/apprentissage-profond`, aux côtés de [[State Space Models]] et de [[Self-attention]]. `ml/series-temporelles` est écarté : le LSTM n'est pas propre aux séries (parole, texte), et ce dossier range ce qui traite une série, pas l'architecture.

## Concepts clés

### Le RNN simple et la rétropropagation à travers le temps

- À chaque pas, l'état est $h_t = \tanh(W_x x_t + W_h h_{t-1} + b)$ et la sortie en découle. L'entraînement **déplie** le réseau sur la longueur de la séquence et applique la rétropropagation ([[Rétropropagation et différentiation automatique]]) : c'est la **BPTT**.
- Le coût en temps est **séquentiel** : $h_t$ attend $h_{t-1}$. Pas de parallélisme sur l'axe du temps à l'entraînement, contrairement à une convolution ou à l'attention.

### Le gradient qui s'évanouit (ou explose)

- Bengio, Simard et Frasconi (*IEEE Trans. Neural Networks* 5(2), 1994) montrent que lorsque la norme du jacobien de la récurrence est inférieure à 1, le gradient décroît **exponentiellement** vers le passé ; au-dessus de 1, il peut remonter mais le système devient localement instable et ne retient pas l'information longtemps. Apprendre une dépendance qui enjambe $k$ pas devient exponentiellement difficile avec $k$.
- Pascanu, Mikolov et Bengio (arXiv 1211.5063) analysent les deux pathologies et proposent le **rognage de la norme du gradient** (*gradient norm clipping*) contre l'explosion, et une contrainte souple contre l'évanouissement. Le rognage reste d'usage courant ; il traite l'explosion, pas l'évanouissement.

### La cellule LSTM

- Idée centrale (Hochreiter et Schmidhuber, *Neural Computation* 9(8), 1997) : une **cellule mémoire** $c_t$ traversée par un flux d'erreur **constant** (*constant error carousel*), dont l'accès est ouvert et fermé par des **portes multiplicatives** apprises. Le résumé de l'article annonce des retards de plus de 1 000 pas franchis, sur des tâches construites pour cela.
- Quatre blocs par pas, lus dans la documentation de PyTorch : porte d'**entrée** $i_t$ (quoi écrire), porte d'**oubli** $f_t$ (quoi garder de $c_{t-1}$), candidat $g_t$ (la valeur à écrire), porte de **sortie** $o_t$ (quoi exposer dans $h_t$).
- **La porte d'oubli n'est pas dans l'article de 1997.** Gers, Schmidhuber et Cummins (*Neural Computation* 12(10), 2000) l'ajoutent : sans remise à zéro, l'état d'une cellule peut croître sans borne sur un flux continu non segmenté. Le LSTM des bibliothèques est cette variante.
- Le gradient emprunte le **chemin de la cellule**, additif, au lieu de repasser par une non-linéarité à chaque pas : c'est ce qui limite l'évanouissement, sans le supprimer (voir les maths).

### Le GRU

- Cho et al. (2014, arXiv 1406.1078) introduisent, dans un encodeur-décodeur récurrent pour la traduction automatique, une unité cachée à deux portes : une porte de **réinitialisation** (quelle part de l'état précédent entre dans le candidat) et une porte de **mise à jour** (quelle fraction de l'état est remplacée par le candidat). Pas de cellule séparée de l'état caché.
- Chung, Gulcehre, Cho et Bengio (arXiv 1412.3555, atelier NIPS 2014) comparent LSTM, GRU et unités $\tanh$ sur la modélisation de musique polyphonique et de signal de parole : les unités à portes battent les $\tanh$, et le GRU est **comparable** au LSTM. Deux tâches, une date : la conclusion ne vaut pas pour une série industrielle sans test.
- Moins de paramètres (trois blocs au lieu de quatre) et un état de moins à propager.

### Variantes d'usage

- **Empilé** : plusieurs couches, la sortie de l'une est l'entrée de la suivante (`num_layers`).
- **Bidirectionnel** : une passe avant et une passe arrière, sorties concaténées. Exige de connaître **toute** la séquence : inutilisable tel quel en flux en ligne, pertinent pour étiqueter un segment déjà enregistré.
- **Encodeur-décodeur** (*seq2seq*) : l'encodeur résume la séquence, le décodeur la reconstruit ou en produit une autre. C'est la forme du **LSTM-AE** de détection d'anomalies, cité dans [[Anomalies multivariées par apprentissage profond]].
- **Projection de sortie** (`proj_size` dans PyTorch) : réduire la taille de $h_t$ sans toucher à la cellule.

### Face aux Transformers et aux modèles à espace d'états

- **Transformer** ([[Transformer architectures]], [[Self-attention]]) : chaque pas regarde tous les autres, entraînement parallèle sur le temps, coût quadratique en longueur. Le LSTM compresse tout le passé dans un état de taille fixe : mémoire constante et inférence en $O(1)$ par pas, au prix d'un rappel exact plus faible sur les séquences très longues.
- **Modèle à espace d'états** ([[State Space Models]]) : même profil de coût que le LSTM à l'inférence, mais une récurrence **linéaire** qui se parallélise à l'entraînement. C'est la lignée qui reprend l'avantage du RNN sans son goulot séquentiel.
- **xLSTM** (Beck, Pöppel, Spanring et al., arXiv 2405.04517, mai 2024, révisé en décembre 2024, dont Hochreiter) : portes exponentielles normalisées, variante à mémoire scalaire (sLSTM) et variante à mémoire matricielle entièrement parallélisable (mLSTM). Les auteurs annoncent des performances compétitives avec Transformers et modèles à espace d'états en modélisation du langage à l'échelle du milliard de paramètres. **Résultat des auteurs, non reproduit ici.**
- **Pour une série de capteurs**, la comparaison utile n'est pas celle du langage. Zeng, Chen, Zhang et Xu (arXiv 2205.13504, « Are Transformers Effective for Time Series Forecasting? ») trouvent qu'un modèle **linéaire à une couche** bat les Transformers de prévision à long horizon sur neuf jeux. Ce n'est pas un résultat sur le LSTM, mais il invite à partir d'un plancher simple avant tout réseau de séquence.

## Les maths, simplement

- **Cellule LSTM** (convention de PyTorch, $\sigma$ sigmoïde, $\odot$ produit terme à terme) :

$$i_t=\sigma(W_{i}[x_t,h_{t-1}]+b_i),\quad f_t=\sigma(W_{f}[x_t,h_{t-1}]+b_f),\quad g_t=\tanh(W_{g}[x_t,h_{t-1}]+b_g),\quad o_t=\sigma(W_{o}[x_t,h_{t-1}]+b_o)$$

$$c_t = f_t\odot c_{t-1} + i_t\odot g_t,\qquad h_t = o_t\odot\tanh(c_t).$$

- **Pourquoi le gradient survit mieux.** Le long de la seule cellule, $\partial c_t/\partial c_{t-1}=\operatorname{diag}(f_t)$ : un produit de facteurs compris entre 0 et 1 **choisis par le réseau**, et non une suite de jacobiens d'une récurrence $\tanh$. Une porte d'oubli proche de 1 laisse l'erreur traverser de nombreux pas. Ce n'est qu'une partie du jacobien (les portes dépendent aussi de $h_{t-1}$) ; la forme additive est ce qui compte. Une porte d'oubli proche de 0 coupe la mémoire, ce qui est parfois voulu.
- **Paramètres d'une couche** : avec $d$ entrées, $h$ unités cachées et les deux vecteurs de biais de PyTorch, $4h(d+h+2)$ ; un GRU de même forme en compte trois quarts, soit $3h(d+h+2)$.
- **GRU** (forme de Cho et al., $z_t$ mise à jour, $r_t$ réinitialisation) :

$$z_t=\sigma(W_z[x_t,h_{t-1}]),\quad r_t=\sigma(W_r[x_t,h_{t-1}]),\quad \tilde h_t=\tanh\big(W[x_t,\,r_t\odot h_{t-1}]\big),\quad h_t=(1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t.$$

  La convention du rôle de $z_t$ (garder l'ancien ou prendre le nouveau) varie selon les bibliothèques : relire la documentation avant de convertir des poids d'un cadre à l'autre.

## En pratique

- **Fenêtrer, puis découper par unité.** Une série se transforme en fenêtres glissantes de longueur $T_w$ ; deux fenêtres voisines d'une même machine sont quasi identiques, donc les répartir des deux côtés du découpage fait fuir de l'information ([[Data leakage]], [[Walk-forward CV]]). La longueur de fenêtre est un hyperparamètre, pas un détail.
- **Normaliser sur l'entraînement seul**, capteur par capteur, régime par régime si la machine en a. Un réseau y est sensible, à la différence d'un arbre de décision, que ne gêne aucune transformation monotone des entrées.
- **Rogner le gradient** (`clip_grad_norm_` dans PyTorch) : peu coûteux, évite les pas aberrants.
- **Séquences de longueurs différentes** : empaqueter ou remplir et masquer, jamais laisser le remplissage compter dans la perte. Sur une fenêtre de longueur fixe, le problème disparaît.
- **État entre fenêtres** : par défaut, l'état est remis à zéro à chaque lot. Le conserver d'un lot au suivant (*stateful*) n'a de sens que si les lots se suivent dans le temps, sans mélange.
- **GPU et reproductibilité** : la documentation de PyTorch indique que le chemin cuDNN n'est pas déterministe par défaut, avec des variables d'environnement à fixer selon la version de CUDA (`CUBLAS_WORKSPACE_CONFIG=:16:8` à partir de CUDA 10.2). Utile quand deux graines doivent donner le même modèle.
- **Mesurer contre un plancher.** Sur les anomalies multivariées, le recueil TSB-AD cité dans [[Anomalies multivariées par apprentissage profond]] met un CNN et un LSTM prédictifs au niveau d'une ACP, devant les architectures à attention : ne pas garder un transformeur qu'un LSTM égale. Sur la RUL, l'écart dû à l'architecture est petit devant celui du protocole (plafond, fenêtre, normalisation), voir [[RUL par apprentissage profond]].
- **Incertitude** : un LSTM rend une valeur, pas un intervalle. Ensembles, MC dropout ou enveloppe conforme ([[Prédiction conforme]]) ; sur une série, l'échangeabilité de la conforme classique ne tient pas.

### Usages vus dans le chantier

- **RUL.** Heimes (PHM 2008) résout le défi PHM08 par un réseau récurrent ; Zheng, Ristovski, Farahat et Gupta (ICPHM 2017) reprochent aux approches à fenêtre aplatie d'ignorer l'ordre de la séquence. Détail et réserves dans [[RUL par apprentissage profond]].
- **Anomalies.** LSTM-AE (Malhotra et al., 2016) : encodeur-décodeur entraîné sur du normal, l'erreur de reconstruction sert de score. Voir [[Anomalies multivariées par apprentissage profond]] et [[Score et seuil d'alerte]].
- **Adaptation entre machines.** da Costa, Akcay, Zhang et Kaymak (arXiv 1907.07480, *Reliability Engineering & System Safety*) combinent un LSTM et un réseau adversarial de domaine pour prédire la RUL quand les conditions d'exploitation diffèrent entre source et cible, sur C-MAPSS. Voir [[Adaptation de domaine]].

## Approches voisines & alternatives

- [[Apprentissage profond]] — le cadre général : rétropropagation, optimisation, régularisation.
- [[Perceptron et MLP]] — sur une fenêtre aplatie, un MLP ignore l'ordre ; c'est le plancher de la famille.
- [[CNN]] — la convolution 1D lit aussi une fenêtre, en parallèle sur le temps ; dans les benchmarks de RUL, c'est le concurrent direct.
- [[State Space Models]] — récurrence linéaire, parallélisable à l'entraînement, même profil de coût à l'inférence.
- [[Self-attention]] et [[Transformer architectures]] — le rappel exact sur longue séquence, au prix du coût quadratique.
- [[Attention linéaire]] — l'autre lignée « récurrente en inférence, parallèle à l'entraînement ».
- [[Autoencodeurs]] — le LSTM-AE en est la version pour séquences.
- [[Time series feature engineering]] — la voie sans réseau : caractéristiques extraites à la main, puis un modèle classique.
- [[Chronos]] et [[Foundation models pour séries temporelles]] — l'alternative pré-entraînée, sans entraînement propre.
- [[PyTorch]] et [[Keras]] — les deux bibliothèques où le LSTM se pose en une ligne.

## Pour aller plus loin

- Hochreiter, Schmidhuber (1997), *Long Short-Term Memory*, Neural Computation 9(8) : 1735-1780. DOI 10.1162/neco.1997.9.8.1735. Résumé lu ; le texte intégral n'a pas été relu pour cette page.
- Gers, Schmidhuber, Cummins (2000), *Learning to Forget: Continual Prediction with LSTM*, Neural Computation 12(10) : 2451-2471. Seules les métadonnées et le résumé ont été vus.
- Bengio, Simard, Frasconi (1994), *Learning long-term dependencies with gradient descent is difficult*, IEEE Transactions on Neural Networks 5(2) : 157-166. DOI 10.1109/72.279181. Résumé vu.
- Pascanu, Mikolov, Bengio (2012), *On the difficulty of training Recurrent Neural Networks* : <https://arxiv.org/abs/1211.5063>
- Cho et al. (2014), *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation* : <https://arxiv.org/abs/1406.1078>
- Chung, Gulcehre, Cho, Bengio (2014), *Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling* : <https://arxiv.org/abs/1412.3555>
- Lipton, Berkowitz, Elkan (2015), *A Critical Review of Recurrent Neural Networks for Sequence Learning* : <https://arxiv.org/abs/1506.00019>
- Beck et al. (2024), *xLSTM: Extended Long Short-Term Memory* : <https://arxiv.org/abs/2405.04517>
- Zeng, Chen, Zhang, Xu (2022), *Are Transformers Effective for Time Series Forecasting?* : <https://arxiv.org/abs/2205.13504>
- da Costa, Akcay, Zhang, Kaymak (2019), *Remaining Useful Lifetime Prediction via Deep Domain Adaptation* : <https://arxiv.org/abs/1907.07480>
- Documentation de `torch.nn.LSTM` : <https://docs.pytorch.org/docs/stable/generated/torch.nn.LSTM.html>
- Connexions brain : [[RUL par apprentissage profond]], [[Anomalies multivariées par apprentissage profond]], [[Maintenance prédictive et RUL]], [[Time series anomaly detection]].
