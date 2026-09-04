---
role: meta
nom: remontees-lot-5-ml
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 / lot 5 — remontées de la conversion « Machine Learning »

Périmètre : « Machine Learning/Séries temporelles/ » (7), « Machine Learning/Suivi
d'expériences/ » (7) et « Machine Learning/Tabulaire/ » (6) — **20 fiches `role: brique`**,
exactement le compte annoncé par la table du découpage. Branche `claude/lot-5-ml-fiches-c0933f`.

Conversation parallèle : elle n'a touché que ces 20 fichiers, n'a régénéré aucun index, n'a
appelé `cloturer-brain` à aucun moment, et n'a modifié aucun document partagé.
`build_bandeau.py` a été **lancé** borné aux trois dossiers, jamais édité.

## 1. Écart mesuré sur cette branche

| Mesure | Avant | Après |
|---|---|---|
| `check_brain.py` — violations dures | 0 | 0 |
| `check_brain.py` — avertissements (vault entier) | 149 | **142** |
| dont avertissements dans le périmètre | 7 | **0** |
| `check_arbo.py` | vert | vert |
| `build_bandeau.py --check` sur le périmètre | 20 à poser | vert |

Les 7 avertissements fermés sont tous des **R15** — « aucun lien vers une notion ou un hub » :
`neuralforecast`, et les six trackers autres que MLflow. La section `## Voir aussi` du nouveau
gabarit les câble par construction, puisqu'elle porte la notion ou le hub du dossier. Le gain
n'est donc pas un effet de bord : **R15 est structurellement satisfaite par le gabarit v3**, ce
qui vaut d'être noté pour les seize autres lots — le passif R15 du vault (102 fiches au constat
C2) devrait se résorber tout seul au fil du lot 6.

## 2. Deux écarts du pilote ne se reproduisent pas ici

- **Nom de la section « déploiement »** (remontée 3 du pilote) : les 20 fiches portaient
  `## Déploiement & coût`, aucune ne portait l'une des deux autres formes.
- **`## Alternatives` manquante** (remontée 11) : les 20 la portaient.

## 3. Le bandeau n'a aucune cellule vide — la piste « famille `application` » est fausse

Le pilote laissait 7 tirets cadratins en colonne **Maturité**, tous sur ses 7
`famille: application`, et suggérait que le champ n'avait peut-être jamais été rempli pour
cette famille. Ce n'est pas le cas : le périmètre contient une `famille: application`,
`TensorBoard`, et elle porte `maturite: production`. Les 20 bandeaux sont complets sur les
quatre colonnes. Le trou du pilote est propre au dossier Administration, pas à la famille.

## 4. Les règles 5 et 8 se contredisent — mesuré, et c'est structurel

C'est la remontée principale de ce lot. La règle 5 (dure) veut un wikilink dans **chaque**
cellule `Écarter si` ; la règle 8 (dure) interdit qu'une même cible apparaisse dans deux
sections de la page.

Mesure sur les 20 fiches d'origine : **60 puces** `## Quand NE PAS l'utiliser`, citant
**65 cibles**, dont **50 — 77 % — sont déjà déclarées dans `alternatives:`**. Les recopier en
`Écarter si` les placerait à la fois dans le tableau et dans `### Alternatives`, ce que la
règle 8 interdit. Elles ne sont donc pas recopiées : leur destination est `### Alternatives`,
et le comparatif du dossier pour l'arbitrage — ce qui reconduit la remontée 7 du pilote.

Résultat après conversion : **19 cellules `Écarter si` sur 88 remplies portent un wikilink**
(2 cellules laissées vides, tableau non équilibré). Le pilote en avait zéro ; le progrès vient
des 15 cibles citées **hors** `alternatives:`, qui, elles, ont pu être reportées, et de sept
liens venus de `## Pièges` ou de `## Liens` vers des notions ([[Data leakage]],
[[Calibration]], [[Stationarity]], [[Walk-forward CV]], [[Apprentissage profond]],
[[Régression logistique]], [[Sélection de variables]]).

> **Arbitrage proposé.** La règle 5 est inatteignable telle qu'écrite tant que la redirection
> vers une alternative déclarée est le motif dominant des exclusions — et elle l'est à 77 %.
> Reformulation qui tient : « toute cellule `Écarter si` **dont le motif est une redirection**
> porte un wikilink ; une redirection vers une cible déjà déclarée en `alternatives:` n'en est
> pas une, elle est portée par `### Alternatives` et par le comparatif du dossier. » Sans cette
> reformulation, durcir la règle 5 au lot 8 obligera soit à violer la 8, soit à réécrire les
> bornes sous la forme comparative que la remontée 20 du lot 5 condamne.

## 5. La règle 8 coûte aussi des liens fonctionnels

Cas rencontrés deux fois : `Chronos` est « intégrable comme modèle dans darts », et
`TensorBoard` s'écrit depuis `torch.utils.tensorboard`. Ces mentions vivent en
`## Mise en œuvre`, mais `[[darts]]` et `[[PyTorch]]` sont respectivement en
`### Alternatives` et en `## Voir aussi` — la règle 8 les y interdit. Les deux mentions sont
donc écrites **en clair**, sans lien.

L'intention de la règle, dans `brain-v3.md` §6, vise le doublon d'alternatives — Mimesis deux
fois sur la page Faker. Appliquée à la lettre à toutes les sections, elle supprime des liens
qui ne sont pas des doublons de navigation mais des faits d'intégration. **À trancher : la
règle 8 porte-t-elle sur toute la page, ou sur les seules sections de navigation
(`### Alternatives`, `### Compléments`, `## Voir aussi`) ?**

## 6. Les 62 puces `Pièges` — où elles sont parties

Aucune supprimée. Répartition : la grande majorité en colonne `Écarter si` comme **borne dure
de la brique seule** (`num_leaves` non borné, `cat_features` non déclarées, `m` à fournir,
format long strict, event files qui grossissent, autocapture bavarde, absence
d'authentification…) ; quelques-unes en `## Définition` quand elles décrivent le
fonctionnement plutôt qu'un choix (la z-normalisation de STUMPY, la croissance leaf-wise de
LightGBM, le modèle global de neuralforecast).

**Aucune `## Retours` créée** : aucune entrée datée dans le périmètre, conforme au brief.

Une seule prose n'avait pas de destination évidente — « `matrixprofile` est l'autre
implémentation Python, moins active », sur STUMPY. Elle est passée en `## Définition` : ce
n'est ni une borne ni un vécu, c'est un fait de contexte.

## 7. `complements:` — un couple posé, le reste remonté

Un seul couple a ses **deux extrémités dans le périmètre** :

| Fiche | Complément | Source |
|---|---|---|
| `Featuretools` | [[category_encoders]] | « encodage catégoriel fin (Target, WoE) » et « encodage fin : [[category_encoders]] », dans ses sections `Quand NE PAS l'utiliser` et `Liens` d'origine |
| `category_encoders` | [[Featuretools]] | réciproque, posée du même geste |

DFS produit les colonnes, les encodeurs les préparent : c'est un enchaînement, pas une
substitution. La réciprocité est donc complète, et aucune fiche hors périmètre n'est mise en
faute.

Tous les autres compléments sourcés pointent **hors périmètre** et sont laissés vides :

| Fiche | Complément sourcé | Dossier de la cible | Lot |
|---|---|---|---|
| `imbalanced-learn` | [[Scikit-Learn]] — « complète scikit-learn plutôt qu'il ne le remplace », verbatim | Machine Learning/Socle/ | lot 4 |
| `darts`, `neuralforecast` | [[PyTorch]] — le backend Lightning | Machine Learning/Apprentissage profond/ | lot 4 |
| `TensorBoard` | [[PyTorch]], [[TensorFlow]] | Machine Learning/Apprentissage profond/ | lot 4 |
| `Chronos` | [[HuggingFace]] — distribution des poids | LLM & IA générative/ | lots 7 à 10 |

### La question de fond : jusqu'où va `complements:` ?

Les sept fiches de « Suivi d'expériences/ » déclarent toutes s'intégrer à des frameworks —
[[PyTorch]], [[Scikit-Learn]], [[XGBoost]], [[Optuna]], [[HuggingFace]], [[TensorFlow]]. Si
« framework qu'un tracker instrumente » compte comme complément, ce seul dossier ouvre une
quinzaine de couples, dont un au moins est **entièrement dans ce périmètre** (`MLflow` et
`XGBoost`, via l'autologging). Il n'a pas été posé : la fiche `XGBoost` ne dit rien de MLflow,
la source est unilatérale, et poser le couple aurait été une décision de portée bien plus large
qu'une conversion de format.

**À trancher avant que les seize autres lots ne remplissent le champ**, sinon chacun le
remplira selon sa propre lecture : `complements:` couvre-t-il l'enchaînement dans un pipeline
(Featuretools → category_encoders, pgvector avec Postgres), ou aussi l'intégration outil ↔
framework (MLflow avec XGBoost) ? La réciprocité étant dure, une divergence de lecture entre
deux lots produit des couples à moitié posés.

## 8. Trois fiches sur 20 n'entrent dans aucun comparatif — un angle mort de R8a

`Featuretools`, `category_encoders` et `imbalanced-learn` sont dans « Tabulaire/ », dont le
comparatif existe — `Comparatif - Boosting` — mais dont le filtre `.base` est
`file.hasTag("boosting")`. Les trois ne portent pas ce tag : elles ne sont dans aucune vue de
comparaison du vault. Leur `## Voir aussi` n'a donc pas de ligne `Comparatif - …`, et leurs
redirections ne peuvent pas « aller au comparatif » comme le veut la remontée 7 du pilote.

R8a ne les signale pas : elle raisonne par `categorie:`, et `ml/tabulaire` **a** un `.base`.
La règle vérifie qu'une catégorie est couverte, pas que ses briques le sont. Sur les 20 fiches
du lot, 17 sont membres d'un comparatif (6 dans Forecasting, 7 dans Suivi d'expériences ML,
3 dans Boosting, STUMPY dans Détection d'anomalies) et 3 ne le sont pas. **Proposition** : R8a
devrait aussi compter les briques d'une catégorie qu'aucune vue `.base` du vault ne retient.

## 9. `imbalanced-learn` n'a pas de section `## Écosystème` — délibéré

Son `alternatives:` est vide dans le vault, et la prose d'origine disait honnêtement « pas
d'équivalent direct dans le brain ». Cette phrase est passée en `## Définition` ; la section
`## Écosystème` n'a pas été créée pour rester vide. Les approches concurrentes qu'elle citait
— `class_weight`, `scale_pos_weight` — sont en `Écarter si`, avec les liens [[XGBoost]] et
[[LightGBM]]. Aucun contenu perdu.

## 10. Un incident de méthode, à faire tenir aux autres lots

La première fiche convertie (`MLflow`) a été réécrite **de zéro**, frontmatter compris — et une
entrée d'`alternatives:` a disparu au passage ([[TensorBoard]]). Rattrapée avant validation,
mais la conséquence aurait été une **violation dure de R1 sur la branche d'un autre lot** :
`TensorBoard` cite `MLflow`, la réciprocité serait tombée chez le voisin, invisible d'ici.

Les 12 fiches suivantes ont été traitées par un script de trois lignes qui remplace uniquement
ce qui suit le titre `# ` et ne touche jamais au frontmatter.

> À faire tenir aux seize autres : **le lot 6 ne modifie pas le frontmatter**, à la seule
> exception de `complements:`. Le plus sûr est de ne pas se donner la possibilité de le faire —
> remplacer le corps sous le H1, pas le fichier.
