---
role: meta
nom: remontees-lot-3-ml-vision-serving-non-supervise
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 / lot 3 — remontées

Périmètre : « Machine Learning/Vision/ » (9 briques), « Machine Learning/Serving/ » (9) et
« Machine Learning/Non supervisé/ » (4). **22 fiches**, exactement le compte annoncé par la
table du découpage. Branche `claude/lot-3-machine-learning-f44962`.

Règle 3 tenue : aucun document partagé touché — ni le brief, ni `CLAUDE*.md`, ni
`taxonomie.md`, ni `brain-v3.md`, ni un script. `build_bandeau.py` a été **lancé**, borné aux
trois dossiers, jamais édité. Règle 2 tenue : aucun index régénéré, `cloturer-brain` pas appelé.

## 1. Les neuf fiches de Serving ne pointaient vers aucune notion ni aucun hub

Mesure avant conversion : `check_brain.py` signalait **R15 sur les neuf** briques du dossier
Serving — « aucun lien vers une notion ou un hub ». Le dossier porte pourtant sa notion,
[[Déploiement de modèles]], depuis le lot 4 : elle n'était simplement citée par aucune fiche.
La ligne « la notion du dossier » de `## Voir aussi` referme les neuf.

Écart de la branche, mesuré des deux côtés du travail : **149 avertissements avant, 140
après**, zéro violation dure dans les deux cas. Les neuf de moins sont exactement ces R15.
Le compte ne vaut que pour cette branche : il lui manque le travail des seize autres.

> À vérifier ailleurs : si un dossier entier a pu rester non câblé à sa propre notion, le cas
> n'est probablement pas isolé. C'est bon marché à détecter — `check_brain.py` le dit déjà,
> dossier par dossier.

## 2. Quatre fiches n'entrent dans aucune vue de comparatif de leur dossier

C'est la remontée la plus utile du lot, et elle contredit une hypothèse implicite du brief :
« le comparatif du dossier porte déjà les puces besoin → concurrent ». Il ne les porte que
pour les **membres de sa vue**, et une vue `.base` filtre par **tag**, pas par dossier.

| Fiche | Dossier | Vue du dossier | Filtre | Membre ? |
|---|---|---|---|---|
| `Kornia` | Vision/ | Détection & segmentation | `object-detection` ou `segmentation` | non |
| `timm` | Vision/ | idem | idem | non |
| `torchvision` | Vision/ | idem | idem | non |
| `hdbscan` | Non supervisé/ | Détection d'anomalies **et** Réduction de dimension | `anomaly-detection` / `dimensionality-reduction` | non aux deux |

Conséquence de conversion : pour ces quatre-là, les puces « besoin → concurrent » **n'avaient
aucun autre endroit où vivre**. Elles sont donc restées en `Écarter si`, avec leur wikilink —
et c'est ce qui remplit la règle 5. Pour les dix-huit autres, la règle du pilote s'applique
telle quelle : la puce est déjà au comparatif, elle n'est pas recopiée.

Leur `## Voir aussi` pointe le **hub** du dossier plutôt que le comparatif, et dit pourquoi en
clair. Un lien vers une vue qui ne les contient pas aurait été un lien menteur.

> À arbitrer par l'intégration : c'est un trou du **lot 5**, pas du lot 6. Soit les vues
> s'élargissent (un filtre par `categorie:` plutôt que par tag), soit ces dossiers gagnent une
> seconde vue, soit on acte qu'un dossier n'est pas tenu de comparer toutes ses briques.

## 3. Les puces « besoin → concurrent » : 77 %, contre 89 % au pilote

Mesure du 2026-09-06 sur les 22 fiches d'origine : **70 puces** en `## Quand NE PAS
l'utiliser`, dont **54 de la forme « besoin → [[concurrent]] »**, soit 77 %. En face,
`## Pièges` en portait **73**.

L'écart avec les 89 % du pilote s'explique par le point 2 : les fiches hors comparatif ont des
exclusions qui pointent vers des voisins que rien d'autre ne départage.

Décompte final des cellules `Écarter si`, sur les 22 fiches : **87 cellules**, dont **14
vides** faute de source, **18 portant un wikilink** et **55 sans**. Aucune cellule n'a été
comblée au jugé.

## 4. La règle 5 reste tenue en échec — dans les mêmes termes qu'au pilote

55 cellules sur 87 ne portent pas de wikilink. La cause est la même qu'au pilote : ce qui reste
en `Écarter si` après retrait des puces comparatives est une **borne dure de la brique seule**,
qui ne pointe nulle part — `min_samples` décalé de 1 entre `hdbscan` et `sklearn`, le
`model_repository` de Triton qui échoue en silence, le mauvais paquet `onnxruntime` qui tombe
sur CPU sans le dire, les quatre paquets pip mutuellement exclusifs d'OpenCV.

Le pilote a laissé la question ouverte. Ce lot a fait le **même** choix que lui, par cohérence
de vault et non par conviction : mieux vaut deux cents fiches homogènes qu'un lot qui invente
sa propre règle. La décision reste à prendre à l'échelle du vault, et elle est de la nature du
lot 8.

## 5. Recouvrement assumé avec le comparatif — deux cas, nommés

Le pilote en avait trois sur 18 fiches et demandait un arbitrage. Ce lot en a **deux sur 22**,
gardés délibérément parce que ce sont des bornes qui mordent avant même le choix :

| Fait | Fiche | Comparatif |
|---|---|---|
| installation fragile, torch/CUDA stricts, Windows limité | `Detectron2`, `Écarter si` | « installation fragile, versions torch/CUDA strictes, Windows natif limité » |
| AGPL-3.0 et l'obligation d'ouvrir le code appelant | `Ultralytics YOLO`, `Écarter si` | « le critère qui tranche n'est pas technique mais juridique — AGPL-3.0 » |

Le troisième candidat, le **BGR** d'OpenCV, a été traité autrement : le comparatif le porte
déjà comme discriminant, et la fiche le pose en `## Définition` — « une limite qui n'oriente
rien mais qu'il faut savoir », troisième destination du brief. C'est peut-être la sortie
générale du débat du point 5 du pilote.

## 6. `complements:` — huit couples posés, tous internes au périmètre

Contrairement au pilote, dont les cinq paires sourcées pointaient toutes dehors, ce lot a pu
refermer huit couples des deux côtés :

| Couple | Sourcé dans | Nature du lien |
|---|---|---|
| `NVIDIA Triton` ↔ `TensorRT` | les deux fiches | le serveur exécute les moteurs compilés |
| `NVIDIA Triton` ↔ `ONNX Runtime` | les deux fiches | le serveur embarque le moteur comme backend |
| `albumentations` ↔ `OpenCV` | les deux fiches | l'augmentation est bâtie sur le moteur d'image |
| `supervision` ↔ `Ultralytics YOLO` | les deux fiches | l'outillage exploite les sorties du modèle |
| `supervision` ↔ `Detectron2` | les deux fiches | idem |
| `supervision` ↔ `segment-anything` | les deux fiches | idem, sur les masques |
| `supervision` ↔ `OpenCV` | `supervision` seule | la couche bas niveau du rendu |
| `umap-learn` ↔ `hdbscan` | les deux fiches | le pipeline UMAP → HDBSCAN |

Un filtre a beaucoup coupé : **un couple déjà déclaré en `alternatives:` ne peut pas devenir
un couple `complements:`** sans violer la règle 8 (pas de double citation). Cinq relations de
composition pourtant écrites en toutes lettres dans les fiches tombent sous ce filtre —
`BentoML` devant `NVIDIA Triton`, `Ray Serve` devant `Triton`, `KServe` avec `Triton` comme
runtime, `Seldon Core` et `KServe` sur le protocole V2, `ONNX Runtime` qui délègue à
`TensorRT`. Ces briques sont **à la fois** concurrentes et composables, et le modèle de données
ne sait pas le dire.

> À trancher, et ce n'est pas propre à ce lot : `alternatives:` et `complements:` sont posés
> comme exclusifs, alors que dans le serving ils se recouvrent. Le fait est écrit dans les
> `## Définition` faute de champ pour le porter.

Complements **hors périmètre**, posés ici et non écrits — la moitié du couple appartient à un
autre lot :

| Fiche | Complément sourcé | Dossier de la cible | Lot |
|---|---|---|---|
| `Ray Serve` | [[Ray]] | Calcul distribué/ | 15 |
| `TensorFlow Serving` | [[TensorFlow]] | Machine Learning/Apprentissage profond/ | 4 |
| `TorchServe`, `Detectron2`, `Kornia`, `timm`, `torchvision`, `Ultralytics YOLO`, `segment-anything`, `albumentations` | [[PyTorch]] | Machine Learning/Apprentissage profond/ | 4 |
| `timm` | [[HuggingFace]] | Machine Learning/ (niveau domaine) | 6 |
| `PyOD`, `hdbscan`, `umap-learn` | [[Scikit-Learn]] | Machine Learning/Socle/ | 4 |
| `KServe`, `Seldon Core` | [[Docker]] | DevOps/ | 17 |

Le cas `PyTorch` mérite d'être vu pour ce qu'il est : **huit** des 22 fiches de ce lot en
dépendent. Si le lot 4 pose la réciprocité côté PyTorch, la fiche portera huit compléments d'un
coup, rien que depuis ce lot. La question n'est pas la réciprocité, elle est de savoir si « la
brique sur laquelle je suis bâtie » mérite le même champ que « ce qui s'utilise avec moi ».

## 7. Le vocabulaire fermé de `Ressources` n'a pas d'étiquette pour une licence

`Ultralytics YOLO` porte une troisième URL, `https://www.ultralytics.com/license`, et l'AGPL
est **le** critère de choix de cette brique. Les sept étiquettes autorisées
(`Documentation, Dépôt, Tutoriel, Article, Papier, Cours, Vidéo`) n'en ont aucune pour ça. La
puce est étiquetée `Documentation`, avec une glose derrière l'URL.

C'est le seul cas du lot. Une huitième étiquette `Licence` serait sans doute utile ailleurs
(les briques `open-core`, `source-available` et `proprietary` ont toutes une page de termes) —
mais le vocabulaire est un document partagé, la règle 3 interdit d'y toucher, et c'est noté ici.

## 8. Trois fiches portaient de la prose **dans** `## Alternatives`

`ONNX Runtime` et `TensorRT` portaient chacune un paragraphe « Nuance : … » après leurs puces,
et `PyOD` une phrase d'introduction (« Pas de substitut unifié équivalent dans le brain »). Le
gabarit v3 ne tolère aucune prose hors de `## Définition`.

Les trois ont été **dissoutes, pas supprimées** : le portable-contre-mono-vendeur d'ONNX
Runtime et de TensorRT est passé en `Prendre si` et en `## Définition`, la composition des deux
en `### Compléments` pour Triton et en clair dans les définitions, et le « pas de substitut
unifié » de PyOD dans les deux cellules `Écarter si` qui nomment scikit-learn et la détection
univariée.

## 9. Aucune `## Retours` créée

Conforme au brief. Les dates présentes dans ces 22 fiches — archivage de TorchServe le 7 août
2025, bascule BSL de Seldon le 22 janvier 2024, intégration Dynamo en mars 2025 — sont des
**faits sur le projet**, pas des retours d'expérience datés au format
`- YYYY-MM-DD — symptôme : correctif.` Aucune entrée du vécu de floSa dans le périmètre.

## 10. Un avertissement R5 préexistant, hors périmètre de correction

`Machine Learning/Serving/TensorRT.md` porte l'alias `tensorrt-llm`, qui est le `nom:` de
`LLM & IA générative/Runtimes/TensorRT-LLM.md` — même rôle, donc collision. Présent avant ce
lot, toujours présent après : corriger un alias est une décision de frontmatter qui engage les
deux fiches, dont l'une appartient au **lot 8**. Signalé, pas touché.
