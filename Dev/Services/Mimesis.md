---
galaxie: dev
type: service
nom: Mimesis
alias: [mimesis, lk-geimfari mimesis]
pitch: "Générateur de données factices Python rapide et entièrement typé — providers et schémas déclaratifs, dizaines de locales ; nettement plus rapide que Faker, pensé pour de gros volumes de données de test."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Faker|Faker]]"]
remplace_par: []
status: actif
tags: [synthetic-data, testing]
url_docs: https://mimesis.name/
url_repo: https://github.com/lk-geimfari/mimesis
---

# Mimesis

## Pourquoi

Mimesis (par lk-geimfari) couvre le même besoin que [[Dev/Services/Faker|Faker]] — générer des **données factices** localisées (identités, adresses, finances, internet, texte…) — mais en misant sur la **performance** et le **typage**. Entièrement typé (autocomplétion), il est de l'ordre de **10× plus rapide** que Faker et produit davantage de valeurs uniques, ce qui le rend adapté aux **gros volumes** de données de test. Son **Schema** déclaratif décrit d'un coup la structure d'un enregistrement (champs imbriqués, relations) au lieu d'appeler chaque provider à la main.

## Quand l'utiliser

- Générer de **grands jeux** de test où la vitesse compte (seed de bases, benchmarks).
- Profiter du **typage strict** et de l'autocomplétion dans un code base typé.
- Décrire la forme complète d'un enregistrement via le **Schema** (champs, structures imbriquées, références entre schémas).
- Locales multiples (dizaines de langues) avec des providers custom.

## Quand NE PAS l'utiliser

- Écosystème / intégrations déjà bâtis autour de Faker (fixtures pytest `faker`, extensions tierces) → rester sur [[Dev/Services/Faker|Faker]].
- Reproduire la **distribution** d'un vrai jeu tabulaire → [[Dev/Services/SDV|SDV]].
- Rééchantillonnage synthétique de classe minoritaire → [[Dev/Services/imbalanced-learn|imbalanced-learn]].

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add mimesis`. Rien à héberger. Python récent (≥ 3.10).
- Calcul **single-node**, CPU, sans dépendance lourde.

## Pièges

- API et organisation des providers **différentes de Faker** : pas un remplacement drop-in, la migration demande de réécrire les appels.
- Comme Faker, les champs sont tirés **indépendamment** : pas de cohérence inter-champs sans la câbler (ou via Schema + handlers).
- Écosystème d'extensions tierces plus restreint que celui de Faker.

## Alternatives

- [[Dev/Services/Faker|Faker]] — Génère des données factices réalistes en Python — noms, adresses, emails, textes, dates — via un système de providers et des dizaines de locales ; le standard pour peupler tests, fixtures et démos.
- [[Dev/Services/SDV|SDV]] — autre nature : synthèse par modèles apprise sur un vrai jeu tabulaire.

## Liens

- [[Synthetic data generation]] — le concept parent : produire de la donnée de substitution (ici par règles, pas par modèle).
- [[Dev/Services/Faker|Faker]] — l'alternative de référence, plus établie mais plus lente.
- Doc : https://mimesis.name/
