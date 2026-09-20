---
role: notion
nom: Catalogue de données et lignage
alias: [catalogue de données, data catalog, metadata catalog, catalogue de métadonnées, lignage de données, lignage colonne, column-level lineage, glossaire métier, gestion des métadonnées]
categorie: data/catalogue
domaines: [data-eng]
tags: [data-catalog, data-lineage, data-governance]
---

# Catalogue de données et lignage

## Aperçu

- Répondre à trois questions sur une donnée — **d'où vient-elle, qui l'utilise, qui en répond** — sans dépendre de quelqu'un qui « sait ». Le catalogue tient l'inventaire et la description des jeux de données ; le lignage tient le graphe de leur fabrication ; le glossaire tient le sens métier des mots.
- Ce sont des **métadonnées**, donc une seconde donnée à produire, à tenir à jour et à héberger. Le coût de cette seconde donnée est la question centrale de la page, avant le choix d'un outil.

## Concepts clés

### Trois familles de métadonnées
- **Techniques** : schéma, types, partitions, volumétrie, format — elles se lisent dans la source, donc se collectent sans intervention humaine.
- **Métier** : description, propriétaire, domaine, sensibilité, définition d'un terme du glossaire — elles n'existent dans aucune source, quelqu'un doit les écrire.
- **Opérationnelles** : dernière exécution, fraîcheur, usage, résultats de tests — elles changent à chaque run et n'ont de valeur que fraîches.
- Le clivage qui compte : les métadonnées techniques et opérationnelles se **collectent** ; les métadonnées métier se **saisissent**. Le projet Ground (CIDR 2017) formule un besoin voisin en termes de « contexte » de la donnée — comment elle est utilisée et comment elle change — à capturer dans un modèle et une API communs.

### Catalogue, lignage, glossaire
- **Catalogue** : l'inventaire interrogeable — recherche, description, propriétaire, étiquettes. Sa question : *qu'est-ce qui existe, et qui en répond ?*
- **Lignage** : le graphe orienté des jeux de données et des traitements qui les produisent. Sa question : *d'où vient ce chiffre, et qu'est-ce qui casse en aval si ceci change ?*
- **Glossaire** : les termes métier et leur définition, rattachés aux colonnes. Sa question : *que veut dire « client actif » ?*
- Les catalogues du brain ([[OpenMetadata]], [[DataHub]]) portent les trois ; la spécification [[OpenLineage]] ne porte que la collecte du deuxième.

### Collecte tirée, collecte poussée
- **Tirée** (*pull*, crawl) : un processus interroge les sources — catalogue d'un SGBD, API d'un outil de BI — et ramène les métadonnées. Goods, le catalogue de Google, procède ainsi, *a posteriori*, sur des milliards de jeux de données produits par des équipes sans système central (SIGMOD 2016). [[OpenMetadata]] collecte par des workflows d'ingestion planifiés ; [[DataHub]] par des recettes lancées en ligne de commande ou depuis l'interface.
- **Poussée** (*push*) : l'outil qui exécute le traitement **émet** ce qu'il a lu et écrit, au moment où il le fait. [[OpenLineage]] en est la forme standardisée : des événements de run, émis au début, à la fin ou à l'échec. [[DataHub]] accepte aussi des émissions par SDK et par Kafka.
- La différence qui se paie : la collecte tirée voit ce qui *existe* mais devine ce qui *s'est passé* (par analyse des requêtes) ; la collecte poussée sait ce qui s'est passé mais **ne voit que les outils instrumentés**. Un trou d'instrumentation est un trou dans le graphe, sans erreur.
- Une lecture, à titre d'analogie : la littérature sur la provenance distingue la capture **précoce** (calculée pendant le traitement, surcoût à l'exécution) de la capture **tardive** (reconstruite à la demande, surcoût à la requête) — l'émission d'événements ressemble à la première, l'analyse de journaux à la seconde.

### Lignage table, lignage colonne
- **Table** : *ce jeu vient de ces jeux*. Suffit pour une analyse d'impact grossière (« si cette table change… »).
- **Colonne** : *cette colonne vient de celles-ci, par identité, transformation ou agrégation*. Seul niveau qui répond à « d'où sort ce chiffre » sur une table de 200 colonnes, et qui permet de suivre une donnée sensible.
- Dans la terminologie de la provenance, ce sont deux **granularités** (grossière et fine). La spécification OpenLineage distingue en plus, par la facette `ColumnLineageDatasetFacet`, les dépendances **directes** (identité, transformation, agrégation) des **indirectes** (jointure, filtre, tri, fenêtre).
- Le niveau colonne n'est pas gratuit : peu d'intégrations OpenLineage l'émettent (Spark, dbt si l'analyse est activée), [[dbt Core]] v1 ne le calcule pas seul et [[SQLMesh]] l'a en natif. Les catalogues le déduisent de l'analyse SQL, ce qui dépend du dialecte. Le détail des fonctions libres et payantes est dans [[Comparatif - Catalogues et lignage de données]].

### Ce qu'un catalogue ne remplace pas
- Un catalogue **affiche** un résultat de test ; il ne le produit pas et ne l'impose pas. Le contrat, la vérification et la fraîcheur d'un jeu vivent ailleurs : [[Contrats de données & qualité]], sans être répétés ici.
- Le lignage documente le **chemin**, pas la **couche** : ce que devient une donnée entre le brut et le consommé est dans [[Architecture médaillon]].
- Un catalogue ne corrige rien : il rend visible un défaut, il ne relance pas un pipeline.

## En pratique

- **Commencer par le lignage émis, pas par le catalogue**, quand la question urgente est « qui casse si ceci change ». Deux sources suffisent à démarrer : le fournisseur OpenLineage d'[[Airflow]] et `dbt-ol` pour [[dbt Core]] ; le catalogue s'ajoute ensuite comme récepteur.
- **Décider qui écrit les métadonnées métier avant d'installer** : un propriétaire par domaine, une règle de saisie à la création d'un jeu. Sans cela, le catalogue est un annuaire de tables sans description.
- **Mesurer l'instrumentation** : lister les traitements qui n'émettent pas (un `PythonOperator` reste une boîte noire, et la liste d'intégrations d'OpenLineage ne cite ni Prefect ni Kestra). Un graphe sans ces nœuds paraît complet.
- **Compter l'empreinte** : un catalogue est une petite plateforme — base SQL, moteur de recherche, souvent Kafka ou un orchestrateur d'ingestion. Sur site, chez un industriel, ce sont trois à cinq services de plus à sauvegarder et à mettre à jour.
- **Pièges** : traiter le catalogue comme un projet ponctuel ; associer un récepteur ancien à un client récent (OpenMetadata annonce l'intégration d'OpenLineage « jusqu'à la 1.7.0 », le client courant est en 1.53) ; croire qu'une colonne « lignée » l'est à tous les niveaux.

### Pourquoi tant de catalogues meurent
- **La part humaine ne s'automatise pas** : propriétaires, descriptions et glossaire se périment sans que rien ne casse. Les éditeurs vendent d'ailleurs, côté payant, la documentation générée par IA (Collate, DataHub Cloud) — signe que la saisie manuelle ne suit pas.
- **L'empreinte est disproportionnée au début** : une pile à héberger avant d'avoir répondu à une seule question.
- **Le projet dépend d'un sponsor.** Constaté le 2026-09-30 : Amundsen, né chez Lyft, est archivé (avis du README : inactivité, septembre 2026) et n'a plus de version depuis 2024-08 ; Marquez n'a plus de commit sur `main` depuis 2026-04-12 ; Apache Atlas est actif (2.5.0 en 2026-04, 2.6.0 en versions candidates) mais conçu pour l'écosystème Hadoop. Aucune fiche n'existe ici pour ces trois : voir le comparatif.
- **Le catalogue n'est consulté que s'il est plus rapide que de demander à un collègue.** Une recherche lente ou une description absente suffisent à lui faire perdre son usage.

## Approches voisines & alternatives

- [[Contrats de données & qualité]] — ce qui garantit la donnée, là où le catalogue la décrit.
- [[Architecture médaillon]] — les couches que le lignage traverse.
- [[Versionnage de données]] — l'état d'un jeu à un instant, l'autre moitié de la reproductibilité.
- [[Modélisation dimensionnelle]] — les faits et dimensions que le glossaire nomme.
- [[OpenMetadata]] — catalogue complet, Apache-2.0, sans Kafka.
- [[DataHub]] — catalogue orienté événements, Kafka obligatoire.
- [[OpenLineage]] — la spécification d'événements de lignage.
- [[Airflow]] et [[Dagster]] — les orchestrateurs qui émettent (Airflow par son fournisseur, Dagster par un paquet communautaire).
- [[dbt Core]] et [[SQLMesh]] — les producteurs de graphe de modèles, dont le lignage colonne.

## Pour aller plus loin

- Alon Halevy, Flip Korn, Natalya Noy, Christopher Olston, Neoklis Polyzotis, Sudip Roy, Steven Whang, *Goods: Organizing Google's Datasets*, SIGMOD 2016 — https://research.google/pubs/goods-organizing-googles-datasets/ (catalogue *a posteriori*, extraction de métadonnées à l'échelle).
- Melanie Herschel, Ralf Diestelkämper, Houssem Ben Lahmar, *A survey on provenance: What for? What form? What from?*, The VLDB Journal 26(6), 2017 — https://www.vldb.org/vldb_journal/index.php/component/article_manager/article/1431 (granularités, capture précoce et tardive).
- Joseph Hellerstein, Vikram Sreekanti, Joseph Gonzalez et al., *Ground: A Data Context Service*, CIDR 2017 — https://rise.cs.berkeley.edu/wp-content/uploads/2017/03/CIDR17.pdf (modèle et API communs pour le contexte des données).
- OpenLineage, *Overview* et *Column Level Lineage Dataset Facet* — https://openlineage.io/docs/ et https://openlineage.io/docs/spec/facets/dataset-facets/column_lineage_facet
- DataHub, *Metadata ingestion* — https://docs.datahub.com/docs/metadata-ingestion/ ; OpenMetadata, *Connectors* — https://docs.open-metadata.org/v2.0.x/connectors
- Amundsen, avis d'archivage — https://github.com/amundsen-io/amundsen (README).
