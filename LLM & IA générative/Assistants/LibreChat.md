---
role: brique
nom: LibreChat
alias: [librechat, libre-chat, danny-avila/LibreChat]
pitch: "Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB."
categorie: llm/assistant
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: "JavaScript, TypeScript"
scaling: distributed
alternatives: ["[[Open WebUI]]", "[[AnythingLLM]]"]
complements: ["[[Ollama]]", "[[LiteLLM]]", "[[MongoDB]]", "[[pgvector]]", "[[Keycloak]]", "[[Authentik]]"]
tags: [llm, local-llm, rag, agents, mcp, self-hosted]
url_docs: https://www.librechat.ai/docs
url_repo: https://github.com/LibreChat-AI/LibreChat
---

# LibreChat

<!-- AUTO:BANDEAU:START -->
> Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript, TypeScript | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Interface de chat **auto-hébergée** qui parle à la plupart des fournisseurs — OpenAI, Anthropic, Google, Azure, Bedrock — et à tout endpoint compatible OpenAI (Ollama, passerelles) déclaré dans `librechat.yaml`. Au-delà du chat : des **agents** (outils, File Search, serveurs MCP, interpréteur de code en bac à sable, artefacts, partage par utilisateur ou groupe), un **RAG** porté par un service séparé sur PostgreSQL et pgvector, une recherche optionnelle (Meilisearch) et un **panneau d'administration** gratuit pour les utilisateurs, groupes et rôles, encore annoncé en préversion. Authentification locale, OAuth2, **OIDC** (pages dédiées pour Keycloak et Authentik), **SAML** et **LDAP**. Version **v0.8.8-rc4** du 2026-09-23 (la dernière non candidate est la v0.8.7 du 2026-06-24, et GitHub marque toutes les versions comme préversions), 45 164 étoiles le 2026-09-30.

**Licence : MIT**, relue dans le dépôt, sans clause de marque ni édition payante des fonctions d'entreprise. Une ESN peut déployer chez un client, retirer ou changer la marque, et redistribuer. Le dépôt a changé de propriétaire : il est passé de `danny-avila/LibreChat` à `LibreChat-AI/LibreChat`, et **ClickHouse a racheté le projet le 4 novembre 2025** en s'engageant à le maintenir ouvert ; le billet ne dit rien de la licence, et aucun changement n'est constaté à ce jour.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un assistant d'entreprise multi-fournisseurs, avec agents et MCP, sous licence MIT sans restriction de marque | L'infrastructure exclut MongoDB : il est obligatoire, et aucune alternative n'est documentée |
| Un SSO libre (OIDC, SAML, LDAP) devant un Keycloak ou un Authentik existant | Le quota doit varier par utilisateur ou par rôle : le budget de jetons est global d'après la documentation |
| Des agents partagés par groupe, avec interpréteur de code et artefacts | Un RAG plus simple, sans service séparé ni PostgreSQL → [[AnythingLLM]] |
| Une interface proche de ChatGPT pour des utilisateurs métier | La surface MCP et les points d'accès personnalisés inquiètent : ce sont eux qui concentrent les avis de sécurité récents → [[Open WebUI]] ne les expose pas de la même façon |

## Mise en œuvre

- Installation — Docker Compose officiel (api, panneau d'administration, MongoDB, Meilisearch, pgvector, service RAG)
- Point d'entrée — interface web ; `librechat.yaml` déclare les endpoints personnalisés, les agents et les règles d'accès
- Prérequis — [[MongoDB]] (Amazon DocumentDB 5.0+ accepté) ; Redis seulement en multi-réplica ; [[pgvector]] pour le RAG
- Exécution — mono-nœud par défaut, multi-réplica avec Redis ; le panneau d'administration est un service distinct sur la même base
- Coût — gratuit sous MIT ; 29 avis de sécurité publiés, dont un critique en juin 2026 (injection d'URL de serveur MCP exfiltrant des secrets) : épingler la version et relire les avis

## Écosystème

### Alternatives

- [[Open WebUI]] — Interface web de chat auto-hébergée pour modèles locaux (Ollama) et API OpenAI-compatibles, licence propre à clause de marque (BSD-3 + interdiction de retirer le nom et le logo au-delà de 50 utilisateurs, non OSI) — RAG, rôles et groupes, LDAP et OIDC, extensible par outils et fonctions Python.
- [[AnythingLLM]] — Application de chat et de RAG par espaces de travail (MIT, Mintplex Labs) — bureau en un clic ou Docker multi-utilisateur, LanceDB embarqué, nombreux fournisseurs de modèles locaux, agents et MCP ; le SSO standard n'existe que dans l'offre Enterprise.

### Compléments

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous.
- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter.
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois.

## Ressources

- Documentation — https://www.librechat.ai/docs
- Dépôt — https://github.com/LibreChat-AI/LibreChat
- Article — rachat par ClickHouse : https://clickhouse.com/blog/clickhouse-acquires-librechat

## Voir aussi

- [[RAG documentaire on-prem - clé en main ou assemblé]] — la notion : ce que fige un RAG intégré
- [[Comparatif - Plateformes LLM auto-hébergées]] — le comparatif qui la situe
- [[Agent patterns]] — la notion : les formes d'agent que ses agents assemblent
- [[Assistants]] — le hub du dossier
