---
galaxie: dev
type: service
nom: pytest
alias: [py.test]
pitch: "Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins."
categorie: tooling/test
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [testing]
url_docs: https://docs.pytest.org/
url_repo: https://github.com/pytest-dev/pytest
---

# pytest

## Pourquoi

Framework de tests **de facto** en Python. Sa marque : on écrit des `assert` Python ordinaires et pytest fournit une **introspection détaillée** en cas d'échec (il décompose l'expression). Le système de **fixtures** (injection de dépendances par paramètre, portées function/module/session) remplace le setup/teardown rigide d'`unittest`. Paramétrage des tests, marqueurs, et un **écosystème de plugins** très riche (couverture, parallélisme, mock, asyncio, conteneurs).

## Quand l'utiliser

- Tests unitaires et fonctionnels de tout projet Python.
- Besoin de fixtures réutilisables et composables (bases jetables, clients HTTP, données).
- Paramétrer un même test sur de nombreux cas (`@pytest.mark.parametrize`).
- S'appuyer sur des plugins : `pytest-cov` (couverture), `pytest-xdist` (parallélisme), `pytest-asyncio`, etc.

## Quand NE PAS l'utiliser

- Contrainte de rester sur la bibliothèque standard sans dépendance externe → `unittest`.
- Tests d'un autre langage : pytest est spécifique à Python.

## Déploiement & coût

- Bibliothèque de développement (`uv add --dev pytest`). MIT, gratuit.
- Local et CI ; rien à héberger. S'intègre à tout runner CI.

## Pièges

- La magie des fixtures peut devenir opaque : nommer et documenter les fixtures partagées (`conftest.py`).
- Portée de fixture mal choisie → état partagé entre tests, échecs intermittents.
- Découverte automatique : respecter les conventions de nommage (`test_*.py`, `test_*`) sinon les tests sont ignorés silencieusement.

## Alternatives

- `unittest` (bibliothèque standard), nose2 — pytest reste le standard de l'écosystème ; il exécute d'ailleurs les tests `unittest` existants. *(Pages dédiées non créées.)*

## Liens

- Conteneurs jetables pour tests d'intégration : [[Dev/Services/testcontainers|testcontainers]].
- Doc : https://docs.pytest.org/
