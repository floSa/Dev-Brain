---
role: brique
nom: Marqo
alias: [marqo, marqo-ai]
pitch: "Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: deprecated
langage: Python/Java
scaling: single-node
alternatives: ["[[Vespa]]", "[[txtai]]", "[[Elasticsearch]]"]
complements: []
tags: [search, vector-db, semantic-search, multimodal]
url_docs: https://github.com/marqo-ai/marqo
url_repo: https://github.com/marqo-ai/marqo
---

# Marqo

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python/Java | open-source | self-hébergé ou managé · mono-nœud | deprecated | à jour · 2026-04-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche vectorielle **end-to-end** : contrairement à une base vectorielle classique,
Marqo **génère lui-même les embeddings** — texte *et* image — à l'indexation comme à la
requête, derrière une seule **API HTTP**. Aucun outil de vectorisation tiers à brancher, aucun
pipeline d'inférence à tenir : c'est sa promesse de « tensor search » multimodale clé en main,
et c'est aussi ce qui le couple au modèle qu'il embarque. L'éditeur a depuis réorienté son
effort vers une offre commerciale de recherche et de découverte produit pour l'e-commerce.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Maintenance d'un existant déjà bâti sur Marqo open-source | Tout nouveau projet open-source : le moteur n'est plus maintenu et ne reçoit aucun correctif de sécurité — risque de conformité en production |
| Évaluation du produit commercial pour un cas d'usage e-commerce (search & discovery) | L'inférence intégrée couple le moteur au choix de modèle et à sa charge GPU : en changer n'est pas anodin |
| Indexation multimodale texte + image sans pipeline d'embedding à monter | Le pivot e-commerce oriente le produit commercial vers un cas d'usage précis : l'adéquation est à vérifier avant tout engagement |
| | Embedding maîtrisé côté application, plus une base vectorielle dédiée → [[Qdrant]], [[Weaviate]] |

## Mise en œuvre

- Installation — conteneur Docker en self-host ; la plateforme commerciale est un service de l'éditeur
- Point d'entrée — une seule API HTTP : indexation et requête, l'embedding compris
- Prérequis — CPU ou GPU pour l'inférence des embeddings, en plus du stockage de l'index
- Exécution — self-hébergé ou managé, mono-nœud
- Coût — gratuit sous Apache-2.0 pour le moteur OSS, plateforme commerciale facturée à l'usage ; la dépense dominante est l'inférence des embeddings

## Écosystème

### Alternatives

- [[Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

## Ressources

- Dépôt — https://github.com/marqo-ai/marqo — il tient lieu de documentation

## Voir aussi

- [[Recherche d'information]] — le cadre général de la recherche
- [[Bases de données vectorielles]] — le versant vectoriel, auquel Marqo ajoute l'inférence intégrée
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
