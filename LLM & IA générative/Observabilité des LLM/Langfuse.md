---
role: brique
nom: Langfuse
alias: [langfuse]
pitch: "Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry."
categorie: llm/observabilite
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[LangSmith]]", "[[Phoenix Arize]]", "[[Helicone]]"]
complements: []
tags: [llm, llm-observability, tracing, llm-eval]
url_docs: https://langfuse.com/docs
url_repo: https://github.com/langfuse/langfuse
---

# Langfuse

<!-- AUTO:BANDEAU:START -->
> Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-core | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'ingénierie LLM qui réunit quatre piliers dans un workflow unique : le **traçage**
(chaque appel de modèle et d'outil en spans imbriqués, avec latence, coût et tokens), la
**gestion de prompts** versionnés et mis en cache, les **évaluations** (LLM-as-judge,
évaluateurs code, annotation humaine) et les **datasets** d'exemples. L'ingestion passe par
OpenTelemetry, par les SDK OpenAI, par [[LangChain]] ou par [[LiteLLM]], ce qui la rend
utilisable sur une stack hétérogène. Elle sait rejouer sur ses traces des évals écrites avec
[[Ragas]] ou [[DeepEval]]. Éditeur YC W23, racheté par ClickHouse en 2026.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Observer une app LLM en production : traces de bout en bout, coûts, latence, débogage des chaînes et des agents | Besoin d'une éval offline en CI seulement, sans plateforme à héberger → [[Ragas]], [[DeepEval]] |
| Centraliser prompts versionnés, évals et datasets au même endroit que les traces | Open-core : la fonction visée peut vivre dans les dossiers `ee/` sous licence commerciale, et non dans le cœur MIT |
| Garder la souveraineté des données en auto-hébergeant, sans renoncer à un cloud managé | Le self-host de production n'est pas trivial : ClickHouse, Postgres et Redis à opérer |
| Stack hétérogène : ingestion OpenTelemetry et intégrations multiples (OpenAI, LangChain, LiteLLM) | |

## Mise en œuvre

- Installation — Docker Compose en développement ; Helm sur Kubernetes ou Terraform AWS/Azure/GCP en production, multi-région possible
- Point d'entrée — SDK Python et JS, ingestion OpenTelemetry, intégrations OpenAI, LangChain, LiteLLM
- Prérequis — ClickHouse, Postgres et Redis pour le self-host de production ; le volume de traces commande le stockage, échantillonnage et rétention à régler
- Exécution — self-hébergé ou Langfuse Cloud managé, architecture distribuée
- Coût — cœur MIT gratuit ; SSO avancé et RBAC fin relèvent des dossiers `ee/` sous licence commerciale ; Langfuse Cloud a un free-tier généreux

## Écosystème

### Alternatives

- [[LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.
- [[Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Ressources

- Documentation — https://langfuse.com/docs
- Dépôt — https://github.com/langfuse/langfuse

## Voir aussi

- [[LLM observability]] — la notion du dossier
- [[LLM-as-judge]] — le mécanisme de ses évals en ligne
- [[Comparatif - Observabilité LLM]] — ce qui départage les plateformes du dossier
