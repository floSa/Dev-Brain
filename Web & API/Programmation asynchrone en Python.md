---
role: notion
nom: Programmation asynchrone en Python
alias: [asyncio, async await, coroutines Python, boucle d'événements, event loop, TaskGroup, concurrence structurée, structured concurrency, python sans gil, free-threading, bloquer la boucle]
categorie: web/backend
domaines: [ai-eng, mlops, data-eng]
tags: [parallel, web-framework]
---

# Programmation asynchrone en Python

## Aperçu

- L'asynchrone d'`asyncio` est de la **concurrence coopérative sur un seul thread** : une boucle d'événements exécute des coroutines, et chaque `await` est un point où la coroutine peut céder la main. Pendant qu'une coroutine attend le réseau ou le disque, une autre avance. Le gain vient de l'attente, jamais du calcul.
- Pour un service Python, c'est le mode d'exécution par défaut de [[FastAPI]] sous [[Uvicorn]]. Le piège numéro un en découle : une seule coroutine qui bloque arrête **toutes** les autres.
- Le sujet a trois moitiés qui se rejoignent à l'exploitation : savoir **lancer et arrêter** des tâches proprement (groupes, annulation, délais), savoir **ne pas bloquer la boucle** (threads, exécuteurs), et savoir **ce que le GIL change** — ou ne change pas. Les annotations de type des coroutines ne sont pas traitées ici : voir [[Typage statique en Python]].
- Historique, d'après les PEP : `asyncio` est né avec la PEP 3156 (Python 3.4, coroutines à base de `yield from`) ; `async`/`await` sont venus avec la PEP 492 (3.5) et ont supplanté cette écriture.

## Concepts clés

### Coroutine, tâche, boucle

- Appeler une fonction `async def` **ne l'exécute pas** : cela rend une coroutine. Il faut `asyncio.run()`, un `await`, ou l'envelopper dans une tâche.
- La vue d'ensemble de la documentation insiste sur un point que les débutants manquent : `await une_coroutine()` ne rend pas la main à la boucle, c'est un appel ordinaire. `await une_tache` la rend. Une suite de `await coro()` n'entrelace donc **rien** ; la concurrence demande de créer des tâches.
- Une boucle par thread. `asyncio.run()` crée la boucle, exécute la coroutine principale, ferme la boucle. `asyncio.Runner` (3.11) expose cette mécanique pour réutiliser une boucle sur plusieurs appels. Au Ctrl-C, le premier signal annule la tâche principale puis lève `KeyboardInterrupt` ; un second interrompt tout de suite.
- À la fermeture, `asyncio.run()` laisse cinq minutes à l'exécuteur par défaut avant d'avertir (documentation de `asyncio.Runner`).

### Tâches et groupes de tâches

- `create_task()` planifie une coroutine. **La boucle ne garde que des références faibles aux tâches** : une tâche que personne ne référence peut être ramassée avant d'avoir fini. La documentation donne le motif : un ensemble global, `add` à la création, `add_done_callback(ensemble.discard)`.
- **`TaskGroup`** (3.11) attend toutes ses tâches à la sortie du bloc `async with` et garde des références fortes. Au premier échec autre qu'une annulation, il annule les tâches restantes, refuse d'en ajouter, et lève à la fin un `ExceptionGroup` qui les rassemble. `KeyboardInterrupt` et `SystemExit` ne sont pas groupés.
- **Les groupes d'exceptions** viennent de la PEP 654 (3.11) : `ExceptionGroup`, `BaseExceptionGroup` et la syntaxe `except*`. La PEP cite `asyncio.gather` et les « nurseries » de Trio parmi ses motivations. On ne mélange pas `except` et `except*` dans un même `try`.
- **`gather` contre `TaskGroup`.** Avec `return_exceptions=False`, la première exception de `gather` se propage mais les autres tâches **continuent**. Annuler `gather` annule ses enfants ; annuler un enfant n'annule pas `gather`. La documentation présente `TaskGroup` comme le choix pour le code nouveau.
- Les **tâches eager** (3.12) font démarrer la coroutine de façon synchrone dans le constructeur et ne la planifient que si elle bloque : l'ordre d'exécution peut changer. `eager_start` est devenu un paramètre de `create_task()` en 3.14.

### Annulation et délais

- `CancelledError` hérite de **`BaseException`** : un `except Exception` ne l'attrape pas. `Task.cancel()` la fait lever dans la tâche au prochain point d'attente.
- Depuis 3.11, un compteur accompagne l'annulation : `cancelling()` et `uncancel()`. La documentation demande de **propager** `CancelledError` après nettoyage (`try/finally` de préférence). Qui la supprime volontairement doit aussi appeler `uncancel()`, sans quoi `TaskGroup` et `timeout()` cessent de fonctionner correctement.
- **`asyncio.timeout()`** (3.11) est un gestionnaire de contexte : à l'échéance, il annule la tâche courante et transforme l'annulation en `TimeoutError`, qui s'attrape **à l'extérieur** du bloc. `wait_for()` a été réécrit sur lui en 3.12.
- **`shield()`** protège une tâche interne, mais la coroutine englobante reçoit quand même l'annulation ; la référence de la tâche protégée reste à conserver.
- Un délai est une décision de conception, pas un réglage : un appel réseau sans `timeout()` attend indéfiniment si l'autre côté se tait. Cela vaut pour tout service appelé, y compris un serveur d'inférence.

### Bloquer la boucle : le piège numéro un

- Tout appel synchrone long dans une coroutine (lecture de fichier volumineux, client HTTP bloquant, requête SQL via un pilote synchrone, calcul) fige la boucle : plus aucune tâche n'avance, plus aucune requête n'est servie.
- **Voir le blocage.** Le mode debug se déclenche par `PYTHONASYNCIODEBUG=1`, `python -X dev`, `asyncio.run(debug=True)` ou `loop.set_debug()`. Il journalise les callbacks qui dépassent `slow_callback_duration` (0,1 s par défaut), garde le traceback de création des tâches et vérifie qu'on n'appelle pas la boucle depuis un autre thread. Une coroutine jamais attendue donne un `RuntimeWarning` ; une exception de tâche jamais récupérée n'est journalisée qu'au ramassage de la tâche.
- **Déporter le blocage.** `asyncio.to_thread()` (3.9) exécute une fonction synchrone dans un thread et propage le contexte (`contextvars`) ; `loop.run_in_executor()` en est la forme de bas niveau. L'exécuteur par défaut est un `ThreadPoolExecutor` de `min(32, cpu+4)` threads (3.8), calculé sur `process_cpu_count` depuis 3.13.
- **Ce que ça ne règle pas.** À cause du GIL, `to_thread()` ne rend non bloquantes que des fonctions d'**I/O**, dit la documentation ; pour du calcul, il faut une extension qui relâche le GIL, une implémentation sans GIL, ou un autre processus.
- **Dans FastAPI.** Une route `def` est exécutée dans un *threadpool* extérieur à la boucle ; une route `async def` tourne **directement dans la boucle**. La documentation conseille `def` quand on ne sait pas. Le threadpool a une limite : 40 jetons par défaut, qui vient d'AnyIO (documentation d'AnyIO et de Starlette), réglable, et distincte de l'exécuteur par défaut d'`asyncio`. Ce sont deux plafonds de threads différents.
- **De l'extérieur vers la boucle.** Depuis un autre thread : `call_soon_threadsafe()` ou `run_coroutine_threadsafe()`. Les verrous et événements d'`asyncio` **ne sont pas thread-safe**.

### Coroutines, threads, processus

- **Coroutine** : un thread, bascule aux `await`, très peu de mémoire par tâche ; adaptée à des milliers d'attentes I/O ; inutile pour du calcul pur Python.
- **Thread** : préemptif, simple quand la bibliothèque est bloquante ; le GIL empêche deux threads de calculer en Python pur au même instant (build classique).
- **Processus** : un interpréteur par processus, donc du vrai parallélisme de calcul, au prix de la mémoire et du transfert des données entre processus. Ce coût relève du raisonnement de rédaction : aucune source n'a été relue ici sur `multiprocessing`.
- **Sous-interpréteurs.** Python 3.14 ajoute `concurrent.interpreters` et `InterpreterPoolExecutor` ; la documentation liste des limites : démarrage non optimisé, partage d'objets restreint, extensions tierces souvent incompatibles.
- Sous [[Uvicorn]], la montée en charge par processus passe par `--workers` (1 par défaut, ou `$WEB_CONCURRENCY`, incompatible avec `--reload`) ; `--limit-concurrency` répond 503 au-delà d'un seuil, sans file d'attente.
- Un talk de PyCon DE 2026 (résumé seul lu) avance que, sous quelques centaines de requêtes concurrentes, les écarts entre threads et `asyncio` sont négligeables, et que `asyncio` vise l'économie de ressources plutôt que la vitesse. Source faible, à ne pas ériger en règle.

### Le GIL et Python sans GIL

- **PEP 703** (acceptée le 2023-10-24, à condition d'un déploiement progressif et réversible) rend le GIL optionnel. **PEP 779** (Final, 2025-06-16) fixe les critères du support officiel et les trois phases : I, build expérimental (3.13) ; II, build supporté mais optionnel (3.14) ; III, build par défaut, **sans date**.
- Critères de la phase II : pénalité mono-thread au plus de 15 % (mesure citée : environ 10 %), mémoire au plus 20 % en plus, API stables, documentation interne.
- **Désaccord sur le surcoût, laissé tel quel** : 5-6 % mono-thread dans la PEP 703, 5-10 % dans « Nouveautés de 3.14 », 1-8 % dans le guide du free-threading, environ 10 % avec plafond de 15 % dans la PEP 779. Les chiffres datent de moments et de benchmarks différents.
- En pratique : exécutable séparé (`python3.13t`, installateurs officiels en 3.14), `sys._is_gil_enabled()` pour savoir où l'on est, et une extension C non déclarée compatible **réactive le GIL** (3.13).
- **`asyncio` sous free-threading** est supporté depuis 3.14 : une boucle **par thread**, jamais partagée ; ne pas manipuler les tâches ou futures d'un autre thread ; entre threads, `queue.Queue` plutôt qu'`asyncio.Queue`.
- Conséquence de lecture : le free-threading ne rend pas une boucle parallèle, il autorise **plusieurs threads** à calculer en même temps. L'attente d'I/O reste le domaine d'`asyncio` ; le calcul gagne des threads. Le blog de Quansight sur la mise à l'échelle d'`asyncio` sans GIL n'a pas pu être ouvert (erreur 429) : aucun chiffre n'est repris.

### Quand l'asynchrone n'apporte rien

- **Calcul pur** (inférence d'un modèle dans le processus, transformation de DataFrame) : la boucle n'accélère rien et se fige. Sortir le calcul vers un thread (si l'extension relâche le GIL), un processus ou un serveur d'inférence séparé.
- **Peu de concurrence** : un script qui appelle trois API l'une après l'autre ne justifie pas la complexité ; c'est un jugement de rédaction.
- **Bibliothèques synchrones** : tout l'écosystème autour doit être asynchrone, sinon on le déporte en threads. Bob Nystrom a nommé cette contamination en 2015 (« What Color is Your Function? ») : une fonction asynchrone ne s'appelle que depuis une autre.
- **Tâches longues hors du cycle de requête** : une file de tâches comme [[Celery]] (qui n'exécute pas les `async def` en 5.x, selon sa fiche) plutôt qu'une tâche d'arrière-plan dans le serveur web.

### Les critiques

- **Concurrence structurée.** Nathaniel J. Smith (2018) compare le lancement d'une tâche d'arrière-plan à un `goto` : l'abstraction de fonction se brise, le nettoyage des ressources n'est plus garanti, les erreurs des tâches orphelines se perdent. Sa réponse, la *nursery* de Trio, garantit que le parent ne sort pas avant ses enfants. `TaskGroup` en est l'héritier dans la bibliothèque standard ; le rapprochement avec `create_task` est une inférence, l'article ne le traite pas.
- **Désaccord entre sources.** La documentation de Python recommande `TaskGroup` contre `gather`. La documentation d'AnyIO le juge insuffisant (pas d'annulation par portée, pas de liste des tâches) et défend une annulation « de niveau » plutôt que le « front » unique d'`asyncio`. Un billet de 2025 (sailor.li) ajoute les références faibles aux tâches et l'absence de contre-pression dans `asyncio.Queue` ; c'est un avis, lu par extraction.
- **Tâches qui disparaissent.** Un billet d'août 2026 décrit trois mécanismes (annulation à l'arrêt, ramasse-miettes, exceptions non journalisées) ; source secondaire, qui recoupe ce que la documentation dit déjà des références faibles.

### Ce qui est déprécié ou retiré

- **Politiques de boucle** : `get_event_loop_policy()`, `set_event_loop_policy()` et les classes `*EventLoopPolicy` sont dépréciées depuis **3.14**, retrait prévu en **3.16**. Remplacement : `asyncio.run(..., loop_factory=...)` ou `Runner(loop_factory=...)`.
- `asyncio.iscoroutinefunction` : dépréciée, retrait prévu en 3.16 ; utiliser `inspect.iscoroutinefunction`.
- `asyncio.get_event_loop()` sans boucle courante lève `RuntimeError` en 3.14. Les avertissements des versions 3.10 à 3.13 n'ont pas été relus.
- Le paramètre `loop=` a été retiré de plusieurs fonctions en 3.10.
- Côté serveur : `uvicorn.workers` est déprécié au profit du paquet `uvicorn-worker`.
- Non vérifié ici : la version qui a retiré le décorateur `asyncio.coroutine`.

## En pratique

- Un appel bloquant dans une route `async def` : l'envelopper dans `asyncio.to_thread()`, ou déclarer la route `def`.
- Plusieurs appels à lancer ensemble : un `TaskGroup`, pas des `create_task()` nus ; sinon garder soi-même les références.
- Chaque appel réseau reçoit un `asyncio.timeout()`.
- En développement : `python -X dev`. En 3.14, `python -m asyncio ps PID` liste les tâches d'un processus qui tourne, `pstree` en donne l'arbre d'attente et signale les cycles ; `capture_call_graph()` fait de même depuis le code.
- Derrière un proxy, les délais du proxy et ceux de la boucle doivent s'accorder : voir [[Reverse proxy et TLS]]. Pour un flux émis par un générateur asynchrone, y compris la détection de la déconnexion du client : [[Server-Sent Events & streaming LLM]].
- Sur un site on-prem, la montée en charge d'un service se fait d'abord par des processus (`--workers`), puis par réplication : voir [[Du Compose à Kubernetes — quand changer d'échelle]]. La communication entre services par événements relève d'[[Architecture pilotée par les événements]] et de [[Kafka]].

## Approches voisines & alternatives

- [[FastAPI]] et [[Uvicorn]] — l'application ASGI et le serveur qui l'exécute, tous deux bâtis sur la boucle d'`asyncio`.
- [[Flask]] — micro-framework WSGI synchrone : ses vues `async` existent depuis la 2.0, mais le modèle reste synchrone et se dimensionne par workers, selon sa fiche.
- [[Celery]] — les tâches longues et les relances, hors du processus web.
- [[SQLAlchemy]] — l'accès aux bases depuis une coroutine : un pilote synchrone y bloque la boucle ; l'usage asynchrone de cet ORM n'a pas été relu pour cette page.
- **Trio** et **AnyIO** (sans fiche) — la concurrence structurée « de niveau » : AnyIO sert de socle à Starlette, donc à FastAPI.
- **`threading`, `concurrent.futures`, `multiprocessing`** — le modèle préemptif, non traité en détail ici.
- Voir aussi : [[Typage statique en Python]], [[Métriques, logs et traces]].
- [[API REST, GraphQL et gRPC]] — les styles d'API des services ASGI ; [[Journalisation structurée et traçabilité]] — le contexte des logs à travers les tâches (contextvars).

## Pour aller plus loin

- `asyncio` — tâches et groupes : https://docs.python.org/3/library/asyncio-task.html ; boucle : https://docs.python.org/3/library/asyncio-eventloop.html ; mode debug : https://docs.python.org/3/library/asyncio-dev.html ; `Runner` : https://docs.python.org/3/library/asyncio-runner.html
- Vue d'ensemble conceptuelle : https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html ; `asyncio` et free-threading : https://docs.python.org/3/library/asyncio-threading.html ; politiques (dépréciation) : https://docs.python.org/3/library/asyncio-policy.html
- PEP 3156 : https://peps.python.org/pep-3156/ ; PEP 492 : https://peps.python.org/pep-0492/ ; PEP 654 : https://peps.python.org/pep-0654/ ; PEP 703 : https://peps.python.org/pep-0703/ ; PEP 779 : https://peps.python.org/pep-0779/
- Guide du free-threading : https://docs.python.org/3/howto/free-threading-python.html ; Nouveautés de 3.11 : https://docs.python.org/3/whatsnew/3.11.html ; de 3.14 : https://docs.python.org/3/whatsnew/3.14.html
- FastAPI — `async` et `await` : https://fastapi.tiangolo.com/async/ ; Starlette — threadpool : https://www.starlette.dev/threadpool/ ; AnyIO — threads : https://anyio.readthedocs.io/en/stable/threads.html ; annulation : https://anyio.readthedocs.io/en/stable/cancellation.html ; pourquoi AnyIO : https://anyio.readthedocs.io/en/stable/why.html
- Uvicorn — réglages : https://www.uvicorn.dev/settings/ ; déploiement : https://www.uvicorn.dev/deployment/
- N. J. Smith, *Notes on structured concurrency* : https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/ ; B. Nystrom, *What Color is Your Function?* : https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/ ; Trio — conception : https://trio.readthedocs.io/en/stable/design.html
- Billet critique (2025) : https://sailor.li/asyncio ; talk PyCon DE 2026 (résumé) : https://pycon.de/archive/2026/talks/asyncio-vs-threads-who-survives-in-the-no-gil-era/
