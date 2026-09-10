---
role: brique
nom: DataRobot
alias: [datarobot]
pitch: "Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée."
categorie: ml/plateforme
famille: plateforme
domaines: [data-sci, mlops]
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Dataiku]]", "[[AWS SageMaker]]", "[[Google Cloud Vertex AI]]", "[[Microsoft Azure Machine Learning]]"]
complements: []
tags: [ml-platform, automl, model-monitoring, model-registry, data-governance, kubernetes]
url_docs: https://docs.datarobot.com/
url_repo: 
---

# DataRobot

<!-- AUTO:BANDEAU:START -->
> Plateforme d'AutoML et de MLOps : elle entraîne et classe des dizaines de modèles candidats, puis déploie et surveille celui qu'on retient ; auto-hébergeable sur Kubernetes ou managée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme | propriétaire | self-hébergé ou managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme dont le cœur est l'**automatisation de la modélisation** : on lui donne un jeu de
données et une cible, elle construit et entraîne un grand nombre de modèles candidats, les
classe sur une métrique, et présente le meilleur avec ses explications. La seconde moitié du
produit est le MLOps : registre, déploiement en endpoint, surveillance de la dérive et de la
performance, réentraînement. L'édition *Self-Managed AI Platform* s'installe sur un cluster
Kubernetes chez le client, par Helm, avec haute disponibilité et reprise documentées ; une
édition managée existe en parallèle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Beaucoup de problèmes supervisés tabulaires à traiter vite, avec peu de data scientists | L'automatisation **cache le modèle** : ce qui est gagné en vitesse se paie en compréhension de ce qui a été appris |
| Les données ne doivent pas quitter le site, et le client dispose d'un Kubernetes | Le périmètre est **plus étroit qu'une plateforme généraliste** : ce n'est pas l'outil pour préparer des données ni construire des pipelines de bout en bout |
| La surveillance des modèles en production est exigée dès le départ | Un problème unique, bien cadré, qu'un modèle écrit à la main traite mieux → [[Scikit-Learn]] puis [[XGBoost]] |
| Il faut présenter au métier une comparaison de modèles justifiée et documentée | Une équipe qui veut maîtriser l'architecture de ses modèles → [[Comparatif - Orchestrateurs ML]] pour assembler soi-même |
| L'organisation veut de l'explicabilité intégrée plutôt qu'à outiller | Un besoin de deep learning sur images ou texte, hors du tabulaire → [[Apprentissage profond]] |

## Mise en œuvre

- Installation — chart Helm sur un cluster Kubernetes pour l'édition self-managed ; souscription pour l'édition managée
- Point d'entrée — l'interface web : jeu de données, cible, puis la liste classée des modèles candidats ; API et client Python pour l'automatisation
- Prérequis — un cluster Kubernetes dimensionné, avec ses workers de modélisation et ses serveurs de prédiction
- Exécution — self-hébergé ou managé ; distribué sur le cluster
- Coût — licence commerciale ; le coût d'exploitation du cluster s'y ajoute en self-managed

## Écosystème

### Alternatives

- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — même liberté d'hébergement, périmètre plus large, automatisation moins poussée.
- [[AWS SageMaker]] — Écosystème ML natif d'AWS : notebooks, entraînement distribué, réglage, registre et endpoints d'inférence managés, réunis avec les services data d'AWS sous SageMaker Unified Studio ; descend sur site par Outposts. — son Autopilot couvre le même terrain, sans la couche métier.
- [[Google Cloud Vertex AI]] — Écosystème ML natif de Google Cloud : entraînement, registre, pipelines et endpoints managés, plus l'accès aux modèles Gemini ; une partie seulement descend sur site, sur l'appliance air-gapped de Google Distributed Cloud. — son AutoML joue le même rôle, chez Google.
- [[Microsoft Azure Machine Learning]] — Écosystème ML natif d'Azure : espaces de travail, entraînement, registre et endpoints managés, pilotables en SDK Python ou en YAML ; seul des trois clouds à faire tourner entraînement et inférence sur un Kubernetes déjà en place, par Azure Arc. — son AutoML joue le même rôle, chez Microsoft.

## Ressources

- Documentation — https://docs.datarobot.com/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Monitoring de modèle en production]] — ce que sa moitié MLOps automatise
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
