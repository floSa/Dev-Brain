---
role: brique
nom: AVEVA PI System
alias: [PI System, PI Server, PI Data Archive, AVEVA PI Server]
pitch: "Historien industriel d'AVEVA — PI Data Archive stocke les séries temporelles de l'atelier, PI Asset Framework les rattache à une hiérarchie d'équipements, PI Vision les affiche ; propriétaire, installé sur site (datasheet : Windows) ; un historien, pas un outil de machine learning."
categorie: database/series-temporelles
famille: plateforme
licence_type: proprietary
hosted: [self]
maturite: production
langage: 
alternatives: ["[[InfluxDB]]", "[[TimescaleDB]]"]
complements: ["[[Seeq]]"]
tags: [timeseries, iiot, predictive-maintenance, self-hosted]
url_docs: https://docs.aveva.com/
url_repo: 
---

# AVEVA PI System

<!-- AUTO:BANDEAU:START -->
> Historien industriel d'AVEVA — PI Data Archive stocke les séries temporelles de l'atelier, PI Asset Framework les rattache à une hiérarchie d'équipements, PI Vision les affiche ; propriétaire, installé sur site (datasheet : Windows) ; un historien, pas un outil de machine learning.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme | propriétaire | self-hébergé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Suite d'AVEVA qui joue le rôle d'**historien** : l'infrastructure où aboutissent, année après
année, les mesures des automates et des capteurs d'un site. Trois pièces comptent pour la
maintenance. **PI Data Archive** est le moteur de séries temporelles, qui archive et sert les
mesures. **PI Asset Framework** est la couche de métadonnées orientée objet : équipement,
actif, élément, attribut, rattaché à un point de mesure ; ses modèles garantissent la cohérence
entre milliers de capteurs et portent des calculs en flux (Asset Analytics) et des
événements (Event Frames) qui repèrent des périodes remarquables. **PI Vision** est le client
web de visualisation. Les données se lisent par PI Web API (authentification de base,
Kerberos ou jeton) ou par les services de données CONNECT d'AVEVA, côté cloud. Le
datasheet de PI Server (édition 23-09) annonce Windows et Windows Core ; plusieurs Data Archive peuvent former une collective, pour la
haute disponibilité et la reprise après sinistre. La licence est un fichier qui encode le type
de licence, le système d'exploitation, la haute disponibilité, une limite de flux de données et
les modules ajoutés.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le site a déjà un PI System : c'est le lieu où se trouvent l'historique des capteurs et la hiérarchie des équipements, donc la matière première d'un projet de maintenance | Ce n'est **pas** un outil de machine learning : l'apprentissage vient d'ailleurs. AVEVA vend pour cela un produit distinct, AVEVA Predictive Analytics, branché sur le PI System (sensor fault, anomalie, diagnostic, délai avant panne) |
| Un historien sur site, propriétaire et supporté, pour un industriel qui l'exige | Un historien neuf sans contrainte d'éditeur → [[InfluxDB]] ou [[TimescaleDB]], libres et administrables sans fichier de licence |
| Lire l'historique par API pour entraîner ses propres modèles : PI Web API est un point d'entrée REST | Parc sans Windows : le datasheet de PI Server (23-09) annonce Windows ; vérifier les systèmes pris en charge de la version visée (les adaptateurs AVEVA, eux, tournent sous Linux et Windows) |
| Rattacher les modèles aux équipements par l'Asset Framework plutôt que par des noms de tags | Coût : licence propriétaire à paramètres (flux de données, haute disponibilité, modules) ; aucun tarif relevé |

## Mise en œuvre

- Installation — installateur AVEVA, fichier de licence obtenu auprès d'AVEVA
- Point d'entrée — PI Web API (REST), PI Vision (web), Asset Framework pour le modèle d'équipements
- Prérequis — Windows ou Windows Core d'après le datasheet 23-09 ; interfaces ou adaptateurs vers les automates (OPC UA et autres) → [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]]
- Exécution — sur site, mono-serveur ou en collective de plusieurs Data Archive
- Coût — propriétaire, licence AVEVA ; aucun tarif relevé

## Écosystème

### Alternatives

- [[InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.
- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

### Compléments

- [[Seeq]] — Application d'analyse en libre-service de séries temporelles de procédé — se branche sur des historiens dont PI System, sans copier les données ; installable sur site ou en cloud, propriétaire.

## Ressources

- Documentation — https://docs.aveva.com/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases temporelles]] — ce qui départage les moteurs du dossier
- [[Données industrielles]] — la chaîne qui amène la donnée d'atelier jusqu'à lui
- [[Surveillance conditionnelle et modes de défaillance]] — l'usage de ses données en maintenance
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres, dont l'auto-hébergement
