---
type: moc
nom: Data & pipelines
galaxie: dev
indexe: data/*
---

# Data & pipelines

<!-- AUTO:START -->
Briques techniques de la catégorie `data/*`.

- [[Dev/Services/Airflow|Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dev/Services/altair|altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.
- [[Dev/Services/Apache Iceberg|Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB).
- [[Dev/Services/Avro|Avro]] — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.
- [[Dev/Services/bokeh|bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- [[Dev/Services/cloudscraper|cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Dev/Services/connectorx|connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination.
- [[Dev/Services/Crawlee|Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Dev/Services/curl_cffi|curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[Dev/Services/Dagster|Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Dev/Services/Docling|Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Dev/Services/docTR|docTR]] — Bibliothèque OCR de bout en bout de Mindee (écosystème PyTorch, backend TF aussi) — pipeline détection de texte (DBNet, LinkNet) puis reconnaissance (CRNN, SAR) avec modèles pré-entraînés ; l'OCR open-source clé en main pour documents.
- [[Dev/Services/Faker|Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- [[Dev/Services/Firecrawl|Firecrawl]] — API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.
- [[Dev/Services/Flink|Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch.
- [[Dev/Services/Kestra|Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Dev/Services/LlamaParse|LlamaParse]] — Service managé de parsing de documents (LlamaCloud) : extraction agentique par LLM des PDF complexes, tableaux et schémas vers du Markdown propre prêt pour le RAG ; API à crédits, non open-source.
- [[Dev/Services/Mage|Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Dev/Services/Marker|Marker]] — Convertisseur PDF (et Office, images) → Markdown / JSON / HTML rapide et précis, bâti sur les modèles OCR Surya ; pipeline vision multi-étapes orienté RAG, code GPL et poids de modèles à licence restreinte.
- [[Dev/Services/matplotlib|matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.
- [[Dev/Services/Maxun|Maxun]] — Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.
- [[Dev/Services/Mimesis|Mimesis]] — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- [[Dev/Services/minim|minim]] — Bibliothèque Python d'interfaces vers les API musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) : récupération de métadonnées et tagging audio semi-automatisé.
- [[Dev/Services/missingno|missingno]] — Boîte à outils de visualisation des valeurs manquantes — matrice, barres, heatmap et dendrogramme de nullité pour repérer la structure des trous d'un jeu pandas.
- [[Dev/Services/Modin|Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dev/Services/numpy|numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]] — Parseur PDF Java sous Apache 2.0 orienté données AI-ready : sortie déterministe en JSON à bounding boxes, Markdown et HTML avec ordre de lecture XY-Cut++, plus l'auto-tagging d'un PDF non balisé en Tagged PDF ; mode hybride optionnel qui route les pages complexes vers un backend IA.
- [[Dev/Services/pandas|pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Dev/Services/Parquet|Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.
- [[Dev/Services/pdf-inspector|pdf-inspector]] — Bibliothèque et CLI Rust qui classent un PDF (texte natif, scanné, mixte) en quelques dizaines de millisecondes et en extraient le texte positionné vers du Markdown, pour ne router vers l'OCR que les pages qui en ont besoin ; bindings Python, Node et WASM.
- [[Dev/Services/pdfplumber|pdfplumber]] — Extraction de texte et de tableaux PDF avec accès détaillé à chaque objet (caractères, lignes, rectangles), bâtie sur pdfminer.six ; extraction de tableaux configurable et débogage visuel, licence MIT.
- [[Dev/Services/Playwright|Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.
- [[Dev/Services/plotly|plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[Dev/Services/Polars|Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/PyMuPDF|PyMuPDF]] — Binding Python de MuPDF (moteur C) : extraction et manipulation de PDF très rapides — texte, images, tableaux, annotations, rendu — avec accès bas niveau au modèle objet PDF ; licence AGPL ou commerciale.
- [[Dev/Services/Scrapling|Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.
- [[Dev/Services/Scrapy|Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[Dev/Services/SDV|SDV]] — Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL).
- [[Dev/Services/seaborn|seaborn]] — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.
- [[Dev/Services/selectolax|selectolax]] — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages.
- [[Dev/Services/sweetviz|sweetviz]] — EDA visuelle en une ligne — rapport HTML auto-porté centré sur l'analyse d'une cible et la comparaison de deux jeux (train vs test, sous-groupes).
- [[Dev/Services/Temporal|Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.
- [[Dev/Services/Unstructured|Unstructured]] — Boîte à outils ETL open-source pour documents : partitionne plus de 60 formats (PDF, Office, HTML, e-mails, images) en éléments structurés et typés (titres, paragraphes, tableaux, listes) prêts à chunker et embarquer pour le RAG.
- [[Dev/Services/xarray|xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).
- [[Dev/Services/ydata-profiling|ydata-profiling]] — Profiling EDA en une ligne — génère un rapport HTML exhaustif (types, distributions, manquants, corrélations, alertes) sur DataFrames pandas et Spark.
<!-- AUTO:END -->

## Notes

