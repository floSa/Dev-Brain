---
galaxie: dev
type: service
nom: uv
alias: []
pitch: "Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/pip|pip]]"]
remplace_par: []
status: actif
tags: [package-manager]
url_docs: https://docs.astral.sh/uv/
url_repo: https://github.com/astral-sh/uv
---

# uv

## Pourquoi

Gestionnaire de paquets et de projets Python **écrit en Rust** par Astral (les auteurs de [[Dev/Services/Ruff|Ruff]]). Résolution et installation de dépendances **10–100× plus rapides** que pip, grâce à un résolveur natif et un cache global partagé entre projets. Outil unique qui absorbe le rôle de **pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine** : gestion de projet (`pyproject.toml` + `uv.lock`), environnements virtuels, installation d'outils CLI isolés, et installation des versions de Python elles-mêmes.

## Quand l'utiliser

- Tout nouveau projet Python : `uv init`, `uv add`, `uv run` — lockfile reproductible et venv géré automatiquement.
- Remplacer un empilement pip + virtualenv + pyenv + pipx par un seul binaire.
- CI : installation de dépendances quasi instantanée, builds reproductibles via `uv.lock`.
- Scripts autonomes avec dépendances inline (`uv run script.py`, PEP 723).

## Quand NE PAS l'utiliser

- Environnement verrouillé sur l'outillage historique, sans marge de changement → [[Dev/Services/pip|pip]].
- Besoin de fonctions binaires propres à conda pour l'écosystème scientifique non-wheel.

## Déploiement & coût

- Binaire unique, installable sans Rust ni Python préalable (script `curl`, ou via pip/pipx). MIT, gratuit.
- Local et CI ; rien à héberger. Cache global sur disque, partagé entre projets.

## Pièges

- Écosystème jeune et en évolution rapide : épingler la version d'uv sur les projets longs.
- `uv.lock` est propre à uv ; une équipe mixte doit s'aligner sur l'outil.
- `uv pip ...` imite l'interface pip mais ne lit pas toute la configuration pip existante.

## Alternatives

- [[Dev/Services/pip|pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.

## Liens

- [[Comparatif - Gestionnaires de paquets Python]] — uv vs pip.
- Même éditeur (Astral) : [[Dev/Services/Ruff|Ruff]].
- Doc : https://docs.astral.sh/uv/
