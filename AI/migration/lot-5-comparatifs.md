---
galaxie: meta
nom: lot-5-comparatifs
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 5 — Les comparatifs deviennent des pages

> **CLOS le 2026-09-06.** Les 47 comparatifs sont des pages `role: comparatif`, chacune à
> côté de son `.base`, dans le dossier que `categorie:` dérive. 258 puces, toutes sourcées
> dans une fiche. Il a fallu **quatre** sessions, pas une. L'état final est au §28 ; les
> *Remontées* de la quatrième session commencent au §23.

Effort : **une session** — ~~annoncé~~, **quatre en réalité** : 10 + 12 + 12 + 13. Le poste
dominant n'est pas l'écriture mais la **lecture** des fiches comparées, et il ne se compresse
pas (remontée 7). 47 fichiers.

Prérequis : lot 3 fait — chaque comparatif doit savoir dans quel dossier il atterrit.

## Contexte

Un `.base` est un fichier YAML de requête : **ni frontmatter, ni corps**. Il ne peut donc ni
porter de couleur dans le graphe, ni pointer vers ce qu'il compare. Mesure au 2026-09-04 :
44 comparatifs sur 47 sont cités par une fiche, et **aucun ne cite quoi que ce soit**. Ce sont
47 culs-de-sac gris, par construction et non par négligence.

~~Trois ne sont cités par personne : `Détection & segmentation`, `Forecasting`,
`Suivi d'expériences ML`.~~ — **mesure du 2026-09-04, fausse depuis les lots 3 et 4.** Les
trois sont cités, chacun deux fois par le hub de son propre dossier, dont une fois dans le
corps écrit à la main. Cf. remontée 15. Le chiffre est barré ici plutôt que corrigé
silencieusement : c'est à cet endroit précis qu'une session neuve le lisait en premier.

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

## Critères d'acceptation — **les cinq sont remplis au 2026-09-06**

- [x] **47 pages `role: comparatif`**, chacune dans le dossier de son domaine. Vérifié
      mécaniquement : 47 `.base`, 47 `.md`, aucun `.base` sans page ni page sans `.base`, et
      `check_arbo` vert — donc chemin et `categorie:` concordent sur les 47.
- [x] **Chaque page porte une ligne « On tranche sur : … »** et au moins deux puces liées —
      **sauf une**, et elle est documentée : `Comparatif - Solveurs d'optimisation` n'a
      qu'un membre, donc qu'une puce. Ce n'est pas un manquement de la conversion mais un
      trou du vault, dit dans la page et ouvert au backlog (remontée 24).
- [x] **Aucun lien entrant ne pointe vers un `.base`** — rempli sans toucher une fiche, les
      liens entrants étant nus (remontée 2). Contrôlé une dernière fois : `build_links`
      annonce 0 lien non résolu sur 764 pages.
- [x] **Chaque comparatif est cité par le hub de son dossier** — `R8c` n'est émis pour aucun
      des 47.
- [x] **`check_brain.py` au vert**, et `check_arbo.py` avec lui — les deux, jamais l'un sans
      l'autre. 149 avertissements du début à la fin du lot, jeu identique ligne à ligne.

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

> **Périmé depuis la troisième session (2026-09-05)** : douze de ces 25 sont faits,
> il en reste **13**. La liste à jour est au §22. Ce tableau est conservé pour la
> trace, pas pour être lu comme l'état courant — c'est le défaut de la remontée 9,
> et il se signale ici plutôt que d'attendre qu'on le découvre.

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

---

# Remontées — troisième session, 2026-09-05

Périmètre : « Machine Learning » (les 3 derniers), « LLM & IA générative » (7 sur 7)
et « Design & diagrammes » (2 sur 2). **12 pages, 83 puces, 57 fiches lues.** Avec
les deux sessions précédentes, **34 des 47** comparatifs sont des pages ; 13 restent,
listés au §22.

## 17. Les trois « orphelins » sont convertis, et la mesure du §15 a tenu

floSa a tranché sur la mesure : les convertir comme les autres, sans clause
particulière. Rien ne s'est passé — et c'est le résultat. Les trois `.base` étaient
déjà dans le dossier que la dérivation donne, leurs membres sont unanimes, aucun
`git mv`, aucun `R8b` ni `R8c` touché. Le domaine « Machine Learning » est clos,
12 sur 12.

Ce que ça confirme rétrospectivement : le décompte « trois non cités » du 2026-09-04
n'a jamais décrit qu'un état de la v2. Les lots 3 et 4 l'ont invalidé en écrivant le
corps des hubs, et rien dans le vault ne l'a signalé — le chiffre est resté dans
`Contexte`, en tête du fichier de lot, à l'endroit exact où une session neuve le lit
en premier. Comme le « 6 comparatifs » de la remontée 1. C'est la troisième
occurrence du même mécanisme en trois sessions, et elle mérite d'être nommée pour ce
qu'elle est : **un chiffre mesuré ne porte pas sa date de péremption, donc personne
ne la voit passer.**

> **Conséquence appliquée ici** : le §16 porte maintenant une note qui dit qu'il est
> périmé et où lire la suite. Ça coûte quatre lignes et ça supprime le piège pour la
> session suivante.

## 18. Le §12 s'est rejoué, et cette fois la règle a suffi — c'est le repli qui n'existait pas

`Comparatif - Frameworks LLM` enjambe quatre sous-domaines : `llm/agents` 9,
`llm/rag` 3, `llm/sortie-structuree` 3, `llm/socle` 2. Aucune égalité — **majorité
stricte, 9 sur 17**, et même majorité absolue. La règle de la remontée 5 tranche
seule, sans passer par les définitions de `taxonomie.md`.

L'intérêt du cas n'est pas là. Il est que le lot 3 avait explicitement décidé
**l'inverse**, et l'avait écrit dans `v3-arborescence.md` : « ses membres enjambent
quatre sous-domaines dont un non promu, il **reste** au niveau du domaine ». Cette
décision était valide au lot 3 et l'est restée jusqu'à ce commit, pour la raison que
le §12 donne déjà : **un `.base` ne porte pas de `categorie:`, donc rien ne
contraignait son chemin.** Le lot 5 supprime ce choix libre. La phrase a été corrigée
avec son motif, pas effacée.

Une tentation à écarter, parce qu'elle s'est présentée : `llm/socle` est une valeur
**non promue** dont la définition — « LangChain, DSPy — on assemble » — dit assez
bien le sujet du comparatif, et l'aurait laissé au niveau du domaine. Ç'aurait été le
repli du §12. Mais le §12 réserve ce repli au cas d'**égalité qui subsiste**, et il
n'y en a pas ici. Choisir `llm/socle` contre une majorité de 9 aurait été un choix
libre réintroduit sous couvert de règle.

> **À ajouter à la remontée 5** : la majorité, quand elle existe, ne se renégocie pas
> au motif que la valeur minoritaire « dit mieux le sujet ». Le précédent est
> `Bases NoSQL` — `database/cle-valeur` pour un comparatif qui contient MongoDB.
> Écrire la catégorie de la majorité est exactement ce que la règle demande, y compris
> quand elle n'est vraie que de la majorité.

## 19. Le §14 mord hors des hubs, et le seul détecteur est le nom du fichier

Le `git mv` du §18 n'a cassé aucun lien — nus, ils résolvent depuis n'importe où,
quatrième remboursement de la convention. Les zones AUTO des deux hubs se sont
régénérées seules, les deux validateurs sont restés verts, les 149 avertissements
identiques.

Et deux phrases sont devenues fausses, dont une **hors de l'arbre des domaines** :

- `AI/design/v3-arborescence.md` — la décision du lot 3 citée au §18.
- `INSTALL.md` §14a — « Ouvre `LLM & IA générative/Comparatif - Frameworks LLM.base` »,
  l'instruction qui sert à vérifier qu'Obsidian rend bien les Bases sur un poste neuf.
  **Ce n'est pas un wikilink, c'est un chemin dans une phrase.** Aucun validateur ne le
  regarde : `check_brain` ne lit pas `INSTALL.md`, et un chemin entre accents graves
  n'est pas un lien à résoudre.

Le §14 disait « chercher le nom du fichier déplacé dans tous les `.md` du vault ».
Cette session précise le périmètre : **tous les `.md` du dépôt**, pas du vault —
`INSTALL.md`, `AI/design/`, `AI/migration/` compris. Et le motif de recherche est le
**nom du fichier**, jamais le lien : c'est précisément parce que le lien nu résiste
que seul le nom trouve les phrases qui, elles, ne résistent pas.

## 20. `## Quand NE PAS l'utiliser` sert 15 fois sur 83, et ce n'est pas la substituabilité qui décide

Répartition des sources sur les 83 puces, à comparer aux deux sessions précédentes :

| Section de la fiche | Pilote (45) | 2ᵉ session (60) | Cette session (83) |
|---|---|---|---|
| `## Pourquoi` | 45 — 100 % | 60 — 100 % | 83 — **100 %** |
| `## Pièges` | 38 — 84 % | 51 — 85 % | 78 — **94 %** |
| `## Quand NE PAS l'utiliser` | 1 — 2 % | 12 — 20 % | 15 — **18 %** |

`## Pourquoi` fournit tout, pour la troisième fois. `## Pièges` monte à 94 %, et
l'écart s'explique par le §21 : ce lot-ci compare beaucoup de briques dont le critère
décisif est un fait de licence ou de cycle de vie, et ces faits vivent dans `Pièges`.
La troisième ligne se stabilise autour de 20 %, ce qui confirme que le 1 sur 45 du
pilote était l'exception et non la règle.

Mais la raison avancée au §10 ne tient pas telle quelle. Le §10 opposait membres
**substituables** (QNP = table d'aiguillage, inutilisable) et membres
**complémentaires** (QNP = table de comparaison, utile). J'ai relu les 15 puces :
**aucune** n'est une redirection « besoin → concurrent ». Les 15 énoncent une **borne
dure de la brique elle-même** — une plateforme non supportée (Maka sous Linux,
ai-memory sous Windows natif), une licence (Phoenix en ELv2 face à une exigence OSI,
swarm-forge sans licence du tout), un périmètre revendiqué (needle qui ne fait pas de
chat, Aim qui ne fait pas de registre, smolagents dont l'exécuteur n'est pas une
frontière de sécurité), une condition d'emploi (DSPy sans métrique, Outlines derrière
une API fermée sans logits), ou un aveu (Penpot, dont la fiche écrit que la maturité
de Figma reste devant).

Et ces 15 puces se répartissent **des deux côtés** de la dichotomie du §10 : Penpot et
Figma sont des substituts purs, Maka et needle sont des voisins d'étage.

> **Correction à porter au §10, et instruction pour le lot 6** : ce qui rend une puce
> de `QNP` utilisable n'est pas la nature du voisinage, c'est sa **forme**. Une puce
> qui énonce une limite de la brique **courante** départage ; une puce qui redirige
> vers un concurrent ne départage rien, quel que soit le type de comparatif. Le
> tableau `Prendre si / Écarter si` du nouveau gabarit hérite donc du défaut par la
> règle dure nº 5 elle-même — « toute cellule `Écarter si` contient un wikilink »
> impose la redirection, donc pousse vers la forme qui ne départage pas. **La règle
> nº 5 est à relire au lot 8** : ce qu'elle devrait exiger, c'est que la cellule
> énonce la limite *et* nomme l'alternative, pas qu'elle se réduise à l'alternative.

## 21. Onze critères décisifs sur 83 ne sont pas techniques — et c'est ce que le tableau ne peut pas dire

Fait mesuré sur les 57 fiches lues, et il n'apparaît pas à cette densité dans les
sessions précédentes. Pour **onze** briques — une puce sur sept — ce qui les départage
est d'abord un fait de licence ou de cycle de vie :

| Brique | Le fait qui départage | Où il se lit |
|---|---|---|
| Neptune | racheté par OpenAI, service arrêté le 5 mars 2026 | P + PG |
| Helicone | racheté par Mintlify le 3 mars 2026, maintenance mode | P + PG |
| Vanna | dépôt OSS archivé le 29 mars 2026 | P + PG |
| AutoGen | en maintenance depuis fin 2025, trois projets coexistent | P + PG |
| Semantic Kernel | remplacé par Microsoft Agent Framework | P + PG |
| RAGatouille | 0.0.9.post2 en mai 2025, aucun commit depuis | P + PG |
| swarm-forge | **aucune licence déclarée** — aucun droit d'usage | QNP + PG |
| Ultralytics YOLO | AGPL-3.0, oblige à ouvrir le code appelant | PG |
| text-generation-webui | AGPL-3.0, copyleft fort | P + PG |
| Phoenix Arize | ELv2 *source-available*, pas OSI | P + QNP + PG |
| LangGraph | lib MIT, `langgraph-api` / Platform non | PG |

Deux enseignements.

D'abord, **c'est exactement ce qu'un comparatif doit porter et qu'un tableau `.base`
ne peut pas** : la vue affiche `licence_type: open-source` pour text-generation-webui
comme pour Excalidraw, et `maturite: production` pour Neptune comme pour MLflow. La
colonne dit vrai et ne dit rien. La puce, elle, dit qu'on ne démarre pas un projet sur
Neptune. C'est la première justification **mesurée** du lot 5 depuis son ouverture —
la page n'apporte pas seulement des liens sortants et une couleur, elle porte le
critère que le tableau efface.

Ensuite, **ces faits périment**. Onze puces datées dans un vault qui n'a aucun
mécanisme de fraîcheur, c'est onze dettes à échéance inconnue. Le brain porte déjà
`AI/scripts/verifier_fraicheur.py` ; il n'est pas branché sur les pages de comparatif,
et il devrait l'être — sujet pour le lot 8, pas pour ici.

## 22. Les 13 comparatifs restants, par domaine

> **Périmé depuis la quatrième session (2026-09-06)** : les 13 sont faits, il n'en reste
> **aucun**. L'état final est au §26. Ce tableau est conservé pour la trace, comme le §16 —
> et la note est posée ici pour la même raison qu'au §16 : un chiffre mesuré ne porte pas sa
> date de péremption (remontée 17).

| Domaine | Reste | Comparatifs |
|---|---|---|
| Data & pipelines | 6 | Outils EDA - profiling · Manipulation de données · Orchestrateurs data · Parsing de documents · Scraping · Visualisation |
| Interfaces & apps data | 2 | Apps data & démos ML · Frontends web légers |
| Automatisation no-code | 1 | Automatisation no-code |
| Calcul distribué | 1 | Calcul distribué |
| Mathématiques | 1 | Solveurs d'optimisation — **1 seul membre**, `[WARN] R8b` |
| Signal & audio | 1 | Traitement du signal |
| Statistiques & inférence | 1 | Outils stats |

Les deux points de vigilance du §16 sont intacts et n'ont pas été touchés, sur
consigne :

- `Solveurs d'optimisation` a **un membre** (PuLP). Le convertir ne réglera pas `R8b`,
  il le rendra silencieux.
- `Frontends web légers` filtre par **liste de 5 noms codée en dur** (`[WARN] R8d`),
  seul des 47 dans ce cas.

Cinq de ces sept domaines n'ont qu'un ou deux comparatifs : la contrainte « un domaine
ne se coupe pas en deux », qui a dicté l'ordre des trois sessions, ne contraint plus
rien. La dernière session peut tout prendre.

## Annexe — le relevé des sources, puce par puce (83)

`P` = `## Pourquoi`, `QNP` = `## Quand NE PAS l'utiliser`, `PG` = `## Pièges`.

**Comparatif - Détection & segmentation** — *l'étage de la chaîne vision, puis temps
réel, modularité ou segmentation sans classes*

| Puce | Source |
|---|---|
| Ultralytics YOLO — un étage temps réel, une API pour quatre tâches, export edge ; AGPL-3.0 | `Ultralytics YOLO.md` P + PG (« intégrer YOLO dans un service distribué peut obliger à ouvrir tout le code appelant ») |
| Detectron2 — implémentations de référence, architecture modulaire, précision plutôt que latence ; installation fragile, Windows limité | `Detectron2.md` P + PG |
| segment-anything — promptable zero-shot ; **ne classe pas**, encodeur ViT lourd | `segment-anything.md` P + PG (« SAM ne classe pas les masques ») |
| supervision — model-agnostic, `Detections` + ByteTrack + zones ; **ne fait pas d'inférence** | `supervision.md` P + PG |
| albumentations — propage la transformation aux boîtes/masques/keypoints ; CPU et NumPy HWC, hors autograd | `albumentations.md` P + QNP (« augmentation sur GPU et différentiable → Kornia ») + PG |
| OpenCV — vision classique et géométrie, cœur C++ ; ni batch ni GPU ni autograd, **BGR** | `OpenCV.md` P + PG |

**Comparatif - Forecasting** — *un modèle par série, un modèle global, ou aucun*

| Puce | Source |
|---|---|
| statsforecast — AutoARIMA/AutoETS compilés Numba, Spark/Dask/Ray ; format long strict, premier appel = compilation | `statsforecast.md` P + PG |
| pmdarima — `auto.arima` en enveloppant statsmodels ; un ajustement par série, non vectorisé | `pmdarima.md` P + PG (« lenteur dès que les séries se multiplient ») |
| Prophet — additif interprétable (ruptures, Fourier, fériés) ; un modèle = une série, demande intermittente exclue | `Prophet.md` P + PG + QNP |
| darts — API unique de l'ARIMA aux réseaux ; tout via `TimeSeries`, past/future covariates | `darts.md` P + PG |
| neuralforecast — 30+ architectures récentes, `Auto*` via Ray/Optuna ; perd sur petits jeux | `neuralforecast.md` P + PG |
| Chronos — modèle de fondation zero-shot, Chronos-2 multivarié ; ne bat pas toujours un modèle dédié, fuite de pré-entraînement | `Chronos.md` P + PG |

**Comparatif - Suivi d'expériences ML** — *où partent les données, et jusqu'où va
l'outil au-delà des courbes*

| Puce | Source |
|---|---|
| MLflow — registre de modèles ouvert, Linux Foundation ; **aucune authentification** par défaut, `mlruns/` qui grossit | `MLflow.md` P + PG |
| Aim — léger, self-host, UI sur des centaines de milliers de runs ; pas de registre ni RBAC, runs sur le disque du serveur | `Aim.md` P + QNP + PG |
| ClearML — données, pipelines, **agents et queues**, capture sans modifier le code ; ES+Mongo+Redis à opérer, autocapture bavarde | `ClearML.md` P + PG |
| Weights & Biases — Sweeps intégrés, Reports ; cloud par défaut, mode *online* bloquant, coût au volume | `Weights & Biases.md` P + PG |
| Comet — tracking **et** observabilité LLM via Opik ; cœur propriétaire, Opik seul open-source | `Comet.md` P + PG |
| TensorBoard — visualiseur d'*event files* : graphe, histogrammes, projecteur, profilage ; comparaison limitée, pas d'auth | `TensorBoard.md` P + QNP + PG |
| Neptune — racheté par OpenAI (déc. 2025), service hébergé arrêté le 5 mars 2026 | `Neptune.md` P + PG |

**Comparatif - Observabilité LLM** — *proxy ou SDK OpenTelemetry, et la licence qui
décide du self-host*

| Puce | Source |
|---|---|
| Langfuse — cœur **MIT**, quatre piliers unifiés ; open-core `ee/`, self-host ClickHouse+Postgres+Redis | `Langfuse.md` P + PG |
| Phoenix Arize — natif **OpenTelemetry/OpenInference**, un conteneur ; **ELv2 ≠ OSI** | `Phoenix Arize.md` P + QNP + PG |
| LangSmith — propriétaire, intégration LangChain/LangGraph la plus serrée ; self-host réservé à l'entreprise | `LangSmith.md` P + PG |
| Helicone — **mode proxy**, une ligne, cache et rate-limiting ; chemin critique, maintenance mode depuis Mintlify (3 mars 2026) | `Helicone.md` P + PG |

**Comparatif - Évaluation LLM** — *la sortie ou les étapes internes, en CI, en YAML ou
en instrumentant*

| Puce | Source |
|---|---|
| Ragas — retrieval et génération mesurés séparément, métriques sans référence, jeux de tests synthétiques ; API 0.x remaniée | `Ragas.md` P + PG |
| DeepEval — « pytest des LLM », 50+ métriques (RAG, agents, sécurité), G-Eval | `DeepEval.md` P |
| promptfoo — YAML déclaratif, matrice de comparaison, **red-teaming** 50+ types ; racheté par OpenAI (mars 2026) | `promptfoo.md` P |
| TruLens — évalue **en instrumentant**, feedback functions par étape, socle Snowflake ; n'est pas une plateforme de monitoring | `TruLens.md` P + PG |

**Comparatif - Fine-tuning LLM** — *écrire la boucle ou la déclarer, et le matériel
visé*

| Puce | Source |
|---|---|
| TRL — un trainer par méthode, le niveau code, base des outils config-driven ; API en évolution rapide | `TRL.md` P + PG |
| Axolotl — un seul YAML versionnable, DeepSpeed/FSDP à la config ; surface de config vaste, échec sans erreur claire | `Axolotl.md` P + PG |
| LLaMA-Factory — 100+ familles **dont des VLM**, interface web LLaMA Board ; largeur ≠ profondeur | `LLaMA-Factory.md` P + PG |
| Unsloth — kernels Triton, ~2× et 70-80 % de VRAM en moins, un GPU grand public ; multi-GPU bridé en OSS | `Unsloth.md` P + QNP + PG |
| Tunix — pendant **JAX/TPU** de TRL, RL agentique, rollouts vLLM/SGLang-JAX ; avantage TPU seulement, 0.1.x | `Tunix.md` P + QNP + PG |

**Comparatif - Frameworks text-to-SQL** — *schéma physique ou couche sémantique,
brique ou UI d'équipe*

| Puce | Source |
|---|---|
| WrenAI — **MDL**, couche sémantique versionnée avec RLAC/CLAC ; investissement à écrire et maintenir | `WrenAI.md` P + PG |
| Vanna — entraîné sur DDL + doc + paires, agnostique base et LLM, **Ollama** local ; dépôt archivé le 29 mars 2026 | `Vanna.md` P + PG |
| DB-GPT — multi-agent, langage AWEL, **fine-tuning Text2SQL** ; coût conceptuel élevé | `DB-GPT.md` P + PG |
| LangChain SQL agent — assemblage `SQLDatabase` + toolkit + boucle de correction ; à maintenir, pas de couche sémantique | `LangChain SQL agent.md` P + PG |
| LlamaIndex NLSQLTableQueryEngine — query engine qui synthétise la réponse, `SQLTableRetrieverQueryEngine` pour les gros schémas | `LlamaIndex NLSQLTableQueryEngine.md` P |

**Comparatif - Exécution & serving LLM** — *le poste ou la charge, puis le matériel et
la forme livrée*

| Puce | Source |
|---|---|
| llama.cpp — ggml, **GGUF**, quantization agressive, dépendances minimales ; backends GPU à compiler | `llama.cpp.md` P + PG |
| Ollama — une commande, registre, Modelfiles, API OpenAI-compatible ; Q4 par défaut, bascule RAM silencieuse | `Ollama.md` P + PG |
| LM Studio — GUI, backend **MLX** sur Apple Silicon ; **application propriétaire** | `LM Studio.md` P + PG |
| text-generation-webui — **backends commutables sans redémarrage** (GGUF/GPTQ/EXL2) ; **AGPL-3.0**, choix du loader | `text-generation-webui.md` P + PG |
| vLLM — **PagedAttention**, continuous batching ; préallocation VRAM surprenante | `vLLM.md` P + PG |
| SGLang — **RadixAttention**, préfixes partagés réutilisés ; gain proportionnel au partage | `SGLang.md` P + PG |
| TGI — routeur **Rust**, moteur des Inference Endpoints ; épisode de licence **HFOIL** mi-2023 → début 2024 | `TGI.md` P + PG |
| TensorRT-LLM — moteur **compilé**, FP8/FP4 Blackwell ; un build par modèle/GPU/précision, verrou NVIDIA | `TensorRT-LLM.md` P + PG |
| needle — **modèle** de 45 M dans 14 Mo, JSON garanti par grammaire, 256 tokens glissants | `needle.md` P + QNP (« conversation, rédaction, raisonnement : hors périmètre ») |

**Comparatif - Assistants de code IA** — *écrire, dire quoi écrire, superviser, ou
fournir le contexte*

| Puce | Source |
|---|---|
| Aider — terminal, **commit git atomique** par édition, repo map ; tout passe par git, coût de la repo map | `Aider.md` P + PG |
| Cline — boucle **Plan/Act**, **MCP de première classe** ; surface d'exécution élargie par les serveurs tiers | `Cline.md` P + PG |
| Continue — seul à faire de l'**autocomplétion inline**, BYOM ; plugin JetBrains en maintenance communautaire | `Continue.md` P + PG |
| pi — **llama.cpp citoyen de première classe** ; **aucun système de permissions** | `pi.md` P + PG |
| freebuff — ni clé API ni paiement, financé par la publicité ; prompts et contenu collé analysés, sessions plafonnées | `freebuff.md` P + PG |
| Spec Kit — **spec-driven development**, constitution de principes ; garbage-in, l'effort se déplace en amont | `Spec Kit.md` P + PG |
| BMAD — rôles agiles nommés, **stories** en chat neuf ; v4 et v6 incompatibles | `BMAD.md` P + PG |
| i-have-adhd — dix règles de sortie, rien à exécuter ; effet **nul sur la justesse** | `i-have-adhd.md` P + PG |
| t3code — **plan de contrôle**, ne parle à aucun LLM ; qualité et coût = ceux de la CLI sous-jacente | `t3code.md` P + PG |
| swarm-forge — tmux, un **git worktree** par agent, handoffs à porte d'audit ; **aucune licence déclarée** | `swarm-forge.md` P + QNP + PG |
| Maka — journal **append-only** rejouable, permissions tracées ; **Linux non supporté**, aucune release ASF | `Maka.md` P + QNP + PG |
| Graphify — knowledge graph du dépôt (Tree-sitter, Leiden, god nodes) ; artefact à régénérer | `Graphify.md` P + PG |
| ai-memory — wiki markdown **versionné par git**, relais d'une CLI à l'autre ; Windows natif expérimental | `ai-memory.md` P + QNP |

**Comparatif - Frameworks LLM** — *la couche qu'on importe : assembler, orchestrer,
récupérer, contraindre*

| Puce | Source |
|---|---|
| LangChain — interfaces standardisées, catalogue d'intégrations ; abstractions qui masquent les prompts réels | `LangChain.md` P + PG |
| DSPy — signatures typées, **optimiseur qui compile les prompts** ; sans métrique il perd son intérêt, coût en tokens | `DSPy.md` P + QNP + PG |
| LangGraph — **graphe cyclique à état persisté**, checkpoints, human-in-the-loop ; lib MIT, Platform non | `LangGraph.md` P + PG |
| CrewAI — **équipe de rôles**, Crews et Flows, indépendant de LangChain ; abstraction trompeuse de simplicité | `CrewAI.md` P + PG |
| AutoGen — **GroupChat** conversationnel ; en maintenance depuis fin 2025, AutoGen / AG2 / Agent Framework | `AutoGen.md` P + PG |
| Semantic Kernel — **parité C#/Python/Java** ; remplacé par Microsoft Agent Framework, planners refondus | `Semantic Kernel.md` P + PG |
| OpenAI Agents SDK — minimalité, **handoffs**, tracing intégré ; tracing par défaut chez OpenAI, robustesse à câbler | `OpenAI Agents SDK.md` P + PG |
| PydanticAI — sortie **Pydantic validée**, injection de dépendances typée ; sans type-checker en CI l'argument tombe | `PydanticAI.md` P + PG |
| smolagents — **CodeAgent** (actions en Python), ~1000 lignes ; `LocalPythonExecutor` **n'isole pas** | `smolagents.md` P + QNP + PG |
| Agno — mémoire/connaissance/raisonnement natifs, **AgentOS** self-host ; « le plus rapide » = instanciation | `Agno.md` P + PG |
| PraisonAI — `agents.yaml` low-code, **auto-réflexion** ; double au moins le nombre d'appels | `PraisonAI.md` P + PG |
| LlamaIndex — part du **pipeline de connaissance**, index variés ; défauts chunk/top-k décisifs, index avancés coûteux | `LlamaIndex.md` P + PG |
| Haystack — **pipeline explicite** de composants, hybride dense+BM25, Apache-2.0 ; rupture 1.x → 2.x | `Haystack.md` P + PG |
| RAGatouille — **late-interaction ColBERT**, index PLAID, minage de négatifs ; aucun commit depuis mai 2025 | `RAGatouille.md` P + PG |
| Instructor — emballe le client, `response_model`, **retry sur validation** ; retries qui gonflent facture et latence | `Instructor.md` P + PG |
| Outlines — **masquage des tokens invalides**, conforme par construction ; inutilisable sans logits, biaise la distribution | `Outlines.md` P + QNP + PG |
| Guidance — **entrelace contrôle et génération**, token healing, fast-forward ; DSL à apprendre, support selon backend | `Guidance.md` P + PG |

**Comparatif - Design & prototypage** — *où vivent les fichiers*

| Puce | Source |
|---|---|
| Figma — composants et variables, prototypes, **dev mode** ; cloud propriétaire **sans self-host**, coût par éditeur, format fermé | `Figma.md` P + PG |
| Penpot — **MPL-2.0 self-hostable**, standards web SVG/CSS ; maturité et plugins en retrait, infra à opérer | `Penpot.md` P + QNP + PG |

**Comparatif - Diagrammes** — *texte versionné, fichier posé à la main, ou artefact
d'agent*

| Puce | Source |
|---|---|
| Mermaid — **diagram-as-code**, rendu natif GitHub/GitLab/Obsidian ; **auto-layout subi** | `Mermaid.md` P + PG |
| draw.io — GUI, placement à la main, plus large catalogue de formes ; **XML illisible en diff** | `draw.io.md` P + PG |
| Excalidraw — style **croquis à main levée** comme signal ; peu de formes structurées, rame sur les grands tableaux | `Excalidraw.md` P + PG |
| FossFLOW — seul **isométrique 3D**, PWA hors ligne, icônes cloud ; périmètre étroit, stockage navigateur | `FossFLOW.md` P + PG |
| Archify — **skill d'agent**, IR JSON typée compilée de façon déterministe ; quatre absences documentées | `Archify.md` P + PG |

---

# Remontées — quatrième session, 2026-09-06 — **le lot est clos**

Périmètre : les **13 derniers**, sur sept domaines. **13 pages, 70 puces, 67 fiches lues.**
Les 47 comparatifs sont des pages.

Sept commits, un par domaine : « Data & pipelines » (6), « Interfaces & apps data » (2),
puis les cinq domaines à un comparatif — « Automatisation no-code », « Calcul distribué »,
« Mathématiques », « Signal & audio », « Statistiques & inférence ». La contrainte « un
domaine ne se coupe pas en deux » ne contraignait plus rien, comme le §22 l'annonçait.

## 23. Le lot a coûté quatre sessions et non une — et la remontée 7 l'avait chiffré juste

Le brief annonce « **une session**, 47 fichiers ». Il en a fallu **quatre** : 10 + 12 + 12 + 13.

Ce n'est pas un dérapage, c'est une mesure qui s'est vérifiée. La remontée 7, écrite à la fin
du pilote, disait : « Budget pour les 41 restants, à la même densité : ~230 fiches à lire.
C'est le poste dominant et il ne se compresse pas. » Le relevé des quatre sessions :

| Session | Comparatifs | Puces | Fiches lues |
|---|---|---|---|
| Pilote — Bases de données | 10 | 45 | 45 |
| 2ᵉ — Machine Learning, Outils de dév. | 12 | 60 | ~50 |
| 3ᵉ — ML (fin), LLM, Design | 12 | 83 | 57 |
| 4ᵉ — les 13 derniers | 13 | 70 | 67 |
| **Total** | **47** | **258** | **~219** |

219 contre 230 annoncées, à 5 % près, quatre jours après l'estimation. Ce qui n'a **pas** été
fait est l'accélérateur que la même remontée proposait — « un dump automatique des sections
`Pourquoi`, `Quand NE PAS l'utiliser` et `Pièges` des membres d'un `.base` […] à écrire comme
script si les 41 se font en plusieurs sessions ». Elles se sont faites en trois, et le dump
est resté à la main à chaque fois. Le script aurait coûté dix minutes une fois.

> **À retenir pour le lot 6**, qui est le plus gros du plan (336 fiches à convertir) : quand
> une remontée chiffre un poste dominant *et* propose l'outil qui l'allège, l'outil se fait à
> la session suivante ou il ne se fait jamais.

## 24. Cas 1 du §16 — la conversion ne rend PAS `R8b` silencieux, et la prédiction était fausse

Les §16 et §22 annonçaient, deux fois : « `Solveurs d'optimisation` a **un membre** (PuLP).
Le convertir ne réglera pas `R8b`, il le **rendra silencieux**. » Mesure faite après
conversion, les deux validateurs relancés :

```
[WARN] R8b — Mathématiques/Optimisation/Comparatif - Solveurs d'optimisation.base :
       1 membre(s) (< 2) — comparatif sans comparaison
```

**L'avertissement est toujours émis**, et le total reste à 149. La prédiction se trompait
pour une raison structurelle, pas par chance : `check_bases()` itère sur
`VAULT.rglob("*.base")` et compte les membres du **filtre**. La variante retenue le
2026-09-05 est à **deux fichiers** — la conversion ne supprime pas le `.base`, elle pose une
page à côté. R8b n'a donc rien perdu de vue. Et le prédicat `role == "brique"` de tous les
filtres garantit en prime que la page ne peut pas se compter elle-même comme membre
(remontée 4).

La prédiction aurait été **exacte avec l'autre variante** — le fichier unique, où le `.base`
disparaissait. C'est une propriété de la décision du 2026-09-05 que personne n'avait
nommée : en gardant le `.base`, on garde le contrôle qui porte sur lui.

Reste que le fond du §16 était juste, et il faut le dire pour ce qu'il est. **Le défaut n'est
pas dans la vue : il est dans le vault.** Le filtre `categorie == "math/optimisation"`
sélectionne exactement ce que le brain contient, et la fiche `PuLP` nomme **onze** briques en
clair sans qu'aucune ait de page — `Pyomo`, `CVXPY`, `scipy.optimize`, `CBC`, `GLPK`,
`HiGHS`, `SCIP`, `Gurobi`, `CPLEX`, `MOSEK`, `XPRESS`. Deux traces écrites plutôt qu'une
conversion muette : une section de la page qui dit qu'elle ne compare rien et nomme les onze,
et une entrée de `AI/backlog-enrichissement-brain.md` avec leur `categorie:`, leur `famille:`
et une priorité à trois pages (Pyomo, CVXPY, HiGHS) qui suffiraient à éteindre `R8b`.

> **Ce que ça dit d'une prédiction dans un document de lot** : elle a la même durée de vie
> qu'un chiffre mesuré, et personne ne la revérifie non plus. Celle-ci a été recopiée du §16
> au §22 sans être testée, alors qu'elle coûtait une commande.

## 25. Cas 2 du §16 — aucun tag ne capture les cinq membres, la liste reste, et son motif est écrit

`Comparatif - Frontends web légers` est le seul des 47 dont le filtre est une **liste de noms
codée en dur** (`[WARN] R8d`). La consigne était de mesurer d'abord s'il existe un tag qui
capture **exactement** ces cinq membres et rien d'autre. Mesure sur les 337 briques de
l'index :

| Candidat | Couvre | Fait entrer en plus |
|---|---|---|
| **intersection des tags des 5** | — | **VIDE** : `HTMX` ne porte que `hypermedia`, qu'aucun des quatre autres n'a |
| `web-framework` | 4/5 (rate HTMX) | Flask, Uvicorn, **Shiny for Python** |
| `data-app` | 2/5 | Marimo, **Shiny for Python** |

Aucun tag ne convient, et le meilleur candidat ferait entrer `Shiny for Python`, qui
appartient à l'**autre** comparatif du même dossier. La liste est donc conservée : c'est
l'expression honnête d'une comparaison **composée à la main**, qu'aucune `categorie:` ni
aucun tag ne capture — trois membres sont `ui/data-app`, un `web/backend`, un `web/frontend`.

Le motif est écrit **deux fois**, et l'endroit compte : en commentaire dans le `.base`, là où
vit la liste et là où pointe l'avertissement, et en section de la page pour le lecteur qui
n'ouvrira jamais le YAML.

> **Ce que ça change pour le lot 8**, qui doit durcir les règles souples : `R8d` n'est pas une
> règle à faire taire ni à durcir. Elle décrit un fait vrai — une brique qui entre dans le
> thème n'entrera jamais dans la vue — sur le seul cas du vault où ce fait est **voulu**. Une
> règle souple avec une exception documentée est un meilleur état qu'une règle dure avec une
> dérogation, ou qu'une règle supprimée.

## 26. `## Pièges` sert 100 % des puces pour la première fois, et `QNP` retombe à 7 %

Répartition des sources sur les 70 puces, à comparer aux trois sessions précédentes :

| Section de la fiche | Pilote (45) | 2ᵉ (60) | 3ᵉ (83) | 4ᵉ (70) |
|---|---|---|---|---|
| `## Pourquoi` | 45 — 100 % | 60 — 100 % | 83 — 100 % | 70 — **100 %** |
| `## Pièges` | 38 — 84 % | 51 — 85 % | 78 — 94 % | 70 — **100 %** |
| `## Quand NE PAS l'utiliser` | 1 — 2 % | 12 — 20 % | 15 — 18 % | 5 — **7 %** |

Sur l'ensemble des 258 puces du lot : `Pourquoi` **258/258**, `Pièges` **237/258** (92 %),
`QNP` **33/258** (13 %).

`## Pourquoi` fournit tout, pour la quatrième fois — c'est acquis. `## Pièges` atteint 100 %
et referme le diagnostic de la spec §6 : cette section, que la v3 **dissout**, est celle qui
porte la limite décisionnelle sur *chacune* des 70 briques de cette session. L'instruction
pour le lot 6 écrite à la remontée 6 n'est donc pas une précaution, c'est une condition : la
ligne de `## Pièges` qui sert de critère dans un comparatif doit se retrouver dans
`## Définition` ou dans `Écarter si`, jamais disparaître.

`QNP` retombe à 7 %, et la remontée 20 explique pourquoi sans avoir à être corrigée : c'est la
**forme** de la puce qui décide, pas le voisinage des membres. Les 5 retenues énoncent toutes
une borne dure de la brique elle-même — `altair` et sa limite de 5000 lignes, `pingouin` en
GPL-3.0, `Fanalysis` à l'arrêt depuis le 4 juin 2018, `minim` dont la v1 est en maintenance,
`PuLP` dont le périmètre s'arrête au LP/MIP. Toutes les autres puces de `QNP` lues cette
session sont des redirections « besoin → concurrent », y compris sur des comparatifs
d'étages : `Playwright` renvoyant à `curl_cffi`, `Streamlit` renvoyant à `Dash`. Le voisinage
n'y change rien, la forme si.

**Un cas limite mérite d'être nommé**, parce qu'il n'existe que sur un comparatif à un membre.
La puce retenue pour `PuLP` est de forme « besoin → concurrent » — « optimisation non linéaire
→ Pyomo ou CVXPY ». Elle a été comptée quand même, et le motif est que **le concurrent est
hors du tableau** : là où la remontée 6 reprochait à cette forme de décrire le voisin plutôt
que la brique, ici elle est la seule façon d'énoncer que le périmètre de PuLP s'arrête au
LP/MIP. La règle de la remontée 20 tient donc avec une précision : une redirection ne
départage rien **entre les membres du tableau** ; elle informe quand la cible n'y est pas.

**Onze puces sur 70 reposent d'abord sur un fait de licence ou de cycle de vie** — 16 %,
contre 13 % à la session précédente (remontée 21) — et le domaine « Automatisation no-code »
bat tous les autres : **quatre de ses cinq membres** se départagent d'abord là-dessus. `n8n`
en Sustainable Use License non OSI contre `Activepieces` au cœur réellement MIT est *l'*arbitrage de ce comparatif, et la vue affiche `licence_type` pour les deux sans jamais le
montrer. S'y ajoutent `Windmill` en AGPLv3, `Zapier` et `gumloop` propriétaires, `PyMuPDF` en
AGPL ou licence Artifex, `Marker` en double licence avec son seuil à 2 M$, `Firecrawl` au cœur
AGPL, `LlamaParse` non open-source, `pingouin` en GPL-3.0, `Fanalysis` à l'arrêt.

## 27. Le §14 s'est rejoué une quatrième fois — sur une passe de correction du §14 lui-même

Deux `git mv` cette session : `Comparatif - Traitement du signal` vers
« Signal & audio/Traitement/ », `Comparatif - Outils stats` vers
« Statistiques & inférence/Tests & estimation/ ». Les deux par le mécanisme du §12 — un
`.base` ne porte pas de `categorie:`, la page en porte une, et `check_arbo` en dérive le
dossier — et les deux à **majorité stricte**, sans passer par `taxonomie.md` : 2 contre 1 pour
le signal, 4 contre 3 pour les stats.

Comme les trois fois précédentes, aucun lien cassé, zones AUTO régénérées seules, validateurs
verts, 149 avertissements identiques. Et comme les trois fois précédentes, des phrases
devenues fausses, trouvées uniquement par recherche du **nom de fichier** dans tous les `.md`
du dépôt. Cinq cette fois, toutes dans `AI/design/v3-arborescence.md` :

| Phrase | Devenue fausse |
|---|---|
| « `Comparatif - Outils stats` […] il **reste au niveau du domaine** » | par ce lot |
| « `Comparatif - Traitement du signal` […] il **reste au niveau du domaine** » | par ce lot |
| « `[c]` Comparatif - Traitement du signal — **rangé** dans « Signal & audio/ » » | par ce lot |
| « `[c]` Comparatif - Détection d'anomalies — **rangé** dans « Machine Learning/ » » | **à la deuxième session** |
| « `[c]` Comparatif - Réduction de dimension — **rangé** dans « Machine Learning/ » » | **à la deuxième session** |

Les deux dernières sont le point de cette remontée. Elles ont été invalidées par les `git mv`
de la **deuxième** session — celle qui a écrit la remontée 14, « après tout `git mv`, chercher
le nom du fichier déplacé dans tous les `.md` du vault ». Cette session-là a bien appliqué sa
propre instruction sur les **corps de hub**, qu'elle a corrigés dans un commit dédié, et a
manqué la liste de `v3-arborescence.md` qui nommait les mêmes deux fichiers. La troisième
session a élargi le périmètre du vault au dépôt (remontée 19) et a corrigé
`v3-arborescence.md` pour `Frameworks LLM` — sans revoir les entrées voisines de la même
liste.

> **Ce que ça ajoute aux remontées 14 et 19** : le périmètre de la recherche était bon dès la
> deuxième session, c'est son **exécution** qui a été partielle, et rien ne l'a signalé — une
> passe de correction ne se vérifie pas elle-même, exactement comme le reste. Le seul contrôle
> qui aurait vu les deux est mécanique : `grep` du nom de fichier, puis **lire toutes les
> occurrences**, y compris celles qui ressemblent à des lignes déjà traitées. C'est aussi un
> candidat pour le lot 8 : un script qui, pour chaque page du vault, cherche son nom en clair
> dans les `.md` de gouvernance et signale les phrases contenant un nom de dossier qui n'est
> pas le sien.

## 28. État final du lot 5

**47 comparatifs, 47 pages, 47 `.base`**, appariés un pour un, chacun dans le dossier que
`check_arbo` dérive de la `categorie:` de la page. Vérifié mécaniquement : aucun `.base` sans
page, aucune page sans `.base`.

| Domaine | Comparatifs | Session |
|---|---|---|
| Bases de données | 10 | pilote |
| Machine Learning | 12 | 2ᵉ (9) et 3ᵉ (3) |
| Outils de développement | 3 | 2ᵉ |
| LLM & IA générative | 7 | 3ᵉ |
| Design & diagrammes | 2 | 3ᵉ |
| Data & pipelines | 6 | 4ᵉ |
| Interfaces & apps data | 2 | 4ᵉ |
| Automatisation no-code · Calcul distribué · Mathématiques · Signal & audio · Statistiques & inférence | 5 | 4ᵉ |

**Cinq `git mv` en tout**, tous par le mécanisme du §12 : `Détection d'anomalies` et
`Réduction de dimension` (2ᵉ session), `Frameworks LLM` (3ᵉ), `Traitement du signal` et
`Outils stats` (4ᵉ). Chacun a rendu fausse au moins une phrase qu'aucun validateur ne lit.

**Les deux avertissements du §16 sont traités, et tous deux restent émis** — c'est le
résultat, pas un échec : `R8b` sur `Solveurs d'optimisation` décrit un trou réel du vault,
ouvert au backlog ; `R8d` sur `Frontends web légers` décrit un choix délibéré, désormais
motivé par écrit à deux endroits. Le compteur du validateur est à **149 avertissements du
premier au dernier commit du lot**, jeu identique ligne à ligne, mesuré à chaque commit.

**Ce que le lot laisse aux suivants :**

- **lot 6** — la dépendance créée par la remontée 6 et confirmée au §26 : 237 puces de
  comparatif citent en clair une ligne de `## Pièges`, section que la spec dissout. Elles
  doivent réapparaître dans `## Définition` ou dans `Écarter si`.
- **lot 8** — quatre sujets nommés : relire la règle dure nº 5 (`Écarter si` doit énoncer la
  limite *et* nommer l'alternative, pas se réduire à l'alternative — remontée 20) ; brancher
  `AI/scripts/verifier_fraicheur.py` sur les pages de comparatif, qui portent maintenant une
  trentaine de faits datés de licence et de cycle de vie (remontée 21 et §26) ; corriger le
  chiffre « 6 comparatifs » de `brain-v3.md` §1 (remontée 1) ; outiller la recherche de
  phrases invalidées par un déplacement (§27).
- **enrichissement** — l'entrée « Solveurs d'optimisation » du backlog, onze briques nommées.

## Annexe — le relevé des sources, puce par puce (70)

`P` = `## Pourquoi`, `QNP` = `## Quand NE PAS l'utiliser`, `PG` = `## Pièges`.

**Comparatif - Outils EDA - profiling** — *l'étendue du rapport : tout le jeu, la relation à
une cible, ou la seule nullité*

| Puce | Source |
|---|---|
| ydata-profiling — rapport exhaustif + **alertes**, seul à profiler du Spark ; $O(p^2)$, mode `minimal` | `ydata-profiling.md` P + PG |
| sweetviz — construit autour d'une **cible** et de `compare` / `compare_intra` ; `pairwise_analysis="off"` en haute dimension | `sweetviz.md` P + PG |
| missingno — un seul problème, la nullité, quatre vues dessus ; la `matrix` **échantillonne** | `missingno.md` P + PG |

**Comparatif - Manipulation de données** — *la forme de la donnée, puis ce qui borne : la RAM
ou la dette d'API*

| Puce | Source |
|---|---|
| pandas — l'**index** de premier ordre et l'interop ; mono-thread, tout en RAM, vue vs copie | `pandas.md` P + PG |
| Polars — Rust/Arrow, **lazy** + optimiseur, moteur streaming ; pas d'index, rien avant `.collect()` | `Polars.md` P + PG |
| Modin — **remplaçant transparent** de pandas ; couverture non totale, repli **silencieux** | `Modin.md` P + PG |
| numpy — le `ndarray` **homogène** contigu, la brique du dessous ; vues, débordements entiers | `numpy.md` P + PG |
| xarray — les **étiquettes** sur le N-dim, NetCDF/Zarr, `chunks=` vers Dask ; `NaN` d'alignement | `xarray.md` P + PG |

**Comparatif - Orchestrateurs data** — *ce que le pipeline déclare : une tâche, une donnée
produite, un YAML, ou un processus qui survit au crash*

| Puce | Source |
|---|---|
| Airflow — DAG de tâches + le plus large catalogue d'operators ; `logical_date`, re-parse, XCom | `Airflow.md` P + PG |
| Dagster — l'**asset** comme unité, lignage déduit, tests de données ; modèle mental à changer | `Dagster.md` P + PG |
| Prefect — `@flow`/`@task`, **pas de DAG statique** ; donc pas de visualisation a priori | `Prefect.md` P + PG |
| Kestra — **déclaratif YAML** sur JVM, découplé du langage des tâches ; autre stack, verbosité | `Kestra.md` P + PG |
| Mage — ELT **low-code par blocs** avec preview ; OSS ralenti depuis Mage Pro | `Mage.md` P + PG |
| Temporal — **exécution durable**, historique event-sourced ; workflow **déterministe** obligatoire | `Temporal.md` P + PG |

**Comparatif - Parsing de documents** — *l'étage, puis où le calcul se fait et sous quelle
licence*

| Puce | Source |
|---|---|
| pdf-inspector — l'étage de **tri**, 10-50 ms, routage OCR page par page ; tables heuristiques | `pdf-inspector.md` P + PG |
| PyMuPDF — **référence de vitesse** + modèle objet PDF ; **AGPL-3.0** ou licence Artifex | `PyMuPDF.md` P + PG |
| pdfplumber — **MIT**, tableaux à stratégies, **débogage visuel** ; pas d'OCR, plus lent | `pdfplumber.md` P + PG |
| docTR — **OCR** en deux étages, backend au choix ; ordre de lecture non garanti | `docTR.md` P + PG |
| Docling — multi-format vers `DoclingDocument`, modèles **CPU en local**, MIT ; premier run lourd | `Docling.md` P + PG |
| Unstructured — **ETL**, éléments typés + connecteurs ; binaires système, `hi_res` lent | `Unstructured.md` P + PG |
| Marker — pipeline **vision** Surya, débit GPU ; **double licence**, seuil 2 M$ | `Marker.md` P + PG |
| LlamaParse — le seul **managé**, tiers et crédits ; documents dans le cloud | `LlamaParse.md` P + PG |
| OpenDataLoader PDF — le seul **déterministe**, bounding boxes, **Tagged PDF** ; tables 0,489 en local, JVM | `OpenDataLoader PDF.md` P + PG |

**Comparatif - Scraping** — *l'étage, puis ce qui bloque : l'empreinte, le JS ou la refonte de
la page*

| Puce | Source |
|---|---|
| Scrapy — crawl **structuré**, Twisted, AutoThrottle ; ne rend pas le JS | `Scrapy.md` P + PG |
| Crawlee — **API unifiée** HTTP ↔ navigateur, Node/TS ; deux ports non identiques | `Crawlee.md` P + PG |
| Playwright — le **vrai navigateur**, attentes auto-résolues, session rejouable ; coût, détectable | `Playwright.md` P + PG |
| curl_cffi — **empreinte TLS/JA3 et HTTP/2** imitée ; l'empreinte vieillit, UA à accorder | `curl_cffi.md` P + PG |
| cloudscraper — le **JS challenge IUAM** de Cloudflare, drop-in requests ; dépassé par Turnstile | `cloudscraper.md` P + PG |
| Scrapling — parseur **adaptatif** + fetchers **furtifs** ; bibliothèque récente, API mouvante | `Scrapling.md` P + PG |
| selectolax — **parsing** seul, Lexbor, un ordre de grandeur ; pas de client HTTP, CSS only | `selectolax.md` P + PG |
| Firecrawl — Markdown/JSON pour **LLM**, rendu et anti-bot inclus ; **AGPL-3.0**, coût, infra | `Firecrawl.md` P + PG |
| Maxun — le seul **no-code**, robot enregistré et planifié ; beta, plafonne sur les sites défendus | `Maxun.md` P + PG |
| minim — sept plateformes musicales, **API privées** reproduites ; **zone grise**, v1 en maintenance | `minim.md` P + QNP + PG |

**Comparatif - Visualisation** — *où le graphe est rendu, et comment on le décrit*

| Puce | Source |
|---|---|
| matplotlib — le **socle**, contrôle au pixel, export vectoriel ; deux API, état global, verbeux | `matplotlib.md` P + PG |
| seaborn — surcouche **statistique** sur DataFrame, facettes, IC ; pas d'interactivité, `set_theme` global | `seaborn.md` P + PG |
| plotly — interactif **immédiat**, moteur de Dash ; pages lourdes, **Kaleido**, `scattergl` | `plotly.md` P + PG |
| bokeh — interactif **côté serveur**, gros volumes et streaming ; sessions à apprendre, pas d'export image | `bokeh.md` P + PG |
| altair — le seul **déclaratif**, spec Vega-Lite réutilisable ; **5000 lignes** par défaut | `altair.md` P + QNP + PG |

**Comparatif - Apps data & démos ML** — *ce qui se recalcule à chaque interaction*

| Puce | Source |
|---|---|
| Streamlit — script linéaire, **re-run global** ; `@st.cache_*`, `session_state`, flux vertical | `Streamlit.md` P + PG |
| Dash — **callbacks explicites**, Flask + React + Plotly.js ; verbeux, `dcc.Store` obligatoire | `Dash.md` P + PG |
| Shiny for Python — graphe de dépendances **déduit** ; réactivité à apprendre, Shinylive/Pyodide | `Shiny for Python.md` P + PG |
| Gradio — part d'une **fonction**, file d'attente et streaming, SDK de HF Spaces ; `share=True` temporaire | `Gradio.md` P + PG |

**Comparatif - Frontends web légers** — *jusqu'où on descend : un widget Python, ou une page
qu'on écrit*

| Puce | Source |
|---|---|
| Streamlit — aucun HTML, l'app en quelques heures ; re-run global, mise en page contrainte | `Streamlit.md` P + PG |
| Gradio — autour d'une fonction, pas d'une page ; c'est une démo, `share=True` temporaire | `Gradio.md` P + PG |
| Dash — le premier à demander une structure, multi-pages ; verbeux, `dcc.Store` en multi-worker | `Dash.md` P + PG |
| FastAPI — backend **API** typé, OpenAPI déduite ; **ne rend aucune page**, `def` bloque l'event loop | `FastAPI.md` P + PG |
| HTMX — attributs qui **échangent un fragment HTML** ; latence par interaction, fragments à servir | `HTMX.md` P + PG |

**Comparatif - Automatisation no-code** — *la licence et l'hébergement d'abord, puis qui écrit
le workflow*

| Puce | Source |
|---|---|
| n8n — 400+ nœuds, code insérable, nœuds IA ; **Sustainable Use License**, non OSI, queue mode | `n8n.md` P + PG |
| Activepieces — cœur **réellement MIT**, pièces npm, MCP ; open-core, écosystème plus restreint | `Activepieces.md` P + PG |
| Windmill — le seul **code-first**, moteur Rust distribué ; **AGPLv3** + Enterprise | `Windmill.md` P + PG |
| Zapier — **8000+ apps**, tout managé ; facturation **à la tâche**, lock-in sans export | `Zapier.md` P + PG |
| gumloop — **l'IA dans chaque nœud** ; éditeur jeune, coûts LLM, exécutions moins déterministes | `gumloop.md` P + PG |

**Comparatif - Calcul distribué** — *ce qu'on distribue, ou bien on ne distribue rien et on
descend sur le GPU*

| Puce | Source |
|---|---|
| Spark — moteur **JVM** unifié, lakehouse ; overhead JVM, **shuffle**, UDF Python lentes | `Spark.md` P + PG |
| Dask — **Python pur**, collections numpy/pandas + graphe ; `.compute()`, partitionnement, couverture partielle | `Dask.md` P + PG |
| Ray — **tâches et acteurs**, donc code Python quelconque + l'écosystème ML ; cloudpickle, ressources, object store | `Ray.md` P + PG |
| CuPy — **numpy sur GPU**, zéro-copie vers PyTorch/JAX ; transfert CPU↔GPU, wheels CUDA strictes | `CuPy.md` P + PG |

**Comparatif - Solveurs d'optimisation** — *la classe du problème, et le couplage au solveur*

| Puce | Source |
|---|---|
| PuLP — un **modeleur** qui délègue, solveurs interchangeables ; périmètre LP/MIP, CBC, `LpStatus` | `PuLP.md` P + QNP + PG |

**Comparatif - Traitement du signal** — *la représentation cherchée : fréquence, temps-échelle,
ou features audio*

| Puce | Source |
|---|---|
| scipy.signal — la boîte **DSP** de référence ; Nyquist, format **SOS**, ondelettes **retirées** | `scipy.signal.md` P + PG |
| PyWavelets — le **temps-échelle** et le **seuillage** ; ondelette mère, padding, CWT coûteuse | `PyWavelets.md` P + PG |
| librosa — l'étage **audio** haut niveau ; lent, `sr=22050` rééchantillonne, hors ligne | `librosa.md` P + PG |

**Comparatif - Outils stats** — *l'étage, puis la question : tester, factoriser, dater un
effet, modéliser une durée*

| Puce | Source |
|---|---|
| scipy.stats — le **socle bas niveau**, ~100 lois, bootstrap ; par fonctions, sans diagnostics | `scipy.stats.md` P + PG |
| statsmodels — l'**objet modèle** et son résumé annoté, formules R ; constante, API double | `statsmodels.md` P + PG |
| pingouin — p-value + **taille d'effet + IC + puissance** d'un coup ; **GPL-3.0** | `pingouin.md` P + QNP + PG |
| lifelines — la seule **survie**, Kaplan-Meier, Cox, AFT ; **censure**, risques proportionnels | `lifelines.md` P + PG |
| PyMC — **programmation probabiliste** en Python pur ; backend mouvant, divergences NUTS | `PyMC.md` P + PG |
| Stan — **langage dédié compilé**, artefact `.stan` réutilisable ; compilation, toolchain C++ | `Stan.md` P + PG |
| ArviZ — le seul **indépendant du moteur**, `InferenceData`, LOO/WAIC ; $\hat{R}$ ne suffit pas | `ArviZ.md` P + PG |
| CausalImpact — l'**effet d'une intervention datée** par contrefactuel BSTS ; écosystème fragmenté | `CausalImpact.md` P + PG |
| Prince — toute la famille **factorielle** en API sklearn ; API mouvante, Altair, single-node | `Prince.md` P + PG |
| Fanalysis — les **aides à l'interprétation** FactoMineR ; **à l'arrêt depuis le 4 juin 2018** | `Fanalysis.md` P + QNP + PG |
