---
role: brique
nom: Amazon Lookout for Equipment
alias: [AWS Lookout for Equipment, Lookout for Equipment]
pitch: "Service managé AWS de détection d'anomalies sur capteurs d'équipements industriels — un modèle entraîné sur l'historique de jusqu'à 300 capteurs, déposé dans S3, puis appliqué en temps réel — fermé aux nouveaux clients depuis le 2025-10-07 et arrêté le 2026-10-07."
categorie: ml/maintenance
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: deprecated
langage: 
alternatives: []
complements: []
tags: [predictive-maintenance, anomaly-detection, timeseries, condition-monitoring]
url_docs: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/what-is.html
url_repo: 
---

# Amazon Lookout for Equipment

<!-- AUTO:BANDEAU:START -->
> Service managé AWS de détection d'anomalies sur capteurs d'équipements industriels — un modèle entraîné sur l'historique de jusqu'à 300 capteurs, déposé dans S3, puis appliqué en temps réel — fermé aux nouveaux clients depuis le 2025-10-07 et arrêté le 2026-10-07.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Service d'apprentissage automatique d'AWS pour surveiller des équipements industriels : il
détecte un comportement anormal et signale des défaillances potentielles. Le principe,
d'après la documentation : déposer dans un bucket S3 l'historique des capteurs (issu d'un
historien de procédé, d'un système SCADA ou d'un autre système de surveillance), créer un
jeu de données, choisir les signaux de l'équipement, y ajouter si on les a les périodes de
pannes passées, entraîner un modèle (jusqu'à 300 capteurs dans un même modèle), puis le
lancer sur les nouvelles mesures en temps réel, par la console ou le SDK. Le service est
prévu pour des équipements fixes qui fonctionnent avec peu de variabilité de régime :
pompes, compresseurs, moteurs, machines CNC, turbines, échangeurs, chaudières, onduleurs.
**Arrêt le 2026-10-07** : après cette date, la console et les ressources ne sont plus
accessibles. Les nouveaux clients n'y avaient plus accès depuis le 2025-10-07. Cette page
existe pour un seul cas : un projet qui en dépend et doit migrer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lire une architecture existante qui l'appelle, pour savoir quoi remplacer (jeu de données S3, étiquettes de pannes, planificateur d'inférence) | **Arrêt le 2026-10-07** : aucun nouveau projet ne doit en dépendre |
| Retrouver le vocabulaire du service pour migrer | AWS recommande AWS IoT SiteWise, dont la détection d'anomalies multivariée (lancée en juillet 2025) prend en charge la modélisation de Lookout, avec un dépôt GitHub de scripts de migration ; sinon des solutions de la Solutions Library ou de partenaires AWS |
| | Détection sur site, sans compte cloud (cas on-prem) : le service ne s'y prêtait pas, les données partent dans un bucket S3 d'un compte AWS |
| | Régimes de fonctionnement variables : le service vise explicitement les équipements à variabilité limitée → [[Maintenance prédictive avec peu de pannes]], [[PyOD]] ou [[STUMPY]] en local |
| | Une bibliothèque locale pour garder la main sur le modèle → [[time-series-anomaly-detector]], [[Orion]], [[DeepOD]] |

## Mise en œuvre

- Installation — rien à installer ; plus de nouvelle ressource possible depuis le 2025-10-07
- Point d'entrée — console AWS et SDK : jeu de données, modèle, planificateur d'inférence
- Prérequis — un compte AWS déjà client avant la fermeture ; l'historique des capteurs déposé dans S3
- Exécution — managé, hébergé par AWS ; aucune exécution locale
- Coût — facturation à l'usage sur la page de tarification AWS (non relevée ici) ; sans objet après l'arrêt

## Écosystème

### Alternatives

- Aucune fichée : les alternatives à portée de main ne sont pas interchangeables. [[Amazon Monitron]] est l'autre service d'AWS pour la maintenance, mais il apporte ses propres capteurs ; [[Azure AI Anomaly Detector]] a connu le même sort (retrait le 2026-10-01).

## Ressources

- Documentation — https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/what-is.html
- Article — Préserver l'accès et explorer des alternatives (AWS, blog Machine Learning) : https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment

## Voir aussi

- [[Maintenance prédictive et RUL]] — le cadre dont le service est une offre commerciale
- [[Maintenance prédictive avec peu de pannes]] — le cas où l'historique d'entraînement manque d'étiquettes de pannes
- [[Time series anomaly detection]] — la notion de détection sur séries qu'il applique
- [[Anomalies multivariées par apprentissage profond]] — la famille de méthodes d'un modèle multicapteur
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres du dossier
