---
role: notion
nom: Bases graphe — modèles et langages de requête
alias: [Bases graphe : modèles et langages de requête, property graph vs RDF, Cypher GQL Gremlin, langages de requête de graphe, graphe ou relationnel]
categorie: database/graphe
domaines: [data-eng, ai-eng]
tags: [graph-db, knowledge-graph, relational, distributed]
---

# Bases graphe — modèles et langages de requête

## Aperçu

- Une base de graphe stocke des **entités** (nœuds) et des **relations** (arêtes) et répond à des **parcours** : trouver les chemins, les voisinages, les motifs. Deux modèles s'affrontent — le **graphe de propriétés** (property graph) et **RDF** — et quatre familles de langages les interrogent : Cypher, GQL, Gremlin, SPARQL.
- La question utile n'est pas « graphe ou pas graphe » mais **quel modèle, quel langage, et à quelle profondeur de relations**. Un relationnel bien indexé rivalise sur des parcours peu profonds sur un seul nœud ; l'avantage d'un moteur de graphe se joue sur les chemins de longueur variable, les motifs cycliques et la lisibilité de la requête. Les briques du brain sont dans [[Bases de graphes]] ; le comparatif est [[Comparatif - Bases graphes]].

## Concepts clés

### Deux modèles : graphe de propriétés et RDF
- **Graphe de propriétés** : nœuds et arêtes portent chacun des propriétés, et une arête a une identité propre. C'est le modèle de [[Neo4j]], [[Memgraph]], [[Apache AGE]], [[Nebula Graph]], [[JanusGraph]] et [[Dgraph]] (chacun avec ses particularités de schéma).
- **RDF** : des triplets sujet–prédicat–objet identifiés par des IRI, dans des graphes nommés. Une arête RDF n'a ni identité ni propriétés propres ; pour en attacher, il faut **réifier** la relation en nœud (Angles et al., 2017), ou, depuis RDF 1.2, utiliser des « triple terms » — RDF 1.2 n'était encore que *Candidate Recommendation* le 2026-04-07.
- **Ce que RDF apporte et que le graphe de propriétés n'a pas** : un écosystème normalisé par le W3C — SPARQL 1.1 (avec ses chemins de propriétés), SHACL pour valider des formes, OWL 2 pour raisonner sur des ontologies. Rien d'équivalent n'est normalisé du côté des graphes de propriétés.
- **Aucun moteur RDF n'est dans le brain.** Les sept briques sont toutes des graphes de propriétés ; le choix RDF se fait d'abord sur le besoin de raisonnement et de données liées, pas sur la performance.

### Quatre familles de langages
- **Cypher** : déclaratif, en ASCII-art de motifs (`(a)-[:CONNAIT]->(b)`). Décrit dans Francis et al. (SIGMOD 2018), dont l'auteur principal est chez Neo4j, comme le langage « évolutif » d'openCypher ; Cypher impose des arêtes distinctes par motif. Parlé par [[Neo4j]], [[Memgraph]] et [[Apache AGE]] — chacun avec des écarts (Memgraph documente des expressions de label et des fonctions absentes).
- **GQL** : norme ISO/IEC 39075, publiée en avril 2024 (610 pages, première édition). Elle couvre la création, l'accès, la requête et la maintenance de graphes de propriétés. openCypher déclare évoluer vers elle. Neo4j dit en couvrir la majorité des fonctions obligatoires, sans la gestion de session et de transaction ; Spanner Graph couvre GQL avec des écarts (pas de `CREATE GRAPH TYPE` exact, pas le DML de GQL).
- **Gremlin** (Apache TinkerPop, 3.8.2 au 2026-09-01) : un langage de **parcours** qui décrit *comment* marcher dans le graphe, pas le motif cherché ; c'est celui de [[JanusGraph]]. Pas d'optimiseur déclaratif : sur LDBC SNB Interactive, les systèmes TinkerPop sont les plus lents de l'étude de Pacaci et al. (jusqu'à deux ordres de grandeur contre Cypher sur Neo4j).
- **SPARQL**, et les dialectes propriétaires : AQL ([[ArangoDB]]), nGQL ([[Nebula Graph]], compatible en partie seulement avec openCypher 9), DQL et GraphQL ([[Dgraph]]).

### SQL/PGQ : le graphe dans SQL
- **SQL/PGQ** (partie 16 de SQL:2023) ajoute à SQL des vues de graphe sur un schéma relationnel et des requêtes de motifs en lecture seule. Son cœur de motifs (GPML) est **le même que celui de GQL** (Deutsch et al., SIGMOD 2022), avec les mêmes restrictions de parcours (TRAIL, ACYCLIC, SIMPLE) et le sélecteur ALL SHORTEST.
- **Implémentations** : Oracle Database propose les property graphs SQL et `GRAPH_TABLE` depuis 23ai ; DuckDB en extension communautaire (DuckPGQ), décrite comme en développement actif ; PostgreSQL 19 l'avait commité le 2026-03-16, puis **retiré le 2026-09-07** avant sa sortie, faute de confiance dans les bogues restants — le retour n'est pas daté. Pour Postgres, [[Apache AGE]] reste la voie d'extension.

### Quand un graphe bat un relationnel, et quand il ne le bat pas
- **Ne le bat pas d'office.** Dans Pacaci et al. (GRADES 2017, LDBC SNB Interactive, facteurs d'échelle 3 et 10), Postgres et Virtuoso en SQL ont les latences de lecture les plus basses, et jusqu'à un ordre de grandeur de débit d'avance en écriture. Les auteurs concluent à l'absence de supériorité nette des bases spécialisées sur un seul nœud. **Limite** : l'étude date de 2017, avec les versions d'alors.
- **Ce qui fait la différence** : les chemins de longueur variable, le plus court chemin, les motifs **cycliques** (triangles, cliques) et les jointures plusieurs-à-plusieurs. Nguyen et al. (2015) montrent que les plans de jointures deux à deux sont asymptotiquement sous-optimaux sur les motifs cycliques, et qu'un moteur relationnel à jointures « worst-case optimal » rivalise avec un système de graphe — donc l'avantage tient à l'algorithme, pas à l'étiquette « graphe ». Jin et Salihoğlu (PVLDB 2022) rendent un relationnel compétitif par des jointures prédéfinies.
- **Et les critiques vont dans les deux sens.** Les mesures récentes sont contestables : LDBC a jugé partiels les résultats publiés par TigerGraph, Oracle et Neo4j (revues rétrospectives de 2022) ; le benchmark BI de Szárnyas et al. (2022) compare un relationnel (Umbra, prototype académique) à TigerGraph, avec des précalculs et un plus court chemin pondéré écrit en SQL récursif d'environ 3 000 caractères ; l'article Kùzu (CIDR 2023), de ses propres concepteurs, juge Neo4j Community « non compétitif » sur SNB BI.

### Passage à l'échelle : le graphe se partitionne mal
- **Une coupe d'arêtes est inévitable.** Partager un graphe sur plusieurs machines sépare des arêtes de leurs extrémités ; un parcours profond paie alors des sauts réseau. Les systèmes choisissent où couper : TAO (Meta, USENIX ATC 2013) stocke une arête sur le shard de sa source, sans atomicité quand l'arête inverse vit ailleurs, et beaucoup d'objets dépassent 6 000 arêtes (donc non mis en cache) ; [[Nebula Graph]] partitionne statiquement par `vid % numParts + 1` et stocke chaque arête deux fois ; [[Dgraph]] partage par prédicat, pas par nœud, avec des jointures distribuées entre groupes.
- **Neo4j Infinigraph** (annoncé en 2025, disponibilité générale le 2026-01-27, « 100 To et plus » sans benchmark cité) ne répartit que les **propriétés** : la topologie reste sur un seul « graph shard », et il n'y a pas de rééquilibrage automatique. Les sources se contredisent : le billet de l'éditeur laisse entendre que propriétés et relations d'un nœud restent ensemble, la documentation dit que le shard de graphe ne contient aucune propriété.
- **Un nœud puissant suffit souvent.** McSherry et al. (HotOS 2015) montrent, sur d'autres systèmes que des bases de graphes, qu'un fil unique bien écrit bat des clusters entiers ; le raisonnement vaut comme garde-fou, non comme mesure sur les moteurs du dossier.

## Les maths, simplement

- **Chemin de longueur variable** : les nœuds atteignables en un nombre quelconque de sauts forment la fermeture transitive $E^{+} = E \cup (E^{+} \bowtie E)$ de la relation d'arêtes $E$. SQL la calcule par `WITH RECURSIVE`, à condition de gérer soi-même les cycles avec `UNION ALL` (clauses `CYCLE` et `SEARCH` depuis PostgreSQL 14). Un moteur de graphe fait la même chose, mais **sans écrire** la récursion.
- **Part d'arêtes coupées** par un partage aléatoire en $k$ parties égales : les deux extrémités d'une arête sont dans la même partie avec la probabilité $1/k$, donc une fraction $1 - 1/k$ des arêtes est coupée. Pour $k = 8$ : $7/8$, soit 87,5 %. Un partage qui respecte la structure du graphe fait mieux ; c'est le calcul qui montre pourquoi un partage par hachage est coûteux en sauts.
- **Doublement du stockage** : si chaque arête est stockée côté source et côté cible, comme le fait Nebula Graph, la capacité des arêtes est multipliée par 2.

## En pratique

- **Commencer par [[Postgres]].** Si les relations sont peu profondes (deux ou trois sauts) et le volume tient sur un nœud, une jointure indexée ou `WITH RECURSIVE` suffit ; passer à un graphe est une décision à justifier par des requêtes qui le demandent, pas par la forme des données.
- **Un graphe de connaissances n'est pas forcément dans une base de graphes.** [[GraphRAG]] et [[Construction de graphes de connaissances]] en ont besoin, mais les évaluations divergent : Edge et al. (2024) trouvent GraphRAG meilleur qu'un RAG vectoriel sur les questions *globales* d'un corpus d'environ un million de jetons, tandis que Xiang et al. (2025) concluent que le graphe fait souvent moins bien qu'un RAG standard en conditions réelles. Les deux dépendent de la tâche et de la taille du modèle.
- **Choisir le langage avant le moteur, quand on le peut.** Un portage entre deux dialectes voisins (Cypher, nGQL) n'est pas mécanique. Un code écrit en GQL ou en SQL/PGQ réduira le coût de sortie le jour où les moteurs l'implémenteront vraiment — ce n'est pas encore le cas de Postgres.
- **Lire la licence avant les performances.** Les bornes qui comptent on-prem sont des bornes de licence : édition Community mono-instance, binaires plafonnés, usage interne seulement. Chaque fiche du dossier les nomme.
- **Mesurer sur ses données.** Aucune source lue ne donne de comparatif audité entre les moteurs du dossier ; LDBC publie une méthode, pas un classement.

## Approches voisines & alternatives

- [[Neo4j]], [[Memgraph]], [[Nebula Graph]], [[Dgraph]], [[Apache AGE]], [[JanusGraph]], [[ArangoDB]] — les sept moteurs du dossier, ce que chacun fait et ce que sa licence permet.
- [[Comparatif - Bases graphes]] — ce qui les départage : un nœud ou un cluster, le prix d'exploitation, la licence.
- [[Bases de données]] — le domaine, et les autres familles de moteurs ; [[Postgres]] en est le défaut relationnel.
- [[GraphRAG]], [[Construction de graphes de connaissances]] — l'usage du graphe de connaissances côté LLM.
- [[Graph Neural Networks]] — l'apprentissage sur un graphe, branché sur les données stockées ici.
- **Écartés du dossier, faute d'être éprouvés** : FalkorDB (SSPL, projet de 2023 dont le moteur vient d'être réécrit en Rust) et Kùzu (dépôt archivé le 2025-10-10, forks jeunes) — mentionnés ici et dans le comparatif, sans fiche.

## Pour aller plus loin

- Angles, Arenas, Barceló, Hogan, Reutter, Vrgoč (2017) — *Foundations of Modern Query Languages for Graph Databases* — https://arxiv.org/abs/1610.06264
- Francis et al. (2018, SIGMOD 2018) — *Cypher: An Evolving Query Language for Property Graphs* — https://www.pure.ed.ac.uk/ws/files/56321692/cypher_sigmod18_crc_1.pdf
- openCypher — https://www.opencypher.org/
- Deutsch et al. (2022, SIGMOD/PODS 2022) — *Graph Pattern Matching in GQL and SQL/PGQ* — https://arxiv.org/abs/2112.06217
- ISO/IEC 39075:2024, GQL (fiche AFNOR, la page ISO n'a pas pu être ouverte) — https://www.boutique.afnor.org/en-gb/standard/iso-iec-390752024/information-technology-database-languages-gql/xs143588/417172
- Neo4j — conformité à GQL — https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/
- Google Spanner Graph — GQL et SQL/PGQ — https://docs.cloud.google.com/spanner/docs/graph/iso-standards
- Oracle — SQL property graphs — https://docs.oracle.com/en/database/oracle/property-graph/25.1/spgdg/sql-property-graphs.html
- DuckDB — requêtes de graphe (DuckPGQ) — https://duckdb.org/docs/current/guides/sql_features/graph_queries.html
- The Register (2026-09-15) — SQL/PGQ retiré de PostgreSQL 19 — https://www.theregister.com/databases/2026/09/15/postgresql-19-graph-queries-fail-the-would-you-ship-this-test/5296343
- W3C — RDF 1.1 Concepts — https://www.w3.org/TR/rdf11-concepts/ · RDF 1.2 Concepts (Candidate Recommendation) — https://www.w3.org/TR/rdf12-concepts/ · SPARQL 1.1 — https://www.w3.org/TR/sparql11-query/ · SHACL — https://www.w3.org/TR/shacl/ · OWL 2 — https://www.w3.org/TR/owl2-overview/
- Apache TinkerPop — https://tinkerpop.apache.org/
- Pacaci, Zhou, Lin, Özsu (2017, GRADES 2017) — *Do We Need Specialized Graph Databases? Benchmarking Real-Time Social Networking Applications* — https://event.cwi.nl/grades/2017/12-Apaci.pdf
- Erling et al. (2015, SIGMOD 2015) — *The LDBC Social Network Benchmark: Interactive Workload* — https://ir.cwi.nl/pub/23380
- Szárnyas et al. (2022, PVLDB 16(4)) — *The LDBC Social Network Benchmark: Business Intelligence Workload* — https://www.vldb.org/pvldb/vol16/p877-szarnyas.pdf
- LDBC — revues rétrospectives des résultats publiés — https://ldbcouncil.org/benchmarks/snb/retrospective-reviews/
- Ngo, Porat, Ré, Rudra (2012) — *Worst-case Optimal Join Algorithms* — https://arxiv.org/abs/1203.1952
- Nguyen et al. (2015) — *Join Processing for Graph Patterns: An Old Dog with New Tricks* — https://arxiv.org/abs/1503.04169
- Jin, Salihoğlu (2022, PVLDB 15(5)) — *Making RDBMSs Efficient on Graph Workloads Through Predefined Joins* — https://www.vldb.org/pvldb/vol15/p1011-jin.pdf
- Feng et al. (2023, CIDR 2023) — *Kùzu Graph Database Management System* — https://vldb.org/cidrdb/2023/kuzu-graph-database-management-system.html
- PostgreSQL — requêtes `WITH` (récursives) — https://www.postgresql.org/docs/current/queries-with.html
- Bronson et al. (2013, USENIX ATC 2013) — *TAO: Facebook's Distributed Data Store for the Social Graph* — https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf
- McSherry, Isard, Murray (2015, HotOS XV) — *Scalability! But at what COST?* — https://www.usenix.org/conference/hotos15/workshop-program/presentation/mcsherry
- Neo4j — Infinigraph, billet (2025-09-03) — https://neo4j.com/blog/graph-database/property-sharding-infinigraph/ · documentation — https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/overview/
- Nebula Graph — service de stockage — https://docs.nebula-graph.io/3.8.0/1.introduction/3.nebula-graph-architecture/4.storage-service/
- Dgraph — architecture — https://docs.dgraph.io/installation/dgraph-architecture
- Edge et al. (2024) — *From Local to Global: A Graph RAG Approach to Query-Focused Summarization* — https://arxiv.org/abs/2404.16130
- Xiang et al. (2025) — *When to use Graphs in RAG* — https://arxiv.org/abs/2506.05690

> Désaccords entre les sources, non tranchés : la date exacte de GQL (11 ou 12 avril 2024 selon les pages lues, « avril 2024 » seul chez l'AFNOR) ; ce que contient le shard de graphe d'Infinigraph (billet contre documentation) ; le gain du graphe en RAG, selon la tâche. Non vérifié : les pages ISO de 39075 et de 9075-16 (inaccessibles), la date de publication de SQL/PGQ (2023, d'après un moteur de recherche seulement), le papier de Jouili et Vansteenberghe (2013), et tout résultat LDBC audité par système — la page des résultats n'en liste pas. Écartés faute de source ouverte : aucune étude à comité de lecture sur l'usage abusif des bases de graphe, seul l'avis d'un universitaire rapporté par la presse.
