---
galaxie: meta
nom: lot-8-durcissement
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 8 — Durcissement du validateur

> [!success] **CLOS le 2026-09-06.** Dernier lot de la migration v3, et la migration est close
> avec lui. Le compte de violations de chaque règle avant durcissement, les deux réécritures et
> ce qui a été vérifié par exécution sont dans le *Journal du lot 8*, en fin de fichier.
> Ce qui suit est le brief d'origine, conservé tel quel.

Effort : **une demi-session**. Dernier lot.

Prérequis : tous les autres lots faits, validateur au vert. **Le lot 6 est clos depuis le
2026-09-06** — il est le dernier à avoir bougé, et ce qu'il verse ici est en fin de fichier.

## Contexte

Le principe tenu depuis la v2 : **on ne durcit pas une règle que le vault viole encore.** Les
règles nouvelles entrent donc en avertissement, et ne passent en erreur dure qu'une fois le
contenu conforme. Ce lot fait ce passage, en dernier, quand le coût de la mise en conformité
est nul par construction.

## Les dix règles de la v3

Spec complète : [[AI/design/brain-v3|brain-v3]] §10.

| # | Règle | État visé |
|---|---|---|
| 1 | Réciprocité d'`alternatives:` et de `complements:` | dure |
| 2 | Le dossier d'une page concorde avec son `categorie:` | dure après lot 3 |
| 3 | Toute brique du dossier apparaît dans le hub du dossier | dure |
| 4 | Une brique isolée dans un dossier peuplé est signalée | **avertissement, définitif** |
| 5 | Toute cellule `Écarter si` contient un wikilink | dure |
| 6 | Réinjection du pitch dans `Alternatives` et `Compléments` | dure |
| 7 | Étiquettes fermées de `Ressources` et `Mise en œuvre` | dure |
| 8 | Pas de double citation d'une cible dans deux sections | dure |
| 9 | Le bandeau généré concorde avec le frontmatter | dure |
| 10 | `## Définition` ne recontient pas famille, licence ni maturité | dure après lot 6 |

La règle 4 reste un **avertissement pour toujours** : une brique peut légitimement n'avoir
aucune alternative. La signaler aide, l'interdire mentirait.

> **Une onzième règle est déjà dure, et n'attend pas ce lot** — R17, *frontmatter lisible*,
> posée le 2026-09-05 en clôture du lot 4 (remontée 44). Elle ne relevait pas du principe
> ci-dessus : ce n'était pas une règle en avertissement à durcir, c'était **l'absence de
> règle**. Une page dont le frontmatter ne parsait pas était silencieusement sautée par
> `check_brain` **et** par `check_arbo` — hors du total, hors de toutes les autres règles,
> liens non résolus, chemin non confronté à sa catégorie. Un `pitch:` non quoté contenant
> « : » suffisait. Le durcir n'a rien coûté : la mesure avant durcissement donnait **zéro
> page** dans ce cas, aucune réparation n'a été nécessaire.

## Procédure

1. Lancer `check_brain.py` et relever le nombre de violations de chaque règle encore souple.
2. Pour chaque règle à **zéro violation** : passer en dure, immédiatement.
3. Pour chaque règle à violations résiduelles : les corriger si elles sont mécaniques, ou les
   écrire dans les *Remontées* du pilote si elles demandent un arbitrage. Ne pas durcir avant.
4. Rebrancher le hook `Stop` — l'audit axe 3 avait mesuré qu'il n'avait **jamais tourné** et
   ne pouvait pas tourner : aucun `settings.json` versionné, chemin de vault faux en dur dans
   `session_to_devbrain.py`. Vérifier que les deux causes sont levées.
5. Mettre à jour le tableau d'avancement du pilote et clore la migration.

## Critères d'acceptation

- [ ] Chaque règle est soit dure, soit souple avec un motif écrit.
- [ ] Aucune exception ajoutée au validateur pour faire passer une règle.
- [ ] Le hook `Stop` tourne réellement — vérifié en fin de session, pas supposé.
- [ ] `AI/design/brain-v2.md` porte une mention en tête renvoyant vers la v3.
- [ ] Le pilote est à jour et la migration close.

## Interdictions

- Ne pas durcir une règle avec des violations résiduelles, même peu nombreuses. Une règle dure
  qui échoue au quotidien finit désactivée, et on perd les dix.
- Ne pas supprimer `AI/design/brain-v2.md` : il documente les arbitrages de la v2 qui restent
  valides, notamment les deux axes `categorie:` × `famille:` et la convention de réinjection
  du pitch.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md §10 puis AI/migration/lot-8-durcissement.md.

Mesure les violations de chaque règle encore souple, durcis uniquement celles à zéro
violation, et montre-moi la liste de ce qui reste avant de conclure.

Vérifie que le hook Stop tourne réellement, ne te contente pas de le déclarer.
```

---

## Ce que le lot 6 verse au lot 8 — arrêté le 2026-09-06

Huit points, tous mesurés sur les 337 fiches converties. Le détail et les mesures par lot sont
dans le *Journal du lot 6* de `AI/migration/lot-6-gabarit.md` ; les numéros de remontée
renvoient à ce journal.

### 1. La règle dure nº 5 est à réécrire — elle est inatteignable telle qu'elle est formulée

**« Toute cellule `Écarter si` contient un wikilink » : 356 cellules sur 1 388, soit 26 %.**
Le taux va de **0 %** — Automatisation no-code, DevOps, Interfaces & apps data — à **44 %**
(Machine Learning). Sur les branches prises isolément, l'écart allait de 0 % (pilote) à 48 %
(lot 10).

Ce n'est pas un défaut de rédaction, et **aucun travail d'enrichissement ne le comblera** : la
cause est l'exact revers de la règle 2 du lot 6. Quand la redirection vers un concurrent part
au comparatif — ce qu'elle doit faire dès que la brique et sa cible sont co-membres d'une
vue —, ce qui reste sur la fiche est une **borne dure de la brique seule**, qui ne pointe vers
personne : « le cache n'est jamais purgé seul », « `max_elements` est fixé à l'initialisation »,
« il n'y a pas de révocation native ».

Deux familles composent les 1 032 cellules sans lien, et la seconde est celle qu'il faut nommer
dans la règle :

- **la borne n'a pas de substitut**, parce qu'elle décrit une limite de conception, une
  maturité, ou une plateforme non supportée ;
- **la cible n'existe pas dans le vault.** Le lot 14 cite dix-neuf outils non fichés — Click,
  argparse, Fire, mypy, unittest, conda, MkDocs, attrs, Flake8, Black, isort, pylint… — et le
  lot 17 en ajoute six : Wireshark, `rsync`, Qualys SSL Labs, Pyomo, Podman, Kubernetes.
  Exiger un wikilink les rendrait **tous obligatoires à ficher**, ce qui n'est pas une décision
  de format.

Deux reformulations sont proposées par les lots, et elles disent la même chose :

> « Toute cellule `Écarter si` **dont le motif est une redirection** porte un wikilink ; une
> redirection vers une cible déjà déclarée en `alternatives:` n'en est pas une, elle est portée
> par `### Alternatives` et par le comparatif du dossier. » — lot 5

> « Toute exclusion qui nomme un besoin **couvert par une autre brique du brain** porte son
> wikilink. » — lot 4

La seconde est la plus courte et la plus contrôlable : elle se vérifie en cherchant, dans le
texte de la cellule, le `nom:` ou un `alias:` d'une brique du vault non lié. **Sous cette
forme, la règle est durcissable ; sous sa forme actuelle, non.**

> Corollaire à ne pas rater : la remontée 20 du lot 5 des comparatifs **condamne** la sortie
> facile. Réécrire les 1 032 bornes sous forme comparative pour leur donner une cible ferait
> exactement ce que le lot 5 a passé quatre sessions à défaire.

### 2. La règle dure nº 8 est à réécrire aussi, et pour la même raison

**« Pas de double citation d'une cible dans deux sections » est impossible** dès qu'une
catégorie n'a pas de comparatif. Le mécanisme est arithmétique, et quatre lots l'ont décrit
indépendamment (10, 12, 13, 14) : la règle 2 **garde** la cible en `Écarter si` faute de
comparatif d'accueil, et **R11 — violation dure — exige** qu'elle figure en `### Alternatives`.
Les deux contraintes sont dures et contradictoires.

Le lot 16 en donne la preuve par corrélation, sur cinq dossiers choisis pour couvrir les deux
cas : 20 doublons dans Stockage (aucun comparatif), 2 dans Web & API (aucun pour 4 fiches sur
6), **0** dans Automatisation no-code et Interfaces & apps data, dont toutes les briques sont
co-membres d'une vue. Le recouvrement apparaît exactement là où aucun comparatif ne peut porter
la redirection, et nulle part ailleurs.

La lecture qui sauve la règle est celle du lot 9, et elle **restitue le défaut d'origine** que
la règle visait — sur la page Faker, Mimesis apparaissait en `Alternatives` **et** en `Liens`,
deux **listes de liens** :

> La règle porte sur les **sections de liste de liens** — `### Alternatives`,
> `### Compléments`, `## Voir aussi`. La prose de `## Définition` et les cellules du tableau de
> décision ne sont pas des listes de liens et peuvent citer librement.

**Sous cette lecture, les 337 fiches sont conformes**, et la règle est durcissable telle
quelle. Deux cas restent à trancher séparément, parce qu'ils ne relèvent d'aucune des deux
lectures :

- `docTR → [[OCR]]`, présent en `Écarter si` **et** en `## Voir aussi` (lot 11). Supprimer le
  renvoi perd l'orientation, supprimer le lien parent casse R15 ;
- `jupytext ↔ papermill` (lot 14), à la fois **redirection** — « si vous ne voulez qu'exécuter
  en CI, prenez papermill » — et **complément** — « l'appariement versionne le source,
  papermill l'exécute ». Les deux phrases sont vraies et ne disent pas la même chose.

### 3. R8a a un angle mort, et il vaut 38 briques

R8a vérifie qu'une **catégorie** a un comparatif. Elle ne vérifie pas que ses **briques** y
entrent — une vue peut filtrer par tag, ou par une liste de noms, et laisser dehors des briques
de son propre dossier. Le décompte, fait à l'intégration sur les 47 vues :

| | Briques |
|---|---|
| membres d'**aucune** des 47 vues | **89 sur 337 (26 %)** |
| — dont relevant des 13 catégories que R8a signale | 51 |
| — dont **invisibles à R8a** : leur catégorie *a* un `.base`, elles n'y entrent pas | **38** |

Les 38 se répartissent sur 28 catégories. Les deux groupes les plus nets ont été trouvés à la
main par les lots concernés, chacun croyant à un cas isolé : `ml/tabulaire` — Featuretools,
category_encoders, imbalanced-learn, hors du `file.hasTag("boosting")` de leur vue (lot 5) — et
`ml/vision` — Kornia, timm, torchvision, hors du filtre `object-detection or segmentation`
(lot 3). Le lot 15 en trouve trois de plus dans `Calcul distribué/`, où le `.base` filtre
`compute/distribue or compute/gpu` et laisse dehors les trois bacs à sable.

**Proposition du lot 5, à retenir** : R8a doit aussi compter les briques d'une catégorie
qu'**aucune vue du vault ne retient**. C'est la seule formulation qui attrape les 38.

La conséquence est directe sur la règle 2 du lot 6 : une brique hors de toute vue garde
**toutes** ses redirections en `Écarter si`, faute de comparatif d'accueil. Les 89 briques
ci-dessus sont donc aussi celles qui pèsent le plus dans le taux de la remontée 1.

### 4. Cinq comparatifs manquants, signalés par la conversion

Un lot de conversion ne crée pas de comparatif — c'est le travail du lot 5. Mais lire 337
fiches à la file fait apparaître les trous, et **l'axe de départage est déjà écrit** dans les
fiches, ce qui rend chacun bon marché à ouvrir :

| Catégorie | Briques | Ce qui départage, déjà écrit | Signalé par |
|---|---|---|---|
| `ml/apprentissage-profond` | **8** | quatre paragraphes « Nuance : … » faisaient mot pour mot le travail d'une section « Ce qui départage » : bas niveau contre structure imposée, moteur d'optimisation contre surcouche, `Fabric` comme pendant d'`accelerate` | lot 4 |
| `llm/assistant` | 5 | et `Comparatif - Frameworks LLM` les **exclut explicitement** par un commentaire de son propre filtre | lot 8 |
| `data/format` | 3 | Parquet contre Avro, colonnaire contre ligne ; Iceberg au-dessus des deux, qui n'est pas un format mais une sémantique de table | lot 13 |
| `data/synthetique` | 3 | Faker contre Mimesis, écosystème contre vitesse ; SDV ailleurs, il apprend une distribution | lot 13 |
| `compute/a-la-demande` | 3 | Daytona, E2B, Modal partagent un dossier avec quatre moteurs sans partager leur vue | lot 15 |

Le cas de `ml/apprentissage-profond` est le plus coûteux des cinq, et c'est celui à ouvrir en
premier : faute de comparatif, les quatre « Nuance » du lot 4 ont dû être **repliées en cellules
`Écarter si`**, ce qui conserve l'information mais l'éclate en quatre morceaux qui devront
rester d'accord entre eux.

Un sixième trou, d'une autre nature : `Comparatif - Gestionnaires de paquets Python` ne dit
rien de la **vitesse**, alors que `pip → uv` sur la vitesse était la redirection la plus nette
de la fiche `pip` (lot 14). L'intégration a retenu la borne sur la fiche ; ajouter la vitesse
au comparatif reste possible.

### 5. `verifier_fraicheur.py` — une règle morte réparée, une extension à faire

**Réparé à la clôture du lot 6, parce que c'est le lot 6 qui l'avait cassé.** Sa constante
`SECTIONS` — les sections « qui parlent du sujet lui-même » — valait `{Pourquoi, Déploiement &
coût, Installation & plateformes, Pièges}` : **les quatre noms d'avant, qui n'existent plus sur
aucune des 337 fiches**. `lignes_sujet()` ne rendait plus une seule ligne, et la règle C2
(`corps_declin_vs_maturite_vive` — le corps décrit un projet en déclin alors que `maturite:`
le dit vivant) était morte sur le vault entier, **en silence** : le script sort 0 en toutes
circonstances, et une règle qui ne trouve rien ressemble à une règle satisfaite. Le
commentaire du script anticipait pourtant la rupture — « le lot 6 fusionnera les deux en
*Mise en œuvre* ».

Corrigé vers les sections v3. Mesure après : **7 890 lignes** balayées contre 0, et **4
signalements** C2 — `pytorch-crf` (« dormant : dernière release en 2019 »), `rank-bm25`,
`selectolax`, `RAGatouille`. Quatre fiches dont le corps dit le déclin et dont le frontmatter
dit le contraire : c'est exactement ce que la règle existe pour trouver.

> À retenir au-delà de ce cas : **un script qui filtre sur un nom de section est cassé par
> toute refonte de gabarit, et il ne le dit pas.** Le lot 8 gagnerait à ce que
> `verifier_fraicheur.py` échoue bruyamment quand `SECTIONS` ne matche rien sur les 337 fiches
> — un compteur à zéro n'est pas une bonne nouvelle.

### 5 bis. Il reste à le brancher sur les comparatifs

**Onze puces datées vivent dans les pages de comparatif** — Helicone en maintenance mode depuis
le rachat Mintlify, RAGatouille dont la maintenance s'arrête en mai 2025, Vanna dont le dépôt
OSS est archivé le 29 mars 2026, promptfoo racheté par OpenAI en mars 2026, TorchServe archivé
le 7 août 2025, Seldon basculé en BSL le 22 janvier 2024, la fermeture de TensorBoard.dev, le
tier Teams de Flyway fermé aux nouveaux clients depuis mai 2025 (relevé du lot 9, remontée 7, et
des lots 3 et 17).

Ce sont exactement les faits que `verifier_fraicheur.py` existe pour surveiller, et **il ne les
voit pas** : son périmètre ne couvre pas `role: comparatif`. Une page de comparatif est une page
comme une autre depuis la clôture du lot 5, le 2026-09-06 — le script n'a simplement pas été
rebranché.

C'est un travail de deux lignes de périmètre, et il vaut mieux le faire au lot 8 qu'au moment
où l'un de ces onze faits sera devenu faux sans que rien ne l'ait dit.

### 6. Les règles que le lot 6 rend durcissables sans travail, et celles qui coûtent

Relevé sur les 337 fiches, le 2026-09-06 :

| Règle | Violations résiduelles | Verdict |
|---|---|---|
| 9 — le bandeau concorde avec le frontmatter | **0** — `build_bandeau.py --check` vert sur les 337 | **durcissable tel quel** |
| 7 — étiquettes fermées de `Ressources` et `Mise en œuvre` | **0** sur `Mise en œuvre` (les cinq étiquettes, 337 fois) ; **4** sur `Ressources`, toutes `Site` | durcissable après décision sur `Site` — cf. remontée 7 ci-dessous |
| 10 — `## Définition` ne redit pas le bandeau | 0 après reformulation, **mais le test ne se scripte pas entièrement** | durcissable, avec la réserve ci-dessous |
| 6 — réinjection du pitch | 0 | durcissable |
| 1 — réciprocité d'`alternatives:` **et de `complements:`** | 0 après l'intégration — 154 demi-arêtes, aucune asymétrie | **durcissable, et il faut le faire** : rien ne contrôle aujourd'hui la réciprocité de `complements:`, et c'est ce qui a laissé douze moitiés orphelines pendant tout le lot |
| 3 — toute brique du dossier apparaît dans le hub | 0, les zones AUTO étant générées | durcissable |
| 5 et 8 | cf. remontées 1 et 2 | **à réécrire avant de durcir** |

**La réserve sur la règle 10**, mesurée par quatre lots (4, 10, 14, 15) : `production`,
`paquet`, `modèle`, `application` et `open-source` sont des mots français ordinaires. Les
chercher tels quels dans un paragraphe produit du bruit — « pensé dès l'origine pour le passage
en **production** », « une app de production », « le projet reste maintenu en **open-source** ».
Le test n'est implémentable que sur les **cellules rendues du bandeau**, avec des motifs bornés,
et il ne se scripte **jamais** pour la valeur `production`. Sur celle-là, c'est une relecture.
Les lots 14 et 15 rappellent qu'il attrape tout de même de vraies fuites qu'aucune relecture ne
voit — trois sur 20 fiches pour l'un, trois sur 24 pour l'autre.

### 7. Six décisions de forme, laissées ouvertes par les lots

Aucune n'est bloquante ; toutes produisent aujourd'hui deux conventions concurrentes dans le
vault.

1. **Une étiquette `Site` dans le vocabulaire de `## Ressources` ?** Quatre puces l'emploient
   déjà (lots 16 et 17) pour un site officiel de projet distinct de la doc et du dépôt —
   `opencut.app`, `superwhisper.com`, `sniffnet.app`, `getcroc.com`. Le lot 7 a choisi l'autre
   voie, `- Documentation — https://t3.codes (site du projet)`, qui produit deux lignes
   `Documentation` sur la même fiche. Le lot 3 signale un besoin voisin pour une **licence**,
   l'AGPL d'`Ultralytics YOLO` ayant sa propre URL et étant *le* critère de choix de la brique.
2. **`url_docs == url_repo` : une ligne ou deux ?** Trois traitements coexistent — une ligne
   `Dépôt` « qui tient lieu de documentation » (lot 2), `- Documentation — le README du dépôt ;
   il n'existe pas de site séparé` (lot 16), une seule ligne `Dépôt` sans glose (lot 6).
3. **`## Écosystème` est-elle obligatoire ?** Quatre fiches ne la portent pas — `Ruff`,
   `Obsidian`, `Quarto` (lot 14) et `imbalanced-learn` (lot 5) — parce que leur `alternatives:`
   est vide. Rien ne le vérifie : `check_brain` ne contrôle `### Alternatives` que si le champ
   est non vide. La forme du lot 15 est la meilleure candidate à généraliser, parce qu'elle dit
   **pourquoi** il n'y a rien et nomme le concurrent hors brain : *« Aucune dans le brain :
   lifelines est la seule bibliothèque d'analyse de survie répertoriée, et son pendant ML,
   scikit-survival, n'y figure pas encore. »*
4. **Un `###` de données sous `## Mise en œuvre` ?** Le lot 16 a conservé le tableau des 13
   modèles locaux de `Superwhisper` sous un `### Modèles locaux disponibles`, après les cinq
   étiquettes. *« Perdre treize lignes de données sourcées pour tenir une forme aurait été le
   mauvais arbitrage. »*
5. **Un numéro de version daté a-t-il sa place dans une fiche ?** Le lot 17 en a conservé un
   (`Web-Check`, 2.2.0 au 2026-07-28) et perdu deux (`Beszel` v0.18.8, `Stirling PDF` v2.14.3),
   sur le même lot. Deux traitements pour un même type de fait, et le gabarit v3 n'a pas de case
   pour ce qui se périme.
6. **`famille:` devrait être requis.** R14 contraint la valeur quand elle est présente et
   **laisse passer l'absence** : `Outils de développement/Obsidian.md` n'en porte pas, échappe
   donc à R14 *et* à R16, et perd deux colonnes de bandeau sur quatre (lot 14). Le correctif est
   d'une ligne.

### Ce qui n'est PAS pour le lot 8 — le backlog d'enrichissement

À verser à `AI/backlog-enrichissement-brain.md`, parce que c'est du **contenu** et non de la
règle : les **39 champs de frontmatter vides** que `build_bandeau.py` nomme à chaque passage,
34 en `maturite:` seule (le trou suit les **dossiers** saisis sans ce champ, pas la famille —
six lots l'ont mesuré) ; les **six déclarations d'`alternatives:` que la fiche elle-même
dément**, `t3code`, `Spec Kit` et `BMAD` qui se placent *au-dessus* de ce qu'elles déclarent
concurrent, `PyTorch Lightning` et `accelerate` qui déclarent `DeepSpeed` alors que les trois
fiches disent que c'est un backend ; et les **briques nommées mais non fichées** — `psycopg 3`
et `asyncpg` (lot 1), `scikit-survival` (lot 15), `verl` et `OpenRLHF` (lot 8), les onze
solveurs de `PuLP` (lot 17).

Deux **notions** citent en prose une catégorie qui n'existe plus — `Contrats de données &
qualité` (`data/quality`) et `Versionnage de données` (`data/versioning`). Elles n'ont pas été
corrigées : ce sont des pages `role: notion`, et on ne les réécrit pas sans que floSa l'ait
demandé.

---

## Journal du lot 8 — clos le 2026-09-06

> Une conversation, la 39e. Dernier lot de la migration v3, et le seul dont le livrable
> principal est un **tableau de mesures** : la sévérité de chaque règle est le résultat d'un
> comptage, jamais d'une intention.

### Le constat de départ, qui n'était pas celui du brief

Le brief suppose dix règles implémentées, dont trois « démarrent en avertissement ». La
lecture du code dit autre chose : **quatre règles sur dix étaient écrites**. Les six autres
n'étaient pas souples, elles étaient **absentes** — et une règle absente ne ressemble pas à
une règle souple, elle ressemble à une règle satisfaite. C'est le défaut exact que le lot 6
a trouvé dans `verifier_fraicheur.py`, à un autre endroit du même outillage.

| Règle du §10 | État réel avant le lot 8 |
|---|---|
| 1 — réciprocité | écrite pour `alternatives:` **seulement** |
| 2 — chemin ↔ catégorie | écrite, dure, dans `check_arbo.py` |
| 3 — brique dans le hub | **absente** (R7 vérifiait « atteignable depuis un hub », pas « présente dans le hub de son dossier ») |
| 4 — voisinage déclaré | **absente** |
| 5 — exclusion sourcée | **absente** |
| 6 — réinjection du pitch | écrite pour `alternatives:` **seulement** |
| 7 — étiquettes fermées | **absente** |
| 8 — pas de double citation | **absente** |
| 9 — bandeau à jour | écrite dans `build_bandeau.py --check`, **exécutée par rien** |
| 10 — anti-répétition | **absente** |

Écrire d'abord, mesurer ensuite, durcir en dernier : c'est l'ordre qui a été suivi, et
c'est ce qui rend le tableau ci-dessous vérifiable.

### Le tableau des mesures — 337 briques, 764 pages, le 2026-09-06

| Code | Règle | Violations mesurées | Verdict |
|---|---|---|---|
| R12 | réciprocité d'`alternatives:` | 0 | **dure** (l'était déjà) |
| R18 | réciprocité de `complements:` | **0** | **durcie** |
| R19 | brique présente dans le hub de son dossier | **0** | **durcie** |
| R21 | règle 5 réécrite | **1** → 0 | **durcie** après réparation |
| R22 | pitch réinjecté en `### Compléments` | **2** → 0 | **durcie** après réparation |
| R23 | cinq étiquettes de `## Mise en œuvre` | **0** | **durcie** |
| R24 | règle 8 réécrite | **0** | **durcie** |
| R15 | un lien vers une notion ou un hub | **0** | **durcie** (souple depuis la v2) |
| — | règle 2, chemin ↔ catégorie | 0 | dure, `check_arbo.py` sort 1 |
| — | règle 9, bandeau ↔ frontmatter | 0 | dure, `build_bandeau.py --check` sort 2 — **et entre dans `cloturer-brain`** |
| R20 | règle 4, voisinage non déclaré | **62** | **souple définitivement**, par conception |
| R23 | étiquette de `## Ressources` | **5** | **souple**, arbitrage de vocabulaire à floSa |
| R26 | règle 10, `## Définition` ↔ bandeau | **4** signalés, 11 candidats | **souple définitivement**, non scriptable |
| R8e | angle mort de R8a *(nouvelle)* | **11** | souple, comme toute la famille R8 |
| R14b | absence de `famille:` *(nouvelle)* | **1** | souple par décision de taxonomie |
| R5 | collisions d'alias | 13 | souple, décision d'audit v2 |
| R8a/b/c/d | couverture des comparatifs | 15 | souple, décision éditoriale |

**28 avertissements avant, 111 après.** La hausse est le but : 83 des 84 nouveaux viennent de
règles qui n'existaient pas et qui disent maintenant ce qu'elles voient. Zéro violation dure.

### Les deux réécritures

#### Règle 5 — aucune des deux reformulations proposées ne tient seule

Le brief demandait de choisir l'une des deux, ou de dire pourquoi aucune ne tient. **Aucune
ne tient prise séparément**, et la mesure le montre :

| Forme | Violations | Ce qui ne va pas |
|---|---|---|
| d'origine — « toute cellule `Écarter si` contient un wikilink » | **1 031** / 1 388 cellules | inatteignable, et aucun enrichissement ne le comble |
| lot 4 — « nomme un besoin couvert par une autre brique » | **177** | confond *nommer* une brique et *rediriger* vers elle. « Centré Postgres : inutile dès qu'il faut toucher un autre moteur » nomme Postgres sans lui renvoyer personne. Les alias courts ajoutent du bruit — `fabric` (PyTorch Lightning) attrapé dans une phrase sur Neo4j, `scipy` dans une phrase sur CuPy |
| lot 5 — « le motif est une redirection » | **18** | 5 sont des flèches de **version** (`0.x → 1.x`, `ONNX → TensorRT`, `v1 → v2`), 13 des redirections vers une cible **hors brain** (`→ argparse`, `→ unittest`, `→ mypy`, `→ un wiki d'équipe`, `→ Textual`). Les exiger rendrait vingt-cinq outils non fichés obligatoires à ficher |
| **conjonction retenue** | **1** | — |

La forme retenue : **une cellule qui redirige — la flèche le dit — et dont la cible est une
brique fichée, porte son wikilink.** Le lot 5 fournit la *position*, le lot 4 la *condition*.
345 des 1 388 cellules portent une flèche ; 17 la portent sans lien, et aucune de ces 17 ne
nomme une brique du brain — ce sont toutes des cibles externes ou des sauts de version.

La violation unique était `Machine Learning/Socle/River.md` : « Entraînement distribué
multi-nœuds sur flux → Spark Structured Streaming et MLlib, **hors brain** », alors que
`Calcul distribué/Spark.md` existe. La même affirmation fausse figurait deux lignes plus bas,
en `### Alternatives` ; les deux sont corrigées.

#### Règle 8 — la lecture du lot 9, plus une précision qu'il fallait ajouter

La lecture « sections de liste de liens » est la bonne, et le lot 6 l'annonçait conforme sur
les 337 fiches. **Elle ne l'était pas tout à fait : 1 violation**, `CausalImpact.md`, où
`[[Diff-in-Diff]]` apparaît en `### Alternatives` et en `## Voir aussi`.

Et ce cas n'est **pas** un défaut : la puce d'`Alternatives` est celle que le lot 6 recommande
lui-même pour une section vide — « Aucune outillée dans le brain : côté méthode, l'approche
concurrente est [[Diff-in-Diff]] ». Le lien y **explique**, il ne liste pas. Punir cette forme
aurait fait du validateur l'adversaire de sa propre recommandation.

D'où la précision : la règle porte sur ce qu'une puce **liste**, c'est-à-dire sur les liens de
son **entrée** — ce avec quoi elle commence, éventuellement plusieurs enchaînés par `·`. Sous
cette forme : **0 sur 337**, et le défaut d'origine est toujours attrapé (Mimesis listé en
`Alternatives` **et** en `Liens` sur la page Faker, deux listes de liens).

Contrôle inverse, pour être sûr que la règle voit encore quelque chose : la lecture « toutes
sections confondues » donne **242 violations**. Ce n'est pas une règle assouplie jusqu'à
l'inutilité, c'est une règle recentrée sur ce qu'elle visait.

### L'angle mort de R8a — les « 38 briques » se décomposent

Le compte du lot 6 est reproduit **à l'unité** : 89 briques hors de toute vue, 51 dans les 13
catégories que R8a signale, **38 invisibles à R8a**, sur 28 catégories. Ce que le lot 8 ajoute,
c'est que ces 38 ne sont pas un bloc :

- **11** sont le vrai défaut : une vue existe pour leur catégorie, elle retient leurs pairs, et
  son filtre les a laissées dehors. Réparable en élargissant un filtre. C'est ce que **R8e**
  signale, et il retrouve les deux groupes que les lots 3 et 5 avaient trouvés à la main —
  `ml/tabulaire` (Featuretools, category_encoders, imbalanced-learn) et `ml/vision` (Kornia,
  timm, torchvision) — plus cinq autres qu'aucun lot n'avait vus ;
- **27** vivent dans une catégorie de **1 ou 2 briques**, où aucun comparatif n'a de sens : les
  seuils sont à 3 briques et 2 membres, et à raison. Les signaler aurait produit 27
  avertissements irréparables et rendu R8a illisible. Leur seule issue est de **ficher des
  voisins**, donc le backlog d'enrichissement.

La proposition du lot 5 — « R8a doit aussi compter les briques qu'aucune vue ne retient » —
est donc retenue **dans sa moitié réparable**, et le reste est versé au backlog avec son
décompte. Attraper les 38 sans distinguer les deux populations aurait fabriqué du bruit.

### `verifier_fraicheur.py` — le branchement n'était pas « deux lignes »

Le lot 6 estimait le branchement sur les comparatifs à « un travail de deux lignes de
périmètre ». Ce n'en est pas : ajouter `comparatif` au filtre de rôle **n'aurait rien
produit**. Les deux règles hors ligne lisent `maturite:` et `alternatives:`, qu'un comparatif
ne porte pas — le compteur serait resté à zéro, et un compteur à zéro ressemble à une règle
satisfaite. Exactement le piège que le lot 6 venait de trouver, à deux fichiers de là.

Il a donc fallu une règle **croisée**, C2' : le fait est écrit sur le comparatif, le champ
qu'il contredit vit sur la fiche, et personne ne relit les deux ensemble. 258 puces
confrontées, **5 contradictions** — rank-bm25, Helicone, RAGatouille, promptfoo, evaluate. Les
silences sont vérifiés un par un : Vanna, TorchServe, Neptune et LIME sont déjà
`maturite: deprecated`, donc le frontmatter est d'accord avec le comparatif ; Seldon Core est
un fait de **licence** (BSL), pas de maturité.

Deux ajouts au passage : `FIN_DE_VIE`, qui couvre les faits de cycle de vie que `DECLIN` ne
voyait pas (dépôt archivé, rachat, service fermé, bascule BSL) et qui trouve 4 fiches de plus
— Flyway, Helicone, TruLens, promptfoo ; et l'**autotest** que le lot 6 demandait : le script
compte au démarrage ce que ses filtres attrapent, et s'ils n'attrapent rien il l'annonce en
bannière et sort en **3**. Le contrat « toujours 0 » protège le vault d'un dépôt tiers en
panne ; il n'a jamais couvert le script lui-même en panne, et c'est cette confusion qui a
laissé la règle C2 morte pendant tout le lot 6.

Défaut de périmètre corrigé du même geste : `Templates/` n'était pas écarté du balayage, et
ses deux gabarits portent `role: brique`. Le script annonçait « 339 fiches » sur un vault qui
en compte 337.

Et un **troisième** défaut de la même famille, trouvé à la clôture même du lot, en lisant le
diff : le side-car `AI/index/fraicheur.json` portait **101 entrées, toutes clés en
`Dev/Outils/…` et `Dev/Services/…`** — des chemins qui n'existent plus depuis le lot 3.
Aucune ne correspondait donc plus à une page. Conséquence invisible : `frais()` ne trouvait
jamais rien, le mécanisme de reprise (« ne pas re-sonder une fiche sondée depuis moins de
`--age-max-jours` ») était **mort**, et le script re-sondait tout le vault à chaque passage
sans que rien ne le dise. Trois fois le même schéma dans un seul fichier — une clé dérivée
d'un nom de section, d'un rôle, ou d'un chemin, cassée par une réorganisation, et muette.

Il n'y a pas de remède par une clé stable : une page du vault n'a pas d'identifiant. Ce qu'on
peut faire, c'est refuser de se taire — le script compte maintenant les entrées du side-car
qui ne visent plus aucune page et les nomme. Vérifié en remettant l'ancien side-car en place :
« 101 entrée(s) du side-car ne visent plus aucune page ». Les 101 entrées mortes ont été
purgées par le premier passage du script réparé ; rien d'utilisable n'a été perdu, puisque
rien ne pouvait plus les lire.

### Ce qui a été vérifié par exécution, et non déclaré

Le brief insiste sur un point, et il a raison : **une règle qui ne trouve jamais rien
ressemble à une règle satisfaite.** Rien de ce qui suit n'est une lecture de code.

- **Les sept règles dures refusent réellement.** Sept cas de non-conformité fabriqués un par
  un sur des pages réelles — `complements:` déréciproqué, puce de `Compléments` tronquée,
  redirection délinkée, étiquette `Install` au lieu d'`Installation`, cible listée deux fois,
  hub délié, `## Voir aussi` vidé. Chacun refusé sous **son propre code R**, vault remis vert
  après les sept.
- **Les hooks git refusent.** Dépôt de test isolé : message propre accepté ; trailer refusé au
  commit ; casse basse refusée ; trailer **commenté** accepté (git le retirera) ; `commit-msg`
  retiré → commit refusé ; trailer forcé en `--no-verify` → **push refusé et distant
  immobile** ; `amend` puis push accepté. Non-régression d'identité : `aosis.net` toujours
  refusé au commit et au push.
- **L'autotest de `verifier_fraicheur` refuse.** `SECTIONS` remis aux quatre noms d'avant le
  lot 6 → bannière et code 3 ; `PUCE_COMPARATIF` neutralisée → bannière et code 3 ; scripts
  remis → code 0.
- **Le hook `Stop` tourne.** Payload réel : arbre propre → « aucune écriture », `check_brain`
  non lancé, code 0 ; page touchée et vault vert → « check_brain vert », silencieux ; page
  touchée et violation dure → `systemMessage` portant les `[FAIL]`, code 0 (il ne bloque
  jamais).

Cette dernière vérification a trouvé **deux défauts que la relecture ne montrait pas**, et
c'est tout l'argument pour exécuter :

1. `run_check_brain()` lançait son sous-processus en `text=True` sans `encoding`, donc décodait
   en cp1252 une sortie UTF-8. Le `systemMessage` arrivait en mojibake — « contrÃ´lÃ©es » —
   illisible par le lecteur auquel il est destiné. L'appel voisin, `touched_in_git()`, passait
   déjà l'encodage.
2. Le message portait la **queue brute** de la sortie sur 2 000 caractères. Ça marchait avec 28
   avertissements ; ce lot les a portés à 111, et la queue s'est mise à charrier des R20 et des
   R8e avant d'arriver à la seule chose utile. **C'est mon propre changement qui a cassé ce
   message**, et le réparer faisait partie du lot. Il ne remonte plus que les lignes `[FAIL]`.

### La seule chose qui manque, et qui n'est pas un bug

`session_to_devbrain.py`, la seconde moitié du hook `Stop`, ne produit rien sans
`ANTHROPIC_API_KEY`, et la variable n'est pas positionnée sur cette machine. C'est la cause du
trou dans `AI/sessions/`, qui s'arrête au 2026-09-03 alors que les lots 5, 6 et 7 ont tourné
depuis. Le script est branché, résout correctement le vault, et sort proprement en 0. **Les
deux causes que l'audit axe 3 avait relevées sont bien levées** — `settings.json` est versionné
avec sa clé `hooks.Stop`, et plus aucun chemin de vault n'est en dur. Il lui manque une clé,
qui est une donnée personnelle et appartient à floSa.

### Gouvernance

- **Les hooks git passent de deux à trois.** Cinq commits de `main` portent un trailer
  `Co-Authored-By` — 859cc55, 2b6dde7, f23d72f, aaeda03, b18a4e3, tous du lot 6. Les hooks ne
  les ont pas vus, et ce n'était pas un bug : ils cherchent une adresse dans l'**identité**, et
  un trailer est une ligne de **message**. `pre-commit` ne peut pas porter ce test — git
  l'exécute **avant** de composer le message, et `COMMIT_EDITMSG` porte alors encore celui du
  commit précédent. Le mettre là aurait écrit une règle qui ne voit rien. D'où
  `.githooks/commit-msg`, seul hook à recevoir le message ; `pre-commit` garde le rôle de
  refuser un commit quand **ce hook-là n'est pas installé** ; `pre-push` scanne aussi les
  messages de la plage poussée, ce qui couvre le `--no-verify` et le commit importé.
  Les cinq commits déjà poussés ne sont **pas** rattrapés : les retirer demanderait une
  réécriture d'historique, qui ne se décide pas seule.
- **25 branches `claude/` supprimées côté `origin`**, chacune après vérification qu'elle est
  bien ancêtre de `main`. Il ne reste sur `origin` que `main` et la branche du lot 8,
  `claude/lot-8-validateur-durcissement-2472bf`. Les 54 branches **locales** et les 27
  worktrees encore montés ne sont pas touchés — cf. les *Remontées* du pilote.

### Les cinq comparatifs manquants, et les six décisions de forme

Aucun n'est traité ici, et c'est la règle du lot : ce sont du **contenu**, pas de la règle.
Tous versés à `AI/backlog-enrichissement-brain.md` avec leur axe de départage déjà écrit, en
sept sections. Des six décisions de forme du lot 6, deux ont un effet sur une règle et sont
donc tranchées ici — l'étiquette `Site` (R23 reste souple, l'arbitrage est à floSa) et
`famille:` requis (R14b, refusé parce que contraire à `taxonomie.md`). Les quatre autres sont
des conventions de rédaction : elles restent au backlog.

### Critères d'acceptation

- [x] Chaque règle est soit dure, soit souple **avec un motif écrit** — dans le code, à côté de
      la règle, et dans le tableau ci-dessus.
- [x] **Aucune exception ajoutée au validateur pour faire passer une règle.** Deux règles ont
      été *réécrites*, ce qui n'est pas la même chose : la mesure a montré leur formulation
      inatteignable, et la nouvelle forme est plus stricte que l'ancienne sur ce qu'elle vise
      (contrôle : la lecture large de la règle 8 donne 242 violations, la lecture retenue en
      trouve toujours le défaut d'origine). Trois pages ont été réparées, pas contournées.
- [x] Le hook `Stop` tourne réellement — vérifié par exécution, avec deux défauts trouvés et
      corrigés au passage. Sa moitié « résumé » attend une clé d'API, et c'est écrit.
- [x] `AI/design/brain-v2.md` porte une mention en tête renvoyant vers la v3.
- [x] Le pilote est à jour et la migration close. Aucune décision n'y reste ouverte sans être
      tranchée ou nommée comme reportée ; `brain-v3.md` ne parle plus d'aucun lot au futur.

---

## R25 — le trou de périmètre, refermé le 2026-09-06

Le lot 8 avait constaté le symptôme sur `README.md` (seul fichier illisible du dépôt, hors
périmètre de R17) sans refermer la cause. Elle est mesurée : **ni la racine, ni
`Documentation/`, ni `Templates/` n'entrent dans le périmètre des deux validateurs**, qui
énumèrent les dossiers de premier niveau portant des pages.

Conséquence constatée le 2026-09-06, deux jours après la clôture de la migration : `Inbox.md`,
`Home.md`, `CHANGELOG.md` et **onze** documents de gouvernance portaient encore
`galaxie: meta` ou `type:`, champs supprimés au lot 2. Aucune des quarante conversations de
migration ne l'a vu, parce que rien ne regardait là.

**R25, dure** : aucun des cinq champs supprimés par la v3 — `galaxie`, `type`, `status`,
`remplace_par`, `indexe` — ne survit dans le frontmatter d'un `.md` de la racine, de
`Documentation/` ou de `Templates/`.

`AI/` en est exclu délibérément : ses journaux de lot **citent** ces champs pour raconter leur
suppression. Une règle qui les y interdirait rendrait impossible d'écrire l'histoire de la
migration.

Compte à l'écriture : 7 violations, toutes dans `Documentation/` — corrigées dans le même
commit. Depuis, zéro.
