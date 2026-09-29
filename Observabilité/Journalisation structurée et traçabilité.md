---
role: notion
nom: Journalisation structurée et traçabilité
alias: [logs structurés, structured logging, logging Python, structlog, loguru, identifiant de corrélation, correlation id, canonical log lines, wide events, journalisation, syslog]
categorie: observability/supervision
domaines: [infra-ops, mlops]
tags: [observability, logging, tracing]
---

# Journalisation structurée et traçabilité

## Aperçu

- Un log est un événement daté. Il s'écrit en **ligne de texte** pour un humain, ou en **événement structuré** (des paires clé-valeur, le plus souvent en JSON) pour une machine. Dès que plusieurs requêtes s'entremêlent, la ligne de texte ne permet plus de retrouver « tout ce qui concerne cette requête » ; l'événement structuré, si.
- Cette page traite de ce qu'il y a **avant** l'outil de stockage : comment écrire l'événement, comment lui donner un contexte, comment le relier à une trace, ce qu'il ne doit jamais contenir, ce qu'il coûte. Le rôle du log face aux métriques et aux traces est dans [[Métriques, logs et traces]], non répété ici.
- La consigne de départ est celle de la méthode Twelve-Factor (facteur XI) : l'application écrit son flux d'événements sur la sortie standard, sans tampon, et **ne s'occupe ni de son routage ni de son stockage** ; c'est l'environnement d'exécution qui capture et route.
- Les bibliothèques Python citées — `logging`, structlog, Loguru — se comparent ici sans trancher. Structlog et Loguru n'ont pas de fiche dans le brain.

## Concepts clés

### Texte ou événement structuré

- La méthode Twelve-Factor décrit les logs comme un flux d'événements ordonnés dans le temps, un par ligne en brut ; la page date de 2017 et **ne dit rien du JSON**.
- Le cookbook de `logging` ne fournit pas de formateur JSON complet : il montre une classe qui sérialise un message en `message >>> {json}` et un encodeur JSON personnalisé pour les types non sérialisables. Un formateur complet vient d'une bibliothèque ou s'écrit soi-même.
- L'ANSSI (guide ANSSI-PA-012, v2.0 du 2022-01-28) demande un format **interprétable** : lisible par un humain et structuré pour l'analyse automatique, avec des champs fixes à la grammaire bien définie, et un champ « version » pour signaler un changement de syntaxe.
- La structure n'est pas nouvelle : la RFC 5424 (syslog, mars 2009, qui remplace la RFC 3164) définit déjà un champ `STRUCTURED-DATA` fait d'éléments `[SD-ID NOM="valeur"]`, avec échappement de `"`, `\` et `]`.
- **logfmt** (`clé=valeur`) est le compromis que Brandur Leach choisit en 2016 entre lisibilité humaine et lisibilité machine. Choisir entre JSON et logfmt est un arbitrage de rédaction : le JSON gagne dès que les valeurs sont imbriquées ou que le collecteur l'attend.

### Les niveaux, et trois échelles qui ne se recouvrent pas

- **Python** : NOTSET 0, DEBUG 10, INFO 20, WARNING 30, ERROR 40, CRITICAL 50 ; niveau par défaut WARNING.
- **Syslog** (RFC 5424) : de 0 (urgence) à 7 (debug) ; la priorité est `facilité × 8 + sévérité`. Le plus petit est le **plus grave**, à l'inverse de Python.
- **OpenTelemetry** : `SeverityNumber` de 1 à 24 en six tranches de quatre (TRACE 1-4, DEBUG 5-8, INFO 9-12, WARN 13-16, ERROR 17-20, FATAL 21-24), 0 pour « non spécifié » ; `SeverityText` garde la chaîne d'origine ; à partir de 17, la situation est erronée.
- La table de correspondance du modèle de données OpenTelemetry couvre Syslog, Log4j, Zap et d'autres, **sans colonne Python** : la conversion revient au pont d'export.
- Aucune source primaire n'a été lue sur le bon niveau à garder **en production**. Le seul constat vérifié : un niveau trop bas fait suivre le volume au trafic (voir la section sur le coût).

### Le modèle de `logging`

- Un `Logger` est l'interface de l'application, un `Handler` envoie vers une destination, un `Formatter` produit la chaîne, un `LogRecord` porte l'événement. Les loggers forment une **hiérarchie par noms pointés** ; `getLogger(__name__)` la fait suivre celle des paquets.
- `propagate` vaut vrai par défaut. Un handler posé sur un logger **et** sur l'un de ses ancêtres émet l'enregistrement plusieurs fois (la documentation décrit ce cas). Une **bibliothèque** n'attache qu'un `NullHandler` et ne logue jamais sur le root ; la configuration est l'affaire de l'application.
- Le formatage des arguments est **différé** : `logger.info("%s a échoué", nom)` ne construit le message que si le niveau passe. La documentation propose `isEnabledFor()` quand le calcul des arguments est lui-même coûteux. Aucune des trois pages lues ne met en garde contre les f-strings : l'argument défendable est celui du formatage différé, pas une consigne officielle.
- `dictConfig` : clé `version` (seule valeur valide : 1) ; **`disable_existing_loggers` vaut vrai par défaut**, ce qui coupe les loggers déjà créés par les bibliothèques ; `'()'` désigne une fabrique appelable. `logging.config.listen()` passe par `eval()` : un risque d'exécution de code, que son argument `verify` atténue.
- Le module est thread-safe mais **inutilisable depuis un gestionnaire de signal asynchrone** (verrous non réentrants).
- Changements récents, relevés dans les notes de version : 3.12 ajoute l'attribut `taskName` du record (pour asyncio) et la configuration de `QueueHandler`/`QueueListener` par `dictConfig` ; 3.13 ajoute `merge_extra` à `LoggerAdapter` ; 3.14 fait de `QueueListener` un gestionnaire de contexte. L'argument `strm` des handlers personnalisés est déprécié, retrait prévu en 3.16.

### Le contexte et l'identifiant de corrélation

- Un événement utile dit **dans quelle requête** il a été émis. Le cookbook donne trois voies : un `LoggerAdapter` (qui écrase silencieusement un `extra` passé à l'appel), un `Filter` qui ajoute des attributs au record, et `contextvars` (« généralement préférable » aux variables locales de thread).
- **structlog** : le contexte d'un logger est **immuable** (`bind()` en renvoie un nouveau) ; les *processors* sont des fonctions qui prennent et rendent un dictionnaire ; `merge_contextvars` doit être le premier processor, et la documentation recommande `clear_contextvars()` au début du traitement d'une requête. **Limite documentée** : dans une application hybride Starlette/FastAPI, les variables posées en code synchrone n'apparaissent pas dans les logs asynchrones, et inversement. Le détail des threads et de `asyncio.to_thread` (qui propage le contexte) est dans [[Programmation asynchrone en Python]].
- **Loguru** : `bind()` crée un logger avec `extra` ; `contextualize()` est local à chaque thread et à chaque tâche asynchrone ; `serialize=True` produit du JSON ; `enqueue=True` fournit une file sûre entre processus (appeler `logger.complete()` avant la fin du processus). Son option `diagnose` affiche les **valeurs des variables** dans les traces : à désactiver en production, dit la documentation.
- **Deux postures, laissées sans verdict** : structlog se **branche** sur `logging` (`ProcessorFormatter`, quatre approches décrites) ; Loguru l'**intercepte** (un `InterceptHandler`, recette de son README). Rythmes de publication : structlog 26.1.0 (2026-06-06, Python 3.10 ou plus) ; Loguru 0.7.3 (2024-12-06), sans publication depuis, mais avec des commits fin août 2026.
- **Un identifiant par requête** : le poser en entrée (un middleware), le porter dans une variable de contexte, le renvoyer en en-tête de réponse. C'est un raisonnement de rédaction ; le billet de Brandur place bien un identifiant de requête dans sa ligne canonique.
- **[[Uvicorn]]** : `--log-config` accepte un fichier `.json` ou `.yaml` (passé à `dictConfig`) ; `--no-access-log` coupe le seul journal d'accès. Dans son code source, `uvicorn` et `uvicorn.access` ont `propagate: False` : **un handler JSON posé sur le root ne les reçoit pas** sans reconfiguration. Aucune page de [[FastAPI]] sur la journalisation n'a été relue.

### Le lien avec les traces

- Le modèle de données des logs d'OpenTelemetry compte douze champs, dont `Timestamp` (nanosecondes), `ObservedTimestamp`, `TraceId`, `SpanId`, `TraceFlags` (un seul indicateur défini : `SAMPLED`), `SeverityNumber`, `Body` et `Attributes`. `TraceId` et `SpanId` suivent le W3C Trace Context et sont **optionnels** ; si `SpanId` est présent, `TraceId` devrait l'être.
- **Statut, un décalage entre spécification et implémentation.** La page de statut de la spécification déclare stables la Bridge API, le SDK et le protocole des logs ; la page Python et le README du dépôt disent « Development » pour les logs, et annoncent des changements cassants. Pour Python, retenir « Development ».
- **`opentelemetry-instrumentation-logging`** (0.66b0, Beta) : l'injection du contexte de trace est **opt-in** — `inject_trace_context=True`, ou `set_logging_format=True`, ou `OTEL_PYTHON_LOG_CORRELATION=true`. Elle ajoute aux records `otelTraceID`, `otelSpanID`, `otelServiceName` et `otelTraceSampled`. **Deux pièges documentés** : un format qui cite ces champs sans injection active provoque des `KeyError` que `logging` avale en silence ; une configuration de `logging` posée avant l'intégration empêche l'usage du format par défaut. La page est aussi incohérente sur le nom d'une variable (`OTEL_PYTHON_LOG_CODE_ATTRIBUTES` ou `OTEL_PYTHON_CODE_ATTRIBUTES`).
- La page des logs d'OpenTelemetry cite, par résumé, trois stratégies de corrélation : des *appenders* dans l'application, la collecte de fichiers par le Collector, l'envoi OTLP direct.
- **Les exceptions** : `exception.type`, `exception.message` (au moins l'un des deux) et `exception.stacktrace`. La convention équivalente pour les événements de span est **dépréciée** au profit de celle des logs ; l'opt-in passe par `OTEL_SEMCONV_EXCEPTION_SIGNAL_OPT_IN`.
- **Côté stockage.** Avec [[Loki]], l'identifiant de trace ou de requête **n'est pas un label** : la documentation demande des labels statiques et bornés, et chiffre l'effet d'un label dynamique (un `level` qui coupe un flux en cinq donne cinq fois plus de morceaux). L'identifiant se filtre à la requête. L'outil `logcli series --analyze-labels` diagnostique. Le seuil de 100 000 flux actifs par tenant vaut « pour les très gros tenants ». La chaîne [[OpenTelemetry]] → [[Loki]] / [[Tempo]] → [[Grafana]] est décrite dans [[Métriques, logs et traces]].

### Ce qu'il ne faut pas journaliser

- **OWASP** (aide-mémoire sur la journalisation), section « données à exclure » : pas de données sans base légale ; à retirer, masquer, assainir, hacher ou chiffrer plutôt qu'enregistrer tels quels — code source, identifiants de session (au besoin leur empreinte), jetons d'accès, mots de passe, chaînes de connexion, clés, données bancaires, données personnelles sensibles, données collectées sans consentement. Des chemins de fichiers, chaînes de connexion, noms et adresses réseau internes demandent un traitement particulier. Les secrets : [[Gestion des secrets]].
- **Injection de logs** : un champ contenant des retours à la ligne peut forger de fausses lignes. L'aide-mémoire demande d'assainir CR, LF et délimiteurs, et d'encoder pour le format de sortie. Une journalisation qui échoue ne doit pas bloquer l'application ni fuiter d'information.
- **CNIL, délibération n° 2021-122 du 14 octobre 2021** (non prescriptive, limitée à la journalisation applicative de traçabilité des accès et actions sur des traitements de données personnelles) : enregistrer création, consultation, modification et suppression, avec l'auteur identifié individuellement, l'horodatage, la nature de l'opération et la **référence** des données concernées, sans dupliquer les données. Conservation **de six mois à un an** dans le cas général (§8), séparée du système principal ; au-delà d'un an, une justification, et « dans les cas les plus courants » trois ans au plus pour le contrôle interne ; d'autres finalités (obligation légale, analyse après attaque) peuvent justifier plus. Si le traitement principal garde ses données moins de six mois, ne pas garder de données personnelles dans les journaux. Horodater et signer dès la création ; ne pas réutiliser les journaux pour une autre finalité.
- **ANSSI** : horodater tous les événements (R3), avec une précision d'au moins la seconde (R4) et des sources de temps cohérentes (R5) ; ne pas retraiter avant l'envoi aux serveurs centraux (R13) ; minimiser les données personnelles des journaux métier, avec suppression automatique après la rétention. Le guide renvoie à la CNIL pour la durée. Un résumé de recherche parlait de « douze mois minimum » : cette formulation n'a **pas** été retrouvée dans le guide.

### Coût et volume

- Le log **suit le trafic** ; le niveau par défaut, le nombre de lignes par requête et les logs d'accès fixent le volume (voir [[Métriques, logs et traces]]).
- **Ligne canonique** (Brandur Leach, 2016 ; Stripe, 2019) : en plus des logs habituels, **une** ligne longue par requête, émise à la fin par un middleware, avec les caractéristiques clés (méthode, chemin, statut, durée, identifiant de requête, authentification, révision du code, nom du service). Stripe l'envoie aussi, de façon asynchrone, vers Kafka pour un entrepôt de données. Limites citées : le coût des licences Splunk et sa rétention limitée ; l'entrepôt perd le temps réel.
- **Événements larges** (Charity Majors, Honeycomb, 2024, mis à jour en décembre) : des événements structurés très larges comme source unique, agrégés à la lecture, avec un échantillonnage dynamique. **C'est un billet d'éditeur**, qui admet lui-même que le terme « observabilité 2.0 » pourrait ne pas s'imposer ; aucune critique indépendante n'a été lue.
- **Les chiffres de réduction** (30 à 50 %, 40 à 70 %) vus dans des billets d'éditeurs ne sont pas repris. Grafana Cloud facture au volume ingéré, avec comme leviers l'échantillonnage des traces et des règles de filtrage ; rien de primaire n'a été lu sur l'échantillonnage des **logs**.
- **Écrire sans bloquer.** `QueueHandler` + `QueueListener` sortent du thread critique les handlers lents (SMTP, socket) ; `queue.Full` est à prévoir sur une file bornée ; `prepare()` écrase `args` et `exc_info`, donc le handler côté listener ne reformate plus l'exception lui-même. Avec `multiprocessing`, éviter `SimpleQueue` et ne pas réutiliser la même file que le `QueueHandler`. Plusieurs processus ne doivent pas ouvrir le même fichier : un `SocketHandler` ou un `QueueHandler` vers un processus récepteur ; sous Gunicorn ou uWSGI, le cookbook déconseille les handlers de fichier directs dans les workers.

## En pratique

- **stdout, une ligne JSON par événement**, la plateforme (le runtime du conteneur, puis le collecteur) route. Pas de rotation de fichier dans l'application.
- Chaque événement porte au minimum : horodatage, niveau, nom du logger, message, nom du service, identifiant de requête et, quand une trace existe, `trace_id` et `span_id`.
- Poser l'identifiant de requête en entrée, par une variable de contexte ; vérifier qu'il traverse `asyncio.to_thread` (contexte propagé) et ne se perd pas entre code synchrone et asynchrone.
- Vérifier, avant la mise en production, que les loggers d'[[Uvicorn]] passent par le même formateur JSON que l'application.
- Un événement par requête à la fin (ligne canonique) coûte moins qu'un log par étape et se requête mieux ; garder les logs d'étape en DEBUG.
- Ne jamais journaliser un jeton, un mot de passe ni le corps brut d'une requête ; masquer ou hacher. Pour des données personnelles, appliquer la durée de la CNIL **avant** de dimensionner le stockage.
- Un compteur Prometheus à côté de chaque ligne d'erreur reste la règle de la documentation de Prometheus : le compteur alerte, le log détaille (voir [[Métriques, logs et traces]], [[SLO et alerting]]).

## Approches voisines & alternatives

- [[OpenTelemetry]] — le modèle de données des logs et la corrélation avec les traces ; [[Loki]] — le stockage de logs par labels ; [[Grafana]] et [[Kibana]] — la lecture ; [[Tempo]] — les traces ; [[Prometheus]] — les métriques qui doublent le log.
- [[Uvicorn]] et [[FastAPI]] — le serveur dont il faut raccorder les loggers.
- Notions : [[Métriques, logs et traces]], [[SLO et alerting]], [[Gestion des secrets]], [[Programmation asynchrone en Python]] (le contexte à travers les tâches), [[API REST, GraphQL et gRPC]] (le format des erreurs que l'API renvoie, qui ne doit pas non plus fuiter).
- **structlog**, **Loguru** et **syslog** (sans fiche) ; collecteurs de logs tels que Fluent Bit ou Vector : non relus ici.

## Pour aller plus loin

- Python `logging` : https://docs.python.org/3/library/logging.html ; HOWTO : https://docs.python.org/3/howto/logging.html ; cookbook : https://docs.python.org/3/howto/logging-cookbook.html ; configuration : https://docs.python.org/3/library/logging.config.html ; handlers : https://docs.python.org/3/library/logging.handlers.html
- structlog : https://www.structlog.org/en/stable/ ; Loguru : https://loguru.readthedocs.io/en/stable/ ; https://github.com/Delgan/loguru
- Twelve-Factor, facteur XI : https://12factor.net/logs ; RFC 5424 : https://www.rfc-editor.org/rfc/rfc5424.html
- OpenTelemetry — modèle de données des logs : https://opentelemetry.io/docs/specs/otel/logs/data-model/ ; statut de la spécification : https://opentelemetry.io/docs/specs/status/ ; Python : https://opentelemetry.io/docs/languages/python/ ; instrumentation `logging` : https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html ; exceptions dans les logs : https://opentelemetry.io/docs/specs/semconv/exceptions/exceptions-logs/
- OWASP — journalisation : https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html ; CNIL — recommandation (2021) : https://www.cnil.fr/sites/cnil/files/atoms/files/recommandation_-_journalisation.pdf ; ANSSI — guide ANSSI-PA-012 : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-recommandations_securite_architecture_systeme_journalisation.pdf
- Lignes canoniques — Brandur : https://brandur.org/canonical-log-lines ; Stripe : https://stripe.com/blog/canonical-log-lines ; événements larges (Honeycomb, billet d'éditeur) : https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes
- Loki — bonnes pratiques de labels : https://grafana.com/docs/loki/latest/get-started/labels/bp-labels/ ; Grafana Cloud — coûts : https://grafana.com/docs/grafana-cloud/observe-and-act/monitor-applications/application-observability-kg/optimize-costs.md ; Uvicorn — réglages : https://www.uvicorn.dev/settings/
