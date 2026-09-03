---
role: brique
nom: OmniRoute
alias: [omniroute]
pitch: "Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production."
categorie: llm/passerelle
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: ["[[LiteLLM]]", "[[OpenRouter]]"]
complements: []
tags: [llm, llm-gateway, routing, reliability, context-engineering]
url_docs: https://github.com/diegosouzapw/OmniRoute/wiki
url_repo: https://github.com/diegosouzapw/OmniRoute
---

# OmniRoute

## Pourquoi

**Passerelle LLM auto-hébergée**, écrite en **TypeScript** (Next.js), sous licence **MIT**. Même rôle que [[LiteLLM]] : une API unique devant un parc de fournisseurs. Deux différences de conception. D'abord le **routage par combos** : une liste ordonnée de couples (fournisseur, modèle), avec fallback au niveau du compte puis du modèle, et un moteur de sélection automatique qui score sur neuf facteurs (coût, latence p95, taux de succès, marge de quota, proximité de lockout, état du circuit breaker, échecs récents, disponibilité du modèle, affinité de tags). Le **fallback conscient des quotas** est le cœur du projet. Ensuite la **compression de requêtes**, appliquée avant la traduction vers le fournisseur : règles lexicales (« Caveman » : packs de langue, suppression d'articles et de mots vides), filtres de sortie d'outils (« RTK » : troncature avec récupération du brut), pipelines empilables par combo, et moteurs de type LLMLingua-2. **Ce n'est pas du cache** ([[LLM caching]] réutilise un calcul identique) : c'est une **réécriture destructive du prompt**, donc du [[Context engineering]] avec perte assumée.

## Quand l'utiliser

- Jongler avec **beaucoup de comptes et de quotas gratuits** hétérogènes : c'est le seul cas où le fallback quota-aware apporte plus qu'un fallback classique.
- Poste de travail ou machine unique : distribution npm, Docker multi-arch, Electron, Android/Termux, PWA.
- Explorer les **pipelines de compression de prompt** avec une UI, avant d'en écrire un soi-même.
- Contexte personnel, expérimental, sans exigence de conformité.

## Quand NE PAS l'utiliser

- **En contexte professionnel** : le wiki documente des fournisseurs de type « cookie web » (ChatGPT Web, Gemini Web) et « OAuth / abonnement » (Claude Code, GitHub Copilot) détournés vers une API, avec une promesse d'« IA gratuite illimitée ». C'est structurellement contraire aux CGU de ces fournisseurs — le risque contractuel est réel et rédhibitoire.
- Passerelle **d'équipe** à opérer (clés virtuelles, redondance, état partagé) → [[LiteLLM]], dont le proxy se réplique.
- Ne rien héberger du tout → [[OpenRouter]].
- **Servir** un modèle : OmniRoute ne fait aucune inférence, il route.
- Prompts où la **fidélité littérale** compte (juridique, code, extraction) : la compression par règles altère le texte.

## Déploiement & coût

- **Mono-nœud**, Next.js sur `PORT=20128`, persistance **SQLite** (`~/.omniroute/storage.sqlite` : fournisseurs, clés, combos, pricing, journaux). Pas d'état partagé, donc pas de réplication.
- Une synchronisation cloud existe côté configuration (`NEXT_PUBLIC_CLOUD_URL`), mais le wiki place l'implémentation serveur **hors périmètre** : **aucune offre managée**, d'où `hosted: self`.
- Gratuit (MIT) ; les tarifs des fournisseurs appelés s'appliquent normalement.
- Créé le 2026-02-13, commits quotidiens, version v3.8.51 à cadence de release rapide.

## Pièges

- **Chiffres auto-déclarés.** Le gain de tokens annoncé (« 15 à 95 %, moyenne 89,2 % ») vient de l'éditeur, sans protocole publié ni mesure de l'impact sur la qualité des réponses. À mesurer soi-même sur ses propres prompts.
- **Nombre de fournisseurs contradictoire selon la source** : 352 dans la description du dépôt, 350 dans le README indexé, 226 dans le wiki Providers-Guide. Retenir l'ordre de grandeur (quelques centaines), pas le chiffre.
- **Six mois d'existence**, environ 200 issues ouvertes, aucun audit tiers ni adoption industrielle documentée — d'où `maturite: beta`.
- Dépôt d'environ **475 Mo** pour une passerelle TypeScript : assets ou binaires vendorés, à inspecter avant de faire confiance à la chaîne de build.
- La page d'accueil annoncée (`omniroute.online`) n'était **pas joignable** au moment de la vérification ; la seule documentation est le wiki GitHub.
- Toute la configuration (clés API comprises) vit dans **un fichier SQLite local** non chiffré par défaut.

## Alternatives

- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.

## Liens

- Voisin sans être une alternative : [[Helicone]] (observabilité LLM en mode proxy, avec cache et rate-limiting — l'angle est la mesure, pas le routage).
- Concepts : [[Routing and cascading]], [[Reliability patterns]] (circuit breaker, fallback), [[Context engineering]] (compression de prompt), [[LLM caching]] (en contraste : réutilisation, pas réécriture).
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Wiki : https://github.com/diegosouzapw/OmniRoute/wiki
