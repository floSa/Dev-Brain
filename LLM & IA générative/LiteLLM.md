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

## Pourquoi

**Passerelle** (gateway) LLM unifiée de **BerriAI**, à ne pas confondre avec un framework d'application : son rôle est l'**abstraction du fournisseur**. Elle expose un seul format — celui de l'API **OpenAI** — pour appeler **100+ fournisseurs** (OpenAI, Anthropic, Google, Bedrock, Azure, Cohere, ainsi que des moteurs locaux comme [[vLLM]] ou [[Ollama]]). Deux formes : un **SDK Python** (un appel `completion()` pour tous), et un **proxy serveur** (AI Gateway) centralisé qui ajoute **clés virtuelles**, **suivi des coûts**, **load-balancing / fallbacks**, **garde-fous** et journalisation pour une équipe. Écrit en **Python**, cœur sous licence **MIT** (le dossier `enterprise/` relève d'une licence commerciale séparée). C'est la **brique de plomberie** que les frameworks d'apps LLM appellent dessous.

## Quand l'utiliser

- **Découpler** le code applicatif du fournisseur : changer OpenAI ↔ Anthropic ↔ local sans réécrire les appels.
- **Centraliser** l'accès LLM d'une équipe derrière un proxy : quotas, clés virtuelles, **suivi des coûts**, journalisation.
- **Fiabilité** : fallbacks automatiques, retries et load-balancing entre modèles/déploiements.
- Donner un endpoint **OpenAI-compatible** unique devant un parc hétérogène (cloud + [[vLLM]]/[[Ollama]] locaux).

## Quand NE PAS l'utiliser

- Besoin de **composer des chaînes, du RAG ou des agents** : LiteLLM ne fait pas l'orchestration → [[LangChain]], [[LlamaIndex]], [[Haystack]] (qui peuvent l'utiliser dessous).
- Un seul fournisseur, sans besoin de routage ni de centralisation : le SDK natif du fournisseur suffit.
- **Servir** un modèle (inférence GPU) : ce n'est pas un moteur de serving → [[vLLM]], [[TGI]].

## Déploiement & coût

- Cœur open-source (MIT), gratuit. **SDK** : importé dans l'app (`hosted: self`). **Proxy** : conteneur auto-hébergé, réplicable derrière un load-balancer (état partagé via Redis/Postgres) — d'où `hosted: both`.
- Fonctions **entreprise** (SSO, intégrations avancées) sous **licence commerciale** séparée (`enterprise/`).
- N'ajoute pas de coût d'inférence : il **route** vers les fournisseurs, dont les tarifs s'appliquent ; sa valeur est la visibilité/maîtrise de ces coûts.

## Pièges

- Surcouche = **point de défaillance unique** s'il est mal dimensionné : le proxy doit être rendu redondant.
- La **couverture des features** varie par fournisseur (tools, vision, streaming, JSON) : le format unique n'efface pas toutes les différences — tester par provider.
- **Léger surcoût de latence** et décalage possible quand un fournisseur publie une nouveauté avant son support dans LiteLLM.
- Bien séparer ce qui est **MIT** de ce qui relève de la **licence enterprise**.

## Alternatives

- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.

<!-- Autre passerelle, mais managée : OpenRouter. Côté frameworks d'apps, pas d'alternative directe — ils s'appuient plutôt sur LiteLLM. -->
- Les frameworks d'applications ([[LangChain]], [[LlamaIndex]], [[Haystack]], [[DSPy]]) offrent leur propre abstraction de modèles, mais résolvent l'orchestration, pas la passerelle multi-fournisseurs centralisée.
- [[OmniRoute]] — Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.

## Liens

- Équivalent **managé** (SaaS) de la même fonction : [[OpenRouter]].
- Utilisé **en dessous** des frameworks d'apps : [[LangChain]], [[LlamaIndex]], [[Haystack]], [[DSPy]] (qui appelle LiteLLM en interne).
- Route aussi vers les moteurs locaux à endpoint OpenAI : [[vLLM]], [[Ollama]], [[TGI]].
- Expose des [[Guardrails|garde-fous]] (modération, PII) au niveau du proxy, avant/après l'appel.
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.litellm.ai/
