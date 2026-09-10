---
type: session
mode: brain
date: 2026-09-10
tags: [meta, build-mode, a-reprendre]
---

# Conversation 55 — DevBrain, les plateformes de données et d'IA — À REPRENDRE

Interrompue par floSa le 2026-09-10 (économie de crédits) **avant toute écriture dans une
page du vault**. Seul ce fichier a été créé. Aucun commit.

## Où l'on travaille

- Worktree `.claude/worktrees/brainkit-lot-7-skills-8723f2`, branche `claude/devbrain-data-ai-1b96f2`,
  HEAD = `8274072` = `origin/main`. Divergence vérifiée : `HEAD..origin/main` vide, merge-base OK.
- Identité locale vérifiée : `floSa` / adresse laposte (perso). `core.hooksPath` = `.githooks`. Rien à changer.
- BrainKit trouvé au voisinage : `../../../../BrainKit` (`outils/fidelite.py --vault <vault>` existe).

## Baselines relevées avant écriture

- `check_brain` : **0 dure, 127 avertissements** — voisinage_declare 62 · couverture_des_vues/a 13 ·
  collision_alias 13 · couverture_des_vues/e 11 · amont_concorde/ancien 10 · etiquettes_fermees/Ressources 5 ·
  anti_repetition 4 · amont_concorde/archive 4 · amont_concorde/contredit 2 · vocabulaire_ferme/axe_vide 1 ·
  couverture_des_vues/d 1 · couverture_des_vues/b 1.
- `check_arbo` : OK partout. `[V1] verif_pitch` : 0 ligne à traiter dans tout le vault.
- Scripts du skill extraits dans le scratchpad (`ou.py`, `verif_pitch.py`) — à ré-extraire depuis
  `enrichir-brain/SKILL.md` si le scratchpad a disparu.

## Ce qui est établi (à ne pas re-dériver)

- `ml/plateforme` **n'existe pas** : `ou.py "ml/plateforme"` rend « Machine Learning » (préfixe connu, valeur
  inconnue → il faut la déclarer). À poser dans **deux** endroits : `taxonomie.md` (bloc ```domaine ligne
  `ml/{…}` + arbre de décision + frontières) **et** `brain.yml` → `axes.rangement.prefixes[cle: ml].sous.plateforme`
  avec `libelle:`, `motif:`, `frontiere:`. Sans `libelle:`, `promotions()` lève KeyError au franchissement du seuil.
- Promotion : 8 pages en `ml/plateforme` > seuil 5 ; le plafond (« aucune page au niveau du domaine ») ne joue
  pas — « Machine Learning/ » garde ~17 pages à son niveau (ZenML, Metaflow, Flyte, Optuna…). Donc le
  sous-dossier **naît** : `Machine Learning/<Libellé>/` + hub `<Libellé>.md` (`role: hub`). Libellé à choisir
  unique dans le vault à la casse près (proposition : « Plateformes ML » — vérifier `find . -iname`).
- Rayon P1→P6 pour les huit : P1 = hub du nouveau sous-dossier (à créer, corps à la main) ; P2 = `Machine
  Learning/Machine Learning.md` (zone AUTO bouge : nouveau sous-hub ; corps `## Choisir` à compléter d'une
  ligne) ; P3 = comparatif neuf `Comparatif - Plateformes ML.md` + `.base` (filtre `role == "brique"` et
  `categorie == "ml/plateforme"`), plus `Comparatifs/Comparatifs.md` (AUTO) et le `## Voir aussi` → `[[Comparatifs]]` ;
  P4 = notion du dossier à **créer** (aucune notion existante ne couvre « plateforme ML de bout en bout ») ;
  P5 = les huit entre elles (alternatives réciproques) ; P6 = pitchs réinjectés.
- Hors rayon mais exigé par floSa : Snowflake ↔ ClickHouse et DuckDB en `alternatives:` des deux côtés, puce
  dans `## Alternatives` de chaque (pitch réinjecté), et une puce Snowflake dans « Ce qui départage » de
  `Bases de données/Comparatif - Bases colonnes.md` (préfixée `voisin :` côté ClickHouse/DuckDB inutile : ils
  seront en `alternatives:`). Snowflake **n'entrera pas** dans le `.base` « Bases colonnes » (filtre
  `database/analytique`) — à dire dans les remontées, pas à contourner.
- Faits vérifiés sur le web (2026-09-10) :
  - Dataiku : s'installe sur Linux / Kubernetes on-prem (doc.dataiku.com/dss/latest/installation) → `hosted: [self, managed]`.
  - DataRobot : « Self-Managed AI Platform » sur Kubernetes via Helm, HA/DR documentés (docs.datarobot.com/en/docs/install) → `[self, managed]`.
  - Alteryx : Designer = application desktop ; Server on-prem/VM/cloud ; Analytics Cloud managé (help.alteryx.com) → `[self, managed]`, famille probable `application` (F7, point d'entrée GUI).
  - Databricks : uniquement AWS/Azure/GCP, compute plane dans le compte client, pas d'on-prem → `saas` (F5), `[managed]`.
  - Snowflake : pas d'on-prem, ne le sera pas → `saas`, `[managed]` (docs.snowflake.com).
  - Azure ML : contrôle dans Azure ; **Arc-enabled Kubernetes** permet entraînement/inférence on-prem (learn.microsoft.com/azure/machine-learning/how-to-attach-kubernetes-anywhere) → `saas` (compte Azure obligatoire), `[managed]`, mais l'Arc va en « Prendre si ».
  - SageMaker : « SageMaker Unified Studio » (GA 2025) est le nom courant ; hybride = ingestion depuis on-prem, pas d'exécution on-prem → `saas`, `[managed]`.
  - Vertex AI : en cours de rebaptême « Gemini Enterprise Agent Platform » (Next '26) ; APIs pré-entraînées sur Google Distributed Cloud air-gapped (appliance 1 GPU) → `saas`, `[managed]` ; le GDC en « Prendre si » avec sa limite.
  - Tous propriétaires ; aucun `url_repo` (sonde → « sans amont atteignable », attendu).
- Familles : Dataiku et DataRobot → F5 non (self possible), F6 : consommateur nominal humain (web UI) → **`application`** par R3 ; à confirmer ; `scaling:` pour Alteryx Designer (mono-poste) contre Server : à trancher ou remonter.
- Tags existants utilisables : `ml-pipeline`, `experiment-tracking`, `model-registry`, `model-serving`,
  `feature-store`, `low-code`, `lakehouse`, `columnar`, `olap`, `distributed`, `orchestration`, `data-pipeline`.
  Aucun tag `automl`, `mlops-platform`, `cloud`, `data-warehouse` : ne pas inventer, proposer dans `tags.md` si besoin.
- Remontées déjà identifiées : BigQuery, Redshift, dbt absents (question d'une catégorie d'entrepôt) ;
  Snowflake hors du `.base` « Bases colonnes » ; `Feature store — concept.md` et `Monitoring de modèle en
  production.md` (notions) citent Databricks/Snowflake en clair sans lien — proposer, ne pas réécrire.

## À reprendre — dans cet ordre

1. Poser `ml/plateforme` (taxonomie.md + brain.yml), vérifier `ou.py "ml/plateforme"` → nouveau dossier.
2. Créer dossier + hub, 8 briques, notion, comparatif + `.base`, liens croisés Snowflake.
3. P1→P6 ligne par ligne, `[V1]`, `git status` vs `ls`.
4. `cloturer-brain` sans push ; commande PowerShell d'intégration pour floSa.
