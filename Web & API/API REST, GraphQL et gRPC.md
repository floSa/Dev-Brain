---
role: notion
nom: API REST, GraphQL et gRPC
alias: [REST, API REST, GraphQL, gRPC, protocol buffers, protobuf, openapi, problem details, pagination par curseur, versionnage d'API, api first]
categorie: web/api
domaines: [ai-eng, data-eng, mlops]
tags: [web-framework, schema-evolution, idempotence, serialization]
---

# API REST, GraphQL et gRPC

## Aperçu

- Une API est un **contrat** entre un client et un service. Trois styles dominent et optimisent des choses différentes : **REST** (des ressources adressées par URL, la sémantique de HTTP, ses caches et ses outils), **GraphQL** (le client choisit les champs qu'il veut, sur un schéma typé) et **gRPC** (un contrat Protobuf, des flux, HTTP/2).
- Ce n'est pas un classement : chaque style déplace le coût ailleurs. REST le met sur le nombre d'allers-retours, GraphQL sur le serveur (coût d'une requête libre), gRPC sur les clients (outillage, navigateur).
- Le choix se fait sur une frontière — interne ou exposée, navigateur ou service, requête-réponse ou flux — pas sur une préférence. La section « Choisir » de cette page relève du raisonnement de rédaction : aucune source sérieuse sur des services internes n'a été lue en entier.
- Ce qui revient dans les trois — contrat, versionnage, erreurs, pagination, idempotence — est traité à part : c'est là que les équipes se trompent.

## Concepts clés

### REST : un style d'architecture, pas un protocole

- La thèse de Fielding (2000, chapitre 5) définit REST comme un **style hybride** dérivé d'autres styles réseau, avec six contraintes : client-serveur, **sans état**, cache, **interface uniforme**, système en couches, et le code à la demande, seule contrainte optionnelle.
- L'interface uniforme a quatre volets : identification des ressources, manipulation par représentations, messages auto-descriptifs, et **l'hypermédia comme moteur de l'état de l'application** (HATEOAS).
- Fielding a reproché en 2008 à beaucoup d'« API REST » d'être des appels de procédure sur HTTP : pour lui, une API qui n'est pas pilotée par l'hypertexte n'est pas RESTful, et l'effort de conception doit porter sur les types de médias, pas sur une documentation « méthode X sur l'URL Y ».
- Le **modèle de maturité de Richardson** (présenté à QCon 2008, repris par Fowler en 2010) gradue : niveau 0, un seul point d'entrée ; 1, des ressources ; 2, les verbes et codes de statut HTTP ; 3, les contrôles hypermédia. Fowler précise que ce n'est pas une définition de REST mais un outil pour apprendre.
- **Désaccord laissé tel quel** : Fielding exige le niveau 3 ; la pratique courante s'arrête au niveau 2. Phil Sturgeon (2019) défend la valeur de la démarche sans imposer l'hypermédia partout.

### La sémantique HTTP qu'on emprunte (RFC 9110)

- La RFC 9110 (juin 2022, STD 97) remplace notamment la RFC 7231. Elle définit les méthodes **sûres** (§9.2.1, essentiellement en lecture seule : GET, HEAD, OPTIONS, TRACE) et **idempotentes** (§9.2.2 : l'effet voulu sur le serveur de plusieurs requêtes identiques est celui d'une seule). Sont idempotentes les sûres, plus PUT et DELETE. POST ne l'est pas.
- **PATCH n'est pas dans la RFC 9110** : il est défini à part, dans la RFC 5789 (non relue ici). L'idempotence d'un PATCH dépend de son contenu.
- L'idempotence parle de l'**effet**, pas de la réponse : un second DELETE peut rendre un 404 sans avoir changé l'état.
- **`Idempotency-Key`**, l'en-tête que beaucoup de services de paiement ont popularisé pour rendre POST rejouable, n'est **pas un standard** : le brouillon du groupe de travail `httpapi` en est à la révision -07 (2025-10-15), classé « expiré et archivé », sans numéro de RFC. Les lignes directrices de Zalando le citent comme optionnel (règle 230) et demandent de rendre POST et PATCH idempotents quand c'est possible (règle 229).
- **La méthode QUERY** (RFC 10008, juin 2026, voie des normes) est sûre et idempotente et porte un **corps** de requête : elle règle le cas d'une recherche trop riche pour une URL. La page de la RFC a été ouverte ; la spécification OpenAPI 3.2 l'a déjà intégrée. Rien n'a été relu sur son adoption par les serveurs et les proxys.

### Les erreurs

- **RFC 9457** (juillet 2023, rend obsolète la RFC 7807) : un document `application/problem+json` à cinq membres standard — `type` (une URI, `about:blank` par défaut), `title`, `status` (donné par commodité), `detail` (propre à l'occurrence) et `instance`. Des membres d'extension sont permis, les clients ignorent ceux qu'ils ne connaissent pas, et la RFC avertit de ne pas y fuiter d'informations sensibles. Zalando demande ce format (règle 176).
- **FastAPI** renvoie par défaut `{"detail": ...}` pour une `HTTPException` et un 422 pour une validation échouée ; on remplace ces comportements avec `@app.exception_handler`. La documentation lue ne parle **pas** de Problem Details : l'écrire demande un gestionnaire maison, et aucun exemple officiel n'a été trouvé.
- **gRPC** a 17 codes de statut (de `OK` à `UNAUTHENTICATED`) ; le statut passe en **trailers** HTTP/2 (`grpc-status`). La ligne directrice AIP-193 de Google demande un `google.rpc.Status` avec un `ErrorInfo` (raison, domaine, métadonnées). Selon la documentation, sept de ces codes ne sont jamais produits par les bibliothèques elles-mêmes mais seulement par le code applicatif (`INVALID_ARGUMENT`, `NOT_FOUND`, `ALREADY_EXISTS`, `FAILED_PRECONDITION`, `ABORTED`, `OUT_OF_RANGE`, `DATA_LOSS`).
- **GraphQL** : la documentation de sécurité demande de masquer les messages d'erreur détaillés en production. Le format des erreurs de la spécification n'a pas été relu ici.

### La pagination

- **Par décalage** (`skip`/`limit`) : simple, mais la page bouge quand des lignes arrivent ou partent. **Par curseur** : un jeton opaque désigne la position. Zalando rend la pagination obligatoire et préfère le curseur (règles 159 et 160). La documentation de FastAPI lue ne montre qu'un exemple `skip`/`limit` ; une bibliothèque tierce existe, non relue.
- **AIP-158** : `page_size`, `page_token`, `next_page_token`, jetons opaques que l'utilisateur ne doit pas analyser ; une taille trop grande se ramène au maximum, une taille négative est une erreur. Point à retenir : **ajouter la pagination après coup casse les clients** — la prévoir dès le premier jour.
- **GraphQL** recommande le curseur sous forme de **connexions** (`first`, `after`, `edges`, `node`, `cursor`, `pageInfo` avec `hasNextPage` et `endCursor`) et déconseille le décalage. La spécification GraphQL, elle, **ne normalise pas** la pagination.
- **REST** peut annoncer les pages suivantes par l'en-tête `Link` (RFC 8288, octobre 2017) : des relations typées dont `next`, `prev`, `first`, `last` au registre IANA (liste confirmée en partie seulement).

### OpenAPI : décrire une API HTTP pour les machines

- La spécification OpenAPI décrit chemins, opérations, schémas et sécurité dans un document lisible par des outils (documentation, clients générés, validation). La **3.1.1** (2024-10-24) s'aligne sur JSON Schema 2020-12 ; la **3.2.0** (2025-09-19) ajoute la méthode `query`, des sections sur le streaming (dont les événements serveur) et un registre de types de médias ; les dernières versions publiées par ligne sont 3.2.1, 3.1.2 et 3.0.4 (dates non relevées). Les numéros `major.minor` désignent un jeu de fonctionnalités, les correctifs ne font que clarifier.
- **FastAPI émet OpenAPI 3.1.0 par défaut** (`openapi_version`, surchargeable, par exemple en 3.0.2 pour un outil qui ne comprend pas 3.1). Écart à signaler : la spécification courante est en 3.2.x ; aucune page de FastAPI lue ne parle de 3.2.
- **Contrat d'abord ou code d'abord.** Zalando prescrit « API first » avec une description OpenAPI 3.1 (règles 100 et 101) ; FastAPI fait l'inverse : le code typé produit la description. Les deux se défendent ; le second garantit que la description ne ment pas, le premier que le contrat précède l'implémentation (raisonnement de rédaction).

### Versionner et faire évoluer un contrat

- **Ce qui est compatible** (AIP-180) : ajouter des composants, des champs, des valeurs d'énumération — mais pas un champ requis dans une requête existante. **Ce qui casse** : supprimer, renommer, changer un type même compatible sur le fil, changer un défaut ou une sérialisation.
- **Protobuf** : un champ se désigne par son numéro (1 à 536 870 911 ; 1 à 15 tiennent sur un octet ; 19000 à 19999 réservés). On ne réutilise **jamais** un numéro, on marque l'ancien `reserved` ; les champs inconnus sont préservés. L'outil `buf breaking` compare le schéma courant à une référence passée selon quatre niveaux de rigueur : `FILE`, `PACKAGE`, `WIRE_JSON`, `WIRE`. Les **éditions** protobuf (2023 la première, 2024 la plus récente de la page ; une 2025 n'a pas été vérifiée) remplacent la déclaration `syntax = "proto2/proto3"`.
- **GraphQL** se dit « sans version » : on ajoute des champs et on marque les anciens `@deprecated`.
- **REST** : le désaccord est net. Zalando **rejette** le versionnage par l'URL (règle 115) et prescrit celui par type de média (règle 114), avec un numéro sémantique pour la spécification (règle 116). La pratique courante est un préfixe `/v1`. FastAPI permet de préfixer un routeur ; la page lue n'en fait pas une recommandation de versionnage, et des sous-applications montées y sont déconseillées pour cet usage.
- **Fowler (2014)** : pour des services, préférer le lecteur tolérant et les contrats pilotés par les consommateurs ; le versionnage est un dernier recours.
- **Annoncer la fin d'un point d'accès** : l'en-tête `Deprecation` (RFC 9745, mars 2025 ; la valeur est une date au format de champ structuré) et l'en-tête `Sunset` (RFC 8594, mai 2019, statut informatif) ; la date de `Sunset` ne peut pas précéder celle de `Deprecation`. Zalando les demande (règles 187 à 191).

### GraphQL : la requête sélective

- La spécification (édition de septembre 2025, publiée le 2025-09-03 ; un brouillon est daté du 2026-09-28) normalise le langage de requête, le système de types, l'introspection, la validation et l'exécution. **Hors périmètre** : le transport, la sérialisation, l'autorisation, la pagination.
- Promesse de graphql.org : demander exactement les champs voulus (contre la sur-récupération et la sous-récupération), un point d'entrée unique, un schéma typé interrogeable.
- **Le coût passe au serveur.**
  - **N+1** : pour N amis, N+1 accès aux sources ; le remède est le regroupement, que **DataLoader** (utilitaire JavaScript issu de Facebook, dépôt `graphql/dataloader`) fait par lots avec un cache par requête.
  - **Sécurité** : documents de confiance (requêtes persistées), pagination, limites de profondeur et de largeur, analyse de complexité, limitation de débit, validation des entrées, introspection désactivée en production. Les documents de confiance ne conviennent vraiment qu'aux clients maison.
  - **Cache** : un POST sur un point d'entrée unique n'a pas de cache HTTP par URL ; la documentation demande d'exposer des identifiants globaux d'objets pour un cache côté client.
- **GraphQL sur HTTP** : POST obligatoire, GET facultatif pour les requêtes ; types de médias `application/graphql-response+json` (recommandé) et `application/json` (hérité). La spécification de ce transport est encore au stade de brouillon (2026-09-28). La page de graphql.org garde une consigne datée du 1er janvier 2025, **passée**.
- **Critique.** Un billet de WunderGraph (2026, mis à jour le 2026-09-24) conteste deux chiffres populaires (« 56 % des équipes ont des difficultés de cache », « 80 % des API GraphQL vulnérables au déni de service ») ; son auteur dirige un éditeur de fédération GraphQL : source partisane. Le billet confirme que le POST casse le cache par défaut et que les requêtes persistées permettent un cache GET sur un CDN. **Aucune source critique indépendante de GraphQL n'a été lue en entier.**

### gRPC et Protocol Buffers

- **Quatre formes d'appel** : unaire, flux serveur, flux client, flux bidirectionnel ; l'ordre des messages est garanti dans un appel. Le contrat est un fichier `.proto` d'où l'on génère clients et serveurs.
- **Délais.** Par défaut, **aucune échéance** : le client attend indéfiniment, ce que la documentation déconseille. Il faut en fixer une, la propager aux appels suivants, et que le serveur surveille les annulations. Annuler n'annule pas les effets déjà produits.
- **Sur le fil** (spécification HTTP/2) : un POST sur `/Service/Méthode`, `content-type: application/grpc`, chaque message préfixé d'un octet de compression et de quatre de longueur ; le statut final voyage en **trailers**.
- **Navigateur.** Aucune API de navigateur n'offre le contrôle nécessaire : **gRPC-Web** passe par un proxy et ne gère que l'unaire et le flux serveur (l'article lu date de 2018, l'état actuel du dépôt n'a pu être ouvert : erreur 504). **Connect-RPC** parle trois protocoles (Connect, gRPC, gRPC-Web) sur HTTP/1.1, 2 et 3 ; son protocole propre n'utilise pas de trailers, et un appel unaire est un POST ordinaire. **grpc-gateway** génère, depuis des annotations, un proxy REST/JSON devant un service gRPC.
- **Critiques, et leurs intérêts.** Un billet de Speedscale (2025, éditeur d'un outil de rejeu de trafic : source intéressée) liste six leçons de production : complexité de HTTP/2, opacité de la sérialisation binaire sans outils, valeurs par défaut absentes en JSON, flux longs qui peuvent bloquer, délais et relances faciles à mal régler. Un billet de 2026 (blog personnel, favorable à Connect-RPC) soutient que les trailers posent problème côté navigateur et que la plupart des appels ne sont que des requête-réponse qui devraient suivre la sémantique HTTP. **Désaccord** : la documentation officielle présente gRPC-Web comme la solution navigateur ; ces auteurs la tiennent pour un pis-aller.

## Choisir pour des services internes sur site

Cette section est du raisonnement de rédaction, pas une source lue.

- **REST/JSON par défaut.** Tout client, tout proxy, tout outil de debug le comprend ; l'équipe peut `curl` un service à 3 h du matin. Une description OpenAPI donne les clients générés et la documentation. Le coût : un contrat moins strict, des flux à part (voir [[Server-Sent Events & streaming LLM]]).
- **gRPC quand le contrat doit être strict entre services** : plusieurs langages, flux bidirectionnels, volumes où le binaire compte. Le cas typique en data/ML est le service d'inférence appelé par d'autres services. Le coût : l'outillage et l'opacité du binaire, le navigateur hors de portée sans proxy. Le cas de Spotify (CNCF, 2019) montre l'adoption de gRPC pour remplacer un protocole maison, avec un effet espéré sur le contrat et la compatibilité ; aucun retour chiffré n'a été relu.
- **GraphQL quand beaucoup de clients composent des vues différentes sur un même graphe de données**, typiquement un front. Pour des services internes qui échangent des messages fixes, il apporte surtout de la surface d'attaque à gérer.
- **Un monolithe d'abord** : Fowler (*Monolith First*, 2015) observe que les microservices qui réussissent viennent souvent d'un monolithe découpé ; la question du style d'API ne se pose qu'à la frontière qu'on décide de créer.
- **Passerelle et proxy.** Le reverse proxy ou la passerelle est le point où l'on met le TLS, le routage, la limitation de débit ; voir [[Reverse proxy et TLS]], dont la Gateway API déclare un `GRPCRoute`. Le statut gRPC voyageant en trailers, un intermédiaire doit relayer HTTP/2 et trailers de bout en bout (déduction de la spécification HTTP/2 ci-dessus, non testée sur les proxys du brain).
- **Qui appelle.** L'authentification du client (jeton porteur, métadonnées gRPC) est dans [[OAuth2 et OpenID Connect]].
- **Messages plutôt qu'appels.** Quand l'appelant n'a pas à attendre la réponse, un bus d'événements remplace l'API : [[Architecture pilotée par les événements]] et [[Kafka]].

## En pratique

- Écrire le contrat avant le premier client, et décider **dès le début** de la pagination, de l'idempotence des écritures, du format des erreurs et de la règle de dépréciation : les changer après coup casse les clients.
- Rendre idempotentes les écritures qu'un client peut rejouer (réseau instable, tâches de relance) : une clé fournie par le client côté serveur, ou une méthode idempotente par nature (PUT). La clé n'est pas un standard (voir plus haut).
- Poser un délai sur chaque appel inter-services, quel que soit le style : un délai absent est le défaut de gRPC et de beaucoup de clients HTTP.
- Générer la description OpenAPI depuis le code ([[FastAPI]]) ou le code depuis la description ; dans les deux cas, la mettre dans l'intégration continue.
- Ne pas faire fuiter un message d'exception dans un corps d'erreur (RFC 9457, documentation de sécurité de GraphQL).
- Tester à la main avec [[Postman]] ou [[Bruno]] ; leur définition dans le vocabulaire du brain couvre REST, GraphQL et gRPC.

## Approches voisines & alternatives

- [[FastAPI]] — génère la description OpenAPI depuis ses annotations ; [[Pydantic]] fournit la validation dont il dérive les schémas ; [[Flask]] est l'alternative synchrone ; [[Uvicorn]] exécute l'application.
- [[Postman]] et [[Bruno]] — les clients d'API du brain.
- [[public-apis]] — un annuaire d'API publiques, utile pour s'exercer sur un contrat réel.
- [[Nginx]] et [[Traefik]] — des reverse proxys qui peuvent porter la passerelle ; leur prise en charge de gRPC n'a pas été relue pour cette page.
- [[Programmation asynchrone en Python]] — le modèle d'exécution des services ASGI qui exposent ces API.
- Voir aussi : [[Architecture pilotée par les événements]], [[Reverse proxy et TLS]], [[OAuth2 et OpenID Connect]].
- Non traités : SOAP, JSON-RPC, WebSocket, tRPC.
- [[Journalisation structurée et traçabilité]] — journaliser une requête sans fuiter de données ni d'exception.

## Pour aller plus loin

- Fielding, thèse (ch. 5, REST) : https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm ; *REST APIs must be hypertext-driven* : https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven
- Fowler — modèle de maturité de Richardson : https://martinfowler.com/articles/richardsonMaturityModel.html ; Sturgeon : https://apisyouwonthate.com/blog/rest-and-richardson-maturity-model/ ; microservices : https://martinfowler.com/articles/microservices.html ; *Monolith First* : https://martinfowler.com/bliki/MonolithFirst.html
- RFC 9110 : https://www.rfc-editor.org/rfc/rfc9110.html ; RFC 9457 : https://www.rfc-editor.org/rfc/rfc9457.html ; RFC 8288 : https://www.rfc-editor.org/rfc/rfc8288.html ; RFC 8594 : https://www.rfc-editor.org/rfc/rfc8594.html ; RFC 9745 : https://www.rfc-editor.org/rfc/rfc9745.html ; RFC 10008 (QUERY) : https://www.rfc-editor.org/rfc/rfc10008.html
- Brouillon `Idempotency-Key` : https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- OpenAPI : https://spec.openapis.org/oas/ ; 3.2.0 : https://spec.openapis.org/oas/v3.2.0.html ; 3.1.1 : https://spec.openapis.org/oas/v3.1.1.html ; FastAPI — erreurs : https://fastapi.tiangolo.com/tutorial/handling-errors/ ; sa classe : https://fastapi.tiangolo.com/reference/fastapi/
- GraphQL — spécification : https://spec.graphql.org/ ; apprendre : https://graphql.org/learn/ ; pagination : https://graphql.org/learn/pagination/ ; performance : https://graphql.org/learn/performance/ ; sécurité : https://graphql.org/learn/security/ ; cache : https://graphql.org/learn/caching/ ; sur HTTP : https://graphql.org/learn/serving-over-http/ ; DataLoader : https://github.com/graphql/dataloader
- gRPC — concepts : https://grpc.io/docs/what-is-grpc/core-concepts/ ; délais : https://grpc.io/docs/guides/deadlines/ ; statuts : https://grpc.io/docs/guides/status-codes/ ; protocole HTTP/2 : https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md ; gRPC-Web : https://grpc.io/blog/state-of-grpc-web/ ; Connect-RPC : https://connectrpc.com/docs/protocol/ ; grpc-gateway : https://github.com/grpc-ecosystem/grpc-gateway
- Protocol Buffers — proto3 : https://protobuf.dev/programming-guides/proto3/ ; éditions : https://protobuf.dev/editions/overview/ ; `buf breaking` : https://buf.build/docs/breaking/
- Google AIP — pagination : https://google.aip.dev/158 ; compatibilité : https://google.aip.dev/180 ; erreurs : https://google.aip.dev/193 ; Zalando — lignes directrices : https://opensource.zalando.com/restful-api-guidelines/
- Critiques : WunderGraph (partisan) : https://wundergraph.com/blog/fact-checking-graphql-vs-rest ; Speedscale (intéressé) : https://speedscale.com/blog/six-lessons-from-production-grpc/ ; kmcd.dev : https://kmcd.dev/posts/grpc-web-should-have-fixed-grpc/ ; Spotify (CNCF) : https://www.cncf.io/case-studies/spotify/
