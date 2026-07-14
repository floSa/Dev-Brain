---
galaxie: dev
type: service
nom: Langfuse
alias: [langfuse]
pitch: "Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry."
categorie: llm/observability
licence_type: open-core
hosted: both
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[Dev/Services/LangSmith|LangSmith]]", "[[Dev/Services/Phoenix Arize|Phoenix Arize]]", "[[Dev/Services/Helicone|Helicone]]"]
remplace_par: []
status: actif
tags: [llm, llm-observability, tracing, llm-eval]
url_docs: https://langfuse.com/docs
url_repo: https://github.com/langfuse/langfuse
---

# Langfuse

## Pourquoi

Plateforme d'**ingénierie LLM** open-core (cœur sous **MIT**, dossiers `ee/` sous licence commerciale ; éditeur racheté par **ClickHouse** en 2026, YC W23). Elle réunit quatre piliers dans un workflow unique : **observabilité/traçage** (chaque appel LLM et outil en spans imbriqués — latence, coût, tokens), **gestion de prompts** versionnés (avec cache), **évaluations** (LLM-as-judge, évaluateurs code, annotation humaine) et **datasets** d'exemples. Écrite en **TypeScript**, elle s'intègre à **OpenTelemetry**, aux SDK OpenAI, à [[Dev/Services/LangChain|LangChain]], [[Dev/Services/LiteLLM|LiteLLM]] et autres. Auto-hébergeable ou en SaaS (Langfuse Cloud).

## Quand l'utiliser

- **Observer une app LLM en production** : traces de bout en bout, coûts, latence, débogage des chaînes/agents.
- Centraliser **prompts versionnés**, **évals** et **datasets** au même endroit que les traces.
- Exiger de l'**open-source auto-hébergeable** (souveraineté des données) sans renoncer à un cloud managé.
- Stack hétérogène : ingestion via **OpenTelemetry** et intégrations multiples (OpenAI, LangChain, LiteLLM…).

## Quand NE PAS l'utiliser

- Besoin uniquement d'**éval offline en CI** (pas de plateforme à héberger) → [[Dev/Services/Ragas|Ragas]], [[Dev/Services/DeepEval|DeepEval]].
- App **100 % écosystème LangChain** cherchant l'intégration la plus serrée et un produit clé en main → [[Dev/Services/LangSmith|LangSmith]].
- Préférence pour une plateforme **bâtie nativement sur OpenTelemetry/OpenInference** avec un fort volet éval → [[Dev/Services/Phoenix Arize|Phoenix Arize]].

## Déploiement & coût

- **Self-host** : Docker Compose en dev ; Kubernetes/Helm et Terraform AWS/Azure/GCP en prod, multi-région — stack ClickHouse + Postgres + Redis, d'où `distributed`.
- **Langfuse Cloud** managé avec free-tier généreux (`hosted: both`).
- Cœur **MIT gratuit** ; certaines fonctions entreprise (SSO avancé, RBAC fin) relèvent des dossiers `ee/` sous licence commerciale.

## Pièges

- **Open-core** : vérifier que les fonctions visées sont dans le cœur MIT et non dans `ee/`.
- Le self-host de prod n'est **pas trivial** (ClickHouse + Postgres + Redis à opérer).
- Le **volume de traces** fait exploser le stockage : régler échantillonnage et rétention.

## Alternatives

- [[Dev/Services/LangSmith|LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Dev/Services/Phoenix Arize|Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.
- [[Dev/Services/Helicone|Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Liens

- Ingestion via [[Dev/Services/LiteLLM|LiteLLM]] (proxy), [[Dev/Services/LangChain|LangChain]], OpenTelemetry.
- Peut exécuter des évals issues de [[Dev/Services/Ragas|Ragas]] / [[Dev/Services/DeepEval|DeepEval]] sur les traces.
- Concepts : [[LLM observability]], [[LLM-as-judge]] (évals en ligne).
- [[Comparatif - Observabilité LLM]] — comparatif de la catégorie
- Doc : https://langfuse.com/docs
