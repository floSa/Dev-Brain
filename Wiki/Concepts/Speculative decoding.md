---
galaxie: wiki
type: concept
nom: Speculative decoding
alias: [décodage spéculatif, speculative sampling, échantillonnage spéculatif, draft model, modèle brouillon, EAGLE, Medusa, DSpark, DeepSpec, semi-autoregressive, ordonnanceur de confiance]
categorie: concept/llm
domaines: [ai-eng]
tags: [inference-optimization, decoding, llm, inference]
---

# Speculative decoding

## Aperçu

- Le décodage spéculatif **accélère la génération** : un modèle rapide (brouillon) propose plusieurs tokens d'avance, que le grand modèle **vérifie en une seule passe**. Typiquement **2–3×** plus rapide.
- Propriété clé : la sortie est **distributionnellement identique** à celle du grand modèle seul — accélération **sans perte de qualité**.

## Concepts clés

### Brouillon puis vérification
- Un **drafter** (petit modèle, têtes auxiliaires, ou n-grammes) génère $k$ tokens candidats. Le **modèle cible** les évalue **en parallèle** (un seul forward), accepte le plus long préfixe cohérent et rejette le reste.
- Le gain vient du régime *memory-bound* du decode : vérifier $k$ tokens d'un coup coûte presque autant qu'en générer un, car le goulot est la lecture des poids, pas le calcul (cf. [[Inference optimization]]).

### Acceptation et correction
- Un critère d'acceptation (rejection sampling) garantit que la distribution finale est **exactement** celle du modèle cible. Le nombre de tokens acceptés par passe (*acceptance length*) détermine l'accélération réelle.

### Familles de méthodes
- **Draft model séparé** : un petit modèle de la même famille (formulation d'origine, Leviathan / Chen 2023).
- **Medusa** : des têtes de décodage supplémentaires greffées sur le modèle, pas de second modèle ; vérification en arbre.
- **EAGLE (1 → 3)** : prédiction au niveau des *features* plutôt que des tokens ; devenu le **standard de fait** (2025), meilleurs taux d'acceptation.
- **Self-speculative / n-gram / prompt lookup** : brouillon tiré du modèle lui-même ou du contexte, sans entraînement.
- **[[Multi-Token Prediction|MTP]]** : le modèle porte ses propres têtes de brouillon, apprises pendant le pré-entraînement. La configuration « MTP-1 » (un token d'avance) est la **baseline de production** contre laquelle se mesurent les frameworks plus ambitieux.

### DSpark : profondeur de vérification pilotée par la charge (2026)
- Publié par DeepSeek avec l'Université de Pékin (fin juin 2026, codebase **DeepSpec** sous licence MIT). Le cadre reste brouillon-puis-vérification ; l'apport est **ordonnancemental**, pas algorithmique au sens du critère d'acceptation.
- **Brouillon semi-autorégressif** — au lieu d'un brouillon purement parallèle (positions indépendantes, incohérentes) ou purement séquentiel (lent), un tronc parallèle est couplé à un petit module séquentiel qui modélise les dépendances **à l'intérieur** du bloc proposé. Cela freine la dégradation de qualité du brouillon quand on propose loin.
- **Vérification ordonnancée par la confiance** — c'est l'idée centrale. Une tête de confiance estime, **avant** de vérifier, la probabilité de survie de chaque préfixe de brouillon. L'ordonnanceur croise cette estimation avec un **profil de débit mesuré** du moteur et fixe une longueur de vérification **par requête**.
  - GPU sous-utilisé → vérifier profond, la capacité est gratuite. GPU saturé → vérifier court, chaque token vérifié en trop retire du débit à d'autres utilisateurs. On ne joue donc que les paris rentables **compte tenu de la charge**.
- Résultat annoncé : **+60 à 85 %** de vitesse de génération **par utilisateur** sur DeepSeek-V4-Flash (+57 à 78 % sur V4-Pro), **à débit agrégé équivalent** et face à la baseline MTP-1. Le « à débit égal » est la clause importante : le gain est une meilleure répartition de la capacité, pas de la capacité créée.
- Précision utile : l'ordonnanceur agit sur **combien** de tokens sont proposés et vérifiés, pas sur la règle d'acceptation. Les poids du modèle cible ne changent pas. Le papier ne revendique cependant pas explicitement l'exactitude distributionnelle dans son résumé — à vérifier dans le corps du texte avant de promettre du « sans perte » sur un projet.

## Les maths, simplement

- Accélération $\approx$ *acceptance length* $\alpha$ (tokens acceptés par passe), atténuée par le surcoût du brouillon : plus $\alpha$ est élevé, plus le gain approche $\alpha$. Si le brouillon vise mal (peu accepté), le gain s'effondre, voire devient négatif.
- Acceptation par rejection sampling : accepter le token brouillon $x$ avec probabilité $\min\!\big(1,\ \tfrac{p_{\text{cible}}(x)}{q_{\text{brouillon}}(x)}\big)$, sinon rééchantillonner sur la distribution résiduelle → la distribution finale égale $p_{\text{cible}}$.

## En pratique

- Gain maximal sur les sorties **prévisibles** (code, texte structuré) où le brouillon vise juste ; faible sur du texte très entropique.
- Le brouillon doit être **bien plus rapide** que la cible et **aligné** avec elle (même famille / tokenizer).
- Activable nativement dans les runtimes : [[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]], [[Dev/Services/TGI|TGI]] et [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] supportent draft model et/ou EAGLE/Medusa.
- N'améliore **pas** le *time-to-first-token* (prefill) : c'est une optimisation du **decode**.
- **Lire les annonces de gain avec méfiance** : « 2× plus rapide » ne veut rien dire sans préciser (a) par utilisateur ou en débit agrégé, (b) à quelle charge, (c) contre quelle baseline. Un gain par utilisateur mesuré sur une machine vide s'évapore souvent à concurrence réelle — c'est précisément le problème que DSpark attaque en pilotant la profondeur de vérification sur la charge.

## Approches voisines & alternatives

- [[Inference optimization]] — le décodage spéculatif en est un cas ; partage le régime memory-bound du decode.
- [[Multi-Token Prediction]] — la source de brouillon intégrée au modèle : entraînée avec lui, elle sert de baseline (MTP-1) au reste de la famille.
- [[Decoding strategies]] — le spéculatif change *la vitesse* de génération, pas le choix du token (distribution inchangée).
- [[Quantization]] — accélération sans spéculation, orthogonale et cumulable : réduit les octets à lire, ce qui attaque le même goulot memory-bound.
- [[Calculs adaptatifs]] — autre façon de moduler le calcul selon la difficulté, au niveau des couches traversées plutôt que des tokens validés par passe.
- Accélération **sans** spéculation : [[Inference optimization|continuous batching, KV-cache, paged attention]].

## Pour aller plus loin

- Leviathan et al. (2023, Google) — *Fast Inference from Transformers via Speculative Decoding*.
- Chen et al. (2023, DeepMind) — *Accelerating Large Language Model Decoding with Speculative Sampling*.
- Cai et al. (2024) — *Medusa* ; Li et al. (2024–2025) — *EAGLE / EAGLE-3*.
- DeepSeek & Université de Pékin (2026) — *DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation* (arXiv 2607.05147) ; codebase **DeepSpec**, MIT.
