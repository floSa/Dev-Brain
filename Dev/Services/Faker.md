---
galaxie: dev
type: service
nom: Faker
alias: [faker, fake-factory, joke2k faker]
pitch: "Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Mimesis|Mimesis]]"]
remplace_par: []
status: actif
tags: [synthetic-data, testing]
url_docs: https://faker.readthedocs.io/
url_repo: https://github.com/joke2k/faker
---

# Faker

## Pourquoi

Faker (importé `faker`, paquet PyPI `Faker`, par joke2k / Daniele Faraglia) génère des **données factices** plausibles : identités, adresses, emails, numéros, entreprises, textes lorem, dates, IBAN, etc. Le mécanisme repose sur des **providers** thématiques et un large jeu de **locales** (`fr_FR`, `en_US`…) qui adaptent le réalisme culturel. C'est de la génération **par règles**, pas un apprentissage de distribution : utile pour remplir une base de démonstration ou des fixtures de test, pas pour reproduire la statistique d'un jeu réel.

## Quand l'utiliser

- Peupler une base / des fixtures de test avec des enregistrements crédibles (la fixture `faker` est fournie pour pytest).
- Anonymiser en remplaçant des PII par des valeurs factices du même type.
- Générer des jeux de démonstration localisés (plusieurs langues / pays).
- Écrire un provider custom pour un domaine métier précis.

## Quand NE PAS l'utiliser

- Besoin de **vitesse** sur de très gros volumes → [[Dev/Services/Mimesis|Mimesis]] (entièrement typé, nettement plus rapide).
- Reproduire la **distribution statistique** d'un vrai jeu tabulaire (corrélations, lois marginales) → [[Dev/Services/SDV|SDV]] (synthèse par modèles).
- Rééquilibrer une classe minoritaire par interpolation → [[Dev/Services/imbalanced-learn|imbalanced-learn]] (SMOTE).

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add Faker`. Rien à héberger. Python ≥ 3.10.
- Calcul **single-node**, CPU. Pas de dépendance lourde.

## Pièges

- Données **réalistes mais incohérentes entre elles** : email et nom tirés indépendamment ne correspondent pas par défaut ; câbler soi-même les dépendances.
- Sans `seed` fixé (`Faker.seed()`), les jeux ne sont pas reproductibles.
- Unicité non garantie d'office : utiliser `fake.unique` au risque d'épuiser l'espace de valeurs.
- Plus lent que les alternatives typées sur les gros volumes.

## Alternatives

- [[Dev/Services/Mimesis|Mimesis]] — Générateur de données factices Python rapide et entièrement typé — API par providers et schémas déclaratifs ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.
- [[Dev/Services/SDV|SDV]] — autre nature : apprend la distribution d'un vrai jeu tabulaire au lieu de tirer des valeurs par règles.

## Liens

- [[Synthetic data generation]] — le concept parent : générer de la donnée quand le réel manque (ici par règles, pas par modèle).
- [[Dev/Services/Mimesis|Mimesis]] — l'alternative directe, plus rapide.
- Doc : https://faker.readthedocs.io/
