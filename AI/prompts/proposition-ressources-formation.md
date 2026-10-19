# Proposition d'ajouts depuis les documents « Ressources_Formation_IA »

Établie le 2026-10-19 par lecture de 29 documents (six lectures parallèles, lecture seule). À valider par floSa avant tout lot. Aucune page n'est écrite.

Source : `C:\Users\FlorianHorellou\OneDrive - Aosis Consulting\Documents\Ressources_Formation_IA\<dossier>\<dossier>.md` (vu de WSL : `/mnt/c/Users/FlorianHorellou/OneDrive - Aosis Consulting/Documents/Ressources_Formation_IA/`).

## Règles retenues pour ces lots

- Règle 15 corrigée : gratuit et déployable sur site. Service payant, cloud seulement, licence non vérifiée : texte simple, pas de page.
- Les prix, classements, versions et sorties de modèles vieillissent vite : ils ne vont pas en notion. Les **méthodes de lecture** et les **formules** sont durables.
- Rien n'est écrit dans une page `role: notion` existante de floSa : les enrichissements se proposent.
- Schémas : refaits en Mermaid ou SVG, source citée avec l'horodatage de la vidéo. Les captures d'écran de vidéos d'autres auteurs ne sont pas copiées dans le dépôt public (1 867 images, 271 Mo, sous-titres incrustés).
- Chaque lot termine par `bash AI/scripts/verifier_depot.sh` : GitHub ne porte que `main`, tout est poussé (règle 18).

## Lot 31 — Inférence : mémoire, débit, coût d'un token

Notions : plafond de débit d'un GPU (roofline) ; dimensionner la mémoire d'un serveur LLM ; taille du cache KV par token ; prefill par morceaux, désagrégation prefill/decode, TTFT/ITL ; parallélisme en inférence (tenseurs, données, experts) ; coût d'un token et taux d'utilisation ; mesurer une latence. Sources : Inference_LLM_sur_GPU, Servir_un_LLM, Economie_de_l-Inference, DeepSeek-V4.1-Flash, LightOnOCR (calcul de débit).

## Lot 32 — Lire un tarif, un score, un service

Notions : tarif catalogue contre coût par tâche ; effort de raisonnement et courbe coût/qualité ; lire un score publié (indice composite versionné, checkpoint ajusté, banc saturé) ; ce qui change derrière une API ; canari de dérive d'un LLM en API (candidat pattern). Briques (poids ouverts, sur site) : DeepSeek-V4.1-Flash (MIT), MiMo-V2.6-Flash et Pro (MIT), Qwen-Image et Qwen-Image-Layered (Apache-2.0, licence à relire), Qwen-Image-2.1 (non commercial : avertissement en première phrase). Comparatif : ajouts au comparatif des modèles open weights. Sources : Claude-Opus-5.5, GPT-6-Sol-et-Luna, Xiaomi-MiMo, Gemini-3.8-Live, Qwen-Image-2.1, Modeles_Nerfes.

## Lot 33 — Modèles de décision (famille absente du brain)

Notions : modèle de décision ; choisir entre règle, classifieur ajusté, modèle de décision et LLM ; décomposer une question en signaux étroits ; entraîner pour la calibration (daté). Briques : Clef et Clef-flash et Clef-omni (Apache-2.0), Laya (Apache-2.0, à ajuster), d1-3B et d1-omni-600M (LFM Open License). Jev : texte simple (API fermée). Comparatif : Modèles de décision. Source : les cinq dossiers « Jev / Laya / Clef / Modèles de décision ».

## Lot 34 — OCR et documents

Notions : évaluer un OCR (CER, F1 de boîtes, banc de test) ; OCR vision-langage en une passe avec grounding ; cascade OCR et contrôle arithmétique des factures (candidat pattern) ; couche de texte d'un PDF contre OCR. Briques : LightOnOCR-3 (Apache-2.0), Indra OCR (code Apache-2.0, poids OpenRAIL-M modifiée, gratuit pour floSa). Ajouts au comparatif de parsing de documents. Sources : LightOnOCR-3, Indra-OCR.

## Lot 35 — RAG : droits, multimodal, hiérarchique

Notions : droits d'accès dans un RAG (priorité, profil ESN) ; coller le corpus ou récupérer (règle de décision, coût avec cache) ; embedding multimodal et modality gap ; RAG hiérarchique (RAPTOR, parent-enfant, STAIR). Briques : EmbeddingGemma 2 (Apache-2.0), Qwen3-VL-Embedding, SigLIP 2, LightRAG (MIT), Microsoft GraphRAG (MIT, en maintenance). Comparatifs : ajouts aux comparatifs d'embeddings et de bases vectorielles ; GraphRAG contre LightRAG. Sources : les trois documents RAG.

## Lot 36 — Agents : garde-fous hors modèle

Notions : garde-fous hors modèle (isolation, autorisation, approbation) ; excessive agency et lethal trifecta ; isolation par politique déclarative (Landlock, seccomp, proxy) ; checkpointing et reprise (idempotence) ; sycophancy. Briques : OpenShell (Apache-2.0, priorité), DeepSeek Harness et Cordis (MIT), sandbox-runtime (licence à vérifier). Comparatif : isolation d'exécution d'un agent, ou ajout à « Garde-fous pour LLM ». Sources : Securite_des_Agents, DeepSeek-Harness, Agents_IA_Harness.

## Lot 37 — Fondamentaux : méthodes et culture

Notions : RLVR (récompense vérifiable) ; vérificateur externe (et loi de Goodhart) ; boucle d'amélioration d'un agent ; pré-entraînement, affinage et apprentissage en contexte (zéro et quelques exemples) ; preuve formelle et assistant de preuve (Lean). Pages de culture, datées, avec leurs schémas Mermaid déjà prêts : histoire de l'IA 1943-2026 ; généalogie des modèles de langage 2011-GPT-3 (20 schémas). Sources : RLHF_DPO_GRPO, Auto-Amelioration, Navier-Stokes, Histoire_de_l-IA, Genealogie.

## Enrichissements à proposer à floSa (notions existantes, non modifiées sans accord)

- Calibration : calibrer par type de question ; le fine-tuning dégrade la calibration.
- Context engineering : nommer la compaction de contexte.
- Licences de modèles open weights : ajouter le cas `qwen-research`.
- GRPO : GSPO, RLOO, défaut de TRL sans terme KL.
- Scaling laws et Self-attention : compléments de la généalogie.
- GraphRAG : facteurs de coût d'indexation (1,6 à 11,7 fois le corpus).
- Late-interaction retrieval : calcul de stockage en kio, MUVERA.
- Ontologie : sens « plateforme » (objets, actions, permissions) et modèle sémantique.
- Deux phrases fausses du lot 29, à corriger : « Bases graphe — modèles et langages de requête » ligne 23 ; « Plongements de graphe et prédiction de liens » ligne 57.

## Écarté

Prix, classements et sorties datés (Opus, GPT-6, Gemini, Grok, Together, Fireworks, Groq, Cerebras) ; services payants ou cloud seulement ; démos ; chiffres d'éditeurs non recoupés ; Claude Code et Codex ; Neurons Cloudflare.

## Licences à lire à la source avant toute page

Marlin, MLX et mlx-vlm, XGrammar, NIXL, Mooncake, LMCache, ripgrep, PyMuPDF4LLM, Surya, ModernBERT et mmBERT, verl, OpenRLHF, Lean 4, sandbox-runtime, Qwen-Image-Layered.
