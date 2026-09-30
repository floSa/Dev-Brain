---
role: brique
nom: Label Studio
alias: [label-studio, labelstudio, HumanSignal Label Studio]
pitch: "Plateforme d'annotation web multimodale — images, texte, audio, vidéo, séries temporelles — configurée par un gabarit XML, avec pré-annotation par un backend ML ; l'édition Community est sous Apache-2.0, rôles, SSO SAML, métriques d'accord et boucle d'active learning automatique sont réservés aux éditions payantes."
categorie: ml/annotation
famille: application
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Python
alternatives: ["[[CVAT]]"]
complements: ["[[Ultralytics YOLO]]", "[[segment-anything]]", "[[spaCy]]", "[[GLiNER]]", "[[Postgres]]", "[[Docker Compose]]", "[[Kubernetes]]"]
tags: [annotation, human-in-the-loop, self-hosted, computer-vision, ner]
url_docs: https://labelstud.io/guide
url_repo: https://github.com/HumanSignal/label-studio
---

# Label Studio

<!-- AUTO:BANDEAU:START -->
> Plateforme d'annotation web multimodale — images, texte, audio, vidéo, séries temporelles — configurée par un gabarit XML, avec pré-annotation par un backend ML ; l'édition Community est sous Apache-2.0, rôles, SSO SAML, métriques d'accord et boucle d'active learning automatique sont réservés aux éditions payantes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-core | self-hébergé ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme web d'annotation, **multimodale**. Un projet se décrit par un gabarit XML qui assemble des
balises d'objet (`Image`, `Text`, `Audio`, `Video`, `TimeSeries`, `HyperText`…) et des balises de
contrôle (`Choices`, `Labels`, `RectangleLabels`, `PolygonLabels`, `BrushLabels`, `KeyPointLabels`,
`Relations`). Le même outil sert donc la classification, la détection, la segmentation, la
reconnaissance d'entités, la transcription et le découpage de séries. Les tâches s'importent dans le
*Data Manager* ; l'export sort en JSON, JSON_MIN, CSV, TSV, COCO, YOLO, Pascal VOC, CoNLL2003, spaCy,
ASR_MANIFEST, ou en masques NumPy et PNG pour la brosse. Un **backend ML** — un petit serveur écrit avec
le SDK `label-studio-ml-backend` (méthode `predict()`, `fit()` facultative) — renvoie des
pré-annotations que l'annotateur corrige, en lot ou à la demande.

Relevé le 2026-09-30 : **1.23.2** du 2026-09-29, environ 28 400 étoiles, dépôt en Apache-2.0 tenu par
HumanSignal (ex-Heartex).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs types de données à étiqueter avec un seul outil — texte, images, audio, vidéo, séries — sur une machine sans cloud | Des images et des vidéos seulement, avec suivi d'objets, squelettes ou cuboïdes à grande échelle → [[CVAT]] |
| Pré-annoter avec un modèle maison ou un modèle public : le dépôt du SDK livre des exemples pour [[Ultralytics YOLO]], [[segment-anything]], [[spaCy]] et [[GLiNER]] | Plusieurs équipes, des rôles distincts, l'affectation automatique des tâches et des workspaces : ces fonctions sont payantes |
| Un outil gratuit à installer en quelques minutes (`pip` ou Docker) pour un petit lot ou un prototype | Un accord inter-annotateurs à mesurer sans le calculer soi-même : les métriques d'accord, les tableaux de bord et la performance par annotateur sont payants |
| Garder les données sur site : SQLite ou PostgreSQL, stockage local, aucun appel sortant exigé par l'application | Un SSO d'entreprise : SAML seulement, et seulement en Enterprise ; aucune page relevée ne décrit Keycloak, Authentik ou OIDC |
| | Une boucle d'active learning **automatique** : la documentation la réserve à Enterprise, la Community se contente d'un tri manuel des tâches |

## Mise en œuvre

- Installation — `pip install label-studio`, Docker, Docker Compose (avec PostgreSQL), chart Helm (`helm repo add heartex https://charts.heartex.com/`), Homebrew ou Anaconda
- Point d'entrée — l'interface web sur le port 8080, une API REST et un SDK Python ; le compte local se crée au premier lancement
- Prérequis — Python 3.10 ou plus d'après `pyproject.toml` (la page d'installation annonce encore 3.8 : désaccord, le fichier du dépôt fait foi) ; SQLite 3.35 ou plus par défaut, PostgreSQL 14 ou plus recommandé en production ; 8 Gio de mémoire au minimum, 16 Gio conseillés, 50 Gio de disque en production
- Exécution — stockage des fichiers local, S3, GCS, Azure Blob ou Redis en Community ; l'application n'exige aucun GPU, seuls les backends ML qui servent YOLO ou SAM en demandent un
- Coût — gratuit en Community ; Starter Cloud (SaaS) et Enterprise sont payantes, tarifs non relevés

## Licence et gouvernance

- **Apache-2.0** pour le dépôt (copyright Heartex, Inc.), et pour le SDK des backends ML. Licence permissive : rien à craindre pour un usage interne ou pour une redistribution.
- **Open-core.** La page officielle de comparaison des éditions réserve à **Enterprise** : les rôles Admin / Manager / Reviewer / Annotator et les permissions fines, les workspaces, les métriques d'accord personnalisées, les tableaux de bord de projet, le suivi de la performance des annotateurs, les journaux d'audit, la réaffectation automatique selon l'accord, les boucles d'active learning, le SSO SAML et la conformité SOC2. L'affectation des tâches, les règles de distribution et la revue assignée descendent jusqu'à **Starter Cloud**, qui n'est pas auto-hébergeable.
- **Conséquence sur site.** Une installation Community sert un annotateur ou un petit groupe sans hiérarchie ; dès qu'il faut des rôles, une revue et une mesure de l'accord, la voie gratuite s'arrête.
- **Gouvernance** : société commerciale, sans fondation. Le chart Helm reste hébergé sur le domaine de l'ancien nom, `charts.heartex.com`.

## Limites à connaître

- **Pas de revue ni de consensus en Community** : tout annotateur voit tout, le calcul d'accord se fait hors de l'outil sur l'export.
- **Une version de Python contradictoire** entre la page d'installation et le dépôt : se fier au dépôt.
- **Compatibilité S3 de type MinIO ou Ceph** : la page de stockage relevée ne la mentionne pas ; non établi, à tester avant de s'y appuyer.
- **Pré-annotation et biais d'ancrage** : un modèle qui pré-remplit raccourcit le travail et oriente le regard de l'annotateur ; le risque est décrit dans [[Annotation de données]].

## Écosystème

### Alternatives

- [[CVAT]] — Outil d'annotation pour la vision — images, vidéo, nuages de points 3D — avec boîtes, polygones, masques, squelettes, cuboïdes et suivi d'objets par interpolation, 27 formats d'export et pré-annotation par fonctions serverless (SAM, YOLOv7, Detectron2) ; MIT, mais SSO, contrôle qualité automatique, analytics et agents sont réservés à l'édition Enterprise. — recouvre les images et les vidéos ; Label Studio ajoute le texte, l'audio et les séries, CVAT la vision en profondeur (suivi, squelettes, 3D, 27 formats).

### Compléments

- [[Ultralytics YOLO]] — Famille de modèles de détection temps réel (YOLOv8 → YOLO11 → YOLO26) avec une API Python unifiée pour détection, segmentation, pose et suivi — entraînement, export et inférence en quelques lignes ; le défaut productif de la détection d'objets, sous licence AGPL-3.0. — exemple officiel `yolo` du dépôt du SDK pour la pré-annotation en détection, et export au format YOLO.
- [[segment-anything]] — Code et poids officiels du Segment Anything Model de Meta — segmentation promptable zero-shot (points, boîtes, masques) sans réentraînement par classe ; la brique de référence pour pré-segmenter et annoter, prolongée par SAM 2 (vidéo) et SAM 3 (texte). — exemples officiels `segment_anything_model`, `segment_anything_2_image` et `segment_anything_2_video` : segmentation interactive à partir de points ou de boîtes.
- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs. — exemple officiel `spacy` pour pré-annoter des entités, et export au format spaCy.
- [[GLiNER]] — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger. — exemple officiel `gliner` : reconnaissance d'entités à zéro exemple, sans entraînement préalable sur les étiquettes du projet.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base recommandée en production (PostgreSQL 14 ou plus), là où SQLite suffit à l'essai.
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — mode d'installation documenté, avec PostgreSQL.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm documenté (une réplique, 1 Gio et 1 CPU demandés par défaut).

## Ressources

- Documentation — https://labelstud.io/guide
- Documentation — https://labelstud.io/guide/label_studio_compare
- Dépôt — https://github.com/HumanSignal/label-studio
- Dépôt — https://github.com/HumanSignal/label-studio-ml-backend

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[Annotation de données]] — la notion : types de tâches, guides, accord entre annotateurs, pré-annotation et ses biais, active learning, annotation sur site
- [[NER et étiquetage de séquence]] — le cas du texte, où l'outil sert à produire les spans IOB
