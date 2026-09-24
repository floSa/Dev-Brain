---
role: notion
nom: Typage statique en Python
alias: [Typage statique, typage graduel, gradual typing, type hints, annotations de type, static typing, type checking Python]
categorie: devtools/qualite
domaines: [data-sci, data-eng, ml-eng, ai-eng, mlops]
tags: [type-checker, type-hints]
---

# Typage statique en Python

## Aperçu

- Annoter le code avec des types (`def f(x: int) -> str`) et laisser un **vérificateur** ([[mypy]], [[Pyright]]) lire ces annotations **sans exécuter le programme** pour signaler les incohérences. C'est du typage *graduel* : on annote ce qu'on veut, le reste n'est pas vérifié.
- Le gain est un défaut attrapé avant l'exécution, dans l'éditeur et en CI, et une documentation qui ne dérive pas. La limite est nette : **l'interpréteur n'applique aucune annotation** (la documentation de `typing` l'écrit tel quel). Une valeur de mauvais type entre à l'exécution sans erreur si aucune validation ne la contrôle.

## Concepts clés

### Typage graduel et `Any`
- `Any` est compatible avec tous les types, dans les deux sens ; une expression de type `Any` n'est **pas vérifiée du tout** (PEP 484, doc de `typing`). `object` est l'inverse : presque aucune opération n'y est permise. La règle de la documentation : `object` pour « n'importe quel type, en sûreté », `Any` pour « typé dynamiquement ».
- Un `Any` se propage : un import sans types, un `# type: ignore` ou une bibliothèque non typée rendent `Any` tout ce qui en découle. Dropbox le note sur ses 4 millions de lignes : les imports hors du build donnent des valeurs « non vérifiées du tout ».

### Annotations et validation à l'exécution
- Deux couches différentes. Le vérificateur statique lit les annotations et ne les applique jamais ; la **validation à l'exécution** les applique sur des données qui entrent. [[Pydantic]] le dit pour sa part : il garantit les types et contraintes de la **sortie**, pas ceux de l'entrée. Le détail de la validation est dans sa fiche, pas ici.
- Le pont entre les deux est `dataclass_transform` (PEP 681) : une bibliothèque déclare que sa classe se comporte comme une dataclass, et un vérificateur comprend les modèles sans plugin — c'est ainsi que [[Pyright]] lit Pydantic, quand [[mypy]] passe par son plugin `pydantic.mypy`.

### `Protocol` : le sous-typage structurel
- Un objet est accepté s'il a les bons membres, sans hériter de rien (PEP 544) — le « duck typing » rendu vérifiable. Un `Protocol` convient aux frontières (un objet qui sait `.predict`, un stockage qui sait `.read`) sans imposer une classe de base.
- `@runtime_checkable` ne contrôle que la **présence** des méthodes à l'exécution, pas leurs signatures ni leurs types. Un `isinstance` sur un protocole n'est donc pas une preuve de conformité.

### `TypedDict` : des dictionnaires à clés connues
- Décrit la forme d'un dictionnaire (typiquement un JSON déjà chargé) : clés, types, `Required` / `NotRequired` (PEP 655), `ReadOnly` (PEP 705, Python 3.13). Les PEP précisent que **tout est vérifié statiquement seulement** : rien ne contrôle le dictionnaire reçu.
- `closed=True` et `extra_items` (PEP 728) sont finals pour Python 3.15 et disponibles par `typing_extensions` 4.13.0 ou plus ; le support de chaque vérificateur est à vérifier avant de s'en servir (le PEP cite Pyright parmi les implémentations ; le support de mypy n'a pas été vérifié pour cette fiche).

### Génériques
- La syntaxe moderne (PEP 695, Python 3.12) écrit `def premier[T](xs: list[T]) -> T` et `class Boite[T]` sans déclarer de `TypeVar` ; les valeurs par défaut de paramètres de type viennent en 3.13 (PEP 696). `ParamSpec` conserve la signature d'un décorateur, `Self` type les méthodes qui renvoient leur instance, `@override` (3.12) fait échouer une méthode qui ne redéfinit plus rien.
- `TypeIs` (PEP 742, 3.13) réduit le type dans les **deux** branches d'une fonction de garde, là où `TypeGuard` ne le fait que dans la vraie : à préférer pour les cas courants.

### Évaluation des annotations
- Depuis Python 3.14 (PEP 649 et 749), les annotations ne sont plus évaluées à la définition mais à la demande : plus besoin de guillemets pour une référence en avant, et `from __future__ import annotations` (PEP 563, supplanté) devient inutile quand seules les versions 3.14 ou plus sont visées. Les bibliothèques qui lisent les annotations à l'exécution peuvent devoir s'adapter. La date de retrait de l'import `__future__` n'est pas fixée.

### Stubs et `py.typed`
- Une bibliothèque se dit typée par un fichier `py.typed` (PEP 561) ; sinon ses types vivent dans des paquets de **stubs** : `foo-stubs`, ou les paquets `types-*` du dépôt typeshed, versionnés sur la bibliothèque stubbée. Sans l'un ni l'autre, [[mypy]] traite le module comme `Any` et ne devine rien.
- Un stub peut décrocher de la bibliothèque : il faut les installer d'avance sur une machine sans réseau.

### Mode strict
- Un vérificateur propose un mode qui exige les annotations et interdit les `Any` implicites. À activer module par module, pas d'un coup : les options exactes sont dans les fiches [[mypy]] (`--strict`) et [[Pyright]] (`typeCheckingMode`).

## En pratique

### Adopter progressivement
- Ce que la documentation de mypy recommande : partir d'un sous-ensemble (5 000 à 50 000 lignes) et faire passer le vérificateur **avant** d'annoter ; l'installer en CI tôt, avec la version épinglée ; configurer **par module** ; ne pas activer `ignore_missing_imports` globalement (il cache des erreurs) ; annoter d'abord les modules les plus importés et tout code nouveau ; durcir ensuite module par module.
- Maîtriser la dette de `# type: ignore` : `warn_unused_ignores` signale ceux devenus inutiles, `ignore-without-code` impose un code d'erreur pour ne pas masquer un autre problème sur la même ligne.
- Un fichier de **référence** (*baseline*) évite de tout corriger d'un coup : basedpyright (`--writebaseline`) et Pyrefly (`--baseline`, `pyrefly suppress`) enregistrent les erreurs existantes pour ne signaler que le code nouveau.

### Dans un code data et ML
- **[[numpy]]** : livré avec `py.typed`. `NDArray` fixe le dtype mais pas la forme (seul le nombre de dimensions s'exprime) ; son plugin mypy est déprécié depuis NumPy 2.3.
- **[[pandas]]** : n'est pas `py.typed` (sa documentation de contribution le dit, et la roue 3.0.6 ne contient pas le marqueur), sans être sans annotations. Les types viennent de `pandas-stubs` (BSD-3, 3.0.5.260914 du 2026-09-14, équipe pandas), qui couvre « les cas d'usage typiques » de l'API publique.
- **[[PyTorch]]** : `torch.Tensor` est une classe non générique dans le code source : ni forme ni dtype dans le type. Pour les exprimer, `jaxtyping` (MIT, 0.3.11) ajoute `Float[Tensor, "batch channels"]`, vérifié **à l'exécution** par beartype ou typeguard ; pour un vérificateur statique, c'est un tableau tout court.
- **[[Polars]]** : le dépôt livre `py.typed` (non vérifié dans la roue).
- Règle de prudence : annoter les **frontières** (fonctions publiques, entrées et sorties de pipeline, configuration) avant l'intérieur des calculs vectorisés, où le type ne dit rien de la forme.

### Quand un vérificateur ralentit plus qu'il n'aide
- Le guide officiel de typing.python.org dresse la liste : un coût d'annotation parfois prohibitif sur un gros code existant, un framework très dynamique où le gain est faible, des `Protocol` ou des `Any` partout quand tout comportement observable est utilisé, un vérificateur lent ou mal intégré, et une couverture de tests qui peut suffire.
- Le temps de CI compte : Dropbox rapportait plus de 15 minutes pour un build propre de mypy avant sa compilation par mypyc, et le daemon ramenait la plupart des relances à quelques secondes ; Dagster annonce être passé d'environ 15 minutes (Pyright) à une à deux minutes avec ty, au prix d'environ 4 500 diagnostics à traiter. Chiffres des éditeurs eux-mêmes, non reproduits.
- La suite de conformité de la spécification vérifie qu'un outil suit la spécification ; elle n'est **pas** un classement, et ses auteurs déconseillent de s'en servir comme critère principal de choix.

## Approches voisines & alternatives

- [[mypy]] et [[Pyright]] — les deux vérificateurs fichés ; [[Comparatif - Vérificateurs de types Python]] les départage, et cite Pyrefly et ty sans fiche.
- [[Ruff]] — lint et format, **aucune** vérification de types : les deux contrôles ne se remplacent pas.
- [[pytest]] et [[Hypothesis]] — les tests exécutent le code, ce que le typage statique ne fait jamais ; un test par propriétés couvre ce qu'une annotation ne dit pas.
- [[pre-commit]] — rejouer le vérificateur avant chaque commit.
- [[Pydantic]] — la validation à l'exécution, couche complémentaire du typage statique.

## Pour aller plus loin

- Spécification du système de types — https://typing.python.org/en/latest/spec/ ; guide « Reasons to avoid static type checking » — https://typing.python.org/en/latest/guides/typing_anti_pitch.html
- PEP 483 et 484 (typage graduel) — https://peps.python.org/pep-0484/ ; PEP 544 (Protocol), PEP 561 (distribution des types), PEP 681 (`dataclass_transform`), PEP 695 (syntaxe des génériques), PEP 728 (`closed`), PEP 749 (annotations différées)
- Adopter dans du code existant — https://mypy.readthedocs.io/en/stable/existing_code.html
- Dropbox, « Our journey to type checking 4 million lines of Python » — https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python
- NumPy — https://numpy.org/doc/stable/reference/typing.html ; pandas-stubs — https://github.com/pandas-dev/pandas-stubs ; jaxtyping — https://github.com/patrick-kidger/jaxtyping
