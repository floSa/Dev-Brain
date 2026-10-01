---
role: brique
nom: NeMo Guardrails
alias: [nemo guardrails, nemoguardrails, NVIDIA NeMo Guardrails, Colang, NeMo Guardrails library]
pitch: "Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée."
categorie: security/ia
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[Presidio]]", "[[Llama Guard]]", "[[garak]]"]
tags: [guardrails, ai-security, safety, llm]
url_docs: https://docs.nvidia.com/nemo/guardrails/
url_repo: https://github.com/NVIDIA-NeMo/Guardrails
---

# NeMo Guardrails

<!-- AUTO:BANDEAU:START -->
> Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python de **garde-fous programmables** pour applications LLM : une couche qui s'intercale entre l'utilisateur et le modèle, et décide quoi laisser passer. Cinq types de **rails** : *entrée* (avant le modèle : refuser, reformuler, masquer), *dialogue* (guider le fil de la conversation), *récupération* (filtrer les passages RAG), *exécution* (contrôler les appels d'outils) et *sortie* (vérifier la réponse). Les rails se déclarent dans un répertoire de configuration : un `config.yml` (modèles, rails actifs, prompts) et, pour les scénarios de dialogue, des fichiers **Colang**, un langage dédié qui décrit des flux (« si l'utilisateur demande X, répondre Y »). Un catalogue de rails prêts à l'emploi couvre la sûreté du contenu, la détection de jailbreak, le contrôle de thème, les données personnelles (via [[Presidio]] ou un modèle GLiNER dédié), la vérification des faits et la sécurité des appels d'outils.

Relevé le 2026-10-01 : **v0.24.1** (2026-09-16), 7 229 étoiles, dernier commit le 2026-09-29, neuf versions en douze mois. Le dépôt est passé de `NVIDIA/NeMo-Guardrails` à `NVIDIA-NeMo/Guardrails` (l'ancienne adresse redirige). Licence **Apache-2.0** : le fichier `LICENSE.md` ne porte que l'en-tête SPDX et la notice, ce que l'API GitHub rend en « NOASSERTION » ; le texte complet est dans `LICENSE-Apache-2.0.txt`. Les **modèles** de garde que NVIDIA publie avec (NemoGuard, Nemotron Safety Guard) sont sous une autre licence : voir *Limites*.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des politiques de conversation **déclaratives** (sujets autorisés, refus, enchaînements) qu'un non-développeur peut relire dans un fichier versionné | Un simple filtre de sortie à schéma : un validateur Pydantic suffit → [[Instructor]] |
| Un serveur de garde-fous compatible OpenAI devant un modèle local (`nemoguardrails server`) | Zéro latence ajoutée : chaque rail sémantique est un appel de modèle de plus |
| Assembler en un seul endroit un classifieur de sûreté ([[Llama Guard]], ShieldGemma, modèles NemoGuard), de la détection de données personnelles ([[Presidio]]) et des règles maison | Une garantie : la documentation du détecteur de jailbreak annonce elle-même qu'il « échoue ouvert » (voir *Limites*) |
| Des documents ou des tours d'agent à contrôler avant l'outil : rails de récupération et d'exécution | Un jailbreak en dehors de l'anglais : les heuristiques de perplexité sont, de l'aveu de la documentation, pour l'anglais seul |

## Mise en œuvre

- Installation — `pip install nemoguardrails` ; l'extra `[server]` ajoute le serveur ; LangChain est devenu optionnel à partir de la 0.22.0. Python : voir PyPI
- Point d'entrée — un répertoire `config/` (`config.yml`, fichiers `.co`), chargé par `RailsConfig.from_path` puis `LLMRails(config).generate(...)` ; ou `nemoguardrails server --config <répertoire>` pour un point d'accès compatible OpenAI avec une interface de chat intégrée
- Prérequis — **un LLM** : les rails dits *self-check* (entrée, sortie, faits) demandent au modèle de l'application de juger, d'après un prompt à écrire ; la documentation dit que la qualité « dépend fortement » du modèle et conseille un modèle dédié au contrôle, déclaré dans `config.yml`. **Hors ligne** : le moteur Ollama est intégré (`localhost:11434/v1`) et tout point d'accès compatible OpenAI sert de modèle, de sorte qu'un site sans internet peut tout garder en interne ; les rails à base de modèle de garde supposent d'héberger ce modèle (voir [[Llama Guard]] pour un exemple)
- Exécution — un processus Python embarqué dans l'application, ou un service HTTP ; un moteur plus récent (*IORails*, depuis la 0.21.0, mars 2026) exécute en parallèle les rails des modèles NemoGuard, sans prise en charge de l'heuristique de jailbreak
- Coût — gratuit sous Apache-2.0 ; le coût réel est la latence et les jetons des appels de contrôle (un prompt complexe, dit la documentation, « ajoute de la latence » ; aucun chiffre publié n'a été lu)

## Limites à connaître

- **Colang : deux versions, une en bêta.** La 1.0 reste le défaut ; la 2.0, prise en charge depuis la 0.8, est encore en bêta d'après la page *Colang* (« jusqu'à ce que Colang termine sa phase bêta »), avec une limite écrite : la bibliothèque de rails n'est pas encore pleinement utilisable depuis Colang 2.0. Les rails prêts à l'emploi passent donc par Colang 1.0 ou par `config.yml`. Un projet qui apprend Colang aujourd'hui choisit entre un langage stable et un langage qui bouge.
- **Le détecteur de jailbreak échoue ouvert.** Connexion perdue, délai dépassé ou erreur : la requête passe, un message est écrit dans le journal, aucune erreur ne remonte à l'appelant. Une panne du détecteur retire la protection sans signal visible : superviser le détecteur, pas seulement l'application. Le mode « dans le processus » des heuristiques est réservé aux essais, non recommandé en production. Chiffres annoncés par l'éditeur dans sa documentation, sur son propre jeu de données et non datés : environ 31 % de jailbreaks détectés pour 7 % de faux positifs au seuil par défaut de l'heuristique de perplexité ; 49 attaques de suffixes adverses (GCG) sur 50 détectées pour 0,04 % de faux positifs avec l'heuristique par préfixe et suffixe.
- **La licence des modèles de garde n'est pas Apache-2.0.** Les cartes Hugging Face (non protégées par accès sur demande, relevé du 2026-10-01) donnent la *NVIDIA Open Model License* pour Nemotron Safety Guard 8B v3 (août 2025) ; le modèle de sûreté du contenu v1 (janvier 2025) est classé « autre » et ajoute la *Llama 3.1 Community License* (« Built with Llama »). Le code du framework est librement utilisable, redistribuable et exploitable en service ; les poids de ces modèles se lisent séparément avant de les livrer à un client ou de les embarquer dans un produit. Les conteneurs NIM de NVIDIA forment une offre distincte, hors périmètre ici.
- **Langues.** La sûreté du contenu v3 annonce neuf langues dont le français (carte du modèle) ; les heuristiques de jailbreak sont prévues pour l'anglais et donnent « nettement plus de faux positifs » ailleurs, code compris.
- **Raisonnement.** Avec un modèle à raisonnement, fixer `max_tokens` (1 024 par défaut) : sinon la sortie sort vide et le rail la bloque.
- **Adoption** : aucun chiffre lu à la source. Signaux : rythme de versions mensuel à bimestriel, périmètre qui s'élargit (agents, outils), éditeur unique. Un bogue du rail Presidio qui bloquait la boucle asynchrone a été corrigé le 2026-09-25 (n° 2400) : le rail PII est exploitable, pas définitivement stabilisé.

## Écosystème

### Alternatives

- *Aucune alternative déclarée : les deux autres frameworks de garde-fous candidats n'ont pas de fiche — Guardrails AI (Apache-2.0) a fermé son Hub de validateurs le 2026-08-25 puis a été racheté par Harvey en septembre 2026 ; LLM Guard (MIT) est archivé depuis le 2026-07-09. Le [[Comparatif - Garde-fous pour LLM]] dit pourquoi, et compare avec [[Llama Guard]] qui n'est pas un framework mais le classifieur qu'on lui branche.*

### Compléments

- [[Presidio]] — Détection et anonymisation de données personnelles dans du texte, des images et des tables (MIT, projet communautaire Data Privacy Stack, ex-Microsoft) — reconnaisseurs par regex et NER (spaCy, Transformers, Stanza), opérateurs de masquage dont un chiffrement réversible, tout en local ; mais anglais seul par défaut et aucun reconnaisseur propre à la France. — c'est le moteur du rail de données personnelles du catalogue.
- [[Llama Guard]] — Classifieur de sûreté de Meta, un modèle de langage qui juge une conversation sûre ou non selon 13 à 14 catégories (licence propre de Meta, pas open source) — Llama Guard 3 en 1B et 8B (texte), Llama Guard 4 en 12B multimodal ; à héberger soi-même (vLLM, Ollama), huit langues dont le français pour le 8B, et une clause d'exclusion pour les sociétés établies dans l'UE que la génération 4 peut déclencher. — cité par la documentation de NeMo Guardrails parmi les modèles du rail de sûreté du contenu.
- [[garak]] — Scanner de vulnérabilités de LLM par sondes (Apache-2.0, NVIDIA) — une quarantaine de familles de sondes (injection de prompt, jailbreaks, encodages, fuites, génération de code malveillant) lancées contre un modèle local ou distant, avec détecteurs, rapports JSONL et HTML ; la plupart des détecteurs tournent en local, les attaques multi-tours demandent un modèle juge. — son générateur `NeMoGuardrails` enveloppe une configuration de rails : de quoi mesurer ce qu'elle retient.

## Ressources

- Documentation — https://docs.nvidia.com/nemo/guardrails/
- Dépôt — https://github.com/NVIDIA-NeMo/Guardrails
- Documentation — catalogue de rails : https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/self-check.md
- Documentation — protection contre le jailbreak (échec ouvert, anglais seul) : https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/jailbreak-protection.md
- Documentation — Colang 1.0 et 2.0 : https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang.md
- Documentation — fiche de modèle, Nemotron Safety Guard 8B v3 : https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3
- Documentation — fiche de modèle, NemoGuard content safety 8B : https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety

## Voir aussi

- [[Guardrails]] — la notion : la couche de contrôle autour des appels LLM, entrée et sortie
- [[Prompt injection]] — la menace que le rail d'entrée atténue sans la supprimer
- [[Données personnelles et anonymisation pour LLM]] — la notion du rail de données personnelles
- [[Systèmes IA]] — le hub du dossier
- [[Comparatif - Garde-fous pour LLM]] — NeMo Guardrails et Llama Guard par usage
