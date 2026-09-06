---
role: brique
nom: PyWavelets
alias: [pywt, pywavelets, wavelet transform]
pitch: "Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle."
categorie: signal/traitement
famille: paquet
licence_type: open-source
maturite: production
langage: C / Cython / Python
alternatives: ["[[scipy.signal]]"]
complements: []
tags: [signal-processing, wavelet]
url_docs: https://pywavelets.readthedocs.io/
url_repo: https://github.com/PyWavelets/pywt
---

# PyWavelets

<!-- AUTO:BANDEAU:START -->
> Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C / Cython / Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque dédiée aux transformées en ondelettes en Python (`import pywt`). Elle
implémente la DWT et l'IDWT — et leur version 2D pour l'image —, la décomposition
multiniveau (`wavedec` / `waverec`), la CWT et son scalogramme, les paquets d'ondelettes
et le seuillage des coefficients pour le débruitage, avec une large bibliothèque
d'**ondelettes mères** : Daubechies, Symlets, Coiflets, Haar, Morlet. Le choix de
l'ondelette mère et du niveau de décomposition conditionne le résultat, et il n'existe
pas de réglage universel — c'est la décision qui structure l'usage, pas un paramètre
de finition. Reconstruire après seuillage exige la cohérence DWT ↔ IDWT : même ondelette,
même mode de padding.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analyse temps-échelle ou multirésolution d'un signal non stationnaire | Compresser ou débruiter par CWT : elle est redondante et coûteuse — c'est la DWT qui sert là, la CWT reste un outil d'analyse et de visualisation |
| Débruiter par seuillage des coefficients, là où un passe-bas lisserait les ruptures | Interpréter les extrémités comme le milieu du signal : le mode de padding (`symmetric`, `periodization`…) change les coefficients aux bords |
| Compression, détection de singularités ou de transitoires (vibrations, ECG) | |
| Extraire des features ondelettes avant un modèle ML | |

## Mise en œuvre

- Installation — `uv add pywavelets` ; le module importé s'appelle `pywt`
- Point d'entrée — import Python, `import pywt`
- Prérequis — NumPy ; cœur compilé en C et Cython, donc une roue binaire par plateforme
- Exécution — dans le process appelant, CPU, en mémoire ; rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.

## Ressources

- Documentation — https://pywavelets.readthedocs.io/
- Dépôt — https://github.com/PyWavelets/pywt

## Voir aussi

- [[Ondelettes]] — la notion : DWT, CWT, multirésolution, seuillage
- [[Traitement du signal]] — la notion du dossier
- [[Comparatif - Traitement du signal]] — ce qui départage les outils du dossier
