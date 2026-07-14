---
galaxie: dev
type: service
nom: papermill
alias: [Papermill]
pitch: "Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI."
categorie: tooling/notebook
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [notebook, reproducibility]
url_docs: https://papermill.readthedocs.io/
url_repo: https://github.com/nteract/papermill
---

# papermill

## Pourquoi

Exécute un notebook Jupyter de **manière non interactive et paramétrée**. On marque une cellule du tag `parameters` ; papermill **injecte** de nouvelles valeurs au-dessus à l'exécution (`papermill in.ipynb out.ipynb -p date 2026-06-11`), lance le notebook de bout en bout via un kernel et écrit un **notebook de sortie exécuté** (sorties incluses). Cela transforme un notebook en **brique rejouable** : même notebook, paramètres différents → un rapport daté, un balayage de configs, une étape planifiée en CI ou orchestrée. API Python et CLI ; lecture/écriture vers le système de fichiers, S3, GCS, Azure.

## Quand l'utiliser

- **Rejouer** un notebook avec des paramètres variables (date, dataset, région) sans dupliquer le code.
- Exécuter un notebook **headless en CI** pour vérifier qu'il tourne de bout en bout, et échouer si une cellule lève.
- En faire une **étape orchestrée** (Airflow, cron) produisant un notebook de sortie archivable.
- Lancer un **balayage** : N exécutions du même notebook sur une grille de paramètres.

## Quand NE PAS l'utiliser

- Versionner le notebook source proprement → [[Dev/Services/jupytext|jupytext]] (papermill exécute, ne nettoie pas le diff).
- Produire un document mis en page (HTML/PDF) plutôt qu'un `.ipynb` exécuté → [[Dev/Services/Quarto|Quarto]].
- Logique destinée à la production durable : extraire le cœur en module `.py` importé et testé, plutôt que d'exécuter un notebook.
- Notebook réactif interactif → [[Dev/Services/Marimo|Marimo]].

## Déploiement & coût

- Bibliothèque Python (`uv add papermill`) ; API `papermill.execute_notebook(...)` ou CLI `papermill`. BSD-3-Clause, gratuit, single-node.
- S'appuie sur un kernel (`nbclient`) : le bon kernel/env doit être disponible à l'exécution.
- E/S vers fichiers locaux ou stockage objet (S3/GCS/Azure) via les handlers intégrés. Coût nul côté licence.

## Pièges

- Le notebook doit être **idempotent** et exécutable dans l'ordre : un état caché le fait échouer en headless (c'est un effet de bord souhaitable — ça révèle le problème).
- La cellule `parameters` doit être taguée correctement, sinon l'injection est silencieusement ignorée.
- Le notebook de sortie embarque les sorties : ne pas le commiter en git brut (cf. [[Notebooks-as-code]]).
- Kernel/env manquant ou divergent = échec d'exécution : épingler l'environnement ([[Dev/Services/uv|uv]]).

## Alternatives

- _Alternative classique non fichée : `jupyter nbconvert --execute` (exécution sans la couche de paramétrage). [[Dev/Services/Quarto|Quarto]] exécute aussi un notebook, mais pour le publier, pas pour produire un `.ipynb` paramétré._

## Liens

- [[Notebooks-as-code]] — papermill assure l'exécution non interactive et rejouable du concept.
- [[Dev/Services/jupytext|jupytext]] — versionner le source ; papermill exécute. Souvent combinés.
- [[Dev/Services/uv|uv]] — environnement épinglé garantissant une exécution reproductible.
- Doc : https://papermill.readthedocs.io/
