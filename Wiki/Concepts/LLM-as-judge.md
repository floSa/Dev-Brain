---
galaxie: wiki
type: concept
nom: LLM-as-judge
alias: [LLM as a judge, LLM juge, LLM évaluateur, G-Eval, pairwise comparison, reference-free evaluation, MT-Bench]
categorie: concept/llm
domaines: [ai-eng]
tags: [llm-as-judge, llm-eval, llm]
---

# LLM-as-judge

## Aperçu

- Utiliser un LLM (souvent fort) pour **noter la sortie** d'un autre, selon des critères en langage naturel. Réponse à un problème dur : évaluer du texte libre à grande échelle, sans réponse de référence ni annotateurs humains.
- C'est le moteur des métriques **sans référence** (cf. [[RAG eval]], [[LLM eval metrics]]) et des arènes de [[LLM benchmarks]].

## Concepts clés

### Trois protocoles
- **Pointwise** : noter une sortie seule sur une échelle (1-5) ou un critère binaire.
- **Pairwise** : préférer A ou B — plus fiable que l'absolu ; base des arènes type Chatbot Arena.
- **Reference-guided** : juger en fournissant une réponse de référence au juge.

### Avec ou sans grille
- **G-Eval** : le juge produit d'abord les étapes d'évaluation ([[Chain-of-Thought]]) puis la note → plus stable.
- **Rubriques** : critères explicites (exactitude, complétude, ton) notés séparément, plutôt qu'un score global flou.

### Les biais (le point sensible)
- **Position** : préférence pour la 1ʳᵉ (ou 2ᵉ) réponse en pairwise → permuter et moyenner.
- **Verbosité** : biais pour les réponses longues.
- **Self-preference** : un juge préfère les sorties du même modèle / style.
- **Sensibilité** au format et au prompt de jugement.

## Les maths, simplement

- Accord juge ↔ humain mesuré par un **κ de Cohen** : $\kappa = \dfrac{p_o - p_e}{1 - p_e}$ ($p_o$ = accord observé, $p_e$ = accord attendu par hasard). Tant que κ n'est pas validé sur un échantillon humain, les scores du juge ne valent rien.
- En pairwise → **win rate** = part des comparaisons gagnées ; agrégé en classement (ex. Elo dans les arènes).

## En pratique

- **Calibrer avant de croire** : aligner le juge sur 30-50 jugements humains, mesurer l'accord, puis seulement automatiser.
- **Préférer le pairwise** au scoring absolu quand c'est possible (plus stable).
- **Neutraliser les biais** : permuter les positions, borner la longueur, fixer un modèle juge précis (versionné) pour la comparabilité dans le temps.
- Coût et latence non négligeables : un juge fort par requête peut coûter plus que la génération évaluée.
- Outiller : [[Dev/Services/DeepEval|DeepEval]] (G-Eval), [[Dev/Services/Ragas|Ragas]] (métriques reference-free), [[Dev/Services/TruLens|TruLens]] (feedback functions), [[Dev/Services/Langfuse|Langfuse]] (évals en ligne).

## Approches voisines & alternatives

- [[LLM eval metrics]] — le juge est une famille de métriques (sans référence) parmi d'autres.
- [[RAG eval]] — applique directement le LLM-as-judge (faithfulness, answer relevancy).
- [[LLM benchmarks]] — MT-Bench et les arènes reposent sur le jugement (LLM ou humain).
- [[LLM observability]] — le juge sert aussi à scorer en ligne le trafic de production.
- [[Chain-of-Thought]] — G-Eval fait raisonner le juge avant qu'il note.

## Pour aller plus loin

- Zheng et al. (2023) — *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Liu et al. (2023) — *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*.
