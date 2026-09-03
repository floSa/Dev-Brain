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

> **État au 2026-09-05 — le domaine pilote est fait.** « Statistiques & inférence » a été
> traité en premier : **37 notions rangées**, 4 sous-dossiers créés, 2 valeurs de catégorie
> ouvertes (`stats/probabilite`, `stats/experimentation`), `concept/stats` retiré du
> vocabulaire. Il reste **260 notions** sous `Wiki/Concepts/` et 9 MOC vivantes. Les dix
> *Remontées* en fin de document sont la méthode telle que le terrain l'a corrigée — les lire
> avant d'attaquer un autre domaine, en particulier les nº 1, 3 et 5.

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
- [ ] `math` (26) — le suivant. La frontière `stats/probabilite` ↔ `math/*` est déjà écrite
      dans `taxonomie.md` : elle contraint ce lot, la relire avant de rouvrir la question.
- [ ] `llm` (57) · [ ] `ml` (67) · [ ] les 18 sans domaine

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

### Les 18 sans domaine

La plupart sont en fait évidentes une fois posée la question « de quoi ça parle » :
`ORM` → `database/orm`, `Migrations de schéma` → `database/migration`,
`Web scraping` → `data/scraping`, `Notebooks-as-code` → `devtools/notebook`,
`Index ANN — internes` → `database/vecteur`. Les proposer groupées, en une seule question.

Les notions de sécurité IA (`Prompt injection`, `Jailbreaking and defenses`, `Guardrails`)
n'ont pas de domaine dans le vocabulaire actuel : c'est une **vraie** décision, à remonter.

## Critères d'acceptation

Ils se vérifient **par domaine**, pas seulement à la fin — c'est ce qui permet de clore un
domaine à la fois. Entre parenthèses, l'état du pilote `stats`.

- [ ] Aucune notion ne reste sur une `categorie: concept/*`. *(stats : fait, et la valeur
      `concept/stats` est retirée du bloc de `taxonomie.md` — laisser une valeur sans page
      autorise une rechute silencieuse)*
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

Il est câblé dans `Home.md`, qui annonce désormais 6 axes, et `CLAUDE.md` suit. **À trancher :
garder 6 axes, ou retirer `infra-ops` de `themes.md`.** Revenir en arrière coûte une ligne dans
`build_mocs.py` et une suppression de page.

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

**À décider par floSa, et la réponse vaudra pour les 9 autres** : les supprimer au fil des lots
dès que la mesure est remplie, ou toutes ensemble à la fin du lot 4.

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
