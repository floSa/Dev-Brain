---
role: hub
nom: Passerelles
alias: [passerelle LLM, routage LLM]
pitch: Une seule API devant plusieurs fournisseurs — router, replier, plafonner, et ne pas rappeler ce qu'on a déjà demandé.
domaines: [ai-eng]
tags: [llm-gateway, routing, caching]
---

# Passerelles

> Une seule API devant plusieurs fournisseurs — router, replier, plafonner, et ne pas rappeler ce qu'on a déjà demandé.

## Ce qu'il faut comprendre

- Une application qui parle à **un seul fournisseur** est un point de rupture unique : une panne, un changement de tarif ou la dépréciation d'un modèle l'arrête. La passerelle unifie le format d'appel et rend le repli possible — c'est le préalable matériel des [[Reliability patterns]], pas un confort.
- **Deux décisions d'aiguillage, et elles se cumulent** : [[Routing and cascading]]. Le *routing* envoie chaque requête à la bonne ressource (modèle, index, outil) ; le *cascading* enchaîne du moins cher au plus cher et s'arrête dès que la réponse suffit. L'étage léger naturel d'une cascade est un [[Small Language Models|petit modèle]].
- **L'étage zéro d'une cascade est de ne pas appeler du tout** : [[LLM caching]], en clé exacte ou en clé sémantique. À distinguer du [[prompt-caching]], qui est côté fournisseur et met en cache le **calcul du préfixe** — l'un supprime l'appel, l'autre le rend moins cher.
- C'est aussi le point de passage naturel des **plafonds et des garde-fous** : quotas par équipe, budget par clé, journalisation, filtrage. Une règle posée ici vaut pour toutes les applications derrière ; posée dans le code, elle est à repasser partout.

## Choisir

- Self-hébergé, tous fournisseurs, budgets et clés virtuelles → [[LiteLLM]].
- Managé, rien à opérer, catalogue large et facturation unique → [[OpenRouter]].
- La bascule automatique sur quota épuisé comme besoin principal → [[OmniRoute]].
- Servir soi-même le modèle plutôt que le consommer → [[Runtimes]].

<!-- AUTO:START -->
### Notions
- [[LLM caching]] — domaines : ai-eng
- [[Routing and cascading]] — domaines : ai-eng

### Briques
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[OmniRoute]] — Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.
- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.
<!-- AUTO:END -->
