---
role: meta
nom: remontees-ml-rl-nlp-domaine
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 du découpage — remontées « Machine Learning : RL, NLP, niveau domaine »

Périmètre : `Machine Learning/Apprentissage par renforcement/` (6 briques),
`Machine Learning/NLP/` (6) et les fiches posées directement dans `Machine Learning/` (12).
**24 fiches, exactement le compte annoncé par la table du découpage.**
Branche `claude/machine-learning-batch-6-6ba45a`.

Aucun autre fichier du vault n'a été modifié : `git status` liste 24 fiches converties, plus
ce fichier de remontées. Ni hub, ni notion, ni comparatif, ni `.base`, ni script, ni document
partagé. `build_bandeau.py` a été **lancé et jamais édité**, borné aux 24 fiches — le scope
`Machine Learning` seul aurait récursé dans les dossiers des seize autres conversations.

État des validateurs sur la branche : `check_brain.py` **OK, 0 violation dure**, 149 → **144**
avertissements ; `check_arbo.py` **OK** ; `build_bandeau.py --check` concordant sur les 24.
La baisse de 5 est intégralement expliquée au §8 — ce n'est pas le compte de `main`, qui
ignore le travail des seize autres branches.

---

## 1. Les trois règles du 2026-09-06 sont arrivées en cours de conversion

Le commit `98f4112` est arrivé alors que les 24 fiches étaient converties. Les trois règles
ont tout de même été **appliquées**, pas seulement signalées — le détail par règle ci-dessous.
La lecture s'est faite par `git show origin/main:AI/migration/lot-6-gabarit.md`, sans rebase
ni merge, la règle 6 du protocole parallèle les interdisant.

> Point de méthode pour l'intégration : une règle publiée pendant que dix-sept conversations
> tournent n'atteint que celles qui relisent le brief. Rien dans le protocole ne demande de
> re-fetcher en cours de route. Si d'autres règles doivent tomber, elles arriveront de la même
> façon — c'est-à-dire au hasard de l'avancement de chacune.

## 2. Règle 1 (wikilink nu en cellule) — le piège a été rencontré avant d'être publié

Trois occurrences écrites puis corrigées **avant** l'arrivée du commit, par vérification de la
vraie expression régulière (`LINK_RE`, `check_brain.py:150`) :

| Fiche | Écrit d'abord | Corrigé en |
|---|---|---|
| `NLTK` | un lien à alias vers `Classification de texte` | `classification naïve Bayes ([[Classification de texte]])` |
| `NLTK` | un lien à alias vers `Tokenization` | `tokenisation ([[Tokenization]])` |
| `OpenSpiel` | un lien à alias vers `AlphaZero and self-play` | `approches type AlphaZero ([[AlphaZero and self-play]])` |

Le mécanisme confirme la mesure du lot 4 : le groupe 1 de `LINK_RE` accepte l'antislash, donc
un lien à alias échappé donne une cible terminée par `\` — un lien mort, en **violation dure**.
Sans échappement, le pipe coupe la ligne du tableau. Vérification finale : **0 wikilink à
alias et 0 pipe échappé** dans une ligne de tableau, sur les 24 fiches.

> Formulation qui aurait aidé plus tôt : le piège ne se voit pas à la relecture, parce que la
> forme échappée **s'affiche correctement dans Obsidian**. Seul `check_brain` la voit.

## 3. Règle 2 (routage des puces « besoin → concurrent ») — appliquée, mesure à l'appui

`AI/scripts/mesure_membres_bases.py`, que la règle cite, **n'existe pas dans le dépôt** : le
commit `98f4112` ne touche que `lot-6-gabarit.md`. L'appartenance a donc été mesurée
directement sur les quatre `.base` du périmètre. **À créer, ou à retirer de la règle.**

Appartenance mesurée, et non supposée :

| Vue `.base` | Filtre | Fiches du périmètre membres |
|---|---|---|
| `Comparatif - Reinforcement learning` | `role == brique` ET `categorie == ml/rl` | les 6 du dossier RL |
| `Comparatif - NLP` | `role == brique` ET tag parmi 5 | les 6 du dossier NLP, **plus** `HuggingFace`, `datasets`, `sentence-transformers` (tag `nlp`) |
| `Comparatif - Optimisation d'hyperparamètres` | `categorie == ml/hyperopt` | `Optuna`, `Hyperopt`, `Ray Tune` |
| `Comparatif - Orchestrateurs ML` | `categorie == ml/orchestration` | `Flyte`, `Metaflow`, `ZenML` |

**Trois fiches ne sont membres d'AUCUNE des 47 vues du vault** : `Evidently`
(`ml/monitoring`), `Feast` (`ml/feature-store`), `PyTorch Geometric` (`ml/graphe`). Leurs
puces « besoin → concurrent » **restent en `Écarter si` avec leur wikilink** — les écarter les
supprimerait. C'est exactement le cas prévu par le second tiret de la règle, et il concerne
**3 fiches sur 24**, soit 12,5 % : le cas n'est pas marginal.

Pour les 21 fiches membres, **17 cellules** ont été routées vers le comparatif. Le tri n'a pas
été « toute cellule à wikilink », mais un test à trois conditions, toutes vérifiées :

1. la cellule est une redirection **pure** — elle n'énonce aucune borne de la brique elle-même ;
2. la cible est **membre de la même vue** ;
3. le discriminant figure déjà dans la section « Ce qui départage » du comparatif.

Ce qui est resté : les cellules de la forme **borne + alternative**, celle que la remontée 20
du lot 5 réclame (« la cellule énonce la limite *et* nomme l'alternative »). Exemples tenus :
« Reverb et Launchpad ne tournent que sous Linux » (Acme), « le vocabulaire est figé à
l'entraînement » (sentencepiece), « `hp.choice` renvoie un index et non la valeur » (Hyperopt),
« sans storage persistant, une étude en mémoire est perdue » (Optuna).

> **Troisième cas non prévu par la règle, et rencontré 9 fois** : une redirection pure dont la
> cible est **hors de toute vue**. `datasets → [[Polars]]`, `HuggingFace → [[XGBoost]]`,
> `Flyte → [[Dagster]]`, `ZenML → [[Airflow]]`, `SetFit → [[Scikit-Learn]]`,
> `spaCy → [[Scikit-Learn]]`… La règle 2 ne dit rien de ce cas : la brique est membre d'une
> vue, mais **le comparatif de cette vue ne porte pas la cible**, donc la puce n'y a aucune
> destination. Elles ont été **conservées**, par application de « aucune puce supprimée sans
> destination ». À trancher pour l'intégration : c'est le troisième tiret qui manque à la règle.

Cas limite conservé sciemment : `sentence-transformers → [[rank-bm25]] ou [[Elasticsearch]]`.
`rank-bm25` est membre de `Comparatif - NLP`, `Elasticsearch` non — retirer la cellule aurait
perdu la moitié Elasticsearch.

## 4. Règle 3 (`complements:`) — 7 couples envisagés, 5 tenus, 2 défaits

Le filtre « appariement énoncé comme une recommandation, pas simple intégration » change le
résultat : deux couples déjà écrits ont été **défaits**.

| Couple | Verdict | Ce que la fiche source dit |
|---|---|---|
| `Gymnasium` ↔ `Stable-Baselines3` | **tenu** | « l'API d'environnements sur laquelle SB3 entraîne ses agents » — appariement structurel, énoncé des deux côtés |
| `SetFit` ↔ `sentence-transformers` | **tenu** | « le socle qu'il fine-tune » — SetFit n'existe pas sans lui |
| `HuggingFace` ↔ `datasets` | **tenu** | « bibliothèques sœurs » de la même stack |
| `HuggingFace` ↔ `spaCy` | **tenu** | « complément plus que substitut » — la fiche emploie le mot |
| `HuggingFace` ↔ `sentence-transformers` | **tenu** | bibliothèque sœur : son `url_repo` est sous l'organisation `huggingface` |
| `Gymnasium` ↔ `TF-Agents` | **défait** | « environnements utilisables via les suites/wrappers » — intégration, pas recommandation |
| `sentencepiece` ↔ `HuggingFace` | **défait** | `AutoTokenizer` **remplace** l'appel direct : c'est l'`Écarter si` de la fiche, pas un complément |

Les deux relations défaites n'ont pas disparu : elles sont descendues en `## Voir aussi`.

**Moitié de couple posée, cible hors périmètre** — une seule qualifie :

| Fiche | Complément | Dossier de la cible | Lot qui le portera |
|---|---|---|---|
| `Evidently` | `[[MLflow]]` | Machine Learning/Suivi d'expériences/ | lot 5 du découpage |

La fiche Evidently écrit « complémentaire d'Evidently » en toutes lettres — c'est un
appariement énoncé, pas une énumération. La moitié est posée de mon côté, conformément à la
règle 3 ; **c'est à l'intégration de fermer l'autre**. Aucun risque de validateur : la
réciprocité de `complements:` n'est **contrôlée nulle part** dans `check_brain.py` — seul R2
vérifie que le lien n'est pas mort. À noter pour la règle dure nº 1 du lot 8, qui l'annonce.

Écartés **par** la règle 3, et c'est le cœur de son utilité — chacun aurait ouvert un couple
sous l'ancienne lecture : `ZenML → MLflow, BentoML, KServe` (« orchestre des outils
existants » — l'énumération même que la règle condamne), `Metaflow → MLflow` (« s'intègre
avec »), `Feast → Redis, Postgres` (énumération parmi DynamoDB, BigQuery, Snowflake),
`Hyperopt → Spark`, `pytorch-crf → PyTorch`, `PyTorch Geometric → PyTorch`. Soit **une
dizaine de couples évités sur 24 fiches** : le champ serait devenu du bruit, exactement comme
la règle le prédit.

Cas à arbitrer : `Ray Tune → [[Ray]]`. La fiche écrit « indissociable de Ray ». Ce n'est ni une
intégration ni une recommandation — c'est une **dépendance de famille**, Ray Tune étant un
module de Ray. Laissé fermé, faute de catégorie dans la règle.

## 5. Le tableau ne s'équilibre pas, et il penche du côté droit

Mesure sur les 24 fiches : **116 lignes**, dont **89 cellules `Prendre si` remplies** et
**106 `Écarter si` remplies** — donc 27 cellules `Prendre si` vides et **10 `Écarter si`
vides**.

C'est l'inverse du pilote, qui comptait 17 `Écarter si` vides sur 13 fiches. La dissolution de
`Pièges` explique l'écart : ces fiches portaient des sections `Pièges` denses et
majoritairement faites de bornes dures — couplage de versions TF/tf-agents/Reverb, installation
des extensions creuses de PyG, symbole `▁` de sentencepiece, vecteur `batch` du mini-batching
de graphes — toutes décisionnelles, toutes parties à droite.

Aucune cellule n'a été comblée.

## 6. 65 cellules `Écarter si` sur 106 ne portent pas de wikilink

Le critère d'acceptation du brief (« chaque cellule `Écarter si` contient un wikilink ») n'est
donc **pas atteint, et ne peut pas l'être sans inventer**. 41 cellules sur 106 en portent un.

Les 65 restantes sont des bornes dures sans substitut nommable : « CFR tabulaire explose avec
la taille du jeu » (OpenSpiel), « le cache n'est jamais purgé seul » (datasets),
« over-smoothing » (PyTorch Geometric), « une référence non représentative déclenche de
fausses alertes » (Evidently). Nommer une alternative à chacune reviendrait à fabriquer une
redirection — précisément ce que la règle 2 vient d'interdire.

> Les deux règles se contredisent frontalement sur ce point : la règle 2 pousse les
> redirections **hors** de `Écarter si`, le critère d'acceptation en exige une **dans chaque
> cellule**. Le brief porte les deux. **À trancher au lot 8**, où la règle dure nº 5 est déjà
> notée comme à relire.

## 7. Aucune section `## Retours` créée

Conforme : aucune des 24 fiches ne portait d'entrée datée dans `Pièges`. La seule du vault
reste `LLM & IA générative/Agents de code/t3code.md`, du ressort du lot 7 du découpage.

## 8. Cinq avertissements R15 résorbés — et ce qu'ils révèlent

`datasets`, `Flyte`, `HuggingFace`, `Metaflow`, `ZenML` ne portaient **aucun lien vers une
notion ou un hub**. Résolu en ajoutant `- [[Machine Learning]] — le hub du domaine` à leur
`## Voir aussi`, sur le modèle du pilote (`[[Bases de données]] — le hub du domaine` sur
DBeaver).

Le fait intéressant est **où** ces cinq vivent : toutes les cinq sont au **niveau domaine** de
`Machine Learning/`, aucune dans un sous-dossier. Les sous-dossiers ont leur notion chapeau
sous la main — `Reinforcement learning`, `Traitement du langage naturel` — et les fiches y
pointent naturellement. Le niveau domaine n'a pas d'équivalent : trois des cinq
(`Flyte`, `Metaflow`, `ZenML`) portent `ml/orchestration`, une **catégorie sans notion**. Le
seul rattachement disponible est le hub.

> À vérifier sur les lots 1, 10 et 13, qui portent les trois autres niveaux domaine : si le
> même trou s'y retrouve, R15 ne mesure pas un oubli de câblage mais **l'absence de notion
> chapeau pour certaines catégories**. Candidates repérées ici : `ml/orchestration`,
> `ml/hub`, `ml/graphe`.

## 9. `Evidently` : `famille: paquet` ne peut pas dire son hébergement hybride

Sa fiche décrit un modèle **hybride** — bibliothèque d'évaluation, plus un service de
monitoring self-hostable, plus Evidently Cloud managé et payant. Mais `famille: paquet`
interdit `hosted:` (R16), et `build_bandeau.py` affiche donc « en bibliothèque, rien à
héberger » : **exact pour la bibliothèque, faux pour le produit**.

Ce n'est pas une faute de conversion, et ce n'est pas non plus un bug du script — le bandeau
dit fidèlement ce que le frontmatter porte. C'est `famille:` qui ne sait pas exprimer « paquet
avec un service optionnel ». L'information est en `Mise en œuvre → Coût`, seule place possible.
Arbitrage éditorial de floSa, pas déduction de conversion.

## 10. `GLiNER` : `url_docs` et `url_repo` sont la même URL

Les deux pointent le dépôt GitHub. La section `## Ressources` ne porte donc qu'une puce,
`Dépôt`. Écrire `Documentation` avec la même URL aurait dupliqué la ligne sans rien apprendre,
et fabriquer une ancre `#readme` aurait été une invention. Le vocabulaire fermé n'impose pas la
présence de `Documentation` — la fiche est conforme, mais **elle n'a pas de doc distincte de
son dépôt**, ce qui est le vrai fait.

Confirme la réserve connue du brief : ce lot n'a produit **aucune** puce `Tutoriel`, `Article`,
`Papier`, `Cours` ni `Vidéo`. Toutes les puces `Ressources` des 24 fiches valent
`Documentation` ou `Dépôt`.

## 11. Recouvrement fiche / comparatif — 6 faits, contre 3 pour le pilote

Même phénomène qu'au §7 du pilote : un fait est à la fois le discriminant du comparatif et la
borne dure de la brique.

| Fait | Fiche, `Écarter si` | Comparatif |
|---|---|---|
| aucun algorithme fourni | Gymnasium | « ne fournit **aucun algorithme** » |
| tout reste à écrire | RLax | « ni agents, ni environnements, ni replay, ni boucle » |
| figé sur TF 2.15, couplage strict | TF-Agents | « figé sur TF 2.15, avec un couplage de versions strict » |
| NER borné aux types appris | spaCy | « son NER est borné aux **types appris** » |
| pas de pruning intra-essai | Hyperopt | « pas de pruning intra-essai » |
| un cross-encoder ne se pré-calcule pas | sentence-transformers | « un cross-encoder ne se pré-calcule pas » |

Six sur 24 fiches, contre trois sur 18 au pilote — la proportion double. La question posée par
le pilote (« recouvrement toléré, ou fiche muette sur son propre discriminant ») reste ouverte,
et elle devient plus coûteuse à mesure que les lots avancent : c'est **six paires de plus à
tenir d'accord**. Position tenue ici, faute d'arbitrage : recouvrement **toléré**, parce
qu'une fiche muette sur sa propre borne dure oblige à ouvrir le comparatif pour savoir ce qui
mord.
