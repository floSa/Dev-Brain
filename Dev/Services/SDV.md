---
galaxie: dev
type: service
nom: SDV
alias: [Synthetic Data Vault, sdv, sdv-dev]
pitch: "Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL)."
categorie: ml/framework
licence_type: source-available
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [synthetic-data, generative-model, gan]
url_docs: https://docs.sdv.dev/sdv
url_repo: https://github.com/sdv-dev/SDV
---

# SDV

## Pourquoi

SDV (Synthetic Data Vault, projet DataCebo, né au Data to AI Lab du MIT en 2016) **apprend les patterns d'un vrai jeu tabulaire** et en émet une copie **synthétique** statistiquement proche, sans exposer les enregistrements d'origine. Contrairement à [[Dev/Services/Faker|Faker]] / [[Dev/Services/Mimesis|Mimesis]] (valeurs tirées par règles), SDV **modélise la distribution jointe** : corrélations, marginales, contraintes. Il offre plusieurs synthétiseurs, du statistique (**GaussianCopula**) au profond (**CTGAN**, **TVAE**, CopulaGAN), pilotés par des **métadonnées** décrivant le schéma. Couvre la **table unique**, le **multi-tables relationnel** (HMA) et le **séquentiel** (PAR), avec des rapports de **qualité** et de diagnostic.

## Quand l'utiliser

- Partager / tester sur des données **sensibles** sans diffuser le réel (PII, santé, finance).
- Augmenter un jeu tabulaire en préservant **corrélations et lois marginales**.
- Synthétiser une **base relationnelle** entière (clés étrangères) ou des **séries** par entité.
- Mesurer la fidélité du synthétique (rapports qualité, diagnostics de validité).

## Quand NE PAS l'utiliser

- Simples **fixtures / fakes** sans souci de distribution → [[Dev/Services/Faker|Faker]], [[Dev/Services/Mimesis|Mimesis]] (plus simples, plus rapides).
- Seulement **rééquilibrer une classe minoritaire** → [[Dev/Services/imbalanced-learn|imbalanced-learn]] (SMOTE), plus léger.
- Usage **commercial de type service de données synthétiques** : la licence BSL l'interdit (voir ci-dessous).

## Déploiement & coût

- **Source-available** : Business Source License 1.1 — gratuit en usage non commercial ; interdit d'en faire un *Synthetic Data Service* commercial. Chaque version **bascule en MIT** 4 ans après sa sortie.
- `uv add sdv`. Rien à héberger ; calcul **single-node**. CTGAN / TVAE entraînent un réseau (GPU utile pour les gros volumes), GaussianCopula reste léger (CPU).
- Offre managée séparée (SDV Enterprise) chez DataCebo pour l'usage commercial.

## Pièges

- **Licence BSL** : vérifier la conformité avant tout usage commercial — ce n'est pas de l'open-source au sens OSI.
- Le synthétique **n'est pas anonyme par défaut** : sans contrôle, un modèle peut mémoriser et réémettre des lignes réelles ; valider la confidentialité.
- CTGAN / TVAE demandent **assez de données** et du tuning ; sur petits jeux, GaussianCopula est souvent plus robuste.
- Toujours **évaluer la fidélité** (rapports qualité) avant d'exploiter le jeu généré — un synthétique plausible peut casser des corrélations clés.

## Alternatives

Pas d'équivalent direct dans le brain. Briques voisines mais de **nature différente** : [[Dev/Services/Faker|Faker]] et [[Dev/Services/Mimesis|Mimesis]] génèrent des fakes par règles (pas de distribution apprise) ; [[Dev/Services/imbalanced-learn|imbalanced-learn]] (SMOTE) synthétise des exemples minoritaires par interpolation, sans modèle génératif global.

## Liens

- [[Synthetic data generation]] — le concept parent : ici, synthèse tabulaire par modèles appris (vs génération par LLM).
- [[Dev/Services/Faker|Faker]] / [[Dev/Services/Mimesis|Mimesis]] — génération par règles, le pendant simple.
- [[Dev/Services/imbalanced-learn|imbalanced-learn]] — synthèse ciblée de classe minoritaire (SMOTE).
- Doc : https://docs.sdv.dev/sdv
