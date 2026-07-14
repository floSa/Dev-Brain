---
galaxie: dev
type: service
nom: LangSmith
alias: [langsmith]
pitch: "Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise."
categorie: llm/observability
licence_type: proprietary
hosted: both
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Dev/Services/Langfuse|Langfuse]]", "[[Dev/Services/Phoenix Arize|Phoenix Arize]]", "[[Dev/Services/Helicone|Helicone]]"]
remplace_par: []
status: actif
tags: [llm, llm-observability, tracing, llm-eval]
url_docs: https://docs.langchain.com/langsmith
url_repo: 
---

# LangSmith

## Pourquoi

Plateforme **propriétaire** (closed-source, SaaS) d'**observabilité, d'évaluation et de déploiement** d'agents LLM, éditée par **LangChain Inc.** Elle fournit traçage détaillé, dashboards de monitoring, jeux d'évaluations (datasets, LLM-as-judge, annotation) et déploiement d'agents. Bien que née dans l'écosystème [[Dev/Services/LangChain|LangChain]], elle est **framework-agnostique** : elle instrumente une app quel que soit son framework, et supporte **OpenTelemetry** (depuis 2026). C'est le produit « clé en main » de l'éditeur, le plus intégré avec LangChain / [[Dev/Services/LangGraph|LangGraph]].

## Quand l'utiliser

- App bâtie sur **LangChain / LangGraph** : intégration la plus serrée, traçage quasi sans configuration.
- Vouloir un **produit managé** complet (observabilité + éval + déploiement) sans opérer d'infra.
- Workflow d'**éval continue** (datasets, comparaisons, regression testing) couplé au monitoring de prod.
- Contraintes de résidence des données → offre **self-host / BYOC** (entreprise).

## Quand NE PAS l'utiliser

- Exigence d'**open-source auto-hébergeable** gratuit → [[Dev/Services/Langfuse|Langfuse]] ou [[Dev/Services/Phoenix Arize|Phoenix Arize]].
- Besoin seulement d'**éval offline** en bibliothèque/CI → [[Dev/Services/Ragas|Ragas]], [[Dev/Services/DeepEval|DeepEval]].
- Refus d'un **SaaS propriétaire** ou budget contraint (self-host réservé à l'entreprise).

## Déploiement & coût

- **Cloud managé** (smith.langchain.com) par défaut ; **self-host** et **BYOC** réservés à l'offre **entreprise** (contrat + Kubernetes) — d'où `hosted: both`, mais self-host inaccessible aux tiers Developer/Plus.
- **Propriétaire**, payant par usage/siège ; pas de code source ouvert (langage d'implémentation non divulgué).
- SSO, RBAC, audit logs et self-host **gated** derrière l'offre entreprise.

## Pièges

- **Propriétaire** : risque de verrouillage (lock-in) et dépendance à l'éditeur.
- Self-host **non disponible** hors entreprise : les petites équipes restent sur le SaaS.
- Le **volume de traces** facturé peut surprendre : échantillonner.

## Alternatives

- [[Dev/Services/Langfuse|Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[Dev/Services/Phoenix Arize|Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.
- [[Dev/Services/Helicone|Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.

## Liens

- Produit de l'écosystème [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LangGraph|LangGraph]] (mais framework-agnostique).
- Concepts : [[LLM observability]], [[LLM eval metrics]].
- [[Comparatif - Observabilité LLM]] — comparatif de la catégorie
- Doc : https://docs.langchain.com/langsmith
