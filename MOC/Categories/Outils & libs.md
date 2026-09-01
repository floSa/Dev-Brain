---
type: moc
nom: Outils & libs
galaxie: dev
indexe: tooling/*
---

# Outils & libs

<!-- AUTO:START -->
Briques techniques de la catégorie `tooling/*`.

- [[Dev/Outils/ai-memory|ai-memory]] — Serveur MCP de mémoire long terme pour CLI de code (MIT, Rust) : capture les sessions, les consolide en wiki markdown versionné sur SQLite/FTS5, et permet de reprendre sous Codex une tâche entamée sous Claude Code.
- [[Dev/Outils/Aider|Aider]] — Pair-programmeur IA dans le terminal : édite ton dépôt git en langage naturel, commit automatique, agnostique de l'éditeur.
- [[Dev/Services/Alembic|Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.
- [[Dev/Services/altair|altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.
- [[Dev/Outils/Archify|Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.
- [[Dev/Services/ArviZ|ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- [[Dev/Outils/BMAD|BMAD]] — Framework de développement piloté par agents (MIT avec clause de marque, npm `bmad-method`) : installe dans Claude Code ou Cursor un jeu d'agents nommés — analyst, PM, architect, dev, UX, scrum master, test architect — et le flux brief → PRD → architecture → implémentation story par story.
- [[Dev/Services/bokeh|bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- [[Dev/Outils/Bruno|Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.
- [[Dev/Services/CausalImpact|CausalImpact]] — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.
- [[Dev/Outils/Claude Video|Claude Video]] — Skill /watch qui donne à un agent la capacité de regarder une vidéo (YouTube, TikTok, Loom, fichier local) : télécharge via yt-dlp, extrait des frames JPEG horodatées via ffmpeg, récupère une transcription (captions natives ou Whisper), puis remet frames + transcript à l'assistant pour analyse.
- [[Dev/Outils/Cline|Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Dev/Services/connectorx|connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.
- [[Dev/Outils/Continue|Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Dev/Outils/DataGrip|DataGrip]] — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[Dev/Outils/draw.io|draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Dev/Services/dynaconf|dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[Dev/Outils/Excalidraw|Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[Dev/Services/Faker|Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- [[Dev/Services/Fanalysis|Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR.
- [[Dev/Outils/Figma|Figma]] — Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.
- [[Dev/Services/Flyway|Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Dev/Outils/FossFLOW|FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.
- [[Dev/Outils/freebuff|freebuff]] — Assistant de code multi-agents gratuit financé par la publicité (ex-Codebuff) : modèles hébergés sans clé API, sessions journalières plafonnées et prompts exploités pour le ciblage.
- [[Dev/Outils/Graphify|Graphify]] — Transforme un dépôt (code, docs, SQL, images) en knowledge graph interrogeable pour que l'assistant IA lise la structure avant de grep : god nodes, communautés, outils MCP.
- [[Dev/Outils/HeidiSQL|HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- [[Dev/Services/hydra|hydra]] — Framework de configuration hiérarchique composable (Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Dev/Outils/i-have-adhd|i-have-adhd]] — Skill/plugin MIT pour agents de code (Claude Code, Cursor, Codex, Gemini, Qwen, Kimi) imposant dix règles de sortie : action en premier, étapes numérotées, état rappelé à chaque tour, ni préambule ni récapitulatif.
- [[Dev/Services/jupysql|jupysql]] — SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats.
- [[Dev/Services/jupytext|jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.
- [[Dev/Services/Liquibase|Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.
- [[Dev/Outils/Maka|Maka]] — Espace de travail local-first pour agents IA, en incubation à l'ASF (Apache-2.0, Electron) — chaque message, appel d'outil et décision de permission est écrit dans un journal append-only rejouable sur la machine.
- [[Dev/Services/Marimo|Marimo]] — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.
- [[Dev/Services/matplotlib|matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.
- [[Dev/Services/mcpjam|mcpjam]] — « Postman pour MCP » : inspecteur open-source pour tester, déboguer et évaluer un serveur MCP — exécution manuelle des outils, observabilité JSON-RPC et playground LLM.
- [[Dev/Outils/Mermaid|Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[Dev/Services/Mimesis|Mimesis]] — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- [[Dev/Services/missingno|missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.
- [[Dev/Services/Modin|Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dev/Outils/MongoDB Compass|MongoDB Compass]] — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- [[Dev/Outils/MySQL Workbench|MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- [[Dev/Services/numpy|numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- [[Dev/Services/pandas|pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Dev/Services/papermill|papermill]] — Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI.
- [[Dev/Outils/Penpot|Penpot]] — Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.
- [[Dev/Outils/pgAdmin|pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- [[Dev/Outils/pi|pi]] — Boîte à outils d'agent IA en TypeScript (API LLM unifiée, boucle d'agent, TUI, CLI de codage) avec support de première classe de llama.cpp et des endpoints OpenAI/Anthropic-compatible auto-hébergés.
- [[Dev/Services/pingouin|pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- [[Dev/Services/pip|pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.
- [[Dev/Services/plotly|plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[Dev/Services/Polars|Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Dev/Outils/Postman|Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.
- [[Dev/Services/Prince|Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
- [[Dev/Outils/public-apis|public-apis]] — Annuaire communautaire d'APIs publiques et gratuites (MIT, maintenu depuis 2016) : de l'ordre de 1 700 entrées classées en 52 catégories, dans un seul README — pas un client d'API, pas de service, rien à installer.
- [[Dev/Services/PuLP|PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…).
- [[Dev/Services/Pydantic|Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.
- [[Dev/Services/Pydantic Settings|Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.
- [[Dev/Services/PyMC|PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- [[Dev/Services/pytest|pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.
- [[Dev/Services/python-dotenv|python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Dev/Services/PyWavelets|PyWavelets]] — Transformées en ondelettes en Python — DWT/IDWT, CWT, décomposition multiniveau et seuillage, avec une large famille d'ondelettes (Daubechies, Morlet, Haar…) ; le standard de l'analyse temps-échelle.
- [[Dev/Services/Quarto|Quarto]] — Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia).
- [[Dev/Outils/Redis Insight|Redis Insight]] — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).
- [[Dev/Services/Rich|Rich]] — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.
- [[Dev/Services/Ruff|Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.
- [[Dev/Services/scipy.signal|scipy.signal]] — Module de traitement du signal de SciPy : filtres FIR/IIR (Butterworth…), analyse spectrale (périodogramme, Welch, STFT/spectrogramme), convolution, corrélation et ré-échantillonnage, au-dessus de NumPy.
- [[Dev/Services/scipy.stats|scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[Dev/Services/seaborn|seaborn]] — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.
- [[Dev/Outils/Spec Kit|Spec Kit]] — CLI de GitHub pour le spec-driven development : une spécification exécutable pilote un agent de codage IA du cahier des charges à l'implémentation (constitution → specify → plan → tasks → implement).
- [[Dev/Services/Stan|Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
- [[Dev/Services/statsmodels|statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
- [[Dev/Outils/Superwhisper|Superwhisper]] — Application propriétaire de dictée vocale (macOS, Windows, iOS) qui transcrit en local via whisper.cpp (modèles de 75 Mo à 3 Go) ou WhisperKit/Parakeet, avec repli sur des modèles cloud ; freemium, Pro à 8,49 $/mois ou 249,99 $ à vie.
- [[Dev/Outils/swarm-forge|swarm-forge]] — Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée.
- [[Dev/Services/sweetviz|sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[Dev/Outils/t3code|t3code]] — Plan de contrôle au-dessus des CLI d'agents de code installées localement (Claude Code, Codex, Cursor, OpenCode, Grok) : desktop, web et mobile, sans parler lui-même à un LLM.
- [[Dev/Services/testcontainers|testcontainers]] — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.
- [[Dev/Services/Typer|Typer]] — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.
- [[Dev/Services/uv|uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.
- [[Dev/Services/xarray|xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).
- [[Dev/Services/ydata-profiling|ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
<!-- AUTO:END -->

## Notes

