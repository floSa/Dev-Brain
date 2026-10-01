---
role: notion
nom: Modélisation dimensionnelle
alias: [dimensional modeling, modélisation de Kimball, schéma en étoile, star schema, faits et dimensions, SCD, slowly changing dimensions]
categorie: data/fiabilite
domaines: [data-eng]
tags: [data-modeling, data-transformation, data-pipeline]
---

# Modélisation dimensionnelle

## Aperçu

- Méthode de Ralph Kimball pour organiser des données destinées à l'analyse en **tables de faits** (les mesures d'un événement métier) entourées de **dimensions** (le contexte : qui, quoi, où, quand, pourquoi, comment). Un fait relié à ses dimensions dessine, en général, une étoile.
- Elle répond à un besoin de lecture, pas d'écriture : des requêtes prévisibles pour les outils de BI, des définitions métier tenues à un seul endroit, et un vocabulaire que les analystes reconnaissent. C'est la forme classique de la couche *gold* d'une [[Architecture médaillon]].

## Concepts clés

### Quatre étapes, dans cet ordre
- Choisir le **processus métier**, déclarer le **grain**, identifier les **dimensions**, puis les **faits**. Les réponses viennent des besoins métier et de la réalité des sources, pas de la structure de l'application source (Kimball Group, *Four-Step Design Process*).

### Le grain
- Le grain dit « exactement ce que représente une ligne » de la table de faits ; Kimball en fait l'étape charnière et un « contrat » de la conception. Le **grain atomique** — le niveau le plus bas auquel le processus capte la donnée — est le point de départ recommandé.
- Deux grains différents ne cohabitent pas dans une table. C'est aussi la règle qui donne un test : une clé composite qui doit rester **unique**.

### Faits
- Un fait est une mesure, presque toujours numérique, née d'un événement observable, et non d'un rapport à produire. Quatre formes de table : **transactionnelle** (une ligne par événement), **snapshot périodique** (une ligne par période, même sans activité), **snapshot cumulatif** (une ligne par processus, mise à jour à chaque jalon — la seule dont les lignes sont mises à jour) et **sans fait** (l'événement consigne seulement que des entités se sont rencontrées).
- Additivité : un fait **additif** se somme sur toutes les dimensions, un **semi-additif** sur certaines seulement (un solde ne se somme pas dans le temps), un **non additif** (un ratio) se recalcule à partir de ses composantes additives.

### Dimensions
- **Clé de substitution** : un entier anonyme par ligne de dimension, parce que le suivi des changements crée plusieurs lignes par clé naturelle et que les sources peuvent être plusieurs.
- **Dimension dégénérée** : un identifiant sans contenu propre (un numéro de facture), gardé dans la table de faits. **Dimension à rôles multiples** : une même dimension référencée plusieurs fois (date de commande, date d'expédition), une vue par rôle. **Junk** : un flag par dimension serait un gaspillage, une seule dimension porte les combinaisons présentes. **Conforme** : des attributs de même nom et de même domaine dans plusieurs dimensions, ce qui permet de combiner des faits de tables différentes. **Table pont** : rattache une dimension multivaluée à un fait.

### Étoile contre flocon
- L'**étoile** garde chaque dimension dénormalisée en une table. Le **flocon** normalise ses hiérarchies en tables secondaires. Kimball recommande de l'éviter : difficile à comprendre pour un utilisateur métier, et il pèse sur la performance des requêtes. Les *outriggers* sont tolérés « avec modération » (Design Tip 105, Margy Ross, 2008).
- La documentation de Microsoft Fabric va dans le même sens (dimensions « presque toujours » dénormalisées) et nomme trois cas où le flocon se justifie : une dimension si grande que le stockage l'emporte sur la performance, des faits de grain supérieur qui doivent se relier à un niveau intermédiaire, un historique à suivre à un niveau plus haut.

### Slowly changing dimensions
- Que devient une ligne de dimension quand l'attribut change ? **Type 0** : jamais modifié. **Type 1** : écrasé, sans historique (les agrégats touchés sont à recalculer). **Type 2** : une **nouvelle ligne** avec une nouvelle clé de substitution ; au moins une date d'effet, une date d'expiration et un indicateur de ligne courante. **Type 3** : une colonne conserve l'ancienne valeur. **Types 4 à 7** (Design Tip 152) : mini-dimension séparée, mini-dimension avec clé courante, type 2 qui embarque aussi les attributs courants, faits portant deux clés étrangères.
- Le type 2 n'est pas gratuit : chaque fait doit pointer sur la version de la dimension en vigueur à sa date, d'où la nouvelle clé de substitution à chaque ligne.

## En pratique

- **Ce que dbt change.** Il ne pose aucune méthode, il fournit des pièces. Les **snapshots** de [[dbt Core]] implémentent le type 2 (stratégie `timestamp` ou `check`, colonnes `dbt_valid_from` et `dbt_valid_to`, `hard_deletes` depuis la 1.9) et ignorent `--full-refresh`, l'historique n'étant pas reconstructible. `dbt_utils.generate_surrogate_key` produit un **hash** déterministe de la clé naturelle, pas l'entier séquentiel décrit par Kimball, et ne gère pas seul l'historique. Les tests `unique`, `not_null` et `relationships` verrouillent le grain et les clés (`relationships` ignore les valeurs NULL : ajouter `not_null` sur la clé étrangère). Les gros faits passent en matérialisation incrémentale. [[SQLMesh]] porte le type 2 comme *kind* de modèle (`SCD_TYPE_2_BY_TIME`, `SCD_TYPE_2_BY_COLUMN`).
- **Ce que dbt ne fait pas à la place de l'équipe** : déclarer et documenter le grain (un test à écrire), créer les membres « inconnu », tenir la conformité entre dimensions. L'article de référence de la documentation dbt (Jonathan Neo, 2023) construit une étoile sur AdventureWorks et dit lui-même ne pas traiter les SCD, les lignes inconnues ni les dimensions conformes. Aucune source lue ne traite les faits arrivés en retard face à un type 2 : à traiter avec soin.
- **Avec la médaillon.** Databricks range le modèle dimensionnel dans la couche gold et précise que la médaillon est une bonne pratique recommandée, pas une obligation ; Microsoft Fabric décrit un gold « organisé pour les rapports » sans citer Kimball. Silver peut tenir un modèle proche du Data Vault. La médaillon dit **quand** raffiner, la modélisation dimensionnelle dit **comment** ranger la sortie.
- **Une seule table large** ? Des mesures publiées donnent aux tables larges un avantage de 25 à 50 % en temps de requête sur Redshift, Snowflake et BigQuery (Hightouch, 2021 ; Fivetran, 2022, pour un stockage d'environ 60 Go contre 127 Go en normalisé). Elles datent de plusieurs années, comparent l'étoile à la table unique et non le flocon à l'étoile. La conclusion la plus répandue est un compromis : l'étoile comme modèle de référence, les tables larges matérialisées en aval comme un cache (Brooklyn Data, 2025).
- Pièges : mélanger deux grains dans une table de faits ; utiliser la clé naturelle comme clé de dimension ; du type 2 partout, faute de se demander quel historique le métier lira ; un flocon par réflexe de normalisation ; des faits dont la dimension est absente, perdus par une jointure interne faute de ligne « inconnu ».

## Approches voisines & alternatives

- [[Architecture médaillon]] — les couches dont le gold porte, le plus souvent, le modèle dimensionnel.
- [[ELT vs ETL & idempotence]] — le chargement des faits et des dimensions doit pouvoir se rejouer sans doublon.
- [[Contrats de données & qualité]] — le grain, les clés et les relations se vérifient en continu.
- [[Versionnage de données]] — ne pas confondre : le type 2 historise **les valeurs d'un attribut** dans la table, le versionnage fige **un état entier** du jeu de données.
- [[Partitionnement & layout de données]] — comment ranger une grande table de faits physiquement.
- [[dbt Core]] et [[SQLMesh]] — les outils qui matérialisent faits et dimensions ; [[Great Expectations]], [[Soda Core]] et [[pandera]] vérifient les tables produites.
- Alternatives de modélisation : **Data Vault 2.0** (Dan Linstedt : hubs, links, satellites), plus adapté à l'intégration agile de sources nombreuses, avec des étoiles construites au-dessus pour le reporting ; **Inmon** (entrepôt d'entreprise normalisé, dimensionnel en aval). Le désaccord de fond, exposé côté Kimball par Margy Ross en 2004, porte sur la forme de la donnée atomique : normalisée pour Inmon, dimensionnelle pour Kimball. Un comparatif de 2026 conclut qu'aucune méthode n'est universellement meilleure : le choix dépend de l'échelle, du cadre réglementaire, de la maturité analytique et de l'investissement initial acceptable.
- Voir aussi : [[OLTP, OLAP et lakehouse]].

## Pour aller plus loin

- Kimball Group, *Dimensional Modeling Techniques* — https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/ (grain, faits, dimensions, SCD types 0 à 3).
- Margy Ross, *Design Tip 152 : Slowly Changing Dimension Types 0, 4, 5, 6, 7* (2013) — https://www.kimballgroup.com/2013/02/design-tip-152-slowly-changing-dimension-types-0-4-5-6-7/
- Margy Ross, *Design Tip 105 : Snowflakes, Outriggers, and Bridges* (2008) — https://www.kimballgroup.com/2008/09/design-tip-105-snowflakes-outriggers-and-bridges/
- Jonathan Neo, *Building a Kimball dimensional model with dbt* (2023) — https://docs.getdbt.com/blog/kimball-dimensional-model
- Documentation dbt, *Snapshots* — https://docs.getdbt.com/docs/build/snapshots
- Microsoft Fabric, *Modeling Dimension Tables in Warehouse* — https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables (le cas du flocon justifié, les colonnes d'un type 2)
- Michael Kaminsky, *One Big Table vs Star Schema* (Fivetran, 2022) — https://fivetran.com/blog/obt-star-schema
- Issar Arab, *Enterprise Data Modelling Methodologies: A Comparative Analysis of Inmon, Kimball, and Data Vault*, arXiv:2606.29355 (2026) — https://arxiv.org/abs/2606.29355
- Databricks, *Medallion architecture* — https://docs.databricks.com/aws/en/lakehouse/medallion
