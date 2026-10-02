---
role: brique
nom: Amazon Monitron
alias: [AWS Monitron, Monitron]
pitch: "Système AWS de surveillance conditionnelle livré de bout en bout — capteurs de vibration et de température, passerelle, analyse dans le cloud AWS (seuils ISO 20816 et modèles d'apprentissage) et application mobile — fermé aux nouveaux clients depuis le 2024-10-31, sans nouvelle fonctionnalité."
categorie: ml/maintenance
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: deprecated
langage: 
alternatives: []
complements: []
tags: [predictive-maintenance, condition-monitoring, iiot, timeseries]
url_docs: https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html
url_repo: 
---

# Amazon Monitron

<!-- AUTO:BANDEAU:START -->
> Système AWS de surveillance conditionnelle livré de bout en bout — capteurs de vibration et de température, passerelle, analyse dans le cloud AWS (seuils ISO 20816 et modèles d'apprentissage) et application mobile — fermé aux nouveaux clients depuis le 2024-10-31, sans nouvelle fonctionnalité.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de surveillance conditionnelle vendu avec son matériel. Des capteurs se fixent sur
la machine (jusqu'à 20 par actif) et mesurent vibration et température ; une passerelle,
branchée sur le Wi-Fi ou en Ethernet, transmet les mesures au cloud AWS ; l'analyse y
compare les signaux aux seuils de la norme ISO 20816 et à des modèles d'apprentissage, puis
notifie les techniciens dans une application mobile ou web (états sain, avertissement,
alarme, maintenance). Les techniciens y saisissent un retour sur chaque alerte, dont le
système dit tirer parti pour s'améliorer. Cibles citées : roulements, moteurs, réducteurs,
pompes. Les données s'exportent par Kinesis ou vers S3. **Statut** : fermé aux nouveaux
clients depuis le 2024-10-31 ; les clients existants (un capteur mis en service dans les
30 jours précédant cette date) continuent à l'utiliser ; la vente de matériel s'est arrêtée
en juillet 2025 ; AWS maintient la sécurité et la disponibilité mais n'ajoute aucune
fonctionnalité.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exploiter un parc Monitron déjà en service : le service continue pour les clients existants, la garantie de cinq ans du matériel est honorée | **Fermé aux nouveaux clients depuis le 2024-10-31**, plus de matériel vendu depuis juillet 2025 : aucun nouveau projet |
| Récupérer les mesures d'un parc existant pour les analyser ailleurs (export Kinesis ou S3) | Mesures et analyse partent dans le cloud AWS : pas d'usage sur un site coupé d'Internet ni sous contrainte de données sur site (cas on-prem) |
| Comprendre l'architecture type d'un système prêt à l'emploi, pour la comparer à une chaîne maison | Maîtriser les features et le modèle : l'analyse est une boîte fermée, seuils ISO 20816 et modèle propriétaire → [[Analyse vibratoire]] et [[Indicateurs de santé]] pour reconstruire les descripteurs soi-même |
| | AWS renvoie vers des partenaires de sa place de marché (Tactical Edge, IndustrAI, Factory AI) ; chaîne libre sur site → [[Telegraf]], [[Mosquitto]], [[InfluxDB]] |

## Mise en œuvre

- Installation — plus de nouvelle ressource possible ; matériel : capteurs fixés sur la machine, passerelle sur prise secteur
- Point d'entrée — console AWS (projet, gestion des utilisateurs) ; application mobile et web pour la surveillance
- Prérequis — un projet Monitron ouvert avant le 2024-10-31 ; réseau Wi-Fi ou Ethernet pour la passerelle
- Exécution — managé, hébergé par AWS ; le matériel est la seule part sur site
- Coût — achat du matériel, plus un abonnement par capteur en service (documentation AWS) ; tarifs non relevés ici

## Écosystème

### Alternatives

- Aucune fichée : [[Amazon Lookout for Equipment]] est l'autre service AWS de maintenance, mais il ne fournit pas de capteurs et il a été arrêté le 2026-10-07.

## Ressources

- Documentation — https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html
- Article — Maintenir l'accès et envisager des alternatives pour Amazon Monitron (AWS, blog Machine Learning) : https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron

## Voir aussi

- [[Surveillance conditionnelle et modes de défaillance]] — le cadre, et les normes de vibration dont l'ISO 20816
- [[Analyse vibratoire]] — les descripteurs que le système calcule à la place de l'utilisateur
- [[Diagnostic de défauts de roulements]] — l'étape suivante d'une alarme sur un roulement
- [[Maintenance prédictive et RUL]] — le cadre de pronostic
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres du dossier
