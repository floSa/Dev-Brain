---
galaxie: wiki
type: concept
nom: Code and math benchmarks
alias: [benchmarks code, benchmarks maths, HumanEval, MBPP, SWE-bench, GSM8K, MATH, AIME, pass@k, éval par exécution]
categorie: concept/llm
domaines: [ai-eng, ml-eng]
tags: [benchmark, code-generation, reasoning, llm-eval, llm]
---

# Code and math benchmarks

## Aperçu

- Sous-famille des [[LLM benchmarks]] où la réponse est **vérifiable mécaniquement** : on exécute le code ou on vérifie le résultat numérique. Pas besoin de [[LLM-as-judge|juge]] ni de référence floue — la métrique est objective.
- C'est le terrain où se mesurent surtout les [[Reasoning models]].

## Concepts clés

### Côté code
- **HumanEval, MBPP** : générer une fonction à partir d'un énoncé, validée par des **tests unitaires**.
- **SWE-bench** : résoudre de vraies issues GitHub sur des dépôts entiers → mesure des capacités d'**agent de code**, pas seulement de complétion.
- Métrique reine : **pass@k** (au moins 1 des $k$ générations passe les tests).

### Côté maths
- **GSM8K** : problèmes arithmétiques de primaire (raisonnement multi-étapes).
- **MATH** : problèmes de compétition (lycée / olympiades).
- **AIME, GPQA** : très difficiles, peu saturés — la nouvelle barre des modèles de raisonnement.
- Vérification par **réponse finale exacte** (et parfois par étapes).

### Pourquoi ils comptent
- Éval **objective et automatisable** : idéale pour l'entraînement (signal de récompense vérifiable, RL) et la CI.
- Discriminants : laissent encore de la marge quand les QCM saturent.

## Les maths, simplement

- **pass@k** $= \mathbb{E}\left[\,1 - \dfrac{\binom{n-c}{k}}{\binom{n}{k}}\,\right]$ : sur $n$ générations dont $c$ passent les tests, probabilité qu'un tirage de $k$ en contienne au moins une bonne. À $k = 1$, c'est le taux de réussite brut.
- Avantage clé : le **vérificateur** (tests, calcul) est sûr — pas de bruit de juge, pas de biais de format.

## En pratique

- Vérifier la **contamination** : GSM8K et HumanEval sont anciens et largement fuités → préférer MATH, SWE-bench, AIME récents.
- Distinguer **complétion** (HumanEval) et **agent** (SWE-bench) : ce ne sont pas les mêmes capacités.
- Le **prompt** compte énormément ([[Chain-of-Thought]], auto-vérification) : reporter les conditions exactes.
- Pour ses propres besoins : construire un petit jeu d'exécution privé (entrées → sorties attendues) plutôt que se fier au leaderboard.

## Approches voisines & alternatives

- [[LLM benchmarks]] — la famille générale dont ceci est la spécialisation vérifiable.
- [[Reasoning models]] — entraînés et mesurés en priorité sur ces tâches.
- [[Chain-of-Thought]] — le levier de prompt qui débloque le raisonnement multi-étapes.
- [[LLM eval metrics]] — l'« éval par exécution » est une de ses familles.

## Pour aller plus loin

- Chen et al. (2021) — *Evaluating Large Language Models Trained on Code* (HumanEval, pass@k).
- Cobbe et al. (2021) — *Training Verifiers to Solve Math Word Problems* (GSM8K).
- Jimenez et al. (2023) — *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*
