---
role: meta
nom: remontees-lot-4
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 / lot 4 — remontées

Périmètre : « Machine Learning/Apprentissage profond/ » (8 briques), « Machine Learning/
Interprétabilité/ » (7), « Machine Learning/Socle/ » (2) et « Machine Learning/Évaluation de
modèles/ » (2). **19 fiches, le compte annoncé par la table du découpage.** Branche
`claude/lot-4-machine-learning-57b861`.

Conforme aux six règles du protocole parallèle : rien touché hors de ces quatre dossiers,
aucun hub, aucune notion, aucun comparatif, aucun script, aucun document partagé ;
`build_bandeau.py` lancé **borné au périmètre** et jamais édité ; ni `build_index`, ni
`build_mocs`, ni `build_links`, ni `cloturer-brain`.

Mesure avant/après, vault entier : `check_brain.py` passe de **149 à 145 avertissements**,
**0 violation dure** des deux côtés. Le `diff` des deux sorties ne contient que quatre
lignes, toutes des R15 **levées** — `JAX`, `Keras`, `PyTorch Lightning`, `TensorFlow`, qui ne
portaient aucun lien vers une notion ou un hub et pointent désormais le hub de leur dossier.
Aucun avertissement créé. `check_arbo.py` vert, `build_bandeau --check` vert sur les 19.

---

## 1. Divergence assumée avec le pilote sur les puces « besoin → concurrent »

La remontée 7 du pilote laissait le point **à trancher pour les dix-sept** : les puces de la
forme « besoin → [[concurrent]] » vont-elles en `Écarter si`, ou sont-elles réputées déjà
portées par le comparatif du dossier ? Le pilote les a écartées ; **ce lot les garde**.

Trois raisons, dans l'ordre où elles pèsent :

1. **Trois de mes quatre dossiers n'ont pas de comparatif.** Le pilote pouvait renvoyer aux
   onze lignes de `Comparatif - Bases vectorielles`. Ici, seul « Interprétabilité/ » en a un
   (`Comparatif - Explicabilité`). Pour « Apprentissage profond/ », « Socle/ » et
   « Évaluation de modèles/ », écarter la puce ne l'aurait envoyée nulle part — ce que le
   brief interdit explicitement (« aucune puce supprimée sans destination »).
2. **La spec dit le contraire du pilote.** `brain-v3.md` §6 : « chaque exclusion **doit**
   pointer vers l'alternative — ce qui est contrôlable » ; l'exemple canonique du gabarit
   (Faker) met « Respecter la distribution du réel → [[SDV]] » en `Écarter si`, qui est
   exactement la forme condamnée par la remontée 7 ; et le critère d'acceptation du lot 6
   demande un wikilink dans chaque cellule `Écarter si`.
3. **Le profil du corpus n'est pas le même.** Mesuré sur mes 19 fiches d'origine : 67 puces
   en `Quand NE PAS l'utiliser`, dont **35 de la forme « besoin → [[concurrent]] », soit
   52 %** — contre 89 % chez le pilote. La majorité de mes exclusions étaient déjà des bornes
   propres ; le tri n'avait pas le même rendement.

Conséquence pour l'intégration : **les deux formes coexistent dans le vault**, et il faudra
choisir. Si l'arbitrage retient la ligne du pilote, ce sont mes 19 fiches qu'il faut reprendre
— mais il faudra alors créer d'abord les comparatifs manquants (cf. §2), sans quoi le contenu
disparaît.

## 2. « Apprentissage profond/ » n'a pas de comparatif, et ça se voit dans les fiches

`check_brain` le signale déjà : `[WARN] R8a — categorie ml/apprentissage-profond : 8 briques,
aucun comparatif .base ne les réunit`. Ce n'est pas un détail de forme. Quatre fiches du
dossier — `Keras`, `PyTorch Lightning`, `accelerate`, `DeepSpeed` — portaient en fin de
`## Alternatives` un paragraphe « **Nuance :** » qui faisait, mot pour mot, le travail d'une
section « Ce qui départage » :

> « accelerate est **bas niveau** (on garde sa boucle) ; Lightning **impose une structure**.
> Le pendant direct d'accelerate côté Lightning est **Fabric**. Face à DeepSpeed, le partage
> est différent : DeepSpeed est le **moteur** d'optimisation mémoire qu'accelerate sait
> activer par config — on les combine plus qu'on ne les oppose. »

Le nouveau gabarit ne tolère pas de prose dans `## Écosystème`. J'ai donc **replié ces quatre
nuances dans des cellules `Écarter si`**, ce qui les conserve et les rend décisionnelles, mais
les éclate en quatre morceaux qui devront rester d'accord entre eux. Leur vraie place est un
`Comparatif - Frameworks d'entraînement` (ou deux : les trois frameworks d'un côté, les trois
surcouches de l'autre), qui n'existe pas. **À ouvrir après le lot 6** — un lot de conversion
ne crée pas de comparatif, c'était le travail du lot 5.

## 3. Une quatrième destination pour `Pièges` : `## Mise en œuvre`

Le brief en nomme trois — `Écarter si`, `## Définition`, `## Retours`. Sur les **76 puces**
`Pièges` du périmètre, environ **25 (comptées à la main)** n'appartenaient à aucune des trois
mais avaient une place évidente sous une étiquette de `Mise en œuvre` :

| Puce d'origine | Étiquette d'accueil |
|---|---|
| « installer la roue qui correspond au driver/CUDA, sinon GPU non détecté » (PyTorch) | Installation |
| « deux paquets coexistent, `pytorch-lightning` et `lightning`, les imports diffèrent » | Installation |
| « la v3 a changé l'interface, `TransformerBridge` est le point d'entrée » (TransformerLens) | Installation |
| « le backend se fixe **avant** d'importer Keras » | Point d'entrée |
| « sur du texte, agréger au niveau du mot avant d'afficher » (Captum) | Point d'entrée |
| « surveiller les *dead features* » (SAELens) | Exécution |
| « file d'attente NDIF : le mode distant n'est pas interactif » (nnsight) | Exécution |

Ce sont des contraintes d'**installation ou d'exécution**, pas des critères de choix : les
mettre en `Écarter si` aurait pollué la décision, les mettre en `Définition` l'aurait noyée.
**Proposition : inscrire cette quatrième destination dans le brief**, elle est sans ambiguïté
et elle évite que dix-sept conversations l'inventent chacune à sa façon.

## 4. Cellules `Écarter si` sans wikilink — 13, et pourquoi

Le critère d'acceptation demande un wikilink par cellule. **13 cellules sur 19 fiches n'en ont
pas**, et aucune ne peut en recevoir sans inventer :

| Motif | Cellules | Exemples |
|---|---|---|
| Borne de **maturité** ou de **stabilité d'API** | 5 | « Production : outil de recherche » (TransformerLens, SAELens, nnsight), « Development Status :: 3 - Alpha » (interpreto) |
| Borne de **périmètre** sans concurrent référencé | 4 | « Modèles autres que des LLM » (SAELens), « architecture exotique non portée » (TransformerLens) |
| Le substitut est **hors brain** | 2 | « Spark Structured Streaming et MLlib » (River), « efficient-kan, FastKAN » (pykan) |
| Borne **méthodologique** de la famille entière | 2 | « explication destinée à un métier : elle produit des tenseurs, pas des rapports » (Captum, nnsight) |

S'y ajoutent **6 cellules vides** (PyTorch, accelerate, Captum, River, evaluate, seqeval) :
le tableau ne s'équilibre pas, une fiche peut avoir quatre raisons de la prendre et trois de
l'écarter. Jamais comblées — même constat que la remontée 9 du pilote, 17 cellules chez lui.

Une seule cellule a gagné un lien qu'elle n'avait pas : `Scikit-Learn`, « volume qui ne tient
plus en mémoire → [[River]] ». Elle est sourcée des **deux** côtés (River : « trop volumineuses
pour la RAM »), et les deux fiches sont dans mon périmètre.

> **Conclusion pour la règle dure nº 5 du lot 8** : « toute cellule `Écarter si` contient un
> wikilink » n'est pas tenable telle quelle. Environ un tiers des exclusions réelles ne
> pointent vers rien parce qu'il n'y a rien vers quoi pointer. La règle durcissable est plus
> étroite : *toute exclusion qui nomme un besoin couvert par une autre brique du brain porte
> son wikilink*.

## 5. `complements:` — neuf couples posés, sept moitiés laissées ouvertes

Contrairement au pilote (remontée 5), mon périmètre contient les deux bouts de plusieurs
couples. Règle que je me suis donnée, faute qu'elle soit écrite : **un couple `complements:`
suppose que les deux briques s'utilisent ensemble par choix ; une simple dépendance d'exécution
(« bâti sur PyTorch ») reste un lien de `## Voir aussi`.** Sans cette règle, `PyTorch` héritait
de neuf compléments — toutes les briques du vault qui importent `torch`.

Couples posés, réciprocité faite dans les deux fiches :

| A | B | Source |
|---|---|---|
| `PyTorch` | `Keras` | Keras 3 tourne sur backend PyTorch |
| `PyTorch` | `PyTorch Lightning` | Lightning organise du code PyTorch |
| `PyTorch` | `accelerate` | accelerate distribue une boucle PyTorch |
| `PyTorch` | `DeepSpeed` | DeepSpeed s'initialise dans une boucle PyTorch |
| `PyTorch` | `pykan` | pykan n'avait **aucun** voisin déclaré |
| `TensorFlow` | `Keras` | backend par défaut |
| `JAX` | `Keras` | backend visé pour la perf et le TPU |
| `evaluate` | `seqeval` | evaluate charge seqeval comme métrique |
| `interpreto` | `nnsight` | dépendance directe pour l'extraction d'activations |

Moitiés **non posées**, cible hors périmètre — à fermer par le lot qui convertira la cible :

| Fiche du lot | Complément sourcé | Dossier de la cible | Lot |
|---|---|---|---|
| `SHAP` | [[XGBoost]], [[LightGBM]], [[CatBoost]] | Machine Learning/Tabulaire/ | 5 |
| `Scikit-Learn` | [[Prince]] — « écrit sur l'API scikit-learn » | Statistiques & inférence/Analyse factorielle/ | 15 |
| `accelerate`, `DeepSpeed`, `evaluate` | [[HuggingFace]] | Machine Learning/ (niveau domaine) | 6 |
| `accelerate`, `evaluate` | [[datasets]] | Machine Learning/ (niveau domaine) | 6 |

## 6. Un piège de format qui casse le validateur en dur : le wikilink à alias dans un tableau

Écrire un wikilink à alias dans une cellule de tableau **coupe la ligne du tableau**, la barre
verticale de l'alias étant lue comme un séparateur de colonne. L'échapper d'une contre-oblique
répare le rendu Obsidian et **casse `check_brain`** : `LINK_RE` exclut la barre du nom de
cible, la contre-oblique reste donc collée au nom, `link_target_ok` ne trouve pas la page, et
la fiche part en violation **dure** « lien mort ». Vérifié sur la vraie expression du script.

Le gabarit met des wikilinks dans un tableau pour la première fois du vault : les dix-sept
conversations vont toutes rencontrer le cas. **La règle est simple et mérite d'être écrite :
dans une cellule `Prendre si / Écarter si`, un wikilink est toujours nu.** Si l'on veut un
libellé différent du nom de la page, on écrit le libellé en clair et on met le lien à côté.
Trois occurrences dans ce lot, toutes corrigées avant commit.

## 7. La règle 10 (anti-répétition) ne peut pas se vérifier sur le frontmatter brut

Un contrôle maison de la règle 10 — « `## Définition` ne recontient ni la famille, ni la
licence, ni la maturité » — sort **deux faux positifs sur les 19**, tous deux sur `TensorFlow` :
la Définition dit « pensé dès l'origine pour le passage en **production** » (`maturite:
production`) et « l'ancien comportement vit dans le **paquet** `tf-keras` » (`famille: paquet`).

`production`, `paquet`, `modèle`, `application` sont des mots français ordinaires ; les
chercher tels quels dans un paragraphe produira du bruit sur tout le vault. La règle n'est
implémentable que sur les **cellules rendues du bandeau** et avec des motifs bornés, pas sur
les valeurs brutes du frontmatter. À reprendre avant le lot 8, qui veut durcir cette règle.

## 8. Une contradiction sourcée que je n'ai pas corrigée : DeepSpeed n'est pas une alternative

`PyTorch Lightning` et `accelerate` déclarent `DeepSpeed` en `alternatives:`, et les trois
fiches disent le contraire dans leur propre texte :

> « **DeepSpeed** n'est pas un concurrent mais un **backend** : Lightning sait l'activer comme
> stratégie pour le sharding ZeRO. »

C'est un couple `complements:`, pas `alternatives:`. Je ne l'ai **pas** changé : défaire trois
déclarations réciproques touche la section `### Alternatives` des trois fiches et la règle R11,
et le brief du lot 6 demande de *remplir* `complements:`, pas de réviser `alternatives:`. La
nuance est conservée dans la cellule `Écarter si` de Lightning. **À arbitrer à l'intégration.**

## 9. Les quatre fiches sans voisin déclaré gardent une `### Alternatives` en une puce

`pykan`, `River`, `evaluate` et `seqeval` portent `alternatives: []` — ce sont quatre des
fiches que la règle 4 du validateur signale déjà (voisinage déclaré, souple). Leur ancienne
`## Alternatives` contenait de la prose (« pas d'équivalent direct dans le brain, hors brain
Vowpal Wabbit… »). Le gabarit interdit la prose hors `## Définition` ; j'ai gardé **une puce
unique** disant l'absence de substitut et nommant les pistes hors brain. C'est une forme
inventée faute d'être prévue : le gabarit ne dit pas ce que devient `### Alternatives` quand
il n'y a pas d'alternative. **À trancher — puce unique, ou section absente.**

## 10. `## Retours` n'a été créée nulle part, et aucun bandeau n'a de cellule vide

Aucune entrée datée dans le périmètre — la seule du vault reste
`LLM & IA générative/Agents de code/t3code.md` (lot 7). Conforme au brief.

Et contrairement aux sept `famille: application` du pilote (remontée 6), **les 19 fiches
remplissent leurs quatre cellules de bandeau** : `build_bandeau` ne signale aucun trou de
frontmatter. L'hypothèse du pilote — « le champ `maturite:` n'a peut-être jamais été rempli
pour la famille `application` » — se confirme par la négative : mes 19 sont toutes
`famille: paquet`, et toutes complètes.
