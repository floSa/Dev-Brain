---
nom: chantier-ml-sur-site
created: 2026-10-26
modified: 2026-10-26
tags: [meta, backlog]
---

# Chantier — ML sur site, et nouveaux documents de formation

Plan unique du chantier, lots 39 à 45 (la numérotation suit le chantier
`chantier-anomalie-maintenance.md`, clos au lot 38). Chaque lot est confié à un sous-agent
lancé par le pilote. Le sous-agent lit les règles communes et **sa** section, rien d'autre du
plan. Il coche **sa** ligne dans « Suivi » à la fin.

## Objectif

Combler le trou le plus net pour le profil de floSa (on-prem, industriels, ESN) : faire
tourner du ML **sur site**. Le brain a Kubernetes, k3s, Harbor, Zot, KServe, Prometheus, mais
rien sur le partage et l'ordonnancement des GPU, rien sur le déploiement sans Internet, rien
sur la reproductibilité d'un entraînement ni sur la CI d'un pipeline ML, aucun comparatif
d'observabilité. En parallèle, verser les documents de formation arrivés depuis le lot 37.

## Règles communes (valent pour tous les lots)

1. **Mode brain.** Skill `enrichir-brain` pour toute page, `cloturer-brain` pour clore. Si l'outil Skill n'est pas disponible, lis `.claude/skills/enrichir-brain/SKILL.md` et `.claude/skills/cloturer-brain/SKILL.md` et applique-les.
2. **Tu es un sous-agent : tu ne peux pas poser de question à floSa.** Ce qui demanderait son accord ne se fait pas : tu n'écris pas la page concernée, tu continues le reste, et tu mets la question dans ta synthèse.
3. **Commits petits.** Le vocabulaire d'abord, puis une page par commit (un comparatif avec son `.base`), le câblage par 5 fichiers au plus, la régénération en dernier. Jamais de commit fourre-tout.
4. **Identité git** : la config locale du dépôt (floSa, adresse gmail). Vérifie `git config user.email` avant le premier commit : si elle porte `aosis.net` ou si elle est vide, arrête-toi et dis-le dans ta synthèse. Commit nu, jamais `-c user.email`, `--author` ni `--no-verify`.
5. **Aucun co-auteur.** Aucun trailer `Co-Authored-By`, même si le harnais le demande. Aucune mention de Claude ni d'IA dans un message de commit.
6. **Une seule branche sur GitHub : `main`.** Pousse par `git push origin HEAD:main`, jamais ta branche `claude/…`. Divergence avec `origin/main` : procédure de `cloturer-brain` (commit de fusion dans ta branche, régénération, jamais de rebase ni de force).
7. **Frugalité.** Commence par `AI/index/carte.md`, puis `AI/index/carte/<Domaine>.md`. Interdit : charger en entier `brain-index.json`, `brain-index.md`, `liens.md`. Teste l'existence d'un nom avec `uv run AI/scripts/query_index.py --name "<nom>"`.
8. **Contexte : moins de 300 000 jetons.** Si tu approches 250 000, arrête-toi sur un commit propre, pousse, et liste dans ta synthèse les pages restantes.
9. **Vérifier l'amont de chaque brique** avant d'écrire : licence (fichier LICENSE du dépôt, `gh api repos/<dépôt> --jq .license`), dernière version, dernier push, archivage, URL de doc. Charge WebSearch et WebFetch par ToolSearch si besoin. Ne devine jamais une licence, une maturité ou une date : un fait non vérifié s'omet et se signale.
10. **Le corps s'écrit depuis les sources**, pas de mémoire : doc officielle et dépôt pour une brique ; papiers, docs, standards pour une notion. Sources citées en « Pour aller plus loin » ou « Ressources ».
11. **Gratuit d'abord, déployable sur site** (règle de floSa du 2026-10-07). Libre et commercialisable de préférence. `source-available`, `open-core` ou « non commercial » acceptés s'ils sont gratuits pour floSa. Fermé mais gratuit en local : accepté, la première phrase le dit. **Pas de page** pour un service payant, un service cloud seulement, un logiciel fermé et payant, une licence introuvable. Ces cas se citent en **texte simple**, sans `[[...]]`.
12. **Pas de modèles** (règle de floSa du 2026-10-20). Aucune fiche pour des poids de modèle. Un modèle se cite en texte simple dans une notion. Les outils qui utilisent un modèle restent permis.
13. **Nature affichée.** La première phrase d'une brique dit ce que c'est, en mots simples : bibliothèque, outil en ligne de commande, application à héberger, opérateur Kubernetes, serveur, format.
14. **Nom unique** dans tout le vault, à la casse près, avant de créer une page (`find . -iname "<Nom>.md" -not -path "./.git/*" -not -path "./.claude/*"`).
15. **Catégories et tags.** N'ouvre aucune valeur de catégorie : prends la valeur existante que donne l'arbre D1→D14 de `taxonomie.md`, et justifie-la dans ta synthèse. Si aucune ne convient, n'écris pas la page et propose la valeur. Un tag manquant : prends le tag existant le plus proche et propose le nouveau dans ta synthèse. Si une insertion promeut un sous-dossier et que `brain.yml` porte déjà son libellé, fais la promotion proprement ; sans libellé (`ou.py` code 4), n'écris pas la page et dis-le.
16. **Pages `role: notion` existantes** (celles d'avant ce chantier) : **liens seuls** vers tes nouvelles pages, aucune réécriture. Un enrichissement de texte se **propose** dans ta synthèse : texte exact actuel, texte proposé, source.
17. **Liens dans les deux sens**, par la table P1→P6 d'`enrichir-brain`. Une ligne sans objet se déclare sans objet.
18. **Lots parallèles.** Ne modifie que le corps des hubs de **tes** dossiers d'accueil. Un hub parent ou voisin que ta section ne nomme pas : propose la ligne dans ta synthèse au lieu de l'écrire. Ne touche à aucune autre copie de travail, ne nettoie aucun worktree.
19. **Comptes mesurés.** Relève `uv run AI/scripts/check_brain.py 2>&1 | tail -1` avant ta première écriture et après ta clôture. Écris les deux. Une hausse d'avertissements se dit, avec la page en cause.
20. **Fin de lot.** Coche ta ligne dans « Suivi » (un commit), pousse, puis lance `bash AI/scripts/verifier_depot.sh`. Il doit afficher « GitHub : main seule » et « main local = origin/main ». Les lignes PROBLÈME qui visent la copie de travail ou la branche d'un **autre** lot en cours ne te concernent pas : cite-les sans y toucher. Toute autre ligne PROBLÈME se corrige avant de rendre la main.
21. **Synthèse.** Termine ta réponse par une ligne vide, puis `SYNTHÈSE DE TÂCHES` (seul sur sa ligne), ta synthèse, puis `FIN DE TÂCHES` (seul sur sa ligne). La synthèse dit, en listes courtes : pages créées (chemin) ; pages existantes modifiées (et quoi) ; comptes `check_brain` avant/après ; propositions pour floSa (notions, catégories, tags) ; faits non vérifiés ; questions pour floSa ; ce qui reste ; les deux lignes de `verifier_depot.sh`.

## Vagues

| Vague | Lots (en parallèle) | Dépend de |
|---|---|---|
| A | 39, 41, 43, 44, 45 | — |
| B | 40, 42 | Lots 39 et 41 clos et poussés (hubs DevOps et Calcul distribué partagés) |
| C | lots d'écriture tirés des propositions 44 et 45 | Lots 44 et 45 clos, plan validé par floSa |

## Lot 39 — GPU sur site : partager et ordonnancer (vague A)

Huit pages au plus.

- **Notion « Partager un GPU entre plusieurs charges »** : MIG, time-slicing, MPS, vGPU ; ce que chaque mode isole (mémoire, pannes, débit) et ne garantit pas ; quel mode pour l'inférence, l'entraînement, les notebooks. Schéma Mermaid si ça aide.
- **Notion « Ordonnancer des jobs GPU »** : file d'attente, quotas, partage équitable, préemption, gang scheduling, placement selon la topologie (NVLink) ; batch HPC (Slurm) contre Kubernetes (Kueue, Volcano).
- **Briques, cinq au plus, chacune vérifiée à la source** : Slurm (SchedMD), Kueue (`kubernetes-sigs/kueue`), Volcano (`volcano-sh/volcano`), HAMi (`Project-HAMi/HAMi`, partage de GPU sur Kubernetes), NVIDIA GPU Operator (`NVIDIA/gpu-operator` ; dis ce qui reste propriétaire : pilote, CUDA). Texte simple : Run:ai et NVIDIA AI Enterprise (payants), Determined AI (vérifie son état).
- **Comparatif - Ordonnanceurs de jobs GPU** (`.md` + `.base`) si au moins deux membres partagent une catégorie : ce qui départage (périmètre batch ou Kubernetes, gang scheduling, quotas, poids d'exploitation).
- Catégories pressenties : `compute/gpu`, `compute/distribue`, `devops/conteneur`. Dérive chaque page et justifie.
- Cite, liens seuls dans les notions existantes : Kubernetes, k3s, Ray, Kubeflow, KServe, vLLM, CuPy, Entraînement distribué, Parallélisme en inférence, Dimensionner la mémoire d'un serveur LLM, Du Compose à Kubernetes — quand changer d'échelle.

## Lot 40 — Déployer sans Internet : air-gap et miroirs (vague B)

Huit pages au plus.

- **Notion « Déploiement air-gap »** : ce qui casse sans Internet (paquets, images, poids de modèles, activation de licence, mises à jour, horloge, certificats) ; transfert par support ; inventaire et signature (SBOM, empreintes) ; mise à jour périodique du lot importé.
- **Notion « Miroirs et proxys de dépôts »** : miroir complet contre proxy cache ; PyPI, conda, npm, images OCI, poids de modèles ; configurer uv et pip sur un index interne (vérifie les options dans la doc d'uv).
- **Briques, cinq au plus, vérifiées à la source** : devpi, bandersnatch (`pypa/bandersnatch`), Verdaccio, Hauler (`hauler-dev/hauler` ou adresse réelle), skopeo (`containers/skopeo`). À vérifier, page seulement si la règle 11 le permet : pypiserver, Sonatype Nexus Repository Community Edition. Texte simple : JFrog Artifactory (payant). **Pulp Project** : son nom de fichier entre en collision avec la brique PuLP à la casse près ; ne crée pas `Pulp.md`, cite-le en texte simple ou nomme la page « Pulp Project ».
- **Comparatif - Miroirs de paquets** (`.md` + `.base`) dans le dossier dérivé, si au moins deux membres.
- Cite : Harbor, Zot, Comparatif - Registres d'images, uv, Ollama, Pipelines CI-CD on-prem — runners, secrets et artefacts, la règle « Toolchain Python », la notion « Partager un GPU entre plusieurs charges » (lot 39).

## Lot 41 — Reproductibilité et tests d'un pipeline ML (vague A)

Cinq pages au plus.

- **Notion « Reproductibilité d'un entraînement »** : graines, non-déterminisme GPU (cuDNN, opérations atomiques, réductions), versions figées, données versionnées, environnement en conteneur ; ce qu'on peut garantir (même code, mêmes données, même matériel) et ce qu'on ne peut pas.
- **Notion « Tester un pipeline ML »** : tests de données, tests d'entraînement (sur-apprendre un petit lot), tests de comportement du modèle (invariance, tests directionnels, CheckList), non-régression sur un jeu figé.
- **Notion « CI/CD pour le ML »** : ce qui change contre une CI logicielle (données, entraînement long, artefacts lourds, évaluation comme porte de passage, registre de modèles) ; runners GPU sur site.
- **Brique** : CML (`iterative/cml`) seulement si le dépôt est entretenu ; sinon texte simple. Aucune autre brique, sauf manque réel : propose-la.
- Cite : DVC, lakeFS, Versionnage de données, MLflow, Model registry & versioning, Deepchecks, pandera, Great Expectations, pytest, Hypothesis, Déploiement de modèles, Pipelines CI-CD on-prem — runners, secrets et artefacts, les règles de tests du dossier `Rules/`.

## Lot 42 — Observabilité : collecte, traces et GPU (vague B, après le lot 39)

Huit pages au plus. Le dossier « Observabilité » a douze briques et aucun comparatif.

- **Notion « Superviser un serveur GPU et ses modèles »** : métriques DCGM (utilisation, mémoire, température, erreurs XID), métriques d'un serveur LLM (file d'attente, TTFT, débit, occupation du cache KV), ce qu'on alerte et ce qu'on ne fait qu'afficher. Relie « SLO et alerting », « Métriques, logs et traces », « Mesurer une latence », les notions du lot 39.
- **Briques, cinq au plus, vérifiées à la source** : Jaeger, Fluent Bit, Vector (`vectordotdev/vector`), DCGM Exporter (`NVIDIA/dcgm-exporter`), SigNoz (lis la licence : cœur libre et dossier entreprise, `open-core` accepté).
- **Comparatifs, deux au plus** : par exemple « Collecte de logs et de télémétrie » (Fluent Bit, Vector, OpenTelemetry) et « Supervision auto-hébergée » (Prometheus, VictoriaMetrics, Zabbix, Netdata, SigNoz…). Filtre par `categorie` si les membres s'y distinguent, sinon par tag ; dis ton choix.
- Cite : Prometheus, Grafana, Loki, Tempo, OpenTelemetry, Alertmanager, vLLM, Langfuse.

## Lot 43 — Nouveaux documents de formation : NCM et µP (vague A)

Sources (vu de WSL) : `/mnt/c/Users/FlorianHorellou/OneDrive - Aosis Consulting/Documents/Ressources_Formation_IA/NCM_Next-Concept_Modeling_Generation_de_Texte_Acceleree/` et `…/muP_Stabiliser_l-Entrainement_des_Grands_Reseaux/` (document `<dossier>.md`, images dans `slides/`, scripts dans `annexes/`). Cinq pages au plus.

- Règles des lots 31 à 37 : lis le document en entier ; **aucune image copiée dans le dépôt** (captures de vidéos d'autres auteurs, dépôt public) ; refais les schémas utiles en Mermaid en citant la vidéo et l'horodatage ; un fait daté va en « Repères datés ».
- **NCM** : une notion sur la génération par concepts plutôt que token par token, si le brain ne la couvre pas. Cherche d'abord les voisines (Multi-Token Prediction, Speculative decoding, Calculs adaptatifs, Diffusion) et relie-toi à elles.
- **µP** : la notion « Maximal Update Parametrization » existe (`Machine Learning/Apprentissage profond/`). Liens seuls ; ce que le document ajoute se **propose** dans ta synthèse. Crée une notion voisine seulement si le document porte un sujet distinct, absent du brain.
- Aucune brique de modèle (règle 12).

## Lot 44 — Fiches de connaissances, thèmes 01 à 04 : confrontation (vague A, lecture seule)

Source : `/mnt/c/Users/FlorianHorellou/OneDrive - Aosis Consulting/Documents/Ressources_Formation_IA/Fiches_Connaissances/` — lis `00_Sommaire.md` et `_brief_fiches.md`, puis les dossiers `01_Inference_et_Serving`, `02_Evaluer_et_Choisir_un_Modele`, `03_RAG`, `04_Connaissance_Structuree_et_Stockage`.

- **Aucune page du brain n'est écrite.** Le seul livrable est `AI/prompts/proposition-fiches-connaissances-1.md`, un commit, poussé.
- **Lecture frugale** (le dossier pèse 1,2 Mo) : pour chaque fiche, frontmatter, titres et premier paragraphe de chaque section ; `query_index.py` sur chaque notion ou outil nommé ; lecture complète seulement des sections absentes du brain ou en désaccord avec lui.
- Le fichier de proposition dit, par fiche : ce que le brain couvre déjà (pages) ; ce qui manque (page candidate : nom, `role:`, `categorie:` pressentie, dossier dérivé, licence à vérifier pour une brique) ; les désaccords (texte exact de la page du brain, ce que dit la fiche, sa source) ; les enrichissements de notions existantes à proposer à floSa. Termine par un découpage en lots de huit pages au plus, rangés par dossier d'accueil.
- Règles 11 et 12 : pas de modèle, rien de payant ou cloud seulement dans les pages candidates.

## Lot 45 — Fiches de connaissances, thèmes 05 à 09 : confrontation (vague A, lecture seule)

Comme le lot 44, sur `05_Agents_IA`, `06_Securite_des_LLM_et_Agents`, `07_Modeles_de_Decision`, `08_Fondamentaux_des_LLM`, `09_ML_Classique`. Livrable : `AI/prompts/proposition-fiches-connaissances-2.md`. Pour `07_Modeles_de_Decision` : le lot 38 a retiré les fiches de modèles, ne propose que des notions.

## Suivi

- [ ] Lot 39 — GPU sur site : partager et ordonnancer
- [ ] Lot 40 — déployer sans Internet : air-gap et miroirs
- [ ] Lot 41 — reproductibilité et tests d'un pipeline ML
- [ ] Lot 42 — observabilité : collecte, traces et GPU
- [ ] Lot 43 — nouveaux documents de formation : NCM et µP
- [ ] Lot 44 — fiches de connaissances 01 à 04 : confrontation
- [ ] Lot 45 — fiches de connaissances 05 à 09 : confrontation
