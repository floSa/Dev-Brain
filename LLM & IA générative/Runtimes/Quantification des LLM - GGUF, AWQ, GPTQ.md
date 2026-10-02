---
role: notion
nom: Quantification des LLM - GGUF, AWQ, GPTQ
alias: ["Quantification des LLM : GGUF, AWQ, GPTQ", quantification de modèles de langage, quantification pour le serving, Q4_K_M, imatrix, SmoothQuant, NF4, W4A16, W8A8, quantification du cache KV, LLM.int8, bitsandbytes]
categorie: llm/runtime
domaines: [ai-eng, mlops, ml-eng]
tags: [quantization, model-compression, inference-optimization, llm, gpu, local-llm]
---

# Quantification des LLM : GGUF, AWQ, GPTQ

## Aperçu

- Quantifier un LLM pour le **servir** : stocker les poids (et parfois les activations et le cache KV) sur moins de bits pour que le modèle tienne en mémoire et que le décodage aille plus vite. Les principes généraux (PTQ, QAT, granularité, formats FP4 à échelle par bloc) sont dans [[Quantization]] ; cette notion traite ce qui s'y décide quand on déploie : quoi quantifier, avec quelle méthode, dans quel format de fichier, sur quel moteur et matériel, et ce qui casse.
- Ordre de grandeur mesuré par le README de `llama-quantize` sur Llama 3.1 8B : 14,96 Gio en F16, 4,58 Gio en Q4_K_M. Le même README donne pour Q4_K_M : 70B de 280,9 Go (original) à 43,1 Go, 405B de 1 625,1 Go à 249,1 Go.
- Les gains de vitesse existent, mais sont **sous-linéaires** et dépendent du moteur, du matériel et de la taille de lot (voir *Les maths, simplement*).

## Concepts clés

### Ce qu'on quantifie : poids, activations, cache KV

- **Poids seuls (W4A16, W8A16).** Au décodage, la lecture des poids domine : l'article AWQ calcule, pour Llama-2-7B sur une RTX 4090, une intensité arithmétique d'environ 1 FLOP par octet en FP16, très sous le seuil du GPU (165 FLOP/octet), donc un décodage limité par la bande passante mémoire ; passer à 4 bits relève l'intensité de 4 fois. L'article note que les accès aux poids dépassent de plusieurs ordres de grandeur ceux aux activations, d'où l'intérêt du poids seul pour un usage local à lot 1.
- **Poids et activations (W8A8, FP8).** Les activations sont quantifiées aussi : le calcul se fait en entiers ou en FP8 sur les cœurs de calcul, ce qui aide le préremplissage (limité par le calcul) et les gros lots. Kurtić et al. (ACL 2025, plus de 500 000 évaluations sur Llama 3.1) recommandent W4A16 pour des usages synchrones sensibles à la latence et W8A8 pour du *continuous batching* asynchrone à fort débit.
- **Le gain du 4 bits diminue avec le lot.** MARLIN (Frantar et al., 2024), noyau W4A16 de vLLM, annonce près du maximum théorique (4 fois) pour des lots de 16 à 32, un gain moindre à 64–128, et jusqu'à 2,8 fois de bout en bout dans vLLM (résumé lu).
- **Cache KV.** Quantifier le cache réduit la mémoire par séquence, donc la concurrence atteignable ou la longueur de contexte (voir [[Contexte long]]). KIVI (Liu et al., ICML 2024) : clés quantifiées par canal, valeurs par jeton, 2 bits ; annonce 2,6 fois moins de mémoire de pic (poids compris) et un lot jusqu'à 4 fois plus grand. KVQuant (Hooper et al., NeurIPS 2024) : moins de 0,1 de dégradation de perplexité à 3 bits (résumés lus). Côté moteurs : vLLM propose un cache FP8 par tenseur ou par tête (la variante par tête exige un calibrage par llm-compressor ; sans calibrage toutes les échelles valent 1,0) ; Ollama expose `OLLAMA_KV_CACHE_TYPE` (`f16` par défaut ; `q8_0` environ la moitié de la mémoire, `q4_0` environ le quart, avec une perte plus visible à grand contexte ; exige Flash Attention) ; llama.cpp accepte `-ctk` et `-ctv`.

### Les méthodes

- **LLM.int8()** (Dettmers, Lewis, Belkada, Zettlemoyer, NeurIPS 2022) : quantification vectorielle en 8 bits plus décomposition en précision mixte : les quelques dimensions « aberrantes » (environ 0,1 %) restent en 16 bits. Les grandes amplitudes apparaissent à partir de 6,7 milliards de paramètres. Limite écrite : l'implémentation peut ralentir les modèles de moins de 6,7 milliards face au FP16 ; le gain principal est la mémoire.
- **GPTQ** (Frantar, Ashkboos, Hoefler, Alistarh, ICLR 2023) : quantification par couche avec information du second ordre, dérivée d'Optimal Brain Quantization ; calibration sur 128 segments de 2 048 jetons ; un modèle de 175 milliards de paramètres passe à 3-4 bits en environ quatre heures sur un GPU. L'article annonce des accélérations de 3,25 fois (A100) et 4,5 fois (A6000) : la mesure de la table compare à un FP16 réparti sur **5 GPU** pour l'A100, soit un gain de noyau mêlé à la suppression de la communication entre GPU.
- **AWQ** (Lin et al., MLSys 2024, prix du meilleur article) : 1 % environ des canaux de poids sont « saillants », repérés par l'amplitude des **activations** et non des poids ; les mettre à l'échelle avant la quantification réduit leur erreur, sans rétropropagation. Le système TinyChat annonce plus de 3 fois la vitesse de l'implémentation FP16 de Hugging Face sur GPU de bureau et mobile. Les auteurs signalent que GPTQ peut sur-ajuster son jeu de calibration.
- **SmoothQuant** (Xiao, Lin, Seznec, Wu, Demouth, Han, ICML 2023) : les activations ont des valeurs aberrantes environ 100 fois plus grandes que la plupart ; une division par canal côté activations, reportée sur les poids (équivalence mathématique, paramètre α de force de migration), rend W8A8 praticable. Annonce jusqu'à 1,56 fois de vitesse et 2 fois moins de mémoire.
- **QLoRA et NF4** (Dettmers, Pagnoni, Holtzman, Zettlemoyer, 2023) : format NF4 conçu pour des poids gaussiens, double quantification (environ 0,37 bit par paramètre économisé) ; sert d'abord au **fine-tuning** d'un modèle gelé (voir [[LoRA et QLoRA]]).
- **FP8** (Micikevicius et al., 2022) : formats E4M3 et E5M2. Dans vLLM, le calcul FP8 exige une capacité de calcul ≥ 8.9 (Ada, Hopper, Blackwell) ; Turing et Ampere exécutent un modèle FP8 en poids seuls (W8A16) via Marlin ; la doc annonce 2 fois moins de mémoire et jusqu'à 1,6 fois de débit.
- **2 à 4 bits récents.** Quantification vectorielle ou à treillis (QuIP#, AQLM, QTIP), sans calibration (HQQ, billet Mobius Labs), rotations contre les aberrations (QuaRot, SpinQuant, qui visent W4A4 et cache en 4 bits) ; BitNet b1.58 est **entraîné** en ternaire, pas converti. Dans les moteurs, la doc de vLLM annonce, via llm-compressor, des transformations de type QuIP et SpinQuant ; le support de QuIP#, AQLM, QTIP et HQQ n'a pas été retrouvé dans les docs de moteurs lues : à ne pas déduire.

### GGUF

- **Un conteneur, pas une méthode.** GGUF est le format de fichier de GGML et de llama.cpp : un fichier unique, extensible, compatible avec le chargement par `mmap`, qui porte métadonnées, tokenizer et tenseurs, chacun avec son type. Le nom suit une convention qui se termine par l'encodage (`…-Q4_K_M.gguf`). Spécification : `docs/gguf.md` du dépôt ggml.
- **Types de quantification.** Ancien : `Q4_0`, `Q5_0`, `Q8_0`. **K-quants** (Kawrakow, PR n° 1684) : super-blocs de 256 poids avec échelles elles-mêmes quantifiées, et mélange de types selon les tenseurs (`--pure` désactive ce mélange). **IQ-quants** (`IQ1_S` à `IQ4_XS`) : plus agressifs, qui demandent une imatrice. Suffixes `S`, `M`, `L` : variantes petite, moyenne, grande, qui échangent compression et précision (définition donnée par Kurt, 2026).
- **Valeurs mesurées** (README de `llama-quantize`, Llama 3.1 8B ; la machine des débits n'est pas précisée dans le README) :

  | Type | bits par poids | Taille (Gio) | Génération (tok/s) |
  |---|---|---|---|
  | F16 | 16,00 | 14,96 | 29,17 |
  | Q8_0 | 8,50 | 7,95 | 50,93 |
  | Q6_K | 6,56 | 6,14 | 58,67 |
  | Q5_K_M | 5,70 | 5,33 | 67,23 |
  | Q4_K_M | 4,89 | 4,58 | 71,93 |
  | Q3_K_M | 4,00 | 3,74 | 71,68 |
  | Q2_K | 3,16 | 2,95 | 79,85 |

- **Matrice d'importance (imatrix)** (Kawrakow, PR n° 4861, janvier 2024) : un passage sur un texte de calibration (environ 50 000 jetons pour un 7B d'après la PR) mesure les activations ; l'erreur de quantification est pondérée par la moyenne des carrés des activations de chaque dimension. L'imatrice se calcule avec `llama-imatrix` puis se passe à `llama-quantize --imatrix` ; le README déconseille de l'appliquer à `output.weight` (désactivé par défaut).
- **Perte mesurée** (README perplexité de llama.cpp, Llama 3 8B de base, Wikitext-2, une RTX 4090). Δ perplexité et divergence KL face au FP16, sans imatrice :

  | Type | ΔPPL | KLD |
  |---|---|---|
  | q8_0 | 0,003 | 0,0014 |
  | q6_K | 0,022 | 0,0055 |
  | q5_K_M | 0,057 | 0,0108 |
  | q4_K_M | 0,175 | 0,0313 |
  | q3_K_S | 1,632 | 0,2282 |
  | q2_K (imatrice 10 M jetons) | 2,416 | 0,3322 |

  Avec une imatrice de 10 M jetons : q4_K_M passe à 0,151 de ΔPPL (KLD 0,0282), q3_K_S à 1,371 (KLD 0,1998). Le README avertit que la perplexité n'est comparable ni entre modèles ni entre projets.
- **Ne pas re-quantifier.** `--allow-requantize` existe mais le README avertit d'une dégradation possible forte. Partir d'un GGUF F16 ou BF16.
- **Autour de GGUF.** Ollama ne quantifie pas un GGUF à l'import : il faut le préparer avec `llama-quantize` ; son paramètre `quantize` d'API concerne des poids safetensors pour MLX (`nvfp4`, `mxfp8`, `int4`, `int8`). Dans vLLM, GGUF est « très expérimental et sous-optimisé », et son support est passé dans un plugin hors arbre (`vllm-gguf-plugin`). Unsloth publie des GGUF « Dynamic » dont il annonce plus de 10 % de précision top-1 à taille égale : revendication du fournisseur, sans vérification indépendante trouvée.

### Moteurs et matériel (docs lues le 2026-10-02)

- **vLLM** (branche `main`) : AWQ (l'ancien AutoAWQ est déprécié et repris dans llm-compressor), GPTQ, Marlin, llm-compressor (FP8 W8A8, INT4 W4A16, INT8 W4A8 et W8A8), NVFP4 via ModelOpt, bitsandbytes (plugin hors arbre), GGUF (plugin hors arbre), TorchAO. Dans le tableau de compatibilité : AWQ n'est pas pris en charge sur Volta, GPTQ l'est de Volta à Hopper, Marlin de Turing (avec réserve) à Hopper, FP8 W8A8 d'Ada à Hopper et sur GPU AMD. **Le tableau n'a pas de colonne Blackwell**, alors que la page FP8 de la même doc cite Blackwell : écart interne à la doc.
- **TensorRT-LLM** (doc mise à jour le 26 septembre 2026) : recettes FP8 (par tenseur, par blocs, par lignes), NVFP4, cache FP8 et NVFP4, W4A8 et W4A16 en AWQ et GPTQ. Matrice : Hopper n'a pas de FP4 ; NVFP4 et MXFP4 apparaissent sur Blackwell ; Ampere ne garde que le cache FP8 et W4A16 (AWQ, GPTQ), sans calcul FP8. SmoothQuant n'est plus dans la page actuelle alors qu'une version de septembre 2025 de la doc le citait.
- **llama.cpp** : quantifications de 1,5 à 8 bits ; CPU (NEON, AVX), CUDA, HIP, Metal, Vulkan, SYCL. Le support NVFP4 natif sur Blackwell est annoncé dans la version b8967 du 29 avril 2026. Le README ne cite ni GPTQ ni AWQ comme formats de chargement natifs (absence non vérifiée en profondeur).
- **SGLang** : AWQ, GPTQ, compressed-tensors, FP8, ModelOpt (FP4 et FP8), GGUF, auto-round ; recommande la quantification **hors ligne** à la quantification en ligne ; exige de valider les modèles quantifiés par des benchmarks.
- **Quantification native.** gpt-oss est post-entraîné avec les poids MoE en MXFP4 (le 120B tient sur un GPU de 80 Go, le 20B dans 16 Go ; carte du modèle). Gemma 3 a des variantes **QAT** officielles (environ 5 000 pas, int4 : 27B de 54 Go à 14,1 Go de VRAM ; annonce de Google).

### Compromis, pièges

- **La perte n'est pas uniforme.** Kurtić et al. : FP8 W8A8 « effectivement sans perte », INT8 avec 1 à 3 % de dégradation, W4A16 plus compétitif que prévu (page arXiv). Liu et al. (COLM 2025, modèles de raisonnement 1,5 à 70 B) : sans perte avec W8A8 ou W4A16, risque réel en dessous ; la taille, l'origine du modèle et la difficulté de la tâche pèsent.
- **Contexte long.** Mekala et al. (EMNLP 2025, cinq modèles, entrées de plus de 64 k jetons) : le 8 bits perd en moyenne environ 0,8 %, le 4 bits jusqu'à 59 % ; Qwen2.5 72B reste robuste sous bitsandbytes NF4 pendant que Llama 3.1 70B perd 32 % sur la même tâche : l'effet dépend de la méthode, du modèle et de la tâche.
- **Langues.** Marchisio et al. (EMNLP 2024) : une baisse moyenne de 1,7 % mesurée automatiquement en japonais correspond à 16,0 % pour des évaluateurs humains ; les langues à écriture non latine et les tâches complexes souffrent davantage.
- **Agents.** Jang et al. (juillet 2026) : le score moyen reste plat, mais la quantification amplifie jusqu'à 2,5 fois les échecs déjà présents en pleine précision, avec +17,6 points d'hallucination de noms d'outils sur un domaine (résumé lu).
- **La perplexité ne prédit pas la tâche.** Jaiswal et al. (ICLR 2024) montrent qu'une perplexité quasi inchangée à 3-4 bits n'assure pas la qualité aval. Kurt (2026, Llama 3.1 8B Instruct, 13 types GGUF, CPU) : à 5 bits les perplexités sont voisines (7,43 pour Q5_0 contre 7,32 en F16) mais GSM8K varie le plus, et Q3_K_S perd 4 points de moyenne (65,49 contre 69,47).
- **Le noyau compte autant que le format.** Un billet de l'équipe vLLM (avril 2026, lu en résumé) rapporte qu'un cache FP8 faisait passer un test d'aiguille à 128 k de 91 % à 13 % sur Hopper, à cause de l'accumulation en FP32 dans les cœurs de calcul, corrigée par une accumulation à deux niveaux (89 %).
- **Désaccords laissés tels quels.**
  - Kurt classe Q5_0 en tête (69,92 de moyenne contre 69,47 pour le F16, écart qu'il attribue possiblement au bruit), alors que la divergence KL de llama.cpp place q5_K_M (0,0108) devant q5_0 (0,0222). Modèles (Instruct contre base), jeux et métriques diffèrent.
  - Kurtić et al. jugent le W4A16 comparable au W8A8 en moyenne ; Mekala et al. trouvent un 4 bits sévère en contexte long. Protocoles et modèles diffèrent.
  - Les papiers GPTQ et AWQ plaident chacun pour leur méthode ; aucune comparaison commune n'a été lue.
  - Egiazarian et al. (ICLR 2026) et Chen et al. (octobre 2025) concluent que le FP4 n'est pas supérieur à l'INT4 en général, alors que le matériel récent (NVFP4 sur Blackwell, MXFP4 dans gpt-oss) va vers le FP (résumés lus).
- **Traçabilité.** Aucune source lue n'établit l'outil, la version ni le jeu de calibration d'un checkpoint communautaire : le noter soi-même quand on quantifie.

## Les maths, simplement

- **Taille d'un modèle** : $\text{octets} \approx N \cdot \text{bpw} / 8$, avec $N$ le nombre de paramètres et bpw les bits effectifs par poids (métadonnées d'échelle comprises). Llama 3.1 8B : environ $8{,}03 \times 10^9 \times 4{,}8944 / 8 \approx 4{,}9 \times 10^9$ octets, soit les 4,58 Gio du README pour Q4_K_M.
- **Décodage limité par la mémoire** : à lot 1, le débit est borné par $\text{bande passante} / \text{octets lus par jeton}$, soit à peu près la taille des poids. Calcul à partir du tableau GGUF ci-dessus : F16 vers Q4_K_M divise la taille par 3,3 mais ne multiplie la vitesse que par 2,5 (29,17 puis 71,93 jetons/s) ; le décodage ne lit pas que des poids (cache, activations, surcoût de déquantification), et la machine n'est pas précisée. Ce raisonnement est un calcul de cette page, pas une mesure de la source.
- **Intensité arithmétique** : FLOP par octet lu. Le décodage FP16 vaut environ 1 ; un GPU à 165 TFLOP/s et 1 To/s bascule vers le calcul à 165 FLOP/octet. Un lot plus grand ou des poids plus petits la relèvent ; c'est pourquoi le gain du poids seul s'érode quand le lot grandit.
- **Pondération par imatrice** : minimiser $\sum_i \langle a_i^2 \rangle (w_i - \hat w_i)^2$ au lieu de $\sum_i (w_i - \hat w_i)^2$ : une erreur sur un poids multipliant des activations fortes coûte davantage.

## En pratique

- **Raisonnement de choix** (à partir des sources ci-dessus, pas une règle publiée) : GPU Ada, Hopper ou Blackwell avec fort débit → FP8 ou W8A8 ; GPU Ampere ou latence à lot faible → W4A16 (AWQ ou GPTQ, noyau Marlin) ; CPU, Mac ou GPU grand public → GGUF, par défaut Q4_K_M ou Q5_K_M ; en dessous de Q4, utiliser une imatrice et vérifier.
- **Évaluer sur sa tâche, sa langue et sa longueur de contexte** avant de choisir : le score moyen d'un benchmark masque les pertes localisées (raisonnement, contexte long, langues non latines, appels d'outils).
- **Partir d'une source BF16 ou F16** et conserver outil, version et jeu de calibration. Préférer un checkpoint officiel (QAT, MXFP4 natif) quand il existe.
- **Quantifier le cache KV à part** et le valider à la longueur visée, avec le noyau d'attention utilisé en production.
- **Vérifier le matériel d'abord** : la capacité de calcul (FP8 à partir de 8.9), le support du format par le moteur, et la version du moteur — les docs de moteurs évoluent vite (plugins GGUF et bitsandbytes dans vLLM, SmoothQuant dans TensorRT-LLM).
- **Compter la mémoire complète** : poids quantifiés, cache KV de la concurrence visée (voir [[Contexte long]]), et marge du moteur (vLLM préalloue le cache selon `gpu_memory_utilization`).

## Approches voisines & alternatives

- [[Quantization]] — la notion générique : PTQ, QAT, granularité, microscaling, NVFP4 et MXFP4.
- [[LoRA et QLoRA]] — NF4 comme moyen de fine-tuner un modèle gelé sur un seul GPU.
- [[PEFT]] — le parapluie du fine-tuning léger que le 4 bits rend plus accessible.
- [[Inference optimization]] — la quantification s'ajoute à PagedAttention, au batching continu et au décodage spéculatif.
- [[Distillation]] et [[Pruning]] — réduire la taille ou les poids plutôt que la précision ; cumulables.
- [[Small Language Models]] — l'autre voie : un modèle plus petit plutôt qu'un gros modèle quantifié.
- [[Mixed precision]] — le prolongement côté entraînement.
- [[Contexte long]] — le cache KV et sa quantification, et la sensibilité du 4 bits aux longs contextes.
- [[Mixture of Experts]] — un MoE économise du calcul, pas de la mémoire ; la quantification attaque le poste restant.
- [[Licences de modèles open weights]] — une version quantifiée d'un modèle reste soumise à sa licence.
- Briques : [[llama.cpp]] (GGUF, K-quants, imatrice), [[vLLM]] (AWQ, GPTQ, FP8, Marlin), [[TensorRT-LLM]] (FP8, NVFP4, AWQ, GPTQ), [[SGLang]], [[Ollama]] (sert du GGUF), [[Unsloth]] (GGUF « Dynamic » et fine-tuning 4 bits), [[LM Studio]], [[llmfit]] (estime ce qui tient sur une machine).
- Modèles : [[gpt-oss]] (MXFP4 en post-entraînement), [[Gemma]] (variantes QAT), [[Qwen]], [[Mistral]].

## Pour aller plus loin

- Frantar, Ashkboos, Hoefler, Alistarh (2022, ICLR 2023) — *GPTQ* ; arXiv 2210.17323.
- Lin et al. (2023, MLSys 2024) — *AWQ* ; arXiv 2306.00978.
- Xiao et al. (2022, ICML 2023) — *SmoothQuant* ; arXiv 2211.10438.
- Dettmers et al. (2022, NeurIPS) — *LLM.int8()* ; arXiv 2208.07339. Dettmers et al. (2023) — *QLoRA* ; arXiv 2305.14314.
- Micikevicius et al. (2022) — *FP8 Formats for Deep Learning* ; arXiv 2209.05433.
- Kurtić, Marques, Pandit, Kurtz, Alistarh (2024, ACL 2025) — *« Give Me BF16 or Give Me Death »? Accuracy-Performance Trade-Offs in LLM Quantization* ; arXiv 2411.02355.
- Liu et al. (2025, COLM) — *Quantization Hurts Reasoning?* ; arXiv 2504.04823. Mekala et al. (2025, EMNLP) — *Does quantization affect models' performance on long-context tasks?* ; arXiv 2505.20276. Marchisio et al. (2024, EMNLP) — *How Does Quantization Affect Multilingual LLMs?* ; arXiv 2407.03211.
- Kurt (2026) — *Which Quantization Should I Use? A Unified Evaluation of llama.cpp Quantization on Llama-3.1-8B-Instruct* ; arXiv 2601.14277. Jaiswal et al. (2023, ICLR 2024) — *Compressing LLMs: The Truth is Rarely Pure and Never Simple* ; arXiv 2310.01382.
- Egiazarian et al. (2025, ICLR 2026) — *Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization* ; arXiv 2509.23202. Chen et al. (2025) — *INT v.s. FP* ; arXiv 2510.25602.
- Hooper et al. (2024) — *KVQuant* ; arXiv 2401.18079. Liu et al. (2024) — *KIVI* ; arXiv 2402.02750. Frantar et al. (2024) — *MARLIN* ; arXiv 2408.11743.
- Documentation : `tools/quantize/README.md`, `tools/perplexity/README.md` et `tools/imatrix/README.md` de llama.cpp ; `docs/gguf.md` de ggml ; pages « Quantization » de vLLM, TensorRT-LLM et SGLang ; PR llama.cpp n° 1684 (k-quants) et n° 4861 (imatrice). Toutes lues le 2026-10-02.
- Lus au niveau du résumé seulement : KIVI, KVQuant, MARLIN, QuIP# (2402.04396), AQLM (2401.06118), QTIP (2406.11235), QuaRot (2404.00456), SpinQuant (2405.16406), Marchisio, Jaiswal, Jang et al. (arXiv 2607.27275), Egiazarian, Chen, billet vLLM sur le cache FP8, billet HQQ de Mobius Labs, annonce Gemma 3 QAT et page Unsloth Dynamic.
