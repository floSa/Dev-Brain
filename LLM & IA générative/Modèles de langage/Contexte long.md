---
role: notion
nom: Contexte long
alias: [fenêtre de contexte, longueur de contexte, long context, context window, contexte étendu, lost in the middle, needle in a haystack, NIAH, RULER, longueur effective, context rot, extension de contexte, RoPE scaling, YaRN, interpolation de positions]
categorie: llm/modele
domaines: [ai-eng, ml-eng]
tags: [llm, context-engineering, attention, inference-optimization, positional-encoding]
---

# Contexte long

## Aperçu

- La **fenêtre de contexte** est le nombre de jetons qu'un modèle lit en une fois : consigne, historique, documents, résultats d'outils, et sa propre sortie. Les modèles actuels annoncent de 128 000 à plus d'un million de jetons.
- Trois questions distinctes : ce que la longueur **coûte** (calcul, mémoire), comment un modèle est **rendu capable** de la lire (extension de positions, attention allégée), et ce qu'il **en fait réellement** (la longueur annoncée n'est pas la longueur utile).
- Réponse courte aux trois : le coût du cache est prévisible et se calcule ; l'extension est un savoir-faire maîtrisé ; la qualité réelle se mesure sur sa propre tâche, car les benchmarks divergent.

## Concepts clés

### Ce que la longueur coûte

- **Calcul.** L'attention compare chaque jeton à tous les autres : le préremplissage (*prefill*) coûte $O(n^2)$ en longueur. Au décodage, chaque nouveau jeton relit tout le cache : $O(n)$ par jeton. Voir [[Flash Attention and efficient attention]] pour la version économe en mémoire.
- **Mémoire : le cache KV.** Il croît **linéairement** avec la longueur, par séquence, et s'ajoute aux poids. Dans un serveur, c'est souvent lui, et non les poids, qui plafonne la concurrence ([[Inference optimization]]).
- **Exemples calculés** à partir des `config.json` publiés sur Hugging Face, lus le 2026-10-02 (FP16, par séquence, hors poids). Les nombres de couches et de têtes viennent des configs ; les produits sont calculés ici.

  | Modèle (config lue) | Octets par jeton | 128 k | 256 k |
  |---|---|---|---|
  | Mistral Medium 3.5 128B — 88 couches, attention pleine, 8 têtes KV, dimension 128 | 352 Kio | 44 Gio | 88 Gio |
  | Qwen3-32B — 64 couches, 8 têtes KV, dimension 128 | 256 Kio | 32 Gio | 64 Gio |
  | Qwen3.8-2.4T-A95B — 23 couches d'attention pleine sur 92, 4 têtes KV, dimension 256 | 92 Kio | 11,5 Gio | 23 Gio |
  | gpt-oss-120b — 18 couches pleines et 18 à fenêtre de 128, 8 têtes KV, dimension 64 | 36 Kio (couches pleines) | 4,5 Gio | non supporté (131 072 maximum) |

  - Le FP8 divise ces nombres par deux ; à 1 M de jetons, Mistral Medium 3.5 demanderait 352 Gio en FP16, mais 1 M dépasse sa longueur native (262 144) : valeur d'illustration.
  - Pour Qwen3.8, les 69 couches d'attention linéaire gardent un **état de taille constante** non compté ici. L'hybridation y divise le cache par quatre par rapport à un modèle à 92 couches pleines.
  - Qwen3-32B annonce 32 768 jetons en natif (`max_position_embeddings` à 40 960 dans la config) et 131 072 avec YaRN : sa ligne à 256 k dépasse ce qui est annoncé.
- **Réduire le cache** : moins de têtes KV (le partage en groupes, GQA : Mistral Medium 3.5 a 96 têtes de requête pour 8 têtes KV, soit 12 fois moins) ; fenêtre glissante sur une partie des couches ; couches d'attention linéaire ([[Attention linéaire]], [[Architectures hybrides LLM]]) ; compression latente ([[Multi-head Latent Attention]]) ; quantification du cache ([[Quantification des LLM - GGUF, AWQ, GPTQ]]).

### Rendre un modèle capable de lire plus long

- **Le problème.** Les positions sont encodées par rotation (RoPE, voir [[Positional encoding]]). Au-delà de la longueur vue à l'entraînement, les angles sortent de la plage connue et la qualité s'effondre.
- **Interpolation de positions** (Chen, Wong, Chen, Tian, 2023, arXiv 2306.15595) : au lieu d'extrapoler, comprimer linéairement les indices pour rester dans la plage d'origine, avec un ajustement fin court (au plus mille pas). Testée sur LLaMA 7B à 65B, étendus à 8 000, 16 000 et 32 000 jetons.
- **NTK-aware et « par morceaux »** : changer la base de la rotation pour moins comprimer les hautes fréquences et plus les basses. L'origine est un billet de la communauté (bloc97, juin 2023, non ouvert : Reddit était bloqué) ; la méthode est décrite par YaRN.
- **YaRN** (Peng, Quesnelle, Fan, Shippole, 2023, ICLR 2024) : interpolation par morceaux plus un facteur de température sur l'attention, sans surcoût à l'inférence. Annonce : extension à 128 k avec moins de 0,1 % des données de pré-entraînement, 10 fois moins de jetons et 2,5 fois moins de pas que les méthodes précédentes. Les papiers notent que la perplexité seule ne dit pas la longueur effective. YaRN est devenu le mécanisme courant : les configs lues utilisent `rope_type: yarn` (Mistral Medium 3.5, facteur 64 depuis 4 096 ; gpt-oss-120b, facteur 32 depuis 4 096). La carte de Qwen3-32B avertit que le YaRN **statique** des frameworks peut dégrader les textes courts.
- **LongRoPE** (Ding et al., Microsoft, 2024) : facteurs d'interpolation non uniformes trouvés par recherche évolutionnaire ; annonce 2 048 k jetons, avec un ajustement fin à 256 k de moins de mille pas.
- **Attention locale ou parcimonieuse.**
  - *Longformer* (Beltagy et al., 2020) : fenêtre locale plus quelques jetons globaux.
  - *StreamingLLM* (Xiao et al., ICLR 2024) : garder les jetons de tête (*attention sinks*) et une fenêtre récente ; flux stable jusqu'à 4 millions de jetons. Limite écrite par les auteurs : cela **n'étend pas** la fenêtre, donc ne convient ni aux questions sur de longs documents ni au résumé.
  - *DeepSeek Sparse Attention* (DeepSeek-V3.2, 2025) : un indexeur choisit 2 048 paires clé-valeur par jeton ; le cœur de l'attention passe de $O(L^2)$ à $O(Lk)$.
  - *Ring Attention* (Liu, Zaharia, Abbeel, 2023) : répartir la séquence sur plusieurs appareils, sans approximation ; plus d'un million de jetons sur 32 A100 selon l'article. Règle la mémoire, pas la qualité d'usage.
- **Couches locales et globales mélangées.** Gemma 3 alterne 5 couches locales (fenêtre de 1 024) pour 1 globale ; le rapport Gemma 4 garde 5 pour 1 ; la config du 31B lue ici compte 50 couches à fenêtre et 10 globales. gpt-oss alterne couches pleines et fenêtre de 128. Qwen3.8 : 69 couches linéaires pour 23 pleines (une pleine sur quatre). Kimi Linear annonce jusqu'à 75 % de cache en moins et 6 fois plus de débit au décodage à 1 M de jetons (chiffres du constructeur).

### Longueur annoncée contre longueur utile

- **Lost in the middle** (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang, TACL 2024, arXiv 2307.03172). Deux protocoles : questions multi-documents (10, 20 ou 30 documents dont un seul utile) et récupération de paires clé-valeur synthétiques. Résultat : une **courbe en U** — la performance est meilleure quand l'information est au début ou à la fin, et chute au milieu. GPT-3.5-Turbo perd plus de 20 % et, dans le pire cas, tombe sous son score sans aucun document (56,1 %). Les modèles à contexte étendu ne font pas mieux quand l'entrée tient dans les deux fenêtres. Placer la requête avant **et** après le contexte rend la tâche clé-valeur quasi parfaite. Tous les modèles testés datent de 2023 : aucune réfutation directe sur des modèles de 2026 n'a été trouvée, et la forme du U n'est pas à supposer pour les modèles actuels sans mesure.
- **Needle in a haystack** (Greg Kamradt, novembre 2023, billet et dépôt GitHub — pas un papier) : une phrase insérée à diverses profondeurs dans des essais de Paul Graham, sur une grille longueur × profondeur. Limites : le résultat dépend du prompt — Anthropic rapporte que Claude 2.1 ne réussissait que 27 % d'un test de ce type sur 200 000 jetons, et 98 % après ajout d'une seule phrase en début de réponse (billet du 6 décembre 2023) ; RULER, NoLiMa et HELMET lui reprochent d'être trop facile ou de ne pas prédire les tâches réelles.
- **RULER** (Hsieh et al., NVIDIA, COLM 2024, arXiv 2404.06654) : 13 tâches en quatre catégories (récupération enrichie, traçage multi-sauts, agrégation, questions-réponses avec distracteurs), de 4 k à 128 k, 17 modèles. La **longueur effective** est la plus grande longueur où le score reste au-dessus de celui de Llama 2 7B à 4 k (85,6 %). Constat : tous les modèles annoncent 32 k ou plus, mais seule la moitié tient 32 k ; GPT-4 annoncé à 128 k est effectif à 64 k. Modes d'échec relevés sur Yi-34B-200K : non-robustesse au type d'aiguille, distracteurs (jusqu'à 40 points perdus à 256 k), information incomplète, recopie du contexte.
- **NoLiMa** (Modarressi et al., Adobe, ICML 2025, arXiv 2502.05167) : aiguilles **sans recouvrement lexical** avec la question, donc une inférence est nécessaire. Seuil : 85 % du score de base de chaque modèle. GPT-4o passe de 99,3 % à 69,7 % à 32 k (longueur effective 8 k) ; Llama 3.3 70B annoncé à 128 k est effectif à 2 k ; Claude 3.5 Sonnet annoncé à 200 k, à 4 k. Les modèles de l'article datent de 2025.
- **HELMET** (Yen et al., Princeton, ICLR 2025, arXiv 2410.02694) : sept catégories orientées applications (RAG, re-classement, citations, résumé…), 59 modèles. Trois constats : les tâches synthétiques comme NIAH ne prédisent pas la performance aval ; les catégories corrèlent peu entre elles ; les modèles ouverts restent derrière les fermés dès qu'il faut raisonner sur tout le contexte. Les auteurs recommandent les tâches RAG pour le développement rapide.
- **Context rot** (Chroma, juillet 2025 — rapport technique non relu par des pairs) : 18 modèles, dégradation avec la longueur ; un seul distracteur suffit à baisser l'exactitude ; une botte de foin **mélangée** donne de meilleurs résultats qu'une botte cohérente, résultat que le rapport n'explique pas. La documentation d'Anthropic reprend le terme : la précision et le rappel se dégradent quand le nombre de jetons croît, d'où la nécessité de trier ce qui entre dans le contexte.
- **La longueur seule dégrade** (Du et al., EMNLP 2025, arXiv 2510.05381) : même quand le modèle récupère toute l'évidence par récitation exacte, l'exactitude baisse de 13,9 % à 85 % avec la longueur ; l'effet persiste quand les jetons inutiles sont remplacés par des espaces. Atténuation : faire réciter l'évidence avant de répondre (jusqu'à +4 % pour GPT-4o sur RULER).
- **Une cause d'entraînement** (An et al., 2024, STRING) : les grandes distances relatives sont sous-représentées à l'entraînement, d'où une longueur effective souvent inférieure à la moitié de la longueur d'entraînement ; réutiliser à l'inférence des positions bien entraînées donne plus de 10 points sur RULER et InfiniteBench pour Llama 3.1 70B et Qwen2 72B.
- **Désaccords** entre explications : positions lointaines sous-entraînées (An), attention plus difficile sans correspondance littérale (NoLiMa), longueur seule (Du), distracteurs et structure (Chroma). Elles ne s'excluent pas, mais aucune source ne les départage. Les seuils de « longueur effective » de RULER (absolu) et NoLiMa (relatif) ne sont pas comparables entre eux.

### Contexte long contre RAG

- **Xu et al. (NVIDIA, ICLR 2024)** : un modèle à 4 k de contexte avec récupération égale un modèle à 16 k étendu par interpolation, pour bien moins de calcul (GPT-43B : 29,32 contre 29,45 ; Llama 2 70B : 36,02 contre 36,78), et la récupération améliore aussi les modèles à 16 k et 32 k.
- **Li et al. (Google DeepMind, EMNLP 2024 industrie)** concluent l'inverse sur des modèles plus récents : à ressources suffisantes, le contexte long bat le RAG en moyenne (Gemini-1.5-Pro 49,70 contre 37,33 ; GPT-4O 48,67 contre 32,60), mais le RAG coûte bien moins, et leurs prédictions sont identiques pour 63 % des requêtes. Leur méthode *Self-Route* tente le RAG d'abord et bascule en contexte long si le modèle déclare ne pas pouvoir répondre : 65 % de coût en moins pour Gemini-1.5-Pro et 39 % pour GPT-4O, pour un écart de performance de −0,2 % à −2,2 % avec le contexte long. Ils attribuent « possiblement » la divergence avec Xu à des modèles plus forts ; ce n'est pas testé.
- **Yu et al. (NVIDIA, 2024)** : en conservant l'ordre d'origine des fragments récupérés (OP-RAG), la qualité suit une courbe en U inversé du nombre de fragments, et un « point idéal » bat le contexte complet sur ∞Bench En.QA avec Llama 3.1 70B. Li et al. mesurent l'inverse avec un RAG qui n'a pas cet ordre.
- **2025-2026** : SagaScale (romans de plus de 250 000 jetons, décembre 2025) trouve que le contexte long l'emporte sur le RAG naïf quand le problème tient dans la fenêtre et que le RAG agentique bat le RAG naïf ; une étude de cas industrielle sur de petits modèles (Hamilton et al., juin 2026) donne 73,1 % contre 65,4 % pour le contexte long, à 26 fois le coût en jetons par requête. Les deux sont peu généralisables (jeux et modèles spécifiques).

### Longueurs annoncées (état lu le 2026-10-02)

- **Claude** : fenêtre de 1 M de jetons pour Fable 5.1, Opus 5.5, Sonnet 5.5 et d'autres modèles récents, 200 k pour Sonnet 4.5 (documentation Anthropic) ; 1 M par défaut, sans en-tête bêta, au tarif standard.
- **Poids ouverts** : Qwen3.8-2.4T-A95B, 262 144 en natif, extensible à environ 1 010 000 (carte du modèle) ; Mistral Medium 3.5 et Gemma 4 31B, 262 144 dans la config (256 k annoncés) ; gpt-oss-120b, 131 072. Voir [[Qwen]], [[Mistral]], [[Gemma]], [[gpt-oss]].
- Les cartes de modèles publient aussi des scores RULER ou MRCR : ce sont des chiffres de constructeur, jamais reproduits ici.

## Les maths, simplement

- **Taille du cache KV** par séquence : $\text{octets} = 2 \cdot L \cdot h_{kv} \cdot d \cdot n \cdot b$, avec $L$ le nombre de couches d'attention pleine, $h_{kv}$ le nombre de têtes KV, $d$ la dimension d'une tête, $n$ la longueur, $b$ les octets par élément (2 en FP16, 1 en FP8) ; le `2` compte clés et valeurs. Mistral Medium 3.5 : $2 \cdot 88 \cdot 8 \cdot 128 \cdot 2 = 360\,448$ octets par jeton, soit 44 Gio à 131 072 jetons.
- **Fenêtre glissante de largeur $w$** : une couche ne garde que $\min(n, w)$ positions ; une couche d'attention linéaire garde un état de taille fixe.
- **Interpolation de positions** : pour étendre de $L$ à $L' > L$, remplacer l'indice $m$ par $m \cdot L/L'$. Les angles restent dans la plage vue à l'entraînement ; le prix est une résolution de position plus grossière, d'où l'ajustement fin.
- **Longueur effective (RULER)** : plus grande $n$ telle que score$(n) \ge$ 85,6 %, le score de Llama 2 7B à 4 k ; **(NoLiMa)** : score$(n) \ge 0{,}85 \times$ score de base du modèle.

## En pratique

- **Calculer le cache avant de promettre une concurrence** : prendre `num_hidden_layers`, `num_key_value_heads` et `head_dim` dans le `config.json`, multiplier par la longueur visée et le nombre de requêtes simultanées, puis comparer à la VRAM restante après les poids. Les estimateurs qui ne tiennent pas compte du cache à long contexte sont trop optimistes (cf. [[llmfit]]).
- **Mesurer la longueur utile sur sa tâche** plutôt que de se fier à l'annonce ni à un score NIAH : un jeu de questions maison à la longueur réelle, avec des distracteurs réalistes ; RULER, NoLiMa ou HELMET donnent des protocoles.
- **Mettre l'information critique au début ou à la fin**, répéter la question après le contexte, et ne pas noyer un document utile sous des documents voisins : un seul distracteur suffit à dégrader.
- **Ne pas remplir la fenêtre par principe.** Trier et résumer coûte souvent moins que de payer le cache, et le rendement décroît ([[Context engineering]]).
- **Trancher contre le RAG sur trois critères** : le corpus tient-il dans la fenêtre, la requête a-t-elle besoin de tout le texte (agrégation, résumé) ou d'un fait, le coût par requête est-il acceptable. L'approche hybride *Self-Route* est un point de départ.
- **Extension YaRN statique** : l'activer seulement si les contextes dépassent la longueur native, car elle peut dégrader les textes courts.
- **Cache KV quantifié** : gain mémoire réel, mais à vérifier à la longueur cible (voir [[Quantification des LLM - GGUF, AWQ, GPTQ]]).

## Approches voisines & alternatives

- [[Positional encoding]] — RoPE et ses variantes, ce que l'interpolation modifie.
- [[Flash Attention and efficient attention]] — rend le calcul exact économe en mémoire ; l'attention parcimonieuse en change la nature.
- [[Inference optimization]] — le cache KV, PagedAttention et le batching, qui décident de la concurrence atteignable.
- [[Architectures hybrides LLM]], [[Attention linéaire]], [[State Space Models]] — attaquer le coût linéaire du cache par l'architecture.
- [[Multi-head Latent Attention]] — compresser le cache par projection latente.
- [[RAG]], [[Advanced RAG]] — ne mettre dans la fenêtre que ce qui est utile ; l'alternative de principe au contexte long.
- [[Context engineering]] — gérer le budget de jetons d'un agent ou d'une application.
- [[prompt-caching]] — réduire le coût d'un long préfixe répété, sans changer ce que le modèle lit.
- [[Scaling laws]] et [[LLM benchmarks]] — où se placent les évaluations de contexte long.
- [[Hallucinations des LLM]] — un contexte long mal exploité augmente les erreurs de fidélité.
- Briques : [[vLLM]], [[SGLang]], [[TensorRT-LLM]], [[llama.cpp]], [[Ollama]] — les moteurs où la longueur et le cache se règlent ; [[Qdrant]] — l'alternative RAG côté recherche.

## Pour aller plus loin

- Liu et al. (2023, TACL 2024) — *Lost in the Middle: How Language Models Use Long Contexts* ; arXiv 2307.03172.
- Chen, Wong, Chen, Tian (2023) — *Extending Context Window of Large Language Models via Positional Interpolation* ; arXiv 2306.15595.
- Peng, Quesnelle, Fan, Shippole (2023, ICLR 2024) — *YaRN* ; arXiv 2309.00071. Ding et al. (2024) — *LongRoPE* ; arXiv 2402.13753.
- Xiao et al. (2023, ICLR 2024) — *Efficient Streaming Language Models with Attention Sinks* ; arXiv 2309.17453.
- Hsieh et al. (2024, COLM) — *RULER* ; arXiv 2404.06654. Modarressi et al. (2025, ICML) — *NoLiMa* ; arXiv 2502.05167. Yen et al. (2024, ICLR 2025) — *HELMET* ; arXiv 2410.02694.
- Kamradt (2023) — *LLMTest_NeedleInAHaystack*, dépôt GitHub ; Anthropic (6 décembre 2023) — *Long context prompting for Claude 2.1*.
- Du et al. (2025) — *Context Length Alone Hurts LLM Performance Despite Perfect Retrieval* ; arXiv 2510.05381. An et al. (2024) — *Why Does the Effective Context Length of LLMs Fall Short?* ; arXiv 2410.18745.
- Xu et al. (2023, ICLR 2024) — *Retrieval meets Long Context Large Language Models* ; arXiv 2310.03025. Li et al. (2024) — *Retrieval Augmented Generation or Long-Context LLMs?* ; arXiv 2407.16833. Yu et al. (2024) — *In Defense of RAG in the Era of Long-Context Language Models* ; arXiv 2409.01666.
- Gemma Team (2025) — *Gemma 3 Technical Report* ; arXiv 2503.19786. Gemma Team (2026) — *Gemma 4 Technical Report* ; arXiv 2607.02770.
- Non ouverts ou lus au résumé : bloc97 (billet Reddit, juin 2023), Ring Attention (arXiv 2310.01889), Longformer (2004.05150), DeepSeek-V3.2 (2512.02556), Kimi Linear (2510.26692), SagaScale (2601.09723), Hamilton et al. (2606.20898), Chroma *Context Rot* (page web lue, rapport non évalué par des pairs).
