---
role: brique
nom: OpenRouter
alias: [openrouter, openrouter.ai]
pitch: "Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through."
categorie: llm/passerelle
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[LiteLLM]]", "[[OmniRoute]]"]
complements: []
tags: [llm, llm-gateway, routing, inference]
url_docs: https://openrouter.ai/docs
url_repo: 
---

# OpenRouter

<!-- AUTO:BANDEAU:START -->
> Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Service hébergé qui expose une seule API OpenAI-compatible vers plus de 300 modèles de plus de
60 fournisseurs (OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, xAI). Une clé, une
facture, une URL de base — le routage vers le bon fournisseur est fait pour l'appelant, avec
fallback automatique quand l'un d'eux est indisponible. C'est l'équivalent managé de
[[LiteLLM]] : il n'y a pas de proxy à opérer. Le modèle économique tient en trois lignes :
crédits prépayés, tarifs fournisseurs en pass-through sans marge sur le token, et environ
5,5 % de frais de plateforme sur l'achat de crédits ; un palier gratuit ouvre des modèles à
coût nul, sous limites de débit strictes. Comme sur toute passerelle, la couverture des
fonctions — tools, vision, streaming, JSON — varie selon le modèle qui se trouve derrière
l'API unique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tester et comparer rapidement beaucoup de modèles sans ouvrir un compte chez chaque fournisseur | Exigence de self-host ou de souveraineté : les données transitent par un tiers, dont la politique de rétention et l'éligibilité réglementaire sont à vérifier → [[LiteLLM]] en proxy auto-hébergé |
| Vouloir une seule facture et une seule clé pour un parc hétérogène, sans héberger de passerelle | Contrôle fin voulu — clés virtuelles internes, garde-fous maison, logs chez soi → [[LiteLLM]] |
| Avoir besoin de fallbacks et de bascule de modèle sans coder la logique de routage | Composer des chaînes, du RAG ou des agents : OpenRouter n'orchestre pas → [[LangChain]], [[LlamaIndex]] |
| Projet perso, prototype ou agent : friction minimale pour accéder aux derniers modèles | Servir un modèle sur GPU → [[vLLM]], [[TGI]] |
| | Point de dépendance externe : une panne d'OpenRouter coupe l'accès à tous les modèles — les fallbacks jouent entre fournisseurs, pas si la passerelle elle-même tombe |

## Mise en œuvre

- Installation — rien à installer
- Point d'entrée — `https://openrouter.ai/api/v1`, au format OpenAI, avec une clé unique
- Prérequis — un compte et des crédits prépayés
- Exécution — managé uniquement, serverless
- Coût — prix du fournisseur en pass-through, majoré d'environ 5,5 % de frais sur l'achat de crédits ; palier gratuit à limites de débit strictes ; ces frais sont à intégrer au calcul face à un accès direct au fournisseur

## Écosystème

### Alternatives

- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[OmniRoute]] — Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.

## Ressources

- Documentation — https://openrouter.ai/docs

## Voir aussi

- [[Routing and cascading]] — la notion du dossier
- [[Reliability patterns]] — les fallbacks qu'il applique pour l'appelant
- [[Langflow]], [[Flowise]], [[Dify]] — les builders low-code qui l'appellent en dessous
- [[Comparatif - Frameworks LLM]] — le comparatif du domaine LLM, dont les passerelles sont hors périmètre par construction
