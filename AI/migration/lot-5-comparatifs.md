---
galaxie: meta
nom: lot-5-comparatifs
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 5 — Les comparatifs deviennent des pages

Effort : **une session**. 47 fichiers.

Prérequis : lot 3 fait — chaque comparatif doit savoir dans quel dossier il atterrit.

## Contexte

Un `.base` est un fichier YAML de requête : **ni frontmatter, ni corps**. Il ne peut donc ni
porter de couleur dans le graphe, ni pointer vers ce qu'il compare. Mesure au 2026-09-04 :
44 comparatifs sur 47 sont cités par une fiche, et **aucun ne cite quoi que ce soit**. Ce sont
47 culs-de-sac gris, par construction et non par négligence.

Trois ne sont cités par personne : `Détection & segmentation`, `Forecasting`,
`Suivi d'expériences ML`.

## Périmètre

- Les 47 fichiers `Dev/Patterns/Comparatif - *.base`.
- Les fiches qui les citent, pour que le lien pointe vers la page et non vers le `.base`.

**Hors périmètre** : les 5 `Pattern - *.md`, les Rules, le corps des briques.

## Décision préalable — **TRANCHÉE le 2026-09-05 : deux fichiers**

**Ne pas rouvrir.** Le test du bloc de code annoncé au lot 0 n'a **jamais été exécuté**,
et la variante à deux fichiers est celle que ce document appelle « sûre » en son
absence. La décision ouverte nº 5 du pilote est close par là même : les 47 `.base`
restent en place, chacun à côté de sa page, et la page embarque la vue par un lien
d'embed portant l'extension — syntaxe vérifiée le 2026-09-04.

Ce qui suit est conservé pour la trace du raisonnement, pas comme un choix à refaire.

Le lot 0 a testé si une requête de base s'écrit directement en bloc de code dans une page.

- **Si le test a réussi** : un seul fichier par comparatif. Le `.base` disparaît, la page
  porte la requête en bloc de code. 47 fichiers supprimés, rien à synchroniser.
- **Si le test a échoué** : deux fichiers. La page embarque la vue par `![[X.base]]`, syntaxe
  vérifiée le 2026-09-04.

Lire les *Remontées* du pilote avant de commencer. En l'absence de résultat, prendre la
version à deux fichiers, qui est sûre.

## Gabarit cible

```markdown
---
role: comparatif
nom: Comparatif - Bases vectorielles
categorie: database/vecteur
tags: [vector-db]
---

# Comparatif - Bases vectorielles

> On tranche sur : self-host possible, filtrage pendant la recherche, volume.

![[Comparatif - Bases vectorielles.base]]

## Ce qui départage

- [[Qdrant]] — filtrage payload appliqué pendant la recherche, pas après
- [[Weaviate]] — l'embedding est délégué à la base
- [[pgvector]] — le bon choix si du Postgres est déjà en place
```

La ligne d'accroche dit **le critère de décision**, pas le sujet. « On tranche sur : … » est
la formule imposée : c'est elle qui distingue un comparatif utile d'un tableau de plus.

Chaque puce de `## Ce qui départage` nomme **ce qui rend cette brique différente des autres du
tableau** — pas son pitch, qui est déjà dans la colonne du tableau. C'est la seule section où
l'on écrit une comparaison plutôt qu'une description.

## Procédure

1. Pour chaque `.base`, déterminer son dossier d'accueil depuis son filtre `categorie`.
   **Neuf comparatifs ne filtrent pas sur `categorie`** — ils passent par les tags. Leur
   dossier se pose à la main ; ils sont listés en fin de `v3-arborescence.md`.
2. Créer la page `.md` au gabarit ci-dessus, dans ce dossier.
3. Écrire la ligne « On tranche sur : … » et la section `Ce qui départage`. Cette partie se
   **lit dans les fiches comparées**, elle ne s'invente pas : chaque puce doit être vérifiable
   dans le corps de la brique correspondante.
4. Repointer les liens entrants vers la page, plus vers le `.base`.
5. Traiter les trois comparatifs orphelins : soit les citer depuis le hub de leur dossier,
   soit les signaler comme inutiles dans les *Remontées*.

## Critères d'acceptation

- [ ] 47 pages `role: comparatif`, chacune dans le dossier de son domaine.
- [ ] Chaque page porte une ligne « On tranche sur : … » et au moins deux puces liées.
- [ ] Aucun lien entrant ne pointe plus directement vers un `.base`.
- [ ] Chaque comparatif est cité par le hub de son dossier.
- [ ] `check_brain.py` au vert.

## Interdictions

- Ne pas inventer un critère de départage. S'il n'est pas dans les fiches comparées, il se
  demande — ou la puce ne s'écrit pas.
- Ne pas modifier le corps des briques comparées.
- Ne pas supprimer un `.base` tant que sa page ne fonctionne pas.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md puis AI/migration/lot-5-comparatifs.md, et vérifie les
Remontées de AI/migration/README.md pour savoir quelle variante appliquer.

Commence par les 6 comparatifs du domaine Bases de données et montre-les-moi avant
de dérouler les 41 autres.

Chaque puce de « Ce qui départage » doit être vérifiable dans la fiche de la brique
concernée : cite-moi la source quand tu me les montres. Clôture avec cloturer-brain.
```

---

# Remontées — pilote « Bases de données », 2026-09-05

Périmètre du pilote : le domaine « Bases de données » seul, 10 comparatifs sur 47.
Le reste du lot n'est pas commencé.

## 1. Le pilote porte DIX comparatifs, pas six

`brain-v3.md` §1 annonce « 6 comparatifs `.base` » pour ce domaine, et le prompt du
lot le reprend. La mesure date du 2026-09-04 : les 47 vivaient encore dans
`Dev/Patterns/`, et le décompte rattachait au domaine ceux dont la catégorie filtrée
était un `database/*`. Le lot 3 les a ensuite rangés **par leurs membres**
(remontée 16 du lot 4), et le domaine en a reçu dix. Vérifié : les dix filtrent bien
une `categorie: database/*`, aucun n'est un visiteur d'un autre domaine.

Les dix ont été faits. Six sur dix aurait laissé le domaine à moitié converti — le
pire état pour juger un gabarit, puisqu'on ne saurait pas si ce qui manque relève du
gabarit ou du reste à faire.

> **À corriger au lot 8** : le chiffre de `brain-v3.md` §1 est périmé. Ce n'est pas
> une erreur d'origine, c'est une mesure qui a survécu à la migration qui l'invalidait.

## 2. Les liens entrants ont basculé SEULS — la convention nue paie une seconde fois

Le critère d'acceptation nº 3 dit « aucun lien entrant ne pointe plus directement vers
un `.base` ». Il est rempli **sans avoir touché une seule fiche**, et l'interdiction
« ne pas modifier le corps des briques comparées » n'a donc jamais été mise à
l'épreuve.

Le mécanisme : les 44 liens entrants sont **nus** — `[[Comparatif - Bases
vectorielles]]`, jamais `[[…​.base]]`. La page créée porte le **même stem** que le
`.base` qu'elle embarque, et un lien nu vise un `.md`. Le lien pointe donc vers la
page dès qu'elle existe. Mesuré dans `liens.md` : les backlinks des dix comparatifs
sont attribués à la page.

C'est la deuxième fois que la convention de lien nu du lot 3 rembourse son coût — la
première étant les 682 fichiers déplacés sans toucher un lien. Elle avait été tenue
pour une propriété de robustesse au déplacement ; elle vaut aussi pour la
**substitution d'un fichier par un autre de même nom**, ce qui n'était pas prévu.

Même effet sur le critère nº 4 (« cité par le hub de son dossier ») : `build_mocs`
génère la section « ### Comparatifs » depuis les `.base` du dossier, avec un lien nu.
R7 est satisfaite d'office, et **aucun hub n'a été modifié par ce commit** — le
`git status` du commit des pages ne montre que 10 pages et 3 index.

> **Conséquence pour les 41 restants** : ne PAS repointer les liens entrants « au cas
> où ». Un lien repointé vers `[[X.base]]` serait une régression — il rendrait au
> `.base` un backlink que la page vient de gagner.

## 3. L'outillage ne connaissait pas `role: comparatif`, et trois défauts sur quatre
   étaient bloquants

Traités dans un commit isolé, **avant** toute page, et mesuré neutre : 149
avertissements avant comme après, les deux validateurs verts, aucun artefact modifié.

1. **R3 refusait le rôle.** `check_brain.ALLOWED` portait le commentaire « le déclarer
   avant qu'il existe inventerait un gabarit ». Il existe : quatre champs, `role`,
   `nom`, `categorie`, `tags`.
2. **Les deux résolveurs de liens déclaraient l'embed MORT.** `resolvable_names()` et
   `build_links` n'indexaient que le **stem** ; un embed porte l'extension, seule
   syntaxe qui vise un fichier non-`.md`. Les 47 embeds à venir auraient été 47
   violations dures et 47 liens non résolus. Les deux portent maintenant stem + nom
   complet, ce qui garde le test exact : un lien vers `Foo.base` ne résout que si
   `Foo.base` existe, jamais par repli sur un `Foo.md` de même stem.
3. **Une page de comparatif aurait pesé sur le seuil de promotion.** `promotions()`
   compte les pages par catégorie : convertir 47 `.base` en `.md` aurait pu promouvoir
   un sous-domaine **parce qu'on a converti un fichier**, sans qu'une brique ou une
   notion soit arrivée. La règle existait déjà, écrite en tête de `SEUIL` pour les
   vues — « un comparatif n'est pas un membre du comparatif » — mais elle ne
   s'appliquait qu'aux `.base`, qui ne sont pas des pages. Reconduite en
   `arbo.ROLES_HORS_SEUIL`.
4. **R8c ne voyait pas un embed comme une citation** (elle compare des stems, l'embed
   portait l'extension). Sans effet ici — les fiches citent déjà en nu — mais le
   défaut mordrait sur les trois comparatifs que personne ne cite.

> Le nº 3 mérite d'être retenu pour les 41 restants : il ne s'est pas déclenché ici
> par chance (aucun sous-domaine de « Bases de données » n'était à 4 pages), pas parce
> qu'il ne pouvait pas. **Le vérifier reste inutile : `ROLES_HORS_SEUIL` le rend
> impossible.** C'est le bon niveau de garantie — mécanique, pas vigilant.

## 4. La remontée 11 se rejoue au lot 5, et elle est déjà désamorcée

La remontée 11 du lot 4 prévoyait que le mécanisme d'absorption « se rejouera à
l'identique au lot 5, quand les 47 `.base` deviendront des pages `role: comparatif`
portant une `categorie:` ». C'est exact sur la prémisse : les dix pages portent bien
une `categorie: database/*` et entrent dans le champ des filtres des autres.

Mais le correctif du lot 4 les couvre déjà : les 47 filtres portent `role == "brique"`,
et un ET strict avec ce prédicat ne peut sélectionner une page `role: comparatif`.
**`mesure_membres_bases.py` renvoie un diff VIDE** sur les 47, avant/après.

C'est ce que la remontée 22 attendait : le script « est écrit pour le lot 5 », il y a
servi, il n'a rien trouvé. Le relevé se refait à chaque domaine des 41 restants —
c'est trente secondes, et c'est le seul contrôle qui voit un membre **perdu**.

Le jeu d'avertissements a lui aussi été comparé **ligne à ligne**, pas seulement en
compte : identique. C'est la règle de la remontée 11, appliquée.

## 5. Le seul arbitrage non mécanique : un comparatif qui enjambe deux catégories

`Comparatif - Bases NoSQL` réunit MongoDB (`database/document`), Redis et Cassandra
(`database/cle-valeur`). Il n'existe pas de valeur « NoSQL » dans la taxonomie, et
c'est normal : le vocabulaire range par modèle de données, pas par famille marketing.

Règle appliquée, à reprendre pour les 41 : **la `categorie:` d'un comparatif est celle
qui rassemble le plus de ses membres.** Ici `database/cle-valeur`, 2 contre 1.

Ce qui rend l'arbitrage tenable, c'est qu'il ne décide de rien d'autre : ni
`database/document` ni `database/cle-valeur` n'est promu, donc le dossier d'accueil est
le niveau du domaine dans les deux cas — et `ROLES_HORS_SEUIL` garantit que la valeur
choisie ne fera jamais franchir un seuil à l'un des deux.

> **À surveiller sur les 41** : si un comparatif enjambe deux sous-domaines dont l'un
> est promu et l'autre non, la valeur choisie décidera du DOSSIER, et la règle de
> majorité ne suffira plus — c'est la remontée 46 du lot 4 (« le dossier de ses
> membres suppose que les membres en aient un commun ») qui s'appliquera, et la place
> est alors au niveau du domaine.

## 6. Où les critères de départage se lisent, et ce que ça dit du lot 6

Les 45 puces sont toutes tirées du corps des fiches. Aucun critère n'a été inventé,
aucune puce n'a manqué de source — le cas prévu par les *Interdictions* (« s'il n'est
pas dans les fiches comparées, il se demande ») ne s'est pas produit une seule fois.

Répartition des sources sur les 45 puces, et elle est contre-intuitive :

| Section de la fiche | Puces qui s'y appuient |
|---|---|
| `## Pourquoi` | **45** — la totalité |
| `## Pièges` | **38** |
| `## Quand NE PAS l'utiliser` | **1** |

Deux faits, et le second est le plus utile.

**`## Pièges` porte 38 départages sur 45.** C'est la section que la spec v3 §6 dissout,
au motif mesuré que son contenu « est de la limite de conception recopiée de la doc, et
elle est décisionnelle ». Le pilote confirme le diagnostic **et** montre l'enjeu : ces
contenus ne sont pas à jeter, ce sont eux qui départagent. La spec le prévoit — ils
« remontent dans `## Définition` ou dans la colonne `Écarter si` ».

**`## Quand NE PAS l'utiliser` n'a servi qu'UNE fois**, alors que c'est la section dont
le nom promet le plus de départage. La raison se lit en l'ouvrant : ses puces ont la
forme « *tel besoin* → `[[Autre brique]]` ». Elles nomment **le concurrent**, jamais le
critère qui distingue la brique **courante**. Sur la fiche Qdrant, « déléguer
l'embedding à la base → [[Weaviate]] » dit ce que fait Weaviate, pas ce que fait Qdrant.
Cette section est donc une **table d'aiguillage**, pas une table de comparaison — et
c'est exactement pour ça que le comparatif ne pouvait pas se dériver mécaniquement de
son contenu.

> Ce que ça vaut pour le lot 6 : le tableau `Prendre si / Écarter si` du nouveau gabarit
> **hérite de ce défaut par construction** si l'on se contente de reformater
> l'existant — la spec impose déjà que chaque exclusion pointe vers l'alternative
> (règle dure nº 5), ce qui reconduit la forme « besoin → concurrent ». Le contenu qui
> manque pour départager est dans `## Pièges`, et c'est la section qui disparaît.

> **Instruction pour le lot 6, qui n'est pas encore écrite** : quand une fiche passera
> au nouveau gabarit, la ligne de `## Pièges` qui sert de critère dans un comparatif
> doit se retrouver dans `## Définition` ou dans `Écarter si`, **pas disparaître**. Le
> lot 5 crée ici une dépendance qui n'existait pas : un comparatif cite maintenant, en
> clair, ce que la fiche dit dans une section vouée à la dissolution.

## 7. Le pilote a coûté moins que la lecture

45 fiches lues intégralement, 10 pages écrites. Le temps est passé dans la **lecture**,
pas dans l'écriture ni dans l'arbitrage : le gabarit ne demande qu'une ligne « On
tranche sur : … » et une puce par membre, et le dossier d'accueil se dérive.

Budget pour les 41 restants, à la même densité : ~230 fiches à lire. C'est le poste
dominant et il ne se compresse pas — c'est la lecture qui produit les critères, et
c'est elle qui garantit qu'aucun n'est inventé.

> **Ce qui accélère vraiment** : un dump automatique des sections `Pourquoi`,
> `Quand NE PAS l'utiliser` et `Pièges` des membres d'un `.base`, à partir du relevé de
> `mesure_membres_bases.py`. Fait à la main ici pour les dix ; à écrire comme script si
> les 41 se font en plusieurs sessions.

## 8. Ce que ce pilote n'a PAS fait

- **Les 3 comparatifs orphelins ne sont pas traités** — `Détection & segmentation`,
  `Forecasting`, `Suivi d'expériences ML` sont hors du domaine « Bases de données ».
  L'étape 5 de la procédure les attend. Noter que la correction nº 4 de la remontée 3
  change leur cas : leur page les citera, ce qui satisfera R8c **sans** que la question
  « ce comparatif sert-il à quelqu'un ? » soit tranchée. Le faire quand même
  explicitement, sinon l'avertissement disparaîtra en silence — exactement le défaut
  que la remontée 11 décrit.
- **`role: comparatif` n'est pas dans `.obsidian/graph.json`.** La spec v3 §3 lui
  attribue le rouge ; les couleurs se posent par requête sur `role:`. À faire une fois,
  pas dix fois, donc pas ici.
- **Le champ n'est pas documenté dans `taxonomie.md`.** `role:` y est décrit avec ses
  cinq valeurs ; il en a six.
- **`enrichir-brain` ne connaît pas le rôle.** Sa table de propagation nomme « le
  comparatif du dossier » comme « le fichier `role: comparatif` du dossier » — ce qui
  devient vrai, alors que c'était un `.base` jusqu'ici. Vérifier que le skill parle
  bien de la page et non de la vue, au moment de clore le lot 5.

## Annexe — le relevé des sources, puce par puce

Chaque puce, avec la fiche et la section où son critère se lit. `P` = `## Pourquoi`,
`QNP` = `## Quand NE PAS l'utiliser`, `PG` = `## Pièges`.

**Comparatif - Bases vectorielles** — *serveur ou index embarqué, self-host ou managé,
filtrage pendant la recherche, volume*

| Puce | Source |
|---|---|
| Qdrant — filtrage payload pendant la recherche | `Qdrant.md` P (« filtres appliqués pendant la recherche, pas après ») |
| Weaviate — la base produit les embeddings, hybride dense+BM25 | `Weaviate.md` P |
| Milvus — stockage/calcul découplés, le milliard de vecteurs | `Milvus.md` P + « Quand l'utiliser » |
| Pinecone — managé propriétaire, aucun paramètre d'index | `Pinecone.md` P + PG (« la base décide ») |
| pgvector — pas de service séparé, ACID et jointures SQL | `pgvector.md` P |
| LanceDB — format Lance, multimodal, stockage objet | `LanceDB.md` P |
| Chroma — embarquée textuelle, monte mal en charge | `Chroma.md` P + PG |
| Faiss — index en mémoire, pas de métadonnées, GPU | `Faiss.md` P + PG |
| hnswlib — HNSW nu, header-only, incrémental | `hnswlib.md` P |
| ScaNN — quantification anisotrope, x86/AVX | `ScaNN.md` P + PG |
| Annoy — mmap, immuable après `build()`, maintenance | `Annoy.md` P + PG |

**Comparatif - Bases colonnes** — *un cluster ou un seul process, et la tolérance aux
écritures en place*

| Puce | Source |
|---|---|
| DuckDB — in-process, lit Parquet/CSV/JSON, borné par la machine | `DuckDB.md` P + PG |
| ClickHouse — sharding et réplication, mutations asynchrones coûteuses | `ClickHouse.md` P + PG |

**Comparatif - Bases graphes** — *le graphe tient-il sur un nœud, et à quel prix
d'exploitation*

| Puce | Source |
|---|---|
| Neo4j — Cypher, GDS, Community mono-instance, scaling vertical | `Neo4j.md` P + PG |
| Nebula Graph — trois services, Raft, partitions figées à la création | `Nebula Graph.md` P + PG |

**Comparatif - Bases NoSQL** — *ce qu'on stocke — un document, une structure en RAM, ou
un flux d'écritures massif*

| Puce | Source |
|---|---|
| MongoDB — documents BSON, `$lookup` n'est pas une jointure | `MongoDB.md` P + PG |
| Redis — tout en RAM, mono-thread, éviction, commande bloquante | `Redis.md` P + PG |
| Cassandra — sans maître, cohérence par requête, modèle par requête | `Apache Cassandra.md` P + PG |

**Comparatif - Bases temporelles** — *a-t-on déjà du Postgres, et faut-il du SQL
standard avec des jointures*

| Puce | Source |
|---|---|
| TimescaleDB — hypertable, SQL/ACID gardés, multi-nœuds déprécié | `TimescaleDB.md` P + PG |
| InfluxDB — serveur autonome, append, cardinalité = facteur de coût | `InfluxDB.md` P + PG |

**Comparatif - Migrations de schéma** — *du SQL à la main, un format abstrait portable,
ou un diff généré depuis l'ORM*

| Puce | Source |
|---|---|
| Alembic — autogénération depuis SQLAlchemy, à relire | `Alembic.md` P + PG |
| Flyway — SQL-first, à réécrire par moteur, undo payant | `Flyway.md` P + PG |
| Liquibase — changelog portable, rollback, couche en plus | `Liquibase.md` P + PG |

**Comparatif - ORM** — *le langage de la stack, et la quantité de SQL qu'on veut garder
sous la main*

| Puce | Source |
|---|---|
| SQLAlchemy — Core + ORM, migration non incluse (Alembic) | `SQLAlchemy.md` P + PG |
| SQLModel — une classe Pydantic + table, mais 0.0.x et API partielle | `SQLModel.md` P + PG |
| Prisma — le seul TypeScript, client Python communautaire | `Prisma.md` P + PG |

**Comparatif - Moteurs de recherche** — *bibliothèque ou moteur déployé, lexical ou
sémantique, ranking dans le serving ou après*

| Puce | Source |
|---|---|
| Elasticsearch — BM25 sur Lucene, pas une base primaire, JVM gourmande | `Elasticsearch.md` P + QNP + PG |
| Vespa — ranking ML dans le serving, complexité opérationnelle réelle | `Vespa.md` P + PG |
| txtai — index vecteur + SQL + graphe, single-node | `txtai.md` P + PG |
| bm25s — scores pré-calculés en matrices creuses, pas d'incrémental | `bm25s.md` P + PG |
| rank-bm25 — Python pur, dormant depuis 2022, tout en mémoire | `rank-bm25.md` P + PG |
| Marqo — embeddings intégrés, projet OSS déprécié | `Marqo.md` P + PG |

**Comparatif - Bases relationnelles** — *serveur ou fichier embarqué, un nœud ou
plusieurs, licence et écosystème*

| Puce | Source |
|---|---|
| Postgres — extensibilité (PostGIS, pgvector, TimescaleDB), VACUUM et connexions | `Postgres.md` P + PG |
| SQLite — une base = un fichier, un seul écrivain, verrou global | `SQLite.md` P + PG |
| CockroachDB — Raft, protocole filaire pg, compatibilité incomplète | `CockroachDB.md` P + PG |
| MySQL — le plus déployé, défauts historiques à forcer | `MySQL.md` P + PG |
| MariaDB — fork 100 % OSS, ColumnStore/Galera, divergence croissante | `MariaDB.md` P + PG |
| Microsoft SQL Server — le seul propriétaire, T-SQL, licence par cœur | `Microsoft SQL Server.md` P + PG |

**Comparatif - Clients de bases de données** — *un seul moteur ou tous, et le poids
qu'on accepte sur le poste*

| Puce | Source |
|---|---|
| DBeaver — universel, NoSQL en édition payante | `DBeaver.md` P + PG |
| DataGrip — complétion et refactoring d'IDE, gratuit non commercial | `DataGrip.md` P + PG |
| HeidiSQL — le plus léger, Windows seulement | `HeidiSQL.md` P + PG |
| pgAdmin — console officielle Postgres, UI web | `pgAdmin.md` P + PG |
| MySQL Workbench — le seul à faire modélisation ER et reverse engineering | `MySQL Workbench.md` P |
| MongoDB Compass — le seul à analyser le schéma, sur échantillon | `MongoDB Compass.md` P + PG |
| Redis Insight — modules JSON/Search, analyse mémoire, licence SSPL | `Redis Insight.md` P + PG |

---

# Remontées — deuxième session, 2026-09-05

Périmètre : « Machine Learning » (9 des 12 — les 3 orphelins écartés) et
« Outils de développement » (3 sur 3). **12 pages, 60 puces.** Avec le pilote,
**22 des 47** comparatifs sont des pages ; 25 restent, listés au §16.

## 9. Les trois soldes du pilote sont faits, et l'un des trois n'était pas ce qu'il disait

Traités dans un commit isolé, **avant** toute page, et mesuré neutre : 149
avertissements avant comme après, jeu identique ligne à ligne.

Le troisième surprend. Le §8 annonçait « `role: comparatif` n'est pas dans
`.obsidian/graph.json` ». Il y était déjà — la règle avait été **posée d'avance
au lot 2**, avec son rouge `#EF4444`, dans le bloc `colorGroups` de
`Documentation/perso/obsidian-graph.md`, seule source versionnée du fait que
`.obsidian/graph.json` est gitignoré. Ce qui manquait n'était pas la règle,
c'était de **retirer la phrase qui disait qu'elle ne colorait rien**. Deux rôles
y étaient encore annoncés « sans aucune page » ; `hub` en a depuis le lot 3,
`comparatif` depuis le pilote. La béquille `path:MOC/` de la règle `hub` est
tombée avec, `MOC/` étant mort à la clôture du lot 4.

> La leçon vaut au-delà du graphe : une règle posée d'avance **ne se signale
> jamais** le jour où elle commence à mordre. Elle marche, et la prose qui la
> décrit reste fausse. C'est le même mécanisme que la remontée 11 — un
> avertissement qui disparaît en silence — vu par l'autre bout.

Les deux autres soldes étaient bien tels qu'annoncés. `taxonomie.md` déclarait la
sixième valeur mais avec « à définir » en colonne `categorie:` et « aucune
page » en colonne emplacement ; elle porte désormais la règle de majorité et une
section à quatre champs. `enrichir-brain` nommait « le `.base` du dossier » comme
seul objet de propagation P3 — le skill aurait mis à jour la vue, qui se met à
jour toute seule, et sauté la seule chose à écrire à la main.

## 10. `## Quand NE PAS l'utiliser` passe de 1 puce sur 45 à 12 sur 60, et la raison invalide à moitié la remontée 6

Répartition des sources sur les 60 puces, à comparer aux 45 du pilote :

| Section de la fiche | Pilote (45) | Cette session (60) |
|---|---|---|
| `## Pourquoi` | 45 — 100 % | 60 — **100 %** |
| `## Pièges` | 38 — 84 % | 51 — **85 %** |
| `## Quand NE PAS l'utiliser` | 1 — 2 % | 12 — **20 %** |

Les deux premières lignes se reproduisent au point près : `## Pourquoi` fournit
toujours tout, `## Pièges` toujours cinq puces sur six. La troisième décuple, et
ce n'est pas du bruit d'échantillon.

La remontée 6 expliquait le 1 sur 45 ainsi : les puces de `QNP` ont la forme
« *tel besoin* → `[[Autre brique]]` », elles nomment **le concurrent** et jamais
le critère qui distingue la brique courante. C'est exact — **quand les membres
sont des substituts**. Le pilote ne comparait que ça : dix bases de données, dix
ORM, dix clients SQL. On choisit l'un *à la place* de l'autre.

Six des douze comparatifs de cette session ne sont pas de cette nature. Leurs
membres ne se remplacent pas, ils occupent des **étages différents de la même
chaîne** :

- `Gymnasium` ne remplace pas `Stable-Baselines3` : il fournit l'environnement,
  l'autre l'algorithme. La puce « Gymnasium ne fournit que les environnements »
  est dans son `QNP`, et c'est **le** départage.
- `RLax` « ne fournit ni agents, ni environnements, ni replay, ni boucle » — `QNP`
  encore, et c'est toute la différence avec `Acme`, qui le consomme.
- `Typer` déclare les commandes, `Rich` peint la sortie, et `Typer` **appelle**
  `Rich` pour son aide enrichie.
- `ONNX Runtime` « n'est qu'un moteur d'exécution », `NVIDIA Triton` est le
  serveur — qui l'utilise comme backend.

Là, nommer le concurrent **est** nommer le critère, parce que le concurrent n'en
est pas un : c'est le voisin d'étage. La forme que la remontée 6 tenait pour un
défaut est exactement adaptée à ce cas, et inadaptée à l'autre.

> **Correction à porter à la remontée 6, et instruction pour le lot 6** :
> `## Quand NE PAS l'utiliser` n'est pas une table d'aiguillage *par nature*. Elle
> l'est quand les membres sont substituables, elle est une table de comparaison
> quand ils sont complémentaires. Le tableau `Prendre si / Écarter si` du nouveau
> gabarit n'hérite donc du défaut que **sur les fiches du premier type** — et la
> règle dure nº 5 (« toute cellule `Écarter si` contient un wikilink ») est
> justement ce qu'il faut sur les fiches du second.

## 11. Un comparatif qui départage des étages a besoin d'une ligne d'accroche qui le dise

Conséquence pratique du §10, et elle touche le gabarit. La formule imposée
« On tranche sur : … » suppose un choix **entre** des options. Sur un comparatif
d'étages, elle ment si on la remplit mécaniquement : « on tranche entre Typer et
Rich » n'a aucun sens, on prend les deux.

Quatre lignes de cette session nomment donc l'**axe** plutôt que l'arbitrage :

- Frameworks CLI — « déclarer les commandes ou peindre la sortie — ce sont deux
  couches, pas deux options ».
- Reinforcement learning — « la couche dont on a besoin — l'environnement,
  l'agent tout fait ou la brique mathématique ».
- Serving de modèles — « un moteur d'exécution ou un serveur complet ».
- NLP — « l'étage de la chaîne texte qu'on outille ».

C'est toujours un critère de décision, et c'est bien ce que la spec demande : la
question « lequel ? » devient « lequel, à quel étage ? ». Le gabarit n'a pas
besoin d'être modifié, mais l'instruction si — **ne pas fabriquer une opposition
qui n'existe pas** pour honorer la formule.

## 12. Le cas que la remontée 5 avait annoncé s'est produit, et sa règle de repli est inapplicable

La remontée 5 posait la règle — la `categorie:` d'un comparatif est celle qui
rassemble le plus de ses membres — et signalait le cas à surveiller : « si un
comparatif enjambe deux sous-domaines dont l'un est promu et l'autre non, la
valeur choisie décidera du DOSSIER, et la règle de majorité ne suffira plus […]
la place est alors au niveau du domaine ».

Deux comparatifs de « Machine Learning » sont tombés dessus, en pire : les deux
sous-domaines sont **promus tous les deux**, et il y a **égalité stricte**.

| Comparatif | Membres par catégorie | Ce que la majorité donne |
|---|---|---|
| `Détection d'anomalies` | `ml/non-supervise` 1 (PyOD), `ml/series-temporelles` 1 (STUMPY) | rien — égalité |
| `Réduction de dimension` | `ml/non-supervise` 2, `stats/exploratoire` 2, `ml/socle` 1 | rien — égalité |

**Et le repli « au niveau du domaine » ne s'écrit pas.** Une page porte une
`categorie:` obligatoire (R3) dont `check_arbo` dérive le dossier, en dur. Pour
qu'une page atterrisse à la racine de « Machine Learning », il lui faut une
`categorie:` `ml/*` **non promue** : il en existe sept (`ml/embeddings`,
`ml/feature-store`, `ml/graphe`, `ml/hub`, `ml/hyperopt`, `ml/monitoring`,
`ml/orchestration`), et **aucune ne veut dire « détection d'anomalies » ni
« réduction de dimension »**. Le repli exige donc d'écrire une catégorie fausse.

C'est une contradiction réelle de la règle, et elle vient de ce que le lot 3
avait rangé ces deux `.base` à la racine du domaine **par un choix libre** — un
`.base` ne porte pas de `categorie:`, donc rien ne contraignait son chemin. Le
lot 5 supprime ce choix libre : la page en porte une, et le dossier suit.

Les deux ont donc été tranchés par la **majorité, en deux temps, et vérifiés
contre le vocabulaire** :

- `Réduction de dimension` — égalité 2-2 au niveau de la catégorie, mais pas au
  niveau du **domaine** : `ml/*` 3, `stats/*` 2. Puis à l'intérieur de `ml`,
  `ml/non-supervise` 2 contre `ml/socle` 1. Contrôle : `taxonomie.md` nomme la
  « réduction de dimension du ML — t-SNE/UMAP, manifold learning, ICA, NMF »
  dans la définition même de `ml/non-supervise`.
- `Détection d'anomalies` — égalité 1-1 indépartageable par le comptage.
  Tranché par le **vocabulaire seul** : « repérer l'anormal (outliers univariés
  et multivariés, isolement, densité locale, enveloppe) » est l'un des trois
  usages nommés de `ml/non-supervise`, et la chaîne « anomal- » n'apparaît dans
  **aucune** autre frontière de `taxonomie.md`.

Corroboration indépendante : le hub `Non supervisé.md` portait déjà, avant ce
lot, les tags `dimensionality-reduction` et `anomaly-detection`.

> **Règle à reprendre pour les 25 restants**, et à ajouter à la remontée 5 : la
> majorité se compte **par domaine d'abord, par sous-domaine ensuite**. En cas
> d'égalité qui subsiste, on tranche par les **définitions de `taxonomie.md`**,
> et on cite la phrase — jamais à l'intuition, et jamais en écrivant une
> catégorie fausse pour obtenir un dossier. Le repli « au niveau du domaine »
> n'est praticable que si le domaine offre une valeur non promue qui **dit
> vraiment le sujet** ; sinon il n'existe pas.

## 13. Un `.base` qui déménage est le seul écart que le relevé sait produire, et il faut savoir le lire

Les deux `.base` du §12 ont suivi leur page dans « Non supervisé/ » par `git mv`
— la convention est que le `.base` vit dans le dossier de ses membres, et le §10
de la spec veut que le voisinage d'une page soit `ls` de son dossier. Un `.base`
resté ailleurs que sa page ferait mentir ce `ls`.

Conséquence : `mesure_membres_bases.py` **ne renvoie pas un diff vide** sur ce
commit. Le script indexe chaque base par son chemin ; deux chemins changent,
quatre lignes de titre bougent. Ce n'est pas ce que le contrôle cherche.

Le contrôle cherche un membre **perdu**. Comparés par **nom de fichier** plutôt
que par chemin, les 47 jeux de membres sont identiques : 47 clés avant, 47 après,
mêmes clés, et **aucune base dont la liste de membres diffère d'une ligne**.
Le commit suivant (« Outils de développement ») rend, lui, un diff vide au sens
strict.

> **À retenir pour les 25** : un diff non vide n'est pas forcément une régression,
> mais il n'est **jamais** à accepter sans le rejouer par nom. La lecture par
> chemin et la lecture par nom disent deux choses différentes — l'une voit un
> déménagement, l'autre voit une perte. Seule la seconde est le contrôle.

## 14. Ce qu'un `git mv` casse et qu'aucun validateur ne voit : la phrase, pas le lien

Corollaire du §13, et c'est le point le plus transposable de la session.

Déplacer les deux `.base` n'a cassé **aucun lien** — ils sont nus, ils visent le
stem, ils résolvent depuis n'importe où (remontée 2, troisième remboursement de
la convention). Les zones AUTO des deux hubs concernés se sont régénérées seules.
Les deux validateurs sont restés verts, les 149 avertissements identiques.

Et pourtant trois phrases du vault étaient devenues fausses — dans le **corps**
des hubs, écrit à la main, hors zone AUTO :

- `Machine Learning.md` : « Cf. [[Comparatif - Réduction de dimension]], **qui
  reste ici** parce que ses membres enjambent trois dossiers. »
- `Non supervisé.md` : « Cf. [[Comparatif - Réduction de dimension]], **au niveau
  du domaine**. » — alors qu'il est maintenant dans ce dossier même.
- `Séries temporelles.md` : « l'outillage tabulaire est **au niveau du domaine**,
  cf. [[Comparatif - Détection d'anomalies]]. »

Rien ne les signale. Le lien résout, le validateur se tait, l'index est juste.
Seule une lecture les voit. Elles ont été corrigées dans un commit dédié.

> **Instruction pour les 25 restants, et au-delà** : après tout `git mv` d'une
> page ou d'une vue, chercher le nom du fichier déplacé dans tous les `.md` du
> vault et **lire les phrases**, pas seulement vérifier que les liens résolvent.
> Ce que la convention de lien nu achète en robustesse, elle le rend en silence :
> elle supprime le symptôme qui aurait attiré l'œil sur la phrase.

## 15. Les trois « orphelins » n'en sont plus, et la mesure le dit

Les trois comparatifs que le lot déclare non cités — `Détection & segmentation`,
`Forecasting`, `Suivi d'expériences ML` — n'ont pas été convertis ici, sur
consigne. Mesure faite pour l'arbitrage, et elle renverse la prémisse.

**Ils sont cités, et pas par une zone générée.** Chacun l'est deux fois par le
hub de son propre dossier : une fois dans la zone `AUTO` (que `build_mocs`
remplit depuis les `.base` du dossier, donc sans valeur de preuve), et une fois
**dans le corps écrit à la main**, section `## Choisir`, avec un motif :

| Comparatif | Citation manuscrite |
|---|---|
| `Détection & segmentation` | `Vision.md` §Choisir — « Brancher annotateurs, zones et suivi sur un modèle déjà choisi → [[supervision]]. Cf. … » |
| `Forecasting` | `Séries temporelles.md` §Choisir — « Prévoir sans entraîner de modèle par série → [[Chronos]]. Cf. … » |
| `Suivi d'expériences ML` | `Suivi d'expériences.md` §Choisir — « [[Neptune]] n'est plus un choix pour du neuf : racheté par OpenAI, service hébergé arrêté en mars 2026. Cf. … » |

Ces lignes datent des lots 3 et 4, quand `MOC/Categories/` est devenu les hubs de
l'arbre et que leur corps a été écrit. Le décompte « trois non cités » date du
2026-09-04 et n'a pas survécu à la migration qui l'a invalidé — **exactement le
même mécanisme que le « 6 comparatifs » de la remontée 1**.

Il n'y a par ailleurs **rien à arbitrer sur leur rangement** : leurs membres sont
unanimes (`ml/vision` 6, `ml/series-temporelles` 6, `ml/tracking` 7), les trois
catégories sont promues, et les trois `.base` sont **déjà** dans le dossier que
la dérivation donne. Aucun ne relève du §12. Aucun ne déclenche R8b ni R8c.

> **Ce qui reste à trancher** n'est donc pas « où les ranger » mais « les
> convertir ou non ». Ma mesure dit : les convertir comme les autres, sans clause
> particulière. Elle est posée à floSa en fin de session, pour les trois d'un
> coup.

## 16. Les 25 comparatifs restants, par domaine

| Domaine | Reste | Comparatifs |
|---|---|---|
| LLM & IA générative | 7 | Assistants de code IA · Frameworks LLM · Fine-tuning LLM · Observabilité LLM · Exécution & serving LLM · Frameworks text-to-SQL · Évaluation LLM |
| Data & pipelines | 6 | Outils EDA - profiling · Manipulation de données · Orchestrateurs data · Parsing de documents · Scraping · Visualisation |
| Machine Learning | 3 | Détection & segmentation · Forecasting · Suivi d'expériences ML — les trois du §15 |
| Design & diagrammes | 2 | Design & prototypage · Diagrammes |
| Interfaces & apps data | 2 | Apps data & démos ML · Frontends web légers |
| Automatisation no-code | 1 | Automatisation no-code |
| Calcul distribué | 1 | Calcul distribué |
| Mathématiques | 1 | Solveurs d'optimisation — **1 seul membre**, `[WARN] R8b` |
| Signal & audio | 1 | Traitement du signal |
| Statistiques & inférence | 1 | Outils stats |

Deux points de vigilance pour les sessions suivantes, tous deux déjà dans les
149 avertissements :

- `Solveurs d'optimisation` a **un membre** (PuLP). Une page à une puce n'est pas
  un comparatif — le convertir ne réglera pas `R8b`, il le rendra silencieux.
- `Frontends web légers` filtre par **liste de 5 noms codée en dur**
  (`[WARN] R8d`) : c'est le seul des 47 dans ce cas, et une brique qui entre dans
  le thème n'entrera jamais dans sa vue.

## Annexe — le relevé des sources, puce par puce (60)

`P` = `## Pourquoi`, `QNP` = `## Quand NE PAS l'utiliser`, `PG` = `## Pièges`.

**Comparatif - Boosting** — *la nature des colonnes, le temps d'entraînement, la
taille du jeu*

| Puce | Source |
|---|---|
| XGBoost — level-wise plus prudent, distribué Spark/Dask/Ray/Flink mature | `XGBoost.md` P + PG |
| LightGBM — leaf-wise + GOSS/EFB, le plus rapide, à borner par `num_leaves` | `LightGBM.md` P + PG |
| CatBoost — ordered target encoding, arbres symétriques, plus lent sur numérique | `CatBoost.md` P + PG |

**Comparatif - Reinforcement learning** — *l'étage : environnement, agent tout
fait, ou brique mathématique*

| Puce | Source |
|---|---|
| Gymnasium — le contrat `reset`/`step`, aucun algorithme, mono-agent | `Gymnasium.md` P + QNP |
| OpenSpiel — information imparfaite, CFR/MCTS/exploitabilité, API à lui | `OpenSpiel.md` P + PG |
| Stable-Baselines3 — clé en main PyTorch, et c'est le **zoo** qui fait le résultat | `Stable-Baselines3.md` P + PG |
| Acme — acteurs/learners/replay, Reverb et Launchpad Linux seulement, release 2022 | `Acme.md` P + PG |
| RLax — la couche mathématique nue : ni agents, ni env., ni replay, ni boucle | `RLax.md` P + QNP + PG |
| TF-Agents — équivalent SB3 côté TF, bandits contextuels, figé sur TF 2.15 | `TF-Agents.md` P + PG |

**Comparatif - Optimisation d'hyperparamètres** — *une machine ou un cluster, et
comment le budget d'essais se coupe*

| Puce | Source |
|---|---|
| Optuna — define-by-run et pruning, qui exige une métrique par étapes | `Optuna.md` P + PG |
| Ray Tune — enveloppe les moteurs, ajoute schedulers et reprise ; hérite de Ray | `Ray Tune.md` P + PG |
| Hyperopt — TPE historique, `SparkTrials`, rien depuis 2021, `hp.choice` = index | `Hyperopt.md` P + PG |

**Comparatif - Orchestrateurs ML** — *l'infrastructure qu'on accepte d'opérer*

| Puce | Source |
|---|---|
| Flyte — K8s-natif, tâches typées, cache ; compétence cluster exigée, SDK en bascule | `Flyte.md` P + PG |
| Metaflow — local→cloud sans réécriture, `resume` ; abouti sur AWS, sans ordonnanceur | `Metaflow.md` P + PG |
| ZenML — n'exécute rien, orchestre l'existant ; backend et serveur à opérer quand même | `ZenML.md` P + PG |

**Comparatif - Explicabilité** — *une prédiction, un modèle ou un circuit ; le
framework ; la taille du modèle*

| Puce | Source |
|---|---|
| SHAP — attributions additives qui somment, TreeSHAP exact ; KernelSHAP prohibitif | `SHAP.md` P + PG |
| LIME — surrogate local instable ; dépôt sans commit depuis juillet 2021 | `LIME.md` P + PG |
| Captum — par gradient, jusqu'au neurone et aux exemples d'entraînement (TracIn) | `Captum.md` P + QNP |
| TransformerLens — notation canonique, têtes séparées ; local et gourmand en mémoire | `TransformerLens.md` P + QNP + PG |
| nnsight — exécution différée et **distante** (NDIF) ; pas de notation canonique | `nnsight.md` P + PG |
| SAELens — le catalogue de SAE déjà entraînés, contre un entraînement cher | `SAELens.md` P + PG |
| interpreto — pipeline concept de bout en bout et scoring ; alpha en 0.5.0 | `interpreto.md` P + QNP + PG |

**Comparatif - Serving de modèles** — *moteur ou serveur, un framework ou tous,
l'infra qu'on opère*

| Puce | Source |
|---|---|
| BentoML — le Bento (modèle + code + env) ; pas le batching GPU fin de Triton | `BentoML.md` P + PG |
| NVIDIA Triton — batching dynamique et concurrence ; `model_repository` strict | `NVIDIA Triton.md` P + PG |
| KServe — `InferenceService` déclaratif, scale-to-zero ; démarrage à froid | `KServe.md` P + PG |
| Ray Serve — autoscaling et graphes **en Python** ; indissociable de Ray | `Ray Serve.md` P + PG |
| Seldon Core — graphe complet + Alibi ; **BSL depuis le 22 janvier 2024** | `Seldon Core.md` P + PG |
| TensorFlow Serving — `SavedModel` seul, mais versionnage, hot-reload, REST+gRPC | `TensorFlow Serving.md` P + PG |
| TorchServe — **dépôt archivé le 7 août 2025**, plus aucun correctif | `TorchServe.md` P + PG |
| ONNX Runtime — un moteur, pas un serveur ; fallback CPU silencieux | `ONNX Runtime.md` P + PG |
| TensorRT — moteur compilé figé sur l'architecture GPU ; calibration INT8 à valider | `TensorRT.md` P + PG |

**Comparatif - NLP** — *l'étage de la chaîne texte : découper, étiqueter, classer,
encoder, retrouver, évaluer*

| Puce | Source |
|---|---|
| sentencepiece — Unicode brut sans pré-segmentation, modèle Unigram | `sentencepiece.md` P |
| spaCy — pipeline complet et rapide ; NER borné aux types appris | `spaCy.md` P + PG |
| NLTK — corpus et lexiques, algorithmes explicites ; verbeux et lent, centré anglais | `NLTK.md` P + PG |
| GLiNER — NER zero-shot par libellés ; qualité dépendante de la formulation | `GLiNER.md` P + QNP + PG |
| pytorch-crf — une couche de sortie (Viterbi) ; release 2019, souvent optionnelle | `pytorch-crf.md` P + PG |
| SetFit — fine-tuning contrastif few-shot sans prompt ; dépassé au-delà d'un volume | `SetFit.md` P + QNP |
| sentence-transformers — bi-encoder pour indexer, cross-encoder pour le top-k | `sentence-transformers.md` P + PG |
| RAGatouille — late-interaction ColBERT, index PLAID ; rien depuis mai 2025 | `RAGatouille.md` P + PG |
| bm25s — scores pré-calculés en matrices creuses ; réindexation pour ajouter | `bm25s.md` P + PG |
| rank-bm25 — Python pur, API minimale ; tout en mémoire, dernière release 2022 | `rank-bm25.md` P + PG |
| HuggingFace — la couche au-dessus ; licences hétérogènes, « open weights » ≠ libre | `HuggingFace.md` P + PG |
| datasets — Arrow memory-mappé et `streaming` ; pas un moteur de requête | `datasets.md` P + QNP |
| evaluate — métriques versionnées sur le Hub ; LightEval prend le relais pour les LLM | `evaluate.md` P + PG |
| seqeval — score au niveau **entité**, là où `sklearn` surévalue ; release oct. 2020 | `seqeval.md` P + PG |
| interpreto — explique un LM entraîné, attributions **et** concepts ; alpha | `interpreto.md` P + QNP |
| DSPy — signatures typées, un optimiseur compile les prompts ; coûteux en tokens | `DSPy.md` P + QNP + PG |

**Comparatif - Détection d'anomalies** — *un point aberrant dans un tableau, ou
une forme inattendue dans une série*

| Puce | Source |
|---|---|
| PyOD — 50+ détecteurs pour **comparer**, ECOD/COPOD sans paramètre ; `contamination` | `PyOD.md` P + PG |
| STUMPY — matrix profile et discords ; la fenêtre `m`, et les régions plates | `STUMPY.md` P + PG |

**Comparatif - Réduction de dimension** — *axes interprétés ou variété apprise ;
voisinage local ou forme d'ensemble*

| Puce | Source |
|---|---|
| Scikit-Learn — PCA/KernelPCA/ICA/NMF dans la même grammaire ; single-node, sensible à l'échelle | `Scikit-Learn.md` P + PG |
| umap-learn — le seul manifold à `transform` des points nouveaux, et supervisable | `umap-learn.md` P + PG |
| PaCMAP — paires mid-near : global **et** local, plus robuste ; API sous la 1.0 | `PaCMAP.md` P + PG |
| Prince — toute la famille factorielle (CA, MCA, FAMD, MFA, GPA), pas que la PCA | `Prince.md` P |
| Fanalysis — les aides à l'interprétation FactoMineR ; rien depuis le 4 juin 2018 | `Fanalysis.md` P + QNP |

**Comparatif - Clients d'API** — *où vivent les collections, et le prix d'une
équipe*

| Puce | Source |
|---|---|
| Bruno — `.bru` versionnables, 100 % local ; format propre, ni mocks ni monitoring | `Bruno.md` P + PG |
| Postman — la plateforme entière ; cloud par défaut, **un seul utilisateur** en gratuit depuis mars 2026 | `Postman.md` P + QNP + PG |

**Comparatif - Frameworks CLI** — *déclarer les commandes ou peindre la sortie*

| Puce | Source |
|---|---|
| Typer — déduit la CLI des annotations de type ; redescendre à Click au besoin | `Typer.md` P + PG |
| Rich — compose la sortie, et c'est lui que Typer appelle ; couleurs coupées hors TTY | `Rich.md` P + PG · `Typer.md` PG |

**Comparatif - Gestionnaires de paquets Python** — *le dénominateur commun, ou
l'outil unique qui gère aussi lock, venv et versions de Python*

| Puce | Source |
|---|---|
| pip — volontairement minimal, donc présent partout ; ni lockfile ni isolation | `pip.md` P + PG |
| uv — absorbe sept outils, `uv.lock` et les versions de Python ; lock propre à uv | `uv.md` P + PG |
