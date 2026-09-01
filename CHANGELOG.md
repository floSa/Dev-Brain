---
galaxie: meta
nom: CHANGELOG
type: meta-doc
created: 2026-05-20
modified: 2026-09-03
tags: [meta]
---

# Changelog DevBrain

> Log des changements significatifs sur la **taxonomie**, les **conventions**, et les **piliers structurels**. Pas un dump de tous les ajouts de fiches — ceux-ci se voient dans `git log`.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/).

---

## [Unreleased]

À venir éventuellement :
- CI : validation frontmatter via GitHub Action (le hook `Stop` la couvre en session, pas les éditions Obsidian)
- Job planifié de joignabilité des URLs — `verifier_fraicheur.py` sonde déjà, mais 403/429 sont confondus avec un 404 et rien n'est bloquant
- Computer vision (concepts CNN, Transformers vision, segmentation)
- NLP traditionnel (BERT, tokenization spécialisée)
- Patterns : Active learning, RAG hybride, Multi-tenant SaaS
- Couche embedding sur `discover-links.ps1` (similarité sémantique au-delà des tags)
- Pre-commit hook : auto-run `audit-links` et bloquer si liens manquants > seuil

## [2026-09-03 — Audit en six axes, taxonomie à deux axes, validateur armé]

Le vault avait grandi au fil de l'eau — 647 pages, 112 catégories, 321 tags — sans que son rangement, ses contrôles ni ses skills soient instruits à froid. Six audits menés en conversations isolées (rapports dans `AI/audit/rapports/`), puis dix correctifs. La cause commune de la plupart des défauts : **la mécanique annoncée n'existait pas**. Le hook `Stop` documenté depuis juin n'avait jamais tourné une seule fois et ne pouvait pas tourner.

### Added — la taxonomie prend un second axe

- **Champ `famille:`** sur les 336 fiches Dev — 9 valeurs fermées (`paquet` 177, `plateforme` 78, `application` 28, `cli` 17, `saas` 13, `extension` 12, `modele` 5, `specification` 4, `annuaire` 2). Il porte la **nature** de la brique ; `categorie:` garde le **domaine**. `type:` cesse de porter la nature : l'audit a mesuré qu'il n'était pas discriminant, 57 fiches en `application`/`cli`/`extension` se répartissant en 34 `type: outil` et 23 `type: service`.
- **Arbre de décision déterministe** dans `taxonomie.md` : 9 questions fermées en ordre strict pour la famille, les branches de domaine, et des règles de départage. Le rangement d'un repo entrant ne dépend plus de qui écrit la fiche.
- **Skill `cloturer-brain`** — la clôture mécanique (régénérer, valider, vérifier la divergence, committer, intégrer) sort d'`enrichir-brain`, où elle était **dupliquée trois fois**. Idempotent et invocable seul, il couvre le cas qui ne l'était par rien : une modification faite à la main dans Obsidian. **Seul endroit du vault où la politique git est écrite.**
- **`AI/scripts/verifier_fraicheur.py`** — détecte les faits périmés des fiches (dépôt transféré ou archivé, licence divergente, version périmée, URL détournée, corps contredisant le `status:`). C'est un rapport, jamais un correcteur : il sort toujours en 0 et n'écrit dans aucune fiche.
- **`AI/scripts/audit_mesures.py`** — état des lieux chiffré et reproductible, socle factuel commun des audits.
- **`.claude/settings.json` versionné**, avec un hook `Stop` qui lance `check_brain` dès qu'une session a touché `Dev/` ou `Wiki/`.
- **`Templates/Outil-Dev.md`** — les 39 fiches Outil suivaient un gabarit implicite parfaitement tenu mais jamais écrit ; aucune fiche neuve n'aurait posé le nouvel axe.
- **`MOC/Types/`** — hubs générés par `type:` et non par `categorie:`, ce qui rend les Patterns et les Rules atteignables.

### Changed — `categorie:` éclate en 94 domaines

- **266 des 336 fiches Dev changent de catégorie.** Plus gros domaine : 13 pages contre 64 avant (`ml/framework`). Part des trois plus gros : **10,1 % contre 32,7 %**. `ml/framework` (64 pages) se répartit en 17 domaines, `llm/framework` (33) en 10, et le préfixe `tooling/*` (86 pages, 19 familles) disparaît — ce n'était pas un domaine mais un fourre-tout de natures.
- **29 des 47 comparatifs `.base`** reprises : 15 par substitution de valeur, 10 réécrits parce que leur catégorie source éclatait, 4 filtres par tag ramenés sur `categorie` après preuve que les membres étaient identiques. Aucun ne tombe sous 2 membres. `MOC/Categories/` passe de 15 à 20 hubs.
- **`check_brain.py` : 6 règles → 16**, dont 10 dures neuves. Les liens du **frontmatter** entrent dans le contrôle de liens morts ; les 4 types de pages qui n'avaient aucun gabarit contrôlé (`outil`, `pattern`, `rule`, `rex`) en ont un ; un `type:` absent est refusé ; la réciprocité échoue explicitement au lieu d'être ignorée en silence ; la synchronisation des pitchs — règle cardinale du skill — est enfin vérifiée. Chaque règle a été **vue échouer** avant d'être acceptée.
- **`brain-index.json` : 10 champs → 13** (`status`, `maturite`, `famille`). Huit briques `abandonne` étaient proposables par `planifier-projet`, qui filtre l'index sans ouvrir les fiches. Le skill écarte désormais d'office une brique abandonnée et propose son `remplace_par:`.
- **Procédure de mise à jour d'une page** dans `enrichir-brain`, avec sa table « champ modifié → consommateurs à repropager → commande de vérification » pour 12 champs. Elle n'existait pas : l'instruction tenait en cinq mots, « patch la fiche concernée ».
- **Convention de réinjection du pitch tranchée** — quatre variantes coexistaient, ce qui rendait la règle cardinale inapplicable. Une seule reste, en trois clauses. Le passif de 14 lignes désynchronisées est soldé.
- **16 fiches corrigées sur des faits périmés** : `fastmcp` → `PrefectHQ`, `hydra` → `hydra-ecosystem` (sortie de la tutelle Meta le 2026-08-13, gouvernance communautaire), `AutoGen` en maintenance, plus 5 `url_docs` et 6 passages en `abandonne`/`deprecated`.

### Removed — le pilier REX

- **Le pilier REX est supprimé**, les retours d'expérience vont dans la section `## Pièges` de la fiche Service. Motif : il n'avait **jamais produit un seul retour réel** en 86 jours — son unique fiche était un exemple de gabarit auto-déclaré — et la cible de fusion existait déjà, les 297 fiches Service portant toutes une section `## Pièges` remplie. Il coûtait 34 pointeurs morts invisibles du validateur et une exception permanente dans deux scripts, qui ne protégeait aucun lien tout en désarmant le contrôle pour la classe entière des liens `REX - *`.
- Supprimés : `Dev/REX/`, `Templates/REX.md`, `Templates/REX-entry.md`, les tags `rex` et `bugs`, la section « Conventions REX » de `CLAUDE-build.md`, la section « Log de bug » de `CLAUDE-project.md`.
- **`created:` et `modified:`** retirés des 5 Patterns et 5 Rules : 9 des 10 mentaient (2026-06-11 déclaré, 2026-07-14 réel), aucun script ne les lisait, et aucune autre page v2 ne les portait.
- **Trois MOC de catégorie** dont le préfixe n'existe plus : `Auth`, `Frameworks`, `Outils & libs`.

### Fixed

- **La politique git n'avait pas de source unique** : `enrichir-brain` disait « d'office, sans demander », `CLAUDE-build.md` disait « ne commit et ne push jamais automatiquement », `CLAUDE.md` la rangeait dans ce qui exige confirmation. Trois documents, deux contradictions frontales. Tout renvoie désormais vers `cloturer-brain`.
- **`scaling: serverless-ok`** documenté dans `CLAUDE-build.md` et `brain-v2.md` : valeur que ni le gabarit ni le validateur ne connaissent. Un agent suivant la consigne à la lettre écrivait une fiche rejetée.
- **Chemin de vault en dur** (`~/DevBrain`) dans `session_to_devbrain.py` et `CLAUDE-project.md`, hérité d'une machine antérieure — en contradiction avec `Documentation/perso/machines.md`. Remplacé par une résolution racine git → variable d'environnement.
- **`build_mocs.py` ignorait en silence** les 11 pages sans `categorie:` ; il les compte et les nomme désormais.
- **Trois balayages depuis la racine du vault** excluaient `.git` mais pas `.claude/`, où vivent les worktrees git — donc des copies complètes du vault. Conséquence grave et silencieuse : un wikilink mort pouvait se résoudre contre la copie d'un worktree, masquant une violation d'une règle dure.
- **Le parseur de `taxonomie.md` lisait tous les blocs de code** : déclarer les familles dans un bloc nu aurait rendu `categorie: paquet` valide (122 catégories reconnues au lieu de 112). Les fences sont désormais distingués par leur langue.

### Notes

- **Le `fetch` HTTPS anonyme de `origin` a cessé de fonctionner** (`could not read Username`). Or le protocole de session commence par `git fetch origin` pour détecter une divergence : cet échec est silencieux si l'on ne lit pas sa sortie. Passer par l'alias SSH, ou basculer `origin` en SSH.
- **`Wiki/` n'a pas été touché** de toute la session, hormis quatre concepts recâblés vers de nouvelles fiches Dev. Les 12 `concept/<sous-domaine>` gardent leur vocabulaire ; l'aligner sur les 94 domaines Dev est la question ouverte 5 de l'axe 1.
- **32 avertissements souples assumés** : 13 domaines à 3+ pages sans comparatif, 13 collisions d'alias, 6 sur les comparatifs. Plus 102 au titre de la règle R15 (une fiche service sans aucun lien vers `Wiki/Concepts`) — le couple Dev↔Wiki que le skill impose n'existe pas sur un tiers des fiches. Aucun domaine n'a été fusionné pour faire baisser un compteur.
- **Deux arbitrages en attente** : les quatre pages hors périmètre du brain (`OpenCut`, `SmartTube`, `Superwhisper`, `public-apis`) et la création des comparatifs manquants — décisions éditoriales, pas techniques.

## [2026-07-07 — Harmonisation documentaire post-migration v2]

La reconstruction v2 (2026-06-04/05, cf. `AI/design/brain-v2.md`) avait changé la structure du vault (`Dev/`, `Wiki/`, `MOC/`, `Documentation/`) et les skills (`enrichir-brain`, `planifier-projet` remplaçant les 12 skills v1) sans mettre à jour les meta-docs. Repéré début juillet : `README.md`, `CLAUDE.md`, `CLAUDE-build.md`, `CLAUDE-project.md`, `INSTALL.md`, `CONTRIBUTING.md` décrivaient encore l'arborescence et les skills v1.

### Changed — Meta-docs réalignés sur la v2

- **`README.md`** — structure réelle, stats à jour (264 Services, 261 Concepts, etc.), table des 2 skills réels, avertissements sur les docs pas encore réalignées.
- **`CLAUDE.md`** — chemins `Dev/`/`Wiki/`/`MOC/`/`Documentation/`, conventions de nommage v2, skills réels dans `.claude/skills/`.
- **`CLAUDE-build.md`** — schéma frontmatter réel (Service : ~14 champs, champs morts `score`/`mes_projets`/etc. actés comme supprimés), taxonomie renvoyée vers `Documentation/general/taxonomie.md`, workflow `enrichir-brain` au lieu des 5 skills v1 ; règle Git durcie (plus d'auto-commit/push, cohérent avec `CLAUDE.md`).
- **`CLAUDE-project.md`** — chemins `Dev/Rules`, `Dev/REX` ; suppression des références à `Rules/Documentation/` et `Templates/ServiceDocs/` (jamais remigrés) ; kickoff via `planifier-projet`.
- **`INSTALL.md`** — section Templater et section skills (2 réels, `.claude/skills/`) ; code couleur ramené à 3 galaxies (`dev`/`wiki`/`meta`) + regroupement par chemin pour les skills (`.claude/skills/`, plus `AI/skills/` qui n'existe pas) ; référence Roadmap corrigée (`Wiki/Roadmaps/`, vide).
- **`CONTRIBUTING.md`** — anatomie du repo et workflows type réécrits avec les vrais dossiers/skills v2 ; statuts Outils alignés sur Services (`actif/en-eval/abandonne`).

### Notes

- `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` restent vides (scaffold seulement) — contenu v1 pas remigré, cf. `Documentation/perso/reservoir-v1.md` et `Archive-v1.zip`.
- 3 fichiers non trackés suspects repérés à la racine et dans `Dev/Patterns/` (doublons de `.base` existants) — décision utilisateur en attente.

## [2026-05-20 (4) — Hygiène vault : audits, wikilinks, galaxie meta]

Outillage et nettoyage massif du vault, après les marathons V6-V24.

### Added — Scripts d'audit et de découverte (`AI/scripts/`)

- **`audit-vault.ps1`** — Audit complet : pages vides/stubs, sans galaxie,
  fiches Concepts incomplètes, wikilinks fantômes. Génère
  `AI/audits/audit-YYYY-MM-DD.md`.
- **`discover-links.ps1`** — Engine de découverte de wikilinks par
  similarité metadata (alias / categorie / domaines / sous_categories /
  tags / mots du titre). Scoring pondéré, top-N candidats avec
  justification. Usage : avant création (metadata) ou sur fiche existante
  (`-Path`).
- **`audit-links.ps1`** — Pour chaque fiche du vault, détecte les liens
  pertinents manquants (candidats forts non-linkés). Génère
  `AI/audits/links-audit-YYYY-MM-DD.md`.

### Added — Intégration `discover-links` dans 5 skills de création

- `add-wiki-concept`, `add-wiki-outil`, `add-wiki-workflow`,
  `add-service`, `add-pattern` : leur étape "Wikilinker" appelle
  désormais `discover-links.ps1` avec les metadata pressentis et
  présente les top candidats à l'utilisateur (workflow + reverse linking).
- Documentation de la stratégie : `AI/decisions/2026-05-20-discover-links-strategy.md`.

### Added — 4e galaxie `meta` (slate-gray)

- Champ `galaxie: meta` (couleur `#94A3B8`) pour les docs du brain
  lui-même : CHANGELOG, README, INSTALL, Home, Inbox, CLAUDE.md,
  CLAUDE-build.md, CLAUDE-project.md, CONTRIBUTING.md, +
  `AI/audits/`, `AI/decisions/`, `AI/scripts/`.
- CSS `.obsidian/snippets/galaxies.css` étendu (sélecteurs sidebar,
  onglets, frontmatter, source/preview view).
- `CLAUDE-build.md` : ajout de la galaxie meta dans la table de
  référence des 3-galaxies → désormais 4-galaxies.

### Fixed — Wikilinks fantômes et casse

- Corrigés ~20 wikilinks case-sensitive : `Embeddings` →
  `embeddings`, `MCP Protocol` → `mcp-protocol`,
  `Tool Use` → `tool-use`, `Agent loops` →
  `agent-loops`, `AUC` → `ROC AUC`,
  `Multiple testing` → `Multiple testing correction`,
  skills Claude bundled (`loop` → `claude-loop`, etc.),
  `Wiki-Skill` → `Wiki-Outil`.
- Dewikilink-és les fantômes purs (concepts non créés) :
  Great Expectations, MLops, Random Forest, Reinforcement learning,
  Thompson sampling, VAE/autoencoder.
- Supprimés 8 fichiers parasites racine 0-ligne créés par Obsidian sur
  clic wikilink fantôme (Dash, hydra, Shiny for Python, Redis,
  Pattern - Z, Rules/Types/X, Unstructured, X, Y).

### Added — Section `Code minimal` pour 6 fiches LLM/AI eng anciennes

Format pre-marathon manquait `Code minimal`. Ajout d'exemples concrets
dans : `RAG` (pipeline Anthropic + sentence-transformers + FAISS),
`embeddings` (BGE/OpenAI + Matryoshka + binary quant),
`agent-loops` (ReAct from scratch + critique pattern),
`mcp-protocol` (MCP server Python FastMCP + intégration Claude),
`prompt-caching` (Anthropic explicit + OpenAI auto + Gemini + ROI calc),
`tool-use` (round-trip Anthropic + OpenAI + Pydantic validation).

### Stats finales du vault

| Métrique | Valeur |
|---|---:|
| Total .md | 315 |
| Sans galaxie | **0** (était 22) |
| Pages vides | 3 (templates Templater, normal) |
| Stubs | 115 (légitimes : SKILL.md, REX, services courts) |
| Concepts incomplets | 0 |
| Wikilinks fantômes | 133 (alternatives Services voulues — workflow Obsidian click-to-create) |

## [2026-05-20 (3) — Marathon AI Engineering : Roadmap-AI + vagues V15-V24]

Import du document `competences_ai_engineer.md` (~2866 lignes, sans section 11 GPU)
en `Wiki/Roadmap-AI.md`, puis 10 vagues autonomes pour couvrir l'AI eng complet.

### Added — `Wiki/Roadmap-AI.md`

- ~2525 lignes, carte AI engineer (sections 1-10 et 12, sans GPU/scale)
- Frontmatter `galaxie: wiki, type: roadmap`
- Lié depuis Home.md

### Added — Vague V15 Transformers & architectures (7 concepts)

- Self-attention, Positional encoding (RoPE/ALiBi), Tokenization (BPE/SentencePiece)
- Transformer architectures (encoder/decoder/encoder-decoder)
- Flash Attention & efficient attention (FA1-3, GQA/MQA/MLA, PagedAttn)
- Mixture of Experts (Mixtral/DeepSeek/Llama 4)
- State Space Models (Mamba, RWKV, Jamba)

### Added — Vague V16 LLM training & adaptation (6 concepts)

- SFT (instruction/chat tuning), RLHF & DPO (PPO/DPO/GRPO/KTO)
- PEFT (LoRA/QLoRA/DoRA), Quantization (GPTQ/AWQ/GGUF/NF4)
- Scaling laws (Chinchilla, emergent), Distillation (Hinton, Phi, R1)

### Added — Vague V17 Inference & prompt engineering (6 concepts)

- Decoding strategies, Speculative decoding (Medusa/EAGLE/lookahead)
- Prompt engineering (CoT/ToT/ReAct/DSPy), Structured outputs (Outlines/Instructor)
- Context engineering (prompt caching, lost-in-middle), Inference optimization (vLLM/SGLang)

### Added — Vague V18 RAG avancé (5 concepts)

- Chunking strategies (recursive/semantic/late/Contextual Retrieval)
- Hybrid retrieval (BM25+dense/RRF/SPLADE/ColBERT)
- Reranking (Cohere/BGE/ColBERT/LLM rerankers)
- Query transformations (HyDE/multi-query/decomposition/RAG-Fusion)
- Advanced RAG (Self-RAG/CRAG/GraphRAG/RAPTOR/agentic)

### Added — Vague V19 Agents (5 concepts)

- Agent patterns (ReAct/Plan-Execute/Reflexion/LATS, workflow vs agent)
- Tool use patterns (function calling/parallel/MCP/computer use)
- Agent memory (MemGPT/Letta/Mem0/Zep)
- Multi-agent systems (AutoGen/CrewAI/LangGraph/debate)
- Agent evaluation (SWE-Bench/GAIA/BFCL/tau-bench)

### Added — Vague V20 Multimodal AI (5 concepts)

- Vision Language Models (LLaVA/Qwen-VL/Claude/GPT-4o)
- Diffusion models (DDPM/DDIM/SDE/CFG/latent/DiT)
- Image generation (SDXL/FLUX/SD3, ControlNet, LoRA, DreamBooth)
- Speech models (Whisper, ElevenLabs/F5-TTS, voice agents)
- Video generation (Sora/Veo/Runway/HunyuanVideo)

### Added — Vague V21 LLM production (5 concepts)

- LLM observability (Langfuse/LangSmith/Helicone, OTel)
- Guardrails (NeMo/Guardrails AI/LLM Guard, input+output filters)
- LLM routing & cascading (RouteLLM/NotDiamond/LiteLLM)
- Reliability patterns (retries/circuit breakers/fallbacks)
- LLM caching (exact/semantic/prompt/KV cache reuse)

### Added — Vague V22 LLM evaluation (4 concepts)

- LLM benchmarks (MMLU-Pro/GPQA/HLE/IFEval/Arena)
- Code & math benchmarks (HumanEval/SWE-Bench/AIME/MATH)
- LLM-as-judge (G-Eval/Prometheus, biais)
- RAG eval (RAGAS faithfulness/answer relevance/context precision)

### Added — Vague V23 AI safety & security (3 concepts)

- Prompt injection (direct/indirect/multi-turn, OWASP LLM01)
- Jailbreaking & defenses (DAN/GCG/many-shot, constitutional AI)
- AI security (sleeper agents/supply chain/safetensors/MITRE ATLAS)

### Added — Vague V24 Frontier & advanced (4 concepts)

- Small Language Models (Phi/Gemma/SmolLM/OLMo, edge)
- Reasoning models (o1/o3/R1/GRPO, test-time compute)
- Synthetic data generation (Self-Instruct/Evol/Magpie/Cosmopedia)
- Chain-of-Thought (zero-shot/few-shot/self-consistency/ToT)

### Stats

- Concepts Wiki : 76 → **127** (+51)
- Roadmaps : 2 (DS/ML + AI Engineer)
- Couverture AI Engineering : presque exhaustive

## [2026-05-20 (2) — Marathon métriques + TS + production ML : vagues V12-V14]

Inspiré par la galaxy DEV (services Prophet/statsforecast/neuralforecast/darts
+ workflow "Evaluer un modele forecast") qui manquaient leur fondement
théorique en wiki.

### Added — Vague V12 Métriques d'évaluation (5 concepts)

- Regression metrics, Classification metrics, Forecasting metrics,
  Ranking metrics, LLM eval metrics

### Added — Vague V13 Time series approfondi (6 concepts)

- ARIMA SARIMA, Exponential smoothing, Hierarchical forecasting,
  Intermittent demand, Time series anomaly detection, Time series feature engineering

### Added — Vague V14 Data quality & production ML (5 concepts)

- Data leakage, Data drift, Imbalanced classification,
  Feature engineering, Missing data

### Stats

- Concepts Wiki : 60 → **76** (+16)
- Couverture forecasting maintenant complète (du basique au lumpy/hierarchical)
- Section "data quality & production" couvre les pieges senior-level critiques

## [2026-05-20 — Marathon fondamentaux DS/ML : Roadmap + vagues V6-V11]

Import du document de référence `competences_ds_ml.md` (~1500 items) en `Wiki/Roadmap.md`,
puis 6 vagues autonomes pour combler les fondamentaux théoriques (35 concepts).

### Added — `Wiki/Roadmap.md`

- ~2770 lignes, carte exhaustive DS/ML (6-7 niveaux de profondeur)
- Frontmatter `galaxie: wiki, type: roadmap`
- Lié depuis `Home.md`

### Added — Vague V6 Théorie de l'information (7 concepts)

- Shannon entropy, Cross-entropy, KL divergence, Jensen-Shannon divergence,
  Wasserstein distance, Mutual information, Perplexity

### Added — Vague V7 Algèbre linéaire pour ML (6 concepts)

- SVD, Eigendecomposition, Vector norms, Matrix decompositions,
  Matrix products, Projections

### Added — Vague V8 Optimisation (6 concepts)

- Gradient descent, Adam optimizer, Newton & quasi-Newton, Convexity,
  Learning rate schedules, Loss landscape and saddle points

### Added — Vague V9 Théorie de l'apprentissage (5 concepts)

- VC dimension, PAC learning, No Free Lunch theorem,
  Rademacher complexity, Generalization bounds

### Added — Vague V10 Probabilités fondamentales (6 concepts)

- Markov chains, Poisson process, Brownian motion, Central limit theorem,
  Concentration inequalities, MCMC

### Added — Vague V11 Stats avancée / expérimentation (6 concepts)

- Maximum likelihood estimation, MAP estimation, Bayesian inference,
  A/B testing, CUPED, Multi-armed bandits

### Stats

- Concepts Wiki : 24 → **60** (+36)
- Couverture du Roadmap : ~5% → ~30%

## [2026-05-19 (3) — Refactor 3-galaxies + vagues DS V3-V5 + patterns]

### Added — Vague V3 ML supervisé classique

- 6 concepts : Bias-variance, Cross-validation, Regularization, Ensembling, ROC AUC, Calibration
- 3 services ML : XGBoost, LightGBM, CatBoost

### Added — Vague V4 Stats inférentielle

- 6 concepts : Hypothesis testing, t-test and ANOVA, Chi-squared tests, Bootstrap, Multiple testing correction, Confidence intervals
- 2 services : PyMC (bayésien), lifelines (survie)

### Added — Vague V5 Réduction dim & clustering

- 5 concepts : t-SNE and UMAP, K-means, DBSCAN, GMM, Clustering evaluation
- 2 services : umap-learn, hdbscan

### Added — 4 patterns architecturaux

- `Pattern - Agent ReAct` : agent autonome LLM avec tools + garde-fous + observabilité
- `Pattern - LLM Eval setup` : pipeline complet d'éval LLM (gold dataset + LLM-as-judge + CI + drift)
- `Pattern - Pipeline ELT moderne` : Parquet + DuckDB + dbt + Polars + Dagster/Airflow (medallion)
- `Pattern - Forecasting production` : statsforecast/neuralforecast + Airflow + MLflow + monitoring drift

### Added — Refactor 3-galaxies

- Renommage `Wiki/Skills/` → `Wiki/Outils/` (dossier + base + template + skill `add-wiki-outil`)
- Champ `galaxie: dev | wiki` ajouté au frontmatter de 137 fiches
- CSS snippet `.obsidian/snippets/galaxies.css` (3 couleurs : bleu/vert/violet)
- 3 skills update-wiki-* (concept/workflow/outil)
- 4 skills DEV (update-service, add-rule, update-rule, add-pattern)
- 3 skills meta (list-skills, add-custom-skill, validate-skill)
- Convention MCP Obsidian préférence documentée (CONTRIBUTING + sub-note référence)

### Added — Navigation

- `Home.md` à la racine — page d'accueil avec liens vers toutes les zones du brain

### Fixed

- 5 skills initiaux (add-service, compare-services, log-bug, propose-stack, add-wiki-outil) patchés pour conformité avec validate-skill grid
- Wikilinks fantômes corrigés (`DevBrain`, `Local REST API & MCP Server`)
- Templates Wiki-*.md ont `galaxie: wiki` (initialement `dev` par script bug)

### Changed — Conventions

- Taxonomie `categorie` étendue : `skill/{documents, dev-flow, code-quality, knowledge, data, meta}`
- Status workflow documenté : `discovered → tested → used → abandoned` pour Outils ; `actif → en-eval → abandonne` pour Services

### Stats post-marathon

- **70 services** (+14 sur la session)
- **24 concepts Wiki** (+17 sur la session)
- **4 workflows Wiki**
- **22 outils catalogués Wiki**
- **22 skills custom exécutables** (+10 sur la session)
- **6 patterns architecturaux** (+4 sur la session)
- **137 fiches au total** avec galaxie: explicite

## [2026-05-19] — Marathon Wiki + Services AI eng

### Added — Pilier Wiki/ (nouveau)

- **`Wiki/_guide.md`**, **`Wiki/_installer-un-skill.md`** : pages d'index
- **`Wiki/Outils/`** : 22 fiches skill curées dans 4 sous-dossiers
  - `Claude-Code/` (13 fiches) : 5 anthropic-skills + 8 native (api, init, review, security-review, simplify, update-config, keybindings-help, fewer-permission-prompts, loop, schedule, consolidate-memory, setup-cowork)
  - `Obsidian/` (2 fiches) : kepano-obsidian-skills, kepano-defuddle
  - `MCP-Servers/` (4 fiches) : mcp-obsidian, mcp-filesystem, mcp-github, mcp-postgres
  - `CLI-Tools/` (1 fiche) : uv
- **`Wiki/Concepts/`** (4 fiches) : RAG, prompt-caching, mcp-protocol, embeddings
- **`Wiki/Workflows/`** (2 fiches) : Bootstrap projet AI eng, Évaluer un système LLM
- **`Wiki/Comparatif - Outils.base`** : 3 vues filtrées (tous, discovered, used)

### Added — Services

6 fiches critiques pour AI eng / data eng :
- LiteLLM, Instructor, DSPy, PydanticAI (`Services/LLM/`)
- DuckDB (`Services/Databases/`)
- Polars (`Services/Data/`)

### Added — Patterns

- `Pattern - RAG basique.md` (stack + décisions clés + pièges)

### Added — Templates

- `Templates/Wiki-Outil.md`
- `Templates/Wiki-Concept.md`
- `Templates/Wiki-Workflow.md`

### Added — Skills custom (`AI/skills/`)

- `add-wiki-outil` : symétrique à `add-service`, pour le Wiki

### Added — Infra

- `.claude/settings.example.json` (allowlist read-only Bash + WebFetch ciblé + deny destructeur)
- `.claude/settings.local.example.json` (template perso pour push)
- `.claude/README.md`
- `INSTALL.md` (guide d'install pas à pas avec 25 captures dans `docs/install/`)
- `CONTRIBUTING.md`
- `CHANGELOG.md` (ce fichier)

### Changed — Conventions

- **Trois modes** au lieu de deux : `build`, `project`, **`wiki`**
- Taxonomie `categorie:` étendue avec `skill/{documents, dev-flow, code-quality, knowledge, data, meta}` pour les fiches Wiki/Outils
- Valeurs autorisées pour `status` documentées par périmètre :
  - Services : `actif | en-eval | abandonne`
  - Outils wiki : `discovered | tested | used | abandoned`
- `CLAUDE.md` : section `Mode wiki` ajoutée avec règles strictes (Wiki/ verrouillé hors mode wiki)
- `CLAUDE-build.md` : mention explicite que `Wiki/` est hors-périmètre du mode build
- `CLAUDE.md` identité utilisateur : personnalisée (DS / DE / MLops / ML eng / AI eng)

### Fixed

- Wikilinks brisés dans 4 fiches Wiki/Outils : `DevBrain` (n'existe pas) → plain text ; `Local REST API & MCP Server` (n'existe pas comme fiche) → référence inline + URL
- `.gitignore` : exclusion explicite de `.obsidian/plugins/`, `.obsidian/community-plugins.json`, `.claude/settings.local.json`

### Notes

- Identité Git du repo : `floSa <34608761+floSa@users.noreply.github.com>` (extraite de la clé SSH perso, set en local au repo)
- Remote : basculé sur SSH perso (`git@github.com-perso:floSa/DevBrain.git`)

---

## [2026-05-pré] — État avant le marathon

Snapshot de référence avant les changements du 19 mai (cf. README, section *État du brain (mai 2026)*) :
- ~50 fiches Services
- 8 comparatifs `.base`
- 1 pattern architectural
- Rules : Global + Types + Documentation
- Templates : Service, Pattern, Rule, Project, REX, ServiceDocs
- 5 skills custom : add-service, compare-services, log-bug, propose-stack, doc-service
- 0 Wiki, 0 documentation utilisateur formelle
