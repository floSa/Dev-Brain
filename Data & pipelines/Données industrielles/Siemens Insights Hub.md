---
role: brique
nom: Siemens Insights Hub
alias: [Insights Hub, MindSphere, Siemens MindSphere]
pitch: "Plateforme IoT industrielle de Siemens (ex-MindSphere) — collecte des données de machines, modèle d'actifs, tableaux de bord, applications low-code (Mendix) et module Predict de prévision et de détection d'anomalies ; en cloud public, en cloud privé virtuel ou en cloud privé local géré par Siemens."
categorie: data/industrie
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
alternatives: ["[[Cognite Data Fusion]]"]
complements: []
tags: [iiot, predictive-maintenance, timeseries, anomaly-detection]
url_docs: https://documentation.mindsphere.io/
url_repo: 
---

# Siemens Insights Hub

<!-- AUTO:BANDEAU:START -->
> Plateforme IoT industrielle de Siemens (ex-MindSphere) — collecte des données de machines, modèle d'actifs, tableaux de bord, applications low-code (Mendix) et module Predict de prévision et de détection d'anomalies ; en cloud public, en cloud privé virtuel ou en cloud privé local géré par Siemens.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme | propriétaire | auto-hébergeable ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'IoT industriel de Siemens, issue de MindSphere : la page de Siemens écrit que
« MindSphere has evolved into Insights Hub ». Elle relie des machines à un cloud, organise
leurs données en actifs, aspects et variables, et sert des applications au-dessus :
surveillance et visualisation, santé des actifs, suivi du rendement global (OEE), et des
applications construites avec Mendix. Le module **Predict** fait tourner un moteur de
prédiction ou de détection d'anomalies sur les séries temporelles des variables d'un actif,
selon un calendrier, et réécrit le résultat dans l'actif pour le réutiliser dans les règles,
les événements et les tableaux de bord (manuel Predict, 07/2026). Trois modes de déploiement
sont décrits : cloud public (AWS et Azure), cloud privé virtuel chez le client sur AWS ou
Azure, et **cloud privé local** sur l'infrastructure du client, où le logiciel reste géré par
Siemens et s'appuie sur Kubernetes (déploiement Rancher).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un parc de machines Siemens à relier à une plateforme unique, avec le support du même éditeur | Aucune brique libre sous le capot : propriétaire, contrat et tarifs non publics dans les pages consultées |
| Garder les données derrière le pare-feu : le cloud privé local les stocke sur site, pour des exigences de réglementation ou de résidence | Le cloud privé local reste une offre gérée par l'éditeur sur une infrastructure que le client fournit : la mise à jour passe par le support Siemens (avis CISA : « contacter le support pour les correctifs ») |
| Poser la prédiction et l'anomalie dans la même interface que les tableaux de bord et les règles | Le module Predict est un moteur à configurer : pour maîtriser le modèle, les features et la validation, chaîne libre → [[Telegraf]], [[Mosquitto]], [[asyncua]], [[InfluxDB]] |
| Construire des applications d'atelier en low-code | Besoin de lire et d'écrire les données par des API ouvertes standard : vérifier les droits d'export avant de s'engager (non établi ici) |

## Mise en œuvre

- Installation — cloud public : abonnement ; cloud privé virtuel ou local : déploiement coordonné avec Siemens
- Point d'entrée — portail web et API de la plateforme ; applications Mendix ; module Predict
- Prérequis — cloud privé local : une infrastructure Kubernetes (Rancher) fournie et exploitée par le client ; pour la connectivité des machines, la FAQ renvoie à une section « Connectivity » que les pages consultées ne détaillent pas → [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] pour les protocoles d'atelier
- Exécution — public : managé par Siemens sur AWS ou Azure ; privé : sur l'infrastructure du client, logiciel géré par Siemens
- Coût — propriétaire, licence sur contrat ; aucun tarif relevé

## Écosystème

### Alternatives

- [[Cognite Data Fusion]] — Plateforme de données industrielles de Cognite — modèle de données en graphe, extracteurs (OPC UA, PostgreSQL), contextualisation et API REST avec SDK Python ouvert ; service cloud, sans offre sur site décrite dans la documentation consultée.

## Ressources

- Documentation — https://documentation.mindsphere.io/
- Article — FAQ Insights Hub : https://www.siemens.com/en-us/products/insights-hub/resources/faq/
- Article — Avis CISA sur Insights Hub Private Cloud : https://www.cisa.gov/news-events/ics-advisories/icsa-25-100-05

## Voir aussi

- [[Données industrielles]] — le hub du dossier
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — les protocoles par lesquels les machines arrivent à la plateforme
- [[Maintenance prédictive et RUL]] — le cadre de pronostic auquel son module Predict s'adresse
- [[Time series anomaly detection]] — la notion de détection sur séries que Predict applique
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres, dont l'auto-hébergement
