---
role: brique
nom: SDV
alias: [Synthetic Data Vault, sdv, sdv-dev]
pitch: "Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL)."
categorie: data/synthetique
famille: paquet
licence_type: source-available
maturite: production
langage: Python
alternatives: []
complements: []
tags: [synthetic-data, generative-model, gan]
url_docs: https://docs.sdv.dev/sdv
url_repo: https://github.com/sdv-dev/SDV
---

# SDV

<!-- AUTO:BANDEAU:START -->
> Génère des données tabulaires synthétiques en apprenant la distribution du réel — synthétiseurs statistiques (GaussianCopula) et profonds (CTGAN, TVAE) pour table unique, multi-tables relationnelles ou séquentielles, avec rapports de qualité ; licence source-available (BSL).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | source-available | en bibliothèque, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Synthèse tabulaire **par modèles** : SDV apprend les patterns d'un vrai jeu et en émet une
copie statistiquement proche, sans exposer les enregistrements d'origine. Là où un
générateur par règles tire chaque champ isolément, SDV modélise la **distribution jointe** —
corrélations, lois marginales, contraintes — à partir de métadonnées décrivant le schéma.
Plusieurs synthétiseurs couvrent le spectre, du statistique (GaussianCopula) au profond
(CTGAN, TVAE, CopulaGAN), sur table unique, base relationnelle entière (HMA, clés étrangères
suivies) ou séquences par entité (PAR). Des rapports de qualité et de diagnostic mesurent la
fidélité du résultat : l'étape n'est pas facultative, un synthétique plausible peut avoir
cassé une corrélation clé. Projet DataCebo, né au Data to AI Lab du MIT en 2016.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Partager ou tester sur des données sensibles sans diffuser le réel (PII, santé, finance) | Simples fixtures ou fakes, sans souci de distribution → [[Faker]], [[Mimesis]] |
| Augmenter un jeu tabulaire en préservant corrélations et lois marginales | Seulement rééquilibrer une classe minoritaire → [[imbalanced-learn]] (SMOTE), plus léger |
| Synthétiser une base relationnelle entière, clés étrangères comprises, ou des séquences par entité | Usage commercial de type *service de données synthétiques* : la Business Source License 1.1 l'interdit — chaque version bascule en MIT quatre ans après sa sortie |
| Mesurer la fidélité du synthétique produit (rapports qualité, diagnostics de validité) | Le synthétique n'est pas anonyme par défaut : sans contrôle, un modèle peut mémoriser et réémettre des lignes réelles |
| | Petits jeux : CTGAN et TVAE demandent du volume et du tuning, GaussianCopula est plus robuste là |

## Mise en œuvre

- Installation — `uv add sdv`
- Point d'entrée — import Python : métadonnées du schéma, puis un synthétiseur (`GaussianCopulaSynthesizer`, `CTGANSynthesizer`, `PARSynthesizer`…)
- Prérequis — les métadonnées décrivant le schéma ; assez de données pour les synthétiseurs profonds
- Exécution — single-node ; CPU pour GaussianCopula, GPU utile pour CTGAN et TVAE sur gros volumes
- Coût — gratuit en usage non commercial (BSL 1.1) ; SDV Enterprise, chez DataCebo, couvre l'usage commercial

## Écosystème

### Alternatives

- Aucune brique du brain ne couvre la synthèse tabulaire par modèles. Les voisins cités en `Écarter si` sont d'une autre nature : génération par règles, ou rééchantillonnage d'une seule classe.

## Ressources

- Documentation — https://docs.sdv.dev/sdv
- Dépôt — https://github.com/sdv-dev/SDV

## Voir aussi

- [[Synthetic data generation]] — la notion parente : ici, synthèse tabulaire par modèles appris
