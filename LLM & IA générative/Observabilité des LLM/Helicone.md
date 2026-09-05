---
role: brique
nom: Helicone
alias: [helicone]
pitch: "Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode."
categorie: llm/observabilite
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[Langfuse]]", "[[LangSmith]]", "[[Phoenix Arize]]"]
complements: []
tags: [llm, llm-observability, llm-gateway, tracing]
url_docs: https://docs.helicone.ai/
url_repo: https://github.com/Helicone/helicone
---

# Helicone

<!-- AUTO:BANDEAU:START -->
> Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Observabilité LLM en **mode proxy** : on change l'URL de base du SDK, chaque requête transite
par Helicone, qui journalise requête et réponse, compte tokens et coûts, mesure la latence,
puis applique cache, rate-limiting et métadonnées avant de relayer au fournisseur. C'est ce
qui la sépare d'un traçage par SDK — rien à instrumenter, mais un intermédiaire de plus sur
le chemin des appels. Le tableau de bord repose sur Cloudflare Workers, ClickHouse et Kafka ;
la passerelle elle-même est un binaire Rust séparé, `Helicone/ai-gateway`. Éditeur YC W23,
racheté par Mintlify le 3 mars 2026.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Brancher de l'observabilité LLM en une ligne — un changement d'URL, aucun code à instrumenter | Maintenance mode depuis le rachat Mintlify : correctifs de sécurité et de bugs seulement, plus de nouvelles intégrations ni de roadmap |
| Vouloir une passerelle et pas seulement des logs : cache de réponses, rate-limiting, routage, métadonnées | Le proxy est sur le chemin critique des appels — latence ajoutée et dépendance ; le logging asynchrone existe mais couvre moins de fonctions |
| Self-host rapide (un `docker compose`) pour garder les traces derrière son pare-feu | |
| Maintenir une app déjà intégrée : le proxy et l'image Docker restent fonctionnels | |

## Mise en œuvre

- Installation — `docker compose` en self-host, Docker ou Kubernetes en déploiement
- Point d'entrée — l'URL de base du SDK ; la passerelle est un binaire Rust distinct (`Helicone/ai-gateway`)
- Prérequis — architecture distribuée à opérer (Cloudflare Workers, ClickHouse, Kafka) ; le volume de logs commande le stockage, échantillonnage et rétention à régler
- Exécution — self-hébergé, ou Helicone Cloud managé
- Coût — code Apache-2.0 gratuit ; Helicone Cloud a un free-tier ; le dépôt accepte encore les contributions malgré le mode maintenance

## Écosystème

### Alternatives

- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.

## Ressources

- Documentation — https://docs.helicone.ai/
- Dépôt — https://github.com/Helicone/helicone

## Voir aussi

- [[LLM observability]] — la notion du dossier
- [[LiteLLM]] — l'autre proxy du vault, côté passerelles multi-fournisseurs
- [[Comparatif - Observabilité LLM]] — ce qui départage les plateformes du dossier
