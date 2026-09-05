---
role: brique
nom: Mimesis
alias: [mimesis, lk-geimfari mimesis]
pitch: "Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test."
categorie: data/synthetique
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Faker]]"]
complements: []
tags: [synthetic-data, testing]
url_docs: https://mimesis.name/
url_repo: https://github.com/lk-geimfari/mimesis
---

# Mimesis

<!-- AUTO:BANDEAU:START -->
> Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Générateur de données factices qui couvre le même besoin que Faker en misant sur deux
choses : la vitesse et le typage. Entièrement typé, il donne l'autocomplétion dans un code
base annoté, tourne de l'ordre de dix fois plus vite que Faker et produit davantage de
valeurs uniques — ce qui le rend tenable sur de grands volumes de test. Son objet
distinctif est le **Schema** déclaratif : au lieu d'appeler chaque provider à la main, on
décrit d'un coup la forme complète d'un enregistrement, champs imbriqués et références entre
schémas compris. Comme tout générateur par règles, il tire les champs indépendamment : la
cohérence entre eux reste à câbler.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Générer de grands jeux de test où la vitesse compte : seed de bases, benchmarks | Écosystème déjà bâti autour de Faker — fixtures pytest, extensions tierces → [[Faker]] ; l'API diffère, ce n'est pas un remplacement drop-in |
| Profiter du typage strict et de l'autocomplétion dans un code base annoté | Reproduire la distribution d'un vrai jeu tabulaire → [[SDV]] |
| Décrire la forme complète d'un enregistrement via le `Schema` (champs imbriqués, références entre schémas) | Rééchantillonnage synthétique de classe minoritaire → [[imbalanced-learn]] |
| Locales multiples, avec des providers custom | Cohérence inter-champs : les champs sont tirés indépendamment, à câbler via `Schema` et handlers |

## Mise en œuvre

- Installation — `uv add mimesis`
- Point d'entrée — import Python : providers thématiques, ou `Schema` déclaratif pour un enregistrement entier
- Prérequis — Python ≥ 3.10, aucune dépendance lourde
- Exécution — CPU, single-node, rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.

## Ressources

- Documentation — https://mimesis.name/
- Dépôt — https://github.com/lk-geimfari/mimesis

## Voir aussi

- [[Synthetic data generation]] — la notion parente : produire de la donnée de substitution, ici par règles
