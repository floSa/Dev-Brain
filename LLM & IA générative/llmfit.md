---
role: brique
nom: llmfit
alias: [llm-fit, alexsjones/llmfit]
pitch: "CLI Rust (MIT) qui détecte le matériel — RAM, CPU, GPU, VRAM, backend d'accélération — puis classe des centaines de modèles locaux sur quatre axes : tenue en mémoire, vitesse estimée, qualité et contexte ; TUI interactive, mode script et benchmarks communautaires."
categorie: llm/outillage
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Rust
alternatives: []
complements: []
tags: [local-llm, hardware-sizing, quantization, benchmark, terminal-ui]
url_docs: https://github.com/AlexsJones/llmfit
url_repo: https://github.com/AlexsJones/llmfit
---

# llmfit

<!-- AUTO:BANDEAU:START -->
> CLI Rust (MIT) qui détecte le matériel — RAM, CPU, GPU, VRAM, backend d'accélération — puis classe des centaines de modèles locaux sur quatre axes : tenue en mémoire, vitesse estimée, qualité et contexte ; TUI interactive, mode script et benchmarks communautaires.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Répond à une question qui précède tout déploiement local : **quel modèle cette machine
peut-elle réellement faire tourner**. L'outil inspecte le matériel — cœurs CPU, RAM, GPU
dédié ou intégré, VRAM, architecture d'accélération (CUDA, Apple Silicon, ROCm, OneAPI) —
puis confronte ce profil à un catalogue de plusieurs centaines de modèles. Le résultat n'est
pas un oui/non mais un classement sur **quatre axes** : tenue en mémoire, vitesse estimée,
qualité, longueur de contexte soutenable — un modèle peut tenir en mémoire et rester
inutilisable en vitesse, et les axes séparés rendent ce compromis lisible au lieu de le
masquer derrière un score unique. Il **outille la décision, il ne sert aucun modèle** : les
runtimes d'inférence sont détectés comme environnements cibles, pas remplacés. Il gère les
configurations multi-GPU, les architectures Mixture-of-Experts — dont les paramètres actifs
ne correspondent pas à l'empreinte totale —, le choix du format de quantization (GGUF, AWQ,
GPTQ, EXL2) et une surcharge manuelle de la mémoire pour simuler une autre machine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Dimensionner un poste ou un serveur avant d'acheter du matériel ou de choisir un modèle | Servir le modèle : c'est le rôle des runtimes → [[Ollama]], [[llama.cpp]], [[vLLM]] |
| Arbitrer entre plusieurs quantizations d'un même modèle sur une machine donnée | Mesurer la **qualité** d'un modèle sur une tâche métier : l'axe qualité est une note de catalogue qui vieillit vite, pas une évaluation → [[Comparatif - Évaluation LLM]] |
| Simuler une cible différente de la machine courante, via la surcharge de mémoire | Dimensionner un **entraînement** ou un fine-tuning : l'outil raisonne inférence |
| Confronter une intuition de faisabilité à des mesures réelles remontées par d'autres | Modèles absents du catalogue, notamment des poids privés ou très récents |
| | La vitesse est **estimée** et non mesurée, les estimations mémoire ignorent souvent le coût réel du cache KV à long contexte, et les hypothèses de répartition sur MoE ou multi-GPU sont plus fragiles que sur un dense mono-GPU : un ordre de grandeur pour trier, pas un engagement de débit |
| | Les benchmarks communautaires sont auto-déclarés, sur du matériel non contrôlé |

## Mise en œuvre

- Installation — `brew install llmfit` (macOS, Linux), `scoop install llmfit` (Windows), `uv tool install -U llmfit`, `cargo install`, script d'installation, ou binaires prébuild
- Point d'entrée — TUI interactive par défaut ; sortie CLI et JSON pour le scriptage ; un mode serveur expose une API REST et un tableau de bord web
- Prérequis — macOS Intel et Apple Silicon, Linux x86_64 et ARM64, Windows x86_64 ; aucune dépendance à un service tiers pour la détection matérielle
- Exécution — en ligne de commande sur le poste, rien à héberger ; `llmfit bench --share` alimente un jeu de mesures communautaires, en opt-in explicite
- Coût — gratuit

## Écosystème

### Alternatives

Aucun outil équivalent n'est référencé dans le brain à ce jour : llmfit y est seul sur ce
créneau — décider quel modèle une machine peut tenir, sans le servir.

## Ressources

- Dépôt — https://github.com/AlexsJones/llmfit

## Voir aussi

- [[Quantization]] — la notion : le levier principal de la tenue en mémoire
- [[Small Language Models]] — la notion : la classe de modèles que ce cadrage rend accessible
- [[Tokenization]] — la notion : ce qui détermine le coût du contexte
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les runtimes qui, eux, servent le modèle
- [[LM Studio]] — autre runtime détecté comme environnement cible
- [[LLM & IA générative]] — le hub du domaine
