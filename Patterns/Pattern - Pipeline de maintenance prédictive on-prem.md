---
role: pattern
contexte: Surveiller l'état de machines d'atelier sur site, sans cloud — des variables lues sur des serveurs OPC UA, relayées par un broker MQTT, stockées en séries, scorées par un modèle, puis transformées en alerte qu'une équipe de maintenance sait traiter.
services_cles: [asyncua, open62541, Telegraf, Node-RED, Mosquitto, EMQX, InfluxDB, TimescaleDB, Grafana, Alertmanager]
projets_appliques: []
tags: [pattern, predictive-maintenance, iiot, opc-ua, mqtt, anomaly-detection]
---

# Pattern — Pipeline de maintenance prédictive on-prem

## Contexte

Une machine d'atelier expose ses variables (température, courant, vibration, compteurs) par un serveur OPC UA ou par un automate. Le client demande de l'alerte, pas un tableau de bord de plus. La donnée ne sort pas de l'usine, le réseau d'atelier est séparé du réseau bureautique, et personne n'exploitera un cluster.

La chaîne a six étages, et chacun se remplace sans toucher les autres :

```
serveur OPC UA → collecte → broker MQTT → base de séries → modèle → alerte
```

À appliquer quand trois conditions tiennent : des capteurs lisibles, un historique que l'on peut conserver, et une personne désignée pour recevoir l'alerte. Sans la troisième, la chaîne produit des graphiques que personne ne regarde ([[Politique de maintenance et coût]]). Le cadre conceptuel — modes de défaillance, courbe P-F, indicateurs de santé — est dans [[Surveillance conditionnelle et modes de défaillance]] et [[Maintenance prédictive et RUL]] ; les protocoles de l'atelier, dans [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]].

## Stack

| Étage | Brique | Quand la prendre |
|---|---|---|
| Source | serveur OPC UA de la machine | rien à choisir : c'est ce que le constructeur livre |
| Client OPC UA | [[asyncua]] (Python), [[open62541]] (C) | seulement si la collecte est du code ; sinon l'étage suivant le fait déjà |
| Collecte | [[Telegraf]] | collecter par fichier de configuration, sans code, depuis OPC UA, Modbus, S7 ou MQTT |
| Collecte | [[Node-RED]] | l'équipe d'automatisme doit lire et modifier le flux elle-même |
| Broker | [[Mosquitto]] | un seul nœud, matériel modeste, pas de cluster |
| Broker | [[EMQX]] | cluster, règles, intégrations ; licence BSL 1.1, cluster payant |
| Base de séries | [[InfluxDB]], [[TimescaleDB]] | selon que le reste de l'infrastructure parle Influx ou SQL |
| Historien existant | [[AVEVA PI System]] | l'usine en a déjà un : lire dedans plutôt que dupliquer |
| Modèle | les notions du dossier [[Détection d'anomalies]] et [[Maintenance prédictive]] | voir la décision 5 |
| Alerte | [[Alertmanager]], ou l'alerting intégré de [[Grafana]] | regrouper, dédoublonner, router vers une personne |

Le comparatif des brokers est [[Comparatif - Brokers MQTT]].

## Décisions clés

### 1. Collecter par configuration avant de coder

- [[Telegraf]] couvre `inputs.opcua` (interrogation périodique), `inputs.opcua_listener` (abonnements), `inputs.modbus` et `inputs.s7comm`. Un binaire, un fichier TOML, aucune dépendance à installer sur le PC industriel.
- [[Node-RED]] se justifie quand le flux doit être lisible par des automaticiens, ou quand une logique d'aiguillage est nécessaire. Les nœuds OPC UA et Modbus sont communautaires et non revus ; l'éditeur est ouvert par défaut.
- [[asyncua]] se justifie quand la collecte appelle des méthodes OPC UA ou lit de l'historique, et qu'elle est déjà du Python.

### 2. Un broker entre la collecte et la base

- Le broker découple : la base n'est plus la seule consommatrice. Le modèle, un tableau de bord et un autre site s'abonnent au même flux, sans retoucher la collecte.
- Un nœud suffit tant qu'une panne du broker est tolérée quelques minutes. [[Mosquitto]] n'a pas de clustering ; [[EMQX]] en a un, mais sous BSL 1.1 le cluster exige une licence commerciale. Cette ligne se lit avant de promettre de la haute disponibilité à un client.
- Un étage de moins est aussi une option : [[Telegraf]] écrit directement dans la base. Le broker se garde quand plusieurs consommateurs existent, pas par principe.

### 3. Tenir la coupure réseau

- Le tampon de [[Telegraf]] est en mémoire par défaut (10 000 métriques, les plus anciennes écrasées) ; le tampon sur disque existe mais est encore décrit comme expérimental. Pour un atelier dont le réseau tombe, c'est la limite qui décide.
- Placer la collecte au plus près de la machine et le broker sur le même segment réduit la fenêtre de perte. Tester la coupure : débrancher, attendre, rebrancher, compter ce qui manque.

### 4. Stocker le brut, et stocker le score

- La base garde les mesures brutes à leur cadence d'origine, avec une rétention définie par la durée des phénomènes à voir (une dégradation de plusieurs semaines n'est pas lisible dans trois jours d'historique).
- Le modèle réécrit son **score** dans la même base, sous un nom de mesure distinct. Sans cela, impossible de rejouer l'évaluation ou de retoucher le seuil sans la machine ([[Détection d'anomalies en ligne]], rubrique « En pratique »).

### 5. Le modèle vient après le plus simple

- Un modèle appris n'est pas le premier étage. Les règles et le SPC d'abord, l'apprentissage ensuite : [[Pattern - Détection d'anomalies en deux étages]] et [[Contrôle statistique de procédé (SPC)]].
- Peu ou pas de pannes dans l'historique : détection d'anomalies non supervisée sur du normal vérifié ([[Rule - Entraîner sur du normal vérifié]]), pas une RUL ([[Maintenance prédictive avec peu de pannes]]).
- Un indicateur de santé construit sur plusieurs capteurs simplifie la décision ([[Indicateurs de santé]]) ; les briques de séries, [[STUMPY]], [[PyOD]], [[River]] et [[darts]], sont dans le dossier [[Détection d'anomalies]] et dans [[Séries temporelles]].
- Un modèle livré en bord d'usine pose ses propres contraintes de matériel et de mise à jour : [[Inférence en bordure - modèles sur du matériel d'atelier]].

### 6. Du score à l'alerte, avec un budget

- Fixer d'abord le nombre d'alertes par jour que l'équipe peut traiter, puis le seuil ([[Score et seuil d'alerte]]). Regrouper les alertes consécutives en un événement avant de les envoyer.
- Chiffrer le coût d'une intervention inutile contre celui d'une panne subie ([[Politique de maintenance et coût]]).
- Évaluer par événement, pas par point : [[Rule - Évaluer une anomalie par événement, pas par point]].
- Une alerte nomme une machine, un indicateur et un horizon, pas seulement « anomalie détectée ».

### 7. Sécuriser chaque étage

- OPC UA chiffré : le README de `inputs.opcua` de [[Telegraf]] liste `Basic256Sha256` comme politique la plus forte ; sans certificat configuré, un certificat auto-signé temporaire est créé à chaque démarrage et le serveur doit le ré-autoriser. [[open62541]] propose des politiques plus récentes.
- Compte de lecture seule côté serveur OPC UA : la collecte ne doit jamais pouvoir écrire dans l'automate.
- Éditeur de [[Node-RED]] protégé (`adminAuth`) ; broker avec TLS et ACL.

## Pièges

- **Réécrire la collecte en Python par réflexe** : un fichier de configuration se relit et se versionne mieux qu'un script maison.
- **Un broker en cluster promis sans avoir lu la licence** ([[EMQX]]).
- **Tampon en mémoire pris pour une garantie** : un redémarrage ou un tampon plein perd des mesures sans erreur.
- **Entraîner sur l'historique brut** : il contient déjà des pannes et des arrêts de maintenance ; le modèle les apprend comme normaux.
- **Seuil réglé sur un jeu public** puis posé tel quel sur une machine réelle.
- **Mesurer le modèle en exactitude point à point** alors que la maintenance traite des événements.
- **Alerte sans destinataire** : la chaîne est terminée techniquement et n'a aucun effet.
- **Cardinalité non examinée** : la fiche de [[Telegraf]] note qu'aucune page lue ne traite la cardinalité des tags, et qu'avec `outputs.postgresql` un tag ou un champ nouveau ajoute des colonnes. À mesurer sur la base choisie avant de nommer des tags à valeurs libres.

## Voir aussi

- [[Données industrielles]] — le hub du dossier des briques de collecte
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — OPC UA, MQTT et Modbus, Sparkplug B, sécurité d'un réseau d'atelier
- [[Comparatif - Brokers MQTT]] — choisir le broker
- [[Maintenance prédictive et RUL]] — la notion qui cadre le sujet
- [[Pattern - Détection d'anomalies en deux étages]] — règles et SPC d'abord, apprentissage ensuite
- [[Pattern - Inspection visuelle en ligne de production]] — la même idée côté caméra
- [[Rule - Entraîner sur du normal vérifié]], [[Rule - Évaluer une anomalie par événement, pas par point]]
