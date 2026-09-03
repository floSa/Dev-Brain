---
role: hub
nom: Systèmes IA
alias: [sécurité des systèmes IA]
pitch: La surface d'attaque d'un système qui embarque un modèle, et les défenses qui tiennent.
domaines: [ai-eng, infra-ops]
tags: [ai-security, prompt-injection, jailbreak, guardrails]
---

# Systèmes IA

> La surface d'attaque d'un système qui embarque un modèle, et les défenses qui tiennent.

## Ce qu'il faut comprendre

- Ces pages sont rangées **sous « Sécurité » et non sous « LLM & IA générative »**, contre l'ordre de l'arbre de décision qui met D1 (« a besoin d'un LLM ») avant D9 (« porte sur la sécurité »). Arbitrage de floSa : la sécurité est une **pratique qui traverse les modèles**, pas un sous-sujet de l'IA générative. [[AI security]] est la page chapeau.
- Le défaut structurel est qu'**un LLM ne distingue pas l'instruction de la donnée**. Tout ce qui entre dans son contexte — document récupéré, page web, sortie d'outil, e-mail — est candidat à être suivi comme un ordre : c'est [[Prompt injection]], et il n'existe pas de correctif, seulement des atténuations.
- **Deux attaques que le vocabulaire courant confond.** L'injection détourne l'application en passant par sa **donnée** ; le [[Jailbreaking and defenses|jailbreak]] contourne l'**alignement** du modèle en passant par la conversation. La première vise votre système, le second vise le modèle du fournisseur — et les défenses ne sont pas les mêmes.
- **Deux familles de défenses, complémentaires et non substituables.** [[Guardrails]] filtre ce qui entre et ce qui sort ; [[Sandboxing de code généré]] part du principe que le code produit est non fiable par construction, et l'isole. Filtrer ne remplace pas isoler : un filtre se contourne, une microVM se compromet sans atteindre l'hôte.
- Le principe qui tient quand le reste échoue est le **moindre pouvoir** : ne pas donner à un agent une action irréversible. Ce que le filtre laisse passer, l'agent ne pourra pas faire — cf. [[Human-in-the-loop]] pour la validation des actions à fort enjeu.

## Choisir

- Comprendre l'ensemble des risques avant de choisir une défense → [[AI security]].
- L'application suit des instructions venues d'un document ou d'une page → [[Prompt injection]].
- Le modèle produit ce qu'il devrait refuser → [[Jailbreaking and defenses]].
- Filtrer les entrées et valider les sorties → [[Guardrails]].
- L'agent exécute du code qu'il a écrit → [[Sandboxing de code généré]].
- Inspecter une cible de l'extérieur, sans modèle en jeu → [[Sécurité]], au niveau du domaine.

<!-- AUTO:START -->
### Notions
- [[AI security]] — domaines : ai-eng
- [[Guardrails]] — domaines : ai-eng
- [[Jailbreaking and defenses]] — domaines : ai-eng
- [[Prompt injection]] — domaines : ai-eng
- [[Sandboxing de code généré]] — domaines : ai-eng
<!-- AUTO:END -->
