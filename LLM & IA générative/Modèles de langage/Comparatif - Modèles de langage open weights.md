---
role: comparatif
nom: Comparatif - Modèles de langage open weights
categorie: llm/modele
tags: [llm, local-llm, self-hosted]
---

# Comparatif - Modèles de langage open weights

> On tranche sur : la licence **du dépôt** et ce qu'elle permet à une ESN (héberger pour un client, redistribuer les poids, finetuner et livrer), le français cité par l'éditeur, le raisonnement et l'appel d'outils, et la VRAM minimale annoncée. Lecture au 2026-09-30, sans score de benchmark.

![[Comparatif - Modèles de langage open weights.base]]

## Ce qui départage

- [[gpt-oss]] — la licence la plus simple : **Apache-2.0** et une politique d'usage d'une phrase, donc héberger, redistribuer, finetuner et livrer sans condition. 120 B (80 Go) ou 20 B (16 Go) en MXFP4 natif, 131 072 tokens, raisonnement à trois niveaux, outils ; mais **texte seul**, **français non cité** par la carte, et poids inchangés depuis 2025-08-26.
- [[Gemma]] — **Apache-2.0 depuis Gemma 4**, sans accès sur demande, là où Gemma 1 à 3 restent sous Gemma Terms : lire la génération. Cinq tailles de E2B à 31 B, image pour tous et audio sur les trois plus petits, 128K à 256K, QAT officiel en 4 bits (31 B : 17,65 Go en GGUF q4_0) et VRAM chiffrée par l'éditeur ; français non nommé (« 35+ langues »).
- [[Qwen]] — le catalogue le plus large et le plus utilisé, mais **trois licences dans une génération** : le 27 B de Qwen3.8 est en Apache-2.0, Flash-Next et le 2,4 T sont sous des licences propres à clause « Model as a Service », qu'un endpoint hébergé pour un client peut déclencher. Petites tailles seulement en Qwen3.5 ; aucune VRAM annoncée ; français non nommé sur les cartes 3.8.
- [[Mistral]] — le **français cité** sur les cartes et des tailles de 3 à 24 B en Apache-2.0 avec GGUF officiels (Ministral 3), mais un **MIT modifié** sur Medium 3.5 et Devstral 2 : aucun droit au-delà de 20 M$ de revenu mensuel de l'entreprise ou de son employeur, dérivés compris. Small 4 (119 B) est en Apache-2.0 mais ne tient pas sur un GPU de 80 Go.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Licences de modèles open weights]] — la notion : ce que les clauses veulent dire, et ce qu'elles ne disent pas.
- [[Comparatif - Exécution & serving LLM]] — le moteur qui sert le modèle, une fois celui-ci choisi.
