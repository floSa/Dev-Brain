---
role: brique
nom: PyBaMM
alias: [pybamm, Python Battery Mathematical Modelling]
pitch: "Bibliothèque Python de simulation de batteries par modèles physiques (SPM, SPMe, DFN, MPM, MSMR…) : un cadre pour écrire et résoudre des équations différentielles, une bibliothèque de modèles et de jeux de paramètres, des outils d'expériences de cyclage ; les modèles de vieillissement (SEI, dépôt de lithium, perte de matière active) y sont des options, pas de l'apprentissage."
categorie: ml/maintenance
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [digital-twin, predictive-maintenance, rul]
url_docs: https://docs.pybamm.org/
url_repo: https://github.com/pybamm-team/PyBaMM
---

# PyBaMM

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de simulation de batteries par modèles physiques (SPM, SPMe, DFN, MPM, MSMR…) : un cadre pour écrire et résoudre des équations différentielles, une bibliothèque de modèles et de jeux de paramètres, des outils d'expériences de cyclage ; les modèles de vieillissement (SEI, dépôt de lithium, perte de matière active) y sont des options, pas de l'apprentissage.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Simule une cellule lithium-ion à partir de ses équations physiques, et non d'un ajustement sur des données. Le README en décrit trois parties : un **cadre** pour écrire et résoudre des systèmes d'équations différentielles, une **bibliothèque** de modèles de batterie et de jeux de paramètres, et des outils pour simuler des **expériences** propres aux batteries et en visualiser le résultat.

- **Modèles** — le dépôt fournit, côté lithium-ion, `SPM` (particule unique), `SPMe`, `DFN` (Doyle-Fuller-Newman), `MPM`, `MSMR` et `NewmanTobias` (exports du module `pybamm.lithium_ion`), plus des variantes « basic » (`BasicDFN`, `BasicDFNComposite`, `BasicDFNHalfCell`, `BasicDFN2D`, `BasicDFNUnstructured`). Le modèle se choisit selon le compromis entre fidélité et temps de calcul.
- **Vieillissement** — le modèle accepte des options de dégradation, relevées dans le code (`base_battery_model.py`) : `SEI` (`reaction limited`, `solvent-diffusion limited`, `electron-migration limited`, `interstitial-diffusion limited`, `ec reaction limited`…), `lithium plating` (`reversible`, `partially reversible`, `irreversible`), `loss of active material` (`stress-driven`, `reaction-driven`, `current-driven`, et leurs combinaisons) et `particle mechanics` (`swelling only`, `swelling and cracking`). Rien n'est actif par défaut : chaque option vaut `none` ou `false` tant qu'elle n'est pas posée.
- **Expériences** — `pybamm.Experiment` décrit un protocole en phrases (`"Discharge at C/10 for 10 hours or until 3.3 V"`, `"Hold at 4.1 V until 50 mA"`) et le répète, ce qui permet de simuler des centaines de cycles.
- **Paramètres** — des jeux de paramètres nommés d'après leurs articles (le changelog de la version 26.9.0.0 ajoute `Bonkile2024`, graphite/silicium et NMC). Un jeu décrit une cellule précise : l'utiliser pour une autre chimie sans recalage donne un résultat sans valeur.
- **Résolution** — solveurs fondés sur CasADi et `pybammsolvers` ; le changelog de la 26.9.0.0 impose `pybammsolvers>=0.10.0` et cite l'`IDAKLUSolver`. Un solveur JAX est optionnel.

Le projet suit un gouvernement ouvert et est parrainé fiscalement par NumFOCUS. Les versions suivent CalVer (`YY.MM.N.P`) ; le README prévient que toute version peut casser l'API, les ruptures étant listées en tête du `CHANGELOG.md`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comprendre ou prédire un vieillissement à partir de mécanismes (SEI, plating, fissuration) | Aucune connaissance de la chimie ni de paramètres de cellule : les paramètres sont le vrai travail |
| Générer des courbes synthétiques pour un modèle appris, quand les cycles de laboratoire manquent | Prendre ces courbes pour des mesures : leur biais est celui du modèle et du jeu de paramètres |
| Un jumeau numérique de batterie, recalé sur des mesures (voir [[Jumeau numérique et modèles hybrides]]) | Un estimateur de SOH léger à embarquer : PyBaMM est un outil de simulation, pas un estimateur prêt à l'emploi |
| Reproduire un article de modélisation, avec un code ouvert et cité | Un parc de cellules de chimies variées sans modèle physique : un modèle appris sur des courbes réelles ([[Santé de batterie (SOH et RUL)]]) s'y prête mieux |

## Mise en œuvre

- Installation — `uv add pybamm` (ou `pip install pybamm` ; conda-forge propose `pybamm` et `pybamm-base`, avec un trou entre 24.11.2 et 25.6, non disponibles)
- Point d'entrée — API Python : `model = pybamm.lithium_ion.DFN()`, `sim = pybamm.Simulation(model)`, `sim.solve([0, 3600])`, `sim.plot()` ; avec un protocole, `pybamm.Simulation(model, experiment=experiment)`
- Prérequis — Python 3.10 à 3.14 (`>=3.10,<3.15` sur PyPI, version 26.9.0.0) ; Linux, macOS et Windows
- Exécution — en bibliothèque, calcul local ; aucune infrastructure à héberger
- Coût — gratuit, BSD-3-Clause (fichier LICENSE du dépôt) ; coût réel : temps de calcul des modèles complets et surtout l'identification des paramètres. Le paquet voisin PyBOP (BSD-3-Clause, même écosystème) s'en charge : paramétrage et optimisation de modèles de batterie

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucune autre brique du dossier ne simule une cellule, et les autres simulateurs de batterie n'ont pas de fiche.

### Compléments

- Aucun complément déclaré : les briques du dossier traitent des signaux et des durées de vie, pas de modèles physiques de cellule.

## Ressources

- Documentation — https://docs.pybamm.org/
- Dépôt — https://github.com/pybamm-team/PyBaMM
- Papier — Sulzer, Marquis, Timms, Robinson, Chapman, *Python Battery Mathematical Modelling (PyBaMM)*, Journal of Open Research Software 9(1), 2021 : https://doi.org/10.5334/jors.309

## Voir aussi

- [[Santé de batterie (SOH et RUL)]] — la notion : SOH, fin de vie, modèles physiques, empiriques et appris
- [[Jumeau numérique et modèles hybrides]] — la boucle mesurer, recaler, prévoir dont PyBaMM est le modèle
- [[Maintenance prédictive]] — le hub du dossier
- [[Jeux de données PHM]] — les jeux de batteries (NASA PCoE) contre lesquels confronter une simulation
- [[Indicateurs de santé]] — l'état de santé résumé en une grandeur
