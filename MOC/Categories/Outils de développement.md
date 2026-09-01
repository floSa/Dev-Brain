---
type: moc
nom: Outils de développement
galaxie: dev
indexe: devtools/*
---

# Outils de développement

<!-- AUTO:START -->
Briques techniques de la catégorie `devtools/*`.

- [[Dev/Outils/Bruno|Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.
- [[Dev/Services/dynaconf|dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[Dev/Services/hydra|hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Dev/Services/jupysql|jupysql]] — SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats.
- [[Dev/Services/jupytext|jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.
- [[Dev/Services/Marimo|Marimo]] — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.
- [[Dev/Services/papermill|papermill]] — Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI.
- [[Dev/Services/pip|pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.
- [[Dev/Outils/Postman|Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.
- [[Dev/Services/Pydantic|Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.
- [[Dev/Services/Pydantic Settings|Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.
- [[Dev/Services/pytest|pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.
- [[Dev/Services/python-dotenv|python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Dev/Services/Quarto|Quarto]] — Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia).
- [[Dev/Services/Rich|Rich]] — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.
- [[Dev/Services/Ruff|Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.
- [[Dev/Services/testcontainers|testcontainers]] — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.
- [[Dev/Services/Typer|Typer]] — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.
- [[Dev/Services/uv|uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.
<!-- AUTO:END -->

## Notes

