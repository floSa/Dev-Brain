---
role: meta
nom: remontees-lot-11-data-pipelines
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 11 : Data & pipelines, Scraping et Parsing

Périmètre : « Data & pipelines/Scraping/ » (10 briques) et « Data & pipelines/Parsing/ »
(9). **19 fiches, le compte annoncé par la table du découpage.** Branche
`claude/lot-11-data-pipelines-cb7f8e`, partie de `d8f81d6`.

Aucun fichier partagé touché : ni le brief, ni `CLAUDE*.md`, ni la taxonomie, ni
`brain-v3.md`, ni `v3-arborescence.md`, ni aucun script. `build_bandeau.py` a été **lancé**
deux fois, borné à chacun des deux dossiers, jamais édité. Aucune régénération, aucun appel à
`cloturer-brain`.

## 1. Les deux comparatifs du périmètre couvrent 100 % de leurs briques — la règle 2 mord partout

`mesure_membres_bases.py` (recoupé à la main sur les deux `.base`, dont les filtres sont
`role == "brique"` + `categorie == "data/scraping"` / `"data/parsing"`, donc sans exclusion
par tag) :

| Vue | Membres | Briques du dossier |
|---|---|---|
| `Comparatif - Scraping.base` | 10 | 10 |
| `Comparatif - Parsing de documents.base` | 9 | 9 |

Conséquence directe sur la règle 2 — mesurée, pas supposée. Les sections
`## Quand NE PAS l'utiliser` d'origine portaient **59 puces, dont 48 avec wikilink**, soit
**70 renvois** une fois les puces à cibles multiples éclatées :

- **67 renvois sur 70 (96 %) visent une cible membre de la MÊME vue** → partis au comparatif,
  qui les portait déjà ;
- **3 renvois sur 70 seulement tombent dans le « sinon »**, et les trois sont sur `docTR` :
  deux vers [[OCR]], un vers [[Vision Language Models]]. Ce sont des **notions**, jamais
  membres d'une `.base`. Ils **restent** en `Écarter si` avec leur wikilink.

> **Ce lot est l'inverse du cas majoritaire annoncé.** La règle 2 prévient que « la brique est
> membre, la cible ne l'est pas » domine ailleurs (`datasets -> Polars`, `Flyte -> Dagster`…).
> Ici il ne se produit **jamais** : les deux dossiers sont fermés sur eux-mêmes — chaque
> concurrent cité vit dans le même dossier et tombe dans la même vue. Les seuls renvois
> survivants pointent vers des notions. La règle tient, mais son cas fréquent dépend de la
> **fermeture du dossier**, pas d'une propriété générale : un dossier dont le comparatif est
> complet et dont les renvois ne sortent pas produit presque zéro wikilink en `Écarter si`.

Résultat mesuré : **77 cellules `Écarter si` remplies, dont 2 portent un wikilink** (les deux
de `docTR`). Le critère d'acceptation « un wikilink dans chaque cellule `Écarter si` » n'est
donc satisfait qu'à 3 % — conformément à la cession de critère actée le 2026-09-06, et pour la
raison qu'elle donne : recopier les 67 autres aurait dupliqué le comparatif.

## 2. Ce qui reste en `Écarter si` : les bornes dures, et elles suffisent à remplir le tableau

Les 62 puces de `## Pièges` (dont 4 seulement portaient un wikilink) et les 11 puces de
`## Quand NE PAS l'utiliser` **sans** renvoi ont fourni la matière. Aucune n'a été supprimée
sans destination. Les bornes les plus nettes du périmètre :

- juridiques — AGPL-3.0 de `PyMuPDF` (piège du SaaS) et de `Firecrawl` / `Maxun` (self-host
  exposé), double licence code GPL + poids OpenRAIL-M de `Marker` sous 2 M$, module payant
  PDF/UA d'`OpenDataLoader PDF`, zone grise CGU de `minim` et de `cloudscraper` ;
- opérationnelles — `playwright install` obligatoire, JVM relancée à chaque `convert()`,
  binaires Tesseract/Poppler qui gonflent l'image d'`Unstructured`, `AutoThrottle` non réglé
  qui fait bannir l'IP ;
- de conception — absence d'OCR (`pdfplumber`), absence de rendu JS (`Scrapy`, `curl_cffi`),
  absence de client HTTP (`selectolax`), ordre de lecture non garanti (`docTR`).

**Le tableau ne s'équilibre pas, et c'est normal.** 17 cellules `Prendre si` vides et
6 cellules `Écarter si` vides sur les 19 fiches — jamais comblées. Les 6 vides d'`Écarter si`
sont réparties une par une sur `Crawlee`, `Playwright`, `Docling`, `LlamaParse`, `Marker` et
`pdfplumber` : ces fiches avaient plus de raisons de les prendre que de bornes propres, une
fois les renvois partis au comparatif.

## 3. Trois faits sont à la fois discriminant du comparatif et borne dure — laissés sur la fiche

Recouvrement assumé, conformément à la règle arrêtée. Mesure du périmètre :

| Fait | Fiche, `Écarter si` | Comparatif |
|---|---|---|
| AGPL-3.0 du cœur, contrainte du self-host exposé | `Firecrawl` | « Cœur en **AGPL-3.0**, ce qui contraint un self-host exposé » |
| double licence, poids OpenRAIL-M sous 2 M$ | `Marker` | « Sa vraie frontière est la **double licence** » |
| mode local à 0,489 contre 0,928 en hybride sur les tableaux | `OpenDataLoader PDF` | « Le mode local est bien plus faible sur les tableaux » |

Trois sur 19, comme le pilote en trouvait trois sur 18. Les formulations diffèrent — la fiche
dit ce qui va mordre, le comparatif ce qui fait choisir — mais ce sont deux endroits à tenir
d'accord, et le compte semble stable d'un lot à l'autre.

## 4. `complements:` — 11 couples posés, tous internes au périmètre, zéro moitié orpheline

Contrairement au pilote, dont les cinq compléments sourcés pointaient tous hors périmètre,
**les 11 couples de ce lot (22 demi-arêtes, comptées par script) ont leurs deux extrémités
dans mes dossiers**. Ils sont donc posés **dans les deux sens**, et l'intégration n'a rien à
refermer.

| Fiche | `complements:` | Source de l'appariement |
|---|---|---|
| `selectolax` | [[curl_cffi]], [[Playwright]], [[Scrapy]] | les deux sens pour les fetchers ; `Scrapy` seul pour le troisième |
| `curl_cffi` | [[selectolax]] | les deux sens |
| `Playwright` | [[selectolax]], [[Scrapy]] | les deux sens ; `Scrapy` énonce `scrapy-playwright` |
| `Scrapy` | [[Playwright]], [[selectolax]] | « coupler à [[Playwright]] (scrapy-playwright) », « utilisable dans les callbacks » |
| `PyMuPDF` | [[Docling]], [[Marker]], [[Unstructured]], [[OpenDataLoader PDF]] | « étage RAG complémentaire » (PyMuPDF) ; « étage bas niveau complémentaire » (les trois autres) |
| `pdfplumber` | [[Docling]], [[Unstructured]], [[OpenDataLoader PDF]] | idem, dans les deux sens pour les deux premiers |
| `Docling` | [[PyMuPDF]], [[pdfplumber]] | les deux sens |
| `Unstructured` | [[PyMuPDF]], [[pdfplumber]] | les deux sens pour `pdfplumber` |
| `Marker` | [[PyMuPDF]] | énoncé par `PyMuPDF` |
| `OpenDataLoader PDF` | [[PyMuPDF]], [[pdfplumber]] | énoncé par `OpenDataLoader PDF` |

**La lecture de la règle 3 appliquée ici**, à confirmer par l'intégration : un appariement
sourcé **d'un seul côté** ouvre le couple, et le couple s'**écrit** des deux côtés. C'est la
lecture du pilote (remontée 5 : « la réciprocité étant obligatoire, poser la moitié du couple
aurait laissé les cinq fiches cibles en faute » — le sourcing y venait d'une seule fiche). La
lecture stricte inverse — sourcing exigé des deux côtés — n'aurait laissé que **5 couples sur
les 11** : `selectolax`↔`curl_cffi`, `selectolax`↔`Playwright`, `PyMuPDF`↔`Docling`,
`pdfplumber`↔`Docling` et `pdfplumber`↔`Unstructured`. **Si l'intégration tranche pour la
lecture stricte, ce sont les six autres qui sautent** : `selectolax`↔`Scrapy`,
`Playwright`↔`Scrapy`, `PyMuPDF`↔`Marker`, `PyMuPDF`↔`Unstructured`, `PyMuPDF`↔`OpenDataLoader PDF`
et `pdfplumber`↔`OpenDataLoader PDF`.

Ce que le champ n'a **pas** absorbé, et qui est du positionnement, pas un appariement :
- `Crawlee` « API unifiée entre crawler HTTP et crawler navigateur ([[Playwright]]) » —
  `Playwright` est déjà dans ses `alternatives:`, on ne peut pas être les deux ;
- `docTR` « intégrée à l'écosystème [[PyTorch]] », « backend au choix PyTorch ou TensorFlow » —
  c'est un prérequis à trancher, pas une recommandation d'appariement. `PyTorch` est hors
  périmètre (Machine Learning/) : **rien posé, rien à refermer**, mais le cas est signalé au
  cas où le lot qui portera `PyTorch` en juge autrement ;
- `OpenDataLoader PDF` « mode hybride routé vers un backend IA — Docling en pratique » :
  `Docling` est dans ses `alternatives:`. Le fait reste en `## Définition`, **sans wikilink**,
  pour ne pas mettre la même cible dans deux sections. Le lien de navigation existe déjà par
  `### Alternatives`.

## 5. Aucune cellule inventée — trois trous nommés

Rien n'a été comblé au jugé. Les trois endroits où la fiche d'origine ne disait rien et où
j'ai laissé le vide plutôt que du plausible :

- **`selectolax` et `minim` n'ont aucune alternative dans le brain** (`alternatives: []`).
  Leur `### Alternatives` porte une ligne en clair qui nomme le hors-périmètre — BeautifulSoup
  et lxml pour l'un, Mutagen pour l'autre — sans wikilink, puisque ces pages n'existent pas.
  `docTR` est dans le même cas (PaddleOCR, EasyOCR, TrOCR, Tesseract). **Ce sont les 3 fiches
  sans `## Alternatives` que la remontée 11 du pilote annonçait ; elles sont toutes les trois
  dans ce lot.**
- **`minim` n'a pas d'`url_docs:`** (champ vide au frontmatter) : sa section `## Ressources`
  ne porte qu'une ligne, `Dépôt`. Rien d'inventé pour compléter.
- **`LlamaParse` n'a pas d'`url_repo:`** — normal, c'est le seul `famille: saas` du périmètre
  et il n'est pas open-source. Même traitement : `Ressources` ne porte que `Documentation`.

Cas dégénéré à noter : `cloudscraper`, `pdfplumber` et `Marker` ont `url_docs == url_repo`.
Les deux étiquettes pointent donc la même URL. C'est fidèle au frontmatter ; il n'y a pas de
règle qui l'interdise, mais l'intégration voudra peut-être trancher.

## 6. Les 19 fiches ont un frontmatter complet — aucun trou de bandeau

`build_bandeau.py --check` sur les deux dossiers ne signale **aucune** cellule vide : les
19 fiches portent `famille`, `licence_type`, `maturite`, et l'`Exécution` se dérive partout.
C'est l'inverse du pilote, dont les 7 `famille: application` d'Administration affichaient un
tiret cadratin en Maturité. **L'hypothèse du pilote — « le champ n'a peut-être jamais été
rempli pour la famille `application` » — ne se vérifie pas ici** : `Maxun` est
`famille: application` et porte `maturite: beta`. Le trou d'Administration est donc local à ce
dossier, pas propre à la famille.

## 7. Section « déploiement » : les 19 portaient le premier nom

Les trois noms ont été cherchés. Les 19 fiches du périmètre portaient toutes
`## Déploiement & coût` ; ni `## Bases & plateformes` ni `## Installation & plateformes` n'est
apparu. Vérifié après coup par script : aucune des 19 ne porte plus de section ancienne.

## 8. Aucune section `## Retours` créée

Conforme : aucune entrée datée dans le périmètre. La seule du vault est sur `t3code`, du
ressort du lot 7.

## 9. Un doublon de cible qui n'est pas couvert par la cession de critère

`docTR` porte [[OCR]] à la fois en `Écarter si` (règle 2 : la cible est une notion, jamais
membre d'une `.base`, le renvoi reste) et en `## Voir aussi` (c'est la notion parente de la
fiche, sa place naturelle). Les deux sont justifiés séparément, et ils se contredisent au
regard du critère « aucune cible dans deux sections ».

**Ce cas n'est pas celui que la cession du 2026-09-06 décrit** : la cession porte sur
`Écarter si` contre `Alternatives`, pas sur `Écarter si` contre `Voir aussi`. Il est laissé en
l'état — supprimer le renvoi perdrait l'orientation, supprimer le lien parent casserait R15 —
et signalé pour la réécriture des critères au lot 8. C'est le **seul** de mes 19 fiches ; les
trois autres doublons trouvés par mon script de vérification ont été levés par reformulation
(`Crawlee`, `Playwright`, `Unstructured` redisaient un mot du bandeau ;
`OpenDataLoader PDF` citait [[Stirling PDF]] en `Définition` **et** en `Voir aussi`, le lien
ne reste qu'en `Voir aussi`).

## 10. Écart de validateurs — il baisse, comme prévu

Sur ma branche uniquement, périmètre entier du vault :

| | Avant | Après |
|---|---|---|
| `check_brain.py` — violations dures | 0 | 0 |
| `check_brain.py` — avertissements | 149 | **142** |
| `check_arbo.py` | vert | vert |

Les 7 avertissements fermés sont **exactement** les 7 R15 de mon périmètre (« aucun lien vers
une notion ou un hub ») : `Docling`, `LlamaParse`, `Marker`, `pdfplumber`, `PyMuPDF`,
`Unstructured` et `minim`. Le nouveau `## Voir aussi` les câble — les six de Parsing au hub
[[Parsing]], `minim` à la notion [[Web scraping]]. Aucun avertissement nouveau, aucun
avertissement hors périmètre touché.

> Le dossier Parsing n'a **pas** de notion : c'est le hub qui joue ce rôle dans `## Voir
> aussi`, comme le pilote l'a fait pour Administration avec [[Bases de données]]. Scraping a
> la sienne, [[Web scraping]], et les 10 fiches y pointent. Aucune notion, aucun hub, aucun
> comparatif n'a été modifié.
