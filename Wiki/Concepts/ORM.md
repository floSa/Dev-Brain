---
galaxie: wiki
type: concept
nom: ORM
alias: [orm, object-relational mapping, mapping objet-relationnel]
categorie: concept/data
domaines: [data-eng]
tags: [orm, relational]
---

# ORM

## Aperçu

- **Object-Relational Mapping** : faire correspondre des tables relationnelles à des objets/types du langage, pour manipuler la base sans écrire (tout) le SQL à la main.
- Objectif : productivité et sécurité de typage ; on travaille avec des entités, l'ORM traduit en SQL et gère la correspondance lignes ↔ objets.

## Concepts clés

### Mapping & unité de travail
- Une classe/un type ↔ une table ; un objet ↔ une ligne. Les relations (1-N, N-N) deviennent des références entre objets.
- Beaucoup d'ORM suivent les changements en mémoire et les persistent en lot (unit of work / sessions).

### Data Mapper vs Active Record
- Data Mapper : l'entité ignore la persistance, un mapper séparé fait le pont (ex. [[Dev/Services/Prisma|Prisma]], [[Dev/Services/SQLAlchemy|SQLAlchemy]] core).
- Active Record : l'objet porte lui-même ses méthodes de persistance (`user.save()`).

### Schéma & migrations
- Le schéma de l'ORM sert souvent de source de vérité d'où sont **générées** les migrations — cf. [[Migrations de schéma]].

## En pratique

- Gagner en vitesse de développement et en typage ; éviter le SQL répétitif (CRUD).
- Garder une porte de sortie vers le **SQL brut** pour les requêtes complexes ou critiques en performance.
- Pièges : requêtes N+1 (chargement paresseux non maîtrisé), abstractions qui masquent le coût réel des requêtes, fuites d'abstraction sur les fonctions spécifiques d'un moteur.

## Approches voisines & alternatives

- Implémentation Dev : [[Dev/Services/Prisma|Prisma]] (ORM TypeScript).
- Écosystème Python : [[Dev/Services/SQLAlchemy|SQLAlchemy]] (Data Mapper de référence).
- Couche Pydantic + SQLAlchemy : [[Dev/Services/SQLModel|SQLModel]] (un seul modèle typé pour validation et persistance, orienté FastAPI).
- Plus bas niveau : query builders et SQL brut (contrôle maximal, moins d'abstraction).
- Concept parent : [[Wiki/Concepts/Bases de données|Bases de données]].

## Pour aller plus loin

- Comparatif des ORM : [[Comparatif - ORM]] (vue Dev).
- Notion connexe : [[Migrations de schéma]] (souvent fournies par l'ORM).
- Référence : *Patterns of Enterprise Application Architecture* (M. Fowler) pour Data Mapper / Active Record.
