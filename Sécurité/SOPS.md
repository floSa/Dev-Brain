---
role: brique
nom: SOPS
alias: [sops, mozilla sops, getsops, secrets operations]
pitch: "Chiffre les valeurs d'un fichier YAML, JSON, ENV ou INI en laissant clés et structure lisibles (MPL-2.0, Go, CNCF Sandbox) — clés age, PGP, KMS cloud ou Transit de Vault ou OpenBao ; le fichier chiffré se versionne dans Git, mais sans serveur : ni audit, ni révocation, ni rotation automatique."
categorie: security/secrets
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[OpenBao]]"]
complements: ["[[Kubernetes]]"]
tags: [secrets-management, cryptography]
url_docs: https://getsops.io/docs/
url_repo: https://github.com/getsops/sops
---

# SOPS

<!-- AUTO:BANDEAU:START -->
> Chiffre les valeurs d'un fichier YAML, JSON, ENV ou INI en laissant clés et structure lisibles (MPL-2.0, Go, CNCF Sandbox) — clés age, PGP, KMS cloud ou Transit de Vault ou OpenBao ; le fichier chiffré se versionne dans Git, mais sans serveur : ni audit, ni révocation, ni rotation automatique.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Éditeur de **fichiers chiffrés**. `sops secrets.yaml` déchiffre le fichier, l'ouvre dans l'éditeur, puis le rechiffre à l'enregistrement : seules les **valeurs** sont chiffrées (AES-256-GCM), les clés et la structure restent en clair — d'où un `git diff` lisible, qui montre *quel* secret a changé sans dire sa valeur. Formats pris en charge : YAML, JSON, ENV, INI et binaire. Les clés de chiffrement des données sont elles-mêmes chiffrées pour chaque **destinataire** : une clé **age** (dont les clés SSH ed25519 et rsa), PGP, un KMS cloud (AWS, GCP, Azure Key Vault, HuaweiCloud) ou le *Transit* d'un serveur HashiCorp Vault ou [[OpenBao]] — le seul backend qui ne dépend pas d'un cloud et qui passe par un serveur de secrets. Né chez Mozilla en 2015, il est aujourd'hui dans l'organisation `getsops`, **projet CNCF Sandbox** accepté le 2023-05-17. Relevé le 2026-09-30 : **v3.13.3** (2026-07-23), environ 23 300 étoiles, 7 versions en 12 mois, dernier commit le 2026-09-21. Licence **MPL-2.0**.

Ce que SOPS **n'est pas** : un serveur. Rien ne journalise qui lit, rien ne révoque, rien ne fait tourner un secret : le fichier chiffré est une donnée, versionnée comme du code.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des secrets de configuration à **versionner dans Git** avec le reste, sans serveur à exploiter — le cas d'un site isolé qui n'aura jamais de coffre | Des secrets dynamiques, un journal d'accès, la révocation immédiate : c'est le métier d'un serveur — [[OpenBao]] |
| Des manifestes Kubernetes à chiffrer : Flux déchiffre nativement avec SOPS (age, PGP, Vault, KMS), juste avant l'application | Un déploiement piloté par [[Argo CD]] qui génère les manifestes avec SOPS : sa documentation le déconseille, car les secrets se retrouvent en cache dans Redis |
| Une clé **age** par équipe ou par machine : petite, explicite, sans configuration | Une équipe qui change souvent : chaque destinataire porte sa clé, et en retirer un exige de **rechiffrer les fichiers** |
| Un `git diff` qui reste relu par un humain | Un fichier dont l'historique Git sera public un jour : le chiffré reste dans l'historique **pour toujours**, et si la clé fuit plus tard, tout l'historique se lit |

## Mise en œuvre

- Installation — un binaire unique (`sops`), paquets et images des versions publiées
- Point d'entrée — un fichier `.sops.yaml` qui associe des chemins à des destinataires ; `sops edit`, `sops -d`, `sops exec-env`, `sops exec-file` ; pour age, `SOPS_AGE_KEY_FILE`, `SOPS_AGE_KEY` ou `SOPS_AGE_KEY_CMD`
- Prérequis — **la clé privée est le secret zéro** : la stocker hors du dépôt (gestionnaire de mots de passe, disque chiffré, jeton matériel) ; aucune procédure de bootstrap n'est recommandée par la documentation de SOPS ; avec Flux, la clé age privée se pose dans un Secret dont le nom finit par `.agekey`
- Exécution — la faille GHSA-jgf3-f6rg-8x3h (haute, 7,4) : un fichier chiffré malveillant peut envoyer le jeton Vault de l'utilisateur à une adresse choisie par l'attaquant via `vault_address` ; **aucune version corrigée**, seulement une parade depuis la 3.13.0 : renseigner `SOPS_HC_VAULT_ALLOWLIST` (sa valeur par défaut est `all`) ; ne pas déchiffrer de fichiers non fiables
- Coût — gratuit ; les clés KMS cloud, si utilisées, sont facturées par le cloud

## Limites à connaître

- **Le chiffré ne se révoque pas.** Retirer un destinataire ne protège que les *futurs* fichiers ; le passé reste lisible par qui a gardé la clé. La rotation d'un secret, c'est changer la valeur **et** la propager, à la main.
- **Métadonnées en clair** : les noms de clés et la structure du fichier restent lisibles. Un nom de clé qui dit `mot_de_passe_prod_client_x` en dit déjà trop.
- Quatre avis publiés le 2026-08-14, aucun critique : le haut ci-dessus, deux modérés (fuite de mémoire sur des fichiers INI ou ENV non fiables, traversée de chemin dans `sops exec-file --filename`) et un faible.
- Le projet a cinq mainteneurs cités (dont Hidde Beydals et Andrew Block) ; le nombre de contributeurs n'a pas été relevé.

## Écosystème

### Alternatives

- [[OpenBao]] — Serveur de secrets sous MPL-2.0, fork communautaire de HashiCorp Vault (LF Edge puis OpenSSF, Go) : coffre clé-valeur, secrets dynamiques de bases de données, PKI, Transit, scellement Shamir ou auto-unseal, Raft intégré — sans fonction gardée en payant, mais qui diverge volontairement de Vault et ne corrige que sa dernière version. — un service qui distribue, journalise et révoque contre un fichier qui se versionne sans serveur.

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — les manifestes Secret peuvent être chiffrés dans Git avec SOPS puis déchiffrés dans le cluster par Flux.

## Ressources

- Documentation — https://getsops.io/docs/
- Dépôt — https://github.com/getsops/sops
- Documentation — sécurité et modèle de chiffrement : https://getsops.io/docs/security/
- Documentation — identités age : https://getsops.io/docs/usage/identities/age/
- Documentation — avis de sécurité : https://github.com/getsops/sops/security/advisories
- Tutoriel — SOPS avec Flux : https://fluxcd.io/flux/guides/mozilla-sops/
- Documentation — gestion des secrets avec Argo CD : https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/
- Dépôt — age, l'outil de chiffrement dont SOPS reprend les clés : https://github.com/FiloSottile/age

## Voir aussi

- [[Sécurité]] — le hub du domaine
- [[Gestion des secrets]] — la notion : ce qu'il ne faut pas faire, coffre contre chiffrement de fichiers, rotation, bootstrap du premier secret
