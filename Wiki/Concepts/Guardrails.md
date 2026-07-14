---
galaxie: wiki
type: concept
nom: Guardrails
alias: [garde-fous, guardrails, garde-fous LLM, garde-fous d'entrée/sortie]
categorie: concept/ai
domaines: [ai-eng]
tags: [guardrails, safety, llm]
---

# Guardrails

## Aperçu

- **Garde-fous** : couche de contrôle **déterministe** autour des appels LLM qui valide, filtre ou bloque entrées et sorties. Le modèle reste probabiliste ; les guardrails ajoutent des vérifications programmables à la frontière.
- Réponse pratique aux menaces de [[AI security]] : ni l'alignement ni le prompt ne suffisent → on encadre. Défense en profondeur, pas garantie.

## Concepts clés

### Garde-fous d'entrée
- Avant le modèle : détection de [[Prompt injection|prompt injection]] et de [[Jailbreaking and defenses|jailbreak]], filtrage PII, hors-sujet, longueur/coût, modération du contenu utilisateur.

### Garde-fous de sortie
- Après le modèle : **validation de schéma** (la sortie est-elle un JSON conforme ? → [[Structured outputs]]), filtrage toxicité/PII, vérification d'**ancrage** (groundedness vs hallucination), neutralisation des liens/HTML, blocage des secrets exfiltrés.

### Mécanismes
- **Règles** (regex, listes, schémas), **classifieurs ML** (toxicité, injection, NSFW), **[[LLM-as-judge]]** comme garde-fou sémantique, **boucle de repair** (réinjecter l'erreur pour correction, cf. [[Reliability patterns]]).

### Action en cas de violation
- **Bloquer**, **masquer/caviarder**, **réécrire**, **demander une revue humaine**, ou **dégrader** (réponse de secours). Toujours **journaliser** ([[LLM observability]]).

## Les maths, simplement

- Un guardrail est un **classifieur** : compromis précision/rappel. Trop strict → faux positifs (UX cassée) ; trop laxiste → faux négatifs (attaque qui passe). On règle le seuil selon le **coût asymétrique** : sur une action irréversible, privilégier le rappel quitte à bloquer à tort.

## En pratique

- **Empiler** entrée + sortie : aucun garde-fou seul ne suffit (défense en profondeur).
- Côté frameworks : la **validation de sortie structurée** est le garde-fou le plus courant — [[Dev/Services/Instructor|Instructor]] (objets Pydantic validés + retry), [[Dev/Services/PydanticAI|PydanticAI]]. Au niveau passerelle, [[Dev/Services/LiteLLM|LiteLLM]] expose des **guardrails** (modération, PII) avant/après l'appel.
- Garder les guardrails **déterministes et rapides** quand c'est possible (regex/schéma) ; réserver classifieurs et LLM-judge aux cas sémantiques (coût + latence).
- **Mesurer** taux de blocage et faux positifs en prod ([[LLM observability]]) — un garde-fou non observé dérive.
- Piège : tout miser sur les guardrails en oubliant le **moindre privilège** des outils ([[AI security]]) — un garde-fou contourné ne doit pas donner les clés.

## Approches voisines & alternatives

- [[AI security]] — les guardrails sont une couche de la défense en profondeur.
- [[Prompt injection]] / [[Jailbreaking and defenses]] — les menaces que les garde-fous d'entrée visent.
- [[Structured outputs]] — la validation de schéma **est** un garde-fou de sortie.
- [[Reliability patterns]] — validation + repair, dégradation gracieuse : même boîte à outils.
- [[LLM-as-judge]] — sert de garde-fou sémantique (notation de conformité).
- [[LLM observability]] — mesurer l'efficacité et la dérive des garde-fous.
- [[Human-in-the-loop]] — au lieu de bloquer, router une action douteuse vers une revue humaine.

## Pour aller plus loin

- OWASP — *LLM01 / LLM05* : filtrage entrée/sortie comme mitigation.
- Docs **NeMo Guardrails** (NVIDIA) et **Guardrails AI** — frameworks dédiés (pas encore dans le brain).
