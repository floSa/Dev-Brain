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
complements: ["[[HTMX]]"]
tags: [templating]
url_docs: https://jinja.palletsprojects.com/
url_repo: https://github.com/pallets/jinja
---

# Jinja2

<!-- AUTO:BANDEAU:START -->
> Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de gabarits Python de référence : un fichier texte — typiquement du HTML — mêle du
balisage statique et des emplacements `{{ ... }}` et `{% ... %}` remplis à partir de données.
Il apporte l'**héritage de gabarits** (`extends` / `block`), les inclusions, les macros, les
filtres, et un **échappement automatique** du HTML qui ferme la porte au XSS par défaut. La
syntaxe des expressions est proche de Python sans l'être : le gabarit n'est pas censé porter de
logique. Développé par l'organisation Pallets, il sert bien au-delà du web — génération de
fichiers de configuration, d'e-mails, de manifestes, et c'est le moteur d'Ansible.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rendre du HTML côté serveur, en pages complètes ou en fragments | Compiler un gabarit venant d'une **entrée externe** ouvre une injection côté serveur (SSTI) — à ne jamais faire |
| Générer n'importe quel fichier texte paramétré : configuration, e-mails, manifestes, code | L'échappement automatique dépend du contexte : actif pour les extensions HTML, à vérifier ailleurs, et `\| safe` le désactive |
| Vouloir l'héritage de gabarits sans mettre de logique applicative dedans | Logique métier lourde : les gabarits doivent rester de la présentation, sinon ils deviennent illisibles |
| | Front à fort état client : le rendu se fait alors côté navigateur, hors de portée d'un moteur serveur |

## Mise en œuvre

- Installation — `uv add jinja2`
- Point d'entrée — import Python, `from jinja2 import Environment` ; Flask l'expose déjà configuré, FastAPI par `Jinja2Templates`
- Prérequis — aucune dépendance lourde ; le moteur est pur Python
- Exécution — dans le processus de l'application, rien à héberger à part
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

<!-- Aucune : les autres moteurs de gabarits (Mako, Chameleon, gabarits Django) ne sont pas fichés dans le brain. -->

### Compléments

- [[HTMX]] — Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd. — consomme les fragments que Jinja2 rend ; c'est la paire usuelle côté Python

## Ressources

- Documentation — https://jinja.palletsprojects.com/
- Dépôt — https://github.com/pallets/jinja

## Voir aussi

- [[Web & API]] — le hub du domaine
- [[Flask]] — l'embarque comme moteur de gabarits par défaut
- [[FastAPI]] — rendu HTML optionnel, par `Jinja2Templates`
