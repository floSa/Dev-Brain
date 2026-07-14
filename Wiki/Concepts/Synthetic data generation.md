---
galaxie: wiki
type: concept
nom: Synthetic data generation
alias: [synthetic data, génération de données synthétiques, données synthétiques, self-instruct, evol-instruct, distillation de données]
categorie: concept/llm
domaines: [ml-eng, ai-eng]
tags: [synthetic-data, fine-tuning, llm]
---

# Synthetic data generation

## Aperçu

- Utiliser un **LLM pour produire des données d'entraînement** — instructions, réponses, paires de préférences — quand la donnée humaine est rare, chère ou sensible.
- Alimente le [[SFT]] (démonstrations) et l'alignement ([[RLHF and DPO]], [[Reward modeling]]). La **qualité** des données prime ; la génération synthétique sert à l'**échelle** et à la **couverture** de cas rares.

## Concepts clés

### Pourquoi générer
- L'annotation humaine est **coûteuse et lente**. La génération synthétique permet de **passer à l'échelle**, de couvrir des **cas rares** ou dangereux, et d'éviter des données réelles **sensibles**.

### Techniques principales
- **Self-Instruct** : amorcer à partir de quelques exemples *seed*, demander au LLM d'en générer de nouveaux, filtrer, recommencer.
- **Evol-Instruct** : faire **complexifier** des instructions existantes par le LLM (plus difficiles, plus profondes) — base de WizardLM.
- **Distillation** : un **modèle fort** (teacher) génère des réponses pour entraîner un **modèle plus petit** (student). Attention aux **licences** du teacher.
- **Paires de préférences** : un juge LLM ([[LLM-as-judge]], **RLAIF**) classe des réponses pour fabriquer les comparaisons du [[Reward modeling]].

### Qualité & filtrage
- Le levier décisif n'est pas le volume mais le **filtrage** : déduplication, **vérification** (exécuter le code, valider le résultat mathématique), scoring par récompense ou par juge, contrôle de la **diversité**.
- C'est du **rejection sampling** : générer beaucoup, ne **garder** que ce qui passe le filtre.

### Pièges
- **Model collapse** : entraîner un modèle sur ses propres sorties, en boucle, **dégrade** la distribution (perte des queues, homogénéisation).
- **Amplification de biais** du modèle générateur, **contamination de benchmarks** (fuite de données de test), et **licences** interdisant la distillation d'un modèle propriétaire.

## Les maths, simplement

- **Rejection sampling** : on génère un grand pool $\{(x, y_j)\}$ et on ne retient que le sous-ensemble qui passe un **vérificateur / seuil** : $\mathcal{D} = \{(x,y) : v(x,y) = 1\}$, où $v$ teste la correction (code qui passe, résultat juste) ou un score de récompense au-dessus d'un seuil.
- Pas d'équation centrale : la génération synthétique est surtout un **pipeline** (générer → filtrer → mélanger). La règle empirique « **qualité > quantité** » (LIMA) reste le guide.

## En pratique

- Soigner le **seed set** : sa qualité et sa diversité se propagent à tout le reste.
- **Filtrer agressivement** : un petit jeu propre bat un gros jeu bruité (cf. [[SFT]]).
- **Mélanger** avec de la donnée réelle et **plafonner** la part synthétique pour limiter le model collapse.
- Choisir le **teacher** en connaissance des **licences** ; documenter la provenance pour éviter la contamination de benchmarks.
- Outils : `distilabel`, `TRL`, APIs de LLM forts ; vérificateurs (exécution code, solveurs) pour le filtrage.

## Approches voisines & alternatives

- [[SFT]] — premier consommateur : les démonstrations synthétiques remplacent les humaines.
- [[RLHF and DPO]] / [[Reward modeling]] — les **paires de préférences** synthétiques (RLAIF) alimentent l'alignement.
- [[LLM-as-judge]] — sert au **filtrage** et à la fabrication des préférences.
- *RLVR / récompenses vérifiables* (cf. [[Reasoning models]]) — le filtrage par **vérification** rejoint la génération de traces de raisonnement correctes.

### Outils — données tabulaires & factices (hors LLM)

- [[Dev/Services/SDV|SDV]] — synthèse **tabulaire par modèles** (GaussianCopula, CTGAN, TVAE) : apprend la distribution d'un vrai jeu et l'émule (table unique, relationnel, séquentiel).
- [[Dev/Services/Faker|Faker]] — génération de **données factices par règles** (providers, locales) pour tests, fixtures, démos.
- [[Dev/Services/Mimesis|Mimesis]] — même usage que Faker, **plus rapide** et entièrement typé.

## Pour aller plus loin

- Wang et al. (2022) — *Self-Instruct: Aligning Language Models with Self-Generated Instructions*.
- Xu et al. (2023) — *WizardLM: Evol-Instruct*.
- Shumailov et al. (2024) — *The Curse of Recursion / model collapse* (Nature).
