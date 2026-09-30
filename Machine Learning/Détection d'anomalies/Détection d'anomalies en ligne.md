---
role: notion
nom: Détection d'anomalies en ligne
alias: [Online anomaly detection, Streaming anomaly detection, Détection d'anomalies sur flux, Détection d'anomalies en streaming, Half-Space Trees, Random Cut Forest, RRCF]
categorie: ml/anomalie
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection, streaming, timeseries]
---

# Détection d'anomalies en ligne

## Aperçu

- Détecter en ligne, c'est scorer chaque observation **au moment où elle arrive**, sans repasser sur le passé, avec une mémoire bornée, et sans savoir ce que sera la suite. Un détecteur hors ligne (une isolation forest entraînée sur l'historique) répond à une autre question : « parmi ces données, lesquelles sont étranges ? ».
- Trois caractéristiques du problème, d'après Tan, Ting et Liu (IJCAI 2011) : le flux est **infini** (on ne peut pas le stocker pour l'analyser), il contient **surtout du normal** (les anomalies sont rares, souvent absentes de l'entraînement), et il **évolue** (le modèle doit suivre).
- La page traite deux détecteurs de référence pour flux (Half-Space Trees, Random Cut Forest), les seuils qui s'adaptent, l'ambiguïté « le normal a changé, est-ce une anomalie ? », les contraintes de mémoire et de latence, et l'évaluation *prequential*.
- Le cas concret : un capteur de machine échantillonné en continu, un modèle qui doit alerter vite, sans réentraînement par lot, avec des régimes qui changent ([[Détection de ruptures]]).

## Concepts clés

### Ce que le flux impose

Lavin et Ahmad (2015) décrivent le détecteur de flux idéal : détecter chaque anomalie **le plus tôt possible**, ne déclencher aucune fausse alerte, fonctionner sur des données réelles de domaines variés, et **s'adapter automatiquement** aux statistiques changeantes. Les mêmes auteurs ajoutent que le détecteur doit décider en temps réel, apprendre en même temps qu'il prédit, et fonctionner sans réglage humain quand les flux sont nombreux. Cela se traduit en quatre contraintes de conception :

- **un passage** sur les données ; chaque observation est traitée puis jetée ;
- **mémoire bornée**, indépendante de la longueur du flux ;
- **latence bornée** par observation ;
- **adaptation** du modèle de normal, sans réentraînement par lot.

Le modèle est un **état** : dans un moteur de flux, il se sauvegarde et se restaure comme les autres états ([[Stream processing]] : état snapshotté périodiquement, c'est « le vrai coût opérationnel du streaming »).

### Half-Space Trees (Tan, Ting, Liu, IJCAI 2011)

- **Idée.** Un ensemble d'arbres binaires complets de profondeur $h$, dont la **structure est construite sans données** : à chaque nœud, une dimension tirée au hasard, une coupure au milieu de la plage. Les nœuds ne gardent que des **masses** (nombres d'observations) : $r$ pour la fenêtre de référence, $l$ pour la fenêtre courante.
- **Score.** Une observation descend jusqu'à une feuille (ou un nœud contenant au plus `sizeLimit` points) ; son score est $r\times 2^{k}$, avec $k$ la profondeur du nœud, sommé sur les arbres. Une zone de **masse faible ou vide** est interprétée comme anormale : dans l'article, un score **bas** signale l'anomalie.
- **Adaptation par fenêtres.** Le flux est découpé en fenêtres de $\psi$ observations. Pendant qu'une fenêtre se remplit, on score avec la masse de la précédente ; quand elle est pleine, ses masses $l$ **remplacent** celles de référence $r$ et $l$ repart de zéro. La structure ne bouge jamais, donc rien à reconstruire.
- **Coût annoncé.** Temps amorti $O(t(h+1))$ par observation, pire cas $O(t(h+\psi))$ au moment du changement de fenêtre ; mémoire $O(t\,2^h)$ ; constants quand $t$, $h$ et $\psi$ sont fixés. Réglages de l'article : 25 arbres, profondeur 15, fenêtre $\psi=250$, `sizeLimit` $=0{,}1\psi$.
- **Dans River.** `anomaly.HalfSpaceTrees(n_trees=10, height=8, window_size=250, limits=None, seed=None)` : par défaut, les variables sont supposées entre 0 et 1, d'où `MinMaxScaler` ou `limits`. `learn_one(x)` met à jour, `score_one(x)` rend un score où, **à l'inverse de l'article, un score élevé signale l'anomalie** (documentation de River). Les premiers appels à `learn_one` sont coûteux (construction des arbres), les suivants rapides. La documentation présente le modèle comme une « variante en ligne des isolation forests », bon sur des anomalies **dispersées** et en difficulté quand elles **forment un amas**.
- **Taille réelle du modèle** (calcul de cette page) : un arbre de hauteur $h$ a $2^{h+1}-1$ nœuds ; les réglages de l'article donnent donc environ 1,6 million de nœuds ($25\times 65\,535$), les défauts de River environ 5 000 ($10\times 511$).

### Random Cut Forest et RRCF (Guha, Mishra, Roy, Schrijvers, ICML 2016)

- **Arbre.** Dimension de coupure tirée **proportionnellement à la plage** $\ell_i/\sum_j\ell_j$ de chaque dimension (avec $\ell_i=\max_{x\in S}x_i-\min_{x\in S}x_i$), puis valeur de coupure uniforme dans la plage. Les auteurs montrent par un exemple (deux amas de 1 000 points, 30 dimensions dont 29 sans information) qu'une isolation forest, qui traite les dimensions de façon indépendante, rate l'anomalie quand la plupart des coupures tombent sur les dimensions inutiles.
- **Anomalie = déplacement.** Un point est anormal si son **insertion augmente fortement la complexité du modèle**, c'est-à-dire l'externalité qu'il impose au reste des données. Le **déplacement** (*displacement*) d'un point $x$ est l'augmentation de profondeur espérée de tous les autres ; son espérance est le nombre de points du nœud frère de la feuille de $x$ (lemme 1). Pour résister au masquage par doublons, les auteurs définissent le **déplacement collusif** (CoDisp), le maximum sur les sous-ensembles $C\ni x$ d'un déplacement moyen par point de $C$ : les anomalies correspondent aux grandes valeurs.
- **Sur un flux.** L'arbre se maintient sur un **échantillon** : on peut insérer et supprimer un point en conservant la loi de l'arbre, et alimenter l'échantillon par un réservoir uniforme ou biaisé vers le récent. Dans leurs expériences : 100 arbres, échantillon de 256 points par arbre, **shingle** de longueur 4 (une fenêtre glissante de 4 valeurs devient un point à 4 dimensions), chaque point scoré avec la structure construite jusqu'à l'instant précédent.
- **Résultats.** Sur une sinusoïde avec un creux injecté et sur les courses de taxis de New York, les auteurs comparent RRCF à l'isolation forest (jeux visuellement vérifiables) ; ce sont des démonstrations, pas un benchmark. La page n'a pas relu les chiffres.
- **Désaccord sur Half-Space Trees.** Tan et al. annoncent de bons résultats face à une méthode de référence ; Guha et al. écrivent que les travaux antérieurs qui étendent l'isolation au flux, dont Tan et al. (2011), « n'ont pas été jugés efficaces » (en citant Emmott et al. 2013, **non relu ici**). Aucun benchmark commun n'a été lu pour trancher.
- **L'implémentation.** `rrcf` (Bartos, Mullapudi, Troutman, JOSS 2019) est, selon ses auteurs, la **première implémentation open source** de l'algorithme de Guha et al., non une variante « robuste » distincte ; ils indiquent que l'algorithme est employé dans Amazon Kinesis. Le papier reproduit deux cas de l'article de 2016 (amas collusifs ; début d'une anomalie sur une série, avec shingling).

### Seuils adaptatifs

- Un détecteur de flux rend un score ; la décision reste à construire ([[Score et seuil d'alerte]]). En flux, le seuil doit suivre le score, dont la loi bouge avec le normal.
- **Quantile glissant.** `QuantileFilter(q, protect_anomaly_detector)` de River enveloppe un détecteur et classe en anomalie les scores au-dessus du quantile $q$ ; l'option `protect_anomaly_detector` interdit au détecteur d'apprendre sur les instances qu'il juge anormales, afin de ne pas « normaliser » des valeurs aberrantes ponctuelles par exposition répétée. Un quantile décide à l'avance quelle **fraction** sera signalée, pas le taux de fausses alertes futur (voir [[Score et seuil d'alerte]]).
- **Valeurs extrêmes en flux.** SPOT (flux stationnaire) et DSPOT (écart à une moyenne mobile des $d$ dernières observations normales, pour une dérive lente), Siffer et al., KDD 2017, décrits dans [[Score et seuil d'alerte]] et [[Théorie des valeurs extrêmes]].
- **Vraisemblance du score.** Dans NAB, le détecteur HTM de Numenta tient la moyenne et la variance de la distribution récente de ses scores d'anomalie et en sort la **vraisemblance** que le score courant provienne de cette loi normale ; c'est cette vraisemblance qu'on seuille.
- **Carte de contrôle sur le score.** Un CUSUM ou une carte EWMA sur le score détecte un **décalage** du score plutôt qu'un pic isolé ([[Contrôle statistique de procédé (SPC)]]).

### Dérive du « normal »

- Un flux évolue : les trois sources lues (Tan et al., Guha et al., Lavin et Ahmad) en font une exigence. Les mécanismes lus : fenêtres de masse remplacées à chaque période (HS-Trees), réservoir biaisé vers le récent (RCF), et, dans la littérature d'évaluation de flux, **fenêtres glissantes ou facteurs d'oubli** (Gama, Sebastião, Rodrigues, 2013) ; selon ces derniers, les facteurs d'oubli sont plus rapides et sans mémoire que les fenêtres.
- **Tension (raisonnement de cette page).** S'adapter vite fait perdre ce qu'on voulait détecter : une dégradation lente de machine **est** une dérive du normal. Dans HS-Trees, la mise à jour recopie toute la masse de la fenêtre courante, anomalies incluses (algorithme 3 de l'article) ; sans protection, un défaut qui persiste plus d'une fenêtre devient le normal suivant. À l'inverse, un modèle figé signale tout après un changement de régime légitime (nouvelle consigne, changement d'outil).
- **Séparer les deux rôles** plutôt que de les mélanger dans le seuil : un détecteur de dérive ou de rupture surveille le flux ou son score (`drift` de River : `ADWIN` — Bifet et Gavaldà, SDM 2007 —, `PageHinkley`, `KSWIN`), pour dire « le régime a changé » ; le détecteur d'anomalies dit « cette observation sort du régime courant ». Que faire d'un changement (alerter, adapter, réentraîner) est une décision d'exploitation, pas du modèle ([[Data drift]], [[Détection de ruptures]]).
- **Démarrage à froid.** HS-Trees consomme les $\psi$ premières observations pour remplir la référence. NAB réserve les **15 %** premiers de chaque fichier comme période probatoire, où le détecteur apprend sans être jugé.

### Évaluer un détecteur de flux

- **Prequential (test-puis-apprentissage).** Chaque observation est d'abord scorée par le modèle courant, puis apprise. C'est la validation progressive de River : « à chaque étape, le modèle doit soit prédire une observation, soit être mis à jour », et son paramètre `delay` retarde la révélation de la cible, ce qui modélise une étiquette de panne confirmée plus tard (Grzenda et al. 2019, cité par la documentation). Gama et al. (2013) défendent l'erreur prequential **avec mécanismes d'oubli** comme estimateur fiable pour des modèles qui évoluent.
- **Le découpage entraînement/test est inadapté.** Lavin et Ahmad : une séparation artificielle apprentissage/test ne représente pas un scénario de flux ni l'évaluation d'un algorithme qui apprend en continu ; précision et rappel classiques ne reflètent pas la **valeur d'une détection précoce**.
- **NAB** (Numenta Anomaly Benchmark) : une fenêtre d'anomalie centrée sur chaque étiquette, de longueur égale à **10 % de la longueur du fichier divisée par le nombre d'anomalies** ; seule la première détection de la fenêtre compte et vaut d'autant plus qu'elle est précoce (fonction sigmoïde), une détection hors fenêtre est un faux positif pénalisé, une fenêtre sans détection un faux négatif. Trois profils d'application (standard, peu de faux positifs, peu de faux négatifs). Score normalisé entre un détecteur nul (0) et un détecteur parfait (100).
- **Réserve à noter.** Dans l'article de 2015, le seuil de chaque algorithme est réglé par une recherche qui maximise le score NAB sur **tout** le corpus, une seule valeur pour tous les fichiers : c'est un réglage sur les données évaluées, au sens de [[Évaluer une détection d'anomalies]]. Le détecteur aléatoire y obtient 16,8 (profil standard) et non 0, à cause de cette optimisation.
- Les autres pièges (point-adjust, jeux faciles) restent ceux de [[Évaluer une détection d'anomalies]] ; la comparaison entre détecteurs en ligne se fait mieux sur un benchmark qui les contient ([[Jeux de données d'anomalies]]).

## Les maths, simplement

- **Score HS-Trees** : $s(x)=\sum_{T}\mathrm{Node}^*_T.r\times 2^{\mathrm{Node}^*_T.k}$, avec $\mathrm{Node}^*$ le nœud terminal atteint par $x$ dans l'arbre $T$. Sous masse uniforme, $m[i]\,2^i=m[j]\,2^j$ ; sous masse non uniforme, $m[i]\,2^i<m[j]\,2^j$, d'où le classement.
- **Mise à jour par fenêtre** : tous les $\psi$ points, $r\leftarrow l$ pour les nœuds de masse non nulle, puis $l\leftarrow 0$.
- **Coupe RRCF** : dimension $i$ avec probabilité $\ell_i/\sum_j\ell_j$ ; valeur $X_i\sim\mathcal U[\min_{x\in S}x_i,\max_{x\in S}x_i]$.
- **Déplacement collusif** (Guha et al.) : $\mathrm{CoDisp}(x,Z,|S|)=\mathbb E_{S\subseteq Z,T}\Big[\max_{x\in C\subseteq S}\dfrac1{|C|}\sum_{y\in S-C}\big(f(y,S,T)-f(y,S-C,T'')\big)\Big]$, où $f$ est la profondeur dans l'arbre.
- **Shingle de longueur $m$** : $\tilde x_t=(x_{t-m+1},\dots,x_t)$, un point de dimension $m$ ; le détecteur juge alors une **forme** de $m$ valeurs et non une valeur isolée.
- **Fenêtre NAB** : $w=\dfrac{0{,}10\times n}{N_{\text{anomalies}}}$ avec $n$ la longueur du fichier.
- **Quantile en flux** : seuil $\tau_t$ tel que la fraction des scores récents au-dessus de $\tau_t$ vaut $1-q$ ; avec un facteur d'oubli $\alpha$, la fenêtre effective vaut environ $1/(1-\alpha)$ observations (raisonnement de cette page).

## En pratique

- **Partir du plus simple qui tienne le flux.** Une carte EWMA ou CUSUM sur le **résidu** d'un modèle de prévision ([[Contrôle statistique de procédé (SPC)]], [[Forecasting framing]]) coûte quelques opérations par point et s'explique à l'opérateur. Les détecteurs d'ensemble se justifient quand l'anomalie n'est pas un décalage de moyenne, ou quand l'entrée est multivariée. Ce conseil est une position de cette page ; les benchmarks de séries relevés dans [[Évaluer une détection d'anomalies]] vont dans le même sens (méthodes simples souvent compétitives).
- **Mettre les entrées à l'échelle sans fuite** : HS-Trees suppose des variables dans $[0,1]$. Un min-max appris sur tout le flux utilise le futur ; en ligne, utiliser des bornes connues du capteur ou un min-max qui évolue.
- **Fixer la fenêtre sur la durée physique des phénomènes** : $\psi$ ou le réservoir trop courts « oublient » une dégradation, trop longs retardent l'adaptation à un changement de régime légitime. Un shingle $m$ doit couvrir la forme à détecter.
- **Prévoir la latence de pointe**, pas seulement la latence moyenne : HS-Trees paie le changement de fenêtre en une fois (pire cas $O(t(h+\psi))$ de l'article).
- **Protéger l'apprentissage** : ne pas laisser le détecteur apprendre sur ce qui est alerté (`protect_anomaly_detector`), et geler le modèle pendant l'investigation d'une alerte confirmée.
- **Journaliser le score**, pas seulement l'alerte : le score brut permet de retoucher le seuil et de rejouer l'évaluation *prequential* hors ligne, sans l'équipement.
- **Séparer ce qui bouge de ce qui casse** : un score qui monte lentement sur plusieurs jours est du ressort d'un détecteur de dérive ou d'une carte de contrôle sur le score, pas du seuil d'alerte ponctuel.

## Approches voisines & alternatives

- [[River]] — fournit `HalfSpaceTrees`, `QuantileFilter`, `ThresholdFilter`, les détecteurs de dérive et la validation progressive (liste de l'API relue le 2026-10-02).
- [[Stream processing]] — où tourne le détecteur : état, fenêtres, tolérance aux pannes.
- [[Time series anomaly detection]] — le cas général, hors ligne comme en ligne.
- [[Score et seuil d'alerte]] — les seuils, dont SPOT et DSPOT.
- [[Data drift]] — la dérive des entrées d'un modèle en production, côté performance.
- [[Détection de ruptures]] — dater le changement de régime qui invalide le normal appris.
- [[Contrôle statistique de procédé (SPC)]] — les cartes de contrôle, l'ARL et le compromis fausses alertes / délai.
- [[Isolation Forest]] — le pendant hors ligne de Half-Space Trees et de RCF.
- [[Détection d'outliers multivariée]] — les détecteurs statiques, sans dimension temporelle.
- [[Types d'anomalies et régimes de supervision]] — la supervision supposée par un détecteur « normal seulement ».
- [[Évaluer une détection d'anomalies]] et [[Jeux de données d'anomalies]] — les métriques et les terrains d'essai.
- [[Maintenance prédictive et RUL]] — l'usage cible : repérer l'amorce de défaut, puis pronostiquer.

## Pour aller plus loin

- Tan, Ting, Liu (2011), *Fast Anomaly Detection for Streaming Data*, IJCAI 2011 : https://www.ijcai.org/Proceedings/11/Papers/254.pdf
- Guha, Mishra, Roy, Schrijvers (2016), *Robust Random Cut Forest Based Anomaly Detection On Streams*, ICML 2016, PMLR 48 : https://proceedings.mlr.press/v48/guha16.html
- Bartos, Mullapudi, Troutman (2019), *rrcf: Implementation of the Robust Random Cut Forest algorithm for anomaly detection on streams*, JOSS 4(35), 1336 : https://joss.theoj.org/papers/10.21105/joss.01336
- Lavin, Ahmad (2015), *Evaluating Real-time Anomaly Detection Algorithms — the Numenta Anomaly Benchmark*. arXiv : https://arxiv.org/abs/1510.03336
- Gama, Sebastião, Rodrigues (2013), *On evaluating stream learning algorithms*, Machine Learning 90(3), 317-346 : https://link.springer.com/article/10.1007/s10994-012-5320-9 (résumé lu).
- Documentation de River : https://riverml.xyz/latest/api/anomaly/HalfSpaceTrees/ ; https://riverml.xyz/latest/api/anomaly/QuantileFilter/ ; https://riverml.xyz/latest/api/evaluate/progressive-val-score/ ; https://riverml.xyz/latest/api/drift/ADWIN/
- Siffer, Fouque, Termier, Largouët (2017), *Anomaly Detection in Streams with Extreme Value Theory*, KDD 2017 — voir [[Score et seuil d'alerte]].
