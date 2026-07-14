---
galaxie: wiki
type: concept
nom: LLM benchmarks
alias: [bancs d'essai LLM, benchmarks LLM, leaderboard, MMLU, GPQA, BBH, IFEval, MT-Bench, Chatbot Arena, LMArena, HELM]
categorie: concept/llm
domaines: [ai-eng, ml-eng]
tags: [benchmark, llm-eval, model-evaluation, llm]
---

# LLM benchmarks

## Aperçu

- Un benchmark = un **jeu de tâches standardisé + une métrique agrégée**, qui permet de comparer des modèles sur une base commune. C'est la maille au-dessus des [[LLM eval metrics]] : une métrique appliquée à une suite figée.
- Sert à choisir un modèle, suivre les progrès du domaine et mesurer l'effet des [[Scaling laws|lois d'échelle]] — mais corrèle imparfaitement avec l'utilité réelle.

## Concepts clés

### Grandes familles
- **Connaissances / raisonnement** : MMLU, MMLU-Pro, GPQA (questions expertes), BBH.
- **Suivi d'instructions** : IFEval.
- **Préférences / chat** : MT-Bench ([[LLM-as-judge|juge]]), **Chatbot Arena / LMArena** (votes humains, classement Elo).
- **Spécialisés** : code et maths → [[Code and math benchmarks]] ; agents, sûreté, multilingue, long contexte.

### Statique vs vivant
- **Statique** : jeu figé (MMLU) — reproductible, mais se **sature** et se **contamine**.
- **Vivant** : arène à votes continus — résiste mieux au surajustement, au prix de la reproductibilité.

### Les deux maux
- **Contamination** : les questions fuitent dans les données d'entraînement → score gonflé. Parade : jeux **held-out** privés, benchmarks récents (questions postérieures au cutoff).
- **Saturation / Goodhart** : un benchmark visé cesse de discriminer ; « optimiser le benchmark » ≠ « être meilleur ».

## Les maths, simplement

- **Classement Elo** (arènes) : après un duel, $R'_A = R_A + K\,(S_A - E_A)$ avec $E_A = \dfrac{1}{1 + 10^{(R_B - R_A)/400}}$ — l'espérance de victoire de A. Beaucoup de duels → un classement stable à partir de jugements bruités.
- Score d'un benchmark = moyenne (souvent pondérée) des [[LLM eval metrics]] par tâche ; toujours regarder l'**intervalle de confiance**, pas le seul point.

## En pratique

- Lire un leaderboard avec méfiance : vérifier la **date** (contamination), le **prompt / few-shot** utilisé, et si le jeu est public.
- Préférer plusieurs benchmarks complémentaires + une éval **maison** sur sa propre tâche : c'est elle qui décide, pas MMLU.
- Pour le suivi d'instructions et le chat, les **arènes** et MT-Bench reflètent mieux l'usage réel que les QCM.
- Construire un mini-benchmark privé non publié pour ses cas d'usage → immunisé contre la contamination.

## Approches voisines & alternatives

- [[LLM eval metrics]] — les métriques qu'un benchmark agrège.
- [[Code and math benchmarks]] — la famille spécialisée la plus suivie.
- [[LLM-as-judge]] — moteur de MT-Bench et des arènes.
- [[Reasoning models]] — évalués sur les benchmarks de raisonnement les plus durs (GPQA, AIME).
- [[Scaling laws]] — les benchmarks mesurent ce que l'échelle fait gagner.
- [[Perplexity]] — métrique intrinsèque, hors benchmark de tâche.

## Pour aller plus loin

- Hendrycks et al. (2021) — *Measuring Massive Multitask Language Understanding* (MMLU).
- Rein et al. (2023) — *GPQA: A Graduate-Level Google-Proof Q&A Benchmark*.
- Chiang et al. (2024) — *Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference*.
