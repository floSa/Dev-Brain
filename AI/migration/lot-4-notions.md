---
galaxie: meta
nom: lot-4-notions
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 4 — Recatégorisation des 205 notions

Effort : **deux à trois sessions**, par lots de domaine. C'est le **seul poste de travail non
mécanique** de toute la migration.

Prérequis : lot 3 fait pour le domaine concerné.

> **État au 2026-09-05 — sept familles sur douze sont faites.** Le pilote
> « Statistiques & inférence » (37 notions), puis une deuxième conversation —
> **mathématiques (26), data (8 sur 13), signal (5), sécurité IA (4)** —, puis une
> troisième qui a fermé `data` (les **5 remontées**) et traité **`llm` (56)**. Soit
> **141 notions rangées**, 12 sous-dossiers créés, 10 valeurs de catégorie ouvertes,
> 7 valeurs retirées du vocabulaire (6 `concept/*` et `llm/mcp`), 7 MOC supprimées.
> Il reste **156 notions** sous `Wiki/Concepts/` — `dl` (52), `ml` (67), `rl` (17),
> `ts` (13), `nlp` (7) — et **3 MOC** vivantes.
>
> Les *Remontées* en fin de document sont la méthode telle que le terrain l'a corrigée. Les
> dix premières viennent du pilote — lire les nº 1, 3 et 5 avant d'attaquer un domaine. Les
> suivantes (11 à 19) viennent de la deuxième conversation ; la **nº 11 est la plus
> importante du lot**. La nº 20 à 22 viennent de la fermeture de `data`, la nº 23 du
> retrait de `concept/devops`, et les **nº 24 à 28 du domaine `llm`** — dont la nº 24, qui
> dit ce que l'étape 0 ne sait PAS faire, la nº 25, où le seuil ne doit pas non plus
> RETENIR un rangement, et la nº 26, sur les quatre ensembles à croiser pour nommer un
> dossier.

## Contexte

Les deux galaxies utilisent deux vocabulaires pour le même territoire : **94 sous-domaines**
côté Dev, **11** côté Wiki. En fusionnant l'arbre :

| Situation | Nombre |
|---|---|
| Notions qui tombent directement dans un sous-dossier existant | 89 |
| Notions qui tombent sur le bon domaine mais **sans sous-domaine** | 187 |
| Notions dont le domaine lui-même reste à déterminer | 18 |

Sans ce lot, `Machine Learning/` porterait 67 notions à plat et `LLM/` 57 — exactement le tas
que la v3 cherche à supprimer.

> Le pilote a montré que ce tableau **sous-estime le travail de vocabulaire**. Les 37 notions
> de statistiques y étaient comptées dans la deuxième ligne, « bon domaine, sans
> sous-domaine » — vrai, mais 10 d'entre elles n'avaient aucune valeur existante où tomber :
> il a fallu en ouvrir deux. À rejouer sur `math` (26), dont la deuxième ligne cache
> vraisemblablement le même besoin.

Liste nominative, avec cases à cocher : [[AI/design/v3-arborescence|v3-arborescence]],
sections *À arbitrer* de chaque domaine et *Hors arbre*.

## Périmètre

- Le champ `categorie:` des 205 notions listées, et leur emplacement.
- Le vocabulaire de `Documentation/general/taxonomie.md`, à **étendre** : le vocabulaire Dev
  ne couvre pas les mathématiques ni les statistiques théoriques, qui portent à elles seules
  63 notions.

**Hors périmètre** : le corps des notions, les briques, les comparatifs.

## Procédure

### Par domaine, dans cet ordre

`math` (26) et `stats` (37) d'abord — ce sont eux qui exigent de créer du vocabulaire, et il
vaut mieux le faire à froid. Puis `llm` (57), puis `ml` (67). Les 18 sans domaine en dernier,
une fois que le vocabulaire final est connu.

- [x] **`stats` (37) — fait le 2026-09-05.** L'ordre s'est vérifié : deux valeurs nouvelles
      ont été nécessaires, et il a fallu écrire leur frontière contre `math/*` avant de
      savoir où rangeaient six notions. Le faire après `ml` aurait obligé à y revenir.
- [x] **`math` (26) — fait le 2026-09-05.** Trois valeurs ouvertes
      (`math/algebre-lineaire`, `math/information`, `math/theorie-apprentissage`), une
      élargie (`math/optimisation`), quatre sous-dossiers, zéro page au niveau du domaine.
      L'ordre s'est vérifié une seconde fois : la frontière `stats/probabilite` ↔ `math/*`
      écrite au pilote a tenu sans être rouverte. **Le corps du hub a rangé les 26 seul** —
      ses quatre puces les citaient déjà toutes, une fois chacune.
- [x] **`data` (13) — CLOS le 2026-09-05, en deux passages.** Premier passage, par
      famille d'origine : 8 rangées, une valeur ouverte (`data/fiabilite`), aucun
      sous-dossier créé, **5 remontées** parce qu'elles appellent `database/*` ou
      `devtools/notebook`, hors du périmètre de ce lot-là. Second passage, **par domaine
      d'accueil** comme la remontée 15 le suggérait : les 5 sont descendues dans
      « Bases de données/ » (4) et « Outils de développement/ » (1), aucune valeur
      ouverte, aucun sous-dossier promu ni défait. `concept/data` est **sorti du
      vocabulaire**, et `MOC/Concepts/Données (notions)` est morte avec lui.
- [x] **`signal` (5) — fait le 2026-09-05.** Aucune valeur ouverte ; `Traitement/` naît,
      exactement comme `v3-arborescence.md` le décrivait depuis le lot 3.
- [x] **`ai` (4) — fait le 2026-09-05.** Une valeur ouverte, `security/ia`, et c'est
      l'arbitrage le plus discutable du lot : il va **contre** l'arbre de décision du
      domaine (cf. remontée 13).
- [x] **les 5 notions `concept/data` remontées — fait le 2026-09-05** (cf. `data`
      ci-dessus, second passage)
- [x] **`llm` (56) — fait le 2026-09-05.** Trois valeurs ouvertes (`llm/modele`,
      `llm/prompt`, `llm/protocole`) et une **retirée**, `llm/mcp`, que la troisième
      remplace — premier cas du lot où une valeur de brique est recatégorisée.
      **Six sous-dossiers créés** dans le domaine, un septième dans « Sécurité » :
      55 notions descendent ici, la 56e (`Sandboxing de code généré`) va en
      `security/ia` et l'y fait franchir le seuil. L'étape 0 a rangé 35 notions
      sur 56 ; les 21 autres l'ont été par leur section `## Approches voisines`
      (remontée 24)
- [ ] `dl` (52) · [ ] `ml` (67) · [ ] `rl` (17) · [ ] `ts` (13) · [ ] `nlp` (7)

### Pour chaque notion

0. **Lire d'abord le corps du hub du domaine.** Il porte souvent le critère qui départage
   les notions, écrit par quelqu'un qui connaissait le domaine — sur `stats`, la phrase
   « l'analyse factorielle vise l'interprétation des axes, pas la performance d'un modèle en
   aval » a rangé 13 notions à elle seule. Aucun tag n'aurait fait ça (remontée 1).
1. Lire la page — son titre, son `## Aperçu`, ses tags, ses liens sortants. **La page prime
   sur ce que les hubs disent d'elle** : deux hubs annonçaient `Réduction de dimension` comme
   une page de ML, son contenu est le panorama de l'école factorielle (remontée 2).
2. Dériver le sous-domaine par l'arbre de décision de `taxonomie.md`, **pas à l'intuition**.
3. Si aucune valeur existante ne convient : **proposer** une valeur nouvelle, ne pas
   l'inventer seule. Les propositions sont regroupées et soumises à floSa par lot, pas une
   par une.
4. Appliquer la règle de promotion à 5 pages : un sous-domaine qui atteint le seuil devient un
   dossier, sinon la notion reste au niveau du domaine. Deux pièges, tous deux vérifiés sur le
   pilote : le seuil ne doit **jamais** motiver le choix d'une catégorie (remontée 4), et une
   notion qui part vers un **autre domaine** peut y franchir le seuil et forcer une
   restructuration hors périmètre — le compter avant de décider (remontée 3).
5. Après les `git mv` : régénérer, puis **comparer les artefacts avant / après**. Les
   validateurs ne voient pas ce qui a été perdu, seulement ce qui est faux (remontée 5).

### Les 18 sans domaine — **les 18 traitées le 2026-09-05**

La prévision « la plupart sont évidentes une fois posée la question de quoi ça parle » s'est
vérifiée, et c'est justement ce qui a rendu 5 d'entre elles intraitables dans leur lot :
elles étaient évidentes, mais **pour un autre domaine**. `ORM` → `database/orm`,
`Migrations de schéma` → `database/migration`, `Bases de données vectorielles` et
`Index ANN — internes` → `database/vecteur`, `Notebooks-as-code` → `devtools/notebook`.
Consigne de floSa appliquée : une notion qui appelle un sous-domaine hors du périmètre du
lot **se remonte, elle ne se déplace pas**. Effet de seuil mesuré pour les cinq avant de
décider — il est nul, aucune ne forcerait de restructuration. **Les cinq sont descendues
le 2026-09-05**, dans un second passage pris par domaine d'accueil, la mesure de seuil
refaite sur la population réelle des deux domaines et non reprise du lot précédent : les
ensembles de sous-domaines promus sont identiques avant et après, pour l'un comme pour
l'autre. Le script s'arrête de lui-même si ce n'est pas le cas
(`AI/migration/scripts/migrate_lot4_residus.py`).

`Web scraping` → `data/scraping` est la seule des cinq « évidentes » qui restait dans son
domaine ; elle est descendue.

Les notions de sécurité IA n'avaient effectivement pas de domaine : tranchées en
`security/ia` par floSa, contre l'arbre de décision. Cf. remontée 13.

## Critères d'acceptation

Ils se vérifient **par domaine**, pas seulement à la fin — c'est ce qui permet de clore un
domaine à la fois. Entre parenthèses, l'état du pilote `stats`.

- [ ] Aucune notion ne reste sur une `categorie: concept/*`. *(stats, math, signal, ai :
      fait, et les quatre valeurs sont retirées du bloc de `taxonomie.md` — laisser une
      valeur sans page autorise une rechute silencieuse. **`data` est l'exception** : 5 de
      ses 13 notions sont remontées, la valeur reste, et l'exception est écrite à côté
      d'elle dans `taxonomie.md`)*
- [ ] Toute valeur nouvelle de `categorie:` est écrite dans `taxonomie.md` avec sa frontière,
      et son libellé de dossier est ajouté à `DOM_LABEL` ou `SUB_LABEL`. *(stats : fait pour
      `stats/probabilite` et `stats/experimentation` ; ce dernier reste sous le seuil, donc
      sans libellé — c'est voulu, `promotions()` lèvera un KeyError le jour venu)*
- [ ] Chaque notion est dans le dossier que sa catégorie implique. *(stats : `check_arbo.py`
      vert — et penser aux **briques** que la promotion d'un sous-domaine déplace aussi)*
- [ ] Les cases de `v3-arborescence.md` sont cochées au fur et à mesure. *(stats : la section
      du domaine est réécrite avec les quatre sous-dossiers)*
- [ ] `check_brain.py` au vert **et** `check_arbo.py` au vert, sans que le compteur
      d'avertissements augmente. *(stats : 149 avant, 149 après)*
- [ ] Les artefacts générés sont comparés **avant / après** le déplacement, et pas seulement
      revalidés — cf. remontée 5, où `Métiers/` avait perdu une ligne sans qu'aucune règle
      s'en aperçoive.
- [ ] **Le jeu d'avertissements est comparé ligne à ligne, pas seulement son compte.** Une
      BAISSE du compteur est un signal, pas un progrès : c'est ainsi que la remontée 11 a
      été trouvée. *(les quatre domaines du 2026-09-05 : diff vide à chaque commit, sauf le
      chemin d'un `.base` déplacé)*
- [ ] Une `MOC/Concepts/` ne se supprime qu'après **mesure** que zéro notion ne dépend
      d'elle seule pour sa R7, et que `build_mocs.py` ne la régénère plus. La mesure va dans
      le message de commit. C'est la seule exception à « aucun `rm` sur une page ».

## Interdictions

- **Ne jamais inventer une valeur de catégorie en silence.** Une valeur hors vocabulaire est
  une faute ; une proposition explicite est le comportement attendu.
- Ne pas réécrire le corps d'une notion. Ce lot range, il n'édite pas.
- Ne pas traiter plus d'un domaine par conversation — le contexte sature et la qualité de
  l'arbitrage tombe sans signal.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md, AI/design/v3-arborescence.md puis
AI/migration/lot-4-notions.md.

Traite le domaine <NOM DU DOMAINE> uniquement.

Pour chaque notion, dérive le sous-domaine par l'arbre de décision de
Documentation/general/taxonomie.md. Regroupe tes propositions de valeurs nouvelles
et pose-les-moi en une fois avant d'écrire quoi que ce soit.

Clôture avec le skill cloturer-brain.
```

---

## Remontées — domaine pilote « Statistiques & inférence », 2026-09-05

37 notions rangées, 4 sous-dossiers créés, 9 briques déplacées par ricochet, 2 valeurs de
catégorie ouvertes. Aucune violation dure à aucun moment, et le compteur d'avertissements
n'a pas bougé : **149 avant, 149 après**.

### 1. La projection `concept/<sub>` → `<domaine>/<sub>` est fausse ICI AUSSI, autrement

La remontée 20 du lot 3 annonçait le piège pour `concept/dl`, dont le découpage wiki est plus
grossier que le découpage Dev. Sur `concept/stats`, le problème est **l'inverse et pire** : il
n'y avait rien à projeter. Le tableau de `v3-arborescence.md` listait les 37 comme « À
arbitrer — sans sous-domaine », et les 4 valeurs `stats/*` existantes ne couvraient ni la
probabilité ni l'expérimentation. Une projection mécanique aurait produit 37 pages à plat dans
le domaine — exactement le tas que la v3 supprime.

La mesure qui a servi de garde-fou est **le tag, croisé contre les deux galaxies** :
`dimensionality-reduction` est porté par 10 notions `concept/stats` (PCA, CA, MCA, FAMD, MFA,
GPA, PGA, HCPC, Manifold learning, Réduction de dimension) **et** par 3 notions `concept/ml`
(ICA, NMF, t-SNE and UMAP). La frontière v2 entre galaxies passait donc déjà au milieu d'une
famille homogène, sans que rien ne le signale. Suivre le tag aurait mélangé les deux ; suivre
la galaxie aurait été arbitraire.

Ce qui a tranché est une phrase du **corps du hub**, écrite au lot 3 : « l'analyse factorielle
vise l'interprétation des axes, pas la performance d'un modèle en aval ». C'est un critère
opérationnel, et il range les 13 sans hésitation. **Leçon pour les 260 notions restantes :
avant d'arbitrer un domaine, lire le corps de son hub — il contient souvent le critère, écrit
par quelqu'un qui connaissait le domaine, et il vaut mieux que n'importe quel tag.**

### 2. Une page dont deux hubs annoncent le contraire de son contenu — `Réduction de dimension`

Le hub de « Statistiques & inférence » la désignait comme « la Réduction de dimension du ML »,
par opposition à l'analyse factorielle. Le hub de « Mathématiques » la cite « pour le
panorama ». Les deux citations poussaient à l'envoyer en `ml/non-supervise`.

La page dit autre chose. Son arbre de décision ne nomme que PCA, CA, MCA, FAMD, MFA, GPA, PGA
et HCPC — les méthodes de `Prince` —, et sa bibliographie est Husson, Lê et Pagès, c'est-à-dire
FactoMineR. C'est le **panorama de l'école factorielle**, qui mentionne la branche ML sans en
relever. Elle est donc rangée en `stats/exploratoire`, et la phrase du hub a été corrigée pour
nommer la branche ML par ses vraies pages (`t-SNE and UMAP`, `ICA`, `NMF`) plutôt que par elle.

**Deux citations concordantes de hubs ne valent pas une lecture de la page.** Le relevé de
terrain de la remontée 20 est un bon signal, pas une preuve.

### 3. Ranger correctement une notion peut forcer un dossier dans un domaine hors périmètre

`Manifold learning` a ses voisines directes (`t-SNE and UMAP`, `ICA`, `NMF`) en `concept/ml` et
ses briques d'ancrage (`umap-learn`, `PaCMAP`) dans « Machine Learning ». La ranger en
`ml/non-supervise` était défendable — et aurait fait passer ce sous-domaine de 4 à 5 pages,
donc **franchir le seuil** : `arbo.py` aurait promu « Machine Learning/Non supervisé/ », avec
`PaCMAP`, `PyOD`, `hdbscan` et `umap-learn` à déplacer et un sous-hub à écrire, dans un domaine
dont les 67 notions ne sont pas arbitrées.

Le seuil n'est pas négociable page par page : il se compte sur la population du domaine, et
`arbo.py` l'applique seul. **Donc une notion qui traverse une frontière de domaine peut
déclencher une restructuration ailleurs, et il faut le mesurer AVANT de décider, pas le
découvrir après le `git mv`.** Arbitrage de floSa : elle reste en `stats/exploratoire`.

À rejouer sur chaque lot : compter, pour chaque notion candidate au départ, la population du
sous-domaine d'accueil dans l'autre domaine.

### 4. Le seuil ne doit pas décider de la catégorie — le cas `Analyse de puissance`

`stats/experimentation` comptait 4 notions, une sous le seuil. « Analyse de puissance » y
aurait tenu sur le fond (dimensionner un test, c'est le concevoir) et aurait fait exactement 5,
donc un dossier « Expérimentation ».

Le terrain dit non : les 4 autres portent le tag `experimentation`, elle non — elle porte
`statistical-power`, `hypothesis-testing`, `effect-size`. Elle est donc en `stats/inference`,
et `stats/experimentation` reste au niveau du domaine.

**Le seuil est une conséquence du rangement, jamais son motif.** Un arbitrage qui produit
« exactement 5 » mérite d'être relu une fois de plus, dans les deux sens.

### 5. Descendre des notions ÉRODE `Métiers/`, et aucune règle ne le voit

Effet mesuré immédiatement après le `git mv` : la ligne « Statistiques — 37 notion(s) » a
**disparu** de `Métiers/Data Science.md`. Cause : la boucle `Métiers/` de `build_mocs.py`
comptait les seules pages `Wiki/` — périmètre v2, que le lot 3 avait laissé tel quel en notant
que « le lot 4 devra le rebâtir sur l'arbre ».

Rien ne l'aurait signalé. R7 tient toujours, puisque les notions sont citées par le hub de leur
dossier ; `check_arbo` ne regarde que les chemins ; le compteur d'avertissements ne bouge pas.
**Chaque lot de domaine aurait donc retiré une ligne des 5 hubs métier, en silence, jusqu'à ce
qu'ils soient vides.** C'est le pire profil de défaut : progressif, invisible, et sur la seule
vue transverse du vault.

Correctif appliqué dans le même lot, parce que le reporter aurait laissé courir l'érosion : une
page groupe désormais par **son** hub — le sous-hub `MOC/Concepts/` tant qu'elle est sous
`Wiki/`, le dossier de domaine une fois descendue. Les bullets comptent des « page(s) » et non
plus des « notion(s) », un groupe de l'arbre mêlant notions et briques.

**Règle générale pour les lots 5 et 6 : après un déplacement, comparer les artefacts générés
avant/après, et pas seulement le retour des validateurs. Un validateur vert prouve qu'aucune
règle écrite n'est violée, pas que rien n'a été perdu.**

### 6. Le correctif de la remontée 5 a fait apparaître un SIXIÈME hub métier

Conséquence non anticipée, à confirmer par floSa : une fois l'arbre compté, `build_mocs.py` a
généré `Métiers/Infrastructure & Ops.md`, aussitôt signalé en **violation dure R7** — page
atteignable depuis rien.

Ce n'est pas une invention du script. `Documentation/general/themes.md` déclare `infra-ops`
depuis le **2026-09-02**, avec son motif écrit (« aucun des cinq n'accueillait honnêtement un
moniteur de trafic réseau »). Simplement, **aucune notion `Wiki/` ne le portait**, donc sa page
n'avait jamais pu naître : le périmètre v2 masquait un axe que la gouvernance déclarait déjà.
Trois briques le portent — `Sniffnet`, `croc`, `osint4all`.

Il est câblé dans `Home.md`, qui annonce désormais 6 axes, et `CLAUDE.md` suit.
~~**À trancher : garder 6 axes, ou retirer `infra-ops` de `themes.md`.**~~ — **tranché le
2026-09-05 : les 6 axes sont confirmés, `infra-ops` compris.** Motif de floSa : il est
déclaré dans `themes.md` depuis le 2026-09-02, c'est une décision prise et non un accident ;
3 briques le portent ; et pour une spécialité on-prem c'est l'axe le plus concret des six.
Les 5 « domaines de prédilection » de `CLAUDE.md` décrivent l'identité de floSa, pas la
taxonomie du vault — les deux listes n'ont pas à coïncider.

Leçon plus large : **un générateur dont le périmètre est plus étroit que la gouvernance ne
signale pas l'écart, il le cache.** Ici l'écart a tenu trois jours ; sur un champ moins visible
il aurait tenu indéfiniment.

### 7. `MOC/Concepts/Statistiques.md` a rempli sa condition de mort, et n'est pas morte

La condition posée par le lot 3 (remontée 23) était : cette MOC ne meurt qu'une fois ses
notions citées par un hub. Mesure faite avant et après, page par page, sur les 37 :

| Atteignable (R7) par | Avant | Après |
|---|---|---|
| un hub de l'arbre | 11 | **37** |
| `MOC/Concepts/Statistiques.md` seulement | **26** | **0** |
| rien | 0 | 0 |

La condition est donc remplie. La page **n'a pas été supprimée** : la migration v3 n'autorise
aucun `rm` sur une page, et une suppression se demande — c'est le traitement déjà appliqué à
`MOC/Concepts/Gestion des connaissances.md` au lot 3. Elle n'est plus régénérée non plus (la
boucle `MOC/Concepts` ne voit que les pages `Wiki/`, et plus aucune ne porte `concept/stats`) :
elle est **figée**, avec 37 liens nus qui résolvent encore.

~~**À décider par floSa, et la réponse vaudra pour les 9 autres**~~ — **tranché le
2026-09-05 : au fil des lots, et seulement sur mesure.** Une `MOC/Concepts/` se supprime dès
que la mesure R7 est remplie **et** que `build_mocs.py` ne la régénère plus ; la mesure va
dans le message de commit. C'est la seule exception à « aucun `rm` sur une page » de la
migration v3, et elle est conditionnée à cette mesure, jamais à l'intuition. Cinq sont
mortes le jour même ; il en reste 5. Cf. remontée 18.

### 8. Le libellé d'un sous-dossier n'est pas le nom de sa catégorie

Deux des quatre libellés s'écartent volontairement de la catégorie qu'ils portent :

- `stats/inference` → « **Tests & estimation** » et non « Inférence », pour deux raisons
  cumulées : « Inférence » est déjà un alias du hub « Serving » — même `role:`, donc un
  avertissement **R5 de plus**, alors que la clôture demande que le compteur n'augmente pas —
  et le mot redoublerait le nom du domaine parent, « Statistiques & inférence ».
- `stats/exploratoire` → « **Analyse factorielle** », qui nomme la population réelle (Prince,
  Fanalysis, et les huit variantes de la SVD) là où « Exploratoire » se confondrait avec
  `data/eda`.

C'était déjà le cas au lot 3 (`data/tableau` → « DataFrames », `database/vecteur` →
« Vectoriel »), mais sans que la raison soit écrite. **Vérifier l'unicité du nom de hub à la
casse près, et le croiser contre les `alias:` du même rôle, fait partie du choix du libellé —
pas seulement contre les noms de fichiers.**

### 9. Ce que le pilote dit du budget des 260 notions restantes

Le lot annonçait « deux à trois sessions » pour 205 notions. Le pilote en a rangé 37, et le
coût s'est réparti autrement que prévu : la lecture des 37 pages est rapide et largement
mécanisable ; **l'écriture des 4 sous-hubs est le vrai poste**, et il est proportionnel aux
confusions à lever, pas au nombre de pages — c'est la remontée 17 du lot 3, confirmée.
« Probabilités » (6 pages) a demandé autant de travail que « Tests & estimation » (15), parce
qu'il fallait justifier pourquoi ces pages ne sont pas dans « Mathématiques ».

Extrapolation honnête : `ml` (67) et `llm` (57) créeront des sous-dossiers dans un domaine
**déjà pourvu de 9 et 6 sous-hubs**, où la question ne sera pas « quel dossier créer » mais
« ces notions entrent-elles dans les dossiers existants ». C'est un travail différent, et
probablement moins cher par page. Les 18 sans domaine, en revanche, resteront chères à l'unité.

### 10. Le correctif `langage:` a été fait ici, dans un commit isolé

La remontée 2 du lot 7 laissait le choix entre le lot 8 et « un commit isolé de trois lignes ».
C'est le commit isolé, passé avant le lot pour qu'il reste inspectable seul : `langage` est
dans `build_index.FIELDS`, `query_index.py` porte `--langage` et le renvoie par défaut, et
`planifier-projet` décrit le filtre au lieu de la lecture de fiche. 322 des 697 pages portent
le champ. Réserve écrite dans le skill : `langage:` est une enum **ouverte**, donc un filtre
exact ne trouve pas une brique écrite « C++ / Python » quand on demande « Python » — `Stan` est
dans ce cas.

---

## Remontées — quatre domaines, 2026-09-05

`math` (26), `data` (8 sur 13, 5 remontées), `signal` (5), `ai` (4). Soit **43 notions
rangées**, 5 sous-dossiers créés, 3 briques déplacées par ricochet, 1 comparatif déplacé,
5 valeurs de catégorie ouvertes, 4 valeurs `concept/*` retirées, 5 MOC supprimées.
Aucune violation dure à aucun moment. Le compteur d'avertissements est revenu à **149**,
son niveau d'avant le lot — après être passé par 148, et c'est cette baisse qui a révélé
la remontée 11.

### 11. Un comparatif absorbait les notions, et le validateur devenait plus SILENCIEUX

**La remontée la plus importante du lot, et elle date du pilote.**

Jusqu'au lot 3, un `.base` qui filtrait `categorie == "<dom>/<sub>"` ne pouvait sélectionner
que des **briques** : les notions portaient `concept/*`, un vocabulaire disjoint. Le lot 4
supprime cette disjonction — une notion se range désormais sur la même `categorie:` que les
briques de son dossier. Chaque vue de comparatif sans clause de rôle absorbe donc, en
silence, les notions de son sous-domaine.

Mesure au moment de la découverte : **39 des 47 comparatifs** filtrent une catégorie sans
clause de rôle, et **2 étaient déjà corrompus, 45 pages absorbées** —
`Comparatif - Outils stats` (47 membres dont 37 notions, **depuis le pilote du 2026-09-05**,
sans que rien ne le signale) et `Comparatif - Solveurs d'optimisation` (9 membres dont 8).

Ce que R8 ne peut pas voir, et c'est le cœur : **R8b ne se plaint que d'un comparatif à
MOINS de deux membres**. Ajouter des membres le rend plus silencieux. Le défaut a donc le
profil de la remontée 5 — progressif, invisible — plus une propriété pire : il **améliore
le compteur en dégradant le vault**. Concrètement, `Comparatif - Solveurs d'optimisation`
n'avait qu'un membre et déclenchait R8b ; en absorbant 8 notions il est passé à 9 membres,
et l'avertissement a disparu.

Il a été trouvé parce que le compteur est passé de **149 à 148**. Aucun validateur, aucune
règle, aucun `git diff` ne le disait.

> **Règle qui en sort, et elle complète la remontée 5 :** comparer le **jeu**
> d'avertissements ligne à ligne, pas son compte. Une baisse est un signal à expliquer
> avant d'être un progrès à encaisser. Un avertissement qui disparaît sans qu'on l'ait
> corrigé décrit toujours quelque chose.

Correctif appliqué dans le même lot, en commit isolé : `role == "brique"` ajouté au filtre
des 39 (`AI/migration/scripts/patch_bases_role.py`, mesure par
`AI/migration/scripts/mesure_bases_role.py`, qui réutilise l'évaluateur de filtres de
`check_brain` pour avoir exactement la même sémantique). C'est la substitution que le lot 3
avait déjà appliquée à 9 comparatifs (remontées 7, 14, 16). Elle est fidèle par
construction — un ET strict avec un prédicat vrai pour toute brique ne peut retirer aucune
brique — et vérifiée après : 0 page absorbée contre 45.

**Pour les lots 4 restants** : c'est fait, il n'y a rien à refaire. Mais le mécanisme mérite
d'être retenu, parce qu'il se rejouera à l'identique **au lot 5**, quand les 47 `.base`
deviendront des pages `role: comparatif` : une page de comparatif portera une `categorie:`
et entrera à son tour dans le champ des filtres.

### 12. L'étape 0 ne fait pas qu'aider — sur « Mathématiques », elle a tout fait

Le pilote avait établi que le corps du hub range mieux que les tags. Sur « Mathématiques »,
c'est plus fort que ça : ses **quatre puces citent les 26 notions nommément, une seule fois
chacune**. C'est une partition exacte, écrite au lot 3 par quelqu'un qui connaissait le
domaine. Il n'y avait rien à arbitrer, seulement à lire — et à vérifier page par page que la
partition tenait, ce qu'elle a fait sur 25 cas sur 26.

Le vingt-sixième est instructif : `Optimal transport` porte le tag `optimization`, et le hub
le range en théorie de l'information. Le hub a raison — la page ouvre sur « un problème
d'optimisation linéaire » mais enchaîne sur « fournit une géométrie sur l'espace des
distributions », et sa valeur optimale **est** la `Wasserstein distance`, qui porte le tag
`information-theory`. Les séparer aurait mis dans deux dossiers une page et le nombre
qu'elle calcule.

**Conséquence pratique pour `ml` (67) et `llm` (56)** : lire le corps de leur hub *avant*
d'ouvrir la moindre notion, et compter combien de notions y sont déjà citées nommément. Sur
`llm`, le corps du hub en cite déjà plusieurs dizaines. Le travail restant n'est peut-être
pas « arbitrer 56 notions » mais « vérifier 56 arbitrages déjà écrits », ce qui est un
travail différent et bien moins cher.

### 13. Le seul arbitrage du lot qui va CONTRE l'arbre de décision — `security/ia`

Les 4 notions `concept/ai` sont un cas que la procédure ne pouvait pas trancher seule, et
elle le disait déjà (« c'est une **vraie** décision, à remonter »).

Tout pointait vers `llm/*`. L'arbre de décision du domaine met **D1** (« a besoin d'un grand
modèle de langage ») avant **D9** (« porte sur la sécurité ») ; les quatre pages ne parlent
que d'applications LLM et pointent vers `Guardrails`, `Structured outputs`, `RAG`,
`tool-use`, `mcp-protocol` ; et les **deux hubs concernés se répondaient dans ce sens** —
celui de « LLM & IA générative » les revendiquait nommément, celui de « Sécurité » écrivait
qu'elles « ne sont pas descendues ici ». C'est le cas de figure le plus solide qu'un
arbitrage automatique puisse produire.

Arbitrage de floSa : **`security/ia`**, contre tout ça. Deux raisons, toutes deux écrites
dans `taxonomie.md` à côté de la valeur :

- ces pages portent `concept/ai` et non `concept/llm` — **la famille large a été choisie
  exprès** quand elles ont été écrites, et l'information était dans le champ depuis le
  début ;
- la sécurité est une **pratique qui traverse les modèles**, pas un sous-sujet de l'IA
  générative.

Ce n'est pas un effet de seuil, et ça a été mesuré avant de décider : 3 → 7 pages ne promeut
aucun sous-dossier dans « Sécurité ».

**Ce que ça apprend sur l'arbre de décision** : son ordre D1 → D14 encode « ce dont l'objet
a besoin pour tourner », ce qui est le bon critère pour une **brique** — sans LLM, WrenAI ne
produit aucun SQL. Pour une **notion**, le critère pertinent est plutôt « de quelle pratique
ça relève », et les deux divergent ici. À rejouer sur les 56 notions `llm` : combien d'entre
elles sont, comme celles-ci, la théorie d'une pratique plus large qui a son propre domaine ?

### 14. Un hub qui annonce une page qu'il n'a plus ne se répare pas tout seul

Corollaire opérationnel de la 13, et il vaut pour tous les lots restants. La zone
`<!-- AUTO -->` d'un hub se régénère ; **son corps non**. Les deux phrases qui plaçaient les
notions de sécurité IA — l'une dans le hub LLM, l'autre dans le hub Sécurité, chacune
renvoyant à l'autre — seraient restées fausses indéfiniment après le `git mv`, et
`check_brain` n'aurait rien vu : R7 tient, les liens résolvent, rien n'est mort.

C'est le symétrique exact de la remontée 2 : là, un hub disait d'une page quelque chose que
son contenu contredisait ; ici, un hub dit d'une page qu'elle est ailleurs qu'où elle est.
Dans les deux cas, seule la lecture le voit.

**Geste à faire systématiquement** : après les `git mv` d'un domaine, `grep` le nom de
chaque page déplacée dans les corps de hub, et relire les phrases qui la citent. Trois hubs
ont été réécrits à ce titre dans ce lot — « Mathématiques » (réduit : il n'énumère plus les
26 notions, il aiguille vers les quatre sous-hubs), « Sécurité » et « LLM & IA générative ».

### 15. Une notion peut être évidente **et** intraitable dans son lot

Les 13 notions `concept/data` sont l'illustration nette de la consigne « une notion qui
appelle un sous-domaine hors du périmètre se remonte ». `v3-arborescence.md` le voyait venir
dès le lot 3 : « aucune des 13 n'est propre à ce domaine ».

Résultat : 8 rangées, **5 remontées** — `ORM` et `Migrations de schéma` vers `database/orm`
et `database/migration`, `Bases de données vectorielles` et `Index ANN — internes` vers
`database/vecteur`, `Notebooks-as-code` vers `devtools/notebook`. Effet de seuil mesuré pour
les cinq **avant** de décider (remontée 3) : il est **nul**, aucune ne forcerait de
restructuration. Ce n'est donc pas le seuil qui les retient, c'est la frontière de domaine.

Conséquence à assumer et à écrire : **`concept/data` reste dans le vocabulaire** alors que
sa famille a été traitée. C'est la première entorse au critère « aucune notion ne reste sur
une `categorie: concept/*` », elle est motivée — retirer la valeur rendrait ces 5 pages
invalides sans les avoir rangées — et elle est inscrite à côté de la valeur dans
`taxonomie.md`.

**Ce que ça dit du découpage en conversations** : découper le lot 4 par famille `concept/*`
ne coïncide pas avec le découpage par domaine d'accueil. Une conversation qui traiterait
« Bases de données » comme domaine d'accueil ramasserait ces 4 notions d'un coup. Pour les
lots restants, envisager un dernier passage **par domaine d'accueil** plutôt que par famille
d'origine, pour les résidus.

### 16. Deux fois la même règle sur les comparatifs, deux résultats opposés

Un comparatif vit dans le dossier de ses membres. Appliquée aux deux domaines qui ont promu
un sous-dossier, la règle a donné :

- « Mathématiques » — `Comparatif - Solveurs d'optimisation` filtre
  `categorie == "math/optimisation"` **exactement** : tous ses membres sont dans le dossier
  promu, il **descend** avec eux ;
- « Signal & audio » — `Comparatif - Traitement du signal` filtre `role == "brique"` plus le
  tag `signal-processing` : ses 3 membres enjambent `signal/traitement` et `signal/audio`,
  il **reste** au niveau du domaine. Idem pour celui du pilote, qui filtre le préfixe
  `stats/` entier.

**La règle porte sur les MEMBRES, pas sur le nom du fichier ni sur le sous-domaine qui a été
promu.** Le relever ici parce que les trois cas sont maintenant des précédents lisibles, et
que le lot 5 va devoir refaire exactement ce raisonnement pour 47 pages.

### 17. Le libellé d'un dossier se heurte à ses propres pages — `Traitement`

Prolongement de la remontée 8, avec un cas nouveau. `signal/traitement` aurait dû s'appeler
« Traitement du signal » : c'est le nom du sous-domaine, et il n'entre en collision avec
aucun autre hub. Sauf que c'est le `nom:` d'une **notion qui vit dans ce dossier** — deux
fichiers du même nom, et le vault tient les liens nus depuis le lot 3 précisément parce
qu'ils survivent aux déplacements. Le libellé retenu est « **Traitement** ».

La vérification d'unicité d'un libellé de hub porte donc sur **quatre** ensembles, et le
quatrième est le nouveau : les noms de fichiers du vault, les `alias:` des pages du même
rôle (remontée 8), le nom des autres hubs — et **les pages que le dossier va accueillir**,
qui n'existent pas encore à cet emplacement au moment où l'on choisit le libellé.

### 18. Les MOC meurent sur mesure, et une seule refuse de mourir

La question laissée ouverte par la remontée 7 est tranchée : une `MOC/Concepts/` se supprime
**dès que la mesure est remplie**, pas toutes ensemble à la fin. La condition est double, et
les deux moitiés comptent :

1. **mesuré** que zéro page ne dépend d'elle seule pour sa R7 — `mesure_r7.py` énumère les
   pages d'aiguillage du vault et croise ; la mesure va dans le message de commit ;
2. `build_mocs.py` ne la **régénère plus**, sans quoi la suppression est cosmétique.

Cinq sont mortes : `Statistiques` et `Gestion des connaissances` (commit dédié, avant les
domaines), puis `Maths du ML`, `Traitement du signal (notions)` et `IA & sécurité`.

`Données (notions)` **ne peut pas** mourir, et c'est la moitié nº 2 qui bloque : sa mesure
R7 est pourtant remplie — le corps du hub « Data & pipelines » nomme les 5 notions restées
sous `Wiki/` —, mais 5 pages portent encore `concept/data`, donc `build_mocs` la réécrit à
chaque passage. **Une MOC vivante ne se supprime pas, elle se vide.** À retenir pour les
quatre dernières : elles mourront avec leur famille, pas avant.

### 19. Ce qui reste ouvert

- ~~**`concept/devops` est dans le vocabulaire et n'a aucune page.**~~ — **tranché le
  2026-09-05 : retiré.** C'est un résidu, pas un emplacement réservé. Cf. la remontée 23.
- ~~**Les 5 notions `concept/data` remontées** attendent une décision.~~ — **tranché et
  fait le 2026-09-05 : elles descendent.** Cf. la remontée 20 ci-dessous.
- ~~**`MOC/Concepts/Données (notions)`** ne peut pas mourir tant que ces 5 vivent.~~ —
  **morte le 2026-09-05**, une fois les 5 descendues : `build_mocs.py` ne la régénère plus
  (elle a disparu de sa liste, ce n'est pas une réécriture à l'identique) et la mesure R7
  donne 0 page perdue. Les quatre autres (`Deep learning`, `LLM (notions)`,
  `Machine learning (notions)`, `NLP (notions)`) mourront avec leur famille.

---

## Remontées — les résidus `concept/data`, 2026-09-05

Les **5 notions remontées** par la conversation précédente sont descendues, `concept/data`
est sorti du vocabulaire et `MOC/Concepts/Données (notions)` est morte. Zéro valeur
ouverte, zéro sous-dossier promu ou défait, zéro brique déplacée par ricochet. Le compteur
d'avertissements n'a pas bougé — 149 avant, 149 après — et le **jeu** est identique ligne
à ligne.

### 20. Le passage par domaine d'accueil coûte presque rien, et c'est l'intérêt

La remontée 15 suggérait « un dernier passage **par domaine d'accueil** plutôt que par
famille d'origine, pour les résidus ». Le passage a coûté un script de 40 lignes utiles et
trois phrases de hub. La raison est mécanique : les cinq notions avaient déjà été lues,
leur cible déjà écrite, et leur effet de seuil déjà mesuré — il ne restait que l'exécution.

**Ce qui a quand même été refait, et devait l'être** : la mesure de seuil, sur la
population **réelle** des deux domaines d'accueil et non sur le chiffre noté la veille. La
remontée 3 dit de mesurer avant de décider ; elle ne dit pas de faire confiance à une
mesure d'hier, prise avant quatre commits qui ont déplacé des pages. Le script recalcule
`arbo.promotions()` avant et après pour chaque domaine, compare les deux ensembles et
**s'arrête** s'ils diffèrent — le seuil n'est pas négociable page par page, donc une
promotion inattendue rouvre l'arbitrage au lieu d'être encaissée.

### 21. Trois hubs ne disaient rien de pages que leur dossier allait accueillir

Application directe de la remontée 14, dans les deux sens.

- « Data & pipelines » portait une puce disant *« Cinq notions ne sont pas ici et portent
  encore `concept/data` […] leur déplacement est à arbitrer »*. Elle est devenue fausse en
  une commande. Réécrite : elles ne sont toujours pas ici, mais parce qu'elles sont
  **rangées** ailleurs, et la puce dit maintenant pourquoi leur sujet n'est pas le pipeline.
- « Vectoriel » et « Notebooks » posaient le problème **symétrique** : leur corps n'a jamais
  cité les notions, puisqu'elles n'étaient pas là. Après le `git mv`, deux hubs qui
  énuméraient soigneusement leurs briques restaient muets sur la notion chapeau de leur
  propre dossier — la zone `<!-- AUTO -->` l'aurait listée, le corps non. Le cas est plus
  discret que celui d'une phrase fausse, et rien ne le signale : `grep` ne trouve **rien**,
  et c'est justement le symptôme.

**Geste à ajouter à celui de la remontée 14** : après les `git mv`, `grep` le nom de chaque
page déplacée dans les corps de hub — et, quand le `grep` ne renvoie **pas** le hub du
dossier d'accueil, se demander si son corps devrait la nommer. Les deux moitiés du geste
sont nécessaires ; la seconde n'a pas de sortie à lire, seulement une absence à remarquer.

### 22. Un relevé des membres des `.base`, écrit une fois, réutilisable au lot 5

La remontée 11 demande de comparer le **jeu** et non le compte, et `mesure_bases_role.py`
ne signale qu'un intrus — il ne dit rien d'un membre **perdu**. `mesure_membres_bases.py`
comble le trou : il énumère, pour chacun des 47 comparatifs, ses membres un par ligne, dans
un format stable et diffable. Il ne juge rien ; il donne la matière du `diff`.

Sur ce lot le diff est vide, et c'est attendu — les 39 filtres portent `role == "brique"`
depuis le correctif du 2026-09-05, donc une notion ne peut plus être absorbée. Le script
n'a donc rien trouvé ici. Il est écrit pour **le lot 5**, où les 47 `.base` deviendront des
pages `role: comparatif` portant une `categorie:` : à ce moment-là, chaque page de
comparatif entrera dans le champ des filtres des autres, et le mécanisme de la remontée 11
se rejouera à l'identique.

### 23. Une valeur née vide se retire comme une valeur vidée

`concept/devops` n'a jamais porté une page. La règle écrite par floSa au pilote — « une
valeur est retirée du bloc dès que plus aucune page ne la porte » — a été lue jusqu'ici
comme une règle de **fin de lot** : on vide, puis on retire. Elle ne dit pas ça. Son motif
est qu'une valeur sans page autorise une rechute silencieuse, `check_brain` l'acceptant
encore — et ce motif vaut exactement pareil pour une valeur qui n'a jamais servi.

La retenue avait une raison honnête : « rien ne dit si c'est un résidu ou un emplacement
réservé ». Deux mesures la lèvent, et aucune ne demande d'intuition. L'audit du 2026-09-02
listait déjà `concept/devops` parmi **26 valeurs déclarées et jamais utilisées** — ce n'est
pas un cas particulier, c'est un membre d'une population connue. Et la seule trace d'une
réservation est une ligne de `Documentation/perso/reservoir-v1.md` qui hésite entre
`concept/ml` et `concept/devops` pour « MLOps & monitoring » : le réservoir v1 est hors du
vault, et une page qui en reviendrait se rangerait par son **domaine** (`ml/monitoring`,
`devops/*`), pas sur le vocabulaire d'une galaxie supprimée au lot 3.

**Ce qu'il reste à faire un jour, et qui n'est pas de ce lot** : les 25 autres valeurs de
cette liste ne sont pas des `concept/*` et vivent dans le bloc ```domaine. Elles relèvent du
même raisonnement, mais pas de la même mesure — une valeur de brique sans page peut être un
domaine légitimement vide en attente d'une capture, là où `concept/*` est un vocabulaire en
cours de suppression. À poser au lot 8, pas ici.

---

## Remontées — domaine « LLM & IA générative », 2026-09-05

56 notions rangées (55 ici, 1 en « Sécurité »), **7 sous-dossiers créés** — le plus gros
lot de la migration après le lot 3 —, 3 valeurs ouvertes, 1 valeur de brique retirée,
21 briques déplacées par ricochet, 2 comparatifs descendus, 1 MOC supprimée. Aucune
violation dure à aucun moment. Jeu d'avertissements **identique ligne à ligne**, 149 avant
et après, et les 47 comparatifs ont exactement les mêmes membres qu'avant.

### 24. Ce que l'étape 0 ne sait PAS faire, et ce qui prend le relais

L'étape 0 a tenu sa promesse : le corps du hub cite **35 des 56 notions** nommément, et ses
paragraphes ne sont pas des listes mais des **familles** — le RAG et ses cinq étages dans
l'ordre du pipeline, l'éval opposée à l'observabilité, les deux façons de sortir autre chose
que du texte. Ces 35 se rangent en lisant, comme sur « Mathématiques » (remontée 12).

Les 21 restantes montrent la limite, et elle est instructive : **un hub parle de ce qu'on
construit, pas de ce qu'on comprend.** `Tokenization`, `Perplexity`, `Scaling laws`,
`Reasoning models` sont citées par le hub, mais dans un paragraphe qui explique un
*symptôme* (« un LLM ne voit que des tokens ») — il ne dit nulle part qu'elles forment une
famille. `GRPO`, `Reward modeling`, `Multi-Token Prediction`, `a2a-protocol`,
`Agent skills` ne sont pas citées du tout.

Ce qui a pris le relais n'est ni le tag ni l'`## Aperçu`, c'est la section
**`## Approches voisines`**. Elle nomme les pages que la notion se reconnaît comme
parentes, et c'est un signal bien plus fort qu'un tag parce qu'il a été écrit **en pensant
à ces pages-là**. Quatre arbitrages en sont sortis, tous contre l'intuition de départ :

- `Routing and cascading` : le hub la range dans le paragraphe RAG. Ses voisines déclarées
  sont [[LiteLLM]], [[OmniRoute]] et [[OpenRouter]] — les **trois** briques de
  `llm/passerelle` — sous la mention « passerelles qui l'implémentent ». Elle va là.
- `Perplexity` : candidate évidente pour `llm/eval`. Ses voisines sont
  [[Tokenization]], [[Decoding strategies]], [[Cross-entropy]], [[Shannon entropy]], et la
  page écrit que l'éval applicative est « une **alternative** » à ce qu'elle décrit. C'est
  une propriété du modèle, pas une mesure de produit.
- `Server-Sent Events & streaming LLM` : le titre appelle `web/api`. Ses voisines sont
  [[Decoding strategies]], [[Tokenization]] et [[Inference optimization]] — « continuous
  batching et KV-cache alimentent plusieurs flux SSE en parallèle **côté serveur** ». Le
  transport HTTP est le sujet apparent, le débit du serveur est le vrai.
- `Sandboxing de code généré` : voir la remontée 25.

**Geste à ajouter à l'étape 0** : compter les notions que le corps du hub cite nommément,
puis, pour chaque notion restante, lire sa section `## Approches voisines` **avant** son
`## Aperçu`. Sur `ml` (67) et `dl` (52), c'est la seule des trois lectures qui passe à
l'échelle.

### 25. Le cas `security/ia` rejoué — et cette fois le seuil mordait

La remontée 13 demandait : « à rejouer sur les 56 notions `llm` : combien d'entre elles
sont la théorie d'une pratique plus large qui a son propre domaine ? » Réponse mesurée :
**une seule**, `Sandboxing de code généré`.

Elle est plus difficile que les quatre de septembre, parce que l'argument qui les avait
tranchées ne s'applique pas : elle porte `concept/llm` et non `concept/ai`, donc « la
famille large était déjà un choix » tombe. C'est le contenu qui a tranché — la page ouvre
sur « le code généré est **non fiable par construction**… parce que son entrée peut l'être
([[Prompt injection]]) », et quatre de ses cinq voisines déclarées sont les pages déjà
rangées en `security/ia`.

Deux options concurrentes existaient, chacune sourcée sur une page du vault, et c'est ce
qui rendait l'arbitrage réel : `llm/agents`, parce que [[Harnais d'agent]] énumère « la
boucle, les outils, le contexte, le parsing, la reprise, la persistance, **le bac à
sable** » ; `compute/a-la-demande`, parce que `taxonomie.md` décrit littéralement cette
valeur comme « bacs à sable d'exécution de code non fiable (typiquement généré par un
LLM) ». Aucune des deux ne déclenchait d'effet de seuil ; `security/ia` en déclenchait un.

**Arbitrage de floSa, et il vaut comme règle** : « le seuil ne se négocie jamais page par
page, ni pour l'atteindre ni pour l'éviter. La catégorie se décide sur le contenu, le
dossier suit tout seul. » C'est la remontée 4 lue dans l'autre sens — le pilote avait
établi qu'un seuil ne doit pas *motiver* une catégorie, ce lot établit qu'il ne doit pas
non plus la *retenir*.

Distinction explicitement posée avec le cas `Manifold learning` (remontée 3), où floSa
avait au contraire refusé le déplacement : là, la population du domaine cible n'était pas
arbitrée et le contenu de la page contredisait le rangement proposé. Ici les 4 pages
d'accueil sont tranchées depuis le matin et la 5e est sans ambiguïté. **Ce n'est donc pas
le franchissement de frontière qui bloque, c'est l'incertitude sur ce qu'on trouve de
l'autre côté.**

### 26. Nommer un dossier : les quatre ensembles ont mordu tous les quatre, d'un coup

Les remontées 8 et 17 avaient établi qu'un libellé de hub se vérifie contre quatre
ensembles. Sur ce lot, chacun a servi au moins une fois — c'est le premier lot où le
problème est systématique plutôt qu'anecdotique.

| Libellé naturel | Ce qui l'interdit | Retenu |
|---|---|---|
| « RAG » | **une page du dossier** : `RAG.md` (ensemble nº 4, remontée 17) | RAG & retrieval |
| « Observabilité » | **le hub d'un domaine** de l'arbre (ensemble nº 3) | Observabilité des LLM |
| « Observabilité LLM » | un `alias:` de `LLM observability`, **qui vit dans le dossier** | idem |
| « Sortie structurée » / « Sorties structurées » | `alias:` de `Structured outputs`, qui vit dedans | Sortie typée |
| « Génération contrainte » / « Décodage contraint » | `alias:` de `Constrained decoding`, qui vit dedans | idem |
| « Sécurité des systèmes IA » | **redouble le nom du domaine parent** (remontée 8) | Systèmes IA |

Deux enseignements qui n'étaient pas encore écrits. D'abord, **la collision d'alias avec
une page du dossier ne déclenche aucun avertissement** : R5 ne compare que des pages de
**même rôle**, et un hub contre une notion n'en est pas. La règle qui la rend indésirable
n'est donc pas dans le validateur, elle est dans Obsidian — un fichier nommé `X` capture
`[[X]]` et rend inatteignable l'alias `X` d'une autre page. À vérifier à la main, à chaque
libellé.

Ensuite, le libellé retenu **n'a pas à être le nom de la catégorie**, et c'est même
l'inverse qui devient la norme : quatre libellés sur six s'en écartent ici. Ce qu'on nomme
est la **population du dossier**, pas la valeur du champ.

### 27. Une valeur de brique retirée — le premier cas du lot 4

`llm/mcp` nommait **un protocole**. `a2a-protocol` est un second protocole, ouvert, du même
étage — et il n'existait aucun endroit honnête où le mettre : `llm/mcp` aurait menti,
`llm/agents` l'aurait rangé avec des bibliothèques d'orchestration alors que c'est une
spécification.

Arbitrage de floSa : ouvrir `llm/protocole` et **y verser MCP aussi**, ce qui recatégorise
deux briques ([[fastmcp]], [[mcpjam]]) et retire `llm/mcp` du bloc. C'est la première fois
du lot 4 qu'on touche à une valeur portée par des **briques** — jusqu'ici le lot n'ouvrait
que du vocabulaire neuf pour des notions sans domicile.

Ce que ça coûte, mesuré : deux lignes `categorie:` réécrites, aucun déplacement de fichier
(les deux valeurs restent sous le seuil), un commentaire à corriger dans
`Comparatif - Frameworks LLM.base`, qui citait `llm/mcp` dans sa liste des valeurs sorties
de l'ancien `llm/framework`. Rien d'autre — et le relevé des membres des 47 `.base` ne
bouge pas.

Ce que ça apprend : **une valeur de catégorie qui nomme un produit vieillit mal.** `mcp` a
tenu tant qu'il n'existait qu'un protocole ; il a cassé au second. À rejouer sur les
valeurs restantes du vocabulaire qui nomment une technologie plutôt qu'une fonction —
`data/tableau` et `ml/hub` sont les deux candidates visibles, à poser au lot 8.

### 28. Un domaine à douze sous-dossiers, et ce que ça dit du seuil

« LLM & IA générative » passe de 6 à **12 sous-dossiers** pour 129 pages, soit 17 pages au
niveau du domaine. Le seuil n'a été forcé nulle part : six sous-domaines l'ont franchi
parce qu'ils ont reçu leurs notions, dont trois qui l'ont franchi **de justesse** —
`observabilite` 4→5, `sortie-structuree` 3→5, `passerelle` 3→5.

C'est le premier domaine où la question « douze dossiers, est-ce encore de la navigation ? »
se pose honnêtement. Deux faits la referment, et il vaut mieux les avoir écrits avant
`ml` (67 notions, 9 sous-dossiers déjà) :

1. **Les douze se lisent en trois groupes**, et le corps du hub les présente ainsi
   désormais — le modèle (3 dossiers), ce qu'on construit avec (7), ce qui dit si ça
   marche (2). Un dossier de plus dans un groupe nommé ne coûte pas la même chose qu'un
   dossier de plus dans une liste de douze.
2. **Le plafond du seuil n'a jamais été proche** : le plus gros sous-dossier fait 18 pages
   sur 129, et 17 pages restent au niveau du domaine. Le cas que le plafond vise — un fils
   qui redouble son parent — ne s'est pas présenté.

Ce qui, en revanche, **mérite d'être surveillé au lot 6** : `Modèles de langage/` est le
seul sous-dossier du domaine sans aucune brique. Six notions, zéro chose à installer. Ce
n'est pas une anomalie — c'est ce qui arrive quand un domaine a de la théorie propre — mais
c'est un profil nouveau dans l'arbre, et le gabarit de hub §9 (« Choisir » entre des
briques) n'y répond qu'à moitié.
