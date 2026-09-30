---
role: brique
nom: Celery
alias: [celery, Celery Beat, Flower]
pitch: "File de tâches distribuée pour Python : des workers exécutent des fonctions asynchrones postées sur un broker (RabbitMQ, Redis, SQS), avec relances, planification (Beat) et enchaînements (canvas) ; au moins une fois, BSD-3-Clause."
categorie: data/messagerie
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Temporal]]"]
complements: ["[[RabbitMQ]]", "[[Airflow]]", "[[FastAPI]]"]
tags: [task-queue, orchestration, distributed]
url_docs: https://docs.celeryq.dev/en/stable/
url_repo: https://github.com/celery/celery
---

# Celery

<!-- AUTO:BANDEAU:START -->
> File de tâches distribuée pour Python : des workers exécutent des fonctions asynchrones postées sur un broker (RabbitMQ, Redis, SQS), avec relances, planification (Beat) et enchaînements (canvas) ; au moins une fois, BSD-3-Clause.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de **file de tâches distribuée** pour Python. Une application déclare des fonctions
comme tâches (`@app.task`), les poste avec `.delay()` sur un **broker** de messages, et des
processus *workers*, lancés par `celery worker`, les exécutent. Celery n'est pas un broker : il
en emploie un. Autour de ce cœur : des relances (`retry`), des résultats stockés dans un
*backend*, la planification périodique par **Celery Beat**, et le *canvas* (`chain`, `group`,
`chord`) pour composer des tâches.

Relevé le 2026-09-30 : stable **5.6.3** du 2026-03-26 (Python 3.9 à 3.13), alpha 5.7.0a1 du
2026-09-22 (Python 3.10 minimum), BSD-3-Clause, environ 28 900 étoiles, dernier commit du
2026-09-30. Quatre versions stables en douze mois, aucune depuis six mois : le dépôt vit, le
rythme des versions ralentit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Sortir un travail long ou lourd d'une requête web : envoi d'e-mail, génération de rapport, entraînement ou inférence déclenchés par API | Le travail doit survivre à une panne avec état, attentes longues et reprise exacte : un moteur d'exécution durable ([[Temporal]]) |
| Un écosystème mûr — planification, relances, routage par files, `chord`, supervision avec Flower — en Python | Un graphe de tâches avec dépendances, backfill et suivi de bout en bout : un orchestrateur ([[Airflow]], [[Kestra]]) |
| Un broker déjà présent : [[RabbitMQ]], ou [[Redis]] (voir plus bas) | Du `async def` natif : Celery 5 n'exécute pas les tâches asynchrones (aucun calendrier annoncé, discussion #9049) ; voir les alternatives ci-dessous |
| Une application Django ou [[FastAPI]] : Django est supporté nativement, et la doc de FastAPI renvoie vers Celery dès que le travail devient lourd | Un besoin léger, sans routage ni planification : une table [[Postgres]] avec `SKIP LOCKED` peut suffire (voir la notion) |

## Mise en œuvre

- Installation — `pip install celery` ; extras par broker (`celery[redis]`, `celery[librabbitmq]`…) ; **Windows n'est plus supporté** depuis Celery 4 (faute de financement, dit le README)
- Point d'entrée — une instance `Celery("app", broker=…)`, des tâches décorées, `celery -A app worker`, et `celery -A app beat` pour la planification ; brokers : rabbitMQ et Redis (dont Sentinel) et SQS sont *stables* ; Zookeeper, Kafka et Google Pub/Sub sont *expérimentaux*. Backends de résultats : RPC, SQLAlchemy, Redis, Memcached, MongoDB, S3, système de fichiers… **RabbitMQ est le broker par défaut** de la doc. Le tableau officiel donne Redis pour « le transport rapide de petits messages » (les gros messages le congestionnent) et RabbitMQ pour les messages plus gros. [[Redis]] comme broker et comme backend de résultats est un montage courant ; `rpc://` sert de backend côté RabbitMQ
- Prérequis — un broker à exploiter ; un backend de résultats seulement si les résultats sont lus, obligatoire pour les `chord`
- Exécution — workers en processus (*prefork*), threads ou greenlets ; sur Kubernetes, un déploiement par file. Avec un CeleryExecutor, [[Airflow]] emploie Celery pour distribuer ses tâches, avec RabbitMQ, Redis ou Redis Sentinel ; supervision : **Flower** (BSD, environ 7 200 étoiles, 2.2.0 du 2026-09-22, classé *Beta* sur PyPI, intégration Prometheus et authentification OAuth) ; l'exporter communautaire `celery-exporter` (MIT, testé avec Redis et RabbitMQ) alimente Prometheus et Grafana
- Coût — gratuit ; l'exploitation d'un broker et de workers est le prix

## Licence et gouvernance

- **BSD-3-Clause**. Aucune édition payante.
- **Gouvernance communautaire** financée par Open Collective : environ 92 600 USD levés au total, solde de 5 100 USD, budget annuel estimé à 15 400 USD, quatre administrateurs. Sponsors cités par le README : Blacksmith, CloudAMQP, Upstash, Dragonfly ; Tidelift pour le support. Un mainteneur a écrit dans la discussion #9049 manquer de temps et de fonds.
- **Dépôts secondaires actifs** : kombu (5.6.2), billiard (4.3.0, 2026-09-17), amqp (5.4.0, 2026-09-19) ; vine (5.1.0, 2023) est stable.

## Limites à connaître

- **Livraison au moins une fois.** L'acquittement se fait par défaut *avant* l'exécution ; `acks_late` est désactivé par défaut, et l'ack survient même si le processus enfant est tué, sauf `task_reject_on_worker_lost`. Une tâche doit pouvoir être rejouée sans dommage (idempotence).
- **Redis : un piège documenté.** Un message non acquitté au bout du *visibility timeout* (une heure par défaut) est livré à un autre worker ; les tâches à ETA, `countdown` ou `retry` plus longues que ce délai sont exécutées « en boucle ». La doc demande aussi `maxmemory-policy noeviction` sur Redis.
- **Quorum queues de RabbitMQ** : supportées via `x-queue-type: quorum`, mais sans QoS global, donc pas d'autoscale, et les tâches à ETA bloquent le worker.
- **Beat ne doit tourner qu'en un exemplaire**, sinon les tâches partent en double ; les exécutions d'une même tâche périodique peuvent se chevaucher.
- **Le sérialiseur JSON gonfle les messages** sur les workflows complexes ; ne pas confier de gros objets au broker.
- **Pas d'`async def` natif en 5.x**, et aucune feuille de route pour Celery 6 trouvée en source primaire.

## Alternatives Python sans fiche

Aucune n'a la maturité ni l'écosystème de Celery ; **RQ** est la seule qui pèse vraiment. Relevé le 2026-09-30 (versions lues sur PyPI, étoiles sur GitHub) :

- **RQ** (10 696 étoiles, 2.12.0 du 2026-08-30, BSD-2-Clause) : Redis ou Valkey seuls, pas de routage ; sérialiseur `pickle` par défaut, jugé non sûr par sa doc.
- **Huey** (6 041 étoiles, 3.4.0 du 2026-09-04, MIT) : installation minimale, stockage SQLite ou fichier sans serveur.
- **Dramatiq** (5 317 étoiles, 2.2.1 du 2026-09-02, LGPL-3.0) : RabbitMQ ou Redis, asyncio documenté depuis 2.0.0 ; la licence est à examiner si le produit est redistribué.
- **arq** (3 013 étoiles, 0.28.0 du 2026-04-16, MIT) : en **mode maintenance** depuis le 2025-10-18 (annonce de Samuel Colvin, équipe Pydantic) — seules les failles critiques sont corrigées.
- **Taskiq** (2 345 étoiles, 0.13.0 du 2026-09-26, MIT) : asyncio natif, brokers RabbitMQ, Redis, NATS, SQS et Kafka par paquets séparés, injection de dépendances partagée avec FastAPI ; version 0.x, classé *Alpha* sur PyPI, un mainteneur principal.

## Écosystème

### Alternatives
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage. — la doc de Temporal présente sa *Standalone Activity* comme sa file de tâches (« durable retries, a Run ID you can cancel or query, and deduplication at submit time, without running a broker ») et écrit que les équipes qui quittent Celery, Sidekiq ou une file maison peuvent commencer par là ; l'exécution durable remplace le broker, au prix d'un serveur Temporal à exploiter.

### Compléments

- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — broker par défaut de la doc de Celery ; les quorum queues sont supportées (`x-queue-type: quorum`) mais sans QoS global, donc sans autoscale.
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le CeleryExecutor d'Airflow s'appuie sur Celery pour distribuer ses tâches, avec RabbitMQ, Redis ou Redis Sentinel comme broker.
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — la doc de FastAPI renvoie vers Celery pour le calcul lourd qui n'a pas à tourner dans le même processus.

## Ressources

- Documentation — https://docs.celeryq.dev/en/stable/
- Dépôt — https://github.com/celery/celery
- Documentation — https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html (brokers et backends)

## Voir aussi

- [[Messagerie]] — le hub du dossier
