---
galaxie: dev
type: service
nom: Helicone
alias: [helicone]
pitch: "Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode."
categorie: llm/observability
licence_type: open-source
hosted: both
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[Dev/Services/Langfuse|Langfuse]]", "[[Dev/Services/LangSmith|LangSmith]]", "[[Dev/Services/Phoenix Arize|Phoenix Arize]]"]
remplace_par: []
status: actif
tags: [llm, llm-observability, llm-gateway, tracing]
url_docs: https://docs.helicone.ai/
url_repo: https://github.com/Helicone/helicone
---

# Helicone

## Pourquoi

Plateforme d'**observabilité LLM** open-source (**Apache-2.0**, éditeur YC W23) dont la marque de fabrique est le **mode proxy / AI gateway** : on change l'URL de base du SDK et chaque requête transite par Helicone, qui logge requête/réponse, compte tokens et coûts, mesure la latence, puis applique cache, rate-limiting et métadonnées avant de relayer au fournisseur. Le tableau de bord (TypeScript) s'appuie sur une architecture **distribuée** (Cloudflare Workers, ClickHouse, Kafka) ; la passerelle elle-même est un binaire **Rust** séparé ([`Helicone/ai-gateway`](https://github.com/Helicone/ai-gateway)). **À savoir** : Helicone a été **racheté par Mintlify (annoncé le 3 mars 2026)** et est passé en **maintenance mode** — correctifs de sécurité et de bugs uniquement, plus de nouvelles intégrations ni de roadmap, et accompagnement des clients vers une migration.

## Quand l'utiliser

- Brancher de l'**observabilité LLM en une ligne** (changement d'URL), sans instrumenter le code.
- Vouloir un **gateway** : cache de réponses, rate-limiting, routage et métadonnées en plus des logs/coûts.
- **Self-host** rapide (un `docker compose`) pour garder les traces derrière son pare-feu.
- Maintenir une **app déjà intégrée à Helicone** (le proxy et l'image Docker restent fonctionnels).

## Quand NE PAS l'utiliser

- **Nouveau projet à horizon long** → éviter : projet en maintenance, sans roadmap, migration encouragée. Préférer [[Dev/Services/Langfuse|Langfuse]] (OSS actif) ou [[Dev/Services/Phoenix Arize|Phoenix Arize]].
- Besoin fort d'**évals, datasets et gestion de prompts** intégrés → [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/LangSmith|LangSmith]].
- Refus de mettre un **proxy sur le chemin critique** des appels LLM (latence, point unique de défaillance) → traçage par SDK/OpenTelemetry ([[Dev/Services/Phoenix Arize|Phoenix Arize]]).

## Déploiement & coût

- **Self-host** : déploiement Docker / Kubernetes ; architecture distribuée (Cloudflare Workers, ClickHouse, Kafka).
- **Helicone Cloud** managé avec free-tier (`hosted: both`).
- Code **Apache-2.0** gratuit ; le dépôt accepte encore les contributions malgré le mode maintenance.

## Pièges

- **Maintenance mode depuis le rachat Mintlify** : sécurité + bugfix seulement, aucune nouveauté — anticiper une migration pour tout projet durable.
- **Mode proxy** = Helicone sur le chemin critique des appels (latence ajoutée, dépendance) ; le logging asynchrone existe mais couvre moins de fonctions.
- Le **volume de logs** fait grimper le stockage : régler échantillonnage et rétention.

## Alternatives

- [[Dev/Services/Langfuse|Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[Dev/Services/LangSmith|LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Dev/Services/Phoenix Arize|Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.

## Liens

- Recoupe aussi la catégorie passerelle : [[Dev/Services/LiteLLM|LiteLLM]] (proxy multi-fournisseurs).
- Concepts : [[LLM observability]].
- [[Comparatif - Observabilité LLM]] — comparatif de la catégorie
- Doc : https://docs.helicone.ai/
