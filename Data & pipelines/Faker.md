---
role: brique
nom: Faker
alias: [faker, fake-factory, joke2k faker]
pitch: "Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos."
categorie: data/synthetique
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Mimesis]]"]
complements: []
tags: [synthetic-data, testing]
url_docs: https://faker.readthedocs.io/
url_repo: https://github.com/joke2k/faker
---

# Faker

<!-- AUTO:BANDEAU:START -->
> Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de données factices **par règles** : identités, adresses, emails, numéros,
entreprises, textes lorem, dates, IBAN. Le mécanisme tient en deux objets — des *providers*
thématiques qui savent fabriquer un type de valeur, et des *locales* (`fr_FR`, `en_US`…) qui
adaptent le réalisme culturel. Rien n'est appris d'un jeu réel : chaque champ est tiré
indépendamment des autres, ce qui rend le résultat plausible champ par champ et incohérent
d'un champ à l'autre. C'est la limite qui décide de l'usage — peupler une base de
démonstration ou des fixtures, oui ; reproduire la statistique d'un vrai jeu, non.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Peupler une base ou des fixtures de test avec des enregistrements crédibles (fixture `faker` fournie pour pytest) | Vitesse sur de très gros volumes → [[Mimesis]] |
| Anonymiser en remplaçant des PII par des valeurs factices du même type | Reproduire la distribution d'un vrai jeu tabulaire — corrélations, lois marginales → [[SDV]] |
| Générer des jeux de démonstration localisés, sur plusieurs langues ou pays | Nom et email doivent correspondre : les champs sont tirés indépendamment, la cohérence se câble à la main → [[SDV]] |
| Écrire un provider custom pour un domaine métier précis | Rééquilibrer une classe minoritaire par interpolation → [[imbalanced-learn]] |
| | Reproductibilité : sans `Faker.seed()` fixé, deux exécutions ne donnent pas le même jeu |
| | Unicité non garantie d'office : `fake.unique` la force, au risque d'épuiser l'espace de valeurs |

## Mise en œuvre

- Installation — `uv add Faker` ; le module s'importe `faker`
- Point d'entrée — import Python, `from faker import Faker` ; fixture `faker` côté pytest
- Prérequis — Python ≥ 3.10, aucune dépendance lourde
- Exécution — CPU, single-node, rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[Mimesis]] — Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.

## Ressources

- Documentation — https://faker.readthedocs.io/
- Dépôt — https://github.com/joke2k/faker

## Voir aussi

- [[Synthetic data generation]] — la notion parente : ici par règles, pas par modèle appris
