---
role: brique
nom: Llama Guard
alias: [llama guard, Llama Guard 3, Llama Guard 4, Meta Llama Guard, Llama Prompt Guard, Prompt Guard 2, LlamaGuard]
pitch: "Classifieur de sûreté de Meta, un modèle de langage qui juge une conversation sûre ou non selon 13 à 14 catégories (licence propre de Meta, pas open source) — Llama Guard 3 en 1B et 8B (texte), Llama Guard 4 en 12B multimodal ; à héberger soi-même (vLLM, Ollama), huit langues dont le français pour le 8B, et une clause d'exclusion pour les sociétés établies dans l'UE que la génération 4 peut déclencher."
categorie: security/ia
famille: modele
licence_type: source-available
maturite: production
langage: Python
alternatives: []
complements: ["[[NeMo Guardrails]]", "[[vLLM]]", "[[Ollama]]"]
tags: [guardrails, safety, ai-security, local-llm]
url_docs: https://huggingface.co/meta-llama/Llama-Guard-3-8B
url_repo: https://github.com/meta-llama/PurpleLlama
---

# Llama Guard

<!-- AUTO:BANDEAU:START -->
> Classifieur de sûreté de Meta, un modèle de langage qui juge une conversation sûre ou non selon 13 à 14 catégories (licence propre de Meta, pas open source) — Llama Guard 3 en 1B et 8B (texte), Llama Guard 4 en 12B multimodal ; à héberger soi-même (vLLM, Ollama), huit langues dont le français pour le 8B, et une clause d'exclusion pour les sociétés établies dans l'UE que la génération 4 peut déclencher.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | source-available | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Famille de **modèles de langage affinés pour classer** : on leur donne une conversation (le message de l'utilisateur, ou sa réponse) et une liste de catégories de risque, ils répondent `safe`, ou `unsafe` suivi des catégories enfreintes. Les catégories suivent la taxonomie MLCommons : crimes violents ou non, crimes sexuels, exploitation d'enfants, diffamation, conseils spécialisés, vie privée, propriété intellectuelle, armes de destruction massive, haine, automutilation, contenu sexuel, élections, et pour les versions à 14 catégories l'abus d'un interpréteur de code. Le modèle ne bloque rien : c'est à l'application (ou à un framework comme [[NeMo Guardrails]]) de lire le verdict et d'agir.

Générations relevées sur Hugging Face le 2026-10-01 : **Llama Guard 3 8B** (2024-07-22, licence Llama 3.1), **Llama Guard 3 1B** (2024-09-20, licence Llama 3.2, 13 catégories), **Llama Guard 3 11B Vision** (2024-09-20, multimodal, licence Llama 3.2) et **Llama Guard 4 12B** (2025-04-23, multimodal natif texte et images, élagué du modèle Llama 4 Scout, licence Llama 4). Aucune version plus récente n'est publiée par Meta sur Hugging Face à cette date. Le compagnon **Llama Prompt Guard 2** (22 M et 86 M de paramètres, 2025-04-28, licence Llama 4) est un petit classifieur d'**injection de prompt et de jailbreak**, un autre travail que celui de Llama Guard : il n'y a pas de catégorie « injection » dans la taxonomie de Llama Guard. Le dépôt de référence des deux est PurpleLlama (4 410 étoiles, dernier push le 2026-09-29), dont la licence est mixte.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un verdict de sûreté **par un modèle**, sans règles à écrire, sur l'entrée comme sur la sortie, hébergé sur le site | La licence est un frein : texte propre de Meta, non reconnu comme open source par l'OSI, avec une politique d'usage qui peut changer (voir *Limites*) |
| Des conversations en français : le 8B annonce huit langues, dont le français | Une société établie dans l'Union européenne qui veut **Llama Guard 4** : la clause d'exclusion des modèles multimodaux de Llama 4 la vise peut-être (voir *Limites*) → viser Llama Guard 3 |
| Un classifieur à brancher sous [[NeMo Guardrails]], dont la documentation le cite pour le rail de sûreté du contenu | Détecter une injection de prompt par un document récupéré : le sujet de Prompt Guard 2, ou de [[garak]] pour le tester |
| Un modèle de 1 B (1,6 Go sous Ollama) pour un poste modeste, de 8 B (4,9 Go) pour de la précision | Une charge sans GPU et à faible latence sur chaque message : chaque verdict est une inférence d'un modèle de 1 à 12 milliards de paramètres |

## Mise en œuvre

- Installation — les poids se récupèrent sur Hugging Face après **acceptation de la licence et approbation manuelle par Meta** (accès « gated » manuel) ; ensuite `vllm serve meta-llama/Llama-Guard-3-8B` (commande donnée sur la fiche du modèle), ou le tag `llama-guard3` d'Ollama (1B de 1,6 Go, 8B de 4,9 Go, 128 K de contexte ; environ 1,1 million de téléchargements, mis à jour il y a un an). Aucun tag Ollama de Llama Guard 4 n'a été vu ; la prise en charge de `llama.cpp` n'a pas été vérifiée
- Point d'entrée — un appel de chat au modèle avec le gabarit de prompt de la fiche, qui accepte une liste de catégories : on peut n'en garder que certaines ; la réponse est lue par du code (`safe` ou `unsafe` plus les codes `S1` à `S14`)
- Prérequis — **hors ligne** une fois les poids copiés : aucun appel sortant n'est requis pour l'inférence. Le téléchargement initial demande un compte Hugging Face approuvé par Meta ; en site fermé, copier les poids et archiver le texte de licence reçu
- Exécution — un serveur d'inférence (vLLM, Ollama) à côté de l'application, ou un appel direct par `transformers` ; un classifieur ne remplace pas le modèle principal, il s'y ajoute
- Coût — gratuit à l'usage sous les conditions de la licence ; le coût réel est le calcul : une inférence de plus par message vérifié, entrée et sortie comprises

## Limites à connaître

- **Licence : ce que la lecture des textes permet à une ESN.** Relevé le 2026-10-01, texte des licences et politiques d'usage de Meta, pas un conseil juridique (voir [[Licences de modèles open weights]]). *Utiliser chez un client* : permis, licence non exclusive, mondiale, sans redevance. *Redistribuer* (livrer les poids ou un produit qui les contient) : copie de la licence, mention « Built with Llama », et un modèle dérivé distribué doit porter « Llama » en début de nom (génération 4) ; la politique d'usage acceptable est incorporée et modifiable par Meta. *Proposer comme service* : permis tant que le fournisseur final reste sous 700 millions d'utilisateurs actifs mensuels (au-delà, licence à demander à Meta). *Embarquer le modèle dans un produit* : mêmes conditions que redistribuer. Ces conditions sont celles d'une licence d'éditeur, pas d'une licence libre : la fiche porte `source-available`.
- **La clause qui exclut l'Union européenne.** La politique d'usage de Llama 4 écrit que, pour « tout modèle multimodal inclus dans Llama 4 », les droits de la section 1(a) de la licence ne sont pas accordés à un individu domicilié dans l'UE ni à une société dont l'établissement principal y est ; les **utilisateurs finaux** d'un produit ou service qui l'intègre sont exemptés. Le texte équivalent existe pour Llama 3.2 (modèles multimodaux), et **n'existe pas** dans la politique de Llama 3.1. Conséquence de lecture : Llama Guard 4 12B est multimodal et sous licence Llama 4, donc une ESN établie dans l'UE n'a **vraisemblablement pas** le droit de le télécharger et de l'exploiter ; Llama Guard 3 11B Vision est dans le même cas pour la 3.2 ; Llama Guard 3 8B (texte, licence 3.1) et 3 1B (texte, licence 3.2) n'en relèvent pas à la lecture. Aucun texte lu ne tranche le cas d'un modèle de sûreté multimodal ; **à faire confirmer par un juriste avant tout choix de Llama Guard 4**.
- **Pas de garantie, pas de chiffre repris.** Un classifieur se trompe dans les deux sens, plus sur les langues peu représentées et sur les formulations obliques. Les chiffres de rappel et de précision publiés par Meta sur ses propres jeux d'évaluation ne sont pas repris ici. Sa catégorie « vie privée » n'est pas un détecteur de données personnelles : pour masquer des noms ou des numéros, c'est [[Presidio]].
- **Hors sujet : l'injection.** Llama Guard juge le contenu d'une conversation, pas sa provenance. Un document qui dit « ignore tes consignes » n'est pas nécessairement « dangereux » au sens des catégories. Détection d'injection : Prompt Guard 2 (classe binaire bénin ou malveillant, contexte de 512 jetons, plusieurs langues annoncées dont le français et l'allemand, licence Llama 4 mais la clause de l'Union ne vise que les modèles multimodaux, ce qu'il n'est pas — le 22 M est le choix d'un processeur sans GPU) ; voir [[Prompt injection]].
- **Pas de nouvelle version depuis avril 2025.** Les alternatives récentes existent et n'ont pas de fiche ici : voir le [[Comparatif - Garde-fous pour LLM]].

## Écosystème

### Alternatives

- *Aucune alternative déclarée : les autres modèles de sûreté n'ont pas de fiche — ShieldGemma (licence Gemma Terms of Use), Qwen3Guard et gpt-oss-safeguard (Apache-2.0 d'après leurs fiches Hugging Face), Granite Guardian, OpenGuardrails. Le [[Comparatif - Garde-fous pour LLM]] les situe, avec leur licence.*

### Compléments

- [[NeMo Guardrails]] — Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée. — Llama Guard 3 figure parmi les modèles du rail de sûreté du contenu de sa documentation.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU. — la commande `vllm serve` figure sur la fiche des modèles Llama Guard 3 et 4.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage. — le tag `llama-guard3` (1B et 8B) est publié dans sa bibliothèque.

## Ressources

- Documentation — fiche du modèle Llama Guard 3 8B : https://huggingface.co/meta-llama/Llama-Guard-3-8B
- Documentation — fiche du modèle Llama Guard 4 12B : https://huggingface.co/meta-llama/Llama-Guard-4-12B
- Documentation — fiche du modèle Llama Prompt Guard 2 86M : https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
- Dépôt — PurpleLlama (Llama Guard, Prompt Guard, CyberSecEval) : https://github.com/meta-llama/PurpleLlama
- Documentation — Llama 4 Community License : https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE
- Documentation — politique d'usage Llama 4 (clause de l'Union européenne) : https://github.com/meta-llama/llama-models/blob/main/models/llama4/USE_POLICY.md
- Documentation — politique d'usage Llama 3.2 : https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md
- Documentation — bibliothèque Ollama, tag llama-guard3 : https://ollama.com/library/llama-guard3

## Voir aussi

- [[Guardrails]] — la notion : la couche de contrôle autour des appels LLM, dont le classifieur de sûreté
- [[Licences de modèles open weights]] — la notion : lire une licence de modèle, seuils, dérivés, géographie
- [[Systèmes IA]] — le hub du dossier
- [[Comparatif - Garde-fous pour LLM]] — Llama Guard et NeMo Guardrails par usage
