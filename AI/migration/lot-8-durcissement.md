---
galaxie: meta
nom: lot-8-durcissement
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 8 — Durcissement du validateur

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
