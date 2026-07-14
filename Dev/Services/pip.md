---
galaxie: dev
type: service
nom: pip
alias: []
pitch: "Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/uv|uv]]"]
remplace_par: []
status: actif
tags: [package-manager]
url_docs: https://pip.pypa.io/
url_repo: https://github.com/pypa/pip
---

# pip

## Pourquoi

Installeur de paquets **de référence** de Python, maintenu par la **PyPA** (Python Packaging Authority). Installe depuis le **PyPI** et tout index compatible. Présent par défaut dans la plupart des distributions Python : c'est le plus petit dénominateur commun de l'écosystème — si une procédure doit marcher partout, elle marche avec `pip install`. Outil volontairement minimal (installation / désinstallation de paquets) ; la gestion d'environnements, le lockfile et l'isolation d'outils sont laissés à d'autres briques (venv, pip-tools, pipx).

## Quand l'utiliser

- Environnement où l'on ne contrôle pas l'outillage (image de base, doc tierce, support universel).
- Besoin minimal : installer quelques paquets dans un venv existant.
- Compatibilité maximale : tutoriels, scripts d'install, instructions « copier-coller ».

## Quand NE PAS l'utiliser

- Projet géré de bout en bout (résolution rapide, lockfile, venv, versions de Python) → [[Dev/Services/uv|uv]].
- Besoin de vitesse en CI sur de grosses arborescences de dépendances → [[Dev/Services/uv|uv]].

## Déploiement & coût

- Inclus avec Python (ou `python -m ensurepip`). MIT, gratuit.
- Local et CI ; rien à héberger. Nouvelle version environ tous les 3 mois.

## Pièges

- Pas de lockfile natif : la reproductibilité exige `pip freeze` / pip-tools / un autre outil.
- Le résolveur (strict depuis 2020) peut être lent sur de gros graphes de dépendances.
- N'isole pas les environnements : toujours l'utiliser dans un venv pour ne pas polluer le Python système.

## Alternatives

- [[Dev/Services/uv|uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

## Liens

- [[Comparatif - Gestionnaires de paquets Python]] — pip vs uv.
- Doc : https://pip.pypa.io/
