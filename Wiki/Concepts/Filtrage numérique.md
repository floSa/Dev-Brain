---
galaxie: wiki
type: concept
nom: Filtrage numérique
alias: [filtre numérique, Butterworth, fenêtrage, apodisation, FIR, IIR, transformée de Hilbert, digital filter]
categorie: concept/signal
domaines: [data-sci, ml-eng]
tags: [signal-processing, digital-filter]
---

# Filtrage numérique

## Aperçu

- Atténuer ou renforcer des composantes d'un signal selon leur **fréquence** : passe-bas, passe-haut, passe-bande, coupe-bande. Sert à débruiter, isoler une bande utile, ou faire l'anti-aliasing avant un sous-échantillonnage.
- Deux familles : **FIR** (réponse impulsionnelle finie) et **IIR** (infinie, récursive).

## Concepts clés

### FIR vs IIR
- **FIR** : non récursif, **toujours stable**, **phase linéaire** possible (aucune distorsion de forme), mais demande un ordre élevé pour être raide.
- **IIR** : récursif, **raide à faible ordre** (peu de calcul), mais phase non linéaire et risque d'instabilité numérique.

### Butterworth & autres prototypes
- **Butterworth** : réponse **maximalement plate** en bande passante (aucune ondulation) — le choix par défaut, transition douce.
- **Chebyshev** : transition plus raide au prix d'ondulations ; **elliptique** : la plus raide, ondulations des deux côtés. Compromis platitude / raideur / phase.

### Réponse en fréquence
- Un filtre se caractérise par sa réponse $H(f)$ : **gain** et **phase** fréquence par fréquence. On la lit et on la conçoit via la [[Transformée de Fourier]].

### Fenêtrage (apodisation)
- Avant une FFT, ou pour concevoir un FIR : multiplier le signal par une **fenêtre** (Hann, Hamming, Blackman) atténue la **fuite spectrale** due à la troncature. Compromis entre largeur du lobe principal et niveau des lobes secondaires.

### Filtre à phase nulle & Hilbert
- Filtrer en **aller-retour** (`filtfilt`) annule le déphasage — précieux en analyse hors ligne.
- La **transformée de Hilbert** construit le signal analytique → enveloppe et fréquence instantanée (démodulation).

## Les maths, simplement

- Équation aux différences : $y[n] = \sum_k b_k\, x[n-k] - \sum_k a_k\, y[n-k]$. Cas FIR : tous les $a_k$ nuls (sauf $a_0$) → sortie = simple convolution des entrées.
- Butterworth d'ordre $n$ : $|H(f)|^2 = \dfrac{1}{1 + (f/f_c)^{2n}}$, où $f_c$ est la **fréquence de coupure** et $n$ règle la raideur.

## En pratique

- [[Dev/Services/scipy.signal|scipy.signal]] : `butter` + `sosfilt` (format *second-order sections*, stable) ou `filtfilt` (phase nulle) ; `firwin` (FIR) ; `get_window` (fenêtres).
- **Normaliser la coupure par la fréquence de Nyquist** ($f_s/2$) — erreur classique.
- **Toujours filtrer passe-bas avant de sous-échantillonner** (anti-aliasing), sinon repliement irréversible.

## Approches voisines & alternatives

- [[Transformée de Fourier]] — cadre d'analyse de la réponse en fréquence d'un filtre.
- [[Ondelettes]] — débruitage alternatif par **seuillage** des coefficients, plutôt que par coupure fréquentielle ; et la DWT est elle-même un banc de filtres.
- [[STFT et spectrogramme]] — le fenêtrage d'apodisation y est central.
- [[Time series feature engineering]] — lissage et débruitage comme prétraitement avant modèle.
- [[Traitement du signal]] — page chapeau.

## Pour aller plus loin

- Oppenheim & Schafer — *Discrete-Time Signal Processing* (conception FIR/IIR).
- Documentation `scipy.signal` — `butter`, `sosfilt`, `filtfilt`, `firwin`.
