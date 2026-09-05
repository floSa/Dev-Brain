---
role: brique
nom: pytest
alias: [py.test]
pitch: "Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins."
categorie: devtools/test
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[testcontainers]]"]
tags: [testing]
url_docs: https://docs.pytest.org/
url_repo: https://github.com/pytest-dev/pytest
---

# pytest

<!-- AUTO:BANDEAU:START -->
> Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de tests de facto en Python. Sa marque : on écrit des `assert` ordinaires, et en
cas d'échec pytest **décompose l'expression** pour montrer les valeurs intermédiaires — pas
d'API d'assertions à apprendre. Le système de **fixtures** — injection par nom de paramètre,
portées function, module ou session — remplace le setup/teardown rigide d'`unittest`. S'y
ajoutent le paramétrage d'un même test sur N cas, les marqueurs, et un écosystème de plugins
très fourni : `pytest-cov` pour la couverture, `pytest-xdist` pour le parallélisme,
`pytest-asyncio`. La découverte des tests est automatique et repose entièrement sur des
conventions de nommage.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tests unitaires et fonctionnels de tout projet Python | Contrainte de rester sur la bibliothèque standard, sans dépendance externe → `unittest` |
| Fixtures réutilisables et composables : bases jetables, clients HTTP, jeux de données | Tests d'un autre langage : pytest est spécifique à Python |
| Paramétrer un même test sur de nombreux cas (`@pytest.mark.parametrize`) | La découverte est silencieuse : un fichier ou une fonction hors convention (`test_*.py`, `test_*`) n'est jamais exécuté, sans avertissement |
| S'appuyer sur les plugins : couverture, parallélisme, asyncio | Une portée de fixture mal choisie partage de l'état entre tests et produit des échecs intermittents — la magie devient opaque si `conftest.py` n'est pas documenté |

## Mise en œuvre

- Installation — `uv add --dev pytest`
- Point d'entrée — commande `pytest` ; les tests sont des fonctions `test_*` dans des fichiers `test_*.py`
- Prérequis — Python ; les fixtures partagées vivent dans un `conftest.py`
- Exécution — sur le poste et en CI ; s'intègre à tout runner
- Coût — gratuit sous licence MIT

## Écosystème

### Compléments

- [[testcontainers]] — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement. — les conteneurs s'exposent en fixtures pour les tests d'intégration

## Ressources

- Documentation — https://docs.pytest.org/
- Dépôt — https://github.com/pytest-dev/pytest

## Voir aussi

- [[Outils de développement]] — le hub du domaine
