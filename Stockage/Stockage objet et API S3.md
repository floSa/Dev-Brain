---
role: notion
nom: Stockage objet et API S3
alias: [API S3, compatibilité S3, S3-compatible, choisir un stockage objet on-prem]
categorie: storage/objet
domaines: [data-eng, mlops, infra-ops]
tags: [object-storage, s3-compatible]
---

# Stockage objet et API S3

## Aperçu

- Un **stockage objet** range des blocs de données immuables, chacun adressé par une clé dans un *bucket*, derrière une API HTTP. Il n'a ni arborescence réelle, ni écriture partielle : c'est ce qui le rend extensible presque sans limite, et ce qui a obligé les formats de table ([[Apache Iceberg]], Delta) à réinventer la transaction par-dessus.
- L'**API S3** d'Amazon en est devenue le langage commun. Elle n'est pas une norme : c'est une API propriétaire, que tous les autres réimplémentent. Choisir un backend on-prem, c'est donc choisir ce qui **n'est pas dans le contrat** — durabilité, identités, administration, fonctions récentes, état du projet — bien plus que l'API elle-même.

## Concepts clés

### Le modèle objet
- La doc AWS le dit telle quelle : un espace **plat**, sans sous-bucket ni sous-dossier. Les « dossiers » sont des préfixes de clé découpés sur un délimiteur, et la console crée un objet vide dont la clé finit par `/`.
- Quelques limites documentées : clé de 1 024 octets UTF-8 au plus, métadonnées utilisateur de 2 Ko, 10 étiquettes par objet, un PUT simple plafonné à 5 Go, un multipart de 10 000 parties de 5 Mio à 5 Gio. La taille maximale d'un objet est passée à **50 To** le 2025-12-02 ; la page des URL présignées dit encore 5 To, donc les pages AWS ne sont pas à jour entre elles.
- La mise à jour d'une clé est **atomique** : on lit l'ancienne donnée ou la nouvelle, jamais un mélange. Aucune atomicité entre clés, aucun verrou pour écrivains concurrents (le dernier gagne), et renommer un objet revient à en créer un nouveau.

### Ce que l'API S3 standardise
- Une API REST versionnée `2006-03-01` : PUT, GET, HEAD, DELETE, listage, **multipart**, **URL présignées**, avec authentification par **Signature V4**.
- Des fonctions de gestion : **versioning**, cycle de vie, **réplication**, notifications d'événements, chiffrement côté serveur, ACL et politiques de bucket, étiquettes, CORS.
- **Object Lock** : un modèle WORM avec modes Governance et Compliance et *legal holds*, qui exige un bucket versionné. AWS fait état d'une évaluation par Cohasset Associates pour SEC 17a-4, CFTC et FINRA.
- La **lecture après écriture forte** pour les objets et les listings, depuis le 2020-12-01, sans surcoût. Seules les configurations de bucket restent à cohérence à terme.

### Ce qu'elle ne standardise pas
- **Aucune norme.** Aucun effort ISO, IETF ou SNIA sur S3 n'a été trouvé. L'alternative normalisée existe : **CDMI** de la SNIA, ISO/IEC 17826:2016 ; son adoption réelle n'a pas été mesurée dans les sources lues. Une étude de 2026 (Brandes, arXiv) examine justement quand une mention « compatible avec » réduit le risque d'un acheteur et quand elle réduit seulement le coût de première intégration, avec S3 pour l'un de ses cinq cas.
- **La durabilité.** Réplication ou erasure coding, nombre de copies, domaines de panne : chaque implémentation choisit (cf. *Les maths, simplement*).
- **Les identités et l'administration.** Création de clés, quotas, console : Garage a son propre modèle de droits par clé et par bucket, MinIO et R2 ont leurs mécanismes. Migrer d'un serveur à l'autre, c'est réécrire cette couche.
- **Les fonctions récentes.** Les écritures conditionnelles (`If-None-Match` sur PutObject le 2024-08-20, `If-Match` le 2024-11-25 chez AWS) ne sont pas partout. Les nouveautés d'AWS — S3 Express One Zone, Tables, Vectors, Files (2026-04-07), Annotations (2026-06-16) — sont propres à AWS.
- **Les performances et le coût des listings.** AWS facture un `LIST` au tarif d'un `PUT` ; aucune source lue ne donne d'équivalent on-prem.

### Les lacunes déclarées par les implémentations
Chaque projet publie sa page de compatibilité, et aucune ne dit « identique ». Lues le 2026-09-30 :

| Projet | Manques déclarés |
|---|---|
| [[Garage]] | versioning, Object Lock, ACL et politiques, étiquettes, notifications, réplication S3 ; cycle de vie réduit à l'expiration et à l'abandon des multiparts |
| [[Cloudflare R2]] | versioning et Object Lock S3 (remplacés par des « bucket locks » propriétaires), ACL, politiques, étiquettes, notifications ; seul SSE-C côté chiffrement |
| [[SeaweedFS]] | notifications de bucket, réplication S3 native, site web, MFA Delete, règles de transition, `SelectObjectContent` |
| [[Apache Ozone]] | ACL, politiques, CORS, site web, versioning, Object Lock, SSE S3, S3 Select, requêtes conditionnelles, cycle de vie, réplication inter-régions, notifications |
| [[OpenStack Swift]] | notifications, cycle de vie, politiques, site web, étiquettes, inventaire, facturation |
| [[MinIO]] (AIStor) | ACL (les politiques les remplacent), analytics, metrics, journalisation, site web, inventaire |
| [[Ceph]] | réplication de bucket « partielle », entre zones seulement |

### La cohérence selon les implémentations
- **AWS** : forte, depuis 2020.
- **[[Garage]]** : lecture après écriture par quorums (2 sur 3), sans consensus ; le billet de l'équipe (2023-12-06) explique que cette garantie se rompait pendant un changement de disposition du cluster jusqu'à la v0.9.0, et qu'un correctif était prévu pour la v0.10.
- **[[Apache Ozone]]** : cohérence forte, par Raft.
- **[[OpenStack Swift]]** : à terme — une liste de conteneur peut ne pas contenir immédiatement l'objet écrit ; le dernier écrivain gagne.
- **[[Ceph]], [[SeaweedFS]], [[MinIO]], [[Cloudflare R2]]** : déclaration de cohérence non trouvée dans les pages lues.

### Les suites de tests
- `ceph/s3-tests` se décrit comme une suite **non officielle** de tests de compatibilité S3, pour qui implémente une API de type S3 ; elle marque les tests qui échouent sur AWS lui-même.
- **Mint** de MinIO lance des SDK et des clients contre un serveur ; son dépôt est **archivé depuis le 2026-03-26**.
- Un *plugfest* de la SNIA (septembre 2025) a fait remonter des ambiguïtés de protocole, des en-têtes manquants ou incorrects et des appels non supportés ; c'est un compte rendu qualitatif.
- **Aucune mesure indépendante** du taux de compatibilité entre clones, de moins de dix-huit mois, n'a été trouvée.

## Les maths, simplement

- **Réplication** à $n$ copies : surcoût de $n\times$, et $n-1$ pertes tolérées. Trois copies coûtent $3\times$ et supportent deux pertes.
- **Erasure coding** Reed-Solomon $\mathrm{RS}(k, m)$ : $k$ fragments de données, $m$ fragments de parité, surcoût de $\dfrac{k+m}{k}$, et $m$ pertes tolérées.
- Les schémas annoncés par les projets, avec le surcoût que l'arithmétique en tire :

| Projet | Schéma | Surcoût |
|---|---|---|
| [[SeaweedFS]] | RS(10,4), par défaut | $14/10 = 1{,}4\times$ |
| [[Apache Ozone]] | 3:2, 6:3, 10:4 | $1{,}67\times$, $1{,}5\times$, $1{,}4\times$ |
| [[MinIO]] | EC:4 sur 16 disques (exemple de la doc, 75 % utile) | $16/12 = 1{,}33\times$ |
| [[Ceph]] | k=2, m=2, profil par défaut | $2\times$ |
| [[Garage]] | aucun : réplication seule, facteur 3 par défaut | $3\times$ |

- Le surcoût n'est pas tout : l'erasure coding demande un nombre minimal de domaines de panne (Ozone : 10 Datanodes pour RS-6-3), et la doc de Ceph prévient d'un surcoût d'espace avec beaucoup de petits objets.
- **Quorum** : avec $N$ réplicas, une lecture de $R$ et une écriture de $W$ se recouvrent si $R + W > N$. C'est ce qui permet la lecture après écriture de [[Garage]] sans consensus : $2 + 2 > 3$.

## En pratique

- **Le point de départ a changé.** [[MinIO]], longtemps le serveur S3 par défaut, est archivé depuis le 2026-04-25 (cf. sa fiche) : un choix d'il y a deux ans ne se reconduit pas sans relecture. [[RustFS]] en vise la succession et n'a que deux semaines de version stable.
- **Partir des exigences qui éliminent**, pas d'un classement :
  - **WORM ou conformité** : Object Lock présent chez [[SeaweedFS]], [[Ceph]] (documenté) et [[RustFS]] ; absent chez [[Garage]], [[Apache Ozone]] et [[Cloudflare R2]] (qui a ses propres verrous).
  - **Échelle et équipe** : [[Garage]] pour un petit cluster sur plusieurs sites, [[SeaweedFS]] pour l'intermédiaire, [[Ceph]] quand le cluster sert aussi du bloc et du fichier et qu'une équipe l'exploite, [[Apache Ozone]] pour l'analytique Hadoop sur de très gros volumes.
  - **Licence** : AGPL pour [[MinIO]] et [[Garage]] (copyleft réseau, à faire valider) ; Apache 2.0 pour [[RustFS]], [[SeaweedFS]], [[Apache Ozone]] et [[OpenStack Swift]] ; LGPL pour [[Ceph]].
  - **Petits fichiers** : c'est la thèse de [[SeaweedFS]], dont les chiffres publiés viennent d'un portable ; une page de son wiki, non mise à jour depuis 2018, dit elle-même qu'ils sont trompeurs.
- **Tester ses propres clients.** Les SDK, l'outil de sauvegarde, le moteur de requêtes : c'est leur jeu d'opérations qui compte, pas le catalogue du projet. Une liste de manques, comme celle ci-dessus, se confronte à cette liste-là.
- **Se méfier des benchmarks.** Un essai individuel de mars 2026 compare MinIO, SeaweedFS, Garage et RustFS, mais MinIO fait un `fsync` par écriture et les autres non : les politiques de durabilité diffèrent, donc la vitesse ne se compare pas. Un autre, d'août 2025, est mesuré sur un nœud unique sans réglage, et ses auteurs préviennent que le multinœud peut différer beaucoup. Les comparatifs publiés par des éditeurs de produits qui se connectent à ces backends ne sont pas indépendants.
- **Migrer demande de réécrire l'IAM.** L'API se repointe ; les politiques, les clés et la réplication sont propres à chaque serveur.

## Approches voisines & alternatives

- [[Comparatif - Stockage objet]] — ce qui départage les neuf briques du dossier, avec leur état et leur licence.
- [[Stockage]] — le hub du domaine.
- [[AWS S3]] et [[Cloudflare R2]] — les références managées, dont l'egress est le poste de coût qui surprend.
- [[MinIO]], [[RustFS]], [[SeaweedFS]], [[Garage]], [[Ceph]], [[Apache Ozone]], [[OpenStack Swift]] — les serveurs auto-hébergeables.
- [[Apache Iceberg]] — le format de table qui pose des transactions au-dessus d'objets.
- **JuiceFS** n'a pas de page ici : c'est un système de fichiers POSIX, Apache 2.0, qui s'appuie sur un stockage objet existant et sur une base de métadonnées (Redis, PostgreSQL, TiKV). Il se pose sur les briques ci-dessus ; il ne les remplace pas.

## Pour aller plus loin

- AWS — *Amazon S3 data model et clés d'objets* — https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html
- AWS — *Amazon S3 now delivers strong read-after-write consistency automatically for all applications* (2020-12-01) — https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-now-delivers-strong-read-after-write-consistency-automatically-for-all-applications/
- AWS — *Amazon S3 adds support for conditional writes* (2024-08-20) — https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/
- AWS — *Amazon S3 increases maximum object size to 50 TB* (2025-12-02) — https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-maximum-object-size-50-tb/
- AWS — *S3 Object Lock* — https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html
- Brandes (2026-08-21) — *The Substitution Escrow Threshold: When « Compatible With » Becomes Safe Enough to Buy* — https://arxiv.org/abs/2608.21221 (résumé lu)
- SNIA — *Cloud Data Management Interface (CDMI)* — https://www.snia.org/cdmi
- Garage (2023-12-06) — *Preserving read-after-write consistency* — https://garagehq.deuxfleurs.fr/blog/2023-12-preserving-read-after-write-consistency/
- Garage — *S3 compatibility status* — https://garagehq.deuxfleurs.fr/documentation/reference-manual/s3-compatibility/
- Cloudflare — *R2 S3 API compatibility* — https://developers.cloudflare.com/r2/api/s3/api/
- SeaweedFS — *Amazon S3 API* — https://github.com/seaweedfs/seaweedfs/wiki/Amazon-S3-API
- Ceph — *Ceph Object Gateway S3 API* — https://docs.ceph.com/en/latest/radosgw/s3/
- Ceph — `s3-tests` — https://github.com/ceph/s3-tests
- komsit37 (2026-03-25) — benchmark MinIO, SeaweedFS, Garage, RustFS, auteur individuel — https://gist.github.com/komsit37/7029089c05b741931dd21ac49687dd4b
- RepoFlow (2025-08-09) — *Benchmarking self-hosted S3-compatible storage* — https://www.repoflow.io/blog/benchmarking-self-hosted-s3-compatible-storage-a-practical-performance-comparison

> Désaccord entre les sources, non tranché : la taille maximale d'un objet S3 est de 50 To d'après l'annonce AWS du 2025-12-02 et sa FAQ, de 5 To d'après la page des URL présignées, non mise à jour. Non trouvé : une déclaration de cohérence pour Ceph RGW, SeaweedFS, MinIO et R2 ; un support des écritures conditionnelles confirmé pour Ceph et Garage ; une mesure d'adoption de CDMI ; toute mesure indépendante de conformité S3 entre clones ; le coût et la performance des listings hors AWS.
