---
role: brique
nom: pip
alias: []
pitch: "Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout."
categorie: devtools/paquet
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[uv]]"]
complements: []
tags: [package-manager]
url_docs: https://pip.pypa.io/
url_repo: https://github.com/pypa/pip
---

# pip

<!-- AUTO:BANDEAU:START -->
> Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Installeur de paquets de référence de Python, maintenu par la **PyPA**. Il installe depuis
le PyPI et tout index compatible, et son périmètre s'arrête là : ni environnements
virtuels, ni lockfile, ni isolation d'outils en ligne de commande — ces rôles sont laissés
à `venv`, à pip-tools, à pipx. Ce minimalisme est ce qui en fait le plus petit dénominateur
commun de l'écosystème : il est livré avec la plupart des distributions Python, donc une
procédure écrite avec `pip install` marche partout, y compris là où l'outillage n'est pas
le nôtre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Environnement dont on ne choisit pas l'outillage : image de base, doc tierce, support universel | Aucun lockfile natif : la reproductibilité passe par `pip freeze`, pip-tools ou un autre outil |
| Besoin minimal : installer quelques paquets dans un venv déjà en place | Résolveur strict depuis 2020, mais lent sur de gros graphes de dépendances |
| Compatibilité maximale : tutoriels, scripts d'installation, instructions « copier-coller » | N'isole rien de lui-même : hors d'un venv, il installe dans le Python système |

## Mise en œuvre

- Installation — livré avec Python, ou `python -m ensurepip`
- Point d'entrée — ligne de commande : `pip install`, `pip uninstall`, `pip freeze`
- Prérequis — un interpréteur Python, et un venv pour ne pas toucher au Python système
- Exécution — sur le poste et en CI ; rien à héberger
- Coût — gratuit sous licence MIT ; une nouvelle version environ tous les trois mois

## Écosystème

### Alternatives

- [[uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

## Ressources

- Documentation — https://pip.pypa.io/
- Dépôt — https://github.com/pypa/pip

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Gestionnaires de paquets Python]] — ce qui départage les gestionnaires du dossier
