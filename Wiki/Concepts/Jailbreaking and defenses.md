---
galaxie: wiki
type: concept
nom: Jailbreaking and defenses
alias: [jailbreak, jailbreaking, contournement de l'alignement, jailbreaking and defenses, DAN]
categorie: concept/ai
domaines: [ai-eng]
tags: [jailbreak, safety, llm]
---

# Jailbreaking and defenses

## Aperçu

- Faire produire à un LLM un contenu que son **alignement de sécurité** est censé refuser (instructions dangereuses, contenu illicite). Cible le **modèle** et son entraînement, pas la logique de l'app.
- À distinguer de [[Prompt injection]] : le jailbreak attaque la **politique de refus** du modèle ; l'injection détourne les **instructions du développeur**. Un jailbreak peut servir une injection, et inversement.

## Concepts clés

### Techniques d'attaque
- **Roleplay / persona** (« tu es DAN, sans règles »), **hypothétiques** (« dans un roman… »), **obfuscation** (base64, leetspeak, autre langue), **payload splitting** (assembler l'interdit par morceaux), **many-shot jailbreak** (saturer le contexte d'exemples non refusés), **suffixes adversariaux** (Zou et al., 2023 — chaînes optimisées par gradient, souvent transférables d'un modèle à l'autre).

### Pourquoi ça marche
- L'alignement ([[RLHF and DPO]]) couvre une **distribution** de requêtes ; les jailbreaks cherchent les **angles morts** hors distribution. La généralisation du refus est imparfaite, surtout sous formulation inhabituelle.

### Défenses côté modèle
- **Alignement plus robuste** (RLHF/DPO, entraînement adversarial, refus calibrés), **classifieurs de sécurité** en amont/aval (modèles de modération dédiés), **system prompt** durci. Aucune n'est étanche.

### Défenses côté système
- [[Guardrails]] d'entrée (détection de motifs de jailbreak) et de sortie (filtrage du contenu nuisible), **rate-limiting**, journalisation et détection d'abus ([[LLM observability]]). Défense en profondeur.

## Les maths, simplement

- Vu comme une **optimisation adversariale** : l'attaquant cherche une entrée $x$ qui maximise la probabilité d'une réponse interdite sous contrainte de rester plausible. Les suffixes GCG le font littéralement par **descente de gradient** sur les tokens. Côté défense, l'entraînement adversarial minimise ce même objectif — un jeu min-max jamais clos.

## En pratique

- Traiter l'alignement comme **une couche, pas une garantie** : empiler classifieurs + [[Guardrails]] + supervision.
- **Filtrer la sortie** autant que l'entrée : un jailbreak réussi se voit au contenu produit.
- **Red-teaming** continu : les techniques évoluent vite (many-shot, multimodal).
- **Réduire l'enjeu** : un modèle jailbreaké sans outils ni données sensibles fait moins de dégâts (recoupe [[AI security]], moindre privilège).

## Approches voisines & alternatives

- [[AI security]] — le jailbreak dans le panorama des menaces.
- [[Prompt injection]] — attaque les instructions, pas l'alignement ; frontière à garder nette.
- [[Guardrails]] — la défense système concrète.
- [[RLHF and DPO]] — l'alignement que le jailbreak cherche à contourner.
- [[Reasoning models]] — le raisonnement long ouvre de nouvelles surfaces (et défenses) de refus.

## Pour aller plus loin

- Zou et al. (2023) — *Universal and Transferable Adversarial Attacks on Aligned LLMs* (GCG).
- Anthropic (2024) — *Many-shot jailbreaking*.
