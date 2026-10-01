---
role: notion
nom: Diagnostic de défauts de roulements
alias: [Diagnostic de roulements, Défauts de roulements, Bearing fault diagnosis, Spectre d'enveloppe, Kurtogramme]
categorie: ml/maintenance
domaines: [data-sci, mlops]
tags: [predictive-maintenance, condition-monitoring, vibration-analysis, data-leakage, benchmark]
---

# Diagnostic de défauts de roulements

## Aperçu

- **Diagnostiquer** un roulement, c'est dire si un défaut est présent, **où** (bague interne, bague externe, élément roulant, cage) et à quel stade. Le pronostic (le temps qui reste) vient après : [[Maintenance prédictive et RUL]].
- La méthode de référence est physique : **chaque défaut rejoue un choc à une cadence fixée par la géométrie et la vitesse**. On démodule le signal d'accélération autour d'une résonance, puis on cherche cette cadence dans le spectre de l'enveloppe. Les outils de signal sont dans [[Analyse vibratoire]].
- L'apprentissage automatique y ajoute surtout des problèmes d'**évaluation** : le jeu public le plus utilisé (CWRU) se prête mal aux protocoles courants, et les scores très élevés qu'on lit souvent ne disent rien tant que le découpage train/test n'est pas décrit.

## Concepts clés

### Fréquences caractéristiques

- Elles se calculent à partir de la géométrie : $n$ éléments roulants, diamètre d'élément $d$, diamètre primitif $D$, angle de contact $\varphi$, fréquence de rotation de l'arbre $f_r$. Bague externe fixe, bague interne solidaire de l'arbre.
- **BPFO** : passage des éléments sur un défaut de bague externe. **BPFI** : idem, bague interne. **BSF** : rotation d'un élément sur lui-même. **FTF** : rotation de la cage.
- Ce sont des fréquences cinématiques, sans glissement. En réalité les éléments glissent un peu au hasard : le signal d'un roulement est **stochastique** et non strictement périodique (diapositives de Randall), donc les pics sont étalés. D'où les **bandes** autour de chaque fréquence plutôt qu'une raie unique (la fonction `bearingFaultBands` de MathWorks renvoie des bandes $F \pm W/2$). L'ampleur du glissement n'est pas chiffrée ici (non vérifiée).
- Un élément roulant défectueux frappe les deux bagues à chaque tour sur lui-même : la table du jeu CWRU donne pour la bille 4,7135 fois $f_r$, soit $2\times\mathrm{BSF}$ (vérifié par le calcul ci-dessous).

### Spectre d'enveloppe

- Chaîne type (exemple MathWorks sur le jeu MFPT) : bande choisie par kurtogramme, filtre passe-bande, enveloppe par transformée de Hilbert, passe-bas, FFT. Le spectre de l'enveloppe montre les fréquences caractéristiques et leurs harmoniques.
- Le détail de chaque brique est dans [[Analyse vibratoire]] ; la conception du filtre dans [[Filtrage numérique]].

### Choisir la bande : le kurtogramme

- Le **kurtosis spectral** (Antoni, 2006) mesure l'impulsivité par bande de fréquence. Le **kurtogramme rapide** (Antoni, 2007) le parcourt sur un banc de filtres « 1/3-binaire » et rend la fréquence centrale, la largeur de bande et la fenêtre optimales (documentation MathWorks).
- Limite : la bande la plus impulsive n'est pas forcément celle du défaut. Un choc sans rapport avec le roulement l'élève aussi ; Smith et Randall relèvent des enregistrements CWRU avec un contenu impulsif étranger au défaut annoncé (résumé secondaire de leur article). Une alternative est l'**infogram** (Antoni, 2016), qui mesure la négentropie de l'enveloppe carrée et de son spectre.
- Autres étapes de la procédure semi-automatique de Randall : suivi d'ordres, retrait des composantes discrètes (DRS, SANC ou prédiction linéaire), déconvolution (MED). Le **pré-blanchiment cepstral** est une variante (Borghesani et al., 2013).

### Le jeu CWRU et ses biais

- **Ce qu'il contient** (Bearing Data Center) : un moteur de 2 hp, des défauts créés par **électro-érosion** (EDM) sur la bague interne, les billes et la bague externe, de 0,007 à 0,040 pouce de diamètre, des charges de 0 à 3 hp et des vitesses de 1 720 à 1 797 tr/min. Smith et Randall comptent 161 enregistrements répartis en quatre catégories (référence saine à 48 kHz, défauts 12 kHz et 48 kHz côté entraînement, 12 kHz côté ventilateur ; chiffres du résumé secondaire cité plus bas).
- **Un benchmark physique d'abord.** Smith et Randall (2015) appliquent trois techniques établies à tout le jeu. D'après un résumé secondaire de l'article (non relu dans le texte intégral) : les plus petits défauts de bague externe, dans la zone de charge, donnent les signatures classiques ; les défauts de bille sont parmi les plus difficiles ; un **jeu mécanique** pèse plus que la taille du défaut ou la condition de marche ; les auteurs mettent en garde contre des classifications « non physiques » produites par des algorithmes d'apprentissage et recommandent d'indiquer le numéro exact de chaque enregistrement.
- **Défauts artificiels contre défauts naturels.** Une entaille d'EDM est propre et connue ; un défaut naturel évolue et se mêle à d'autres usures. Sur le jeu de Paderborn, entraîner sur des dommages artificiels ou sur des dommages réels donne des exactitudes différentes (Lessmeier et al., 2016) : un score obtenu sur des défauts usinés ne se transpose pas tel quel à une machine en service.
- **Fuite entre fenêtres d'un même enregistrement.** Découper un enregistrement en fenêtres puis tirer train et test au hasard met des fenêtres quasi identiques des deux côtés ; le modèle apprend l'enregistrement, pas le défaut. Vieira et al. (arXiv, 2025 ; accepté à MSSP) montrent que les découpages par segment ou par condition gonflent les métriques, et proposent un découpage **par roulement physique**. Ils rapportent aussi, d'après Rosa et al., que 40 études sur 41 utilisant CWRU entre 2008 et 2020 présentaient un schéma exposé à ce biais, et, à propos de travaux antérieurs, des exactitudes qui passent d'environ 100 % à 40-60 % selon la configuration quand on sépare les roulements.
- **Le jeu est petit.** Une seule configuration saine (donc découpée à coup sûr entre train et test) et, dans l'analyse de Vieira et al., environ vingt composants défectueux distincts. Hendriks, Dumond et Knox (2022) proposent de découper par taille de défaut. Un score proche de la perfection sur CWRU ne vaut que si le protocole de découpage est donné ; aucun score de ce genre n'est cité ici, faute de source lue qui en décrive un protocole propre.

## Les maths, simplement

- Pour $f_r$ en Hz, avec $\varphi$ l'angle de contact :
  - $\mathrm{BPFO}=\dfrac n2 f_r\Big(1-\dfrac dD\cos\varphi\Big)$
  - $\mathrm{BPFI}=\dfrac n2 f_r\Big(1+\dfrac dD\cos\varphi\Big)$
  - $\mathrm{BSF}=\dfrac{D}{2d} f_r\Big(1-\big(\tfrac dD\cos\varphi\big)^2\Big)$
  - $\mathrm{FTF}=\dfrac12 f_r\Big(1-\dfrac dD\cos\varphi\Big)$

  (formules de la documentation MathWorks `bearingFaultBands`, recoupées par une seconde source ; BPFO + BPFI $= n f_r$ en découle directement.)
- **Exemple CWRU, roulement côté entraînement** (SKF 6205-2RS) : $d=0{,}3126$ pouce, $D=1{,}537$ pouce, $\varphi=0$. La page du Bearing Data Center ne donne pas $n$ ; $n=9$ est la valeur qui reproduit ses multiples publiés (3,5848 pour la bague externe, 5,4152 pour la bague interne, 0,39828 pour la cage). À 1 797 tr/min ($f_r\approx 29{,}95$ Hz), cela donne BPFO $\approx 107{,}4$ Hz et BPFI $\approx 162{,}2$ Hz. À 1 730 tr/min, BPFO tombe à 103,4 Hz : **la vitesse réelle compte**, pas la nominale.
- Les mêmes formules avec $n=8$ pour le roulement côté ventilateur (6203-2RS) retrouvent les multiples de la page : 3,053 pour la bague externe et 4,947 pour la bague interne.

## En pratique

- **Mesurer la vitesse** avec l'enregistrement (tachymètre ou estimation), sinon les raies sont mal placées. À vitesse variable : suivi d'ordres.
- **Chercher plusieurs signatures** : la fréquence caractéristique et ses harmoniques dans le spectre d'enveloppe ; une seule raie peut être un hasard.
- **Découper par roulement, pas par fenêtre.** C'est la règle qui compte le plus : voir [[Data leakage]] et [[Validation croisée]]. Garder un roulement entier hors de l'entraînement, y compris pour la classe saine (impossible avec CWRU, qui n'a qu'une configuration saine : limite du jeu).
- **Rapporter par type et taille de défaut**, pas une exactitude globale ; une classe rare se juge avec les métriques de [[Imbalanced classification]].
- **Alimenter un modèle** avec les amplitudes du spectre d'enveloppe aux quatre fréquences plutôt qu'avec le signal brut : le modèle reste lisible et la physique garde la main.
- **Peu de pannes réelles** : la situation normale en usine. Voir [[Maintenance prédictive avec peu de pannes]] et [[Jumeau numérique et modèles hybrides]].
- Sketch minimal, essayé sur un signal synthétique (chocs à 107,36 Hz excitant une résonance à 3 kHz, bruit gaussien, $f_s=12$ kHz ; le pic de l'enveloppe sort à 107,7 Hz avec `nperseg=2**14`) :

```python
import numpy as np
from scipy.signal import butter, sosfiltfilt, hilbert, welch

sos = butter(4, [2000, 4000], btype="bandpass", fs=fs, output="sos")
env = np.abs(hilbert(sosfiltfilt(sos, x)))
f, p = welch(env - env.mean(), fs=fs, nperseg=2**14)   # pic attendu à BPFO
```

## Approches voisines & alternatives

- [[Analyse vibratoire]] — RMS, kurtosis, enveloppe, suivi d'ordres.
- [[Indicateurs de santé]] — suivre l'évolution plutôt que classer.
- [[Surveillance conditionnelle et modes de défaillance]] — où le roulement s'insère parmi les modes de défaillance.
- [[Jeux de données PHM]] — CWRU et ses voisins, avec leurs limites.
- [[Time series anomaly detection]] et [[Détection d'outliers multivariée]] — sans étiquette de défaut, détecter l'écart à l'état sain.
- [[Autoencodeurs]] — apprendre la normalité sur l'état sain.
- [[RUL par apprentissage profond]] — la suite, côté pronostic.

## Pour aller plus loin

- Smith & Randall (2015), *Rolling element bearing diagnostics using the Case Western Reserve University data: A benchmark study*, MSSP 64-65, 100-131. DOI : https://doi.org/10.1016/j.ymssp.2015.04.021
- Randall & Antoni (2011), *Rolling element bearing diagnostics — A tutorial*, MSSP 25(2), 485-520. DOI : https://doi.org/10.1016/j.ymssp.2010.07.017
- Antoni (2006), *The spectral kurtosis: a useful tool for characterising non-stationary signals*, MSSP 20(2), 282-307. DOI : https://doi.org/10.1016/j.ymssp.2004.09.001
- Antoni (2007), *Fast computation of the kurtogram for the detection of transient faults*, MSSP 21(1), 108-124. DOI : https://doi.org/10.1016/j.ymssp.2005.12.002
- Antoni (2016), *The infogram: Entropic evidence of the signature of repetitive transients*, MSSP 74, 73-94. DOI : https://doi.org/10.1016/j.ymssp.2015.04.034
- Hendriks, Dumond, Knox (2022), *Towards better benchmarking using the CWRU bearing fault dataset*, MSSP 169, 108732. DOI : https://doi.org/10.1016/j.ymssp.2021.108732
- Vieira, Bauler, Rosa, Silva (2025), *Towards a more realistic evaluation of machine learning models for bearing fault diagnosis*, arXiv:2509.22267 (accepté à MSSP 258, 2026). https://arxiv.org/abs/2509.22267
- Rosa, Braga, Silva (2024), *Benchmarking deep learning models for bearing fault diagnosis using the CWRU dataset: A multi-label approach*, arXiv:2407.14625. https://arxiv.org/abs/2407.14625
- Lessmeier, Kimotho, Zimmer, Sextro (2016), *Condition monitoring of bearing damage in electromechanical drive systems by using motor current signals of electric motors: a benchmark data set for data-driven classification*, PHM Society European Conference. DOI : https://doi.org/10.36001/phme.2016.v3i1.1577
- Borghesani, Pennacchi, Randall, Sawalhi, Ricci (2013), *Application of cepstrum pre-whitening for the diagnosis of bearing faults under variable speed conditions*, MSSP 36(2), 370-384. DOI : https://doi.org/10.1016/j.ymssp.2012.11.001
- Case Western Reserve University, [Bearing Data Center](https://engineering.case.edu/bearingdatacenter/welcome) et sa [page des caractéristiques de roulement](https://engineering.case.edu/bearingdatacenter/bearing-information) ; documentation MathWorks : [bearingFaultBands](https://www.mathworks.com/help/predmaint/ref/bearingfaultbands.html), [exemple MFPT](https://www.mathworks.com/help/predmaint/ug/Rolling-Element-Bearing-Fault-Diagnosis.html), [kurtogram](https://www.mathworks.com/help/signal/ref/kurtogram.html).
