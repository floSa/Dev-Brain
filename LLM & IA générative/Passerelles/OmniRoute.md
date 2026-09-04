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

<!-- AUTO:BANDEAU:START -->
> Passerelle LLM auto-hébergée (TypeScript/Next.js, MIT) — agrège des centaines de fournisseurs derrière une API unique, avec combos ordonnés, fallback conscient des quotas et compression destructive des prompts ; mono-nœud sur SQLite, projet jeune sans recul de production.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-source | self-hébergé · mono-nœud | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Même rôle que [[LiteLLM]] — une API unique devant un parc de fournisseurs — avec deux partis
pris propres. Le **routage par combos** d'abord : une liste ordonnée de couples (fournisseur,
modèle), avec fallback au niveau du compte puis du modèle, et un moteur de sélection qui score
sur neuf facteurs (coût, latence p95, taux de succès, marge de quota, proximité de lockout,
état du circuit breaker, échecs récents, disponibilité du modèle, affinité de tags) ; le
fallback conscient des quotas est le cœur du projet. La **compression de requêtes** ensuite,
appliquée avant la traduction vers le fournisseur : règles lexicales (« Caveman »), filtres de
sortie d'outils (« RTK »), pipelines empilables par combo, moteurs de type LLMLingua-2. Ce
n'est pas du cache — [[LLM caching]] réutilise un calcul identique — mais une réécriture
destructive du prompt, donc du [[Context engineering]] avec perte assumée. Le nombre de
fournisseurs annoncé varie de 226 à 352 selon la source : retenir l'ordre de grandeur, pas le
chiffre. Créé le 2026-02-13, commits quotidiens, cadence de release rapide (v3.8.51).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Jongler avec beaucoup de comptes et de quotas gratuits hétérogènes — le seul cas où le fallback conscient des quotas apporte plus qu'un fallback classique | En contexte professionnel : le wiki documente des fournisseurs de type « cookie web » (ChatGPT Web, Gemini Web) et « OAuth / abonnement » (Claude Code, GitHub Copilot) détournés vers une API, avec une promesse d'« IA gratuite illimitée » — structurellement contraire aux CGU de ces fournisseurs, risque contractuel réel et rédhibitoire |
| Poste de travail ou machine unique : distribution npm, Docker multi-arch, Electron, Android/Termux, PWA | Passerelle d'équipe à opérer — clés virtuelles, redondance, état partagé → [[LiteLLM]], dont le proxy se réplique |
| Explorer les pipelines de compression de prompt avec une UI, avant d'en écrire un soi-même | Ne rien héberger du tout → [[OpenRouter]] |
| Contexte personnel, expérimental, sans exigence de conformité | Servir un modèle : OmniRoute ne fait aucune inférence, il route |
| | Prompts où la fidélité littérale compte — juridique, code, extraction : la compression par règles altère le texte |
| | Six mois d'existence, environ 200 issues ouvertes, aucun audit tiers ni adoption industrielle documentée ; le gain de tokens annoncé (« 15 à 95 %, moyenne 89,2 % ») est auto-déclaré, sans protocole publié ni mesure de l'impact sur la qualité |
| | Clés API et configuration dans un SQLite local non chiffré par défaut ; dépôt d'environ 475 Mo pour une passerelle TypeScript, à inspecter avant de faire confiance à la chaîne de build |

## Mise en œuvre

- Installation — npm, image Docker multi-arch, Electron, Android/Termux ou PWA
- Point d'entrée — application Next.js sur `PORT=20128`, exposant une API unique devant les fournisseurs
- Prérequis — SQLite local (`~/.omniroute/storage.sqlite`) pour fournisseurs, clés, combos, tarifs et journaux ; aucun état partagé, donc aucune réplication possible
- Exécution — mono-nœud auto-hébergé ; une synchronisation cloud existe côté configuration (`NEXT_PUBLIC_CLOUD_URL`), mais son implémentation serveur est hors périmètre — aucune offre managée
- Coût — gratuit sous MIT ; les tarifs des fournisseurs appelés s'appliquent normalement

## Écosystème

### Alternatives

- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[OpenRouter]] — Passerelle LLM managée (SaaS propriétaire) — une seule API OpenAI-compatible et une seule facture vers 300+ modèles de 60+ fournisseurs, avec routage et fallbacks automatiques ; ~5,5 % de frais sur les crédits, tarifs fournisseurs en pass-through.

## Ressources

- Documentation — https://github.com/diegosouzapw/OmniRoute/wiki — le wiki GitHub est la seule documentation : la page d'accueil annoncée (`omniroute.online`) n'était pas joignable à la vérification
- Dépôt — https://github.com/diegosouzapw/OmniRoute

## Voir aussi

- [[Routing and cascading]] — la notion du dossier
- [[Reliability patterns]] — le circuit breaker et le fallback qu'il implémente
- [[Helicone]] — voisin sans être une alternative : proxy lui aussi, mais l'angle est la mesure, pas le routage
- [[Comparatif - Frameworks LLM]] — le comparatif du domaine LLM, dont les passerelles sont hors périmètre par construction
