---
galaxie: dev
type: service
nom: OpenRouter
alias: [openrouter, openrouter.ai]
pitch: "Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through."
categorie: llm/framework
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: ["[[Dev/Services/LiteLLM|LiteLLM]]"]
remplace_par: []
status: actif
tags: [llm, llm-gateway, routing, inference]
url_docs: https://openrouter.ai/docs
url_repo: 
---

# OpenRouter

## Pourquoi

**Passerelle LLM managée** : un **service hébergé** (SaaS propriétaire) qui expose une **seule API OpenAI-compatible** vers **300+ modèles** de **60+ fournisseurs** (OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, xAI…). Une **clé**, une **facture**, un **base URL** — et OpenRouter gère le routage vers le bon fournisseur, avec **fallbacks** automatiques si un provider est indisponible. Modèle économique : **crédits prépayés**, tarifs fournisseurs en **pass-through** (pas de marge sur le token) plus **~5,5 % de frais** de plateforme sur les crédits ; un palier gratuit donne accès à des modèles à coût nul (rate-limités). C'est l'équivalent **managé** de [[Dev/Services/LiteLLM|LiteLLM]] : pas de proxy à opérer soi-même.

## Quand l'utiliser

- **Tester / comparer** rapidement beaucoup de modèles sans ouvrir un compte chez chaque fournisseur.
- Vouloir **une seule facture** et une seule clé pour un parc hétérogène, sans héberger de gateway.
- Avoir besoin de **fallbacks** et de bascule de modèle sans coder la logique de routage.
- Projets perso, prototypes, agents : friction minimale pour accéder aux derniers modèles.

## Quand NE PAS l'utiliser

- Exigence de **self-host / souveraineté** (données qui ne doivent pas transiter par un tiers) → [[Dev/Services/LiteLLM|LiteLLM]] en proxy auto-hébergé.
- Besoin de **contrôle fin** (clés virtuelles internes, garde-fous maison, logs chez soi) → [[Dev/Services/LiteLLM|LiteLLM]].
- **Composer** chaînes/RAG/agents : OpenRouter n'orchestre pas → frameworks d'apps ([[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]]) qui l'appellent dessous.
- **Servir** un modèle (inférence GPU) → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]].

## Déploiement & coût

- **Managé uniquement** (`hosted: managed`, `serverless`) : rien à déployer, on appelle `https://openrouter.ai/api/v1`.
- **Crédits prépayés** ; le prix par token est celui du fournisseur (pass-through), majoré d'environ **5,5 %** de frais sur l'achat de crédits. Palier gratuit avec modèles à coût nul (rate limits stricts).
- Pas de coût d'infra côté utilisateur, mais **dépendance à un tiers** pour la disponibilité et la confidentialité.

## Pièges

- **Service propriétaire** : les données transitent par OpenRouter — vérifier la politique de rétention et l'éligibilité réglementaire.
- **Point de dépendance externe** : une panne OpenRouter coupe l'accès à tous les modèles (les fallbacks jouent entre fournisseurs, pas si la passerelle elle-même tombe).
- La **couverture des features** (tools, vision, streaming, JSON) varie selon le modèle/fournisseur derrière l'API unique — tester par modèle.
- Frais de plateforme à intégrer au **calcul de coût** par rapport à un accès direct au fournisseur.

## Alternatives

- [[Dev/Services/LiteLLM|LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.

## Liens

- Équivalent **managé** de la passerelle auto-hébergée [[Dev/Services/LiteLLM|LiteLLM]] (même rôle : abstraction multi-fournisseurs au format OpenAI).
- Appelé **en dessous** des frameworks d'apps : [[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]], et des builders [[Dev/Services/Langflow|Langflow]] / [[Dev/Services/Flowise|Flowise]] / [[Dev/Services/Dify|Dify]].
- Concepts : [[Routing and cascading]], [[Reliability patterns]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://openrouter.ai/docs
