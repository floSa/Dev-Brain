---
galaxie: dev
type: pattern
contexte: Démo / POC ML local mêlant données relationnelles, documents et artefacts binaires, le tout reproductible en docker-compose.
created: 2026-06-11
modified: 2026-06-11
services_cles: [Postgres, MongoDB, MinIO, FastAPI, Streamlit, Docker]
projets_appliques: []
tags: [pattern, ml-demo, data-app, container, object-storage]
---

# Pattern — Stack démo ML locale multi-services

## Contexte

Démo ou POC ML qui doit montrer un bout de chaîne réaliste : données structurées **et** documents semi-structurés **et** artefacts binaires (modèles, images), une API d'inférence, une UI — sans cloud, reproductible d'un `docker compose up`. Cas typique : prototype à faire tourner chez soi ou présenter en local.

## Stack

- [[Postgres]] — données structurées et métadonnées (jointures, intégrité)
- [[MongoDB]] — documents / payloads au schéma souple
- [[MinIO]] — stockage objet S3-compatible (modèles, datasets, images)
- [[FastAPI]] (+ [[Uvicorn]]) — API d'inférence / service
- [[Streamlit]] — UI de démonstration
- [[Docker]] / docker-compose — graphe de services local
- [[testcontainers]] — tests d'intégration sur les mêmes images

## Décisions clés

### 1. Trois stores, trois rôles
Relationnel / document / objet, pas de fourre-tout. Postgres pour les jointures et l'intégrité, MongoDB pour le schéma souple, MinIO pour les blobs (S3 sans dépendance AWS). Choisir le store par la forme de la donnée, pas par habitude.

### 2. L'API sépare le service du front
L'inférence vit derrière FastAPI ; Streamlit ne fait que la consommer. On remplace l'UI (ou on ajoute un client) sans toucher au modèle, et la logique lourde n'est pas piégée dans le script Streamlit.

### 3. docker-compose comme contrat
Un seul fichier décrit le graphe : `depends_on`, volumes nommés, healthchecks. C'est la description exécutable de l'environnement, réutilisée telle quelle par testcontainers pour les tests d'intégration.

## Pièges

- **MinIO sans bucket** : le bucket n'existe pas au démarrage → job d'init ou création explicite au boot.
- **`depends_on` ≠ readiness** : il ordonne le démarrage, pas la disponibilité → healthchecks + retry côté client.
- **Streamlit ré-exécute tout le script** à chaque interaction → mettre l'appel modèle derrière l'API et `@st.cache_*` pour ne pas recharger à chaque clic.
- **Persistance** : sans volumes nommés, les données disparaissent au `down`.

## Voir aussi

- Services : [[Postgres]], [[MongoDB]], [[MinIO]], [[FastAPI]], [[Uvicorn]], [[Streamlit]], [[Docker]], [[testcontainers]]
- Comparatifs : [[Comparatif - Apps data & démos ML]], [[Comparatif - Frontends web légers]], [[Comparatif - Bases NoSQL]]
