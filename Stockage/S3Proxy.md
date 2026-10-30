---
role: brique
nom: S3Proxy
alias: [s3proxy, s3 proxy, gaul/s3proxy]
pitch: "Passerelle S3 en Java sous Apache 2.0 qui traduit l'API S3 vers Azure, Google Cloud, OpenStack Swift, SFTP, un autre S3 ou un dossier local, et sert aussi à tester sans AWS : sans stockage propre ni console, avec un seul mainteneur (99 % des commits sur six mois) — une passerelle, pas un moteur."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Versity GW]]", "[[SeaweedFS]]", "[[RustFS]]", "[[Garage]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://github.com/gaul/s3proxy/wiki
url_repo: https://github.com/gaul/s3proxy
---

# S3Proxy

<!-- AUTO:BANDEAU:START -->
> Passerelle S3 en Java sous Apache 2.0 qui traduit l'API S3 vers Azure, Google Cloud, OpenStack Swift, SFTP, un autre S3 ou un dossier local, et sert aussi à tester sans AWS : sans stockage propre ni console, avec un seul mainteneur (99 % des commits sur six mois) — une passerelle, pas un moteur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Passerelle S3** écrite en **Java** (Java 17 ou plus) : un serveur qui parle l'API S3 vers les
clients et traduit chaque requête vers un autre stockage, par la bibliothèque jclouds. Les
backends listés par le README sont Amazon S3, Azure Blob, Google Cloud Storage, OpenStack Swift
(Keystone v3), SFTP, un **dossier local** et un stockage en mémoire. Ses usages : traduire S3 vers
un stockage qui ne le parle pas, **tester sans Amazon** avec le système de fichiers local,
étendre le comportement par des middlewares, ou l'embarquer dans une application Java. Elle ne
stocke rien elle-même et n'a pas d'interface web : durabilité et capacité sont celles du backend.
**Une passerelle, pas un moteur** : [[Versity GW]] couvre l'autre cas courant, celui d'un système
de fichiers que l'on veut servir en S3.

**Un seul mainteneur.** Sur les six derniers mois, un auteur signe 506 des 513 commits (99 %).

*Constat du 2026-10-30 :* version **4.1.1** publiée le 2026-09-10 (4.1.0 le 2026-08-26, 4.0.0 le
2026-08-04), dernier push le 2026-10-02 ; environ **2,4 k étoiles** GitHub ; licence **Apache 2.0**
lue dans le fichier `LICENSE` du dépôt ; dépôt créé en 2014.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une application ne parle que S3 et le stockage cible est Azure, Google Cloud, Swift ou SFTP | Un nouveau stockage est à construire : la passerelle n'en fournit pas → [[SeaweedFS]], [[RustFS]] ou [[Garage]] |
| Un S3 jetable pour les tests et la CI, sur un dossier local ou en mémoire, sans AWS | Une interface web de gestion : il n'y en a pas |
| Des middlewares à insérer entre le client et le backend, ou une intégration dans une application Java | La compatibilité S3 complète : le README liste des écarts selon le backend (ACL par objet, versioning, chiffrement SSE-C) |
| | La continuité du projet compte : un seul mainteneur, 99 % des commits |

## Mise en œuvre

- Installation — un exécutable Java des releases GitHub (Java 17 ou plus), une image Docker (`andrewgaul/s3proxy`), ou la dépendance Maven `org.gaul:s3proxy` pour l'embarquer
- Point d'entrée — l'API S3 ; un fichier de propriétés (`s3proxy.endpoint`, `jclouds.provider`, identifiants du backend)
- Prérequis — un backend accessible et ses identifiants ; Java 17 ou plus sans Docker
- Exécution — self-hébergé, un processus Java ; plusieurs backends possibles, un bucket assigné à un seul
- Coût — gratuit sous Apache 2.0

## Écosystème

### Alternatives

- [[Versity GW]] — Passerelle S3 en Go sous Apache 2.0 qui expose un système de fichiers POSIX, ScoutFS ou Azure Blob comme un serveur S3, ou relaie vers un autre serveur S3 : sans état, sans stockage propre, avec une WebGUI optionnelle et un mode S3 sur RDMA — une passerelle, pas un moteur.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

## Ressources

- Documentation — https://github.com/gaul/s3proxy/wiki
- Dépôt — https://github.com/gaul/s3proxy

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
