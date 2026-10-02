---
role: notion
nom: Analyse vibratoire
alias: [Vibration analysis, Analyse de vibrations, Suivi d'ordres, Order tracking, Facteur de crête]
categorie: signal/traitement
domaines: [data-sci, ml-eng]
tags: [vibration-analysis, signal-processing, fourier, condition-monitoring]
---

# Analyse vibratoire

## Aperçu

- Lire le signal d'un **accéléromètre** posé sur une machine tournante pour en déduire son état.
- Ce signal a une structure propre : des composantes **liées à la rotation** (multiples de la fréquence de rotation) et, pour un défaut local, des **chocs répétés**. D'où une boîte à outils : indicateurs globaux, spectre, suivi d'ordres, enveloppe, cepstre.
- Cette page donne les outils de signal. Les usages vivent à côté : le diagnostic d'un roulement dans [[Diagnostic de défauts de roulements]], la suite de la chaîne (suivre, fusionner, prévoir) dans [[Indicateurs de santé]] et [[Maintenance prédictive et RUL]], le cadre d'ensemble dans [[Surveillance conditionnelle et modes de défaillance]].

## Concepts clés

### Acquérir : capteur et échantillonnage

- La plupart des accéléromètres exploitent l'effet piézoélectrique. Deux familles : en **mode charge** (amplificateur externe) et **IEPE**, qui embarque un amplificateur alimenté par une source de courant (National Instruments, *Measuring Vibration with Accelerometers*). Côté acquisition : couplage AC et, pour un IEPE, excitation en courant.
- Le **montage** borne la bande utile : la même page cite plus de 6 000 Hz pour une fixation par goujon contre 500 Hz pour une sonde tenue à la main. Un capteur mal fixé borne ce qui reste mesurable en haute fréquence, là où s'expriment les chocs de roulement (modèle décrit plus bas).
- **Fréquence d'échantillonnage** $f_s$ : par le théorème d'échantillonnage (Shannon, 1949), tout ce qui dépasse $f_s/2$ se replie dans le spectre et ne se défait plus. Le filtre anti-repliement se place **avant** l'échantillonnage ; en numérique, il précède la décimation. `scipy.signal.decimate` l'applique d'office (Chebyshev de type I d'ordre 8 par défaut, phase nulle par défaut) et conseille, pour un facteur supérieur à 13, de l'appeler plusieurs fois (documentation SciPy).
- Choisir $f_s$ pour couvrir la **résonance** que les chocs excitent, pas seulement la fréquence du défaut. Exemple MathWorks sur le jeu MFPT (48,828 et 97,656 kHz) : pour un défaut de bague externe, le kurtogramme retient une bande centrée à 2,67 kHz, large de 0,763 kHz.

### Indicateurs temporels globaux

- **RMS** : l'énergie moyenne du signal. Il monte quand le niveau vibratoire monte ; des chocs brefs, peu énergétiques, se diluent dans la moyenne.
- **Facteur de crête** : le pic rapporté au RMS. Il grimpe quand des chocs dépassent le niveau de fond.
- **Kurtosis** : le moment d'ordre 4 normalisé, qui pèse très fort les valeurs extrêmes. Il mesure l'**impulsivité**.
- Repères exacts : une sinusoïde a un facteur de crête de $\sqrt2\approx1{,}414$ (valeur de la documentation MathWorks, retrouvée par calcul) et un kurtosis de 1,5 ; un bruit gaussien a un kurtosis de 3. Aucun seuil d'alarme chiffré n'est donné ici : ils dépendent de la machine, du capteur et du point de mesure.
- Ces trois grandeurs se calculent **par fenêtre** et forment une série temporelle, qui devient l'entrée d'un indicateur de santé ([[Indicateurs de santé]]).

### Spectre

- La FFT ([[Transformée de Fourier]]) donne les raies. Pour des signaux bruités, `scipy.signal.welch` estime la densité spectrale de puissance par **moyenne de périodogrammes modifiés** calculés sur des segments qui se recouvrent. Valeurs par défaut de la documentation : segments de 256 points, fenêtre de Hann, recouvrement de 50 %, mise à l'échelle « density » (en unité²/Hz).
- Compromis : segments longs, bonne résolution $\Delta f = f_s/n_\text{perseg}$ mais peu de moyennes ; segments courts, estimation lisse mais raies étalées.
- Dans un spectre brut, les chocs d'un roulement naissant, peu énergétiques, se noient sous les composantes déterministes plus fortes (le tutoriel de Randall note que les signaux d'engrenage, déterministes, peuvent dominer ceux du roulement, stochastiques à cause du glissement aléatoire). C'est la raison d'être de l'enveloppe.

### Suivi d'ordres

- Un **ordre** est une fréquence qui vaut un multiple fixe de la vitesse de rotation de référence : l'ordre 2 vaut deux fois la fréquence de rotation (documentation MathWorks, *Order Analysis*).
- Quand la vitesse varie (démarrage, ralentissement, charge), chaque composante change de fréquence et le spectre s'**étale**. Le **suivi d'ordres** rééchantillonne le signal à incréments de phase constants plutôt qu'à pas de temps constant : chaque ordre redevient une sinusoïde stationnaire. La vitesse vient en général d'un signal de tachymètre.
- Dans la procédure semi-automatique des diapositives de Randall (PHM 2011), c'est la première des cinq étapes : suivi d'ordres, retrait des composantes discrètes, déconvolution, choix de la bande par kurtosis spectral, analyse d'enveloppe.

### Enveloppe par transformée de Hilbert

- Modèle usuel (décrit dans le tutoriel de Randall & Antoni ; non relu dans le texte intégral) : un défaut local produit un choc à chaque passage de l'élément sur le défaut, et chaque choc excite une résonance de la structure. Le signal est alors une **porteuse haute fréquence modulée en amplitude** par la répétition des chocs. L'enveloppe démodule cette porteuse et laisse apparaître la cadence des chocs.
- `scipy.signal.hilbert` calcule le **signal analytique** par FFT : mise à zéro des fréquences négatives et doublement des positives. La partie imaginaire est la transformée de Hilbert ; l'enveloppe est `np.abs` du résultat (exemple de la documentation SciPy 1.18 sur un chirp modulé).
- Chaîne type (exemple MathWorks sur le jeu MFPT) : filtre passe-bande dans la bande choisie, extraction de l'enveloppe, filtre passe-bas, FFT de l'enveloppe. Voir [[Filtrage numérique]] pour la conception du filtre. La suite, avec les fréquences à repérer, est dans [[Diagnostic de défauts de roulements]].

### Cepstre

- Le cepstre réel est la transformée de Fourier inverse du logarithme du module du spectre. L'abscisse s'appelle la **quéfrence** (Bogert, Healy, Tukey, 1963, qui l'ont introduit pour détecter des échos). Il transforme une famille de raies ou de bandes latérales régulièrement espacées en un pic isolé.
- Autre usage : le **pré-blanchiment cepstral**. On édite l'amplitude du spectre dans le cepstre, puis on recompose avec la phase d'origine ; au cas extrême, le cepstre réel est mis à zéro et le spectre d'amplitude devient uniforme, ce qui retire raies discrètes et résonances (diapositives de Randall). Application à vitesse variable : Borghesani et al. (2013).

## Les maths, simplement

- RMS : $\mathrm{RMS}=\sqrt{\dfrac1N\sum_{i=1}^{N}x_i^2}$, pour $N$ échantillons $x_i$.
- Facteur de crête : $\mathrm{CF}=\dfrac{\max_i |x_i|}{\mathrm{RMS}}$ (définition de `peak2rms`, MathWorks).
- Kurtosis : $\kappa=\dfrac{\mathbb E\big[(x-\mu)^4\big]}{\sigma^4}$, avec $\mu$ la moyenne et $\sigma$ l'écart type. `scipy.stats.kurtosis` rend par défaut le kurtosis **de Fisher**, $\kappa-3$, nul pour une loi normale : ne pas comparer ce nombre à des valeurs de kurtosis « de Pearson ».
- Kurtosis spectral : le kurtosis de l'enveloppe complexe $y_f(t)$ du signal filtré autour de $f$, $K(f)=\dfrac{\mathbb E\big[|y_f|^4\big]}{\mathbb E\big[|y_f|^2\big]^2}-2$. Il vaut 0 pour un bruit gaussien et grimpe dans les bandes où des chocs se répètent (forme rapportée par la documentation MathWorks et la littérature secondaire ; non relue dans l'article d'Antoni, 2006). Son parcours systématique sur des bandes de largeur variable s'appelle le **kurtogramme** (Antoni, 2007).
- Signal analytique : $x_a(t)=x(t)+i\,\mathcal H\{x\}(t)$ et enveloppe $A(t)=|x_a(t)|$.
- Ordre : $o=f/f_r$, avec $f_r$ la fréquence de rotation instantanée.
- Cepstre réel : $c(\tau)=\mathcal F^{-1}\big\{\log|X(f)|\big\}$.

## En pratique

- **Fenêtrer** pour calculer RMS, crête et kurtosis, puis suivre la série : c'est la dérive qui informe.
- **Un pic parasite fausse le kurtosis et la crête** : à la puissance 4, un seul échantillon aberrant (câble, choc de manipulation) pèse plus que tout le reste. Contrôler le signal brut avant d'interpréter.
- **Ne pas mélanger les régimes** : un niveau vibratoire dépend de la vitesse et de la charge. Normaliser ou comparer à régime égal, sous peine de lire un changement de régime comme un défaut (voir aussi [[Types d'anomalies et régimes de supervision]]).
- **Filtrer avant l'enveloppe**, sinon la démodulation est dominée par les composantes les plus énergétiques, qui ne portent pas l'information des chocs. Le choix de la bande est le point délicat : voir le kurtogramme dans [[Diagnostic de défauts de roulements]].
- **Vitesse variable** : sans suivi d'ordres, raies étalées. Prévoir un tachymètre dès l'acquisition.
- Ces indicateurs rejoignent les caractéristiques classiques d'une série temporelle ([[Time series feature engineering]]) ; seul le sens physique change.

## Approches voisines & alternatives

- [[Transformée de Fourier]] — le socle : DFT, FFT, fuite spectrale, repliement.
- [[STFT et spectrogramme]] — quand le contenu spectral évolue (démarrage, régime variable) et que le suivi d'ordres n'est pas disponible.
- [[Ondelettes]] — résolution temps-échelle adaptative, souvent employée pour les chocs transitoires ; [[PyWavelets]] pour les mettre en œuvre.
- [[Filtrage numérique]] — passe-bande avant l'enveloppe, anti-repliement avant la décimation.
- [[scipy.signal]] — `hilbert`, `welch`, `decimate`, `butter`, `sosfiltfilt`.
- [[Traitement du signal]] — page chapeau.
- [[Time series anomaly detection]] — détecter une dérive sur la série d'indicateurs plutôt que lire le spectre à la main.
- [[Jeux de données PHM]] — des enregistrements de vibration de roulements pour s'exercer.
- [[Inférence en bordure - modèles sur du matériel d'atelier]] et [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — calculer ces indicateurs sur site et remonter les mesures.

## Pour aller plus loin

- Randall & Antoni (2011), *Rolling element bearing diagnostics — A tutorial*, Mechanical Systems and Signal Processing 25(2), 485-520. DOI : https://doi.org/10.1016/j.ymssp.2010.07.017 ; diapositives de Randall (PHM 2011) : https://phmsociety.org/wp-content/uploads/2010/11/Tutorial-Diagnostics-Randall.pdf
- Antoni (2006), *The spectral kurtosis: a useful tool for characterising non-stationary signals*, MSSP 20(2), 282-307. DOI : https://doi.org/10.1016/j.ymssp.2004.09.001
- Antoni (2007), *Fast computation of the kurtogram for the detection of transient faults*, MSSP 21(1), 108-124. DOI : https://doi.org/10.1016/j.ymssp.2005.12.002
- Borghesani, Pennacchi, Randall, Sawalhi, Ricci (2013), *Application of cepstrum pre-whitening for the diagnosis of bearing faults under variable speed conditions*, MSSP 36(2), 370-384. DOI : https://doi.org/10.1016/j.ymssp.2012.11.001
- Bogert, Healy, Tukey (1963), *The quefrency alanysis of time series for echoes: cepstrum, pseudo-autocovariance, cross-cepstrum and saphe cracking*, in *Proceedings of the Symposium on Time Series Analysis*, Wiley, 209-243.
- Shannon (1949), *Communication in the presence of noise*, Proceedings of the IRE 37(1), 10-21. DOI : https://doi.org/10.1109/JRPROC.1949.232969
- Documentations : SciPy ([hilbert](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html), [welch](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html), [decimate](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html), [stats.kurtosis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html)) ; MathWorks ([Order Analysis](https://www.mathworks.com/help/signal/ug/order-analysis-of-a-vibration-signal.html), [kurtogram](https://www.mathworks.com/help/signal/ref/kurtogram.html), [peak2rms](https://www.mathworks.com/help/signal/ref/peak2rms.html), [roulements MFPT](https://www.mathworks.com/help/predmaint/ug/Rolling-Element-Bearing-Fault-Diagnosis.html)) ; National Instruments, [*Measuring Vibration with Accelerometers*](https://www.ni.com/en/shop/data-acquisition/sensor-fundamentals/measuring-vibration-with-accelerometers.html).
