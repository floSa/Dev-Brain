---
role: brique
nom: LiteLLM
alias: [litellm, BerriAI-litellm]
pitch: "Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous."
categorie: llm/passerelle
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[OpenRouter]]", "[[OmniRoute]]"]
complements: []
tags: [llm, llm-gateway, inference]
url_docs: https://docs.litellm.ai/
url_repo: https://github.com/BerriAI/litellm
---

# LiteLLM

<!-- AUTO:BANDEAU:START -->
> Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Passerelle LLM, et non un framework d'application : son rôle est l'**abstraction du
fournisseur**. Elle expose un seul format — celui de l'API OpenAI — pour appeler plus de 100
fournisseurs (OpenAI, Anthropic, Google, Bedrock, Azure, Cohere) ainsi que des moteurs locaux
comme [[vLLM]] ou [[Ollama]]. Deux formes coexistent : un **SDK Python**, où un unique
`completion()` remplace tous les SDK, et un **proxy serveur** qui centralise clés virtuelles,
suivi des coûts, load-balancing, fallbacks, garde-fous et journalisation pour une équipe.
C'est la brique de plomberie que les frameworks d'apps LLM appellent en dessous — le format
unique n'efface pas pour autant les différences de fonctions entre fournisseurs (tools,
vision, streaming, JSON), qui se testent un par un.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Découpler le code applicatif du fournisseur : basculer OpenAI, Anthropic ou local sans réécrire les appels | Composer des chaînes, du RAG ou des agents : LiteLLM n'orchestre pas → [[LangChain]], [[LlamaIndex]], [[Haystack]], qui l'appellent en dessous |
| Centraliser l'accès LLM d'une équipe derrière un proxy : quotas, clés virtuelles, suivi des coûts, journalisation | Un seul fournisseur, sans routage ni centralisation : son SDK natif suffit |
| Fiabilité : fallbacks automatiques, retries et load-balancing entre modèles et déploiements | Servir un modèle sur GPU : ce n'est pas un moteur d'inférence → [[vLLM]], [[TGI]] |
| Exposer un endpoint OpenAI-compatible unique devant un parc hétérogène, cloud et local mêlés | Le proxy devient un point de défaillance unique s'il n'est pas rendu redondant, ajoute un léger surcoût de latence, et peut retarder le support d'une nouveauté fournisseur |

## Mise en œuvre

- Installation — `uv add litellm` pour le SDK ; conteneur Docker pour le proxy
- Point d'entrée — `completion()` en SDK Python, ou un endpoint OpenAI-compatible en mode proxy
- Prérequis — Redis et Postgres pour l'état partagé dès que le proxy est répliqué derrière un load-balancer
- Exécution — importé dans l'app, ou proxy auto-hébergé réplicable
- Coût — cœur MIT gratuit ; le dossier `enterprise/` (SSO, intégrations avancées) relève d'une licence commerciale séparée, frontière à vérifier avant de compter sur une fonction ; aucun coût d'inférence ajouté — les tarifs des fournisseurs s'appliquent, LiteLLM en donne la visibilité

## Écosystème

### Alternatives

- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.
- [[OmniRoute]] — Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.

## Ressources

- Documentation — https://docs.litellm.ai/
- Dépôt — https://github.com/BerriAI/litellm

## Voir aussi

- [[Routing and cascading]] — la notion du dossier
- [[Guardrails]] — les garde-fous qu'elle expose au niveau du proxy, avant et après l'appel
- [[DSPy]] — l'appelle en interne, comme les autres frameworks d'apps
- [[Comparatif - Frameworks LLM]] — le comparatif du domaine LLM, dont les passerelles sont hors périmètre par construction
