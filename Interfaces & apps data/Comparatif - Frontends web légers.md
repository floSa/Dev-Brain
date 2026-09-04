---
role: comparatif
nom: Comparatif - Frontends web légers
categorie: ui/data-app
tags: [web-framework, data-app, hypermedia]
---

# Comparatif - Frontends web légers

> On tranche sur : jusqu'où on descend — un widget Python qui fabrique la page tout seul, ou une page que l'on écrit et un serveur qui la sert.

![[Comparatif - Frontends web légers.base]]

## Ce qui départage

- [[Streamlit]] — le haut de l'échelle : un script Python linéaire, aucun HTML, et l'app existe en quelques heures parce que **tout le script se ré-exécute à chaque interaction**. Ce qui l'achète est ce qui le borne — sans `@st.cache_*` les I/O repartent à chaque clic, et la mise en page reste un flux vertical.
- [[Gradio]] — la même absence de HTML, mais autour d'une **fonction** plutôt que d'une page : arguments et retour mappés sur des composants, file d'attente et streaming intégrés pour un modèle. C'est une démo, pas une app — moins adapté qu'une vraie app data dès qu'il faut plusieurs vues, et `share=True` ne tient que quelques heures.
- [[Dash]] — le premier à demander une structure : arbre de composants et **callbacks déclarés**, donc recalcul ciblé et apps multi-pages qui tiennent dans la durée. Plus verbeux que Streamlit pour un résultat simple, et l'état se partage par `dcc.Store`, jamais par des globales — le multi-worker ne pardonne pas.
- [[FastAPI]] — on quitte l'app-en-Python : c'est un backend **API** asynchrone qui déduit validation, sérialisation et documentation OpenAPI des annotations de type. Il ne rend **aucune page**, et c'est précisément ce qui le met dans ce tableau : l'option à la main commence ici. Une route déclarée `def` plutôt qu'`async def` qui fait de l'I/O bloque l'event loop sous charge.
- [[HTMX]] — le complément exact du précédent, et non son concurrent : des attributs HTML (`hx-get`, `hx-target`, `hx-swap`) qui **remplacent un fragment de page par le HTML renvoyé par le serveur**, donc l'interactivité d'une SPA sans JavaScript ni état client. Chaque interaction est un aller-retour réseau dont la latence se ressent, et le serveur doit savoir rendre des fragments distincts des pages complètes.

## Pourquoi la vue liste ses membres nom par nom

Les cinq membres sont **codés en dur** dans le filtre de la vue, seul cas des 47 comparatifs
du vault — d'où l'avertissement `R8d`, qui dit à juste titre qu'une brique entrant dans le
thème n'entrera jamais dans le tableau.

C'est délibéré, et **mesuré** : aucun tag ne capture ces cinq-là et rien d'autre.
L'intersection de leurs tags est **vide** — [[HTMX]] ne porte que `hypermedia`, qu'aucun
autre membre n'a. Le meilleur candidat, `web-framework`, en couvre **4 sur 5** (il rate
HTMX) et fait entrer trois briques que ce comparatif ne compare pas : Flask, Uvicorn et
[[Shiny for Python]] — cette dernière appartenant à [[Comparatif - Apps data & démos ML]].
`data-app` fait pire : 2 sur 5, plus Marimo et Shiny.

La liste est donc l'expression honnête d'une comparaison **composée à la main**, qu'aucune
`categorie:` ni aucun tag ne capture. Elle se maintient à la main, et c'est le coût accepté.
