---
role: brique
nom: CVAT
alias: [cvat, Computer Vision Annotation Tool, cvat.ai]
pitch: "Outil d'annotation pour la vision — images, vidéo, nuages de points 3D — avec boîtes, polygones, masques, squelettes, cuboïdes et suivi d'objets par interpolation, 27 formats d'export et pré-annotation par fonctions serverless (SAM, YOLOv7, Detectron2) ; MIT, mais SSO, contrôle qualité automatique, analytics et agents sont réservés à l'édition Enterprise."
categorie: ml/annotation
famille: application
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Python
alternatives: ["[[Label Studio]]"]
complements: ["[[Ultralytics YOLO]]", "[[Detectron2]]", "[[segment-anything]]", "[[Postgres]]", "[[Docker Compose]]", "[[Kubernetes]]", "[[Keycloak]]"]
tags: [annotation, computer-vision, object-detection, segmentation, human-in-the-loop, self-hosted]
url_docs: https://docs.cvat.ai
url_repo: https://github.com/cvat-ai/cvat
---

# CVAT

<!-- AUTO:BANDEAU:START -->
> Outil d'annotation pour la vision — images, vidéo, nuages de points 3D — avec boîtes, polygones, masques, squelettes, cuboïdes et suivi d'objets par interpolation, 27 formats d'export et pré-annotation par fonctions serverless (SAM, YOLOv7, Detectron2) ; MIT, mais SSO, contrôle qualité automatique, analytics et agents sont réservés à l'édition Enterprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-core | self-hébergé ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil web d'annotation **pour la vision par ordinateur**. Les formes : rectangles, polygones,
polylignes, points, ellipses, cuboïdes, squelettes, pinceau pour les masques, tags de classification,
et **pistes vidéo** qui relient une forme d'une image à l'autre. Les données : images, vidéos, nuages de
points 3D et, depuis peu, audio. L'import et l'export couvrent 27 formats — COCO, Pascal VOC, CVAT XML,
Datumaro, Cityscapes, KITTI, MOT, et cinq variantes Ultralytics (détection, segmentation, pose, boîtes
orientées, classification). La **pré-annotation** passe par des fonctions serverless Nuclio : SAM pour
segmenter à partir d'un clic, IOG, YOLOv7, Mask R-CNN ou RetinaNet pour détecter, TransT pour suivre.

Relevé le 2026-09-30 : **v2.77.0** du 2026-09-28, environ 16 800 étoiles, une release toutes les une à
deux semaines, dépôt en MIT (copyright CVAT.ai Corporation après Intel), Python et TypeScript à parts
voisines.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des images ou des vidéos à étiqueter : boîtes, polygones, masques, squelettes, suivi d'objets | Du texte, de l'audio comme corpus de transcription, des séries temporelles : aucune balise dans la documentation lue → [[Label Studio]] |
| Un export directement lisible par un entraînement : COCO, YOLO et ses variantes Ultralytics, Pascal VOC | Un SSO d'entreprise : OIDC et SAML sont documentés pour **Enterprise** seulement ; Authentik n'a pas de page officielle |
| Une pré-annotation locale, sans service externe : les fonctions Nuclio tournent sur CPU (script `deploy_cpu.sh`) ou sur GPU | Les agents d'annotation, SAM 2 et SAM 3, le contrôle qualité par jobs Ground Truth et les analytics : Enterprise ou Online, pas Community |
| Un déploiement sur site par `docker compose up -d`, sans cloud | Une pile légère : le fichier Compose lance le serveur et ses workers, l'interface, PostgreSQL, Redis, Kvrocks, Traefik, OPA, ClickHouse, Vector et Grafana |

## Mise en œuvre

- Installation — `git clone` du dépôt puis `docker compose up -d`, création du superutilisateur dans le conteneur ; chart Helm pour Kubernetes (RWX requis sur plusieurs nœuds) ; fonctions Nuclio en option (`nuctl`, `docker-compose.serverless.yml`)
- Point d'entrée — l'interface web ; une API REST, un SDK et une CLI (`cvat-cli`)
- Prérequis — Docker et Docker Compose ; PostgreSQL 15 et Redis 7.2 dans l'image Compose ; Chrome est le seul navigateur annoncé comme pris en charge ; aucune exigence de mémoire ou de CPU trouvée dans la documentation d'installation
- Exécution — stockage local par volumes ; stockage cloud S3, Azure ou GCS en montage FUSE (MinIO non cité explicitement) ; GPU facultatif, pour les modèles d'auto-annotation seulement
- Coût — Community gratuite. **Online** (cvat.ai) : plan Free limité, plans payants par utilisateur. **Enterprise** auto-hébergée : 12 000 $ pour Basic (une instance, support par courriel sous 24 h), Premium sur devis (VPN, proxy, air-gap)

## Licence et gouvernance

- **MIT** pour le dépôt : copyright Intel 2018-2022, CVAT.ai Corporation 2022-2025. Les modèles des fonctions serverless (SAM, YOLOv7, Detectron2…) ont chacun leur licence, non relevée ici ; à lire avant d'embarquer un modèle.
- **Open-core.** La page officielle de l'offre Enterprise lui réserve : le SSO SAML et OIDC, LDAP, la vérification et le contrôle qualité automatiques par Ground Truth, les analytics et rapports, SAM 2 et SAM 3 pour les images, SAM 2 pour la vidéo, les agents d'IA, les intégrations Hugging Face et Roboflow.
- **Désaccord entre sources** : la page tarifaire place LDAP dans Enterprise, la page de documentation de LDAP le déclare pertinent pour Community et Enterprise (configuration par surcharge de `settings.py`). La documentation est probablement plus à jour ; à tester.
- **Gouvernance** : société commerciale, CVAT.ai Corporation, issue du projet d'Intel. La date exacte du passage de `openvinotoolkit` à `cvat-ai` n'a pas été établie.

## Limites à connaître

- **Vision seulement** : ni NER, ni classification de texte, ni séries temporelles.
- **Pas de tableau officiel unique des éditions** : la liste des fonctions payantes se reconstitue depuis la page tarifaire et la documentation, qui ne concordent pas partout (LDAP, organisations et rôles, analytics).
- **Pile multi-conteneurs** à exploiter : une dizaine de services à mettre à jour ensemble, à chaque release.
- **Adoption non mesurée** : seul indicateur relevé, le nombre d'étoiles et le rythme des releases ; les comparaisons publiées avec Label Studio sont celles de l'éditeur.

## Écosystème

### Alternatives

- [[Label Studio]] — Plateforme d'annotation web multimodale — images, texte, audio, vidéo, séries temporelles — configurée par un gabarit XML, avec pré-annotation par un backend ML ; l'édition Community est sous Apache-2.0, rôles, SSO SAML, métriques d'accord et boucle d'active learning automatique sont réservés aux éditions payantes. — mêmes images et vidéos, mais CVAT pousse la vision (suivi par pistes, squelettes, 3D, formats d'entraînement) là où Label Studio couvre aussi le texte, l'audio et les séries.

### Compléments

- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0. — cinq formats d'export Ultralytics (détection, segmentation, pose, boîtes orientées, classification) ; la fonction serverless fournie détecte avec YOLOv7, pas avec Ultralytics.
- [[Detectron2]] — Plateforme de détection et segmentation de Meta AI (FAIR) sur PyTorch — implémentations de référence Faster/Mask R-CNN, RetinaNet, panoptique, modulaires et étendables via un model zoo ; la base recherche quand on veut customiser l'architecture. — fonction serverless `pytorch/facebookresearch/detectron2` dans le dépôt, pour la détection et la segmentation d'instances.
- [[segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte). — fonction serverless `pytorch/facebookresearch/sam` pour segmenter par clic ; SAM 2 et SAM 3 sont réservés à Enterprise et Online.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base du fichier Compose (PostgreSQL 15).
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — mode d'installation officiel de l'édition Community.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm documenté, avec PostgreSQL, Redis, ClickHouse en option et Nuclio.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — guide de configuration OIDC et SAML dans la page SSO, qui ne vaut que pour Enterprise.

## Ressources

- Documentation — https://docs.cvat.ai
- Article — https://www.cvat.ai/pricing/enterprise
- Dépôt — https://github.com/cvat-ai/cvat

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[Annotation de données]] — la notion : types de tâches, guides, accord entre annotateurs, pré-annotation et ses biais, active learning, annotation sur site
- [[Vision]] — le hub de la vision par ordinateur, où se consomment les jeux annotés ici
