---
role: brique
nom: Cognite Data Fusion
alias: [CDF, Cognite, Cognite Data Fusion CDF]
pitch: "Plateforme de données industrielles de Cognite — modèle de données en graphe, extracteurs (OPC UA, PostgreSQL), contextualisation et API REST avec SDK Python ouvert ; service cloud, sans offre sur site décrite dans la documentation consultée."
categorie: data/industrie
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
alternatives: ["[[Siemens Insights Hub]]"]
complements: []
tags: [iiot, timeseries, predictive-maintenance, knowledge-graph]
url_docs: https://docs.cognite.com/cdf
url_repo: 
---

# Cognite Data Fusion

<!-- AUTO:BANDEAU:START -->
> Plateforme de données industrielles de Cognite — modèle de données en graphe, extracteurs (OPC UA, PostgreSQL), contextualisation et API REST avec SDK Python ouvert ; service cloud, sans offre sur site décrite dans la documentation consultée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de données industrielles (DataOps) de Cognite. La documentation la décrit en
couches : des **extracteurs** qui lisent des sources informatiques et d'automatisme par des
protocoles standards comme PostgreSQL et OPC UA ; une zone de transformation ; un
**graphe de connaissances** structuré par des modèles de données fournis d'office ; des outils de **contextualisation** qui combinent IA, apprentissage
et expertise métier pour relier ces données entre elles. Tout sort par une API REST et des
SDK (Python, JavaScript, Spark), des connecteurs OData pour Excel et Power BI et une intégration
Grafana ; un service de fonctions héberge du code Python. La plateforme « tourne dans le
cloud » chez un fournisseur public, en locataire partagé ou en cluster dédié. Le SDK Python
est ouvert (licence Apache-2.0) ; la plateforme, elle, est propriétaire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un grand parc d'actifs dont les données sont dispersées (historiens, GMAO, documents) et à rattacher à un même modèle d'actifs | **Pas d'hébergement sur site décrit** dans la documentation consultée : un compte chez Cognite est requis, et les données quittent l'atelier → hors cas on-prem strict |
| Lire les données par API standard (REST, SDK Python, OData, Grafana) plutôt que par une interface propriétaire | Une chaîne légère sur une seule ligne : la plateforme vise des sources nombreuses à relier entre elles |
| Construire des modèles de maintenance en Python sur des données déjà contextualisées | Besoin d'un modèle de maintenance prêt à l'emploi : la plateforme fournit les données et l'outillage, pas un détecteur clé en main |
| | Chaîne libre qui reste chez soi → [[asyncua]], [[Telegraf]], [[InfluxDB]] ou [[TimescaleDB]] |

## Mise en œuvre

- Installation — projet ouvert par Cognite chez un fournisseur cloud ; extracteurs à exécuter côté source
- Point d'entrée — API REST et SDK Python (`cognite-sdk`), connecteurs OData et Grafana
- Prérequis — un contrat Cognite ; l'accès réseau de l'atelier vers le cloud ; les sources d'automatisme à relier par OPC UA ou SQL
- Exécution — managé par Cognite, sur Azure ou Google Cloud (pages partenaires de Cognite) ; locataire partagé ou cluster dédié
- Coût — propriétaire, contrat ; aucun tarif relevé

## Écosystème

### Alternatives

- [[Siemens Insights Hub]] — Plateforme IoT industrielle de Siemens (ex-MindSphere) — collecte des données de machines, modèle d'actifs, tableaux de bord, applications low-code (Mendix) et module Predict de prévision et de détection d'anomalies ; en cloud public, en cloud privé virtuel ou en cloud privé local géré par Siemens.

## Ressources

- Documentation — https://docs.cognite.com/cdf
- Documentation — SDK Python ouvert (Apache-2.0) : https://github.com/cognitedata/cognite-sdk-python

## Voir aussi

- [[Données industrielles]] — le hub du dossier
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — les protocoles que ses extracteurs parlent
- [[Maintenance prédictive et RUL]] — le cadre de pronostic que ces données alimentent
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres, dont l'auto-hébergement
