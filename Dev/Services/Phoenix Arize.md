---
galaxie: dev
type: service
nom: Phoenix Arize
alias: [phoenix, "Arize Phoenix", arize-phoenix, arize-ai-phoenix]
pitch: "Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX."
categorie: llm/observability
licence_type: source-available
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Langfuse|Langfuse]]", "[[Dev/Services/LangSmith|LangSmith]]", "[[Dev/Services/Helicone|Helicone]]"]
remplace_par: []
status: actif
tags: [llm, llm-observability, llm-eval, tracing]
url_docs: https://arize.com/docs/phoenix
url_repo: https://github.com/Arize-ai/phoenix
---

# Phoenix Arize

## Pourquoi

Plateforme open-source d'**observabilité et d'évaluation** LLM/agents éditée par **Arize AI**, sous **Elastic License 2.0** (source-available : usage interne large, mais interdiction d'en faire un service managé concurrent). Son traçage est bâti sur **OpenTelemetry / OpenInference** : elle ingère des spans depuis [[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/DSPy|DSPy]], CrewAI, les SDK OpenAI/Anthropic/Bedrock… Elle ajoute des **évals par LLM** (réponse et retrieval), des **datasets** versionnés et des **expérimentations**. C'est la version OSS, auto-hébergeable, de la plateforme entreprise **Arize AX**.

## Quand l'utiliser

- **Standardiser sur OpenTelemetry** : instrumentation ouverte, portable, multi-framework.
- Vouloir **observabilité + éval** dans un même outil open-source, auto-hébergeable simplement (un conteneur).
- Tracer des stacks variés (LangChain, LlamaIndex, DSPy, agents) sans coupler à un éditeur de framework.
- Démarrer gratuitement puis, au besoin, monter vers **Arize AX** (entreprise) sans tout réécrire.

## Quand NE PAS l'utiliser

- Exigence d'**OSI open source** strict (procurement) : ELv2 est *source-available*, pas OSI → [[Dev/Services/Langfuse|Langfuse]] (cœur MIT) convient mieux.
- App **100 % LangChain** cherchant le produit le plus intégré et managé → [[Dev/Services/LangSmith|LangSmith]].
- Besoin uniquement d'**éval offline** en bibliothèque/CI → [[Dev/Services/Ragas|Ragas]], [[Dev/Services/DeepEval|DeepEval]].

## Déploiement & coût

- **Self-host** : un conteneur Docker `arizephoenix/phoenix` (backend SQLite ou Postgres), exécution typiquement mono-nœud (`single-node`).
- Aussi en **cloud** (Phoenix Cloud) et adossé à **Arize AX** managé (`hosted: both`).
- Gratuit, **Elastic License 2.0** : pas de frais de siège ni de plafond d'événements, mais revente en service managé interdite.

## Pièges

- **ELv2 ≠ OSI** : *source-available* — vérifier la compatibilité avec les contraintes légales internes.
- Ne pas confondre **Phoenix** (OSS) et **Arize AX** (plateforme entreprise) : périmètres et licences différents.
- Le **volume de spans** OpenTelemetry grossit vite : régler rétention et échantillonnage.

## Alternatives

- [[Dev/Services/Langfuse|Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[Dev/Services/LangSmith|LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Dev/Services/Helicone|Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Liens

- Traçage **OpenTelemetry/OpenInference** depuis [[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/DSPy|DSPy]].
- Peut exécuter des évals de type [[Dev/Services/Ragas|Ragas]] sur les traces ; complément de [[Dev/Services/TruLens|TruLens]].
- Concepts : [[LLM observability]], [[LLM-as-judge]] (évals par LLM).
- [[Comparatif - Observabilité LLM]] — comparatif de la catégorie
- Doc : https://arize.com/docs/phoenix
