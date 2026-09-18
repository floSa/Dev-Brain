---
role: notion
nom: Supply chain logicielle et SBOM
alias: [sbom, software bill of materials, supply chain logicielle, chaîne d'approvisionnement logicielle, vex, cyclonedx, spdx, nomenclature logicielle, provenance]
categorie: security/analyse
domaines: [infra-ops, mlops]
tags: [sbom, supply-chain, vulnerability-scanning]
---

# Supply chain logicielle et SBOM

## Aperçu

- Un **SBOM** (*Software Bill of Materials*) est la liste des composants qu'un logiciel contient, avec leurs versions et leurs relations de dépendance. La définition de la NTIA (2021) : « un enregistrement formel contenant le détail et les relations de chaîne d'approvisionnement des composants utilisés pour construire un logiciel ». Il répond à une seule question — *qu'y a-t-il dedans ?* — et c'est ce qui permet de répondre à la suivante : *cette faille m'atteint-elle ?*
- Quand on livre une image Docker ou un paquet Python à un client, on livre aussi, sans le savoir, des centaines de composants qu'on n'a pas écrits. Sur site, sans accès internet, le client ne peut pas le vérifier seul : c'est à celui qui livre de dire ce qu'il y a dedans. Trois choses à ne pas confondre : le SBOM dit **ce que contient** l'artefact ; la **signature** dit **qui** l'a publié ; la **provenance** dit **comment** il a été construit.

## Concepts clés

### Ce qu'un SBOM doit contenir

- La NTIA fixait en 2021 sept champs minimaux (fournisseur, nom, version, autres identifiants, relation de dépendance, auteur du SBOM, horodatage). La **version 2026 des éléments minimaux de la CISA** (publiée le 2026-07-29, cosignée par la NSA, le FBI, l'ANSSI, le BSI et d'autres autorités) **remplace** ce texte et compte **17 champs** à la lecture de son tableau (Appendice A) : elle y ajoute notamment la valeur et l'algorithme de hachage de chaque composant, la licence, la signature de l'auteur du SBOM, le nom et la version du format, le nom et la version de l'outil, la version du SBOM et le **contexte de génération**. Le « fournisseur » devient le « producteur du composant », terme jugé moins ambigu.
- **Couverture** : tous les composants, dépendances transitives comprises, « sans profondeur minimale ». Un destinataire doit pouvoir conclure qu'une faille ne le touche pas si le composant concerné n'est pas listé.
- **Le type de SBOM compte autant que le contenu.** La CISA (2023) distingue six moments : conception, source, build, analysé (après coup, sur l'artefact), déployé, exécution. Un SBOM « analysé » repose sur des heuristiques et peut omettre ; un SBOM « build », produit pendant la construction, est plus fiable mais capte mal les dépendances indirectes ou dynamiques ; un SBOM « source » peut lister des composants qui ne tournent jamais ou sont compilés ailleurs. Le texte 2026 reprend l'idée avec le champ *contexte de génération* : « avant build », « build », « après build ».

### CycloneDX contre SPDX

- **CycloneDX** naît à l'OWASP et devient la norme **Ecma-424** : la version 1.6 en est la première édition (juin 2024), la **1.7 (2025-10-21)** la deuxième (décembre 2025). JSON, XML et protobuf ; au-delà du SBOM logiciel, il couvre le SaaS, le matériel, l'apprentissage automatique, la cryptographie, le VEX et les attestations.
- **SPDX**, projet de la Linux Foundation, est la norme **ISO/IEC 5962:2021** (c'est SPDX 2.2.1). **SPDX 3.0** est paru le 2024-04-15, la **3.0.1** le 2024-12-17, avec des *profils* (Core, Software, Security, Licensing, Build, AI, Dataset, Lite…) et JSON-LD comme sérialisation recommandée ; la 3.1 n'était qu'en première version candidate (janvier 2026) à la date de relevé, sans version finale trouvée.
- **Ce que les sources disent de la différence** : pour la NTIA (2021), SPDX vient de la communauté de la conformité de licences, CycloneDX d'un contexte de sécurité et d'analyse de composants, et les champs ne se projettent pas tous d'un format à l'autre. En pratique, un outil qui lit l'un ne lit pas toujours l'autre : Dependency-Track n'ingère que du CycloneDX, Trivy et Grype lisent les deux. **Pas de tranche ici** : le CRA cite les deux comme formats courants.

### VEX : dire qu'une faille ne vous touche pas

- Un scanner liste toutes les failles connues d'un composant, atteignables ou non. Le **VEX** (*Vulnerability Exploitability eXchange*) est la réponse du fournisseur, déclaration par déclaration : pour cette CVE et ce produit, le statut est `not_affected`, `affected`, `fixed` ou `under_investigation` (définition CISA, 2023). Un `not_affected` porte une justification : composant absent, code vulnérable absent, code vulnérable hors du chemin d'exécution, non contrôlable par un attaquant, atténuation déjà en place.
- **Trois formats** : **OpenVEX** (spécification 0.2.0, étiquetée « draft » dans son dépôt), le **VEX de CycloneDX** (états `exploitable`, `in_triage`, `false_positive`, `not_affected`, `resolved`…), et le profil **CSAF VEX** (CSAF 2.0 est une norme OASIS, puis ISO/IEC 20153 depuis 2025-05-20).
- **Côté outils** : Trivy lit les trois (`--vex`, fonction expérimentale ; le VEX CycloneDX seulement en scan de SBOM) ; Grype lit OpenVEX et CSAF, et un `not_affected` ou `fixed` fait disparaître le résultat par défaut ; Dependency-Track importe et exporte du VEX CycloneDX.
- **Le chiffre qui motive** : sur 2 414 dépôts open source, des scanners produisent **92,0 % de faux positifs**, surtout du code non atteignable, et une analyse d'appels de fonctions en élimine 61,9 % (Zhou, Dacier et Konstantinou, arXiv 2511.20313, révisé en avril 2026). Un VEX est un format de communication, pas un moteur d'analyse : l'effort passe du destinataire à l'auteur.

### Signature et provenance

- **Sigstore** : *cosign* signe et vérifie, *Fulcio* délivre un certificat de courte durée lié à une identité OIDC, *Rekor* est un journal de transparence en ajout seul. Un *bundle* Sigstore embarque certificat, entrées de journal et horodatages, ce qui permet de vérifier sans réseau.
- **SLSA** (v1.2, 2025-11-24) : quatre niveaux de la piste Build, de L0 (aucune garantie) à L3 (builds durcis), L1 demandant seulement qu'une provenance existe et L2 qu'elle soit **signée** par la plateforme. **in-toto** fournit le format de l'attestation (un énoncé signé sur un artefact). Les *Artifact Attestations* de GitHub produisent du niveau L2, L3 avec des workflows réutilisables.
- **PyPI** : les attestations numériques (PEP 740, statut *Final*) sont disponibles depuis 2024-11-14, pour les éditeurs de confiance GitHub Actions, GitLab et Google Cloud. Que `pip` les vérifie à l'installation n'a pas été trouvé.
- **Hors ligne** : la documentation de cosign décrit `cosign initialize` avec `--mirror` et `--root` pour partir d'un dépôt TUF local ou d'une instance privée. À tester sur le site cible, pas à supposer.

### Scanner une image, scanner des dépendances

- **Un scan de dépendances** (sur un dépôt) lit ce que le projet *déclare* : `requirements.txt`, `uv.lock`, `poetry.lock`, `package-lock.json`. Il voit ce qui n'est pas encore installé et les dépendances transitives résolues par le verrou ; il ne voit ni l'OS, ni ce qu'un `apt install` ajoutera dans l'image.
- **Un scan d'image** lit ce qui est *installé* dans les couches : paquets d'OS et paquets de langage avec leurs métadonnées (`dist-info`, `egg-info` pour Python). Syft, sur une image, ne lance que les analyseurs « installés » : les fichiers d'intention ne donnent presque jamais la version exacte. Par défaut il lit la vue aplatie : un fichier effacé dans une couche ancienne n'apparaît pas (`--scope all-layers` le garde).
- **Les deux ne se remplacent pas.** Le premier répond « que mettons-nous dans l'image ? » avant le build ; le second « que contient ce que nous livrons ? » après. Trivy et Grype font les deux ; `pip-audit` (PyPA, sans fiche ici) audite un environnement Python ou un fichier de dépendances, avec une résolution à part.

### Ce qu'un scanner ne voit pas

- **Les composants sans métadonnées** : binaires copiés à la main, bibliothèques C++ compilées depuis les sources, code « vendoré » — Anchore écrit que le code compilé depuis les sources ne peut pas être détecté de façon fiable, et que les modules chargés à l'exécution échappent à l'analyse statique. Pour Go, Trivy lit les modules embarqués dans le binaire mais ne dit pas si la fonction vulnérable est appelée (`govulncheck` fait cette analyse d'atteignabilité).
- **Les correctifs rétroportés** : Debian corrige dans la version livrée sans en changer le numéro amont ; comparer un numéro à la base du NVD produit un faux positif. Trivy privilégie donc les avis des distributions pour les paquets d'OS ; les correspondances par CPE de Grype sont à vérifier avant d'agir.
- **Les failles sans correctif, ou sans CVE** : Grype affiche « won't fix » ou laisse la colonne du correctif vide ; OSV agrège des avis d'écosystème (GitHub, PyPA, RustSec) qui n'ont pas tous un identifiant CVE. Le NIST a adopté en avril 2026 une priorisation de l'enrichissement du NVD : les CVE hors critères restent listées mais sont de priorité minimale.
- **Les SBOM eux-mêmes divergent.** Trois générateurs sur plus de 3 000 projets JavaScript et Rust divergent en couverture et en complétude, à cause d'ambiguïtés des spécifications (Prado, Zendra, Boinot, Barais, arXiv 2609.19920, 2026-09-17). Six outils sur 55 444 SBOM et 3 287 dépôts détectent les mêmes paquets dans 7,84 % à 12,77 % des cas selon le langage (Wang et al., arXiv 2601.05622, 2026-01-09). Sur 78 612 SBOM trouvés dans la nature, 52,9 % ne déclarent aucune relation de dépendance (Zięba-Kozarzewski, arXiv 2607.22140, 2026-07).

### Exécuter hors ligne

- Le schéma tient en quatre lignes : le **SBOM se génère sans réseau** (Syft, Trivy) ; la **base de vulnérabilités est une donnée** qu'on télécharge ailleurs et qu'on met en miroir ; la **correspondance SBOM contre base est locale** ; la **réévaluation** d'un SBOM déjà livré demande de rafraîchir la base, à la fréquence qu'on s'impose.
- **Trivy** : télécharger les artefacts OCI de la base avec ORAS ou un registre interne, puis `--skip-db-update`, `--skip-java-db-update`, `--offline-scan` ; aucun âge maximal de base trouvé. **Grype** : `grype db import` d'une archive ; **le scan échoue si la base a plus de 120 heures** (5 jours) par défaut. **Dependency-Track v5** : l'analyseur interne ne fait aucun appel sortant, NVD et OSV se servent depuis des miroirs HTTP internes, GitHub Advisories ne se mire pas ; la page de documentation est déclarée inachevée. **pip-audit** : aucun mode hors ligne documenté.
- **Conséquence pour un site isolé** : la fraîcheur de la base devient un réglage et un engagement (« la base de telle date »), pas un détail technique.

### Pourquoi un client industriel le demande

- Le **règlement européen sur la cyber-résilience (CRA, règlement (UE) 2024/2847)** est entré en vigueur le **2024-12-10** ; les obligations de déclaration s'appliquent à partir du **2026-09-11**, les obligations principales à partir du **2027-12-11** (page de la Commission). L'annexe I, partie II, point 1, exige de documenter les composants, « y compris en établissant une nomenclature logicielle dans un format couramment utilisé et lisible par machine, couvrant au moins les dépendances de premier niveau » (texte du règlement tel que relayé par eucybersecurity.org ; la version EUR-Lex n'a pas pu être ouverte ici). Le SBOM n'a pas à être public : il se tient à la disposition des autorités de surveillance du marché sur demande motivée.
- **IEC 62443** : un webinaire d'exida de 2023 note que la norme n'exige pas explicitement de SBOM ni n'en recommande un format ; 62443-4-1 exige en revanche de gérer les risques des composants tiers. Source secondaire : à reconfirmer auprès du client.

## En pratique

- **Livrer une image** : générer le SBOM à la construction (contexte « build »), le joindre à l'image, le signer ; scanner l'image livrée **et** le SBOM avec deux scanners de sources différentes, parce que leurs listes divergent.
- **Suivre ce qu'on a livré** : envoyer chaque SBOM à un serveur qui réévalue en continu — [[Dependency-Track]] — plutôt que de relancer un scan d'image par client.
- **Garder la preuve d'une date** : la base qui a servi à un scan fait partie du résultat ; noter sa date avec lui.
- **Traiter un scanner comme une dépendance.** Un scanner s'exécute avec les secrets du pipeline ; en mars 2026, la chaîne de publication de [[Trivy]] a été compromise (binaire, tags de `trivy-action`, images Docker Hub), un an après l'affaire `tj-actions/changed-files` de mars 2025 (CVE-2025-30066) : épingler les actions par SHA, vérifier les binaires, garder un miroir interne des versions validées.

## Approches voisines & alternatives

- [[Trivy]] — image, dépôt, secrets, IaC, SBOM en une commande ; [[Grype]] — la comparaison de SBOM à une base, avec Syft en amont ; [[Dependency-Track]] — le suivi dans la durée ; [[Gitleaks]] — les secrets en dur dans l'historique ; [[Semgrep]] — le code lui-même.
- **OSV-Scanner** (Google, Apache-2.0) lit entre autres `uv.lock` et `pylock.toml` et dispose d'un mode hors ligne (`--offline`, bases téléchargeables) : le candidat le plus direct pour un site isolé côté dépendances Python, sans fiche ici.
- **GUAC** (OpenSSF, Kusari et Google) agrège SBOM, VEX et attestations dans un graphe ; **DefectDojo** (OWASP) centralise des résultats de scanners ; ni l'un ni l'autre n'a de fiche.
- [[Gestion des secrets]] — la notion voisine : où ranger un secret une fois qu'un scanner en a trouvé un.

## Pour aller plus loin

- CISA et partenaires — 2026 Minimum Elements for a SBOM (2026-07-29) : https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
- NTIA — The Minimum Elements For a SBOM (2021-07-12) : https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
- CISA — Types of SBOM (2023-04) : https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
- CISA — Minimum Requirements for VEX (2023-04) : https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf
- CycloneDX — v1.7 et Ecma-424 : https://cyclonedx.org/news/cyclonedx-v1.7-released
- SPDX — spécifications : https://spdx.dev/use/specifications/
- OpenVEX — spécification : https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md
- Sigstore — vue d'ensemble : https://docs.sigstore.dev/about/overview/
- SLSA — spécification v1.2 : https://slsa.dev/spec/
- PEP 740 — attestations d'index : https://peps.python.org/pep-0740/
- Commission européenne — Cyber Resilience Act : https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Zhou, Dacier, Konstantinou — A Reality Check on SBOM-based Vulnerability Management, 2025-11 (révisé 2026-04) : https://arxiv.org/abs/2511.20313
- Wang et al. — A Large Scale Empirical Analysis on the Adherence Gap between Standards and Tools in SBOM, 2026-01 : https://arxiv.org/abs/2601.05622
- Zięba-Kozarzewski — No Edges, No Verdict, 2026-07 : https://arxiv.org/abs/2607.22140
- Prado, Zendra, Boinot, Barais — Mind the Gap: How SBOM Specification Ambiguities Lead to Divergent SBOMs, 2026-09 : https://arxiv.org/abs/2609.19920
- Trivy — avis de l'incident de mars 2026 : https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23
