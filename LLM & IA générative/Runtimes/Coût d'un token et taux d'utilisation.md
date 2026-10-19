---
role: notion
nom: Coût d'un token et taux d'utilisation
alias: [coût par million de tokens, coût d'inférence, marge d'un fournisseur de modèles ouverts, taux d'utilisation des GPU, utilisation GPU, économie de l'inférence, coût de production d'un token, seuil de rentabilité d'un GPU, tokenomics]
categorie: llm/runtime
domaines: [ai-eng, mlops]
tags: [inference-optimization, inference, llm, gpu, model-serving]
---

# Coût d'un token et taux d'utilisation

## Aperçu

- Le coût de production d'un million de tokens se calcule avec trois nombres : le loyer horaire d'un GPU `p`, le débit `v` qu'il atteint saturé, et le **taux d'utilisation** `u` (la part de ce débit réellement produite et facturée sur les heures louées) : `c = 10⁶ · p ÷ (3600 · v · u)`.
- La marge d'un fournisseur de modèles ouverts se joue sur `u`. Exemple chiffré : un modèle à experts de très grande taille sur B200, à 9 734 tokens/s par GPU, un GPU loué 8,19 $/h et un prix de vente de 1,61 $ le million de tokens : la marge sur le seul poste GPU vaut **86 % à pleine utilisation** et **3 % à 15 %**, au même prix de vente. Le seuil de rentabilité est à 14,5 % d'utilisation.

## Concepts clés

### Les trois nombres

- `p` : le loyer d'un GPU en dollars par heure (location à la demande, contrat, ou amortissement du matériel acheté, électricité comprise).
- `v` : le débit **agrégé** d'un GPU à un lot donné, en tokens par seconde, entrée et sortie comptées ensemble si le prix les mélange. Ce n'est pas le plafond d'un utilisateur (cf. [[Plafond de débit d'un GPU (roofline)]]) : `v ≈ B × v_utilisateur` tant que la mémoire le permet.
- `u` : le taux d'utilisation. Il réunit deux pertes : le GPU qui attend faute de requêtes, et le GPU qui tourne à un lot plus petit que son lot optimal.

### Ce qui fait baisser `c`

Chaque levier de [[Inference optimization]] agit sur `v` ou sur le prix d'une partie des tokens :

| Levier | Effet sur le coût d'un token | Contrepartie |
|---|---|---|
| Batching continu | ↓ fort jusqu'à saturation mémoire : le coût baisse presque en `1/B` | latence par utilisateur ; capacité mémoire |
| Cache de préfixe | ↓ sur l'**entrée** seulement (jusqu'à 50 fois moins cher qu'un token non caché sur des tarifs relevés) | mémoire retenue ; préfixe exact |
| Quantization (FP8, FP4) | ↓ (environ ×1,5 de débit sur un cas mesuré) | perte de qualité variable |
| Noyaux, fusion, FlashAttention | ↓ non chiffrable de l'extérieur | noyaux à maintenir |
| Décodage spéculatif | surtout une vitesse vendue, peu de coût au lot saturé | gain nul à grand lot |
| Matériel plus récent | un facteur de 5 à 7 relevé entre H200 et B200 sur un même banc, sans comparaison contrôlée | investissement |

Le batching est la raison pour laquelle le volume baisse le coût moyen ; la mémoire est ce qui le limite : au-delà de la capacité (cf. [[Dimensionner la mémoire d'un serveur LLM]]), il faut un GPU de plus.

### Pourquoi la marge dépend de `u`

À prix de vente fixe, `u` est un facteur multiplicatif direct sur le coût. Un fournisseur à 15 % d'utilisation paie le même GPU qu'un fournisseur à 80 %, et produit six fois moins de tokens facturés. Le débit mesuré par un banc (charge régulière, parc sans panne) est le `v` de la formule ; l'écart avec le trafic réel (longueurs variables, pointes et creux, exigences de latence) **est** `u`.

### Qui porte le risque d'inutilisation

Un loueur de GPU avec contrats « take-or-pay » reporte le risque sur son client. Une plateforme d'inférence qui s'engage sur des contrats longs puis vend au token le porte elle-même ; celle qui loue à la demande le limite, mais paie un loyer plus élevé (B200 : 8,19 $/h à la demande, 6,79 $/h à partir de 91 jours de contrat chez un même fournisseur, relevé le 2026-10-04). Pour qui héberge sur site, le même calcul s'applique avec `p` = amortissement : un GPU « gratuit » est un coût fixe, qui ne gagne que s'il est utilisé.

## Les maths, simplement

- `c = 10⁶ · p ÷ (3600 · v · u)` en dollars par million de tokens. Marge brute sur le poste GPU : `m = 1 − c ÷ P` avec `P` le prix de vente par million. Taux d'utilisation de rentabilité : `u* = c(u=1) ÷ P`.
- Exemple (modèle à experts sur B200, `v = 9 734` tokens/s par GPU, `P = 1,61 $` pour un mélange 8 tokens d'entrée pour 1 de sortie) :

| Loyer du GPU | `u` = 100 % | 80 % | 50 % | 30 % | 15 % |
|---|---:|---:|---:|---:|---:|
| 3,69 $/h | 0,11 $ | 0,13 $ | 0,21 $ | 0,35 $ | 0,70 $ |
| 6,00 $/h | 0,17 $ | 0,21 $ | 0,34 $ | 0,57 $ | 1,14 $ |
| 8,19 $/h | 0,23 $ | 0,29 $ | 0,47 $ | 0,78 $ | 1,56 $ |
| 13,00 $/h | 0,37 $ | 0,46 $ | 0,74 $ | 1,24 $ | 2,47 $ |

Marge à 8,19 $/h : 86 % à `u` = 1, 71 % à 50 %, 52 % à 30 %, 3 % à 15 %. Seuil de rentabilité : 10,6 % d'utilisation à 6 $/h, 14,5 % à 8,19 $/h. À `u` = 1 et 6 $/h, huit GPU produisent 280 millions de tokens par heure pour 48 $, soit 0,17 $ le million. Le débit par GPU vient d'un banc public configuré sur 64 GPU désagrégés : c'est un ordre de grandeur, pas une mesure d'un nœud de huit.

- **Ce que le calcul n'inclut pas** : réseau, stockage, ingénieurs, GPU de secours, pannes. C'est un majorant de la marge brute réelle. Le prix réel encaissé est inférieur au tarif catalogue (cache, tarifs creux, remises, traitement par lots).

## En pratique

- Avant de juger un tarif ou un projet d'hébergement : demander `v`, `p` et `u`. Un « prix par million de tokens » sans les trois ne se lit pas.
- Pour un usage sur site avec un GPU acheté : estimer l'utilisation **réelle** (heures de requêtes sur heures d'ouverture), pas l'utilisation du banc. À faible volume, l'API coûte souvent moins ; à volume saturé, le local coûte moins.
- Ne pas déduire du tarif catalogue le coût d'une **tâche** : le nombre de tokens consommés par tâche varie d'un modèle à l'autre.
- Aucune plateforme d'inférence privée ne publie son taux d'utilisation ni sa marge brute ; les chiffres qui circulent sont des estimations d'agrégateurs ou des hypothèses de modèle. Une levée de fonds, une valorisation ou un revenu annualisé n'est pas un bénéfice.

## Repères datés

Relevé le 2026-10-04 dans le cours de floSa ; les prix et les bancs changent en quelques semaines. À relire à la source avant usage ; ces valeurs n'ont pas été rouvertes à leur source pour cette page (la formule et les tableaux, eux, sont recalculés).

- Banc InferenceX (SemiAnalysis), DeepSeek-V4-Pro, B200, FP4 pour les experts, séquences de 8 000 tokens en entrée et 1 000 en sortie, SGLang sous Dynamo, 48 GPU de prefill et 16 de decode, exécution du 2026-09-01 : 9 734 tokens/s par GPU, 22,7 tokens/s par utilisateur. Sur 8 H200 : 707 (SGLang) à 1 427 (vLLM) tokens/s par GPU, exécutions du 2026-07-14.
- Tarif de l'API de l'éditeur, heures pleines : 1,32 $ en entrée, 3,96 $ en sortie par million de tokens ; entrée « cache touché » 0,044 $ (30 fois moins) ; un autre modèle du même éditeur : 0,30 $ contre 0,006 $ (50 fois moins).
- Loyers B200 à la demande : de 3,69 $/h à 13,00 $/h selon le fournisseur.
- Taux d'utilisation : seuls chiffres lus, tous non transposables : environ 82 % d'occupation des nœuds de l'éditeur DeepSeek en 2025 (occupation, pas utilisation des GPU), 60 % d'hypothèse du modèle de coût de SemiAnalysis, 5 % de moyenne tous usages sur des clusters Kubernetes (rapport Cast AI 2026).

## Approches voisines & alternatives

- [[Inference optimization]] — les leviers techniques qui font monter `v`.
- [[Plafond de débit d'un GPU (roofline)]] — d'où vient `v` à un utilisateur.
- [[Dimensionner la mémoire d'un serveur LLM]] — la mémoire borne le lot, donc `v`.
- [[prompt-caching]] — le tarif d'entrée « cache touché ».
- [[Quantization]] — moins d'octets lus, plus de tokens par seconde.
- [[Routing and cascading]] — réduire le coût d'une tâche en choisissant le modèle, plutôt que le coût d'un token.
- [[LiteLLM]] et [[OpenRouter]] — appeler des modèles hébergés par d'autres ; la formule dit ce que ces fournisseurs peuvent tenir comme prix.
- [[llmfit]] — savoir quel modèle tient sur sa propre machine avant de compter son coût.

## Pour aller plus loin

- Banc public [InferenceX](https://inferencex.semianalysis.com/) (SemiAnalysis, partie prenante) : une ligne par exécution consultable.
- Documentation tarifaire de l'API de DeepSeek — [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing).
- Cours de floSa : *L'économie de l'inférence IA* (Nerdy Kings, 2026-10-02, [youtube.com/watch?v=YtvYpgG8pg8](https://www.youtube.com/watch?v=YtvYpgG8pg8) ; la vidéo pose le mécanisme, les chiffres viennent de la recherche écrite du cours) ; formule et tableau refaits et recoupés.
