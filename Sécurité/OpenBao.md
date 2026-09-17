---
role: brique
nom: OpenBao
alias: [openbao, bao, fork de vault, vault open source]
pitch: "Serveur de secrets sous MPL-2.0, fork communautaire de HashiCorp Vault (LF Edge puis OpenSSF, Go) : coffre clé-valeur, secrets dynamiques de bases de données, PKI, Transit, scellement Shamir ou auto-unseal, Raft intégré — sans fonction gardée en payant, mais qui diverge volontairement de Vault et ne corrige que sa dernière version."
categorie: security/secrets
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[SOPS]]"]
complements: ["[[Kubernetes]]"]
tags: [secrets-management, cryptography, self-hosted, kubernetes]
url_docs: https://openbao.org/docs/
url_repo: https://github.com/openbao/openbao
---

# OpenBao

<!-- AUTO:BANDEAU:START -->
> Serveur de secrets sous MPL-2.0, fork communautaire de HashiCorp Vault (LF Edge puis OpenSSF, Go) : coffre clé-valeur, secrets dynamiques de bases de données, PKI, Transit, scellement Shamir ou auto-unseal, Raft intégré — sans fonction gardée en payant, mais qui diverge volontairement de Vault et ne corrige que sa dernière version.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de secrets : les applications ne lisent plus un mot de passe dans un fichier, elles le **demandent** à un service qui les authentifie, applique une politique d'accès, journalise et peut révoquer. Il stocke des secrets statiques (moteur clé-valeur), en **fabrique à la volée** avec un bail (identifiants de base de données uniques par demandeur, révoqués à l'expiration : PostgreSQL, MySQL et MariaDB, Cassandra, InfluxDB, Valkey), émet des certificats (PKI) et chiffre pour le compte d'autres applications sans leur rendre la clé (*Transit*). Au démarrage, il est **scellé** : les données sont chiffrées par une clé elle-même chiffrée par une clé racine, qu'il faut déverrouiller (*unseal*). Relevé le 2026-09-30 : **v2.7.0** (2026-09-23), environ 8 200 étoiles, une version stable environ par mois.

**Filiation avec Vault.** OpenBao est le **fork de HashiCorp Vault** né du changement de licence : le 2023-08-10, HashiCorp a fait passer ses produits de MPL-2.0 à BUSL-1.1 ; le premier groupe de travail d'OpenBao date du 2023-11-09, l'annonce publique du 2023-12-08. Le point de fork est daté de deux façons dans les sources du projet — Vault 1.14.8 (« dernière version sous MPL », selon une discussion du dépôt) ou compatibilité d'API avec 1.14.9 (notes de la 2.0.0) — sans que cette fiche les départage. OpenBao a rejoint LF Edge le 2024-04-30, puis l'OpenSSF (projet *Sandbox*, accepté le 2025-06-17) ; la gouvernance est confiée à un comité technique. Licence **MPL-2.0**, aucune édition payante.

**Le lien n'est pas une équivalence.** La politique du projet vise la **compatibilité d'API**, pas celle du scellement ni du stockage : OpenBao diverge volontairement de Vault. Il a des *namespaces* depuis la 2.3 (bêta le 2025-05-28) à l'API compatible avec Vault Enterprise, et la 2.7.0 ajoute *Control Groups*, les clés externes (PKCS#11 ou KMS pour PKI et Transit), ML-DSA et un stockage PebbleDB. En sens inverse, la 2.7.0 **sort du binaire** les méthodes d'authentification LDAP, Kerberos et RADIUS et le moteur de secrets LDAP (devenus des plugins), supprime le stockage `file` et fait des scellements PKCS#11 et KMS cloud des plugins.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un serveur de secrets **sans licence à lire** : MPL-2.0, toutes les fonctions du binaire, rien de gardé en édition payante | Une stricte équivalence avec Vault ou avec Vault Enterprise : OpenBao diverge, et sa politique de migration le dit |
| Des secrets dynamiques (identifiants de base éphémères, certificats) plutôt que des mots de passe qui durent des années | Un annuaire LDAP ou Kerberos derrière l'authentification : depuis la 2.7.0 ces méthodes sont des plugins à installer à part |
| Le scellement Transit, la clé statique et Shamir sans licence ; du Raft intégré, sans base externe à exploiter | Deux ou trois secrets dans un dépôt Git à protéger : le chiffrement de fichiers de [[SOPS]] suffit et n'exige aucun serveur |
| Des clients, des chartes et des opérateurs conçus pour Vault : l'API est conservée, et External Secrets Operator sait parler à OpenBao par son fournisseur Vault | Un besoin de support contractuel ou d'un calendrier de fin de vie annoncé : seule la dernière version est corrigée, sans politique de fin de support |
| | Un opérateur Kubernetes tout fait : l'injecteur `openbao-k8s` n'a pas eu de version depuis mars 2024 et l'opérateur de secrets est archivé |

## Mise en œuvre

- Installation — images Alpine et UBI (ghcr.io, Quay, Docker Hub), paquets Linux et chart Helm (`openbao-helm` 0.30.0, 2026-09-28) ; un fournisseur CSI existe (`openbao-csi-provider` v2.0.3) ; le verrouillage mémoire `mlock` a été retiré au profit de celui du cgroup
- Point d'entrée — `bao server -config=…`, puis `bao operator init` qui renvoie les parts de clé d'unseal et un jeton racine, à révoquer une fois les méthodes d'authentification en place ; les clients s'authentifient (jeton, AppRole, Kubernetes, OIDC) et lisent `secret/…`
- Prérequis — stockage : **Raft intégré**, 5 nœuds recommandés ; PostgreSQL est possible, avec des lectures scalables depuis la 2.7 ; **le scellement décide du bootstrap** : Shamir par défaut (parts distribuées à des personnes), ou auto-unseal par une clé statique, par le *Transit* d'une autre instance OpenBao (jeton orphelin et périodique), ou par HSM ; si la clé du mécanisme externe est perdue, le cluster est irrécupérable, sauvegardes comprises
- Exécution — passer d'un type de scellement à un autre demande un arrêt ; une version stable environ par mois, et seule la dernière est corrigée
- Coût — gratuit ; l'exploitation d'un cluster à 5 nœuds, de ses sauvegardes de snapshots et de la garde des parts de clé est le coût réel

## Limites à connaître

- **Des avis critiques en série** : six sur 24 mois (un en août 2025, cinq en 2026), dont une exécution de code à distance par remplacement du catalogue de plugins (GHSA-j6wc-jpvg-xfxq, 2026-09-23), une fuite du jeton du mode *recovery* par attaque temporelle (CVE-2026-63132, 2026-07-14) et deux failles de l'authentification OIDC (CVE-2026-33757 et CVE-2026-33758, 2026-03-25). La règle « seule la dernière version est corrigée » impose de suivre.
- **Le secret zéro n'est pas supprimé, il est déplacé** : c'est le jeton d'un autre OpenBao (Transit), la clé statique ou les parts de Shamir. [[Gestion des secrets]] traite ce que la documentation de Vault en dit (AppRole avec *response wrapping*, orchestrateur de confiance).
- **External Secrets Operator** documente OpenBao par son fournisseur Vault, testé avec la seule version 2.2.0 ; la compatibilité avec le Vault Secrets Operator n'a pas de source officielle trouvée.
- Adoption : NVIDIA (NVCF), Adfinis, Fermilab, SAP (ApeiroRA), EdgeX Foundry 4.0. Aucune source officielle lue ne confirme qu'une distribution l'embarque.

## Vault, ce dont OpenBao est le fork

**HashiCorp Vault** (36 300 étoiles, Go, **v2.1.1** du 2026-09-16) n'a pas de fiche : sa licence, **BUSL-1.1 depuis la version 1.15.0 (2023-09-27)**, n'est pas une licence libre.

- **Ce que dit la licence lue** : la production est autorisée, sauf de proposer l'outil à des tiers sous forme hébergée ou embarquée pour concurrencer l'offre payante de l'éditeur ; l'usage interne à une organisation n'est pas une offre concurrente. Chaque version bascule en **MPL-2.0 quatre ans après sa publication**. Le cas d'une ESN qui revend ou intègre Vault dans une offre facturée, avec support payant, tombe dans les termes « embarqué » et « support payant » : la FAQ officielle, qui fait référence d'interprétation, n'a pas été relue ici — à vérifier avant toute offre commerciale.
- **Propriétaire** : IBM a finalisé le rachat de HashiCorp le 2025-02-27 (35 $ l'action, 6,4 Md$) ; le fichier LICENSE désigne IBM comme concédant depuis le 2026-03-26. Vault 2.0 (2026-04-14) passe au versionnement et au support d'IBM, avec au moins deux ans de support standard. Aucun changement de licence depuis la BUSL n'a été trouvé.
- **Ce que l'édition Enterprise garde** : réplication, HSM et PKCS#11, Secrets Sync, *namespaces*, FIPS, *seal wrap*, MFA, Sentinel, *Control Groups*, *performance standbys*, snapshots automatisés, SCIM. Le scellement Transit fonctionne dans toutes les éditions, mais exige un second Vault.
- **Sécurité** : bulletins HCSEC sans gravité publiée ; parmi eux, l'exécution de code sur l'hôte et l'élévation de jeton d'août 2025 (CVE-2025-6000, CVE-2025-5999, que le projet OpenBao classe critique et haute) et quatre bulletins d'avril 2026 (SSRF par challenge ACME, fuite de jetons vers les plugins d'authentification, déni de service, contournement de politique KVv2).
- **Pourquoi pas de fiche** : le plafond de cinq briques, et le critère « open source ou proche ». Vault reste le produit que beaucoup de sites industriels ont déjà : cette section dit ce qu'il faut savoir pour le rencontrer sans le configurer.

## Écosystème

### Alternatives

- [[SOPS]] — Chiffre les valeurs d'un fichier YAML, JSON, ENV ou INI en laissant clés et structure lisibles (MPL-2.0, Go, CNCF Sandbox) — clés age, PGP, KMS cloud ou Transit de Vault ou OpenBao ; le fichier chiffré se versionne dans Git, mais sans serveur : ni audit, ni révocation, ni rotation automatique. — un fichier chiffré dans Git contre un service qui distribue, journalise et révoque ; SOPS sait d'ailleurs utiliser le Transit d'OpenBao comme backend de clés.

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm, fournisseur CSI et méthode d'authentification Kubernetes ; External Secrets Operator sait y synchroniser des secrets depuis OpenBao.

## Ressources

- Documentation — https://openbao.org/docs/
- Dépôt — https://github.com/openbao/openbao
- Documentation — scellement (seal/unseal) : https://openbao.org/docs/concepts/seal/
- Documentation — auto-unseal par Transit : https://openbao.org/docs/configuration/seal/transit/
- Documentation — stockage Raft intégré : https://openbao.org/docs/internals/integrated-storage/
- Documentation — secrets dynamiques de bases de données : https://openbao.org/docs/secrets/databases/
- Documentation — politique de migration depuis Vault : https://github.com/openbao/openbao/blob/main/website/content/community/policies/migration.mdx
- Documentation — politique de support : https://github.com/openbao/openbao/blob/main/website/content/community/policies/support.mdx
- Documentation — avis de sécurité : https://github.com/openbao/openbao/security/advisories
- Article — annonce de l'adoption de la BUSL par HashiCorp : https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license
- Documentation — licence de Vault : https://raw.githubusercontent.com/hashicorp/vault/main/LICENSE

## Voir aussi

- [[Sécurité]] — le hub du domaine
- [[Gestion des secrets]] — la notion : ce qu'il ne faut pas faire, coffre contre chiffrement de fichiers, rotation, bootstrap du premier secret
