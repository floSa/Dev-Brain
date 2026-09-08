---
role: brique
nom: uv
alias: []
pitch: "Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine."
categorie: devtools/paquet
famille: cli
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[pip]]"]
complements: []
tags: [package-manager]
url_docs: https://docs.astral.sh/uv/
url_repo: https://github.com/astral-sh/uv
---

# uv

<!-- AUTO:BANDEAU:START -->
> Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Gestionnaire de paquets et de projets Python écrit par Astral, les auteurs de [[Ruff]]. Un
résolveur natif et un cache global partagé entre projets rendent l'installation dix à cent
fois plus rapide que pip. Surtout, c'est un outil **unique** : il absorbe les rôles de pip,
pip-tools, pipx, poetry, pyenv, virtualenv et twine — projet décrit dans `pyproject.toml`,
dépendances figées dans `uv.lock`, environnements virtuels créés sans qu'on les demande,
outils en ligne de commande isolés, et jusqu'aux versions de Python elles-mêmes, qu'il
télécharge et installe.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Nouveau projet Python : `uv init`, `uv add`, `uv run` — venv et `uv.lock` gérés sans y penser | `uv.lock` lui est propre : une équipe mixte doit s'aligner sur l'outil |
| Remplacer un empilement pip + virtualenv + pyenv + pipx par un binaire unique | Écosystème jeune et en évolution rapide : épingler la version sur les projets longs |
| CI : installation quasi instantanée, build reproductible par le lockfile | `uv pip …` imite l'interface de pip sans lire toute la configuration pip existante |
| Script autonome à dépendances déclarées en tête (PEP 723), lancé par `uv run script.py` | Paquets binaires propres à conda, pour l'écosystème scientifique qui n'existe pas en wheel |

## Mise en œuvre

- Installation — binaire unique par script d'installation, ou via pip et pipx ; ni Rust ni Python préalable
- Point d'entrée — ligne de commande : `uv init`, `uv add`, `uv run`, `uv tool`, `uv python`
- Prérequis — aucun : uv installe lui-même les versions de Python dont il a besoin
- Exécution — sur le poste et en CI ; cache global sur disque, partagé entre projets
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.

## Ressources

- Documentation — https://docs.astral.sh/uv/
- Dépôt — https://github.com/astral-sh/uv

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Gestionnaires de paquets Python]] — ce qui départage les gestionnaires du dossier
