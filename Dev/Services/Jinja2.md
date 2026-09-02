---
role: brique
nom: Jinja2
alias: [jinja, jinja2]
pitch: "Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask."
categorie: web/frontend
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [templating]
url_docs: https://jinja.palletsprojects.com/
url_repo: https://github.com/pallets/jinja
---

# Jinja2

## Pourquoi

Moteur de templates Python de référence : des gabarits texte (typiquement HTML) mêlent du balisage statique et des emplacements `{{ ... }}` / `{% ... %}` remplis à partir de données. Apporte l'**héritage de templates** (`extends` / `block`), les inclusions, macros, filtres, et un **échappement automatique** du HTML (protection XSS). Syntaxe d'expressions proche de Python. Développé par l'organisation Pallets ; c'est le moteur de templates de [[Flask]], et il sert au-delà du web (génération de config, e-mails, fichiers, Ansible).

## Quand l'utiliser

- Rendu HTML côté serveur d'une app [[Flask]] / [[FastAPI]] (pages complètes ou fragments pour [[HTMX]]).
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

## Alternatives

<!-- Pas d'alternative dans le brain : autres moteurs de templates (Mako, Chameleon, Django templates) non documentés. -->

## Liens

- [[Flask]] — embarque Jinja2 comme moteur de templates par défaut
- [[FastAPI]] — rendu HTML optionnel via Jinja2Templates
- [[HTMX]] — consomme les fragments HTML rendus par Jinja2 (paire usuelle)
- Doc : https://jinja.palletsprojects.com/
