---
galaxie: wiki
type: concept
nom: Prompt injection
alias: [injection de prompt, prompt injection, indirect prompt injection, injection indirecte, LLM01]
categorie: concept/ai
domaines: [ai-eng]
tags: [prompt-injection, ai-security, llm]
---

# Prompt injection

## Aperçu

- Attaque où une **entrée non fiable** contient des instructions que le LLM suit à la place (ou en plus) de celles du développeur. Nommée par Simon Willison (2022), classée **LLM01** par l'OWASP — le risque n°1 des apps LLM.
- Cause racine : le modèle ne sépare pas les consignes des données (cf. [[AI security]]). À ne pas confondre avec le [[Jailbreaking and defenses|jailbreak]] (contourner l'alignement du modèle) — même si les deux se combinent souvent.

## Concepts clés

### Directe vs indirecte
- **Directe** : l'utilisateur tape l'instruction malveillante (« ignore les instructions précédentes et… »).
- **Indirecte** (Greshake et al., 2023) : l'instruction est **cachée dans un contenu** que le LLM ingère — page web, PDF, e-mail, ticket, sortie d'outil. L'attaquant n'est pas l'utilisateur. Plus dangereuse : invisible et automatisable à grande échelle.

### Objectifs de l'attaquant
- **Exfiltration** : faire cracher le system prompt (LLM07), des données RAG, des secrets, l'historique — souvent via une URL/image que le modèle est incité à construire (canal de fuite).
- **Abus d'outils** : détourner un agent doté d'outils ([[tool-use]]) pour envoyer un mail, supprimer, payer — l'injection devient **exécution** (lien avec LLM06, agence excessive).
- **Manipulation de sortie** : biaiser une réponse, injecter du HTML/markdown/lien malveillant rendu côté utilisateur.

### Multimodal & obfuscation
- Instructions cachées dans une **image**, de l'audio, du texte blanc ou encodé, des commentaires. Le canal d'entrée n'est pas que le texte visible.

### Pourquoi il n'y a pas de fix parfait
- Tant que consignes et données partagent le même canal, **aucune défense n'est complète**. On **réduit** le risque (cf. [[Guardrails]]), on ne l'élimine pas.

## Les maths, simplement

- Pas de formule, mais un modèle mental : chaque token entrant a une **probabilité non nulle** d'être pris pour une instruction. Sur $n$ sources de contenu non fiables, la probabilité qu'au moins une porte une injection réussie est $1-(1-p)^n$ — elle **croît avec le nombre de sources** (RAG large, multi-outils). D'où : réduire $n$ (périmètre) et $p$ (filtrage), et **borner l'impact** (permissions).

## En pratique

- **Séparer privilèges et données** : ne pas donner à un agent qui traite du contenu non fiable les outils à fort enjeu sans validation humaine.
- **Délimiter** le contenu non fiable (balises, rôle dédié) — atténue, ne résout pas.
- **Filtrer entrée et sortie** ([[Guardrails]]) : détecter les motifs d'injection, neutraliser liens et HTML en sortie.
- **Moindre privilège + human-in-the-loop** sur les actions irréversibles (cf. [[Reliability patterns]]).
- **Red-team** le pipeline [[RAG]] : injection indirecte via un document piégé indexé.

## Approches voisines & alternatives

- [[AI security]] — l'injection est le risque n°1 du panorama (LLM01).
- [[Jailbreaking and defenses]] — viser l'alignement vs détourner les instructions ; souvent combinés.
- [[Guardrails]] — la couche de défense concrète (détection, filtrage).
- [[tool-use]] — les outils transforment une injection en action : surface critique.
- [[mcp-protocol]] — *resources* et outils tiers sont des vecteurs d'injection indirecte.
- [[RAG]] — le contenu récupéré est une entrée non fiable comme une autre.

## Pour aller plus loin

- Simon Willison — série *Prompt injection* (2022 →).
- Greshake et al. (2023) — *Not what you've signed up for* (indirect prompt injection).
- OWASP — *LLM01:2025 Prompt Injection*.
