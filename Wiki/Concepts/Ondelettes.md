---
galaxie: wiki
type: concept
nom: Ondelettes
alias: [wavelets, DWT, CWT, transformée en ondelettes, multirésolution, scalogramme]
categorie: concept/signal
domaines: [data-sci, ml-eng]
tags: [signal-processing, wavelet]
---

# Ondelettes

## Aperçu

- Analyse **temps-échelle** : décompose un signal sur des fonctions localisées (les ondelettes), obtenues en **dilatant** et **translatant** une ondelette mère. Capture *quand* une fréquence apparaît — ce que la [[Transformée de Fourier]] ne dit pas.
- **Multirésolution** : bonne résolution fréquentielle pour les basses fréquences (motifs lents), bonne résolution temporelle pour les hautes fréquences (transitoires brefs).

## Concepts clés

### CWT — transformée continue
- Corrèle le signal avec l'ondelette mère à **toutes** les échelles $a$ et positions $b$. Sortie : un **scalogramme** (carte échelle × temps). Très redondante → analyse et visualisation.

### DWT — transformée discrète
- Échelles **dyadiques** ($a = 2^j$), calculée par un **banc de filtres** (un étage d'approximation passe-bas + un de détails passe-haut, itéré) : c'est l'algorithme de Mallat, en $O(N)$. Non redondante → compression et débruitage.

### Ondelette mère
- **Morlet** (sinusoïde fenêtrée, bonne pour l'analyse fréquentielle), **Daubechies** (compacte, reine de la DWT), **Haar** (la plus simple, marches d'escalier). Le choix dépend de la forme des motifs recherchés.

### Débruitage par seuillage
- DWT → **seuiller** les coefficients de détail (soft / hard thresholding) → reconstruire. Retire le bruit tout en **préservant les ruptures**, là où un filtre passe-bas les lisserait.

## Les maths, simplement

- CWT : $W(a,b) = \frac{1}{\sqrt{a}} \int x(t)\, \psi^*\!\left(\frac{t-b}{a}\right) dt$, où $\psi$ est l'ondelette mère, $a$ l'**échelle** (∝ $1/$fréquence) et $b$ la **translation** (position).
- **Compromis de Heisenberg** : impossible d'être arbitrairement précis en temps *et* en fréquence. Les ondelettes répartissent ce compromis selon l'échelle — fines en temps aux hautes fréquences, fines en fréquence aux basses.

## En pratique

- [[Dev/Services/PyWavelets|PyWavelets]] (`pywt`) : `wavedec` / `waverec` (DWT), `cwt` (scalogramme).
- Terrain de prédilection : signaux **non stationnaires**, transitoires, ruptures — vibrations machine, ECG, défauts — là où la FFT moyenne tout et masque l'instant de l'événement.
- Débruitage, compression (JPEG 2000 repose sur les ondelettes), détection de singularités.

## Approches voisines & alternatives

- [[STFT et spectrogramme]] — temps-fréquence à fenêtre **fixe** ; les ondelettes offrent une résolution **adaptative** à l'échelle.
- [[Transformée de Fourier]] — base fréquentielle globale, sans localisation temporelle.
- [[Filtrage numérique]] — la DWT *est* un banc de filtres passe-bas / passe-haut itéré.
- [[Time series anomaly detection]] — les ondelettes repèrent transitoires et ruptures dans une série.
- [[Traitement du signal]] — page chapeau.

## Pour aller plus loin

- Stéphane Mallat — *A Wavelet Tour of Signal Processing*.
- Ingrid Daubechies — *Ten Lectures on Wavelets*.
