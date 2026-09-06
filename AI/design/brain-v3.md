---
galaxie: meta
nom: brain-v3
type: design-doc
created: 2026-09-04
modified: 2026-09-06
status: arrete
tags: [meta, design, v3]
---

# DevBrain v3 — Spec de refonte

> Document de conception. On écrit la cible **avant** de déplacer un fichier.
> **La migration v3 est CLOSE depuis le 2026-09-06.** Les huit lots sont faits ; plus rien
> ici n'est au futur. Ce document décrit désormais l'état RÉEL du vault, et sert de
> référence — pas de plan. Ce qui reste ouvert est nommé comme tel, avec son motif, au §14.
> Inventaire et arbre chiffrés : [[AI/design/v3-arborescence|v3-arborescence]].
> Ce que la v2 a établi et qui reste vrai : [[AI/design/brain-v2|brain-v2]].

---

## 1. Ce qui déclenche la v3

La v2 a réglé le **rangement des fiches** (deux axes `categorie:` × `famille:`, arbres de
décision déterministes) et l'**intégrité** (validateur, clôture). Elle n'a pas touché à trois
choses, qui sont exactement celles qui gênent à l'usage.

| Constat | Mesure au 2026-09-04 |
|---|---|
| Les dossiers ne portent aucune information | 297 fiches à plat dans `Dev/Services`, 299 dans `Wiki/Concepts`, zéro sous-dossier |
| Le rôle « aiguillage » n'a pas de domicile : il est joué trois fois | `MOC/Categories/Bases de données` (47 briques), `Wiki/Concepts/Bases de données` (26, recouvrement total), 6 comparatifs `.base` |
| Le haut de fiche sert la machine, pas le lecteur | 18 propriétés rendues en panneau vertical avant le titre |

Trois causes annexes, mesurées elles aussi :

- `AI/index/liens.md` porte **10 335 wikilinks** et n'est pas masqué du graphe. À lui seul il
  crée plus d'arêtes que les 8 009 liens écrits dans les pages. Tout est à un saut de tout.
- Un `.base` est un fichier YAML de requête : ni frontmatter, ni corps. Donc **jamais de lien
  sortant, jamais de couleur**. 44 comparatifs sur 47 sont cités, aucun ne cite.
- Le voisinage d'une page n'est calculable par rien. Le skill d'enrichissement doit le
  **deviner** — c'est le mécanisme derrière les 7 étapes sur 11 sans trace de l'axe 3.

---

## 2. Le principe : deux axes, comme pour les fiches

La v2 a séparé `categorie:` (le domaine) de `famille:` (la nature). La v3 applique la même
séparation au vault entier.

| Axe | Porté par | Sert à |
|---|---|---|
| **Le domaine** — de quoi ça parle | le **dossier** | descendre dans l'arbre, avec ou sans Obsidian |
| **Le rôle** — ce que la page est | le champ `role:` | la couleur dans le graphe, le gabarit, les règles |

Conséquence directe : **une seule galaxie, un seul arbre.** `Dev/` et `Wiki/` disparaissent
comme dossiers ; la distinction qu'ils portaient passe dans `role:`. Une notion et les briques
qui l'implémentent vivent côte à côte, dans le dossier de leur domaine.

`galaxie:` et `type:` sont supprimés. `galaxie:` ne servait qu'à la couleur — `role:` le fait
mieux. `type:` ne décrivait que le dossier d'accueil, ce que l'audit v2 avait déjà démontré
(57 fiches de nature identique réparties 34/23 entre `service` et `outil`, sans discriminant).

---

## 3. Les rôles

| `role:` | Ce que c'est | Couleur | Longueur |
|---|---|---|---|
| `hub` | la page d'un dossier, qui porte son nom — l'aiguillage | orange | courte, moitié générée |
| `notion` | ce qu'il faut comprendre : définitions, maths, mécanismes | vert | libre, structurée |
| `brique` | ce qu'on déploie ou importe : service, outil, librairie | bleu | courte et rigide |
| `comparatif` | ce qui départage plusieurs briques | rouge | courte |
| `pattern` | une architecture éprouvée | gris | libre |
| `rule` | une règle transverse | gris | libre |

Les couleurs sont posées dans `.obsidian/graph.json` par requête sur `role:`, comme
aujourd'hui sur `galaxie:`.

---

## 4. L'arborescence

### Règle de construction, mécanique

1. Un dossier par **domaine**, nommé avec son libellé français (table `DOM_LABEL`,
   reprise de `CAT_LABEL` de `build_mocs.py`). 20 domaines.
2. Un **sous-dossier** dès qu'un sous-domaine atteint **5 pages** — sauf s'il ne laisse
   aucune page au niveau du domaine, auquel cas il ne se promeut pas (plafond tranché le
   2026-09-04, cf. §14.4). En-dessous du seuil, ses pages restent au niveau du domaine.
   Aucun arbitrage : le seuil et son plafond décident.
3. Tout dossier porte une page à son nom, `role: hub`.
4. Le chemin d'une page se **dérive** de son `categorie:`. Personne ne choisit un dossier :
   on pose la catégorie par l'arbre de décision de `Documentation/general/taxonomie.md`, et
   le rangement en découle. Un script vérifie que chemin et catégorie concordent.

Le seuil de 5 donne 28 sous-dossiers et aucun dossier de deux fichiers. Mesures et arbre
complet : [[AI/design/v3-arborescence|v3-arborescence]].

```
SecondBrain/
├── Bases de données/
│   ├── Bases de données.md              role: hub        orange
│   ├── Vectoriel/
│   │   ├── Vectoriel.md                 role: hub        orange
│   │   ├── Bases de données vectorielles.md   role: notion     vert
│   │   ├── Comparatif - Bases vectorielles.md role: comparatif rouge
│   │   ├── Qdrant.md  Weaviate.md  pgvector.md  …  role: brique  bleu
│   ├── Relationnel/   Administration/   Recherche/
│   └── SQLAlchemy.md  Prisma.md  …      (17 pages au niveau du domaine)
├── Machine Learning/    241 pages, 9 sous-dossiers
├── LLM & IA générative/ 131 pages, 6 sous-dossiers
├── … 17 domaines
│
├── Métiers/             5 hubs transverses, indexés par `domaines:`
├── Patterns/            1 hub + 5 pages, indexés par `role: pattern`
└── Rules/               1 hub + 5 pages, indexés par `role: rule`
```

Les trois derniers dossiers ne sont pas des domaines : rien ne s'y dérive d'une
`categorie:`, et c'est pourquoi ils sont à la racine plutôt que dans l'arbre. Ils sont
la seule exception à la règle 4, et elle est fermée — `check_arbo.py` compte leurs pages
à part (`arbo.ROLES_SANS_CATEGORIE`).

> Cet arbre décrivait l'état visé **après le lot 4**, pas après le lot 3 : au lot 3,
> `Bases de données vectorielles.md` était une notion rangée par la galaxie wiki et non
> par son domaine, et le lot 3 ne recatégorisait rien. Même écart pour le sous-dossier
> `Traitement/` de « Signal & audio ». **Le lot 4 a clos les deux le 2026-09-05** : la
> notion vit dans `Bases de données/Vectoriel/`, et l'arbre ci-dessus est l'état réel.
> Cf. les *Remontées* de `AI/migration/lot-3-arborescence.md`.

### Ce que l'arbre remplace

`MOC/` disparaît — 39 pages — mais **pas d'un seul coup**. Ses trois étages, plus les
deux dossiers `Dev/` que `categorie:` ne rangeait pas :

- `MOC/Categories/*` → les pages `hub` de domaine, par `git mv` — **fait au lot 3** ;
- `MOC/Types/*` (Patterns, Rules) → les hubs de deux dossiers racine, « Patterns/ » et
  « Rules/ », que les 5 patterns et les 5 règles rejoignent : c'est `role:` qui les
  groupe, aucune `categorie:` ne les range — **fait au lot 3** ;
- `MOC/Themes/*` → descendus à la racine dans « **Métiers/** », 5 pages `role: hub`
  transverses, seul endroit où le champ `domaines:` sert encore — **fait au lot 3**.
  Le dossier ne s'appelle pas « Domaines » : le mot désigne déjà les 20 dossiers de
  l'arbre. La collision de vocabulaire entre le champ et l'arbre est **tranchée à la
  clôture du lot 8** : le champ garde son nom, « domaine » désigne l'axe de l'arbre et
  « métier » ce que `domaines:` porte. Cf. §14, question 1 ;
- `MOC/Concepts/*` → les mêmes pages hub, puisque notions et briques cohabitent désormais
  — mais **seulement au lot 4**, une par une. Ces 10 pages étaient la seule porte d'entrée
  (R7) de 30 des 297 notions. **Les 10 sont supprimées au 2026-09-05, et `MOC/` avec
  elles** : une MOC meurt quand il est **mesuré** que zéro page ne dépend plus d'elle
  seule pour sa R7 **et** que `build_mocs.py` ne la régénère plus, jamais sur l'intuition.
  C'est la seule exception à « aucun `rm` sur une page » pendant la migration.

La suppression des suffixes `(notions)` de `CONCEPT_LABEL` est un effet de bord attendu : ils
n'existaient que pour éviter la collision de nom entre un hub et une notion homonyme. En v3 la
collision n'est plus possible, les deux ayant fusionné.

---

## 5. Le haut de page

### Le problème

18 propriétés rendues en panneau vertical, avant le titre. La définition passe sous la ligne
de flottaison. Le frontmatter sert la machine ; le lecteur a besoin de cinq faits. Un seul
affichage ne peut pas servir les deux.

### La règle

Le panneau natif d'Obsidian est **masqué** — Réglages → Éditeur → *Propriétés dans le
document* → **Masqué**. Vérifié le 2026-09-04 sur la documentation officielle. Les propriétés
restent accessibles par la barre latérale et lisibles par les scripts ; aucune page n'est
modifiée. Le haut de page porte un **bandeau transposé**, généré depuis le frontmatter dans
une zone `<!-- AUTO -->`. Le frontmatter reste, invisible, pour l'index et le validateur.

```markdown
# Faker

> Génère des données factices réalistes en Python — noms, adresses, emails,
> textes, dates — via des providers et des dizaines de locales.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source (MIT) | import, rien à héberger | production |
```

Trois lignes rendues au lieu de dix-huit. `## Définition` commence au-dessus de la ligne de
flottaison.

### Nettoyage du frontmatter

| Champ | Décision | Motif mesuré |
|---|---|---|
| `galaxie`, `type` | supprimés | remplacés par `role:` |
| `status` | supprimé | 272 fiches sur 336 sont `actif`+`production` ; 7 des 8 `abandonne` sont `deprecated`. Redondant avec `maturite` |
| `remplace_par` | supprimé | vide sur 293 fiches sur 297 ; les 7 cibles des 4 restantes figuraient déjà en `alternatives` (mesure corrigée au lot 2) |
| `hosted` | valeurs en **liste**, champ **conditionnel** | `both` (82 fiches) ne dit rien : on énumère `[self, managed]` — sans accent, orthographe de l'énumération en vigueur. Et 177 `paquet` portent une valeur d'hébergement alors qu'une bibliothèque ne s'héberge pas. Le champ n'existe que pour `plateforme`, `saas`, `application` |
| `scaling` | champ **conditionnel** | `single-node` sur 212 fiches = la valeur par défaut de tout ce qui n'est pas distribué. Même traitement |
| `complements` | **ajouté** | symétrique d'`alternatives:` — pgvector et Postgres ne s'excluent pas, ils s'utilisent ensemble |

Frontmatter d'une brique, quatorze champs : `role`, `nom`, `alias`, `pitch`, `categorie`,
`famille`, `langage`, `licence_type`, `maturite`, `alternatives`, `complements`, `tags`,
`url_docs`, `url_repo` — plus `hosted` et `scaling` quand la famille les rend pertinents.

---

## 6. Gabarit — `role: brique`

Le principe est celui de la section `## Alternatives`, la seule que l'usage a validée :
**une ligne, une étiquette, une idée**. Aucune prose hors de `## Définition`.

```markdown
# Faker

> <pitch, une ligne>

| Nature | Licence | Exécution | Maturité |          ← généré depuis le frontmatter
|---|---|---|---|
| Librairie Python | open-source (MIT) | import, rien à héberger | production |

## Définition

Prose vulgarisée, quatre à six lignes. Explique le fonctionnement et la limite qui
structure l'usage. **Ne redit rien de ce que le bandeau affiche déjà.**

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Peupler des tests, fixtures ou une démo | Respecter la distribution du réel → [[SDV]] |
| Anonymiser en substituant du factice | Nom et email doivent correspondre → [[SDV]] |
| Jeux reproductibles par seed | Gros volumes typés, priorité vitesse → [[Mimesis]] |

## Mise en œuvre

- Installation — `uv add Faker`
- Point d'entrée — import Python, `from faker import Faker`
- Prérequis — Python ≥ 3.10, aucune dépendance lourde
- Exécution — CPU, single-node, rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives
- [[Mimesis]] — <pitch courant de Mimesis, réinjecté>
- [[SDV]] — <pitch courant de SDV, réinjecté>

### Compléments
- [[pandas]] — <pitch> — pour matérialiser les tirages en DataFrame

## Ressources

- Documentation — https://faker.readthedocs.io/
- Dépôt — https://github.com/joke2k/faker
- Tutoriel — …
- Article — …

## Voir aussi

- [[Synthetic data generation]] — la notion parente
```

### Ce qui disparaît, et pourquoi

> **Cette section décrit le gabarit cible ; il est en place depuis la clôture du lot 6, le
> 2026-09-06.** Les 337 fiches `role: brique` le portent. Ce qui suit s'est donc vérifié — à
> deux réserves près, écrites en ligne ci-dessous : la section `## Pièges` ne contenait
> **aucun** retour d'expérience, et « chaque exclusion doit pointer vers l'alternative » n'est
> pas contrôlable, faute d'alternative à pointer dans trois quarts des cas. Cf.
> `AI/migration/lot-6-gabarit.md`, remontées 3 et 7 de son journal.

- **`## Pourquoi`** devient `## Définition`. Le mot posait la mauvaise question : on ouvre une
  fiche pour savoir *ce que c'est*, pas *pourquoi elle existe*.
- **`## Quand l'utiliser` / `## Quand NE PAS l'utiliser`** fusionnent en un tableau. C'est une
  seule décision, elle se lit en une fois, et chaque exclusion **doit** pointer vers
  l'alternative — ce qui est contrôlable.
- **`## Déploiement & coût`** devient `## Mise en œuvre`, à étiquettes fixes. Mesure : 84,5 %
  des 297 sections contiennent le mot « gratuit », paraphrase de `licence_type: open-source`,
  mais 4,4 % seulement mentionnent une plateforme. La section reformulait le frontmatter et
  omettait ce que le frontmatter ne peut pas dire.
- **`## Pièges` est dissoute.** 337 sections remplies, ~~**une seule** contient une entrée
  datée~~ — **aucune, vérifié le 2026-09-06 sur les 337** : la fiche que cette phrase désignait
  portait une date de création de dépôt, pas un retour d'expérience au format
  `- YYYY-MM-DD — <symptôme> : <correctif>.`. Le vault n'a **aucun** REX daté, et aucune
  `## Retours` n'a été créée au lot 6. Le reste est de la limite de conception recopiée de la doc,
  et elle est décisionnelle : « Faker tire les champs indépendamment » n'est pas un piège, c'est
  le critère qui fait choisir SDV. Ces contenus remontent dans `## Définition` ou dans la
  colonne `Écarter si`. Une section `## Retours` n'existe **que** si une entrée datée existe.
- **`## Liens` se scinde.** Elle faisait trois métiers : navigation interne, doublon des
  alternatives (Mimesis apparaissait deux fois sur la page Faker), ressource externe. Elle
  devient `## Ressources` (externe, étiqueté) et `## Voir aussi` (navigation).

Réserve à tenir à l'œil : 331 puces `Liens` sur 336 portent déjà une étiquette, mais **286
valent « Doc »**. Typer les liens ne crée pas les tutoriels et les articles qui manquent —
c'est un travail d'enrichissement, page par page, pas un travail de format.

---

## 7. Gabarit — `role: notion`

Inchangé par rapport à la v2 : c'est le gabarit qui fonctionne (499 mots médians, structure
par parties, formules expliquées). La longueur reste libre.

```markdown
## Aperçu
## Concepts clés
## Les maths, simplement
## En pratique
## Approches voisines
## Pour aller plus loin
```

Deux ajouts seulement, pour l'uniformité du repérage : le **bandeau** en haut (`Domaine`,
`Prérequis`, `Voisines`) et les **liens typés** en bas, comme sur les briques.

---

## 8. Gabarit — `role: comparatif`

Un `.base` ne peut ni pointer vers ce qu'il compare, ni porter de couleur. Chaque comparatif
**est** donc une page `.md` qui **embarque** la vue — **les 47 le sont depuis la clôture du
lot 5, le 2026-09-06** :

```markdown
# Comparatif - Bases vectorielles

> On tranche sur : self-host possible, filtrage pendant la recherche, volume.

![[Comparatif - Bases vectorielles.base]]

## Ce qui départage

- [[Qdrant]] — filtrage payload appliqué pendant la recherche, pas après
- [[Weaviate]] — l'embedding est délégué à la base
- [[pgvector]] — le bon choix si du Postgres est déjà en place
```

Le `.base` reste, comme moteur de tableau, rangé à côté. La page porte le `role:`, la couleur,
les liens sortants et donc les backlinks. ~~Neuf comparatifs ne filtrent pas sur `categorie:` :
leur dossier d'accueil est à poser à la main~~ — **les neuf sont rangés depuis la clôture du
lot 3**, cf. la fin de `v3-arborescence.md`. Leur dossier n'est plus à poser : la page porte
une `categorie:`, et `check_arbo` en dérive le chemin comme pour toute autre page. C'est ce
qui rend la règle de majorité de `taxonomie.md` nécessaire, et le repli « au niveau du
domaine » parfois impraticable (lot 5, remontée 12).

**Syntaxe vérifiée** le 2026-09-04 : `![[X.base]]` embarque bien une vue dans une page.

~~**Variante à tester, 30 secondes dans Obsidian**~~ — **close le 2026-09-05, à deux
fichiers. Ne pas rouvrir.** La variante consistait à écrire la requête en bloc de code dans
la page, ce qui aurait supprimé les 47 `.base`. Le test annoncé au lot 0 n'a jamais été
exécuté, et l'identifiant exact du bloc n'a pas pu être confirmé en ligne : c'est la version
sûre — deux fichiers, la page embarquant la vue par `![[X.base]]` — qui a été retenue et
appliquée. Motif et trace du raisonnement : `AI/migration/lot-5-comparatifs.md`, *Décision
préalable*.

> Ce paragraphe restait rédigé au futur alors que la décision était prise : c'est le défaut
> décrit à la remontée 9 du lot 5 — une prose qui survit à ce qui l'invalide, et que rien ne
> signale. Il est corrigé ici parce que ce document est le premier que lit une session neuve.

---

## 9. Gabarit — `role: hub`

```markdown
# Bases de données

> Stocker et interroger de la donnée de façon durable.

## Ce qu'il faut comprendre        ← écrit à la main
- familles, compromis, quand basculer de l'une à l'autre

## Choisir                         ← écrit à la main
- l'arbre de décision du domaine, en quelques lignes

<!-- AUTO:START -->                ← généré
### Sous-domaines
- [[Vectoriel]] · [[Relationnel]] · [[Administration]] · [[Recherche]]
### Notions
- …
### Briques
- …
### Comparatifs
- …
<!-- AUTO:END -->
```

Le hub fusionne l'ancienne MOC générée et l'ancienne notion chapeau. C'est ce qui supprime la
collision de nom « Bases de données », seule collision du vault et symptôme visible du problème.

---

## 10. La règle d'insertion — le rayon de propagation

C'est le point le plus important de la v3, et c'est l'arborescence qui le rend possible.

### Le problème v2

Quand on ajoute une brique, il faut mettre à jour les pages qui doivent lui répondre. En v2,
« quelles sont les pages connexes ? » n'a **aucune réponse mécanique** : le skill doit les
deviner à partir des tags et de l'index. C'est le mécanisme derrière les omissions constatées
à l'axe 3 — sept étapes sur onze ne laissent aucune trace vérifiable.

### La règle v3

> **Le rayon de propagation d'une insertion est le dossier d'accueil, plus ses hubs parents.**

Insérer Qdrant dans `Bases de données/Vectoriel/` définit mécaniquement, sans deviner :

| À mettre à jour | Comment il est trouvé | Qui le fait |
|---|---|---|
| Le hub du dossier — `Vectoriel.md` | c'est le dossier d'accueil | généré |
| Les hubs parents — `Bases de données.md` | remontée de chemin | généré |
| Le comparatif du dossier | c'est le fichier `role: comparatif` du dossier | vue `.base` : automatique ; section « Ce qui départage » : à écrire |
| La notion du dossier — `Bases de données vectorielles.md` | c'est le fichier `role: notion` du dossier | à écrire |
| Les briques pairs — les 11 autres `role: brique` du dossier | contenu du dossier | à écrire, réciprocité obligatoire |
| Les pitchs réinjectés | `alternatives:` et `complements:` des pairs | script de resynchronisation |

Le voisinage cesse d'être une intuition : c'est `ls` du dossier.

### Ce que le validateur contrôle en dur

Ces règles rendent l'omission impossible plutôt qu'improbable. Elles sont vérifiables sans
lire le sens des pages.

> **État arrêté à la clôture du lot 8, le 2026-09-06.** Les dix règles sont écrites et
> mesurées. Sept sont dures, trois restent en avertissement — et le motif de chacune des
> trois est écrit ci-dessous, dans le code à côté de la règle, et dans le *Journal du lot 8*
> de `AI/migration/lot-8-durcissement.md`, qui porte le compte de violations avant
> durcissement. **Deux règles ont été réécrites**, parce que leur formulation d'origine
> était inatteignable : la mesure l'a montré, elle n'a pas été supposée.

| # | Règle | État | Code |
|---|---|---|---|
| 1 | **Réciprocité** — si A cite B en `alternatives:`, B cite A. Idem pour `complements:` | **dure** | R12, R18 |
| 2 | **Cohérence chemin / catégorie** — le dossier d'une page correspond à son `categorie:` | **dure** | `check_arbo.py` |
| 3 | **Complétude du dossier** — toute brique du dossier apparaît dans le hub du dossier | **dure** | R19 |
| 4 | **Voisinage déclaré** — une brique dont le dossier porte d'autres briques et dont `alternatives:` est vide est signalée | avertissement **définitif** | R20 |
| 5 | **Exclusion sourcée** — *réécrite au lot 8*, voir ci-dessous | **dure** | R21 |
| 6 | **Réinjection du pitch** — chaque puce d'`Alternatives` **et de `Compléments`** commence par le pitch courant de sa cible | **dure** | R1, R22 |
| 7 | **Étiquettes fermées** — `Mise en œuvre` porte ses cinq étiquettes ; `Ressources` pioche dans `{Documentation, Dépôt, Tutoriel, Article, Papier, Cours, Vidéo}` | **dure** sur `Mise en œuvre`, avertissement sur `Ressources` | R23 |
| 8 | **Pas de double citation** — *réécrite au lot 8*, voir ci-dessous | **dure** | R24 |
| 9 | **Bandeau à jour** — le bandeau généré concorde avec le frontmatter | **dure** | `build_bandeau.py --check` |
| 10 | **Anti-répétition** — `## Définition` ne recontient ni la famille, ni la licence, ni la maturité affichées par le bandeau | avertissement **définitif** | R26 |

#### Règle 5, réécrite — « exclusion sourcée »

> **Une cellule `Écarter si` qui REDIRIGE — c'est-à-dire qui porte une flèche — et dont la
> cible est une brique fichée dans le brain, porte le wikilink de cette brique.**

La formulation d'origine, « toute cellule `Écarter si` contient un wikilink », est
**inatteignable**, et aucun enrichissement ne la comblera : 357 cellules sur 1 388, soit
26 %, de 0 % à 44 % selon le domaine. La cause est le revers exact de la règle de conversion
du lot 6 — quand la redirection vers un concurrent part au comparatif, ce qui reste sur la
fiche est une **borne de la brique seule**, qui ne pointe vers personne : « le cache n'est
jamais purgé seul », « `max_elements` est fixé à l'initialisation ».

Les deux reformulations proposées par les lots ne tiennent pas **prises séparément**, et la
mesure le dit :

- *« toute exclusion qui nomme un besoin couvert par une autre brique porte son wikilink »* —
  **177 violations**. Elle confond nommer une brique et rediriger vers elle : « Centré
  Postgres : inutile dès qu'il faut toucher un autre moteur » nomme Postgres sans lui
  renvoyer qui que ce soit ;
- *« toute cellule dont le motif est une redirection porte un wikilink »* — **18 violations**,
  dont 5 flèches de **version** (`0.x → 1.x`) et 13 redirections vers une cible **hors
  brain** (`→ argparse`, `→ mypy`, `→ un wiki d'équipe`). Les exiger rendrait vingt-cinq
  outils non fichés obligatoires à ficher, ce qui n'est pas une décision de format.

C'est leur **conjonction** qui tient : la première donne la *position* (la flèche marque la
redirection, 345 cellules sur 1 388), la seconde donne la *condition* (la cible est couverte
par une brique). Sous cette forme : **1 violation**, réparée. La règle est dure.

Corollaire à ne pas rater : réécrire les 1 031 bornes restantes sous forme comparative pour
leur donner une cible ferait exactement ce que le lot 5 a passé quatre sessions à défaire.

#### Règle 8, réécrite — « pas de double citation »

> **Une même cible ne se LISTE pas dans deux sections de liste de liens** — `### Alternatives`,
> `### Compléments`, `## Voir aussi`. Une cible est « listée » quand elle est l'**entrée** d'une
> puce. La prose de `## Définition` et les cellules du tableau de décision citent librement.

La formulation d'origine est **arithmétiquement impossible** : la règle de conversion du
lot 6 *garde* la cible en `Écarter si` faute de comparatif d'accueil, et R11 *exige* qu'elle
figure en `### Alternatives`. Deux contraintes dures et contradictoires — **242 violations**
en lisant « toutes sections ».

La restriction aux **entrées de puce** n'est pas un assouplissement de confort : sans elle,
la règle punirait la forme que le lot 6 recommande pour une section `Alternatives` vide
(« Aucune outillée dans le brain : l'approche concurrente est [[Diff-in-Diff]] »), où le lien
explique au lieu de lister. Sous cette lecture : **0 violation sur 337**, et le défaut
d'origine est toujours attrapé — sur la page Faker, Mimesis apparaissait en `Alternatives`
**et** en `Liens`, deux listes de liens.

#### Les trois qui restent en avertissement, et pourquoi

- **Règle 4** (R20, 62 briques) — **par conception, et pour toujours.** Une brique peut
  légitimement n'avoir aucune alternative. La signaler aide, l'interdire mentirait.
- **Règle 7, moitié `Ressources`** (R23, 5 pages) — quatre `Site` et un `Poids`, qui ne sont
  pas des fautes de rédaction mais deux besoins que le vocabulaire ne couvre pas. La durcir
  demanderait d'ouvrir le vocabulaire, c'est-à-dire d'ajouter une exception pour faire passer
  la règle. L'arbitrage appartient à floSa.
- **Règle 10** (R26) — **non scriptable.** `production`, `paquet`, `modèle`, `application` et
  `open-source` sont des mots français ordinaires. Sur les seuls motifs bornés, la mesure
  donne 11 candidats dont **2 vrais** : « côté open source » chez PuLP parle des *solveurs*,
  « Application de bureau » ajoute « de bureau », « un annuaire de liens » est le cœur de la
  définition. Durcir rendrait la règle contournée, pas respectée. Elle sert de relecture
  assistée, et c'est tout ce qu'elle peut être.

#### Ce que le lot 8 a ajouté au-delà des dix

- **R8e** — l'angle mort de R8a, chiffré. R8a vérifie qu'une *catégorie* a un comparatif,
  jamais que ses *briques* y entrent. 89 briques sur 337 sont hors de toute vue ; 51 relèvent
  des 13 catégories que R8a signale, 38 lui sont invisibles. R8e ne signale que les **11**
  qu'une vue a laissées dehors alors qu'elle retient leurs pairs — la seule population qui
  soit réparable, en élargissant un filtre. Les 27 autres vivent dans une catégorie de 1 ou
  2 briques, où aucun comparatif n'a de sens : elles sont au backlog d'enrichissement, pas
  dans le validateur.
- **R14b** — l'absence de `famille:` devient visible sans devenir une faute. La rendre requise
  aurait contredit une décision écrite de `taxonomie.md` : un champ vide est le **seul** signal
  prévu pour « l'arbre de décision n'a pas tranché ». Ce qu'il fallait corriger n'était pas la
  permissivité, c'était le silence. 1 brique concernée.
- **R15 passe en dur** — « une brique porte au moins un lien vers une notion ou un hub ». Elle
  était souple tant que le passif de 102 fiches n'était pas résorbé ; le gabarit du lot 6 l'a
  fermé par construction, avec `## Voir aussi`.

---

## 11. Impact sur l'outillage

| Script | Ce qui change |
|---|---|
| `build_index.py` | `SCAN_DIRS` devient la racine ; `galaxie`/`type` → `role` ; indexe le chemin |
| `build_mocs.py` | ne génère plus `MOC/` mais les **zones AUTO des pages hub**, et les crée à la demande |
| `build_links.py` | inchangé sur le fond ; sa sortie `liens.md` est **masquée du graphe** |
| `check_brain.py` | les dix règles ci-dessus ; les enums `hosted`/`scaling` deviennent conditionnelles |
| nouveau — `build_bandeau.py` | compose le bandeau de chaque page depuis son frontmatter |
| nouveau — `check_arbo.py` | vérifie chemin ↔ `categorie:`, propose les déplacements |

Environ 37 occurrences de `Dev/` ou `Wiki/` en dur dans les scripts, et `galaxie` lu dans six
d'entre eux. Ce n'est pas un obstacle, c'est une liste.

---

## 12. Impact sur les trois skills

### `enrichir-brain`

C'est lui qui gagne le plus. Son étape « identifier les pages connexes », aujourd'hui
devinée, devient le §10 : lister le dossier d'accueil, remonter les hubs, mettre à jour ce que
la table nomme. La procédure passe d'une intention à une liste fermée, et sept de ses étapes
sans trace deviennent contrôlables.

### `planifier-projet`

Il interroge `brain-index.json`. Trois gains : `famille:` et `langage:` deviennent des
critères affichables — « pour fabriquer de la donnée : Faker, librairie Python » ; le tableau
`Prendre si / Écarter si` lui donne des critères structurés au lieu de prose à interpréter ;
le hub de domaine devient sa porte d'entrée naturelle pour une brique dont il ne connaît pas
le nom.

### `cloturer-brain`

Inchangé dans son principe. Il gagne les nouvelles règles du validateur et l'appel à
`build_bandeau.py`. Sa politique git reste la seule du vault.

---

## 13. Plan de migration

Progressif, un domaine à la fois, le vault restant utilisable entre chaque lot.

| Lot | Contenu | Réversible |
|---|---|---|
| 0 | Masquer `liens.md` du graphe ; masquer le panneau de propriétés | oui, réglages |
| 1 | Écrire la spec et l'arborescence, les valider | sans effet sur le vault |
| 2 | `role:` remplace `galaxie:`/`type:` ; suppression de `status` et `remplace_par` ; scripts adaptés | oui, un commit |
| 3 | Déplacement des fichiers, domaine par domaine, en commençant par **Bases de données** (47 pages, 0 notion à arbitrer) — **CLOS le 2026-09-05** : 20 domaines, puis « Métiers/ », « Patterns/ », « Rules/ » et le dernier comparatif transverse. `Dev/` n'existe plus | oui, `git mv` |
| 4 | Les notions à recatégoriser, par lots — **CLOS le 2026-09-05**. Les 297 sont dans l'arbre, les douze familles passées (`stats` 37, `math` 26, `data` 13, `signal` 5, `ai` 4, `llm` 56, `rl` 17, `ts` 13, `nlp` 7, `dl` 52, `ml` 67), les 10 `MOC/Concepts/` supprimées sur mesure, `Wiki/` et `MOC/` n'existent plus. `math` et `stats` sont passés en premier, pas `ml`/`llm` : ce sont eux qui exigeaient d'ouvrir du vocabulaire, et l'ordre s'est vérifié — `llm` a quand même dû en ouvrir trois | oui |
| 5 | Comparatifs `.base` → pages `.md` — **CLOS le 2026-09-06** : les 47 sont des pages `role: comparatif`, chacune à côté de son `.base`, dans le dossier que `categorie:` dérive. 258 puces, toutes sourcées dans une fiche. Quatre sessions, cf. les 27 *Remontées* de `AI/migration/lot-5-comparatifs.md` | oui |
| 6 | Conversion des fiches au nouveau gabarit, domaine par domaine — **CLOS le 2026-09-06** : les 337 briques y sont, `check_brain` passe de 149 à 28 avertissements, les 121 fermés sont tous des R15 que `## Voir aussi` ferme par construction. Seul lot mené **en parallèle** — un pilote, 17 conversations simultanées sans clôture, une intégration. 20 *Remontées* dans `AI/migration/lot-6-gabarit.md` | oui |
| 7 | Skills et règle de propagation — **fait**, cf. `AI/migration/lot-7-skills.md` | oui |
| 8 | Durcissement des règles du validateur restées en avertissement — **CLOS le 2026-09-06**, et la migration v3 avec lui. Les dix règles du §10 sont écrites et mesurées : sept dures, trois en avertissement à motif écrit, **deux réécrites** parce qu'inatteignables telles qu'elles étaient formulées. 28 avertissements avant, 111 après — la hausse est le but : 83 sont des règles qui n'existaient pas. Cf. le *Journal du lot 8* de `AI/migration/lot-8-durcissement.md` | oui |

Rien n'est irréversible : tout passe par git, un lot par commit, le validateur au vert à
chaque étape.

---

## 14. Questions ouvertes — toutes tranchées au 2026-09-06

> **Aucune de ces quatre questions n'est plus ouverte.** Trois sont tranchées, la quatrième
> l'est aussi mais laisse une dette explicitement **reportée**, avec son motif : renommer le
> champ `domaines:` toucherait 374 pages, l'index, `build_mocs.py` et six hubs, c'est-à-dire
> une migration à part entière — et la migration se clôt ici. La désambiguïsation, elle, est
> écrite : « domaine » = l'axe de l'arbre, « métier » = ce que `domaines:` porte.
> Le titre de section est conservé pour que les liens entrants ne cassent pas.


1. ~~**Les 5 `MOC/Themes`**~~ — **tranché le 2026-09-05 : gardés.** `domaines:` est
   renseigné sur 374 pages, et c'est le seul axe transverse à un arbre rangé par domaine
   technique : il porte les 5 axes métier de floSa. Les 5 pages sont descendues à la
   racine dans « **Métiers/** », `role: hub`, corps au gabarit §9 ; `build_mocs.py` les
   régénère depuis `domaines:` à leur nouveau chemin, périmètre inchangé. Les deux dettes qui restaient sont **tranchées à la clôture du lot 8, le 2026-09-06** :

   - **La collision de vocabulaire** entre le champ `domaines:` et le mot « domaine » de
     l'arbre (remontée 21) : le champ **garde son nom**, et le vocabulaire est fixé ici.
     « Domaine » désigne l'axe de l'arbre, celui que porte `categorie:` et que le dossier
     rend visible ; ce que porte `domaines:`, ce sont les **six métiers** de floSa, et c'est
     le mot à employer quand on en parle — le dossier s'appelle d'ailleurs « Métiers/ »
     depuis le lot 3. Renommer le champ toucherait 374 pages, l'index, `build_mocs.py` et
     les six hubs : c'est une migration à part entière, et la migration se clôt ici. Dette
     **reportée, sciemment**, avec sa désambiguïsation écrite — pas laissée ouverte.
   - **Le champ n'est pas requis sur `role: brique`** (remontée 22) : il **reste facultatif**,
     et c'est définitif. La mesure du 2026-09-06 donne **307 des 337 briques** sans
     `domaines:`. Le rendre requis reviendrait à attribuer un métier à 307 fiches — un
     travail de **contenu**, jamais de format, et le principe du lot 8 est qu'on ne durcit
     pas une règle que le vault viole encore. Les six hubs de « Métiers/ » se régénèrent très
     bien à partir des 30 briques qui le portent, plus les notions.
2. ~~**Les 18 notions sans domaine évident**~~ — **tranché le 2026-09-05, à la clôture du
   lot 4 : les 297 notions sont dans l'arbre**, les 18 comprises, arbitrées page par page.
   Les **9 comparatifs sans filtre `categorie`** sont réglés eux aussi, le dernier le
   2026-09-05. Ce qui suit est conservé parce que le *motif* reste instructif : attendre
   n'était pas neutre pour ces neuf-là, leur filtre croisant un
   chemin `Dev/Services/` avec un tag ou une liste de noms, donc leur vue **se vidait en
   silence** quand leurs membres descendaient, sans que le script de migration les voie.
   La substitution est partout la même, `role == "brique"`, et le relevé des membres des
   47 `.base` avant / après chaque domaine montre qu'elle est fidèle. Le dernier,
   « Frontends web légers », a été **rangé dans « Interfaces & apps data/ »** le
   2026-09-05 : trois de ses cinq membres y vivent, FastAPI et HTMX n'y figurent que
   comme l'option à la main. Cf. remontées 7, 14, 16 et 19 de `lot-3-arborescence.md`.
3. ~~**`Projects/`**~~ — **tranché le 2026-09-06, à la clôture du lot 8 : il reste hors de
   l'arbre des domaines.** Ce n'est pas un domaine de connaissance, c'est un journal de
   projets en cours ; il ne porte ni `categorie:` ni `role:`, et rien n'y est à ranger. La
   décision était déjà appliquée sans être écrite : `Projects/` figure dans le `NON_PAGES` de
   `check_brain.py`, de `check_arbo.py` et du hook `Stop`, donc aucune règle ne l'a jamais
   balayé. La question est close par ce que le code faisait déjà.
4. ~~**Le seuil de promotion à 5 pages**~~ — **tranché le 2026-09-04.** Le seuil reste à 5
   (à 4 il donnerait 34 sous-dossiers, à 8 il en donnerait 12), mais il est **plafonné** :
   un sous-domaine ne se promeut pas s'il ne laisse **aucune** page au niveau du domaine.
   Un dossier fils qui redouble son parent n'apporte aucune information et ajoute un
   niveau à la navigation. Le plafond vit dans `arbo.py` à côté du seuil, et il a été
   appliqué rétroactivement aux deux cas que le lot 3 avait produits —
   `Stockage/Stockage objet/` (6 pages sur 6) et `Automatisation no-code/No-code/`
   (5 sur 5) ont été défaits, leurs pages remontées au domaine et leurs sous-hubs
   fusionnés dans le hub de domaine. Cf. remontée 8 de `lot-3-arborescence.md`.
