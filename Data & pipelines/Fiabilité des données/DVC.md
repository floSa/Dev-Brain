---
role: brique
nom: DVC
alias: [dvc, Data Version Control]
pitch: "Versionnage de données et de modèles en ligne de commande, posé sur Git : des pointeurs `.dvc` dans le dépôt, le contenu dans un cache adressé par le hash et des remotes (S3 compatible, SSH, NAS), plus des pipelines reproductibles par `dvc repro` ; Apache-2.0, projet racheté par lakeFS en novembre 2025."
categorie: data/fiabilite
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[lakeFS]]"]
complements: ["[[MinIO]]", "[[Ceph]]", "[[MLflow]]"]
tags: [data-versioning, reproducibility, ml-pipeline]
url_docs: https://doc.dvc.org
url_repo: https://github.com/treeverse/dvc
---

# DVC

<!-- AUTO:BANDEAU:START -->
> Versionnage de données et de modèles en ligne de commande, posé sur Git : des pointeurs `.dvc` dans le dépôt, le contenu dans un cache adressé par le hash et des remotes (S3 compatible, SSH, NAS), plus des pipelines reproductibles par `dvc repro` ; Apache-2.0, projet racheté par lakeFS en novembre 2025.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui applique à un jeu de données ou à un modèle la mécanique de Git sans
mettre le volume dans Git. `dvc add` calcule l'empreinte d'un fichier ou d'un dossier, le range dans un
**cache adressé par le contenu** et écrit à sa place un petit pointeur `.dvc` que Git versionne ; le
contenu part vers un **remote** par `dvc push`. Un commit Git fige donc le code, les pointeurs et les
paramètres : `git checkout <tag>`, `dvc pull`, puis `dvc repro` rejouent l'entraînement sur le jeu exact.
Le fichier `dvc.yaml` décrit un pipeline d'étapes avec leurs entrées, sorties, paramètres et métriques ;
`dvc repro` ne relance que les étapes dont une entrée a changé. `dvc exp` gère des expériences sans
serveur, `dvc import` et `dvc get` tirent une donnée versionnée d'un autre dépôt (un « registre de
données » sous forme de dépôt Git).

Relevé le 2026-09-30 : **3.67.1** du 2026-03-31 — aucune release depuis six mois —, dernier commit sur
`main` le 2026-08-06, environ 15 900 étoiles, dépôt sous Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Reproduire un entraînement à partir d'un jeu daté : un tag Git désigne code, paramètres et données d'un seul geste | Des milliers d'utilisateurs, des branches de données, des merges atomiques sur un lac entier → [[lakeFS]] |
| Un projet déjà dans Git, conduit par une ou quelques personnes, avec des données de quelques Gio à quelques centaines de Gio | Un très grand nombre de petits fichiers : la documentation reconnaît un surcoût au parcours, au hachage et au téléchargement, et renvoie vers lakeFS à l'échelle de l'objet |
| Un remote sans cloud : dossier réseau ou NAS, SSH, ou stockage S3-compatible sur site | Une table transactionnelle interrogée en SQL avec retour en arrière → le time travel d'un format de table, [[Apache Iceberg]] ou [[Delta Lake]] |
| Relier un run de suivi d'expériences à une version de donnée, en journalisant l'identifiant du commit comme paramètre du run ([[MLflow]]) | Un suivi d'expériences complet avec interface partagée : DVC n'en fournit qu'une version locale en ligne de commande |
| Du versionnage sans serveur à héberger : Git et un stockage suffisent | Aucune équipe qui maîtrise Git : tout le modèle en dépend |

## Mise en œuvre

- Installation — `uv add dvc` ou `pip install dvc`, avec l'extra du remote visé (`dvc[s3]`, `dvc[ssh]`…) ; Python 3.9 ou plus
- Point d'entrée — la commande `dvc` (`add`, `push`, `pull`, `repro`, `exp`, `import`), et une API Python `dvc.api` pour lire une donnée versionnée
- Prérequis — un dépôt Git ; un remote : S3 et compatibles (la documentation du remote S3 cite MinIO et Ceph), Azure Blob, GCS, SSH ou SFTP, HDFS, HTTP, WebDAV, ou un dossier local ou monté (NAS, NFS)
- Exécution — en local, sans service ; le cache lie les fichiers par reflink, lien physique, lien symbolique ou copie (le défaut est reflink puis copie : le disque double sur ext4 ou NTFS)
- Coût — gratuit ; le prix réel est le stockage du remote et la discipline de `dvc push`

## Licence et gouvernance

- **Apache-2.0** : le fichier `LICENSE` de `treeverse/dvc` porte « Copyright 2025 Treeverse », et les paquets satellites relevés (`dvc-data`, `dvc-objects`, `scmrepo`, les plugins de remote) sont déclarés Apache-2.0 sur PyPI. Aucune dépendance restrictive relevée parmi eux.
- **Changement de propriétaire.** lakeFS (Treeverse) a racheté le projet open source DVC à Iterative.ai le **2025-11-18**. Le dépôt vit désormais sous `treeverse/dvc` (l'ancienne adresse `iterative/dvc` redirige). L'annonce présente DVC comme un outil libre qui continue, tourné vers les data scientists et les petits jeux de données, et lakeFS comme l'offre pour l'échelle ; la documentation de DVC appelle lakeFS son « projet frère ». Le prix et les clauses ne sont pas publics.
- **Ce qui change pour un usage autonome.** Rien de technique : DVC s'utilise entièrement en ligne de commande, avec Git et un remote, sans DVC Studio. **DVC Studio** (interface web de comparaison d'expériences et de registre) n'est pas traité par l'annonce de rachat ; les pages officielles de sa documentation n'étaient pas lisibles le 2026-09-30 et des sources tierces parlent d'un produit désormais rattaché à DataChain, d'une offre par équipe et d'un auto-hébergement sur devis — non vérifié à la source. Ne pas bâtir un processus sur Studio.
- **Activité depuis le rachat** : maintenance minimale. Des releases régulières d'août 2025 à mars 2026, puis aucune ; les commits de l'été sont presque tous des mises à jour automatiques de dépendances et de CI, plus un correctif de docstrings. Pause ou ralentissement durable : non établi. **CML**, l'outil de CI pour ML du même éditeur, n'a pas de commit ni de release depuis octobre 2024.

## Limites à connaître

- **Git est obligatoire** : pointeurs, versions et expériences en dépendent ; sans Git, rien à retrouver.
- **Pas de branches ni de transactions côté stockage** : la version est portée par Git, le remote n'est qu'un dépôt d'objets. Un lecteur qui n'a pas le dépôt Git ne sait pas quelle version lire.
- **Pas de contrôle d'accès côté remote** : celui du stockage choisi s'applique, rien de plus.
- **Le suivi d'expériences suppose des runs déterministes** : la documentation le dit ; sans graine fixée, `dvc repro` ne garantit pas le même modèle.
- **Les règles de cycle de vie d'un bucket** peuvent supprimer des versions que le mode `--version-aware` ne saura plus restaurer.

## Écosystème

### Alternatives

- [[lakeFS]] — Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur. — même éditeur depuis le rachat ; DVC versionne des fichiers à travers Git, lakeFS un dépôt d'objets à travers une API, et sa licence est passée en septembre 2026 à la BSL.

### Compléments

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire. — remote S3-compatible cité par la documentation de DVC ; la brique est non maintenue, préférer un autre stockage pour une nouvelle installation.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde. — remote S3-compatible cité par la documentation de DVC.
- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud. — aucune intégration native : l'identifiant du commit Git ou DVC se journalise comme paramètre d'un run, et un article d'AWS de 2026 en donne la recette.

## Ressources

- Documentation — https://doc.dvc.org
- Article — https://lakefs.io/blog/lakefs-acquires-dvc/
- Dépôt — https://github.com/treeverse/dvc

## Voir aussi

- [[Fiabilité des données]] — le hub du dossier
- [[Versionnage de données]] — la notion : snapshot ou versionnage par contenu, fichiers, dépôt ou table
- [[Comparatif - Versionnage de données]] — ce qui départage DVC, lakeFS, Delta Lake et Apache Iceberg
- [[Model registry & versioning]] — la donnée versionnée ici se relie au modèle versionné là
