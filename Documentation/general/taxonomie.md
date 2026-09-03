---
nom: taxonomie
role: gouvernance
created: 2026-06-04
modified: 2026-09-05
tags: [meta, gouvernance, taxonomie]
---

# Taxonomie — deux axes de rangement

Une page du brain est rangée sur **deux axes indépendants**, tous deux à vocabulaire fermé :

| Axe | Question à laquelle il répond | Valeurs |
|-----|-------------------------------|---------|
| `categorie:` | **De quoi ça parle** — le domaine, le sujet | 100 valeurs, cf. section *Axe `categorie:`* |
| `famille:` | **Ce que c'est** — la nature de la chose | 9 valeurs, cf. section *Axe `famille:`* |

`famille:` porte la **NATURE**, `categorie:` porte le **DOMAINE**. Les deux sont contrôlés par
`AI/scripts/check_brain.py` : une valeur hors liste échoue en dur.

**`type:` a été supprimé** au lot 2 de la migration v3, et remplacé par `role:`. La v2 avait
déjà constaté qu'il ne portait pas la nature : il était posé par le dossier d'accueil
(`Dev/Services/` vs `Dev/Outils/`), pas par une question sur l'objet. Le croisement le prouvait :
sur les 336 fiches Dev, 57 relevaient des familles `application`, `cli` ou `extension` — 34 en
`type: outil`, 23 en `type: service`, sans discriminant (Marimo, notebook à interface, était
`type: service` ; DBeaver, client à interface, `type: outil` — même nature, types opposés ;
symétriquement, 11 des 13 `saas` étaient `type: service`). Les deux gabarits ont donc fusionné
en `role: brique`.

**`role:` n'est pas un troisième axe de rangement**, c'est la nature **éditoriale** de la page.
Il choisit le **gabarit** que le validateur applique. `famille:` reste la nature **technique**
d'une brique : est-ce un paquet ou une plateforme ? Pour savoir ce qu'**est** une brique, lire
`famille:` — jamais `role:`, qui dit seulement que c'en est une.

## Axe `role:` — la nature éditoriale de la page (6 valeurs)

Énumération fermée, lue par `check_brain.py` : un `role:` inconnu ou absent est refusé, il n'y
a plus de page sans gabarit [R3].

| `role:` | Ce que la page est | Porte `categorie:` ? | Où elle vit |
|---|---|---|---|
| `brique` | ce qu'on **déploie ou importe** : service, outil, librairie | **oui** — c'est elle qui décide du dossier | `<Dossier>/<Nom>.md` |
| `notion` | ce qu'il faut **comprendre** : définitions, maths, mécanismes | **oui** — son **domaine**, comme une brique | `<Dossier>/<Nom>.md` — les non encore migrées sont sous `Wiki/Concepts/` |
| `pattern` | une **architecture éprouvée** | **non** | `Patterns/Pattern - <nom>.md` |
| `rule` | une **règle transverse** | **non** | `Rules/Rule - <nom>.md` |
| `hub` | la **page d'un dossier**, l'aiguillage | **non** | `<Dossier>/<Dossier>.md` + les 5 de `Métiers/` |
| `comparatif` | ce qui **départage** plusieurs briques | à définir | aucune page — naît au **lot 5**, les comparatifs sont des `.base` |

Trois rôles n'ont **pas** de `categorie:`, et c'est délibéré, pas un oubli :

- un **hub** ne se range pas, il *est* le rangement — son domaine est son chemin ;
- un **pattern** enjambe plusieurs domaines par construction ;
- une **règle** est transverse par définition.

C'est `role:` qui les groupe, dans `Patterns/` et `Rules/`. Le champ est indexé et filtrable :
`uv run AI/scripts/query_index.py --role hub`.

> `role:` a remplacé `galaxie:` et `type:` au lot 2. Le premier ne servait qu'à la couleur du
> graphe ; le second ne décrivait que le dossier d'accueil. Les pages de gouvernance
> (`Documentation/`, `AI/`, docs de la racine) ne sont pas des pages du brain : le validateur
> ne les contrôle pas, et leur `role:` ne vient pas de cette liste.

## Axe `famille:` — la nature de la brique (9 valeurs fermées)

Énumération fermée, lue par `check_brain.py` dans ce bloc de code et **là seulement** :

```famille
paquet
plateforme
application
cli
saas
extension
specification
modele
annuaire
```

Le champ est attendu sur `role: brique`, et interdit sur les autres gabarits (`notion`,
`pattern`, `rule` : ceux-là ne documentent pas une brique). `check_brain` refuse en
dur toute valeur hors de ce bloc [R14] mais **accepte un champ vide** : c'est le seul signal
prévu pour « l'arbre n'a pas tranché, à arbitrer ». Une famille inventée est une faute, un champ
vide est une question ouverte.

### Arbre de décision — ORDRE STRICT, première réponse positive gagne

La famille ne se **choisit** pas, elle se **dérive**. On descend les neuf questions dans l'ordre
et on s'arrête à la première réponse « oui ». Aucune question n'appelle un jugement de valeur :
toutes portent sur un fait vérifiable dans le dépôt amont ou dans la fiche.

| # | Question fermée | Si oui |
|---|-----------------|--------|
| F1 | La page décrit-elle une liste de ressources externes plutôt qu'un logiciel ? | `annuaire` |
| F2 | Est-ce une norme, un format ou un protocole, sans implémentation de référence unique ? | `specification` |
| F3 | Le livrable téléchargé est-il un jeu de poids entraînés ? | `modele` |
| F4 | Faut-il un logiciel hôte tiers (IDE, navigateur, agent, SGBD) pour l'exécuter ? | `extension` |
| F5 | L'auto-hébergement est-il impossible (compte chez un tiers obligatoire) ? | `saas` |
| F6 | Un autre **programme**, et pas seulement un humain, en est-il le consommateur nominal (port, API réseau) ? | `plateforme` |
| F7 | Le point d'entrée nominal est-il une interface graphique ? | `application` |
| F8 | S'invoque-t-il en commande shell sans être importé dans du code ? | `cli` |
| F9 | Aucun des précédents | `paquet` |

Si deux branches semblent convenir, ce n'est pas à l'arbitrage de trancher : c'est une **règle de
départage** ci-dessous. Si aucune ne tranche, laisser le champ **vide** et demander — ne pas
forcer une valeur.

### Six règles de départage

Sans elles, l'arbre laisse 35 fiches en suspens sur 336 ; avec elles, aucune.

| # | Règle | Cas qu'elle résout |
|---|-------|--------------------|
| R1 | Si le code est publié et déployable, la famille est `plateforme`, jamais `saas`, même si l'éditeur pousse son offre managée. | Comet, Neptune, Weights & Biases, LangSmith, E2B |
| R2 | Un moteur exécutable en embarqué **et** en serveur est `paquet` si l'installation par défaut ne lance aucun processus. | DuckDB, SQLite, Chroma, LanceDB |
| R3 | La famille suit le **point d'entrée documenté en premier** (README amont, à défaut la fiche). | Uvicorn (`cli`), Ray (`paquet`), pi (`cli`), Mermaid (`extension`), LM Studio (`application`), TensorRT (`paquet`), Web-Check (`application`) |
| R4 | `specification` seulement si la page ne documente **aucune** implémentation de référence. | Gymnasium → `paquet` ; ADBC, Parquet, Avro, Iceberg → `specification` |
| R5 | Le tri se fait sur ce dont l'objet **a besoin pour tourner**, pas sur ce à quoi il ressemble. | TransformerLens, SAELens, nnsight, sentence-transformers → `paquet` |
| R6 | Une sortie destinée à une **machine** et une sortie destinée à un **humain** ne rangent pas pareil (vaut surtout pour `categorie:`, cité ici pour mémoire). | Stirling PDF vs docTR |

### Les 9 valeurs, définition et frontière

| Famille | Définition | Frontière |
|---------|-----------|-----------|
| `paquet` | S'installe dans un projet et s'importe dans du code. | Distinct de `cli` parce que le point d'entrée est un `import`, pas une commande. Distinct de `extension` parce que l'hôte est un projet, pas un logiciel. |
| `plateforme` | Se déploie et tourne en processus qu'un autre **programme** appelle. | Distinct de `application` parce que le consommateur nominal n'est pas un humain. Distinct de `saas` parce qu'elle est auto-hébergeable (R1). |
| `application` | S'utilise par une interface faite pour un humain. | Distinct de `plateforme` parce qu'aucune API réseau n'y est un point d'entrée documenté. |
| `cli` | S'invoque en commande shell sans être importé. | Distinct de `paquet` par le point d'entrée documenté en premier (R3) : `axolotl train` contre `import trl`. |
| `saas` | Compte chez un tiers obligatoire, aucun auto-hébergement. | Distinct de `plateforme` parce que le code n'est pas déployable (R1) — une offre managée à côté d'un dépôt ouvert ne suffit pas. |
| `extension` | Ne s'exécute qu'à l'intérieur d'un hôte tiers. | Distinct de `paquet` parce que l'hôte est un **logiciel** (IDE, navigateur, agent de code, SGBD), pas un projet : `pgvector` sans Postgres et `jupysql` sans Jupyter n'exécutent rien. |
| `specification` | Norme, format ou protocole sans implémentation de référence. | Distinct de `paquet` parce qu'il existe plusieurs implémentations et aucune canonique (R4). |
| `modele` | Le livrable est un jeu de poids entraînés. | Distinct de `paquet` parce qu'on charge des poids, on n'écrit pas d'algorithme : `timm` (collection de backbones) est un `paquet`, `segment-anything` (code + poids officiels) un `modele`. |
| `annuaire` | Liste de ressources externes, pas un logiciel. | Distinct de tout le reste parce que rien ne s'installe, rien ne se déploie, il n'y a pas de version à suivre. |

### `famille: annuaire` n'exonère pas du domaine

Un annuaire n'a pas de domaine évident : `public-apis` liste 1 700 API de 52 secteurs. La règle est
néanmoins : **`categorie:` reste obligatoire, et vaut le domaine du sujet listé**, pas celui de la
forme « annuaire ». Quand l'annuaire couvre plusieurs domaines, il prend celui de l'**intention de
recherche** qui le fait ouvrir, et cet arbitrage s'écrit en clair dans le corps de la fiche.

Motif du refus de l'exonération : `categorie:` est un champ requis contrôlé (`check_brain`), et
`build_mocs.py` groupe par `categorie:` — une page sans catégorie sort des MOC et viole aussitôt
R7 (toute page atteignable depuis un MOC). Une exonération pour 2 pages sur 336 serait une
exception que personne ne retient, au prix d'une page injoignable.

## Axe `categorie:` — le domaine (100 valeurs, 20 préfixes de tête)

`categorie:` répond à **une seule** question : *de quoi la page parle-t-elle ?* Elle ne dit
rien de la nature de l'objet — c'est `famille:` qui la porte. Le vocabulaire est **fermé** et
lu par `check_brain.py` dans le bloc ```domaine ci-dessous, et **là seulement**. Une valeur
hors liste échoue en dur ; catégorie manquante → **demander avant d'inventer**.

Le domaine ne se **choisit** pas plus que la famille : il se **dérive** de l'arbre D1→D14, puis
le sous-domaine se lit dans le bloc, à l'intérieur de la branche retenue.

```domaine
ml/{socle, tabulaire, apprentissage-profond, vision, nlp, series-temporelles, rl,
    non-supervise, graphe, embeddings, interpretabilite, eval, hyperopt,
    orchestration, tracking, serving, monitoring, feature-store, hub}
llm/{socle, agents, agent-de-code, assistant, rag, memoire, sortie-structuree,
     text-to-sql, low-code, mcp, passerelle, runtime, finetuning, eval,
     observabilite, outillage}
database/{relationnel, document, cle-valeur, vecteur, series-temporelles, graphe,
          analytique, recherche, driver, orm, migration, admin}
data/{ingestion, parsing, scraping, tableau, format, orchestration, streaming,
      synthetique, eda, viz, fiabilite}
devtools/{notebook, config, cli, client-api, paquet, test, qualite, validation}
stats/{inference, bayesien, exploratoire, causal, probabilite, experimentation}
signal/{traitement, audio}
math/{optimisation, algebre-lineaire, information, theorie-apprentissage}
compute/{distribue, gpu, a-la-demande}
storage/{objet}
web/{backend, frontend, api}
ui/{data-app}
network/{analyse, transfert}
security/{recon, auth}
devops/{ci, conteneur}
observability/{supervision}
automation/{no-code}
docs/{capture, pdf}
media/{ingestion, video}
design/{diagramme, ui}
```

### Arbre de décision `domaine` — ORDRE STRICT, première réponse positive gagne

Comme pour `famille:`, l'ordre est la seule décision de conception : il est pris une fois, écrit
ici, et vaut pour toutes les fiches. C'est lui — et non un arbitrage — qui range `WrenAI`
(text-to-SQL gouverné) en `llm/*` plutôt qu'en `database/*` : D1 passe avant D3, et sans LLM
WrenAI ne produit aucun SQL.

| # | Question fermée | Si oui |
|---|-----------------|--------|
| D1 | L'objet a-t-il besoin d'un **grand modèle de langage** pour fonctionner ? | `llm/*` |
| D2 | Entraîne-t-il, sert-il, suit-il ou explique-t-il un **modèle d'apprentissage** ? | `ml/*` |
| D3 | **Stocke et interroge**-t-il des données de façon persistante ? | `database/*` |
| D4 | **Déplace ou transforme**-t-il des données destinées à une **machine** ? | `data/*` |
| D5 | Calcule-t-il des statistiques, du signal ou de l'optimisation mathématique ? | `stats/*`, `signal/*`, `math/*` |
| D6 | Fournit-il de la **capacité de calcul** ou de **stockage brut** ? | `compute/*`, `storage/*` |
| D7 | Sert-il à **exposer une application** à des utilisateurs ? | `web/*`, `ui/*` |
| D8 | Porte-t-il sur **ce qui circule entre machines** ? | `network/*` |
| D9 | Porte-t-il sur la **sécurité** ou le renseignement ? | `security/*` |
| D10 | Sert-il à **déployer ou surveiller** du logiciel en production ? | `devops/*`, `observability/*` |
| D11 | Sert-il à **fabriquer** du logiciel (écrire, tester, configurer, packager) ? | `devtools/*` |
| D12 | Produit-il un document, un média ou un dessin pour un **humain** ? | `docs/*`, `media/*`, `design/*` |
| D13 | Connecte-t-il des applications **sans code** ? | `automation/*` |
| D14 | Aucun des précédents | **arrêt — demander avant d'inventer** |

### Règles de départage du domaine

| # | Règle | Cas qu'elle résout |
|---|-------|--------------------|
| D-R1 | Le tri D1/D2 se fait sur ce dont l'objet **a besoin pour tourner**, pas sur ce à quoi il ressemble. Une bibliothèque qui inspecte des transformeurs sans appeler de LLM est `ml/*`. | TransformerLens, SAELens, nnsight, interpreto, sentence-transformers → `ml/*` |
| D-R2 | `data/*` = sortie destinée à une **machine** ; `docs/*` = sortie destinée à un **humain**. | Stirling PDF → `docs/pdf` ; docTR, PyMuPDF → `data/parsing` |
| D-R3 | Un classement **lexical** (BM25, TF-IDF) est du stockage-interrogation, pas du NLP : `database/recherche`. Le NLP commence là où il y a un modèle de langue. | bm25s, rank-bm25 → `database/recherche` |
| D-R4 | Un moteur qui **indexe et interroge** est `database/recherche`, même s'il embarque des embeddings ou un pipeline RAG : c'est le stockage qui est son point d'entrée. `database/vecteur` est réservé aux moteurs dont l'unique index est vectoriel. | Marqo, txtai, Vespa, Elasticsearch → `database/recherche` ; Qdrant, Milvus, Weaviate → `database/vecteur` |
| D-R5 | Une bibliothèque qui **cherche des hyperparamètres** est `ml/hyperopt`, même si son moteur d'exécution est distribué : le distribué est son moyen, pas son sujet. | Ray Tune → `ml/hyperopt` (et non `compute/distribue`) |
| D-R6 | Un connecteur qui **rapatrie** des lignes vers un DataFrame est `data/ingestion` ; un `database/driver` transporte du SQL sans construire de table en mémoire. | connectorx → `data/ingestion` ; psycopg2, ADBC → `database/driver` |
| D-R7 | `famille: annuaire` n'exonère pas du domaine (cf. section *famille*). Un annuaire multi-domaines prend le domaine de l'**intention de recherche** qui le fait ouvrir, et l'arbitrage s'écrit en clair dans le corps de la fiche. | public-apis → `web/api` |

### Frontières disputées, écrites une fois

- `ml/socle` (généraliste, toutes tâches, aucune hypothèse sur le type de données) **distinct de**
  `ml/tabulaire` (spécialisé données en colonnes) : scikit-learn ne suppose rien du type de
  données, XGBoost si.
- `llm/socle` (LangChain, DSPy — on **assemble**) **distinct de** `llm/agents` (on orchestre une
  boucle d'outils) et de `llm/rag` (on indexe et on récupère).
- `llm/runtime` (**servir** le modèle) **distinct de** `llm/passerelle` (**router** vers des
  fournisseurs) et de `llm/outillage` (**décider** quel modèle, sans le servir).
- `data/*` (sortie machine) **distinct de** `docs/*` (sortie humaine) — règle D-R2.
- `devtools/*` (**fabriquer** du logiciel) **distinct de** `devops/*` (le **déployer**) et de
  `observability/*` (le **surveiller** une fois déployé).
- `design/diagramme` (schémas techniques) **distinct de** `design/ui` (interfaces produit) et de
  `data/viz` (graphiques de données).
- `llm/agent-de-code` (assistants et agents de **codage**, quelle que soit leur famille : extension
  d'IDE, CLI, application, plateforme de mémoire d'agent) **distinct de** `llm/agents` (briques
  génériques d'orchestration d'agents, sans spécialisation code) et de `llm/assistant`
  (application LLM prête à déployer pour un utilisateur final non développeur).
- `database/admin` (clients et consoles d'administration de bases) **distinct de** `devtools/*` :
  le sujet est la base, pas la fabrication de logiciel.

### Sous-domaines qui prêtent à confusion

Définitions reprises du vocabulaire historique — celles qui portaient une frontière réelle et
qui survivent sous un nouveau nom. Les autres puces de l'ancienne taxonomie décrivaient des
valeurs disparues et ne sont pas reconduites.

- `database/driver` — pilote / adaptateur bas niveau d'accès à une base (DB-API 2.0, wrapper
  libpq) : psycopg2, ADBC. Distinct de `database/orm` (mapping objet) : le driver transporte le
  SQL, il n'abstrait pas le schéma. Et distinct de `data/ingestion` par D-R6.
- `data/scraping` — récupération de données depuis des **pages web** : clients HTTP furtifs
  (empreinte TLS), navigateurs headless, contournement d'anti-bot, parsing HTML. Distinct de
  `data/ingestion` (connecteurs vers des sources structurées ou des API).
- `data/parsing` — extraire du contenu **structuré pour une machine** d'un document, typiquement
  pour du RAG. Distinct de `docs/pdf` (manipuler un document pour un humain — fusion, découpe,
  rotation, signature) par D-R2.
- `data/orchestration` — orchestration de pipelines de **données** en code (DAG, dépendances,
  backfills) : Airflow, Dagster, Prefect. Distinct de `automation/no-code`, qui connecte des
  **applications** par déclencheurs et actions dans un éditeur visuel de nœuds. Et distinct de
  `data/fiabilite`, qui décrit ce qu'un pipeline doit garantir là où l'orchestrateur l'exécute.
- `data/fiabilite` — **ouvert au lot 4.** Ce qui rend une donnée digne de confiance, quel que
  soit l'outil qui la déplace : l'ordre d'assemblage et la rejouabilité (ETL/ELT, idempotence,
  backfill sans doublon), le découpage en couches de raffinage (bronze / silver / gold), les
  contrats passés au consommateur et leur vérification continue, le versionnage des jeux qui
  rend un résultat reproductible. Distinct de `data/orchestration` (l'outil qui **exécute** le
  pipeline — Airflow ne dit pas si le sink est idempotent), de `devtools/validation` (valider
  des objets dans du code Python, pas des jeux de données livrés) et de `data/format` (le
  rangement physique sur disque, qui décide de la vitesse de lecture et non de la confiance).
- `compute/a-la-demande` — capacité de calcul créée et détruite à la demande, facturée à
  l'usage : bacs à sable d'exécution de code **non fiable** (typiquement généré par un LLM,
  isolation microVM) et plateformes scale-to-zero. Distinct de `devops/conteneur` (packaging et
  déploiement d'applications de **confiance**) et de `compute/distribue` (calcul réparti sur
  plusieurs nœuds).
- `math/optimisation` — **minimiser une fonction** : le mécanisme, ses garanties et ses cas
  discrets. Descente de gradient et ses réglages, convexité, courbure, paysage de perte, plus
  la branche discrète (programmation linéaire, MIP, optimisation sous contrainte) et les
  modeleurs et solveurs qui la résolvent. Distinct de `ml/hyperopt` (chercher des
  hyperparamètres, pas minimiser une fonction connue), de `ml/*` (les modèles qui *emploient*
  la descente de gradient — la mécanique est ici, l'architecture est là-bas) et de `stats/*`
  (modélisation statistique). **Élargi au lot 4** : la valeur ne portait que la recherche
  opérationnelle tant qu'elle n'avait qu'une brique.
- `math/algebre-lineaire` — **ouvert au lot 4.** Le langage dans lequel données et modèles sont
  écrits : normes, produits matriciels, projections, décompositions (SVD, valeurs propres). Ce
  sont les objets et leurs propriétés, pas les méthodes qui s'en servent. Distinct de
  `stats/exploratoire`, qui *applique* une décomposition à un tableau de données pour en
  interpréter les axes : `SVD` est la factorisation $A = U\Sigma V^	op$, `PCA` est la méthode
  qui l'emploie — les deux pages existent, et elles ne sont pas dans le même dossier.
- `math/information` — **ouvert au lot 4.** Mesurer l'incertitude d'une loi et l'écart entre
  deux lois : entropie, entropie croisée, divergences (KL, Jensen-Shannon), information
  mutuelle, et le transport optimal avec la distance de Wasserstein qui en est la valeur.
  Rangé ici et non en `math/optimisation` alors que le transport optimal *est* un programme
  linéaire : ce que ces pages produisent est une **mesure d'écart entre distributions**, et
  c'est par là qu'on les cherche. Distinct de `stats/inference`, qui teste un écart sur un
  échantillon plutôt que de le définir.
- `math/theorie-apprentissage` — **ouvert au lot 4.** Pourquoi la généralisation est possible,
  et de quoi elle dépend : PAC learning, dimension de VC, complexité de Rademacher, bornes de
  généralisation, No Free Lunch. La valeur nomme la **théorie** et non « apprentissage » seul,
  qui à côté de `ml/*` se lirait comme apprentissage automatique. Distinct de `ml/eval`, qui
  *mesure* l'erreur d'un modèle donné là où ces pages la **bornent** a priori — et ces bornes
  sont trop lâches pour dimensionner quoi que ce soit, leur intérêt est de dire de quoi la
  généralisation dépend.
- `stats/probabilite` — **ouvert au lot 4.** Théorie des probabilités et processus aléatoires :
  théorèmes de convergence (loi des grands nombres, théorème central limite, inégalités de
  concentration) et processus (chaînes de Markov, Poisson, mouvement brownien). Distinct de
  `stats/inference`, qui *applique* ces résultats à un échantillon pour estimer un paramètre :
  le TCL justifie un intervalle de confiance, il n'en calcule pas. Rangé sous `stats/` et non
  sous `math/` parce que ces pages se justifient toutes par l'inférence — et parce que les
  quatre piliers de « Mathématiques » sont l'algèbre linéaire, l'optimisation, la théorie de
  l'information et la théorie de l'apprentissage, pas la probabilité.
- `stats/experimentation` — **ouvert au lot 4.** Concevoir une expérience contrôlée et décider
  quand l'arrêter : randomisation, réduction de variance, arrêt séquentiel, allocation
  dynamique. Distinct de `stats/inference`, qui teste une hypothèse sur un échantillon **déjà
  collecté** : ici la question porte sur le protocole de collecte, pas sur le calcul. Le
  dimensionnement d'un test (« analyse de puissance ») reste en `stats/inference` — c'est une
  propriété du test, employée aussi bien hors expérimentation.
- `stats/exploratoire` — analyse factorielle et descriptive multivariée, tradition « analyse de
  données » (Benzécri, Escofier, Pagès) : PCA, CA, MCA, FAMD, MFA, GPA, PGA, HCPC. Le but est
  d'**interpréter des axes**, pas d'alimenter un modèle en aval. Distinct de `ml/non-supervise`
  (t-SNE/UMAP, ICA, NMF, autoencodeurs), qui vise une représentation utile à une tâche. La
  frontière est réelle mais fine : les deux familles partagent le tag `dimensionality-reduction`.
  Distinct aussi de `data/eda` (profiling automatique d'un jeu de données).
- `ml/eval` — bibliothèques de **métriques** et de validation de modèles ML (accuracy, F1, BLEU,
  ROUGE). Distinct de `llm/eval` (évaluation de systèmes LLM/RAG/agents — faithfulness, scoring
  par juge) et du concept transverse porté par le tag `model-evaluation`.
- `llm/memoire` — mémoire et **contexte** persistants d'un agent : compression du contexte
  envoyé au modèle, élagage, réinjection à la demande, base de faits qui survit à la session.
  Distinct de `llm/observabilite` (mesurer ce qui est envoyé) et de `database/vecteur` (l'index
  qui la stocke éventuellement).
- `network/analyse` — observation et analyse du **trafic** (qui parle à qui, ports, protocoles,
  volumes, alertes). Distinct d'`observability/supervision`, qui instrumente des machines et des
  applications *depuis l'intérieur*.
- `network/transfert` — transfert de fichiers de machine à machine (chiffrement, relais, reprise).
- `security/recon` — reconnaissance d'une cible **depuis l'extérieur**, sans accès privilégié
  (DNS, TLS, en-têtes, technologies détectées), et **renseignement en sources ouvertes** :
  l'ancienne distinction `recon` / `osint` ne portait aucune conséquence, les deux valeurs sont
  fusionnées. Distinct du tag `ai-security` (surface d'attaque des systèmes LLM).
- `observability/supervision` — surveiller du logiciel **déployé** : métriques, journaux, état
  des machines et des conteneurs, tableaux de bord, alertes. L'ancien découpage
  `log` / `metric` / `trace` / `infra` n'a jamais dépassé une page par valeur ; il est fusionné.
  Distinct de `ml/monitoring` (dérive de modèle).
- `devtools/client-api` — clients d'API : composer, envoyer et tester des requêtes
  HTTP/REST/GraphQL/gRPC, gérer collections et environnements. Distinct de `devtools/test`
  (frameworks de test de code, type pytest).
- `docs/capture` — **capture de contenu** externe vers un format texte réutilisable : page web ou
  document converti en Markdown, à l'unité, par un geste manuel. Distinct de `data/scraping`
  (extraction programmatique et à l'échelle).
- `media/ingestion` — ingestion et traitement de médias (vidéo, audio, image) pour donner à un
  assistant IA un **input** multimodal : téléchargement, extraction de frames, transcription.
  Distinct de `media/video` (montage, production, lecture — le média est la finalité) et de
  `signal/*` (traitement du signal comme objet d'étude).

### Les 20 préfixes de tête et leur dossier

Un préfixe = un **dossier de domaine** à la racine, portant une page hub à son nom. Le libellé
vient de la table `CAT_LABEL` de `AI/scripts/build_mocs.py`, dont `DOM_LABEL` de
`AI/scripts/arbo.py` est la copie conforme — c'est cette table qui **dérive le chemin** d'une
page depuis sa `categorie:`. Un préfixe sans libellé sort en anglais capitalisé : **ajouter le
libellé dans les deux tables en même temps que le préfixe**, sinon la dérivation échoue.

`MOC/Categories/` portait ces hubs jusqu'au lot 3 ; le dossier est vide depuis, et les hubs
sont descendus dans l'arbre.

| Préfixe | Dossier de domaine | Portée |
|---------|----------------------|--------|
| `ml` | Machine Learning | entraîner, servir, suivre, expliquer un modèle |
| `llm` | LLM & IA générative | tout ce qui a besoin d'un LLM pour fonctionner |
| `database` | Bases de données | stocker et interroger de façon persistante |
| `data` | Data & pipelines | déplacer et transformer de la donnée pour une machine |
| `devtools` | Outils de développement | fabriquer du logiciel : écrire, tester, configurer, packager |
| `stats` | Statistiques & inférence | inférence, bayésien, exploratoire, causal, probabilité, expérimentation |
| `compute` | Calcul distribué | capacité de calcul : distribué, GPU, à la demande |
| `design` | Design & diagrammes | dessin pour un humain : schémas, interfaces |
| `storage` | Stockage | stockage brut d'objets |
| `web` | Web & API | exposer une application par HTTP |
| `automation` | Automatisation no-code | connecter des applications sans code |
| `media` | Médias | vidéo, audio, image pour un humain |
| `ui` | Interfaces & apps data | interfaces data et démos de modèle |
| `observability` | Observabilité | surveiller du logiciel déployé |
| `security` | Sécurité | sécurité et renseignement |
| `signal` | Signal & audio | traitement du signal, audio |
| `network` | Réseau | ce qui circule entre machines |
| `devops` | DevOps | déployer du logiciel en production |
| `docs` | Documents | produire un document pour un humain |
| `math` | Mathématiques | les quatre socles : algèbre linéaire, optimisation, théorie de l'information, théorie de l'apprentissage |

## Notions (`role: notion`) — `categorie: concept/<sous-domaine>`

```
concept/{data, ai, ml, dl, rl, ts, nlp, devops, llm}
```

- `dl` — deep learning (architectures, attention, génératif)
- `rl` — reinforcement learning
- `ts` — séries temporelles & forecasting
- `nlp` — traitement du langage naturel (TF-IDF, NER, recherche d'information)

> Dérivé du réservoir Wiki v1 + spec brain-v2 (§5.2 : `concept/data`). À valider / étendre.

**Ce vocabulaire est en train de disparaître.** Le lot 4 recatégorise les notions sur le même
vocabulaire que les briques — une notion se range par son **domaine**, comme tout le reste, et
`concept/<sous-domaine>` était le vocabulaire d'une galaxie qui n'existe plus. Une valeur est
**retirée du bloc** dès que plus aucune page ne la porte : l'y laisser autoriserait une rechute
silencieuse, puisque `check_brain` l'accepterait encore.

- `stats` — retiré le 2026-09-05, 37 notions descendues dans « Statistiques & inférence/ ».
- `math` — retiré le 2026-09-05, 26 notions descendues dans « Mathématiques/ ».
- `signal` — retiré le 2026-09-05, 5 notions descendues dans « Signal & audio/ ».

`data` **reste dans le bloc** après le lot du 2026-09-05, et c'est une exception motivée :
8 de ses 13 notions sont descendues dans « Data & pipelines/ », les 5 autres appellent un
domaine que ce lot ne traitait pas — [[Bases de données]] pour `ORM`, `Migrations de schéma`,
`Bases de données vectorielles` et `Index ANN — internes`, [[Outils de développement]] pour
`Notebooks-as-code`. Retirer la valeur les rendrait invalides sans les avoir rangées.

Les valeurs restantes suivront, une par lot de domaine.

## Skills perso (`categorie: skill/<sous-domaine>`)

> Réservé aux **skills / extensions** liés à la pratique perso (Claude Code, Obsidian, MCP). Les **outils techniques** (clients GUI, CLI, BDD, frameworks) ne sont PAS ici — ils vivent dans `Dev/` (cf. *Outils Dev* ci-dessus). Section vide en v2 tant qu'aucun skill n'est documenté.

```
skill/{documents, dev-flow, code-quality, knowledge, data, meta}
```

- `documents` — manipulation PDF, XLSX, DOCX, PPTX
- `dev-flow` — bootstrap, init, package mgmt, API SDK, GitHub
- `code-quality` — review, security, lint, refactor
- `knowledge` — Obsidian, scraping, ingestion de contenu
- `data` — accès DB, query, exploration (skills / connecteurs)
- `meta` — skills sur les skills (creator, eval, debug)

## Champ `domaines:`

Vocabulaire des grandes thématiques transverses → cf. [[themes]] (`data-sci`, `data-eng`, `mlops`, `ml-eng`, `ai-eng`).
