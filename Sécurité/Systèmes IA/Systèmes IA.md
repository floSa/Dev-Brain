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
- **Une troisième pratique, qui ne défend rien : éprouver.** Un scanner d'attaques ([[garak]], le volet red-teaming de [[promptfoo]]) rejoue les attaques connues contre le système et dit lesquelles passent. Il mesure, il ne protège pas, et un score élevé ne prouve que la résistance aux attaques d'hier. À côté, la **donnée personnelle** est un risque de nature différente : elle se traite avant l'appel au modèle ([[Presidio]], [[Données personnelles et anonymisation pour LLM]]), pas à la sortie.
- Le principe qui tient quand le reste échoue est le **moindre pouvoir** : ne pas donner à un agent une action irréversible. Ce que le filtre laisse passer, l'agent ne pourra pas faire — cf. [[Human-in-the-loop]] pour la validation des actions à fort enjeu.

## Choisir

- Comprendre l'ensemble des risques avant de choisir une défense → [[AI security]].
- L'application suit des instructions venues d'un document ou d'une page → [[Prompt injection]].
- Le modèle produit ce qu'il devrait refuser → [[Jailbreaking and defenses]].
- Filtrer les entrées et valider les sorties → [[Guardrails]].
- Appliquer une politique déclarative autour du modèle (sujets, refus, rails d'entrée et de sortie) → [[NeMo Guardrails]] ; héberger un classifieur de sûreté → [[Llama Guard]] ; choisir entre les deux → [[Comparatif - Garde-fous pour LLM]].
- Masquer les noms, courriels et numéros avant d'appeler un modèle → [[Presidio]], et la notion [[Données personnelles et anonymisation pour LLM]] pour ce que le masquage ne garantit pas.
- Éprouver un assistant contre les attaques connues avant de le livrer → [[garak]], ou [[promptfoo]] si le red-teaming doit vivre dans la suite d'évaluation.
- L'agent exécute du code qu'il a écrit → [[Sandboxing de code généré]].
- Inspecter une cible de l'extérieur, sans modèle en jeu → [[Sécurité]], au niveau du domaine.

<!-- AUTO:START -->
### Notions
- [[AI security]] — domaines : ai-eng
- [[Données personnelles et anonymisation pour LLM]] — domaines : ai-eng, infra-ops
- [[Guardrails]] — domaines : ai-eng
- [[Jailbreaking and defenses]] — domaines : ai-eng
- [[Prompt injection]] — domaines : ai-eng
- [[Sandboxing de code généré]] — domaines : ai-eng

### Briques
- [[garak]] — Scanner de vulnérabilités de LLM par sondes (Apache-2.0, NVIDIA) — une quarantaine de familles de sondes (injection de prompt, jailbreaks, encodages, fuites, génération de code malveillant) lancées contre un modèle local ou distant, avec détecteurs, rapports JSONL et HTML ; la plupart des détecteurs tournent en local, les attaques multi-tours demandent un modèle juge.
- [[Llama Guard]] — Classifieur de sûreté de Meta, un modèle de langage qui juge une conversation sûre ou non selon 13 à 14 catégories (licence propre de Meta, pas open source) — Llama Guard 3 en 1B et 8B (texte), Llama Guard 4 en 12B multimodal ; à héberger soi-même (vLLM, Ollama), huit langues dont le français pour le 8B, et une clause d'exclusion pour les sociétés établies dans l'UE que la génération 4 peut déclencher.
- [[NeMo Guardrails]] — Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée.
- [[Presidio]] — Détection et anonymisation de données personnelles dans du texte, des images et des tables (MIT, projet communautaire Data Privacy Stack, ex-Microsoft) — reconnaisseurs par regex et NER (spaCy, Transformers, Stanza), opérateurs de masquage dont un chiffrement réversible, tout en local ; mais anglais seul par défaut et aucun reconnaisseur propre à la France.

### Comparatifs
- [[Comparatif - Garde-fous pour LLM]]
<!-- AUTO:END -->
