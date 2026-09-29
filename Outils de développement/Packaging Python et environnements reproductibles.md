---
role: notion
nom: Packaging Python et environnements reproductibles
alias: [packaging Python, pyproject.toml, fichier de verrouillage, lockfile, uv.lock, pylock.toml, wheel, sdist, environnement virtuel, venv, miroir PyPI, dépendances en réseau fermé, build reproductible]
categorie: devtools/paquet
domaines: [data-sci, data-eng, ml-eng, ai-eng, mlops]
tags: [package-manager, reproducibility]
---

# Packaging Python et environnements reproductibles

## Aperçu

- « Reproductible » veut dire : refaire l'installation plus tard, sur une autre machine, et obtenir les **mêmes paquets**. Cela ne veut pas dire le même résultat compilé, ni le même système : la section sur Docker revient sur cette limite.
- La chaîne a cinq maillons, et chacun a son fichier ou son format : `pyproject.toml` **déclare** ce dont le projet a besoin, un fichier de verrouillage **fige** les versions et leurs empreintes, l'environnement virtuel **héberge** l'installation, la *wheel* et le *sdist* **transportent** le code, un index (public, ou un miroir interne) **sert** les fichiers.
- En on-prem, un maillon est souvent coupé : pas d'accès à PyPI depuis la machine de build ou de production. Le sujet devient alors celui du miroir interne et des installations hors ligne.
- Les outils changent vite (uv est en 0.12.22 au 2026-10-02, pip en 26.2.1) ; les standards, eux, sont des PEP finalisées. La page s'appuie sur les seconds et date les premiers.

## Concepts clés

### Paquet, distribution, environnement

- Un **environnement virtuel** est un répertoire jetable, non versionné, créé au-dessus d'un Python de base. La documentation de `venv` le dit non portable en général : on le **recrée**, on ne le déplace pas.
- Une **distribution** est l'archive publiée (sdist ou wheel) ; le paquet importable est ce qu'elle contient. La définition exacte de « paquet » n'a pas été relue dans le glossaire de PyPA.
- Le guide de PyPA note que les environnements virtuels s'effacent peu à peu derrière des outils de plus haut niveau : [[uv]] en crée un sans qu'on le demande.

### `pyproject.toml` : trois tables, quelques PEP

- **`[build-system]`** : la PEP 518 (2016) y met `requires`, ce qu'il faut installer pour construire le projet. La PEP 517 (2017) fixe l'interface entre l'outil de build et le *backend* : deux hooks, `build_wheel` et `build_sdist`, et `backend-path`. Backends listés par PyPA : Hatchling, setuptools, Flit, PDM, `uv-build` — ce dernier ne gère que du Python pur.
- **`[project]`** : la PEP 621 y met les métadonnées (nom, version, dépendances, `requires-python`) ; un champ peut être `dynamic`, seul `name` ne le peut pas. La PEP 639 remplace les champs de licence libres et les classifieurs par une **expression SPDX** et `license-files`.
- **`[tool]`** : l'espace réservé à chaque outil.
- **Les groupes de dépendances** (PEP 735, résolue le 2024-10-10) : une table `[dependency-groups]` pour les dépendances de développement ou de test, **non publiées** dans les distributions.
- **Les métadonnées dans un script** (PEP 723, 2024-01-08, qui remplace la PEP 722) : un bloc `# /// script` en tête d'un fichier `.py` déclare ses dépendances. [[uv]] le lit, et sait verrouiller un script. Voir aussi [[Notebooks-as-code]] pour le même besoin côté notebook.
- Les PEP portent un bandeau « document historique » : la spécification de référence vit sur `packaging.python.org/specifications`.
- **Périmé** : `python setup.py install`. La documentation de pip le déconseille, car il contourne la vérification des empreintes.

### Wheel et sdist

- Une **wheel** (PEP 427) est une archive ZIP au nom `{distribution}-{version}(-{build})?-{python}-{abi}-{platform}.whl` ; son dossier `.dist-info` contient `METADATA`, `WHEEL` et `RECORD` (empreintes SHA-256). L'installer revient à la copier.
- Un **sdist** est une archive `.tar.gz` avec un `pyproject.toml` et un `PKG-INFO` : il faut le **construire** avant de l'installer, donc exécuter le backend sur la machine. C'est la source de la plupart des surprises (compilateur, bibliothèques C absentes) — c'est un raisonnement de rédaction, pas une phrase de source.
- Les étiquettes de compatibilité disent à quelle machine va une wheel ; celles de `manylinux` sont compatibles vers l'avant (une glibc plus récente) et pas vers l'arrière ; l'installeur choisit la wheel la plus spécifique.
- Par défaut, on publie les deux, sdist et wheel (aperçu de PyPA). `pip wheel` compile des wheels réutilisables, propres à un OS et une architecture.

### Verrouiller : déclarer n'est pas figer

- `dependencies = ["pandas>=2"]` dit ce qu'on accepte ; un **fichier de verrouillage** dit ce qu'on a **installé** : toutes les dépendances, transitives comprises, à une version exacte, avec leurs empreintes.
- **`requirements.txt` + pip.** `--require-hashes` est « tout ou rien » : chaque dépendance, transitive comprise, doit être épinglée et porter une empreinte (SHA-256 recommandé ; MD5, SHA-1 et SHA-224 refusés). La documentation de pip précise que l'épinglage seul « fait confiance aux sources ». `pip-tools` (`pip-compile`, `pip-sync`) produit ce fichier depuis un `.in` ou un `pyproject.toml` ; il faut compiler **dans chaque environnement cible**.
- **`uv.lock`.** Un fichier TOML lisible, **universel** (il couvre tous les marqueurs : système, architecture, version de Python), **propre à uv**, à versionner et à ne pas éditer à la main. `requires-python` borne le verrouillage ; la stratégie par défaut prend les versions les plus hautes ; `exclude-newer` filtre sur la date d'envoi de chaque fichier. `uv sync --locked` **échoue** si le verrou est à refaire ; `--frozen` l'utilise sans le vérifier. La documentation déconseille de garder `uv.lock` et un `requirements.txt` ensemble ; `uv export` produit l'un depuis l'autre.
- **`pylock.toml` (PEP 751).** Le format standard, **Final** depuis le 2025-03-31, qui remplace la PEP 665 (et a mis près de six ans à aboutir, de février 2019 à mars 2025, d'après le billet de Brett Cannon, dont le titre dit pourtant quatre ans). Il exige des empreintes et vise une installation **sans résolution** au moment d'installer ; un fichier peut servir à un seul environnement ou à plusieurs.
- **Qui le lit.** pip : `pip lock` est **expérimental** (25.1, 2025-04-26), la lecture de `pylock.toml` est expérimentale depuis 26.1 (2026-04-26), et le verrou n'est garanti que pour le couple Python-plateforme courant. uv : export et lecture. D'après un billet de 2026-09-07, PDM exporte, Poetry n'avait rien livré à avril 2026 ; ce billet signale aussi que l'implémentation de pip n'a pas les extras ni les groupes.
- **Désaccord laissé tel quel.** Pour la documentation d'uv, `pylock.toml` est un format sans outil propriétaire qui **ne dit pas tout** ce que dit `uv.lock` ; Charlie Marsh y voyait des limites dès 2024 (extras, réglages propres à l'outil, installation éditable). Pour d'autres, c'est une base commune : Poetry, PDM et uv se disaient prêts à l'exporter sans l'adopter comme format natif (DevClass, 2025-04-04). Un billet commercial (RepoForge, 2026) parle d'une adoption « mitigée ».

### Réseau fermé : miroir interne ou dossier de wheels

- **Dossier de wheels** : `pip download -d <dossier>` récupère les fichiers (avec `--platform`, `--python-version` et `--only-binary` pour viser une autre cible), puis `pip install --no-index --find-links <dossier>` installe sans réseau. Pour uv, `--offline` (ou `UV_OFFLINE`) coupe le réseau et le cache sert ; `UV_CACHE_DIR` le place.
- **Miroir** : [devpi](https://devpi.net/) (serveur compatible PyPI, miroir en cache rafraîchi toutes les 30 minutes par défaut, index privés avec héritage), **bandersnatch** (client de miroir à la PEP 381, qui filtre par liste, plateforme ou taille ; un miroir complet de PyPI est volumineux), **Nexus** et **Artifactory** (dépôts proxy, hébergé et groupe ; pip pointe son `index-url` vers le groupe).
- **Configurer uv** : `default = true` ou `--default-index` remplace PyPI (`UV_INDEX_URL` est déprécié au profit de `UV_DEFAULT_INDEX`) ; `explicit = true` avec `[tool.uv.sources]` épingle un paquet à un index. uv **ne lit ni `pip.conf` ni `PIP_INDEX_URL`**.
- **Python lui-même.** uv télécharge par défaut les versions de Python demandées, depuis les binaires `python-build-standalone` d'Astral (hébergés sur GitHub) : sans réseau, régler `python-downloads` (`automatic`, `manual`, `never`) et `python-install-mirror` (`UV_PYTHON_INSTALL_MIRROR`), ou fournir Python dans l'image.
- **La confusion de dépendance.** Mélanger un index privé et PyPI par `--extra-index-url` expose à ce qu'un paquet public de même nom l'emporte sur le paquet privé ; la référence de `pip install` en met en garde. uv prend par défaut `first-index` (il s'arrête au premier index qui contient le paquet), ce qui **diffère de pip** ; `unsafe-best-match` imite pip et réexpose au risque. La demande d'amélioration ouverte dans pip (n° 8606, 2020-07-21) l'est toujours ; dans un fil de 2021, des mainteneurs y voient un problème d'infrastructure plutôt que de conception de pip. Mesures citées : épinglage, proxys privés, espaces de noms, empreintes.
- Les stubs de types (voir [[Typage statique en Python]]) sont des paquets comme les autres : à mettre dans le miroir.

### Reproduire une image Docker

- **Ce que dit Docker** : épingler l'image de base par son **empreinte** (*digest*) garantit la même image même si l'éditeur remplace l'étiquette ; contrepartie, plus de correctifs de sécurité automatiques, à compenser par un outil de mise à jour (Dependabot). Le multi-stage sépare construction et exécution.
- **Ce que dit le guide d'uv** : épingler la version d'uv et, pour le maximum, son empreinte ; une couche de dépendances par `uv sync --locked --no-install-project` ; `--no-editable` pour ne copier que le `.venv` entre étapes ; `UV_LINK_MODE=copy` avec un cache monté ; `UV_COMPILE_BYTECODE=1` en option ; `.venv` dans `.dockerignore` ; pour un *workspace*, `--frozen` d'abord, puis `--locked` une fois tous les membres copiés.
- **Un praticien** (Hynek Schlawack, billet lu par résumé, mis à jour en 2026) : deux étapes, une base Ubuntu plutôt qu'Alpine, `UV_LOCKED=1`, `UV_PYTHON_DOWNLOADS=never`, `UV_NO_DEV=1`, un utilisateur sans privilèges. **Écart** : Docker et uv recommandent l'empreinte, ce billet n'en épingle pas et laisse `uv.lock` porter la détermination.
- **Ce que le verrou n'épingle pas** : l'image de base (hors empreinte), le Python du système, les bibliothèques C. Une empreinte prouve qu'on installe la même **archive**, pas que deux builds de sdist sortent identiques (raisonnement de rédaction). Reproductible s'entend donc « mêmes paquets », pas « mêmes octets ».
- Pour l'image comme artefact, l'image immuable et le réseau fermé : voir [[Infrastructure as code — configuration, provisionnement et idempotence]] ; pour le passage de l'image à l'orchestration : [[Du Compose à Kubernetes — quand changer d'échelle]].

### Publier

- Le tutoriel de PyPA : `python3 -m build` produit une wheel et un sdist dans `dist/`, `twine` les envoie avec un jeton d'API, sur TestPyPI d'abord. Le tutoriel ne parle que de jetons ; **PyPI recommande le « trusted publishing »** (échange d'un jeton d'identité OIDC contre un jeton PyPI valable 15 minutes). `uv build` et `uv publish` couvrent les deux, y compris le trusted publishing, et envoient les attestations existantes (PEP 740, résolue le 2024-07-17).
- Publier vers un index **interne** (devpi, Nexus, Artifactory) n'a pas été relu pour ces serveurs. Les jetons de publication sont des secrets : [[Gestion des secrets]].

### Critiques, et un fait de gouvernance

- **Astral** a annoncé le 2026-03-19 rejoindre OpenAI (équipe Codex), en promettant de continuer à soutenir [[Ruff]], [[uv]] et ty en open source ; le billet ne contient aucun engagement de licence. Le paquet uv porte sur PyPI la licence `MIT OR Apache-2.0` (relevée dans l'API de PyPI). Dans un épisode de podcast de juin 2026 (résumé lu), Charlie Marsh dit que le rythme de publication n'a pas changé. JetBrains juge le risque de réaffectation des ingénieurs réel mais le projet « facilement forkable » : c'est un **avis**.
- **Défauts relevés** : un cache de plus de 20 Go par an et des Python hors CPython officiel (BiteCode, 2025-02-15, billet vieillissant) ; des bornes basses seules ajoutées par défaut et pas de commande « périmé » simple, contournables par `add-bounds = "major"` (Loopwerk, 2026-05-21).
- **Aucun comparatif neutre** uv contre Poetry contre pip-tools n'a été trouvé : le seul lu est un billet commercial, et un autre a renvoyé 404. Les chiffres de benchmark vus dans des résumés ne sont pas repris.

## En pratique

- Nouveau projet : `pyproject.toml` + `uv.lock` **versionné** ; `uv sync --locked` en intégration continue, pour qu'un verrou périmé fasse échouer le job.
- Équipe qui n'a pas uv, ou outil imposé : `uv export` vers un `requirements.txt` avec empreintes, ou `pylock.toml`, plutôt que deux fichiers maintenus à la main.
- Site on-prem : choisir **un** miroir (devpi, Nexus, Artifactory) ou un dossier de wheels, pointer l'index par défaut dessus, ne pas utiliser `--extra-index-url` pour des paquets privés, prévoir Python et les stubs.
- Image Docker : un `uv sync --locked --no-install-project` en couche séparée, l'image de base et uv épinglés, une reconstruction régulière.
- Épingler la version de l'outil lui-même (uv est en 0.x) ; noter le nom des attestations et des jetons de publication comme des secrets.
- Choisir entre pip et uv n'est pas ici : voir [[Comparatif - Gestionnaires de paquets Python]].

## Approches voisines & alternatives

- [[uv]] et [[pip]] — les deux gestionnaires du brain ; [[Comparatif - Gestionnaires de paquets Python]] dit ce qui les sépare. La fiche de pip dit « aucun lockfile natif » : c'est exact pour une installation courante, mais `pip lock` existe depuis 25.1 en expérimental (voir plus haut).
- [[Docker]] — l'image comme unité de livraison reproductible ; [[Ruff]] — l'autre outil d'Astral.
- **Poetry**, **PDM**, **Hatch**, **pip-tools**, **conda** (sans fiche) — Poetry et PDM ont leur propre fichier de verrouillage et un export vers le format standard ; conda n'a pas été relu pour cette page.
- [[Infrastructure as code — configuration, provisionnement et idempotence]] et [[Du Compose à Kubernetes — quand changer d'échelle]] — ce qui entoure l'image.
- Voir aussi : [[Notebooks-as-code]], [[Typage statique en Python]], [[Gestion des secrets]].

## Pour aller plus loin

- PEP 517 : https://peps.python.org/pep-0517/ ; PEP 518 : https://peps.python.org/pep-0518/ ; PEP 621 : https://peps.python.org/pep-0621/ ; PEP 639 : https://peps.python.org/pep-0639/ ; PEP 723 : https://peps.python.org/pep-0723/ ; PEP 735 : https://peps.python.org/pep-0735/ ; PEP 740 : https://peps.python.org/pep-0740/ ; PEP 751 : https://peps.python.org/pep-0751/
- PyPA — écrire `pyproject.toml` : https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ ; tutoriel : https://packaging.python.org/en/latest/tutorials/packaging-projects/ ; aperçu : https://packaging.python.org/en/latest/overview/ ; formats wheel et sdist : https://packaging.python.org/en/latest/specifications/binary-distribution-format/ et https://packaging.python.org/en/latest/specifications/source-distribution-format/ ; `venv` : https://docs.python.org/3/library/venv.html ; trusted publishing : https://docs.pypi.org/trusted-publishers/
- uv — projets et verrou : https://docs.astral.sh/uv/concepts/projects/layout/ ; synchroniser : https://docs.astral.sh/uv/concepts/projects/sync/ ; export : https://docs.astral.sh/uv/concepts/projects/export/ ; index : https://docs.astral.sh/uv/concepts/indexes/ ; compatibilité pip : https://docs.astral.sh/uv/pip/compatibility/ ; versions de Python : https://docs.astral.sh/uv/concepts/python-versions/ ; Docker : https://docs.astral.sh/uv/guides/integration/docker/
- pip — installations sûres : https://pip.pypa.io/en/stable/topics/secure-installs/ ; répétables : https://pip.pypa.io/en/stable/topics/repeatable-installs/ ; `pip lock` : https://pip.pypa.io/en/stable/cli/pip_lock/ ; nouveautés : https://pip.pypa.io/en/stable/news/ ; demande n° 8606 : https://github.com/pypa/pip/issues/8606
- Miroirs : https://devpi.net/docs/devpi/devpi/stable/+doc/index.html ; https://bandersnatch.readthedocs.io/en/latest/ ; https://help.sonatype.com/en/pypi-repositories.html ; https://docs.jfrog.com/artifactory/docs/pypi-repositories
- Docker — bonnes pratiques : https://docs.docker.com/build/building/best-practices/ ; Hynek Schlawack : https://hynek.me/articles/docker-uv/
- Astral et OpenAI : https://astral.sh/blog/openai ; épisode : https://talkpython.fm/episodes/show/552/astral-joins-openai
- Format de verrouillage : https://snarky.ca/why-it-took-4-years-to-get-a-lock-files-specification/ ; https://devclass.com/2025/04/04/python-now-has-a-standard-package-lock-file-format-though-winning-full-adoption-will-be-a-challenge/ ; https://pydevtools.com/handbook/explanation/what-is-pep-751/
- Critiques : https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should ; https://www.loopwerk.io/articles/2026/uv-ux-mess/ ; RepoForge (commercial) : https://repoforge.io/blog/posts/the-state-of-python-packaging-in-2026/
