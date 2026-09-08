---
role: brique
nom: LangSmith
alias: [langsmith]
pitch: "Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise."
categorie: llm/observabilite
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Langfuse]]", "[[Phoenix Arize]]", "[[Helicone]]"]
complements: []
tags: [llm, llm-observability, tracing, llm-eval]
url_docs: https://docs.langchain.com/langsmith
url_repo: 
---

# LangSmith

<!-- AUTO:BANDEAU:START -->
> Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme | propriétaire | self-hébergé ou managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme d'observabilité, d'évaluation et de déploiement d'agents LLM éditée par LangChain
Inc. : traçage détaillé, dashboards de monitoring, jeux d'évaluation (datasets, LLM-as-judge,
annotation humaine) et déploiement d'agents dans un seul produit clé en main. Née dans
l'écosystème [[LangChain]], elle est **framework-agnostique** — elle instrumente une app quel
que soit son framework et accepte OpenTelemetry depuis 2026 — mais c'est avec LangChain et
[[LangGraph]] que le traçage demande le moins de configuration. Le langage d'implémentation
n'est pas divulgué.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| App bâtie sur [[LangChain]] ou [[LangGraph]] : intégration la plus serrée, traçage quasi sans configuration | Besoin d'une éval offline en bibliothèque ou en CI, sans plateforme à opérer → [[Ragas]], [[DeepEval]] |
| Vouloir un produit managé complet — observabilité, éval, déploiement — sans opérer d'infra | Self-host et BYOC réservés à l'offre entreprise : hors de ce contrat, seul le SaaS est accessible |
| Workflow d'éval continue (datasets, comparaisons, tests de régression) couplé au monitoring de production | Code fermé : dépendance à l'éditeur, rien à auditer ni à forker |
| Contrainte de résidence des données, couverte par l'offre self-host / BYOC entreprise | |

## Mise en œuvre

- Installation — rien à installer sur le SaaS (`smith.langchain.com`) ; le self-host et le BYOC passent par un contrat entreprise et un cluster Kubernetes
- Point d'entrée — SDK LangSmith, intégration native LangChain / LangGraph, ou ingestion OpenTelemetry
- Prérequis — un compte ; Kubernetes uniquement pour le self-host entreprise
- Exécution — cloud managé par défaut, self-hébergé ou BYOC en entreprise, architecture distribuée
- Coût — payant à l'usage et au siège ; le volume de traces est facturé, prévoir l'échantillonnage ; SSO, RBAC et audit logs sont derrière l'offre entreprise

## Écosystème

### Alternatives

- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.
- [[Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Ressources

- Documentation — https://docs.langchain.com/langsmith

## Voir aussi

- [[LLM observability]] — la notion du dossier
- [[LLM eval metrics]] — ce que ses évaluations mesurent
- [[Comparatif - Observabilité LLM]] — ce qui départage les plateformes du dossier
