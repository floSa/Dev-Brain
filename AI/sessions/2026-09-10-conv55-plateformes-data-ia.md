---
type: session
mode: brain
date: 2026-09-10
tags: [meta, build-mode, taxonomie, plateformes]
---

# Conversation 55 — DevBrain, les plateformes de données et d'IA

Capture de **huit suites data & IA**, ouverture de la valeur `ml/plateforme`, promotion du
sous-dossier « Plateformes data & IA », comparatif neuf et câblage croisé de Snowflake vers
les moteurs colonnes. Branche `claude/devbrain-data-ai-1b96f2`, worktree
`brainkit-lot-7-skills-8723f2`, base `8274072`. **Non poussée** : l'intégration appartient à floSa.

Session interrompue une fois en cours de route (économie de crédits), reprise sur la note
d'état écrite avant la coupure — ce fichier en est la version finale, déplacée par `git mv`.

## Ce que le lot fait, en une phrase

Le brain sait désormais répondre à « quelle plateforme proposer chez ce client », et il y
répond d'abord par l'hébergement : trois des huit s'installent sur des serveurs qu'on possède,
les cinq autres non.

## 1. La valeur `ml/plateforme` — posée dans les DEUX sources

Une valeur neuve se pose à deux endroits depuis que le vault est une instance de BrainKit, et
une valeur posée dans un seul des deux fait échouer un contrôle.

| Source | Ce qui y a été écrit |
|---|---|
| `Documentation/general/taxonomie.md` | la valeur dans le bloc ` ```domaine `, les règles **D-R8** et **D-R9**, une frontière disputée, et l'entrée longue de *Sous-domaines qui prêtent à confusion* portant l'arbitrage Snowflake |
| `brain.yml` | `axes.rangement.prefixes[ml].sous.plateforme` avec `libelle:`, `motif:` et `frontiere:` ; les deux départages ; la neuvième frontière ; le bloc `mesure:` remis à jour |

**Motif de la valeur** : ces outils couvrent **tout le cycle** — préparation, entraînement,
déploiement, gouvernance — là où `ml/orchestration` (ZenML, Metaflow, Flyte) ne décrit qu'un
pipeline et laisse dehors l'infrastructure, le catalogue et les droits.

**La question fermée qui y mène — D-R9** : après D2, *tout le cycle, ou seulement le pipeline ?*
Elle se vérifie sans jugement, en comptant les quatre étapes que la brique porte elle-même.
ZenML l'écrit lui-même : « il n'exécute rien lui-même ».

**L'arbitrage Snowflake — D-R8** : `database/analytique` existait et a été **écartée, pas
oubliée**. Motif mesuré sur sa population réelle — DuckDB est embarqué, ClickHouse vise le
temps réel, aucun des deux n'est le concurrent rencontré en clientèle, où la question est
« Snowflake ou Databricks ? ». S'y ajoute que Snowpark, Cortex et Snowflake ML exécutent code
et modèles dans le moteur. Un moteur dont le concurrent reste un moteur va toujours en
`database/analytique` : la branche n'a pas bougé, seul Snowflake en sort.

**Trois tags ajoutés** à `Documentation/general/tags.md`, par la procédure documentée
(proposer, ajouter au vocabulaire, puis utiliser) : `automl`, `data-governance`, `ml-platform`.

## 2. La règle de promotion — vérifiée, pas supposée

Mesurée par la dérivation officielle (`arbo.promotions` sur la population réelle) :

- population pesant sur le seuil en `ml/plateforme` : **9** (8 briques + 1 notion ; le
  comparatif ne pèse pas, `ROLES_HORS_SEUIL`), pour un seuil de **5** ;
- **plafond non atteint** : « Machine Learning » garde **17 pages** à son niveau ;
- promotions du vault : **45 → 46**, aucune promotion perdue ;
- dossier dérivé : `Machine Learning/Plateformes data & IA`.

Libellé « Plateformes data & IA » et non « Plateformes » seul : ce dernier se lirait comme
l'axe `famille:`, dont la valeur `plateforme` qualifie des dizaines de briques qui ne sont pas
ici.

## 3. Les dix pages créées

Toutes dans `Machine Learning/Plateformes data & IA/`, chemin **dérivé**, jamais choisi.

| Page | `role:` | `famille:` | `hosted:` |
|---|---|---|---|
| Dataiku | brique | `plateforme` | `[self, managed]` |
| DataRobot | brique | `plateforme` | `[self, managed]` |
| Alteryx | brique | `application` | `[self, managed]` |
| Databricks | brique | `saas` | `[managed]` |
| Snowflake | brique | `saas` | `[managed]` |
| AWS SageMaker | brique | `saas` | `[managed]` |
| Google Cloud Vertex AI | brique | `saas` | `[managed]` |
| Microsoft Azure Machine Learning | brique | `saas` | `[managed]` |
| Plateformes data & IA | hub | — | — |
| Plateforme data & IA — concept | notion | — | — |
| Comparatif - Plateformes data & IA (+ `.base`) | comparatif | — | — |

`famille:` dérivée par l'arbre F1→F9, sans intuition : F5 (auto-hébergement impossible)
tranche les cinq `saas` ; Alteryx tombe en `application` par R3, le point d'entrée documenté
en premier étant Designer, application de poste Windows — d'où son `os: "Windows"`.

## 4. Le rayon de propagation

### Détail pour une capture — Snowflake

```
P1 hub du dossier   : Machine Learning/Plateformes data & IA/Plateformes data & IA.md
                      → CRÉÉ (corps à la main, zone AUTO générée)
P2 hubs parents     : Machine Learning/Machine Learning.md
                      → FAIT : zone AUTO (nouveau sous-hub) + corps, deux lignes ajoutées
                        (« Ce qu'il faut comprendre » et « Choisir »)
P3 comparatif       : Comparatif - Plateformes data & IA.md + son .base → CRÉÉS
                      consommateur supplémentaire d'un comparatif créé :
                      Comparatifs/Comparatifs.md → zone AUTO générée, lien retour écrit
                      Bases de données/Comparatif - Bases colonnes.md → puce ajoutée
P4 notion           : Plateforme data & IA — concept.md → CRÉÉE, citée dans les deux sens
P5 briques pairs    : les 7 autres du dossier → alternatives réciproques
                      hors dossier : ClickHouse, DuckDB → alternatives dans les deux sens
                      compléments : Streamlit → réciproque
P6 pitchs réinjectés: 3 puces chez Snowflake, 1 chez ClickHouse, 1 chez DuckDB,
                      1 chez Streamlit — vérifié par [V1], 0 écart
```

### Chiffré pour les huit

| Ligne | Faites | Sans objet |
|---|---|---|
| P1 hub du dossier | 8 | 0 |
| P2 hubs parents | 8 | 0 |
| P3 comparatif | 8 | 0 |
| P4 notion | 8 | 0 |
| P5 briques pairs | 8 | 0 |
| P6 pitchs réinjectés | 8 | 0 |

**48 lignes sur 48 faites, aucune sans objet** — les huit atterrissent dans le même dossier
neuf, qui porte hub, comparatif, notion et pairs.

Six pages existantes touchées, toutes par réciprocité : `ClickHouse`, `DuckDB`,
`Comparatif - Bases colonnes`, `Spark`, `MLflow`, `Streamlit`. **Aucune notion existante
modifiée.**

## 5. Contrôles

| Contrôle | Verdict |
|---|---|
| `check_brain.py` | **0 violation dure, 127 avertissements** — le compte exact du départ |
| `check_arbo.py` | chemin et catégorie concordent partout |
| `build_bandeau.py --check` | les 345 artefacts concordent |
| `[V1]` réinjection des pitchs | 0 ligne à traiter dans tout le vault |
| `outils/fidelite.py --vault .` | **code 0, 0 divergence inexpliquée** |

**Le compte d'avertissements a bougé puis est revenu.** Trois avertissements sont apparus, tous
sur du texte que je venais d'écrire, et tous corrigés à la source plutôt que tolérés :

- `collision_alias [R5]` ×1 — `AWS SageMaker` portait `SageMaker` et `sagemaker`, doublon
  interne à la casse près. Le doublon minuscule retiré, la résolution étant insensible à la casse.
- `anti_repetition [R26]` ×2 — les `## Définition` de Dataiku et DataRobot redisaient
  `licence_type: proprietary`, déjà au bandeau. Les deux phrases réécrites pour dire ce que le
  bandeau ne dit pas (le mode de facturation), pas pour faire baisser un compteur.

Aucun avertissement nouveau n'a été laissé : 127 avant, 127 après.

**Le manifeste a demandé 26 recalages.** Les compteurs `population:` et `mesure:` de
`brain.yml` sont des mesures datées ; +8 briques, +1 notion, +1 comparatif et +1 hub les
périment tous d'un coup. `fidelite.py` les a sortis en INEXPLIQUEE — l'écart est détecté, la
correction est manuelle. Recalés après vérification de chaque ancienne valeur.

## 6. Fraîcheur

`sonder_amont.py --limit 12` a enregistré les huit en **`sans_amont`**, et leur bandeau affiche
« aucun amont fiché ». C'est le comportement attendu : aucun de ces huit produits n'a de dépôt
public, et **aucune `url_repo` n'a été inventée**. Seule une `url_docs` officielle est portée.
Le hub le dit en clair : l'absence d'amont est ici une propriété du produit, pas un défaut de
la fiche.

## 7. Ce que le comparatif tranche

> On tranche sur **où tournent les données**, et **ce qu'on réécrit le jour où l'on part** —
> dans cet ordre.

- **Sur site, en entier** : Dataiku, DataRobot, Alteryx. Plan de contrôle compris, aucun accès
  fournisseur.
- **« Sur site » des trois clouds, trois sens différents** : Azure ML fait tourner le calcul sur
  un Kubernetes **du client** par Arc ; SageMaker descend par Outposts, des baies **louées à
  AWS** ; Vertex AI n'en descend qu'**une partie**, sur appliance air-gapped. Dans les trois cas
  le plan de contrôle reste chez le fournisseur.
- **Enfermement** : il se mesure au devis de sortie, pas à l'entrée — format de stockage,
  portabilité de la logique métier, catalogue de droits. Le plus profond est Snowflake dès
  qu'on écrit du Cortex en SQL ; le plus faible des managées est Databricks, format de table
  ouvert et moteur connu ; le plus élevé en proportion est Alteryx, dont un flux visuel ne
  s'exporte pas, il se réécrit.

## Remontées

1. **`CLAUDE-build.md` est en retard sur l'outillage.** Il prescrit
   `uv run AI/scripts/build_bandeau.py "<chemin>"` ; depuis le pont BrainKit, le générateur
   **refuse tout argument de fichier** (`unrecognized arguments`). Seule la passe complète existe.
2. **Les compteurs du manifeste n'ont pas de gardien.** 26 valeurs `mesure:`/`population:` à
   recaler à la main pour 10 pages ajoutées. `fidelite.py` les détecte, rien ne les met à jour.
   Un `--fix` du kit, ou un compteur dérivé plutôt que déclaré, éviterait que la prochaine
   capture sorte en INEXPLIQUEE.
3. **`domaines:` et `os:` sont déclarés `deprecies` sur `role: brique` dans `brain.yml`**, alors
   que `CLAUDE-build.md` les prescrit et que les **six hubs de `Métiers/` sont générés depuis
   `domaines:`**. Les huit briques le portent, donc, et rejoignent un écart connu de 38 pages.
   Contradiction à trancher : soit le champ n'est pas déprécié, soit `Métiers/` change de source.
4. **`taxonomie.md` annonçait 101 valeurs quand son bloc en portait 103.** Corrigé à 104 en
   passant, la valeur ajoutée rendant l'écart trop visible pour être laissé.
5. **BigQuery, Redshift et dbt sont absents du vault.** Leur arrivée reposera la question d'une
   catégorie d'entrepôt, distincte de `ml/plateforme`. Le déplacement coûterait alors **une
   commande `git mv`** : les wikilinks sont nus, rien à réécrire.
6. **Snowflake n'entre pas dans la vue `.base` de « Bases colonnes »**, filtrée sur
   `categorie: database/analytique`. Assumé et écrit dans la puce : coder un nom en dur dans le
   filtre serait la régression que `[WARN] R8d` signale.
7. **`langage:` laissé vide sur les huit.** Produits propriétaires dont le langage
   d'implémentation n'est pas documenté de façon citable. Le bandeau affiche donc « Plateforme »
   ou « SaaS » sans langage — le comportement prévu, plutôt qu'une valeur plausible.
8. **`scaling:` laissé absent sur Alteryx.** Designer est mono-poste, Server répartit sur des
   workers : aucune valeur unique n'est vraie pour la page. Le champ est conditionnel, son
   absence est légale, et `fidelite.py` la range en « légal, `si:` permet et n'exige pas ».
9. **Compléments candidats non câblés, par bornage volontaire du rayon** : Featuretools ↔ Alteryx
   (Alteryx maintient Featuretools) et Apache Iceberg ↔ Databricks (concurrent de Delta Lake).
   Nommés en clair dans les corps de page, pas en frontmatter.
10. **Vertex AI change de nom.** Le produit est en cours de rebaptême en « Gemini Enterprise
    Agent Platform » (Google Cloud Next '26). La fiche le dit et l'alias est posé ; à revérifier
    dans six mois, le nom de la page pouvant devoir suivre.
11. **Deux notions existantes mériteraient un lien plutôt qu'une mention en clair** :
    `Feature store — concept` cite « Databricks Feature Store » et Snowflake en prose,
    `Monitoring de modèle en production` cite des concurrents managés. Ce sont des `role: notion`
    — **proposées, non modifiées**.

## À reprendre

1. Trancher la remontée 3 (`domaines:` / `os:` dépréciés contre `Métiers/` généré).
2. Décider si les deux notions de la remontée 11 reçoivent les liens proposés.
3. La remontée 5 le jour où un entrepôt entre dans le vault.
