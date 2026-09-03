---
role: comparatif
nom: Comparatif - Évaluation LLM
categorie: llm/eval
tags: [llm-eval, rag-eval, llm-as-judge]
---

# Comparatif - Évaluation LLM

> On tranche sur : ce qu'on note — la sortie finale ou les étapes internes —, et où ça tourne : une suite de tests en CI, un fichier YAML déclaratif, ou une app instrumentée.

![[Comparatif - Évaluation LLM.base]]

## Ce qui départage

- [[Ragas]] — le spécialiste du **RAG**, et le seul à séparer explicitement la qualité du retrieval de celle de la génération (*context precision/recall* d'un côté, *faithfulness* de l'autre). Ses métriques sont **sans référence** et il génère les jeux de tests depuis les documents : on démarre sans dataset annoté. API 0.x remaniée — épingler la version.
- [[DeepEval]] — le « **pytest des LLM** » : des assertions dans le framework de test Python, donc une régression bloquée avant le merge. C'est aussi le plus large catalogue — 50+ métriques couvrant RAG, agents, tool-use, conversation et sécurité, plus *G-Eval* pour un critère écrit en langage naturel.
- [[promptfoo]] — **déclaratif** : prompts, fournisseurs, cas et assertions dans un YAML versionné, et `promptfoo eval` rend une matrice de comparaison côte à côte. C'est le seul du lot à porter un volet **red-teaming** (50+ types : injection, jailbreak, fuite). Racheté par OpenAI en mars 2026, licence MIT annoncée maintenue.
- [[TruLens]] — évalue **en instrumentant** : il capture les traces de l'app puis y attache des *feedback functions* qui notent chaque étape interne, pas seulement la sortie. C'est le socle de Snowflake AI Observability ; il trace, mais n'est pas une plateforme de monitoring multi-équipes hébergée.
