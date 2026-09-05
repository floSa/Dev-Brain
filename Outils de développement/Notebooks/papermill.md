---
role: brique
nom: papermill
alias: [Papermill]
pitch: "Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI."
categorie: devtools/notebook
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[jupytext]]"]
tags: [notebook, reproducibility]
url_docs: https://papermill.readthedocs.io/
url_repo: https://github.com/nteract/papermill
---

# papermill

<!-- AUTO:BANDEAU:START -->
> Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Exécute un notebook Jupyter de manière **non interactive et paramétrée**. On marque une
cellule du tag `parameters` ; papermill injecte de nouvelles valeurs juste au-dessus au
moment de l'exécution, lance le notebook de bout en bout via un kernel, et écrit un
**notebook de sortie exécuté**, sorties comprises. Le notebook devient une brique rejouable :
mêmes cellules, paramètres différents — un rapport daté, un balayage de configurations, une
étape planifiée. API Python et ligne de commande ; lecture et écriture vers le disque, S3,
GCS ou Azure. Effet de bord souhaitable : un notebook non idempotent échoue en headless,
donc le problème se voit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rejouer un notebook avec des paramètres variables — date, dataset, région — sans dupliquer le code | Versionner proprement le notebook source → [[jupytext]] : papermill exécute, il ne nettoie pas le diff |
| Exécuter un notebook headless en CI pour vérifier qu'il tourne de bout en bout, et échouer si une cellule lève | Produire un document mis en page plutôt qu'un `.ipynb` exécuté → [[Quarto]] |
| En faire une étape orchestrée — Airflow, cron — produisant un notebook de sortie archivable | Notebook réactif interactif au quotidien → [[Marimo]] |
| Lancer un balayage : N exécutions du même notebook sur une grille de paramètres | Logique destinée à durer en production : en extraire le cœur en module `.py` importé et testé, plutôt qu'exécuter un notebook |
| | La cellule `parameters` doit être taguée, sinon l'injection est silencieusement ignorée ; et le notebook de sortie embarque ses sorties, à ne pas commiter brut |

## Mise en œuvre

- Installation — `uv add papermill`
- Point d'entrée — CLI `papermill in.ipynb out.ipynb -p date 2026-06-11`, ou API `papermill.execute_notebook(...)`
- Prérequis — un kernel disponible et un environnement épinglé : kernel manquant ou divergent, et l'exécution échoue ; le notebook doit être exécutable dans l'ordre
- Exécution — dans le process appelant, par `nbclient` ; entrées-sorties vers le disque ou un stockage objet (S3, GCS, Azure)
- Coût — gratuit sous licence BSD-3-Clause

## Écosystème

### Compléments

- [[jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON. — l'appariement versionne le source, papermill l'exécute

## Ressources

- Documentation — https://papermill.readthedocs.io/
- Dépôt — https://github.com/nteract/papermill

## Voir aussi

- [[Notebooks]] — le hub du dossier
- [[Notebooks-as-code]] — la notion du dossier : papermill en porte l'exécution rejouable
