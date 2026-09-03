---
role: hub
nom: Observabilité des LLM
pitch: Voir ce qu'une application LLM fait en production — traces, coût, latence, qualité sur le trafic réel.
domaines: [ai-eng, mlops]
tags: [llm-observability, tracing, observability]
---

# Observabilité des LLM

> Voir ce qu'une application LLM fait en production — traces, coût, latence, qualité sur le trafic réel.

## Ce qu'il faut comprendre

- L'observabilité **n'est pas l'éval**, et confondre les deux fait acheter un outil pour l'autre. L'éval juge un jeu de tests choisi ([[Évaluation]]) ; l'observabilité regarde ce qui arrive vraiment, y compris ce que personne n'avait pensé à tester. [[LLM observability]] pose la distinction.
- La donnée de base est la **trace imbriquée** : un appel utilisateur contient des appels de modèle, des récupérations, des appels d'outils, chacun avec sa latence, ses tokens et son coût. Sans elle, on débogue un système non déterministe à l'aveugle.
- **Le coût par requête est une métrique de production, pas une ligne de facture.** C'est là qu'on voit qu'un préfixe non mis en cache double la note, ou qu'une boucle d'agent part en vrille sur 3 % du trafic.
- Le premier critère de choix entre les plateformes est l'**auto-hébergement** — ce qui transite est le prompt de l'utilisateur — et le second l'**attachement à un framework** : un outil neutre survit à un changement de socle, un outil intégré coûte moins cher à brancher.
- **Une brique du dossier est en maintenance** ([[Helicone]]), et c'est une information de choix, pas une note de bas de page.

## Choisir

- Open-core, self-hébergeable, éval et gestion de prompts au même endroit → [[Langfuse]].
- Standard ouvert, instrumentation OpenTelemetry réutilisable ailleurs → [[Phoenix Arize]].
- Écosystème LangChain / LangGraph déjà en place, managé accepté → [[LangSmith]].
- Un proxy à poser devant l'API sans toucher au code → [[Helicone]], en tenant compte de son état de maintenance.
- Noter la qualité sur un jeu figé plutôt que sur le trafic → [[Évaluation]].
- Surveiller la dérive d'un modèle entraîné maison → [[Machine Learning]].

<!-- AUTO:START -->
### Notions
- [[LLM observability]] — domaines : ai-eng, mlops

### Briques
- [[Helicone]] — Plateforme open-source d'observabilité LLM en mode proxy / AI gateway (Apache-2.0) — trace requêtes, coûts, latence et tokens en une ligne, avec cache et rate-limiting ; self-host ou cloud. Rachetée par Mintlify (mars 2026), en maintenance mode.
- [[Langfuse]] — Plateforme open-core d'ingénierie LLM (cœur MIT + dossiers ee/) — traçage, gestion de prompts, évals (LLM-as-judge) et datasets dans un workflow unifié ; auto-hébergeable ou Langfuse Cloud, intègre OpenTelemetry.
- [[LangSmith]] — Plateforme propriétaire d'observabilité et d'éval LLM de LangChain — traçage, dashboards, évaluations et déploiement d'agents, framework-agnostique au-delà de LangChain ; cloud managé, self-host réservé à l'offre entreprise.
- [[Phoenix Arize]] — Plateforme open-source d'observabilité et d'éval LLM d'Arize (Elastic License 2.0) — traçage bâti sur OpenTelemetry/OpenInference, évals par LLM, datasets et expérimentations ; auto-hébergeable (un conteneur) ou cloud, version OSS de la plateforme Arize AX.

### Comparatifs
- [[Comparatif - Observabilité LLM]]
<!-- AUTO:END -->
