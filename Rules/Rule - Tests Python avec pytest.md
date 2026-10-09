---
role: rule
domaine: tests
applicable: global
strictness: must
tags: [rule, testing, property-based-testing, ci-cd]
---

# Rule — Tests Python avec pytest

## Principe

Un projet Python se teste avec pytest, à deux niveaux : l'essentiel (une commande, un test de bout en bout, un test par bogue corrigé) et le strict (CI, seuil de couverture, propriétés, dépendances réelles).

Le niveau essentiel vaut pour tout projet. Le niveau strict s'ajoute dès que le projet est livré à quelqu'un d'autre ou qu'un agent de code y écrit : c'est alors la suite de tests, et non la relecture, qui dit que le travail est terminé.

## MUST

- Tester avec `pytest`, lancé par une seule commande documentée (`uv run pytest`).
- Ranger les tests dans `tests/`, un fichier `test_*.py` par module testé.
- Écrire au moins un test de bout en bout : il appelle le vrai point d'entrée (CLI, API ou pipeline) sur une petite donnée d'exemple versionnée.
- Écrire d'abord un test qui échoue pour chaque bogue corrigé, puis le corriger.
- Faire passer toute la suite avant de committer et avant de rendre la main.

## SHOULD

- Niveau strict : rejouer la suite en CI à chaque push, par la même commande que sur le poste ([[Rule - Qualité stricte]] pour les hooks et le seuil de couverture).
- Niveau strict : fixer un seuil de couverture avec pytest-cov (`--cov-fail-under`), et mesurer aussi les branches (`--cov-branch`). Le seuil mesure ce qui est exécuté, pas ce qui est juste.
- Énoncer des propriétés avec [[Hypothesis]] pour le parsing, les transformations de données et les fonctions numériques : la bibliothèque génère les cas que personne n'a imaginés.
- Tester contre une vraie base ou un vrai broker lancé à la demande ([[testcontainers]]) plutôt que contre un faux écrit à la main.
- Marquer les tests lents (`@pytest.mark.slow`, marqueur déclaré dans `pyproject.toml`) pour les exclure de la boucle rapide, mais les garder en CI.
- Projet de ML : fixer les graines aléatoires et garder un test de fumée sur un tout petit jeu de données (le pipeline tourne, la métrique dépasse un plancher large).

## NICE-TO-HAVE

- Monter le seuil de couverture par paliers plutôt que d'imposer d'emblée un chiffre irréaliste.
- Un test de non-régression de modèle : la métrique sur un jeu fixe ne baisse pas de plus d'une marge écrite.
- Une suite rapide (moins d'une minute) pour que personne ne la saute.

## Pour AGENTS.md

- Tester : `uv run pytest`. Toute la suite passe avant de rendre la main.
- Un bogue corrigé reçoit d'abord un test qui échoue.
- Ne jamais modifier ni supprimer un test rouge pour le faire passer sans le dire.
- Au moins un test de bout en bout : il appelle le point d'entrée réel.

## Exemples

### Bon

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --cov=mon_projet --cov-branch --cov-fail-under=70"
```

```python
def test_bout_en_bout(tmp_path):
    sortie = tmp_path / "rapport.json"
    r = subprocess.run(
        ["mon-projet", "run", "tests/data/exemple.csv", "--out", str(sortie)],
        check=False,
    )
    assert r.returncode == 0
    assert sortie.exists()
```

### Mauvais

```python
def test_ok():
    assert True          # ne touche aucun code du projet

# tests écrits par l'agent après son code, qui recopient ce que le code fait
# au lieu de ce que la spécification demande
```

## Exceptions

- Script unique et jetable : un test de fumée suffit, ou aucun.
- Exploration en notebook : les tests s'écrivent quand le code sort du notebook vers `src/`.
- Code qui dépend d'un matériel absent de la CI (GPU, automate, capteur) : isoler cette partie derrière une interface testable et marquer le reste du test pour la machine qui l'a.

## Voir aussi

- [[pytest]], [[Hypothesis]], [[testcontainers]] — les trois niveaux d'outils
- [[Rule - Qualité stricte]] — hooks avant commit et seuil de couverture
- [[Rule - Structure de projet]] — `tests/` miroir de `src/`
- [[Rule - Projet assisté par agent]] — pourquoi les tests ne doivent pas venir du code qu'ils jugent
- [[Revue, tests et définition de terminé avec un agent]] — la définition de terminé et le piège de l'agent qui teste son propre code
