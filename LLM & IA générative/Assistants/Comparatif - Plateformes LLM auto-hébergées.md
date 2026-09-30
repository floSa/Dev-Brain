---
role: comparatif
nom: Comparatif - Plateformes LLM auto-hébergées
categorie: llm/assistant
tags: [rag, agents, low-code, self-hosted, local-llm]
---

# Comparatif - Plateformes LLM auto-hébergées

> On tranche sur : ce qu'on déploie pour donner un assistant ou un RAG à des utilisateurs métier — une interface de chat, un moteur RAG ou un constructeur de workflows — puis, pour chacun, la licence et ce qu'elle permet à une ESN, la part du SSO et des rôles qui reste gratuite, et les services à opérer.

![[Comparatif - Plateformes LLM auto-hébergées.base]]

## Ce qui départage

- [[Open WebUI]] — la **communauté et le rythme** (153 644 étoiles, publications rapprochées) et un SSO libre (LDAP, OIDC, SCIM) avec rôles et groupes. La **licence propre** interdit de retirer la marque au-delà de 50 utilisateurs sans licence entreprise, et la page « partenaires » réclame une licence entreprise pour un déploiement chez un client final, ce que le texte du `LICENSE` ne dit pas. Environ cent avis de sécurité entre mai et septembre 2026.
- [[LibreChat]] — **agents, MCP, interpréteur de code et partage par groupe** sous MIT, avec OIDC, SAML et LDAP libres. Il exige MongoDB et un service RAG séparé sur PostgreSQL ; le panneau d'administration est gratuit mais en préversion, et le quota de jetons est global. Propriété de ClickHouse depuis novembre 2025.
- [[AnythingLLM]] — le **plus simple à poser** : bureau en un clic ou un conteneur Docker, LanceDB embarqué, MIT. Son SSO libre se limite à un jeton de passage ; OIDC, SAML et LDAP sont dans l'offre Enterprise. Les droits s'arrêtent à l'espace de travail.
- [[RAGFlow]] — le seul **moteur RAG** du lot : parsing par mise en page, modèles de chunking, GraphRAG, API et MCP, sous Apache-2.0, sans interface de chat généraliste. Le plus lourd à exploiter (MySQL, MinIO, cache, moteur de documents, 16 Go de RAM conseillés) et en candidate de publication 1.0 depuis le 2026-09-29.
- [[Dify]] — la **plateforme LLMOps** : workflows, RAG, gestion des modèles et observabilité dans une console. Sa licence interdit le multi-tenant et le retrait du logo sans accord ; le SSO, le RBAC fin et les espaces multiples sont dans l'édition Enterprise.
- [[Langflow]] — le constructeur **exportable en code Python**, sous MIT, rythme de publication hebdomadaire. Pas de SSO complet dans le dépôt ni d'isolation entre utilisateurs, et six CVE au catalogue CISA des vulnérabilités exploitées : à ne jamais exposer sans protection.
- [[Flowise]] — le constructeur **JavaScript**, **archivé depuis le 2026-08-13** : plus de correctifs officiels, SSO et espaces de travail dans un dossier sous licence commerciale. À lire comme un existant à migrer, pas comme un choix.

## Critères, plateforme par plateforme

| Plateforme | Nature | SSO sans payer | Rôles et multi-tenant | Licence, et ce qu'une ESN peut faire | À opérer |
|---|---|---|---|---|---|
| [[Open WebUI]] | Chat + RAG | LDAP, OIDC, SCIM | Rôles et groupes | Clause de marque : déployer et garder la marque oui ; retirer la marque au-delà de 50 utilisateurs, non sans licence entreprise | Un conteneur ; en multi-instance [[Postgres]], Redis, base vectorielle, stockage partagé |
| [[LibreChat]] | Chat + agents | OIDC, SAML, LDAP | Panneau d'administration ; quota global | MIT : déployer, rebrander, redistribuer | [[MongoDB]] obligatoire ; service RAG sur [[pgvector]] |
| [[AnythingLLM]] | Chat + RAG par espace | Jeton de passage seulement | Trois rôles, Docker uniquement | MIT : déployer, rebrander, redistribuer | Un conteneur, SQLite et [[LanceDB]] |
| [[RAGFlow]] | Moteur RAG | Blocs OIDC et OAuth2 en configuration | Équipes, partage des bases | Apache-2.0 : déployer, rebrander, redistribuer | MySQL, [[MinIO]], cache, moteur de documents |
| [[Dify]] | Constructeur et LLMOps | Aucun (Enterprise) | Un espace de travail | Apache modifiée : une instance par client avec le logo ; multi-tenant ou sans logo, licence commerciale | Plusieurs conteneurs |
| [[Langflow]] | Constructeur | Aucun complet | Administrateur et utilisateur ; aucune isolation | MIT : déployer, rebrander, redistribuer | Un processus ; une instance par client pour isoler |
| [[Flowise]] | Constructeur | Enterprise | Enterprise | Apache-2.0 hors dossier enterprise ; archivé | Node.js, mono-nœud |

Les interfaces voisines n'ont pas de fiche : LobeHub (ex-LobeChat, licence communautaire non OSI, version canary seulement) est la seule à pouvoir concurrencer ce trio pour un assistant interne ; Jan est une application de bureau mono-utilisateur, Chatbot UI n'est plus maintenu depuis 2024 et Open Interpreter est devenu un agent de code. Elles ne sont pas retenues.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
