---
role: comparatif
nom: Comparatif - Garde-fous pour LLM
categorie: security/ia
tags: [guardrails]
---

# Comparatif - Garde-fous pour LLM

> On tranche sur : la nature de l'outil (framework de politiques ou modèle de classification), ce que chaque verdict coûte (un appel de modèle de plus), la détection d'injection, les langues, le fonctionnement hors ligne, la licence de ce qu'on télécharge en plus du code (les poids), et l'état de maintenance — plus, pour les candidats sans fiche, ce qui s'est passé depuis leur lancement.

![[Comparatif - Garde-fous pour LLM.base]]

## Ce qui départage

- [[NeMo Guardrails]] — le framework : cinq types de rails (entrée, dialogue, récupération, exécution, sortie) déclarés en YAML et en Colang, avec un catalogue de rails prêts à l'emploi (sûreté, jailbreak, thème, données personnelles, faits). Il décide *quoi faire* d'un verdict : refuser, reformuler, masquer, router. Le prix : chaque contrôle sémantique est un appel de modèle de plus, le détecteur de jailbreak échoue ouvert, Colang 2.0 est encore en bêta, et les modèles de garde de NVIDIA ne sont pas sous la licence Apache-2.0 du code.

Un framework et un classifieur de sûreté ne se remplacent pas : ils se **superposent**. NeMo Guardrails sait appeler un classifieur (Llama Guard de Meta, décrit plus bas en texte simple) pour son rail de sûreté du contenu ; un classifieur seul laisse à l'application le soin de lire le verdict. La question utile n'est pas « lequel » mais « le classifieur de sûreté, c'est quel modèle, sous quelle licence ». [[Presidio]], dans le même dossier, répond à une question voisine (masquer les données personnelles avant l'appel) et se branche sous les deux ; [[garak]] teste ce que l'un ou l'autre retient.

**Critère par critère**

**Nature.** [[NeMo Guardrails]] : bibliothèque Python et serveur compatible OpenAI, qui orchestre et décrit une politique. Un classifieur de sûreté, lui, n'est que des poids qui jugent : il rend un verdict, et sans cadre autour il n'a ni seuil, ni action, ni journal.

**Entrée et sortie.** [[NeMo Guardrails]] : les deux, plus le dialogue, la récupération (passages RAG) et l'exécution (appels d'outils).

**Injection de prompt et jailbreak.** [[NeMo Guardrails]] : un rail de jailbreak à heuristiques de perplexité ou à classifieur sur plongements, **pour l'anglais**, qui échoue ouvert si le détecteur ne répond pas ; plus un self-check d'entrée par le LLM de l'application. Un classifieur de sûreté comme Llama Guard n'a **aucune** catégorie « injection » ; un modèle voisin, Prompt Guard 2, est conçu pour cela. Dans tous les cas, voir [[Prompt injection]] : aucun filtre ne ferme la faille.

**Politique déclarative.** [[NeMo Guardrails]] : oui, versionnée avec l'application (`config.yml`, fichiers Colang).

**Modèle requis, ou règles.** [[NeMo Guardrails]] : un LLM pour les rails de type self-check (le modèle principal, ou un modèle de contrôle séparé), un modèle de garde pour les rails de sûreté ; des règles et du code Python pour le reste. Des règles déterministes (expressions régulières, listes) ne sont pas le cœur de métier de ce framework.

**Langues.** [[NeMo Guardrails]] : celles du modèle choisi ; sûreté du contenu v3 annoncée en neuf langues dont le français (carte du modèle) ; heuristiques de jailbreak en anglais.

**Latence ajoutée.** [[NeMo Guardrails]] : un appel de modèle par rail sémantique, aucun chiffre publié lu à la source. Mesurer sur le matériel cible, avant de promettre un temps de réponse.

**Hors ligne.** [[NeMo Guardrails]] : oui, avec Ollama ou tout point d'accès compatible OpenAI ; le moteur de rails NemoGuard suppose d'héberger les modèles de NVIDIA.

**Licence.** [[NeMo Guardrails]] : Apache-2.0 pour le code ; *NVIDIA Open Model License* pour Nemotron Safety Guard, et, pour le modèle de sûreté v1, la *Llama 3.1 Community License* en plus.

**Maintenance.** [[NeMo Guardrails]] : v0.24.1 (2026-09-16), neuf versions en douze mois.

**Pas de fiche ici**, faute d'avoir passé le critère « éprouvé et utilisable en on-prem » (le plafond était de quatre briques) :

- **Guardrails AI** — Apache-2.0, v0.11.0 (2026-08-14), environ 7 500 étoiles : un cadre de validateurs d'entrée et de sortie, fort pour la sortie structurée. Écarté : la fermeture annoncée de son **Hub de validateurs** et de l'inférence hébergée (échéance ferme du 2026-08-25, `guardrails hub install` supprimé, validateurs désormais installés par `pip`), puis l'annonce de son rachat par **Harvey** en septembre 2026 (billet « Guardrails AI Joins Harvey ») qui ne dit rien du sort du projet ouvert. Le serveur `guardrails-api` est sous une licence reprise de l'Elastic License (en-tête lu), donc pas open source. À réévaluer quand le projet aura clarifié sa suite.
- **LLM Guard** (Protect AI) — MIT, 3 200 étoiles : une boîte à scanners d'entrée et de sortie (anonymisation, injection, toxicité, secrets). Écarté : le dépôt est **archivé** depuis le 2026-07-09 et son README déclare les modèles Hugging Face associés « plus maintenus ». Protect AI a été racheté en 2025 par Palo Alto Networks (source secondaire) ; le README ne cite pas ce rachat. Son modèle de détection d'injection ne couvre que l'anglais.
- **Llama Guard** (Meta, 1 à 12 milliards de paramètres) — un modèle qui répond « sûr » ou « non sûr » selon des catégories, sans bloquer ni dialoguer : à brancher dans un framework ou dans le code de l'application, qui lit le verdict. Pas de fiche : c'est un modèle, et le brain ne décrit que des outils. Pour mémoire : licence de Meta (Llama 3.1, 3.2 ou 4 selon la génération), usage commercial permis sous conditions (mention « Built with Llama », seuil de 700 millions d'utilisateurs) et clause d'exclusion de l'Union européenne pour les modèles multimodaux des générations 3.2 et 4 ; huit langues dont le français pour Llama Guard 3 8B ; poids à télécharger avec un compte Hugging Face approuvé à la main par Meta ; dernière génération publiée le 2025-04-23.
- **Llama Prompt Guard 2** (Meta, 22 M et 86 M) — détecteur d'injection et de jailbreak, licence Llama 4 ; même statut que Llama Guard.
- **ShieldGemma** (Google, 2B, 9B et 27B, juillet 2024) — classifieur de sûreté sous les *Gemma Terms of Use*, qui renvoient à une politique d'usage interdit et réservent à Google le droit de restreindre l'usage ; accès gated manuel. Anglais.
- **Qwen3Guard** (Alibaba, 0.6B, 4B et 8B, septembre 2025) — classifieur sous Apache-2.0 (métadonnées Hugging Face), 119 langues annoncées, trois niveaux de gravité ; jeune, 513 étoiles sur le dépôt. Premier candidat à une fiche si un site veut un classifieur de sûreté sous licence libre.
- **gpt-oss-safeguard** (OpenAI, 20B et 120B) — Apache-2.0, la politique s'écrit en clair et se fournit à l'inférence, raisonnement visible ; dérivé de gpt-oss. Même statut que Qwen3Guard.
- **IBM Granite Guardian** (Apache-2.0, 180 étoiles, version 4.1 8B du 2026-04-16) — anglais seulement.
- **OpenGuardrails** — Apache-2.0, jeune (51 étoiles sur le dépôt) : non évalué en détail.
- **Lakera Guard** — service propriétaire, racheté par Check Point (annonce du 2025-09-16) : exclu par le critère open source. **Rebuff** — dépôt archivé, dernier push en août 2024. **Purple Llama / CyberSecEval** — jeu de mesures de sécurité de Meta (licence MIT pour CyberSecEval), c'est de l'évaluation, pas un garde-fou. **Giskard** — Apache-2.0, 5 800 étoiles, v3.0.0 du 2026-08-26 : réécriture pour tester des agents ; outil d'évaluation, voisin de [[garak]] et de [[promptfoo]], non un garde-fou.

Un garde-fou ne dispense pas de [[Sandboxing de code généré]] ni du moindre pouvoir ([[AI security]]) : filtrer ne remplace pas isoler.

**Dans la vue « Toute la catégorie », deux briques d'une autre famille** : [[OpenShell]] et [[sandbox-runtime]]. Ce ne sont pas des filtres d'entrée et de sortie : ce sont des runtimes qui **appliquent hors du modèle** une politique sur les fichiers, les appels système et le réseau d'un agent. Ils se comparent entre eux et avec les microVM dans le [[Comparatif - Isolation d'exécution d'un agent]], sans classement ; le principe qui les distingue des garde-fous de cette page est dans [[Garde-fous hors modèle]].

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Systèmes IA]] — le hub du dossier.
- [[Guardrails]] — la notion : la couche de contrôle autour des appels LLM, entrée et sortie.
