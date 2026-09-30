---
role: comparatif
nom: Comparatif - Fournisseurs d'identité
categorie: security/auth
tags: [identity-provider]
---

# Comparatif - Fournisseurs d'identité

> On tranche sur : le rôle (fournisseur complet qui émet des jetons, ou portail qui décide à l'entrée d'un proxy), les protocoles servis (SAML n'est pas partout), ce que l'édition libre laisse à un abonnement — seul Authentik en a un —, l'empreinte à exploiter, et le rythme des correctifs de sécurité à suivre.

![[Comparatif - Fournisseurs d'identité.base]]

## Ce qui départage

- [[Keycloak]] — le fournisseur complet et le plus installé : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, plusieurs *realms*, adossé à la CNCF (incubating) avec un support vendu par Red Hat et aucune fonction gardée en payant. Le prix : une JVM et une base SQL (1 250 Mo de RAM par pod pour 10 000 sessions), 13 avis de gravité haute en 24 mois dont 11 en cinq mois, et des ruptures de comportement d'une mineure à l'autre.
- [[Authentik]] — un seul produit pour le fournisseur d'identité et le portail de forward auth, avec des parcours de connexion composés en interface (flux, étapes, politiques) et LDAP, RADIUS et SCIM en plus d'OIDC et de SAML ; PostgreSQL seul depuis la retraite de Redis. Le prix : c'est le seul des trois à avoir une édition payante qui verrouille des fonctions (audit renforcé, PAM, provisioning Entra et Google, certificats clients : 5 $ par utilisateur et par mois), des avis critiques en 2026 et deux avis qui contournent le forward auth derrière un proxy.
- [[Authelia]] — le portail léger placé à côté du reverse proxy : mot de passe plus MFA, utilisateurs en fichier ou LDAP, une mémoire annoncée sous 30 Mo, et un fournisseur OIDC certifié, sans offre payante ni avis de gravité haute en 24 mois. Le prix : pas de SAML, pas de déconnexions OIDC, pas d'inscription ni de fédération vers d'autres fournisseurs, un chart Helm en bêta.

**Critère par critère**

**Protocoles servis.** [[Keycloak]] : OIDC, OAuth 2.0 et SAML 2.0 (comme fournisseur et comme service) ; SCIM est *preview*. [[Authentik]] : OIDC, SAML, LDAP, SCIM, RADIUS, Kerberos et proxy, la certification OpenID étant acquise à la 2026.8. [[Authelia]] : OIDC seul, certifié ; SAML « planifié » sans échéance.

**Fédération et annuaires.** [[Keycloak]] fédère LDAP, Active Directory, SSSD et FreeIPA, et sert d'intermédiaire vers des fournisseurs sociaux, OIDC, SAML, SPIFFE ou Kubernetes. [[Authelia]] lit un fichier YAML ou un LDAP, sans autre fédération. [[Authentik]] gère des sources externes ; la documentation Enterprise range pourtant les « sources OAuth et SAML externes » dans sa liste payante, ce qui est à revérifier avant de compter sur l'édition libre.

**MFA.** [[Keycloak]] : TOTP et HOTP, WebAuthn, passkeys, codes de récupération. [[Authelia]] : TOTP, clés de sécurité, passkeys WebAuthn, push Duo. [[Authentik]] : non relevé ici en détail ; un avis de 2026 concerne le contournement du MFA par courriel.

**Derrière Traefik, Caddy ou Nginx.** Deux logiques. [[Authelia]] et [[Authentik]] se **placent à côté du proxy** qui leur délègue la décision (ForwardAuth, `forward_auth`, `auth_request`) : chacun a ses trois pages d'intégration officielles. [[Keycloak]] est plutôt une **application derrière le proxy** : il demande `--proxy-headers`, un nom d'hôte déclaré et des en-têtes `X-Forwarded-*` écrasés par le proxy ; ce sont les applications qui lui parlent en OIDC. Le middleware OIDC natif de Traefik n'existe que dans son offre Hub, payante.

**Empreinte.** [[Authelia]] : binaire Go, image sous 20 Mo, mémoire annoncée sous 30 Mo. [[Authentik]] : 2 cœurs et 2 Go de RAM au minimum, un serveur, un *worker*, PostgreSQL. [[Keycloak]] : 1 250 Mo de RAM par pod pour 10 000 sessions en cache, 1 vCPU pour 15 connexions par mot de passe par seconde.

**Exploitation.** Stockage : PostgreSQL, MariaDB, MySQL, MSSQL ou Oracle pour [[Keycloak]] ; PostgreSQL seul pour [[Authentik]] ; SQLite, MySQL ou PostgreSQL pour [[Authelia]], avec Redis pour la haute disponibilité. Mise à jour : la base de Keycloak migre au démarrage ; Authentik interdit tout retour arrière et impose de ne pas sauter de majeure ; Authelia annonce des dépréciations pour sa v5.0.0. Helm : chart officiel pour Authentik ; opérateur pour Keycloak, sans chart officiel trouvé ; chart Authelia en bêta.

**Fonctions payantes et licence.** [[Keycloak]] Apache-2.0 et [[Authelia]] Apache-2.0 : rien de gardé. [[Authentik]] est **open-core** : MIT, sauf un dossier propriétaire (`authentik/enterprise/`), libre en développement, abonnement obligatoire en production.

**Sécurité, sur 24 mois** (avis officiels). Keycloak : aucun critique, 13 de gravité haute. Authentik : au moins trois critiques, dont une exécution de code authentifiée, plus une quinzaine de gravité haute en 2026, surtout sur les sources SAML. Authelia : aucun critique ni haut, un modéré et trois faibles. Les chiffres sont à lire avec la surface : Authelia fait beaucoup moins de choses.

**Pas de fiche ici**, faute d'avoir passé le critère « éprouvé et utile en on-prem » :

- ZITADEL — AGPL-3.0 depuis la v3.0.0 (2025-05-02), v4.19.3 (2026-09-29), environ 15 100 étoiles ; aucune fonction gardée en auto-hébergement n'a été trouvée, mais la page des tarifs est centrée sur son offre Cloud, il est le plus jeune du lot, et son volume d'avis de sécurité est nettement plus élevé (plusieurs critiques en 2025 et 2026, surtout autour du Login V2 : SSRF non authentifié, prise de compte par un callback de fournisseur externe ou par l'enrôlement de passkey). À revoir quand ce rythme aura baissé.
- oauth2-proxy — MIT, CNCF Sandbox, v7.15.4 (2026-08-20) : un intermédiaire qui ajoute l'OIDC devant une application, pas un fournisseur d'identité. Mentionné dans la notion [[OAuth2 et OpenID Connect]].
- Dex, Ory Kratos et Hydra, Gluu, FusionAuth, Casdoor, Zitadel Cloud, les fournisseurs SaaS (Auth0, Okta, Entra ID) : non évalués, ou hors du critère on-prem ouvert.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Authentification]] — le hub du dossier.
- [[OAuth2 et OpenID Connect]] — la notion : flux, jetons, pièges, ce que fait un fournisseur d'identité.
