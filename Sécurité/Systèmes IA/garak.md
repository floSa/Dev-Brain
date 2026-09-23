---
role: brique
nom: garak
alias: [garak, NVIDIA garak, garak llm scanner, Generative AI Red-teaming and Assessment Kit]
pitch: "Scanner de vulnérabilités de LLM par sondes (Apache-2.0, NVIDIA) — une quarantaine de familles de sondes (injection de prompt, jailbreaks, encodages, fuites, génération de code malveillant) lancées contre un modèle local ou distant, avec détecteurs, rapports JSONL et HTML ; la plupart des détecteurs tournent en local, les attaques multi-tours demandent un modèle juge."
categorie: security/ia
famille: cli
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[promptfoo]]"]
complements: ["[[NeMo Guardrails]]"]
tags: [ai-security, prompt-injection, jailbreak, llm-eval]
url_docs: https://reference.garak.ai/
url_repo: https://github.com/NVIDIA/garak
---

# garak

<!-- AUTO:BANDEAU:START -->
> Scanner de vulnérabilités de LLM par sondes (Apache-2.0, NVIDIA) — une quarantaine de familles de sondes (injection de prompt, jailbreaks, encodages, fuites, génération de code malveillant) lancées contre un modèle local ou distant, avec détecteurs, rapports JSONL et HTML ; la plupart des détecteurs tournent en local, les attaques multi-tours demandent un modèle juge.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Scanner de vulnérabilités pour modèles de langage et applications qui en embarquent un : il envoie à la cible des centaines de prompts adverses regroupés en **sondes** (*probes*), lit les réponses avec des **détecteurs** et écrit un rapport. L'analogie avec un scanner de ports est celle du dépôt : on lance une commande contre un point d'accès, on récupère une liste de ce qui a cédé. Trois pièces : le **générateur** (la cible : Ollama, un point d'accès compatible OpenAI, un modèle Hugging Face local, un service REST, `llama.cpp`, LiteLLM, NeMo Guardrails…), la **sonde** (l'attaque) et le **détecteur** (la lecture de la réponse). Famille des sondes au 2026-10-01 : injection de prompt (`promptinject`), jailbreaks (`dan`, `goat`, `tap`, `suffix`), contournements par encodage (`encoding`, `smuggling`, `ansiescape`), injection latente dans un document (`latentinjection`), fuite de données d'entraînement (`leakreplay`) ou du prompt système (`sysprompt_extraction`), génération de code malveillant (`malwaregen`), hallucination de paquets (`packagehallucination`), toxicité, et d'autres.

Relevé le 2026-10-01 : **v0.17.0** (2026-09-09), 9 396 étoiles, dernier push le 2026-09-16, licence **Apache-2.0** (fichier `LICENSE` lu : Leon Derczynski et NVIDIA). Toujours en 0.x : l'API et la configuration peuvent casser d'une version à l'autre (la 0.16.0 d'août 2026 l'a fait).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Éprouver un assistant interne contre les attaques connues **avant** de le livrer, avec une liste de ce qui a cédé | Une garantie : la FAQ du dépôt dit elle-même que les résultats n'ont pas de validité scientifique et que les scores ne se comparent pas d'une sonde à l'autre |
| Cibler un modèle servi en local ([[Ollama]], un serveur compatible OpenAI) sans qu'aucun prompt ne quitte le site, avec les sondes à détecteur local | Des attaques multi-tours pilotées par un adversaire (Crescendo, orchestrations sur mesure) : le framework de Microsoft PyRIT est fait pour cela, sans fiche ici |
| Un outil en ligne de commande qui s'intègre à une CI, avec un rapport JSONL exploitable | Une suite d'évaluation déclarative versionnée avec les tests de qualité du prompt → [[promptfoo]], dont le volet red-teaming vit dans le même YAML |
| Tester aussi l'effet d'un garde-fou : le générateur `guardrails` enveloppe une configuration [[NeMo Guardrails]] | Un poste sans place : la FAQ annonce jusqu'à 9 Go de dépendances sur une installation courante, plus le modèle local visé |

## Mise en œuvre

- Installation — `pip install -U garak` (Python 3.11 à 3.13), de préférence dans un environnement dédié à cause des dépendances lourdes
- Point d'entrée — `python -m garak --model_type ollama --model_name <modèle> --probes promptinject` ; `--list_probes` et `--list_detectors` énumèrent ce qui est disponible ; un point d'accès compatible OpenAI se désigne par son `uri` (valeur par défaut `http://localhost:8000/v1/`, clé par la variable `OpenAICompatible_API_KEY`), un service Ollama par son hôte (`127.0.0.1:11434` par défaut, délai de 30 s)
- Prérequis — **hors ligne** : le code montre un chemin entièrement local (générateurs Ollama, `ggml`, Hugging Face ; sondes à prompts fixes ; détecteurs à mots-clés ou classifieurs téléchargés), mais **aucune page de la documentation lue ne le décrit de bout en bout**. Deux dépendances à connaître : certains détecteurs téléchargent des modèles depuis Hugging Face (deux classifieurs de toxicité `garak-llm/…`) ; les sondes d'attaque pilotée (`goat`, `fitd`, `agent_breaker`) comme les détecteurs du module `judge` appellent un **LLM juge**, par défaut un Llama 3 70B servi par un NIM de NVIDIA (donc une clé et un réseau) — le juge est configurable, mais le pointer sur un modèle local n'a pas été vérifié ici. Les sondes que j'ai lues (`promptinject`, `dan`, `encoding`, `latentinjection`, `leakreplay`, `malwaregen`, `sysprompt_extraction`) déclarent un détecteur qui n'est pas le juge
- Exécution — un processus en ligne de commande, journal `garak.log`, un rapport JSONL par exécution (paramètres, prompts, réponses, scores) et un rapport HTML ordonné par catégories de l'OWASP Top 10 pour les LLM ; aucun format de CI (JUnit, SARIF) relevé
- Coût — gratuit sous Apache-2.0 ; le coût réel est le nombre de requêtes (plusieurs générations par prompt) et la durée : un balayage de toutes les sondes a « pris des heures » selon la FAQ, qui conseille le profil `fast` ou le parallélisme

## Limites à connaître

- **Des résultats indicatifs.** Les sondes sont des prompts connus : un modèle qui les passe n'est pas sûr, il passe les attaques d'hier. Les détecteurs à mots-clés produisent des faux positifs et des faux négatifs ; la FAQ le dit en toutes lettres. Lire les réponses ligne à ligne pour les échecs qui comptent, ne pas se fier au pourcentage.
- **Une cible, pas un système.** garak parle à un modèle ou à un point d'accès. Une attaque qui passe par un document récupéré, un outil ou une base de connaissances ne se teste qu'en écrivant un générateur qui reproduit la chaîne ; les sondes `latentinjection` et `web_injection` couvrent l'injection par contenu, pas toute l'application.
- **Instabilité d'API.** Version 0.x, nom de sondes qui change (la table du README cite encore `gcg` et `xss` que le dépôt ne montre plus). Épingler la version et conserver la configuration avec le rapport.
- **Poids de l'installation.** Jusqu'à 9 Go de dépendances ; prévoir une image dédiée.
- **Aucun chiffre d'efficacité** de l'éditeur n'est repris ici. Version 0.17.0 : ajout d'une correspondance avec l'AI Act européen dans les rapports (notes de version).
- **Adoption** : le dépôt Microsoft PyRIT embarque un scénario qui reprend des sondes de garak (documentation de PyRIT) ; aucune autre intégration n'a été lue à la source.

## Écosystème

### Alternatives

- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic. — le volet red-teaming de promptfoo génère les attaques depuis un service distant par défaut (voir sa fiche) ; garak apporte son propre catalogue de sondes, local, sans génération distante pour les sondes à prompts fixes.

### Compléments

- [[NeMo Guardrails]] — Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée. — garak contient un générateur `NeMoGuardrails` : scanner la cible avec et sans la configuration de rails mesure ce que les rails retiennent.

## Ressources

- Documentation — https://reference.garak.ai/
- Dépôt — https://github.com/NVIDIA/garak
- Dépôt — FAQ (durée des scans, validité des résultats, poids des dépendances) : https://github.com/NVIDIA/garak/blob/main/FAQ.md
- Dépôt — liste des sondes : https://github.com/NVIDIA/garak/tree/main/garak/probes
- Dépôt — notes de version : https://github.com/NVIDIA/garak/releases

## Voir aussi

- [[AI security]] — la notion chapeau : la surface d'attaque qu'un scanner de sondes éprouve
- [[Prompt injection]] — la menace n°1 que les sondes `promptinject` et `latentinjection` rejouent
- [[Jailbreaking and defenses]] — l'attaque contre l'alignement du modèle, que `dan`, `goat` et `tap` rejouent
- [[Systèmes IA]] — le hub du dossier
