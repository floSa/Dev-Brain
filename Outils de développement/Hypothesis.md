---
role: brique
nom: Hypothesis
alias: []
pitch: "Test par propriétés pour Python : on décrit les entrées valides, la bibliothèque en génère des centaines, cherche un contre-exemple et le réduit au plus petit cas qui échoue."
categorie: devtools/test
famille: paquet
licence_type: open-source
maturite: production
langage: Python / Rust
alternatives: []
complements: ["[[pytest]]", "[[numpy]]", "[[pandas]]"]
tags: [testing, property-based-testing]
url_docs: https://hypothesis.readthedocs.io/
url_repo: https://github.com/HypothesisWorks/hypothesis
---

# Hypothesis

<!-- AUTO:BANDEAU:START -->
> Test par propriétés pour Python : on décrit les entrées valides, la bibliothèque en génère des centaines, cherche un contre-exemple et le réduit au plus petit cas qui échoue.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python / Rust | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de **test par propriétés**. Au lieu d'écrire trois exemples à la main, le test
énonce une propriété (« trier deux fois donne le même résultat », « encoder puis décoder
rend l'entrée ») et déclare par des *stratégies* l'espace des entrées valides ; Hypothesis
génère des cas, cherche un contre-exemple, puis le **réduit** (shrinking) jusqu'au plus
petit cas qui échoue. Les échecs trouvés sont gardés dans une base locale `.hypothesis/` et
rejoués d'une exécution à l'autre. Le plugin pytest est livré dans le paquet : un `@given`
se pose sur une fonction de test ordinaire. Version 6.168.3 du 2026-09-28, 9 032 étoiles le
2026-10-01 ; licence **MPL-2.0**, un copyleft par fichier sans effet pour qui l'utilise sans
modifier ses sources.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Fonction de calcul à invariants nets : idempotence, aller-retour, commutativité, équivalence avec une implémentation de référence | La propriété ne se formule pas : un test par exemples, écrit avec [[pytest]], reste plus honnête qu'une propriété creuse |
| Code numérique : `hypothesis.extra.numpy` génère tableaux, formes et formes compatibles en diffusion, `hypothesis.extra.pandas` des DataFrames | Les flottants : NaN, ±inf et sous-normaux sont générés par défaut, il faut borner (`allow_nan=False`, bornes) ou comparer avec une tolérance |
| Analyseur, sérialiseur ou convertisseur dont les entrées réelles sont trop variées pour être listées | Entrées structurées avec contraintes fines (modèles [[Pydantic]]) : `st.from_type` ne respecte qu'une partie des contraintes `annotated-types` et ignore les autres avec un avertissement, le modèle rejette alors la valeur à la validation |
| Retrouver en CI un contre-exemple minimal et reproductible plutôt qu'un échec intermittent | Installation hors ligne sans miroir de roues : depuis 6.156.1 le paquet embarque une extension native Rust, la roue de la plateforme est nécessaire (ou une chaîne Rust pour la source) |

## Mise en œuvre

- Installation — `uv add --dev hypothesis` ; extras optionnels `hypothesis[numpy]`, `hypothesis[pandas]`
- Point d'entrée — décorateur `@given(...)` sur un test pytest, avec des stratégies (`st.integers()`, `st.lists()`, `st.builds(...)`, `st.from_type(...)`)
- Prérequis — Python 3.10 ou plus ; seule dépendance d'exécution, `sortedcontainers` ; roues natives par plateforme depuis 6.156.1, dernière version en Python pur 6.155.7
- Exécution — sur le poste et en CI, sans réseau ; le profil `ci` s'active seul dans les CI connues (`derandomize=True`, `deadline=None`, base d'exemples désactivée)
- Coût — gratuit sous licence MPL-2.0 ; une release presque quotidienne (132 sur les 12 derniers mois), épingler la version dans le verrou

## Écosystème

### Alternatives

- *Aucune alternative fichée dans le brain. Voisins non fichés : Schemathesis (MIT, tests d'API générés depuis un schéma OpenAPI, bâti sur Hypothesis), CrossHair (exécution symbolique, branchée à Hypothesis comme moteur expérimental) et Atheris (fuzzer à couverture de Google, Apache-2.0).*

### Compléments

- [[pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins. — le plugin pytest est inclus dans le paquet Hypothesis (options `--hypothesis-profile`, `--hypothesis-seed`, `--hypothesis-show-statistics`) ; une fixture à portée fonction n'est réinitialisée qu'une fois par test, pas par exemple généré, et un `HealthCheck` le signale.
- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique. — `hypothesis.extra.numpy` offre `arrays`, `array_shapes`, `broadcastable_shapes` et `from_dtype` ; sans `elements` borné, un tableau de flottants contient des NaN.
- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — `hypothesis.extra.pandas` offre `data_frames`, `column`, `series` et `indexes`.
- voisin : [[Pydantic]] — Pydantic 2 a retiré son plugin Hypothesis (sa documentation écrit qu'il pourrait revenir) ; `st.from_type` gère en revanche les contraintes `annotated-types` (`Gt`, `Ge`, `Lt`, `Le`, `MinLen`, `MaxLen`, `Predicate`) en filtrant, et ignore les autres. `st.builds(Modèle)` n'a pas été exécuté pour cette fiche : à essayer sur un modèle réel avant de l'adopter.

## Ressources

- Documentation — https://hypothesis.readthedocs.io/
- Dépôt — https://github.com/HypothesisWorks/hypothesis

## Voir aussi

- [[Outils de développement]] — le hub du domaine
