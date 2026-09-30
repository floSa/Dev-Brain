---
role: brique
nom: OpenStack Swift
alias: [swift, openstack-swift]
pitch: "Stockage objet d'OpenStack (Apache 2.0) : proxy, anneau de placement et réplication ou erasure coding, API native Swift plus S3 par middleware ; maintenu mais historique, pertinent dans un parc OpenStack existant, cohérence à terme et sans cycle de vie ni étiquettes S3."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Ceph]]", "[[Apache Ozone]]", "[[SeaweedFS]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://docs.openstack.org/swift/latest/
url_repo: https://github.com/openstack/swift
---

# OpenStack Swift

<!-- AUTO:BANDEAU:START -->
> Stockage objet d'OpenStack (Apache 2.0) : proxy, anneau de placement et réplication ou erasure coding, API native Swift plus S3 par middleware ; maintenu mais historique, pertinent dans un parc OpenStack existant, cohérence à terme et sans cycle de vie ni étiquettes S3.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Le stockage objet d'**OpenStack**, l'un de ses plus anciens projets, écrit en **Python** et
publié sous **Apache 2.0**. Il se compose de serveurs **proxy** qui reçoivent les requêtes, de
serveurs de **comptes**, de **conteneurs** et d'**objets**, et d'un **anneau** (ring) qui
décide où vit chaque copie. La durabilité passe par trois réplicas par défaut, ou par de
l'erasure coding, au choix par **politique de stockage** et par conteneur. La cohérence est **à
terme** : la documentation admet qu'une liste de conteneur peut ne pas contenir immédiatement
un objet qui vient d'être écrit, et que le dernier écrivain gagne. Les listes de conteneurs sont
des bases SQLite répliquées. L'API de référence est l'**API REST Swift** ; l'API S3 est ajoutée
par le middleware `s3api`, issu du projet `swift3`. La frontière de l'outil est son âge : c'est
une brique qui a du sens à l'intérieur d'un cloud privé OpenStack, plus rarement en dehors.

*Constat du 2026-09-30 :* le projet livre une version par cycle OpenStack — **2.38.2** pour
le cycle Hibiscus (2026.2), 2.37.3 pour Gazpacho, 2.36.3 pour Flamingo —, la page de versions
ne donne pas de date par release. Environ **2,8 k étoiles** sur le miroir GitHub de
`opendev.org` ; dernier commit le 2026-09-29. Licence **Apache 2.0**. Le projet est vivant, mais
les deux constats qui pèsent viennent du marché : OVHcloud, qui a bâti son stockage objet sur
Swift dès 2014 (150 Po en octobre 2018, d'après TechTarget), écrit que ses classes Swift sont des générations
anciennes qui ne bénéficient plus de développements, et propose une offre S3 native pour les
besoins modernes (billet du 2026-07-07). SwiftStack, l'éditeur commercial historique, a été
racheté par NVIDIA en mars 2020 (TechTarget), qui utilise la technologie en interne et ne vend pas le logiciel.

## S3 — ce que le middleware couvre

La page de compatibilité S3 de la documentation (version en développement 2.39) liste :

- **Pris en charge** — objets (lecture, écriture, copie, suppression), multipart complet, **versioning**, ACL d'objets et de buckets, suppression multiple.
- **Non pris en charge** — notifications de bucket, **cycle de vie**, politiques de bucket, hébergement de site, **étiquettes d'objets et de buckets**, inventaire, facturation.
- **Non listé dans le tableau** — Object Lock et CORS : rien n'est annoncé.

Le cycle de vie et les étiquettes manquent : c'est ce qui empêche de le substituer à un
serveur S3 pour la plupart des outils de données modernes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un cloud privé OpenStack existe : Swift est le stockage objet natif, relié à Keystone | Nouvelle installation sans OpenStack : l'écosystème, les retours d'expérience et les nouveautés sont ailleurs → [[Ceph]], [[SeaweedFS]], [[RustFS]] |
| L'API Swift native est exigée par des applications existantes | Les outils exigent du cycle de vie ou des étiquettes S3 : le middleware ne les couvre pas |
| Politiques de stockage multiples par conteneur, avec réplication ou erasure coding au choix | La lecture après écriture doit être garantie : la cohérence est à terme, les listings peuvent être en retard |
| Durabilité attestée sur de grands volumes de longue date (OVHcloud a exploité 150 Po en 2018) | Une équipe d'exploitation doit gérer proxy, serveurs de comptes, conteneurs, objets et anneau : cinq zones sont recommandées au minimum pour trois réplicas |
| | Dynamique en baisse : le principal exploitant public a relégué ses classes Swift à l'usage historique |

## Mise en œuvre

- Installation — paquets des distributions OpenStack, ou déploiement par un outil de configuration ; l'image de conteneur n'est pas le mode de référence
- Point d'entrée — l'API REST Swift, et l'API S3 si le middleware `s3api` est activé dans le pipeline du proxy
- Prérequis — au moins cinq zones et trois réplicas pour le déploiement recommandé, selon le guide de déploiement ; Keystone ou une autre authentification pour les comptes
- Exécution — self-hébergé, distribué ; montée en charge par ajout de nœuds et rééquilibrage de l'anneau
- Coût — gratuit sous Apache 2.0 ; support par les distributions OpenStack commerciales

## Écosystème

### Alternatives

- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Apache Ozone]] — Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.

## Ressources

- Documentation — https://docs.openstack.org/swift/latest/
- Documentation — https://docs.openstack.org/swift/latest/s3_compat.html
- Dépôt — https://github.com/openstack/swift
- Article — https://blog.ovhcloud.com/?p=32743

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
