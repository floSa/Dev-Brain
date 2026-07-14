---
galaxie: dev
type: pattern
contexte: Chaîne de bout en bout collecte web → résolution / matching d'entités → décision par optimisation sous contraintes.
created: 2026-06-11
modified: 2026-06-11
services_cles: [Playwright, bm25s, PuLP, Prefect]
projets_appliques: []
tags: [pattern, web-scraping, string-matching, combinatorial-optimization, linear-programming, data-pipeline]
---

# Pattern — Pipeline scraping → matching → optimisation

## Contexte

Chaîne de bout en bout : **collecter** des données sur le web, les **rapprocher** d'un référentiel (résolution d'entités / matching), puis **décider** via une optimisation (affectation, sélection, planning sous contraintes). Cas typiques : sourcing, pricing, appariement offre/demande, constitution de paniers sous budget.

## Stack

- **Scraping** — [[Playwright]] (sites JS), [[curl_cffi]] / [[cloudscraper]] (anti-bot), [[selectolax]] (parsing HTML rapide)
- **Matching** — [[bm25s]] / [[rank-bm25]] (lexical), [[sentence-transformers]] (sémantique), fuzzy matching (similarité de chaînes)
- **Optimisation** — [[PuLP]] (modèle MIP/LP, solveur CBC par défaut)
- **Orchestration** — [[Prefect]] (ou [[Dagster]]) : enchaîner, reprendre et planifier les étapes

## Décisions clés

### 1. Trois étapes découplées, contrats clairs entre elles
Chaque étape produit un artefact validé ([[Pydantic]]) que la suivante consomme. Le matching ne re-scrape pas ; l'optimisation ne re-matche pas. La reprise est possible à n'importe quelle étape sans rejouer toute la chaîne.

### 2. Matching = lexical + sémantique + seuil
Combiner BM25 (rappel, robuste aux termes exacts) et embeddings (sémantique), puis trancher au-dessus d'un seuil. Les cas ambigus partent en revue plutôt que d'être tranchés au hasard.

### 3. Optimisation formalisée, pas heuristique ad hoc
Poser explicitement variables, contraintes et objectif (MIP). PuLP donne un modèle lisible et vérifiable ; on passe à un solveur dédié seulement si la taille l'impose. Une heuristique maison cache les hypothèses et se révèle fausse en silence.

## Pièges

- **Scraping fragile** (sélecteurs cassants, anti-bot) → isoler l'étape, retry + cache ; un site qui change ne doit pas faire tomber tout le pipeline.
- **Matching tout-ou-rien sans seuil de revue** → faux positifs propagés tels quels dans l'optimisation.
- **Modèle d'optim infaisable ou non borné** → contraintes incohérentes ; vérifier la faisabilité sur un petit cas avant de scaler.
- **Étapes non idempotentes** → un re-run produit des doublons. Clé d'identité + upsert à chaque étape.

## Voir aussi

- Services : [[Playwright]], [[curl_cffi]], [[cloudscraper]], [[selectolax]], [[bm25s]], [[rank-bm25]], [[sentence-transformers]], [[PuLP]], [[Prefect]], [[Pydantic]]
- Concepts : [[Web scraping]], [[Fuzzy matching & similarité de chaînes]], [[BM25]], [[Optimisation combinatoire]], [[Programmation linéaire en nombres entiers (MIP)]]
- Comparatifs : [[Comparatif - Scraping]], [[Comparatif - Solveurs d'optimisation]]
