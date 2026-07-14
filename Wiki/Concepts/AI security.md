---
galaxie: wiki
type: concept
nom: AI security
alias: [sécurité IA, sécurité LLM, LLM security, AI security, OWASP LLM Top 10, sécurité des apps LLM]
categorie: concept/ai
domaines: [ai-eng]
tags: [ai-security, safety, llm]
---

# AI security

## Aperçu

- Panorama des risques de sécurité **propres aux applications LLM** : l'entrée est en langage naturel, la frontière instructions ↔ données est floue, et le modèle est souvent branché sur des outils à effet de bord. La sécurité applicative classique reste nécessaire mais ne suffit pas.
- Page chapeau. Cadre de référence : **OWASP Top 10 for LLM Applications (2025)**. Les attaques précises sont traitées dans [[Prompt injection]] et [[Jailbreaking and defenses]] ; les défenses dans [[Guardrails]].

## Concepts clés

### La faille fondatrice : instructions = données
- Système, message utilisateur et contenu récupéré arrivent dans **le même canal de tokens**. Rien ne distingue structurellement une consigne d'une donnée → toute entrée non fiable peut être interprétée comme instruction. C'est la racine commune de l'injection et du jailbreak.

### OWASP LLM Top 10 (2025)
- Liste de référence. En tête : **LLM01 Prompt injection**. Suivent notamment **LLM02** divulgation d'informations sensibles, **LLM05** mauvais traitement des sorties, **LLM06** **agence excessive** (trop de pouvoir donné aux outils), **LLM07** fuite du system prompt, **LLM08** faiblesses vecteurs/embeddings, **LLM04** empoisonnement données/modèle.

### Surface d'attaque d'une app LLM
- **Entrée** (prompt, documents RAG, sorties d'outils), **modèle** (alignement contournable, hallucination), **sortie** (code/HTML/SQL exécutés en aval), **chaîne d'approvisionnement** (modèles et données tiers), **agence** (outils à effet de bord et leurs permissions).

### CIA appliqué aux LLM
- **Confidentialité** : exfiltration du system prompt, de données RAG, de secrets. **Intégrité** : réponses manipulées, empoisonnement. **Disponibilité** : consommation non bornée (coût, déni de service).

## Les maths, simplement

- Pas de formule : la sécurité se raisonne en **surface d'attaque** et **moindre privilège**. Heuristique de risque d'une action d'agent ≈ probabilité de détournement × pouvoir de l'outil. La première ne tombe pas à zéro (langage naturel) → on **borne le second** (permissions, human-in-the-loop). C'est l'idée derrière LLM06.

## En pratique

- Traiter **toute entrée comme non fiable** — y compris le contenu récupéré (RAG) et les sorties d'outils, pas seulement le prompt utilisateur.
- **Moindre privilège** sur les outils, **human-in-the-loop** sur les actions irréversibles (cf. [[Reliability patterns]], LLM06).
- **Défense en profondeur** : pas de remède unique. Empiler alignement + [[Guardrails]] + permissions + supervision ([[LLM observability]]).
- **Red-teaming** régulier : éprouver l'app avec des prompts adverses avant la prod.
- Ne **jamais exécuter** une sortie LLM (code, SQL, shell, HTML) sans validation (LLM05).

## Approches voisines & alternatives

- [[Prompt injection]] — la menace n°1 (LLM01) : détournement des instructions.
- [[Jailbreaking and defenses]] — contournement de l'alignement, distinct de l'injection.
- [[Guardrails]] — la couche de défense entrée/sortie.
- [[mcp-protocol]] — élargit la surface (serveurs tiers, *resources*) → confiance et permissions.
- [[Reliability patterns]] — moindre privilège, idempotence, bornage des boucles : recoupe la sécurité côté agents.
- [[LLM observability]] — détecter abus et anomalies en production.

## Pour aller plus loin

- OWASP — *Top 10 for LLM Applications 2025*.
- NIST — *AI Risk Management Framework* (AI RMF) et son profil GenAI.
