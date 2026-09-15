---
role: comparatif
nom: Comparatif - Évaluation LLM
categorie: llm/eval
tags: [llm-eval, rag-eval, llm-as-judge]
---

# Comparatif - Évaluation LLM

> On tranche sur : ce qu'on note — la sortie finale ou les étapes internes —, et où ça tourne : une suite de tests en CI, un fichier YAML déclaratif, une app instrumentée, ou un cadre de tâches pour agents. Deux membres n'ont pas la forme d'un cadre de test : [[Prometheus-Eval]] est le juge lui-même, un modèle ouvert qui tourne en local, et [[ARES]] et [[RAGChecker]] sont des méthodes de mesure de RAG — l'une calibre ses juges par PPI, l'autre attribue l'erreur au niveau claim.

![[Comparatif - Évaluation LLM.base]]

## Ce qui départage

- [[Ragas]] — le spécialiste du **RAG**, et le seul à séparer explicitement la qualité du retrieval de celle de la génération (*context precision/recall* d'un côté, *faithfulness* de l'autre). Ses métriques sont **sans référence** et il génère les jeux de tests depuis les documents : on démarre sans dataset annoté. API 0.x remaniée — épingler la version.
- [[DeepEval]] — le « **pytest des LLM** » : des assertions dans le framework de test Python, donc une régression bloquée avant le merge. C'est aussi le plus large catalogue — 50+ métriques couvrant RAG, agents, tool-use, conversation et sécurité, plus *G-Eval* pour un critère écrit en langage naturel.
- [[promptfoo]] — **déclaratif** : prompts, fournisseurs, cas et assertions dans un YAML versionné, et `promptfoo eval` rend une matrice de comparaison côte à côte. C'est le seul du lot à porter un volet **red-teaming** (50+ types : injection, jailbreak, fuite). Racheté par OpenAI en mars 2026, licence MIT annoncée maintenue.
- [[TruLens]] — évalue **en instrumentant** : il capture les traces de l'app puis y attache des *feedback functions* qui notent chaque étape interne, pas seulement la sortie. C'est le socle de Snowflake AI Observability ; il trace, mais n'est pas une plateforme de monitoring multi-équipes hébergée.

- [[Inspect AI]] — un cadre de **tâches composables** (dataset, solver, scorer) pensé pour évaluer des modèles et des **agents** : les agents externes comme Claude Code s'y branchent, et le code généré s'exécute dans un sandbox. Il embarque 200+ évaluations prêtes à lancer. Versionnage 0.x — épingler.
- [[Prometheus-Eval]] — **le seul du lot qui soit le juge lui-même** : des modèles ouverts (7B, 8x7B) qui notent selon une rubrique ou départagent deux réponses, en local sur GPU. Bibliothèque en beta, sans release depuis septembre 2024.

- [[ARES]] — **entraîne ses juges** : de petits modèles affinés sur données synthétiques, puis une correction statistique (PPI) qui donne un **intervalle de confiance**. Le prix est un jeu annoté à la main, au moins 50 exemples. Dernière release PyPI en juillet 2024.
- [[RAGChecker]] — **attribue la faute** : il découpe la réponse en claims et vérifie chacun par entailment, ce qui sépare le retriever (claim recall, context precision) du générateur (fidélité, hallucination, sensibilité au bruit). Il exige une réponse de référence par question. Dernière release PyPI en septembre 2024.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
