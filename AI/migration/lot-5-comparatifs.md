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
