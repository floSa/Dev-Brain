---
role: brique
nom: Phoenix Arize
alias: [phoenix, "Arize Phoenix", arize-phoenix, arize-ai-phoenix]
pitch: "Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX."
categorie: llm/observabilite
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Langfuse]]", "[[LangSmith]]", "[[Helicone]]"]
complements: []
tags: [llm, llm-observability, llm-eval, tracing]
url_docs: https://arize.com/docs/phoenix
url_repo: https://github.com/Arize-ai/phoenix
---

# Phoenix Arize

<!-- AUTO:BANDEAU:START -->
> Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | source-available | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'observabilité et d'évaluation d'applications LLM et d'agents, éditée par Arize
AI. Son traçage est bâti **nativement sur OpenTelemetry** et sur la convention OpenInference :
elle ingère des spans venus de [[LangChain]], [[LlamaIndex]], [[DSPy]], CrewAI ou des SDK
OpenAI, Anthropic et Bedrock, sans coupler l'instrumentation à un éditeur de framework. S'y
ajoutent des évals par LLM (réponse et retrieval), des datasets versionnés et des
expérimentations, et elle peut exécuter des évals de type [[Ragas]] sur les traces collectées.
C'est la version auto-hébergeable de la plateforme entreprise **Arize AX** — deux produits
distincts, aux périmètres et aux licences différents, à ne pas confondre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Standardiser l'instrumentation sur OpenTelemetry : portable, multi-framework, non couplée à un éditeur | Besoin d'une éval offline en bibliothèque ou en CI, sans plateforme à opérer → [[Ragas]], [[DeepEval]] |
| Vouloir observabilité et éval dans un même outil auto-hébergeable, en un conteneur | Elastic License 2.0 : *source-available* et non OSI — usage interne large, mais revente en service managé interdite, et compatibilité juridique interne à vérifier |
| Tracer des stacks variés — LangChain, LlamaIndex, DSPy, agents — sans réécrire l'instrumentation | |
| Démarrer gratuitement puis monter vers Arize AX sans tout réécrire | |

## Mise en œuvre

- Installation — un conteneur Docker `arizephoenix/phoenix`
- Point d'entrée — SDK Python, ingestion OpenTelemetry / OpenInference, interface web
- Prérequis — SQLite pour démarrer, Postgres pour durer ; le volume de spans grossit vite, rétention et échantillonnage à régler
- Exécution — self-hébergé, typiquement mono-nœud, ou Phoenix Cloud et Arize AX managés
- Coût — gratuit : ni frais de siège ni plafond d'événements, mais la revente en service managé est interdite par l'Elastic License 2.0

## Écosystème

### Alternatives

- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Ressources

- Documentation — https://arize.com/docs/phoenix
- Dépôt — https://github.com/Arize-ai/phoenix

## Voir aussi

- [[LLM observability]] — la notion du dossier
- [[LLM-as-judge]] — le mécanisme de ses évals par LLM
- [[TruLens]] — l'autre approche par instrumentation, en bibliothèque plutôt qu'en plateforme
- [[Comparatif - Observabilité LLM]] — ce qui départage les plateformes du dossier
