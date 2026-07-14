---
galaxie: wiki
type: concept
nom: Reasoning models
alias: [modèles de raisonnement, reasoning model, large reasoning model, LRM, test-time compute, inference-time scaling, long chain-of-thought, thinking models]
categorie: concept/llm
domaines: [ai-eng]
tags: [reasoning, llm, alignment]
---

# Reasoning models

## Aperçu

- Un modèle de raisonnement **dépense du calcul à l'inférence** : il génère une longue **chaîne de pensée** interne (réflexion, retours en arrière, vérification) avant de répondre.
- Nouveau levier d'échelle : au lieu d'agrandir l'entraînement, on **augmente le compute au moment de répondre** (*test-time compute*). Plus le modèle « réfléchit », meilleure est la réponse sur les tâches difficiles.

## Concepts clés

### Test-time compute scaling
- Une **deuxième loi d'échelle**, orthogonale au pré-entraînement ([[Scaling laws]]) : la performance monte avec le nombre de tokens de raisonnement dépensés. D'où le réglage d'un « budget de réflexion ».

### Comment on les entraîne
- Surtout par **renforcement** sur des tâches **vérifiables** (maths, code) : le modèle est récompensé sur la **justesse finale** et découvre seul à raisonner. DeepSeek-R1 utilise **GRPO** (RL sans modèle de valeur séparé). Prolonge l'alignement ([[RLHF and DPO]]).
- La capacité à raisonner long **émerge** : les traces passent de centaines à des milliers de tokens au fil de l'entraînement.

### Chaîne de pensée native vs promptée
- Le [[Chain-of-Thought|chain-of-thought]] *prompté* demande à un LLM standard de détailler ses étapes ; un modèle de raisonnement l'a **internalisé** par entraînement et produit souvent une trace **cachée**.

### Exemples
- o1 / o3 (OpenAI, trace cachée), DeepSeek-R1 (ouvert, trace visible, janvier 2025), Qwen QwQ, Gemini « thinking ».

## Les maths, simplement

- Idée d'échelle : sur les tâches difficiles, $\text{perf} \approx a + b \log(\text{tokens de raisonnement})$ — gains réels mais à **coût et latence croissants** (chaque token de réflexion se paie).
- RL à récompense vérifiable : maximiser $\mathbb{E}[\,r(\text{réponse})\,]$ avec $r = 1$ si la réponse finale est correcte, en explorant des trajectoires de raisonnement (GRPO compare un **groupe** d'échantillons, sans critique séparée).

## En pratique

- À réserver aux tâches à **forte valeur de raisonnement** (maths, code, planification) ; sur des requêtes simples, c'est plus **lent et cher** sans gain, voire de l'*overthinking*.
- Régler le **budget de réflexion** (effort / longueur) selon la difficulté ; ne pas traiter la trace cachée comme une sortie fiable à parser.
- Servir un modèle de raisonnement = générer **beaucoup** de tokens → l'[[Inference optimization|optimisation d'inférence]] (KV-cache, batching) devient critique pour le coût.
- Surveiller la latence *time-to-answer* : la trace précède la réponse finale.

## Approches voisines & alternatives

- [[Chain-of-Thought]] — la version *promptée* ; les modèles de raisonnement l'internalisent.
- [[RLHF and DPO]] — même famille de post-training par renforcement ; ici la récompense est la justesse vérifiable.
- [[Scaling laws]] — le raisonnement ajoute l'axe **test-time** à l'échelle d'entraînement.
- [[Inference optimization]] — indispensable car les traces sont longues et coûteuses à générer.
- *GRPO*, *RL for LLMs*, *Reward modeling* (à créer) — la mécanique d'entraînement détaillée.
- Servir ces modèles : [[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]] (débit sur longues sorties).

## Pour aller plus loin

- DeepSeek-AI (2025) — *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*.
- OpenAI (2024) — *Learning to Reason with LLMs* (o1).
- Snell et al. (2024) — *Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Parameters*.
