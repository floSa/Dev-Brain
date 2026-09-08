---
role: brique
nom: altair
alias: [vega-altair, alt]
pitch: "Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[plotly]]", "[[bokeh]]"]
complements: []
tags: [dataviz, declarative-viz, interactive-viz]
url_docs: https://altair-viz.github.io/
url_repo: https://github.com/vega/altair
---

# altair

<!-- AUTO:BANDEAU:START -->
> Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-23 |
<!-- AUTO:BANDEAU:END -->

## Définition

Visualisation **déclarative** : au lieu de tracer pas à pas, on décrit le graphe — quelle
colonne va sur quel encodage (`x`, `y`, `color`, `size`), quelle marque (`mark_bar`,
`mark_line`, `mark_point`). La sortie est une spécification **Vega-Lite** en JSON, rendue de
façon interactive dans le navigateur et réutilisable hors de Python. La grammaire des
graphiques rend le code concis et composable : superposition, facettes et sélections liées
s'expriment par opérateurs. Deux contreparties viennent de ce que la bibliothèque n'est
qu'un générateur de spécification : la personnalisation très fine reste bornée par ce que
Vega-Lite expose, et le rendu dépend de la version du moteur embarqué, à épingler pour la
reproductibilité.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Raisonner en **encodages** — grammaire des graphiques — plutôt qu'en primitives de dessin | Limite par défaut à **5000 lignes** (`MaxRowsError`) : au-delà, il faut agréger ou passer par `alt.data_transformers` |
| Graphes composés déclaratifs : superposition, facettes, sélections interactives liées | Le paradigme déclaratif déroute quand on attend une API impérative |
| Exporter la **spec Vega-Lite** pour la réutiliser ailleurs qu'en Python | La personnalisation très fine est contrainte par ce que Vega-Lite expose, pas par le code Python |
| Code de visualisation lisible et concis à maintenir | Le rendu dépend de la version du moteur Vega-Lite embarqué — à épingler pour reproduire une figure |

## Mise en œuvre

- Installation — `uv add altair`
- Point d'entrée — import Python, `import altair as alt` ; entrée naturelle, un DataFrame
- Prérequis — Python côté génération ; le rendu est délégué à Vega-Lite dans un navigateur
- Exécution — dans le process appelant, mono-nœud ; aucun serveur à tenir, la spec JSON est portable
- Coût — gratuit, licence BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.

## Ressources

- Documentation — https://altair-viz.github.io/
- Dépôt — https://github.com/vega/altair

## Voir aussi

- [[Visualisation]] — le hub du dossier
- [[pandas]] — la source de données attendue en entrée
- [[Comparatif - Visualisation]] — ce qui départage les bibliothèques du dossier
