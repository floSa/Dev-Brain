---
role: comparatif
nom: Comparatif - Frameworks LLM
categorie: llm/agents
tags: [agents, rag, structured-output, multi-agent]
---

# Comparatif - Frameworks LLM

> On tranche sur : la couche qu'on importe — assembler, orchestrer une boucle d'agents, indexer et récupérer, ou contraindre la forme de la sortie — puis, dans chaque couche, ce que la brique fait que ses voisines ne font pas.

![[Comparatif - Frameworks LLM.base]]

## Ce qui départage

- [[LangChain]] — le **catalogue d'intégrations** : des interfaces standardisées derrière lesquelles se branchent des centaines de modèles, vector stores, loaders et outils, ce qui permet de changer de fournisseur sans réécrire la logique. Ses abstractions **masquent les prompts réels**, et pour un agent non trivial il renvoie lui-même vers LangGraph.
- [[DSPy]] — renverse le sujet : on déclare des **signatures typées** et un **optimiseur compile les prompts** contre une métrique, jusqu'à convergence. Sans jeu d'exemples ni métrique, il perd son intérêt principal, et la phase d'optimisation consomme beaucoup de tokens.
- [[LangGraph]] — l'agent modélisé en **graphe cyclique à état persisté** : c'est le seul du lot à offrir checkpoints, reprise après interruption et human-in-the-loop comme primitives. Confusion de licence fréquente — la bibliothèque est MIT, `langgraph-api` / LangGraph Platform ne le sont pas.
- [[CrewAI]] — le problème décrit comme une **équipe de rôles** : agents avec rôle, objectif et outils, regroupés en Crews, plus des **Flows** événementiels quand il faut du déterministe. Réécrit de zéro et **indépendant de LangChain**, contrairement à ses débuts. L'abstraction « rôles » est trompeuse de simplicité — sans cadrage, les agents bouclent.
- [[AutoGen]] — le **GroupChat** conversationnel, qui a fait la catégorie. Le critère n'est plus fonctionnel : le dépôt est **en maintenance depuis fin 2025**, et trois projets coexistent — AutoGen legacy, le fork communautaire AG2, et Microsoft Agent Framework comme successeur.
- [[Semantic Kernel]] — la **parité multi-langage** C#/.NET, Python et Java, seul du lot à l'offrir : c'est le choix d'un écosystème .NET/JVM, pas d'un projet Python. Même réserve de cycle de vie — Microsoft annonce Agent Framework comme son successeur, et ses « planners » ont été refondus plusieurs fois.
- [[OpenAI Agents SDK]] — la **minimalité** assumée : agents, **handoffs**, guardrails, sessions, et un tracing intégré. Peu de garde-fous au-delà des primitives — retries, fallback et timeouts restent à câbler — et le tracing part **par défaut chez OpenAI**.
- [[PydanticAI]] — le **typage** de bout en bout : sortie qui est un objet Pydantic validé, injection de dépendances typée, erreurs capturées à l'écriture par mypy/pyright. L'argument ne vaut que si le type-checker tourne en CI, et les intégrations toutes faites y sont plus rares que chez LangChain.
- [[smolagents]] — le **CodeAgent** : l'agent écrit ses actions en **code Python exécutable** plutôt qu'en appels d'outils JSON, ce qui réduit le nombre d'étapes ; cœur en ~1000 lignes, donc auditable de bout en bout. Contrepartie explicite : `LocalPythonExecutor` **n'est pas une frontière de sécurité**.
- [[Agno]] — mémoire, connaissance et raisonnement livrés comme **briques de base**, plus **AgentOS**, un runtime self-host avec API, RBAC et scheduling : c'est le seul à fournir le plan de contrôle de production avec la bibliothèque. Son « le plus rapide » porte sur l'instanciation en mémoire, pas sur la latence réelle, dominée par le LLM.
- [[PraisonAI]] — l'entrée **low-code** : un `agents.yaml` déclare agents, tâches et processus, et le SDK reste là pour ce qui déborde. Second trait propre, l'**auto-réflexion** — l'agent relit sa sortie avant de la rendre, ce qui double au moins le nombre d'appels.
- [[LlamaIndex]] — part du **pipeline de connaissance** et non de l'orchestration : charger, découper, indexer (vectoriel, résumé, arbre, graphe), récupérer. Ses défauts par défaut — taille de chunk, top-k — conditionnent fortement la qualité, et les index avancés coûtent cher en tokens.
- [[Haystack]] — le RAG en **pipeline explicite** de composants typés, testable et observable, avec la recherche hybride dense + BM25 et une licence Apache-2.0. Rupture dure 1.x → 2.x : `farm-haystack` et la 2.x ont des API incompatibles.
- [[RAGatouille]] — le seul du lot à porter la **late-interaction ColBERT** : index PLAID persisté et fine-tuning avec minage de négatifs, pour les corpus hors domaine où le dense mono-vecteur généralise mal. Maintenance ralentie — 0.0.9.post2 en mai 2025, aucun commit depuis.
- [[Instructor]] — la sortie structurée **sans changer de stack** : il emballe le client du fournisseur, ajoute `response_model` et **re-demande automatiquement** au LLM sur échec de validation. C'est du prompt + validation + retry, donc utilisable sur API fermée — et les retries gonflent facture et latence.
- [[Outlines]] — la garantie par **décodage contraint** : les tokens invalides sont masqués à chaque pas, la sortie est conforme par construction et non par parsing. Il lui faut donc les logits — inutilisable derrière une API fermée — et contraindre **biaise la distribution**.
- [[Guidance]] — le seul à **entrelacer contrôle et génération** dans un même programme : conditionnels, boucles et appels d'outils s'intercalent entre les segments générés, avec *token healing* et *fast-forward*. C'est un DSL à apprendre, et ce qui est réellement contraint dépend du backend.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
