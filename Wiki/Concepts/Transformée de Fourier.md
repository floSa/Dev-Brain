---
galaxie: wiki
type: concept
nom: Transformée de Fourier
alias: [FFT, DFT, transformée de Fourier discrète, transformée de Fourier rapide, analyse spectrale, domaine fréquentiel]
categorie: concept/signal
domaines: [data-sci, ml-eng]
tags: [signal-processing, fourier]
---

# Transformée de Fourier

## Aperçu

- Décompose un signal en une somme de **sinusoïdes** : passage du domaine temporel au **domaine fréquentiel**. Répond à « quelles fréquences composent ce signal, et avec quelle amplitude ? ».
- **DFT** : la version discrète, calculée sur $N$ échantillons. **FFT** : l'algorithme qui la calcule vite, en $O(N\log N)$ au lieu de $O(N^2)$ — c'est elle qui rend l'analyse spectrale praticable.

## Concepts clés

### DFT
- Transforme $N$ échantillons temporels en $N$ coefficients complexes $X[k]$. Chaque $X[k]$ porte l'**amplitude** et la **phase** de la fréquence $k\,f_s/N$.

### FFT
- Algorithme de Cooley-Tukey : exploite la structure récursive de la DFT (diviser pour régner) pour passer de $O(N^2)$ à $O(N\log N)$. Le plus efficace quand $N$ est une puissance de 2.

### Spectre d'amplitude & de puissance
- $|X[k]|$ = spectre d'amplitude ; $|X[k]|^2$ = **densité spectrale de puissance**. En analyse on regarde surtout le module ; la phase est souvent ignorée (mais nécessaire pour reconstruire).

### Limite : aucune localisation temporelle
- La transformée suppose le signal **stationnaire** : elle dit *quelles* fréquences sont présentes, pas *quand*. Pour un signal qui évolue → [[STFT et spectrogramme]] ou [[Ondelettes]].

## Les maths, simplement

- DFT : $X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-i 2\pi k n / N}$. Chaque terme corrèle le signal avec une sinusoïde de fréquence $k\,f_s/N$.
- **Théorème de convolution** : une convolution dans le temps devient un simple **produit** en fréquence → on filtre rapidement via FFT.
- **Wiener-Khinchin** : la densité spectrale de puissance est la transformée de Fourier de l'[[Autocorrelation]] — spectre et autocorrélation disent la même chose autrement.
- Repliement : toute énergie au-delà de $f_s/2$ se replie dans le spectre observé.

## En pratique

- `numpy.fft` / `scipy.fft` pour la FFT ; [[Dev/Services/scipy.signal|scipy.signal]] pour l'estimation spectrale (`periodogram`, `welch`). `rfft` pour un signal réel (deux fois moins de calcul, spectre non redondant).
- **Fenêtrer avant la FFT** : sans fenêtre, la troncature du signal crée de la **fuite spectrale** (l'énergie d'une raie bave sur les voisines) — cf. fenêtrage dans [[Filtrage numérique]].
- Résolution fréquentielle $\Delta f = f_s/N$ : pour distinguer deux raies proches, allonger la durée observée.

## Approches voisines & alternatives

- [[STFT et spectrogramme]] — FFT par fenêtres glissantes, pour suivre l'évolution fréquentielle d'un signal non stationnaire.
- [[Ondelettes]] — résolution temps-fréquence **adaptative**, là où Fourier est purement global.
- [[Filtrage numérique]] — la transformée explique l'action d'un filtre via sa réponse en fréquence.
- [[Autocorrelation]] — équivalent temporel du spectre (Wiener-Khinchin).
- [[Traitement du signal]] — page chapeau.

## Pour aller plus loin

- Cooley & Tukey (1965) — *An Algorithm for the Machine Calculation of Complex Fourier Series*.
- 3Blue1Brown — *But what is the Fourier Transform?* (intuition visuelle).
