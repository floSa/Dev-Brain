# Rules — carte

> Généré par `AI/scripts/build_carte.py`. Ne pas éditer à la main.
> 5 pages, chacune avec son chemin et une ligne.

## Au niveau du dossier
- [[Rule - Config typée]] · règle · `Rules/Rule - Config typée.md` — La configuration est typée et validée au démarrage (Pydantic Settings) ; les secrets ne sont jamais commités.
- [[Rule - Packaging démo]] · règle · `Rules/Rule - Packaging démo.md` — Une démo se lance en une commande et se comprend en un coup d'œil : environnement reproductible, commandes triviales, aperçu visuel.
- [[Rule - Qualité stricte]] · règle · `Rules/Rule - Qualité stricte.md` — La qualité est outillée et automatique : lint sélectif, typage strict, hooks avant commit, couverture mesurée.
- [[Rule - Structure de projet]] · règle · `Rules/Rule - Structure de projet.md` — Un layout standard et prévisible : code sous src/, tests sous tests/, doc sous documentation/, métadonnées dans un seul pyproject.toml.
- [[Rule - Toolchain Python]] · règle · `Rules/Rule - Toolchain Python.md` — Un seul gestionnaire d'environnement (uv) et un seul outil lint+format (Ruff) sur tout projet Python — pas d'empilement pip + venv + flake8 + isort + black.
