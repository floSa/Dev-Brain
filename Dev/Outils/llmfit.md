---
galaxie: dev
type: outil
nom: llmfit
alias: [llm-fit, alexsjones/llmfit]
pitch: "CLI Rust (MIT) qui détecte le matériel — RAM, CPU, GPU, VRAM, backend d'accélération — puis classe des centaines de modèles locaux sur quatre axes : tenue en mémoire, vitesse estimée, qualité et contexte ; TUI interactive, mode script et benchmarks communautaires."
categorie: llm/outillage
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Rust
status: actif
alternatives: []
tags: [local-llm, hardware-sizing, quantization, benchmark, terminal-ui]
url_docs: https://github.com/AlexsJones/llmfit
url_repo: https://github.com/AlexsJones/llmfit
---

# llmfit

## Pourquoi

Répond à une question précédant tout déploiement local : **quel modèle cette machine peut-elle réellement faire tourner**. L'outil inspecte le matériel — cœurs CPU, RAM, GPU dédié ou intégré, VRAM, architecture d'accélération (CUDA, Apple Silicon, ROCm, OneAPI) — puis confronte ce profil à un catalogue de plusieurs centaines de modèles.

Le résultat n'est pas un oui/non mais un classement sur **quatre axes** : tenue en mémoire, vitesse estimée, qualité, longueur de contexte soutenable. Un modèle peut tenir en mémoire et rester inutilisable en vitesse ; les quatre axes séparés rendent ce compromis lisible au lieu de le masquer derrière un score unique.

`tooling/llm` est ici la bonne famille, et non `llm/local` : llmfit **outille la décision**, il ne sert aucun modèle. Les runtimes qui exécutent l'inférence — [[Dev/Services/Ollama|Ollama]], [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/LM Studio|LM Studio]], MLX, Docker Model Runner — sont détectés comme environnements cibles, pas remplacés.

Il gère les configurations **multi-GPU**, les architectures **Mixture-of-Experts** (dont les paramètres actifs ne correspondent pas à l'empreinte totale), le choix du format de quantization (GGUF, AWQ, GPTQ, EXL2), et une surcharge manuelle de la mémoire prise en compte pour simuler une autre machine. Une commande `llmfit bench --share` alimente un jeu de mesures communautaires. Licence **MIT**.

## Quand l'utiliser

- Dimensionner un poste ou un serveur avant d'acheter du matériel ou de choisir un modèle.
- Arbitrer entre plusieurs quantizations d'un même modèle sur une machine donnée.
- Simuler une cible différente de la machine courante via la surcharge de mémoire.
- Confronter une intuition de faisabilité à des mesures réelles remontées par d'autres.

## Quand NE PAS l'utiliser

- Servir le modèle : c'est le rôle des runtimes → [[Dev/Services/Ollama|Ollama]], [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/vLLM|vLLM]] (cf. [[Comparatif - Exécution & serving LLM]]).
- Mesurer la **qualité** d'un modèle sur une tâche métier : l'axe qualité est une note de catalogue, pas une évaluation → [[Comparatif - Évaluation LLM]].
- Dimensionner un **entraînement** ou un fine-tuning : l'outil raisonne inférence.
- Modèles absents du catalogue, notamment des poids privés ou très récents.

## Installation & plateformes

- `brew install llmfit` (macOS, Linux), `scoop install llmfit` (Windows), `uv tool install -U llmfit`, `cargo install`, script d'installation, ou binaires prébuild.
- Cibles : macOS Intel et Apple Silicon, Linux x86_64 et ARM64, Windows x86_64.
- TUI interactive par défaut ; sortie CLI et JSON pour le scriptage ; un mode serveur expose une API REST et un tableau de bord web.
- Aucune dépendance à un service tiers pour la détection matérielle ; le partage de benchmarks est explicite et opt-in.

## Pièges

- La **vitesse est estimée**, pas mesurée sur la machine : c'est un ordre de grandeur pour trier, pas un engagement de débit.
- L'axe **qualité** provient du catalogue et vieillit vite ; un classement n'arbitre pas une tâche particulière.
- Les estimations mémoire ignorent souvent le coût réel du **cache KV** à long contexte — la marge annoncée peut disparaître en usage.
- Sur **MoE** et **multi-GPU**, les hypothèses de répartition sont plus fragiles que sur un modèle dense mono-GPU.
- Les benchmarks communautaires sont **auto-déclarés**, sur du matériel non contrôlé.

## Alternatives

Aucun outil équivalent n'est référencé dans le brain à ce jour : la catégorie `tooling/llm` est neuve et llmfit y est seul.

## Liens

- Runtimes cibles : [[Dev/Services/Ollama|Ollama]], [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/LM Studio|LM Studio]].
- [[Comparatif - Exécution & serving LLM]] — comparatif des runtimes qui, eux, servent le modèle
- [[Quantization]] — concept : le levier principal de la tenue en mémoire
- [[Small Language Models]] — concept : la classe de modèles que ce cadrage rend accessible
- [[Tokenization]] — concept : ce qui détermine le coût du contexte
- Repo : https://github.com/AlexsJones/llmfit
