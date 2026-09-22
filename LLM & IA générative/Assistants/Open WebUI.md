---
role: brique
nom: Open WebUI
alias: [open-webui, openwebui, open webui]
pitch: "Interface web de chat auto-hébergée pour modèles locaux (Ollama) et API OpenAI-compatibles, licence propre à clause de marque (BSD-3 + interdiction de retirer le nom et le logo au-delà de 50 utilisateurs, non OSI) — RAG, rôles et groupes, LDAP et OIDC, extensible par outils et fonctions Python."
categorie: llm/assistant
famille: application
licence_type: source-available
hosted: [self]
maturite: production
langage: "Python, TypeScript"
scaling: distributed
alternatives: ["[[LibreChat]]", "[[AnythingLLM]]"]
complements: ["[[Ollama]]", "[[vLLM]]", "[[LiteLLM]]", "[[Docling]]", "[[Postgres]]"]
tags: [llm, local-llm, rag, self-hosted]
url_docs: https://docs.openwebui.com/
url_repo: https://github.com/open-webui/open-webui
---

# Open WebUI

<!-- AUTO:BANDEAU:START -->
> Interface web de chat auto-hébergée pour modèles locaux (Ollama) et API OpenAI-compatibles, licence propre à clause de marque (BSD-3 + interdiction de retirer le nom et le logo au-delà de 50 utilisateurs, non OSI) — RAG, rôles et groupes, LDAP et OIDC, extensible par outils et fonctions Python.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python, TypeScript | source-available | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Interface de chat **auto-hébergée** qui se branche sur Ollama et sur tout serveur compatible avec l'API OpenAI (vLLM, LM Studio, passerelles), sans envoi de données hors du réseau quand les modèles sont locaux. Elle réunit le chat multi-modèles, le **RAG** (bases de connaissances, extraction de documents, recherche hybride et reranking), des outils et des fonctions Python, des rôles et des groupes, et l'authentification LDAP, OAuth/OIDC et SCIM, sans clé de licence d'après la documentation. Backend Python, frontend Svelte. Version **v0.11.4** du 2026-09-21, 153 644 étoiles le 2026-09-30, dépôt actif au quotidien.

**Licence : ce n'est plus du BSD-3 depuis avril 2025.** Le `LICENSE` actuel reprend les trois clauses BSD puis ajoute une clause 4 : il est interdit de modifier, retirer, masquer ou remplacer la marque « Open WebUI » (nom, logo, identifiants visuels ou textuels) dans tout déploiement ou toute distribution, sauf trois cas — au plus **50 utilisateurs finaux** sur 30 jours glissants, permission écrite du titulaire, ou licence entreprise signée. Le projet dit lui-même que ce n'est pas une licence approuvée par l'OSI. Le code contribué jusqu'à la v0.6.5 (commit `60d84a3`) reste sous BSD-3. Pour une ESN : déployer chez un client, l'opérer et garder la marque est permis sans limite d'utilisateurs ; **retirer ou remplacer la marque au-delà de 50 utilisateurs (white-label) exige une licence entreprise**. La page « partenaires » de la documentation réclame en plus une licence entreprise pour tout déploiement chez un client final, ce que le texte du `LICENSE` ne dit pas : écart à faire lever par écrit avant de chiffrer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un assistant interne sur Ollama ou vLLM, avec RAG sur documents, rôles et groupes, en quelques conteneurs | Le white-label est nécessaire au-delà de 50 utilisateurs sans licence entreprise : [[LibreChat]] ou [[AnythingLLM]] sont sous MIT |
| Une communauté et un rythme de publication qui dépassent ceux des autres interfaces du lot | La règle interne impose une licence approuvée par l'OSI : la clause 4 l'exclut |
| Un RAG intégré qui accepte [[Docling]] ou Tika comme extracteur et plusieurs bases vectorielles | Le RAG doit être un moteur dédié (parsing de mises en page, graphes, droits par document) → [[RAGFlow]] |
| Des outils et fonctions Python ajoutés côté serveur pour adapter l'assistant | Des agents avec interpréteur de code, artefacts et partage d'agents par groupe → [[LibreChat]] |

## Mise en œuvre

- Installation — image Docker (variantes `:ollama`, `:cuda`, `slim`), `pip`, ou manifestes Kubernetes/Helm
- Point d'entrée — interface web ; connexion à Ollama et à des endpoints OpenAI-compatibles dans les réglages d'administration
- Prérequis — SQLite et Chroma locaux par défaut ; en multi-instance, [[Postgres]], Redis, une base vectorielle externe, un stockage partagé et la même `WEBUI_SECRET_KEY` partout
- Exécution — mono-conteneur par défaut ; la montée en charge horizontale est documentée, avec une instance unique pour les migrations de base
- Coût — gratuit sous licence propre ; l'édition entreprise (prix sur devis, non publié) débloque le retrait de la marque, le support et des offres réservées ; une centaine d'avis de sécurité entre mai et septembre 2026, dont un critique (contournement de l'authentification LDAP par mot de passe vide) : épingler la version et suivre les avis

## Écosystème

### Alternatives

- [[LibreChat]] — Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB.
- [[AnythingLLM]] — Application de chat et de RAG par espaces de travail (MIT, Mintplex Labs) — bureau en un clic ou Docker multi-utilisateur, LanceDB embarqué, nombreux fournisseurs de modèles locaux, agents et MCP ; le SSO standard n'existe que dans l'offre Enterprise.

### Compléments

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.

## Ressources

- Documentation — https://docs.openwebui.com/
- Dépôt — https://github.com/open-webui/open-webui
- Dépôt — texte de la licence : https://github.com/open-webui/open-webui/blob/main/LICENSE

## Voir aussi

- [[RAG documentaire on-prem - clé en main ou assemblé]] — la notion : ce que fige un RAG intégré
- [[Comparatif - Plateformes LLM auto-hébergées]] — le comparatif qui la situe
- [[Advanced RAG]] — la notion : ce que son pipeline de récupération met en œuvre
- [[Assistants]] — le hub du dossier
