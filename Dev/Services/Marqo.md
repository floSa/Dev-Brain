---
galaxie: dev
type: service
nom: Marqo
alias: [marqo, marqo-ai]
pitch: "Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce."
categorie: database/search
licence_type: open-source
hosted: both
maturite: deprecated
langage: Python/Java
scaling: single-node
alternatives: ["[[Dev/Services/Vespa|Vespa]]", "[[Dev/Services/txtai|txtai]]", "[[Dev/Services/Elasticsearch|Elasticsearch]]"]
remplace_par: []
status: abandonne
tags: [search, vector-db, semantic-search, multimodal]
url_docs: https://github.com/marqo-ai/marqo
url_repo: https://github.com/marqo-ai/marqo
---

# Marqo

## Pourquoi

Moteur de **recherche vectorielle end-to-end** (Apache-2.0) : contrairement à une base vectorielle classique, Marqo **génère lui-même les embeddings** (texte *et* image) à l'indexation comme à la requête, via une seule **API HTTP** — pas d'outil de vectorisation tiers à brancher. C'est sa promesse de « tensor search » multimodale clé en main. **Statut critique** : le **projet open-source est déprécié** et **ne reçoit plus de mises à jour** ; Marqo a pivoté vers sa **plateforme commerciale** de recherche et de découverte produit pour l'e-commerce (marqo.ai). À ne plus retenir pour un nouveau déploiement open-source.

## Quand l'utiliser

- Quasi exclusivement en **maintenance d'un existant** déjà bâti sur Marqo open-source.
- Évaluation du **produit commercial** Marqo pour un cas d'usage e-commerce (search & discovery) — hors périmètre du moteur OSS décrit ici.
- Pour un nouveau projet → préférer une alternative maintenue ci-dessous.

## Quand NE PAS l'utiliser

- **Tout nouveau projet open-source** : moteur non maintenu, pas de correctifs de sécurité.
- Recherche + vectoriel maintenue à grande échelle → [[Dev/Services/Vespa|Vespa]] ou [[Dev/Services/Elasticsearch|Elasticsearch]].
- Recherche sémantique Python embarquée → [[Dev/Services/txtai|txtai]].
- Embedding maîtrisé côté application + base vectorielle dédiée → [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]].

## Déploiement & coût

- Self-host OSS : conteneur Docker, exécution en service ; **non maintenu** désormais.
- Managé : plateforme commerciale Marqo (e-commerce), facturation à l'usage.
- Coût dominé par l'inférence des embeddings (CPU/GPU) en plus du stockage de l'index.

## Pièges

- **Déprécié / non maintenu** : pas de patch de sécurité — risque de conformité en production.
- L'inférence intégrée simplifie l'usage mais **couple** le moteur au choix de modèle et à sa charge GPU.
- Le pivot e-commerce oriente le produit commercial vers un cas d'usage précis — vérifier l'adéquation.
- Retours d'expérience détaillés : `Dev/REX/REX - Marqo.md`.

## Alternatives

- [[Dev/Services/Vespa|Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[Dev/Services/txtai|txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

## Liens

- [[Recherche d'information]] — le cadre général de la recherche.
- [[Bases de données vectorielles]] — le versant vectoriel (Marqo y ajoute l'inférence intégrée).
- [[Comparatif - Moteurs de recherche]] — comparatif de la catégorie.
- Doc (dépôt) : https://github.com/marqo-ai/marqo
