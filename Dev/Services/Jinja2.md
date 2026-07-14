---
galaxie: dev
type: service
nom: Jinja2
alias: [jinja, jinja2]
pitch: "Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask."
categorie: framework/frontend
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [templating]
url_docs: https://jinja.palletsprojects.com/
url_repo: https://github.com/pallets/jinja
---

# Jinja2

## Pourquoi

Moteur de templates Python de référence : des gabarits texte (typiquement HTML) mêlent du balisage statique et des emplacements `{{ ... }}` / `{% ... %}` remplis à partir de données. Apporte l'**héritage de templates** (`extends` / `block`), les inclusions, macros, filtres, et un **échappement automatique** du HTML (protection XSS). Syntaxe d'expressions proche de Python. Développé par l'organisation Pallets ; c'est le moteur de templates de [[Dev/Services/Flask|Flask]], et il sert au-delà du web (génération de config, e-mails, fichiers, Ansible).

## Quand l'utiliser

- Rendu HTML côté serveur d'une app [[Dev/Services/Flask|Flask]] / [[Dev/Services/FastAPI|FastAPI]] (pages complètes ou fragments pour [[Dev/Services/HTMX|HTMX]]).
- Génération de tout fichier texte paramétré : fichiers de configuration, e-mails, manifestes, code.
- Besoin d'héritage de gabarits et d'échappement automatique sans logique applicative dans les templates.

## Quand NE PAS l'utiliser

- Logique métier lourde : les templates doivent rester de la **présentation**, pas de la logique (la déporter dans le code Python).
- Front à fort état client → rendu côté client (frameworks SPA hors brain).

## Déploiement & coût

- Bibliothèque open-source (BSD-3-Clause), gratuite, intégrée à l'application Python. Aucune dépendance lourde.
- Pas de service à héberger : single-node, suit le déploiement de l'app. Version courante : 3.1.x.

## Pièges

- L'échappement automatique dépend du contexte : actif pour les extensions HTML, à vérifier pour les autres formats ; `| safe` désactive la protection XSS — à manier avec prudence.
- Tentation de mettre trop de logique dans les templates (boucles, conditions imbriquées) → gabarits illisibles.
- Le rendu de templates non fiables (saisis par l'utilisateur) ouvre une surface d'injection (SSTI) — ne jamais compiler de template venant d'une entrée externe.
- Retours d'expérience détaillés : `Dev/REX/REX - Jinja2.md`.

## Alternatives

<!-- Pas d'alternative dans le brain : autres moteurs de templates (Mako, Chameleon, Django templates) non documentés. -->

## Liens

- [[Dev/Services/Flask|Flask]] — embarque Jinja2 comme moteur de templates par défaut
- [[Dev/Services/FastAPI|FastAPI]] — rendu HTML optionnel via Jinja2Templates
- [[Dev/Services/HTMX|HTMX]] — consomme les fragments HTML rendus par Jinja2 (paire usuelle)
- Doc : https://jinja.palletsprojects.com/
