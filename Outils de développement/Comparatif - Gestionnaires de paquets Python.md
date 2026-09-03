---
role: comparatif
nom: Comparatif - Gestionnaires de paquets Python
categorie: devtools/paquet
tags: [package-manager, reproducibility]
---

# Comparatif - Gestionnaires de paquets Python

> On tranche sur : le plus petit dénominateur commun de l'écosystème, ou un outil unique qui gère aussi le lock, le venv et les versions de Python.

![[Comparatif - Gestionnaires de paquets Python.base]]

## Ce qui départage

- [[pip]] — volontairement minimal : il installe, et c'est tout — ni lockfile, ni venv, ni isolation d'outils. C'est ce qui en fait le seul présent **partout**, celui qu'un « copier-coller » de doc tierce peut supposer.
- [[uv]] — absorbe pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine dans un binaire Rust, avec `uv.lock` et l'installation des versions de Python elles-mêmes. Le lock lui est propre : une équipe mixte doit s'aligner.
