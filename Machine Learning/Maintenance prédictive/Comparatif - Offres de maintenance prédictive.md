---
role: comparatif
nom: Comparatif - Offres de maintenance prédictive
categorie: ml/maintenance
tags: [predictive-maintenance, iiot]
---

# Comparatif - Offres de maintenance prédictive

> On tranche sur : l'auto-hébergement (le cas on-prem), la licence, la manière dont les données ressortent, et si l'offre est encore ouverte à un nouveau projet.

![[Comparatif - Offres de maintenance prédictive.base]]

## Ce qui départage

- [[Siemens Insights Hub]] — la seule plateforme d'IoT de la liste dont l'hébergement sur l'infrastructure du client est décrit (cloud privé local, logiciel géré par Siemens, sur Kubernetes) ; propriétaire, contrat non public ; son module Predict traite la prédiction et l'anomalie dans l'interface, pas dans une chaîne de ML que l'on maîtrise.
- [[Cognite Data Fusion]] — service cloud uniquement d'après la documentation consultée : un compte chez Cognite est requis. Son atout est l'**ouverture des données** : API REST, SDK Python Apache-2.0, OData, Grafana. À prendre quand les données sont dispersées dans un parc d'actifs et que l'on construit ses modèles soi-même ; hors cas on-prem strict.
- [[Seeq]] — le seul outil d'**analyse en libre-service** de la liste, installable sur site ou en cloud, qui se branche sur les historiens sans copier les données. Il ne remplace ni l'historien ni la chaîne d'entraînement ; propriétaire, sans édition gratuite.
- [[AVEVA PI System]] — **n'est pas une offre de machine learning** : c'est l'historien où se trouvent les mesures et la hiérarchie des équipements. Sur site, propriétaire, licence à paramètres. À citer parce que les autres offres s'y branchent, et que le produit d'AVEVA pour l'apprentissage est distinct.
- [[Amazon Lookout for Equipment]] — arrêt le 2026-10-07, fermé aux nouveaux clients depuis le 2025-10-07 : présent pour mémoire, pour migrer. Les données partaient dans un bucket S3 d'un compte AWS.
- [[Amazon Monitron]] — fermé aux nouveaux clients depuis le 2024-10-31, vente de matériel arrêtée en juillet 2025, aucune nouvelle fonctionnalité ; le service continue pour les clients existants. Mesures et analyse dans le cloud AWS ; export Kinesis ou S3.

On tranche d'abord sur l'**hébergement** : Seeq, AVEVA PI System et le cloud privé local de Siemens vivent chez le client ; Cognite et les deux services AWS exigent un compte chez l'éditeur. Les deux services AWS sortent de la course (arrêté ou fermé). La licence, elle, ne départage rien entre les six : toutes sont propriétaires. Elle sépare la liste entière d'une chaîne libre → [[Telegraf]], [[Node-RED]], [[Mosquitto]], [[InfluxDB]], plus les bibliothèques ([[scikit-survival]], [[tsfresh]], [[sktime]]).

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Maintenance prédictive]] — le dossier qui range les notions et le jeu de données du sujet.
- [[Maintenance prédictive et RUL]] — la notion qui cadre le sujet.
- [[Politique de maintenance et coût]] — le coût d'une offre se juge à la décision qu'elle outille.
- [[Comparatif - Brokers MQTT]] — le comparatif voisin pour la collecte d'atelier.
