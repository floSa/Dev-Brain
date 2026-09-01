# Rapport d'audit — Axe 4 : Fraîcheur & véracité

Auditeur : conversation « audit axe 4 », le 2026-09-02. Socle : `mesures-axe4.md`
relancé le 2026-09-02, **identique octet pour octet** à `mesures-2026-09-02.md`
(`diff` sans sortie). Aucun écart de chiffre à signaler entre le brief et le vault.
Une réserve porte sur le *libellé* d'un compteur, pas sur sa valeur (cf. C7).

Échantillon : 30 fiches Dev tirées avec `random.seed(20260902)` sur les 336 fiches
`type: service|outil` de `Dev/`, triées par chemin avant tirage — le tirage est
reproductible (script en annexe C). 28 des 30 portent un `url_repo`, tous sur
`github.com` ; 58 URL et 26 dépôts distincts ont été interrogés en ligne.

## Synthèse

Le brain n'est pas truffé de faux : 26 dépôts sur 26 existent, 58 URL sur 58
répondent, et **aucune licence n'est mal classée** — y compris sur trois cas subtils.
Le pourrissement se concentre ailleurs : **4 fiches sur 30 portent au moins un fait
périmé, dont 3 orienteraient un choix de brique dans la mauvaise direction**, soit
34 fiches sur 336 (IC95 [12 ; 86]). Le mécanisme est toujours le même : le **corps
de page sait** que le projet décline, et le **frontmatter dit `actif` / `production`**.
La seule chose à faire si l'on n'en fait qu'une : écrire le script de re-vérification
GitHub (annexe B, ~120 lignes, effort S) — il détecte à froid, sans lecture humaine,
les trois défauts sérieux trouvés dans l'échantillon.

## Constats

### C1. Taux d'erreur mesuré : 4 fiches sur 30, dont 3 défauts décisionnels — gravité : sérieux

- **Constat** : sur les 30 fiches échantillonnées, 4 portent au moins un fait faux
  aujourd'hui. Trois de ces défauts sont *décisionnels* — lus tels quels, ils
  orientent un choix de brique dans la mauvaise direction :
  - `fastmcp` — le corps affirme « **FastMCP 2.0** est la version activement
    développée ». La 3.x est la série stable et la 4.0 est publiée sur PyPI
    (`4.0.1`, 2026-09-02). La page a **deux majeures de retard**, et tout son
    argumentaire (« va bien au-delà du protocole de base ») est ancré sur la 2.0.
  - `hydra` — le `pitch:` (seul champ indexé) attribue le projet à « **(Meta)** » et
    le corps dit « développé par **Meta** (Facebook Research) ». Meta a cédé le
    dépôt à l'organisation communautaire `hydra-ecosystem` (« Hydra's next chapter:
    independent stewardship »). L'attribution indexée est périmée.
  - `TF-Agents` — `status: actif` et `maturite: production`, alors que la dernière
    release stable date du **2023-12-14** (`0.19.0`) et le dernier push du
    **2026-01-16** (229 jours). Le corps de la fiche dit pourtant, deux sections
    plus bas, « Maintenance en **déclin** ».
  Trois défauts mineurs s'y ajoutent : `url_repo` périmé sur `fastmcp` et `hydra`
  (les deux dépôts ont été transférés, la redirection GitHub sauve l'URL pour
  l'instant) et `url_docs` de `DataGrip` qui répond 200 mais atterrit sur une page
  marketing (cf. C8).
- **Preuve** :
  ```
  $ curl -s https://pypi.org/pypi/fastmcp/json | jq -r .info.version
  4.0.1
  $ curl -sL -o /dev/null -w "%{url_effective}\n" https://github.com/jlowin/fastmcp
  https://github.com/PrefectHQ/fastmcp
  $ curl -sL -o /dev/null -w "%{url_effective}\n" https://github.com/facebookresearch/hydra
  https://github.com/hydra-ecosystem/hydra
  $ curl -s https://pypi.org/pypi/tf-agents/json | jq -r '.info.version'
  0.19.0                        # upload_time 2023-12-14
  $ curl -s https://api.github.com/repos/tensorflow/agents | jq -r .pushed_at
  2026-01-16T...                # 229 jours
  ```
  Tableau complet des 30 fiches en annexe A.
- **Portée** : 4/30 = 13,3 % (IC95 Wilson [5,3 ; 29,7]) → **45 fiches sur 336**,
  IC [18 ; 100]. Défauts décisionnels seuls : 3/30 = 10,0 % (IC95 [3,5 ; 25,6]) →
  **34 fiches**, IC [12 ; 86]. L'intervalle est large : n = 30 fixe le plancher de
  précision, il faudrait n = 100 pour resserrer sous ±10 points.
- **Cause** : trois faits différents pourrissent par trois canaux distincts — une
  release amont (version), un transfert de propriété du dépôt (attribution + URL),
  une inactivité progressive (status). Aucun des trois n'émet de signal dans le
  vault : rien ne relit le dépôt après l'écriture de la fiche.
- **Recommandation** : implémenter le script de re-vérification spécifié en annexe B,
  et le passer sur les 316 fiches dont l'`url_repo` est de forme
  `github.com/owner/repo`. Les trois défauts sérieux de l'échantillon sont détectés
  par ce seul script : `pushed_at` ancien (TF-Agents), `full_name` différent du slug
  déclaré (fastmcp, hydra). La version amont n'est pas dans l'API dépôt : la lire
  sur PyPI pour les 4 fiches concernées (cf. C6).
- **Effort** : **S** (< 1 h) pour le script + une passe de lecture des signalements.
  Fichiers impactés : création de `AI/scripts/verifier_fraicheur.py` et de
  `AI/index/fraicheur.json`. Aucune page du vault touchée par le script lui-même.

### C2. Le corps sait, le frontmatter ne sait pas : 5 fiches contredisent leur propre `status:` — gravité : sérieux

- **Constat** : cinq fiches déclarent `status: actif` et `maturite: production`
  (ou vide) alors que leur propre corps, dans `## Pièges` ou
  `## Déploiement & coût`, décrit un projet dormant. `status:` et `maturite:` sont
  les champs sur lesquels un agent filtre ; ils affirment le contraire de la prose.

  | Fiche | frontmatter | ce que dit son propre corps | vérifié en ligne |
  |---|---|---|---|
  | `Acme` | actif / production | « dernière release en 2022 » | `dm-acme 0.4.0`, 2022-02-10 |
  | `TF-Agents` | actif / production | « Maintenance en **déclin** » | `tf-agents 0.19.0`, 2023-12-14 |
  | `pytorch-crf` | actif / production | « **Très dormant** : dernière release en 2019 » | `pytorch-crf 0.7.2`, 2019-02-04 |
  | `rank-bm25` | actif / production | « **Dormant** : dernière release en 2022 » | `rank-bm25 0.2.2`, 2022-02-16 |
  | `OpenCut` | actif / production | « la version *classic* (archivée, plus maintenue) est celle qui sert le site public » | — |

  Deux détections supplémentaires sont des faux positifs assumés : `HuggingFace` et
  `selectolax` parlent du déclin d'un **sous-composant** (backend TF, moteur Modest),
  pas du projet.
- **Preuve** : `uv run` du détecteur reproduit en annexe C §2. Il restreint la
  recherche aux sections qui parlent du sujet (`## Pourquoi`,
  `## Déploiement & coût`, `## Pièges`) et **jette toute ligne citant une autre fiche
  `[[Dev/…]]`** — sans ce filtre, la détection remonte 37 fiches, dont 30 ne font que
  réafficher le pitch d'un voisin mort dans leur section `## Alternatives`.
  ```
  Acme        [## Pièges] - **Maintenance très ralentie** : dernière release en 2022…
  TF-Agents   [## Déploiement & coût] - Maintenance en **déclin** : dernière release stable fin 2023…
  pytorch-crf [## Pièges] - **Très dormant** : dernière release en 2019…
  rank-bm25   [## Pièges] - **Dormant** : dernière release en 2022…
  -> 7 fiche(s) 'actif'/'production' dont le corps decrit son propre declin
  ```
- **Portée** : 5 fiches sur 336 confirmées. C'est la classe d'erreur la plus coûteuse
  du vault, parce qu'elle est **invisible au consommateur machine** : la prose qui
  contient l'avertissement n'est pas indexée (cf. C3).
- **Cause** : `status:` a été rempli au moment de l'écriture par défaut sur `actif`
  (« le projet existe et le code marche ») pendant que l'auteur écrivait dans le
  corps ce qu'il venait de constater sur le dépôt. L'énum `status` ne propose que
  `actif` / `en-eval` / `abandonne` : il n'existe **aucune valeur pour « vivant mais
  dormant »**, donc le rédacteur a choisi `actif` faute de mieux. Le déclin est un
  état intermédiaire que le vocabulaire ne sait pas dire.
- **Recommandation** : deux gestes, dans cet ordre.
  1. Ajouter la valeur **`dormant`** à l'énum `status` (`AI/scripts/check_brain.py:59`)
     et la documenter dans `Documentation/general/taxonomie.md` : « le code
     fonctionne, l'amont ne bouge plus — utilisable, pas à parier dessus ».
     Requalifier les 5 fiches ci-dessus.
  2. Ajouter au script de l'annexe B une règle de **cohérence corps / frontmatter** :
     signaler toute fiche `actif` dont le corps contient le lexique du déclin, hors
     lignes citant une autre fiche. C'est le détecteur de l'annexe C §2, 25 lignes,
     et il tourne **sans réseau**.
- **Effort** : **S** pour la règle du validateur et le détecteur ; **S** pour les
  5 requalifications (décision humaine, une ligne chacune). Fichiers impactés :
  `AI/scripts/check_brain.py`, `Documentation/general/taxonomie.md`,
  `Templates/Service-Dev.md`, et 5 fiches de `Dev/Services` — hors périmètre de cet
  auditeur, à faire côté correcteur.

### C3. Aucun fait périssable n'atteint le consommateur machine — gravité : sérieux

- **Constat** : `AI/index/brain-index.json` — le fichier que `planifier-projet`
  interroge pour proposer des briques — n'expose **aucun** des champs périssables.
  Ni `status`, ni `maturite`, ni `licence_type`, ni `url_repo`, ni `remplace_par`.
  Un agent qui choisit une brique depuis l'index ne peut pas écarter les fiches
  `status: abandonne` : l'information n'est pas là.
- **Preuve** :
  ```
  $ python3 -c "import json; d=json.load(open('AI/index/brain-index.json'));
    print(sorted({k for p in d['pages'] for k in p}))"
  ['alias','alternatives','categorie','domaines','galaxie','nom','path','pitch','tags','type']
  $ … pour f in (status, maturite, licence_type, hosted, scaling, url_repo, url_docs, remplace_par):
    status present dans 0 pages   maturite present dans 0 pages   licence_type present dans 0 pages
    hosted present dans 0 pages   scaling  present dans 0 pages   url_repo     present dans 0 pages
    url_docs present dans 0 pages remplace_par present dans 0 pages
  ```
- **Portée** : 647 pages indexées, dont les 336 fiches Dev et les 10 fiches
  non-actives. C'est ce constat qui rend C1 et C2 coûteux plutôt que cosmétiques :
  un fait faux dans un champ non indexé nuit à un lecteur humain ; un fait faux dans
  un champ indexé nuit à une décision automatisée.
- **Cause** : `build_index.py` projette les champs de **navigation** (comment
  trouver une page) et pas ceux de **jugement** (faut-il la retenir). La distinction
  n'a jamais été explicitée.
- **Recommandation** : ajouter `status`, `maturite` et `licence_type` à la projection
  de `build_index.py`. Trois champs, courts, énumérés — le coût en taille d'index est
  négligeable et ils rendent le filtrage possible côté `planifier-projet`. Ne **pas**
  ajouter `url_repo` / `url_docs` : ce sont des données de vérification, elles vont
  dans le side-car de C7, pas dans l'index de navigation.
- **Effort** : **S** (une liste de champs à étendre + une régénération). Fichiers
  impactés : `AI/scripts/build_index.py`, `AI/index/brain-index.json` (régénéré),
  et le prompt de `.claude/skills/planifier-projet/` pour qu'il exploite le filtre.
  Recoupe l'axe 5 (navigation) : à arbitrer là si le propriétaire préfère.

### C4. `remplace_par: []` sur 297 fiches sur 297 — gravité : sérieux

- **Constat** : le champ `remplace_par:` existe dans le gabarit service, est validé
  par `check_brain`, et est **vide sur la totalité des fiches** — y compris sur les
  5 fiches `status: abandonne`, c'est-à-dire exactement là où il est censé répondre
  à la seule question qui compte face à une brique morte : par quoi je la remplace ?
- **Preuve** :
  ```
  $ grep -rh "^remplace_par:" Dev/ | sort | uniq -c
      297 remplace_par: []
  $ … fiches abandonnees sans remplace_par : osint4all, Marqo, Neptune, TorchServe, Vanna  -> 5
  ```
- **Portée** : 297 fiches portent le champ, 297 l'ont vide. 5 fiches en auraient un
  usage immédiat.
- **Cause** : champ ajouté au gabarit par symétrie avec `alternatives:`, jamais
  intégré à une étape de rédaction. Rien ne le demande, rien ne le vérifie, personne
  ne le lit — il n'est même pas indexé (C3).
- **Recommandation** : trancher entre deux issues, pas trois. **Soit** le remplir sur
  les seules fiches non-actives et faire de « `status != actif` ⇒ `remplace_par`
  non vide » une règle dure de `check_brain` — le champ prend alors un sens et se
  maintient tout seul. **Soit** le retirer du gabarit : un champ vide à 100 % est un
  champ que le validateur fait semblant de contrôler. Ne pas le laisser en l'état.
- **Effort** : **S** pour la première issue (5 fiches à remplir + une règle de
  ~8 lignes) ; **S** pour la seconde (retrait dans `SERVICE_ALLOWED` + 297 fiches
  éditées par script). Fichiers impactés : `AI/scripts/check_brain.py:47-50`,
  `Templates/Service-Dev.md`, `Documentation/general/taxonomie.md`, et 5 ou 297
  fiches selon l'issue.

### C5. Deux contradictions internes entre `status` et `maturite`, non détectées — gravité : mineur

- **Constat** : `AutoGen` porte `status: actif` **et** `maturite: deprecated`.
  `Vanna` porte `status: abandonne` **et** `maturite: production`. Les deux couples
  sont logiquement incompatibles et passent `check_brain` sans un mot, parce que le
  validateur contrôle chaque énum isolément et jamais les combinaisons.
- **Preuve** :
  ```
  == B. contradictions internes frontmatter
    AutoGen     status=actif / maturite=deprecated
    Vanna       status=abandonne / maturite=production
    -> 2 fiche(s)
  ```
  (détecteur en annexe C §2). Les deux `pitch:` sont pourtant justes : AutoGen
  « en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework) », Vanna
  « OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé) ». C'est le frontmatter
  qui est incohérent, pas la connaissance.
- **Portée** : 2 fiches sur 336. Faible, mais le coût de détection est quasi nul.
- **Cause** : `VALUE_ENUMS` valide des valeurs, pas des couples. Deux champs qui
  disent la même chose sous deux angles finissent par divorcer.
- **Recommandation** : une règle de croisement dans `check_brain` :
  `maturite: deprecated` ⇒ `status` ∈ {`abandonne`, `dormant`} ; `status: abandonne`
  ⇒ `maturite` ∈ {`deprecated`}. Six lignes. À écrire en même temps que la valeur
  `dormant` de C2, sinon la règle bloquera les fiches légitimement dormantes.
- **Effort** : **S**. Fichiers impactés : `AI/scripts/check_brain.py`, 2 fiches de
  `Dev/Services`.

### C6. Le socle surestime d'un facteur 2 l'exposition « version » — gravité : mineur

- **Constat** : `mesures-axe4.md` §9 annonce « mentionne un numéro de version :
  **214** ». Le compteur emploie la regex `\bv?\d+\.\d+(\.\d+)?\b`, qui capture
  `Apache-2.0`, `GPL-2.0`, `BSD-3-Clause`, `CC0-1.0` et `Python ≥ 3.10`. Après
  retrait des identifiants de licence SPDX et des exigences de version Python,
  l'exposition réelle tombe à **108** fiches. **106 des 214 sont des faux positifs.**
- **Preuve** :
  ```
  $ uv run vregex.py
  fiches Dev (Dev/ seul)                         : 336
  regex audit_mesures actuelle                   : 214
  apres retrait des licences SPDX et 'Python 3.x': 108
  faux positifs elimines                         : 106
  exemples de faux positifs : Excalidraw, Figma, FossFLOW, Graphify, Maka, Mermaid,
                              Penpot, Sniffnet, Spec Kit, draw.io, osint4all, Agno
  ```
  Script en annexe C §3.
- **Portée** : un chiffre du socle, repris tel quel par le brief de cet axe.
  Conséquence : la surface de pourrissement « version » a été surévaluée du double
  dans le diagnostic d'ouverture du chantier.
- **Cause** : la convention de nommage SPDX (`Apache-2.0`) est syntaxiquement
  indistinguable d'un numéro de version pour une regex naïve. Le compteur n'a jamais
  été relu contre un échantillon de ce qu'il capture.
- **Recommandation** : filtrer les identifiants SPDX et le motif `Python ≥ 3.x` avant
  de compter, dans `audit_mesures.py` §9. Le compteur est un instrument d'audit :
  s'il se trompe, tous les axes héritent de l'erreur.
- **Effort** : **S** (deux regex de retrait, ~6 lignes). Fichier impacté :
  `AI/scripts/audit_mesures.py`. Le fichier est autorisé en écriture pour le
  correcteur, pas pour cet auditeur.

### C7. Aucun horodatage : l'âge d'un fait n'est lisible nulle part — gravité : sérieux

- **Constat** : aucun des 336 frontmatters ne porte de date, ni de rédaction, ni de
  vérification. `SERVICE_ALLOWED` (`check_brain.py:47-50`) interdit tout champ hors
  liste, et aucune date n'y figure. `brain-index.json` n'en porte pas davantage.
  Conséquence directe : **il est impossible, sans `git log`, de dire laquelle de deux
  fiches a été vérifiée le plus récemment** — et `git log` n'est pas accessible à
  l'agent qui lit le brain depuis un projet. Une fiche exacte au jour près (`Neptune`,
  `DataGrip` — cf. « Ce qui va bien ») et une fiche de deux ans et demi de retard
  (`TF-Agents`) sont, pour un lecteur, strictement indiscernables.
- **Preuve** :
  ```
  $ sed -n '47,50p' AI/scripts/check_brain.py
  SERVICE_ALLOWED = {"galaxie", "type", "nom", "alias", "pitch", "categorie",
                     "licence_type", "hosted", "maturite", "langage", "scaling",
                     "alternatives", "remplace_par", "status", "tags",
                     …}          # aucun champ de date
  $ grep -c "^V1_MARKERS" AI/scripts/check_brain.py   # 'created'/'modified' sont
  1                                                    # marqués v1 et rejetés
  ```
  Note de mesure adjacente : le compteur « fiches Dev : **337** » du socle inclut
  `Wiki/Outils/Obsidian.md` (`galaxie: wiki`, `type: outil`), parce que §9 filtre sur
  `type` sans filtrer sur le répertoire. Les fiches réellement dans `Dev/` sont
  **336**. La valeur du compteur est celle du brief — l'écart est un libellé, pas un
  chiffre — mais toutes les extrapolations de ce rapport sont faites sur 336.
- **Portée** : 336 fiches. Répond à la question 4 du brief.
- **Cause** : le gabarit v2 a délibérément banni les dates de v1 (`created`,
  `modified` sont dans `V1_MARKERS` et rejetés), pour éviter le bruit de métadonnées
  Obsidian. La décision était bonne pour les dates de *fichier* ; elle a emporté avec
  elle la date de *vérification*, qui est une donnée différente.
- **Recommandation** : **ne pas** ajouter `verifie_le:` aux 336 fiches. Le coût est
  réel (un champ de plus à maintenir sur 336 pages, `SERVICE_ALLOWED` + trois
  gabarits à modifier, et un champ qu'une session pressée laissera pourrir comme
  `remplace_par` l'a été — C4 est le précédent). Écrire à la place un **side-car
  généré**, `AI/index/fraicheur.json`, clé = chemin de page, produit par le script de
  l'annexe B :
  ```json
  { "Dev/Services/TF-Agents.md": {
      "sonde_le": "2026-09-02", "repo": "tensorflow/agents",
      "pushed_at": "2026-01-16", "archived": false,
      "license_spdx": "Apache-2.0", "stars": 3026,
      "signalements": ["push_ancien:229j", "corps_declin_vs_status_actif"] } }
  ```
  Trois raisons de préférer le side-car au champ : (a) zéro page modifiée, zéro
  gabarit modifié, zéro règle de validateur touchée ; (b) `AI/index/` est déjà
  déclaré « généré, ne pas éditer à la main » — la donnée y est chez elle ; (c) une
  date **sondée par machine** et une date **vérifiée par un humain** ne sont pas la
  même information, et les fondre dans un champ unique produirait un faux sentiment
  de relecture. Si le propriétaire veut tout de même tracer la relecture humaine,
  qu'elle soit portée par la seule fiche où elle a eu lieu, sous forme d'une ligne
  datée dans `## Pièges` — pas par un champ obligatoire sur 336 pages.
- **Effort** : **S** pour le side-car (il tombe du script de l'annexe B, aucun coût
  marginal). Pour comparaison, l'option `verifie_le:` est **M** : `check_brain.py`,
  `Templates/Service-Dev.md`, `Templates/Concept-Wiki.md`,
  `Documentation/general/taxonomie.md`, plus une passe d'initialisation sur 336
  fiches — et les 40 fiches `type: outil` n'ont aucun gabarit où l'ajouter
  (`Templates/` n'en contient pas ; hors périmètre de cet axe). Fichiers impactés
  par la recommandation retenue :
  `AI/scripts/verifier_fraicheur.py` (création), `AI/index/fraicheur.json` (généré).

### C8. Une URL qui répond 200 n'est pas une URL encore valable — gravité : mineur

- **Constat** : les 58 URL de l'échantillon répondent toutes 200. Mais
  `Dev/Outils/DataGrip.md` déclare
  `url_docs: https://www.jetbrains.com/datagrip/documentation/`, qui redirige vers
  `https://lp.jetbrains.com/datagrip/features-overview/` — une **page marketing de
  présentation des fonctionnalités**, pas la documentation. Un contrôle de code HTTP
  aurait validé cette URL ; elle ne mène plus à ce qu'elle annonce.
- **Preuve** :
  ```
  $ curl -sL -o /dev/null -w "%{http_code} %{url_effective}\n" \
      https://www.jetbrains.com/datagrip/documentation/
  200 https://lp.jetbrains.com/datagrip/features-overview/
  ```
  Cas voisins bénins dans l'échantillon (redirection vers la cible canonique, sans
  changement de nature) : MariaDB `mariadb.com/kb/en/documentation/` → `/docs/`,
  Pydantic `docs.pydantic.dev` → `pydantic.dev/docs/`, Gradio, BentoML, TensorRT.
- **Portée** : 1 fiche sur 30 dans l'échantillon (3,3 %, IC95 [0,6 ; 16,7]) →
  ~11 fiches sur 336. Ce n'est pas un lien mort, c'est un lien détourné : le pire cas
  pour un contrôle automatique, parce qu'il passe le test.
- **Cause** : JetBrains a réorganisé son site et redirigé une URL de documentation
  vers une landing page. Personne ne relit une URL qui répond 200.
- **Recommandation** : dans le script de l'annexe B, ne pas se contenter du code
  HTTP. Signaler toute URL dont le **domaine change** en cours de redirection
  (`www.jetbrains.com` → `lp.jetbrains.com`), et **ne rien corriger** : la nouvelle
  cible n'est pas forcément la bonne, seul un humain peut trancher. Le signalement
  doit rester un signalement.
- **Effort** : **S** (une comparaison de `netloc` avant / après suivi de redirection,
  ~10 lignes dans le script de l'annexe B). Fichier impacté :
  `AI/scripts/verifier_fraicheur.py`.

### C9. Classement des champs par vitesse de pourrissement — gravité : mineur (constat de méthode)

- **Constat** : l'échantillon permet de hiérarchiser ce qui pourrit, ce qui répond à
  la question 2 du brief. Les taux ci-dessous sont mesurés sur n = 26 à 58 selon le
  champ : ils ordonnent, ils ne prédisent pas.

  | Champ | Constaté | Vitesse | Détectable par machine |
  |---|---|---|---|
  | version affirmée comme courante (corps) | 1/4 fausse | semaines | oui, via PyPI |
  | attribution / propriété du dépôt (`pitch`, corps) | 2/26 dépôts transférés (7,7 %) | mois | oui, `full_name` ≠ slug |
  | `status` / `maturite` | 1/30 indéfendable, 5/336 par détection à froid | mois | oui, `pushed_at` + lexique |
  | `url_docs` détournée | 1/30 | mois | partiellement (changement de domaine) |
  | prix / conditions de licence | 0/1 vérifiable (DataGrip exact) | mois | non |
  | `licence_type` | **0/26** | années | oui, `license.spdx_id` |
  | existence du dépôt | **0/26** | années | oui |
  | joignabilité HTTP | **0/58** | années | oui |

  Le résultat contredit une intuition du brief : les licences ne sont pas le risque
  « rare mais grave » de ce vault, elles sont **exactes à 26/26**. Le risque réel est
  la **propriété du dépôt**, jamais citée dans le brief : 43 fiches attribuent leur
  projet à une organisation nommée dans le `pitch:` — le champ indexé — et 2 dépôts
  sur 26 ont changé de main dans l'échantillon.
- **Preuve** : annexe A (colonnes *valeur brain* / *valeur constatée* / *verdict*) et
  ```
  $ uv run repocount.py
    fiches Dev                                       336
    avec url_repo                                    318
    url_repo github owner/repo (interrogeable API)   316
    pitch attribuant le projet a une organisation    43
    hebergeurs de url_repo : {'github.com': 317, 'git.deuxfleurs.fr': 1}
  ```
- **Portée** : 336 fiches, dont 316 directement sondables par l'API GitHub.
- **Cause** : les faits périssables du vault ne partagent pas une horloge. Une
  licence change une fois par décennie ; un dépôt change d'organisation à chaque
  cession d'entreprise ; une version majeure sort deux fois par an. Une politique de
  péremption unique serait donc soit trop lâche, soit trop bruyante.
- **Recommandation** : caler la politique de péremption sur le champ, pas sur la page
  (cf. *Questions laissées ouvertes* pour les seuils, qui relèvent de l'arbitrage) :
  sonder `full_name` / `archived` / `pushed_at` / `spdx_id` **à chaque passe** du
  script (le coût est le même, un appel par dépôt les renvoie tous les quatre), et
  ne sonder PyPI que pour les 4 fiches qui affirment une version courante.
- **Effort** : **S**, inclus dans le script de l'annexe B.

## Ce qui va bien

**Aucun lien mort, aucun dépôt disparu.** 58 URL sur 58 répondent 200, 26 dépôts sur
26 existent. Sur 336 fiches, 318 portent un `url_repo` et 317 pointent vers GitHub :
c'est une base propre et homogène, directement exploitable par un script. Le taux
d'URL morte extrapolé est de 0 %, IC95 [0 ; 6,2]. **Ne rien faire de ce côté** — un
`link checker` périodique serait du travail pour un problème qui n'existe pas.

**Les licences sont exactes, y compris sur les cas subtils.** 26/26 `licence_type`
défendables. Trois cas méritent d'être cités parce qu'ils sont précisément ceux où un
rédacteur pressé se trompe :
- `MongoDB Compass` → `source-available`. Le `LICENSE` du dépôt est bien la **SSPL
  v1**, que GitHub classe `NOASSERTION` ; la fiche ne s'est pas laissé piéger par le
  « open source » affiché par MongoDB.
- `TensorRT` → `proprietary`, avec la nuance écrite dans le corps : « **Cœur
  propriétaire** (NVIDIA Software License Agreement) […] composants OSS (parsers,
  plugins, samples) et TensorRT-LLM sous Apache-2.0 ». Le dépôt GitHub est
  effectivement `Apache-2.0` — une lecture naïve du dépôt aurait conclu à tort.
- `GitHub Actions` → `proprietary`, alors que le dépôt déclaré (`actions/runner`) est
  MIT. Même piège, même évitement.

**Les fiches récentes sont exactes au jour près.** Deux vérifications en ligne
indépendantes le confirment. `Neptune` affirme : rachat par OpenAI annoncé en décembre
2025, ~400 M$ en actions, service hébergé arrêté le 5 mars 2026, `maturite:
deprecated`. La presse et le press-kit du projet donnent : annonce le 4 décembre 2025,
« under $400 million in stock », sunset des services au 5 mars 2026 (app et API
coupées le 4). `DataGrip` affirme : gratuité limitée à l'usage non commercial,
disponible à partir de la **2025.2.4**, renouvelable annuellement. Le blog JetBrains
donne exactement cela (annonce du 1er octobre 2025, « not supported for any releases
prior to 2025.2.4 », abonnement d'un an auto-renouvelé). Le problème du brain n'est
pas la qualité de rédaction : c'est l'absence de re-lecture.

**La convention de citation des versions résiste au temps.** Seules **4 fiches sur
336** affirment une version comme étant *la version courante* — et 3 des 4 sont
exactes (`Keras 3 est la version courante` : vrai, `keras 3.15.1` ; `evaluate`
« dernière version 0.4.6 (sept. 2025) » : exact à la quinzaine, `0.4.6` publiée le
2025-09-18 ; `CrewAI` n'avance aucun numéro). Le vault énonce ses versions au **passé
historique** — « Airflow 3.0 (GA avril 2025) introduit… », « API remaniée en
profondeur en 1.2+ » — et une affirmation historique ne pourrit pas. Cette convention
implicite est la bonne : elle mérite d'être écrite noir sur blanc dans le gabarit
plutôt que découverte par audit.

**Les chiffres auto-déclarés sont traités correctement — cela répond « oui » à la
question 6 du brief.** 17 fiches emploient le vocabulaire de la mise à distance, et le
cas contradictoire cité dans le brief est explicitement désamorcé :
```
OpenDataLoader PDF.md:58  - **Benchmarks auto-déclarés** : sur son propre corpus
  `opendataloader-bench` (200 PDF), le projet annonce […] 0,907 […] Chiffres du projet,
  non reproduits ici — et [[pdf-inspector]] revendique 0,875 sur le même corpus, ce qui
  invite à la prudence sur les classements croisés.
```
Trois éléments y sont : la valeur, sa source (le projet lui-même), et la
contradiction nommée. C'est suffisant, et il n'y a pas lieu de bâtir un dispositif
de vérification de benchmarks. Une seule réserve, mineure : la contradiction n'est
signalée que sur `OpenDataLoader PDF`, pas sur `pdf-inspector` — le renvoi est
unilatéral là où la convention du vault est bidirectionnelle partout ailleurs.

**Les fiches réellement abandonnées le disent dans le seul champ indexé.** Les
5 fiches `status: abandonne` portent toutes l'information dans leur `pitch:` —
`osint4all` « sans commit depuis juillet 2022 », `Neptune` « service hébergé arrêté en
mars 2026 », `Vanna` « OSS archivé en mars 2026 », `Marqo`, `TorchServe`. Comme le
`pitch:` est le seul champ de jugement que l'index expose (C3), c'est ce réflexe de
rédaction — et lui seul — qui empêche aujourd'hui un agent de proposer une brique
morte. Il tient à une discipline, pas à un contrôle : **c'est fragile, mais ça
fonctionne**, et il faut le préserver en l'écrivant dans le gabarit.

## Questions laissées ouvertes

1. **Quels seuils de péremption ?** Le rapport recommande de sonder par champ (C9)
   mais ne fixe pas les bornes : à partir de combien de jours sans `pushed_at` une
   fiche est-elle signalée ? L'échantillon fournit des repères, pas une règle :
   `papermill` (58 j) et `Stan` (30 j) sont sains, `TF-Agents` (229 j) ne l'est pas,
   et 21 des 26 dépôts ont été poussés dans la semaine. Un seuil à 180 jours aurait
   signalé 2 fiches sur 26 dans l'échantillon (TF-Agents, TorchServe déjà classée) —
   volume tenable. Un seuil à 90 jours en aurait signalé 3. Arbitrage du
   propriétaire : il fixe le bruit qu'il accepte de relire.
2. **Que fait-on d'une fiche périmée ?** Trois issues possibles, non tranchées ici :
   un signalement hors page (le side-car de C7, invisible au lecteur) ; une ligne
   datée en `## Pièges` (visible, mais éditer 34 fiches) ; ou une valeur `status`
   dédiée. La recommandation de C2 (`dormant`) couvre le cas du déclin amont, pas
   celui de « fiche non relue depuis longtemps » — ce sont deux choses différentes et
   il faut décider si la seconde mérite d'être dite au lecteur.
3. **Un `url_repo` peut-il pointer vers un satellite ?** `Dev/Services/Stan.md`
   déclare `url_repo: github.com/stan-dev/cmdstanpy` — le *wrapper Python* (198
   étoiles, branche `develop`), pas `stan-dev/stan`. Le choix est cohérent avec un
   brain orienté Python et l'`alias:` mentionne CmdStanPy. Mais toute sonde
   automatique mesurera dès lors la santé du wrapper et l'attribuera à Stan. Faut-il
   une convention (`url_repo` = dépôt du projet lui-même, le point d'entrée Python
   allant dans le corps), ou accepter l'approximation ? À trancher avant d'écrire le
   script, parce que la réponse change ce qu'il mesure.
4. **`open-core` doit-il couvrir les clauses de réserve dormantes ?** Le `LICENSE` de
   `MCPJam/inspector` est Apache-2.0 **avec une réserve explicite** : le répertoire
   `/server/services` et le fichier `/server/routes/mcp/evals.ts`, « if that directory
   or file exists », relèvent d'une licence distincte définie dans
   `server/evals/LICENSE`. Vérifié : ces trois chemins renvoient **404** aujourd'hui
   — la réserve est dormante, `licence_type: open-source` est défendable, et GitHub
   classe le dépôt `NOASSERTION`. Mais le vault dispose de la valeur `open-core` et le
   corps de la fiche affirme sans réserve « Licence **Apache-2.0** ». Question de
   politique : une clause qui *prévoit* de fermer une partie du code justifie-t-elle
   `open-core` dès aujourd'hui, ou attend-on que le répertoire apparaisse ? La réponse
   engage bien plus que cette fiche : c'est le motif exact — open-core présenté comme
   open-source — cité dans le brief comme ayant déjà produit un faux le 2026-09-02.
5. **Faut-il porter l'échantillon à 100 fiches ?** L'IC95 sur le taux de défaut
   décisionnel est [3,5 % ; 25,6 %] : il dit « quelques dizaines de fiches », pas
   « 34 ». n = 100 le resserrerait à environ ±6 points. Coût : ~72 appels API GitHub
   supplémentaires (soit deux fenêtres horaires non authentifiées, ou une seule avec
   un token) et une session de lecture. À décider selon l'usage : pour lancer le
   script de l'annexe B, la précision actuelle suffit largement.

---

## Annexe A — les 30 fiches échantillonnées

Tirage : `random.seed(20260902)`, `random.sample(rows, 30)` sur les 336 fiches
`type: service|outil` de `Dev/`, triées par chemin. Sondes du 2026-09-02 :
`api.github.com/repos/<slug>` (redirections suivies), `pypi.org/pypi/<pkg>/json`,
`curl -sL` sur les 58 URL. « j » = jours depuis `pushed_at`.

| # | Fiche | Champ vérifié | Valeur du brain | Valeur constatée | Verdict |
|---|---|---|---|---|---|
| 1 | DataGrip | licence / prix / url_docs | `proprietary` ; gratuit non commercial ≥ 2025.2.4, renouvelable un an | JetBrains, 01/10/2025 : « not supported prior to 2025.2.4 », abonnement 1 an auto-renouvelé | **exact** — sauf `url_docs` : 200 mais redirige vers `lp.jetbrains.com/…/features-overview/` (**périmé, mineur**) |
| 2 | Figma | licence / status | `proprietary` / `actif` | pas d'`url_repo`, non sondable par API | **non falsifiable** (aucune sonde possible) |
| 3 | MongoDB Compass | licence / dépôt | `source-available` | `LICENSE` = **SSPL v1** ; SPDX `NOASSERTION` ; push J-0 | **exact** (cas subtil bien traité) |
| 4 | osint4all | status / dernier commit / licence | `abandonne` ; « sans commit depuis juillet 2022 » ; `open-source` | `pushed_at` **2022-07-09** (1516 j) ; SPDX `CC0-1.0` | **exact** |
| 5 | Airflow | status / version | `actif` / `production` ; « Airflow 3.0 (GA avril 2025) » | push J-0 ; `apache-airflow 3.3.1` (2026-08-12) | **exact** (version énoncée au passé, ne pourrit pas) |
| 6 | BentoML | status / version | `actif` / `production` ; « API remaniée en 1.2+ » | push J-5 ; `bentoml 1.4.39` (2026-05-07) | **exact** |
| 7 | Faker | status / licence | `actif` / `production` / `open-source` | push J-1 ; MIT ; `faker 40.38.0` (2026-09-01) | **exact** |
| 8 | GitHub Actions | licence | `proprietary` (dépôt `actions/runner` = MIT) | dépôt MIT, service propriétaire | **exact** (cas subtil bien traité) |
| 9 | Gradio | status / licence | `actif` / `production` / `open-source` | push J-0 ; Apache-2.0 | **exact** |
| 10 | MariaDB | licence / status | `open-source` / `actif` | push J-0 ; GPL-2.0 | **exact** |
| 11 | Neptune | status / maturité / rachat / arrêt | `abandonne` / `deprecated` ; « rachat OpenAI ~400 M$ », « arrêté le 5 mars 2026 » | dépôt **archivé**, push 2026-03-17 ; annonce 04/12/2025, « under $400M in stock », sunset 05/03/2026 | **exact** (4 faits vérifiés, 4 justes) |
| 12 | Parquet | licence / status | `open-source` (Apache-2.0) / `actif` | push J-1 ; Apache-2.0 | **exact** |
| 13 | Postgres | licence / status | `open-source` / `actif` | push J-0 ; SPDX `NOASSERTION` (licence PostgreSQL, BSD-like) | **exact** |
| 14 | Prophet | status / licence | `actif` / `production` / `open-source` | push J-6 ; MIT | **exact** |
| 15 | PyTorch Lightning | status / licence | `actif` / `production` / `open-source` | push J-1 ; Apache-2.0 ; `pytorch-lightning 2.6.5` | **exact** |
| 16 | PyTorch | licence / status | `open-source` / `actif` | push J-0 ; `NOASSERTION` (BSD-3 modifié) | **exact** |
| 17 | Pydantic | status / licence | `actif` / `production` / `open-source` | push J-0 ; MIT ; `pydantic 2.13.5` | **exact** |
| 18 | Stan | `url_repo` / status | `github.com/stan-dev/cmdstanpy` ; `actif` / `production` | dépôt existe (198 ★, branche `develop`, push J-30) — mais c'est le **wrapper Python**, pas `stan-dev/stan` | **défendable, à trancher** (cf. question ouverte 3) |
| 19 | TF-Agents | status / maturité | `actif` / `production` | dernière release `0.19.0` du **2023-12-14** ; push 2026-01-16 (**229 j**) ; le corps de la fiche dit « maintenance en déclin » | **FAUX — décisionnel** |
| 20 | TRL | status / licence | `actif` / `production` / `open-source` | push J-0 ; Apache-2.0 ; `trl 1.12.0` | **exact** |
| 21 | TensorRT | licence | `proprietary` + corps : « cœur propriétaire, composants OSS Apache-2.0 » | dépôt Apache-2.0, cœur sous NVIDIA SLA | **exact** (cas subtil bien traité) |
| 22 | TorchServe | status / maturité | `abandonne` / `deprecated` | dépôt **archivé**, push **2025-08-06** (392 j) | **exact** |
| 23 | curl_cffi | status / licence | `actif` / `production` / `open-source` | push J-1 ; MIT ; `curl-cffi 0.16.2` | **exact** |
| 24 | fastmcp | version (corps) | « **FastMCP 2.0** est la version activement développée » | 3.x = série stable (`v3.4.3`), `fastmcp 4.0.1` sur PyPI le 2026-09-02 | **FAUX — décisionnel** (2 majeures de retard) |
| 25 | fastmcp | `url_repo` | `github.com/jlowin/fastmcp` | redirige vers `PrefectHQ/fastmcp` (le corps sait : « maintenu sous Prefect ») | **périmé, mineur** |
| 26 | hydra | attribution (`pitch` indexé) | « Framework de configuration hiérarchique composable **(Meta)** » | dépôt cédé à `hydra-ecosystem` — « independent stewardship » | **FAUX — décisionnel** |
| 27 | hydra | `url_repo` | `github.com/facebookresearch/hydra` | redirige vers `hydra-ecosystem/hydra` ; MIT ; push J-0 | **périmé, mineur** |
| 28 | mcpjam | licence | `open-source` ; corps : « Licence **Apache-2.0** » | `LICENSE` = Apache-2.0 **avec réserve** sur `/server/services` et `/server/routes/mcp/evals.ts` sous licence distincte ; ces chemins renvoient **404** ; SPDX `NOASSERTION` | **défendable aujourd'hui, à surveiller** (cf. question ouverte 4) |
| 29 | papermill | status / licence | `actif` / `production` / `open-source` | push J-58 ; BSD-3-Clause ; `papermill 2.7.0` (2026-02-27) | **exact** |
| 30 | scipy.signal | status / licence | `actif` / `production` / `open-source` | push J-0 ; BSD-3-Clause ; `scipy 1.18.1` | **exact** |
| 31 | sentence-transformers | status / licence | `actif` / `production` / `open-source` | push J-0 ; Apache-2.0 ; `sentence-transformers 6.0.1` | **exact** |
| 32 | statsmodels | status / licence | `actif` / `production` / `open-source` | push J-1 ; BSD-3-Clause ; `statsmodels 0.15.0` | **exact** |

30 fiches, 32 lignes : `fastmcp` et `hydra` portent chacune deux défauts distincts
(un décisionnel, un mineur) et occupent deux lignes.

**Décompte.** Fiches avec au moins un défaut : **4/30** (`fastmcp`, `hydra`,
`TF-Agents`, `DataGrip`) = 13,3 %, IC95 Wilson [5,3 ; 29,7] → **45 fiches sur 336**,
IC [18 ; 100]. Fiches avec au moins un défaut **décisionnel** : **3/30** (`fastmcp`,
`hydra`, `TF-Agents`) = 10,0 %, IC95 [3,5 ; 25,6] → **34 fiches**, IC [12 ; 86].
Licences erronées : **0/26**, IC95 [0 ; 12,9]. Dépôts disparus : **0/26**.
URL en erreur HTTP : **0/58**, IC95 [0 ; 6,2].

---

## Annexe B — spécification du script de re-vérification

`AI/scripts/verifier_fraicheur.py` — à créer par le correcteur, ~120 lignes.

### Ce qu'il lit

1. Les frontmatters de `Dev/**/*.md` où `type ∈ {service, outil}` (336 fiches) :
   `nom`, `status`, `maturite`, `licence_type`, `url_repo`, `url_docs`,
   `remplace_par`.
2. Le corps de chaque page, pour la règle hors ligne de cohérence corps/frontmatter
   (C2).
3. Pour les 316 `url_repo` de forme `https://github.com/<owner>/<repo>` :
   `GET https://api.github.com/repos/<owner>/<repo>`, **redirections suivies** (c'est
   la redirection qui révèle un transfert : sans `-L`, l'API renvoie
   `301 Moved Permanently` et rien d'autre — les deux transferts de l'échantillon ont
   d'abord été manqués pour cette raison). Un appel suffit et rend `full_name`,
   `archived`, `pushed_at`, `license.spdx_id`, `stargazers_count`, `default_branch`.
4. Pour les seules fiches qui affirment une version comme courante (4 aujourd'hui,
   détectées par la regex de l'annexe C §3) : `GET pypi.org/pypi/<pkg>/json`.
5. Les `url_docs` et `url_repo` : une requête `HEAD` avec suivi de redirection, pour
   le code final **et le domaine final**.

### Ce qu'il signale

Un enregistrement par page dans `AI/index/fraicheur.json`, avec une liste
`signalements` prise dans ce vocabulaire fermé :

| Code | Déclencheur | Cas de l'échantillon qu'il attrape |
|---|---|---|
| `depot_transfere` | `full_name` ≠ slug déclaré dans `url_repo` | `fastmcp`, `hydra` |
| `depot_archive` | `archived == true` et `status != abandonne` | (aucun ici : Neptune et TorchServe sont déjà classées) |
| `depot_disparu` | HTTP 404 sur l'API | aucun |
| `push_ancien` | `pushed_at` plus vieux que le seuil retenu (question ouverte 1) et `status == actif` | `TF-Agents` (229 j) |
| `licence_divergente` | `spdx_id` incompatible avec `licence_type`, table de correspondance explicite ; `NOASSERTION` → toujours signalé pour lecture humaine | `mcpjam`, et les 4 `NOASSERTION` légitimes (Compass, Postgres, PyTorch) |
| `version_perimee` | version PyPI de majeure supérieure à celle affirmée dans le corps | `fastmcp` |
| `url_domaine_change` | domaine final ≠ domaine déclaré après redirection | `DataGrip` |
| `url_morte` | code final ≥ 400 | aucun |
| `corps_declin_vs_status_actif` | lexique du déclin dans `## Pourquoi` / `## Déploiement & coût` / `## Pièges`, hors lignes citant `[[Dev/…]]`, alors que `status == actif` | `Acme`, `TF-Agents`, `pytorch-crf`, `rank-bm25`, `OpenCut` |
| `status_maturite_incoherents` | couple interdit (cf. C5) | `AutoGen`, `Vanna` |
| `abandonne_sans_remplacement` | `status != actif` et `remplace_par == []` | 5 fiches |

Sortie humaine sur stdout : un tableau trié par gravité, une ligne par signalement,
« fiche — code — valeur du brain — valeur constatée ». Sortie machine :
`AI/index/fraicheur.json` (schéma en C7). Code de retour **0 en toutes
circonstances** : ce script n'est pas un validateur de CI, c'est un rapport. Bloquer
un commit sur la santé d'un dépôt tiers rendrait le vault otage de l'amont.

### Ce qu'il refuse de faire

1. **Ne jamais écrire dans `Dev/`, `Wiki/`, `MOC/`, `Documentation/`, `Templates/`.**
   Aucun mode `--fix`, aucune option de correction automatique. Un `status:` encode un
   jugement (« vaut-il d'être proposé à un projet ? ») qu'aucune métrique de dépôt ne
   contient : `Acme` a 0 release depuis 2022 et reste la bonne réponse pour de la
   recherche RL en JAX. Le script produit la liste à relire, l'humain tranche.
2. **Ne jamais réécrire un `url_repo` transféré.** Une redirection GitHub dit qu'un
   dépôt a bougé, pas que la nouvelle cible est celle que la fiche doit citer — un
   transfert peut accompagner un fork hostile, un abandon ou un rachat, et
   l'attribution du `pitch:` doit être relue en même temps (cas `hydra`).
3. **Ne jamais réécrire une `url_docs` détournée.** Cf. C8 : la cible de redirection
   n'est pas nécessairement de la documentation.
4. **Ne pas déduire `licence_type` du `spdx_id`.** Trois fiches de l'échantillon sont
   correctes *contre* ce que dit le dépôt (`TensorRT`, `GitHub Actions`,
   `MongoDB Compass`) : la déduction automatique les casserait toutes les trois.
   `NOASSERTION` se signale, ne se traduit pas.
5. **Ne pas régénérer `brain-index.json` ni les MOC.** Le side-car est un fichier
   distinct ; il ne partage pas le cycle de vie de l'index de navigation.
6. **Ne pas exiger de jeton GitHub pour tourner.** 316 appels dépassent le quota non
   authentifié (60/h) : prévoir `--limit N`, une reprise sur `AI/index/fraicheur.json`
   (ne re-sonder que ce qui n'a pas de `sonde_le` récent) et la lecture d'un
   `GITHUB_TOKEN` **optionnel** dans l'environnement (5000/h). Sans jeton, une passe
   complète prend 6 fenêtres horaires ; avec, une minute. Ne jamais écrire de jeton
   dans le vault.

---

## Annexe C — scripts de reproduction

Les trois scripts ont tourné depuis
`/tmp/…/scratchpad/` et ne touchent au vault qu'en lecture. Ils ne sont pas versionnés :
seuls leurs résultats comptent, et ils sont reproductibles depuis les extraits
ci-dessous.

**§1 — tirage de l'échantillon** (`sample.py`) : charge les frontmatters de
`Dev/**/*.md` filtrés sur `type ∈ {service, outil}`, **trie par chemin**, puis
`random.seed(20260902)` et `random.sample(rows, 30)`. Le tri avant tirage est ce qui
rend le tirage reproductible indépendamment de l'ordre de `glob`. Renvoie 336 fiches
en base.

**§2 — détection des contradictions de fraîcheur** (`contra.py`, `contra2.py`) :
quatre passes hors ligne sur les 336 fiches — (A) fiches non actives et signalement de
l'état dans le `pitch:` ; (B) couples `status`/`maturite` incompatibles ; (C) corps
décrivant son propre déclin sous `status: actif`, en restreignant aux sections
`## Pourquoi` / `## Déploiement & coût` / `## Pièges` et en écartant toute ligne
contenant `[[Dev/` ; (D) fiches non actives sans `remplace_par`. Le filtre `[[Dev/`
est indispensable : sans lui, (C) remonte 37 fiches dont 30 ne citent que le pitch
d'un voisin mort.

**§3 — surface réelle des versions** (`vregex.py`, `verrot.py`) : rejoue la regex
`\bv?\d+\.\d+(\.\d+)?\b` de `audit_mesures.py` §9, puis la rejoue après retrait des
identifiants SPDX (`Apache-2\.0|GPL-[0-9.]+|BSD-[0-9]-Clause|CC0-1\.0|MPL-2\.0|…`) et
du motif `Python\s*[≥>=]*\s*3\.\d+` → 214 puis 108. `verrot.py` isole ensuite les
formulations qui présentent une version comme *courante* (« la version courante »,
« dernière version », « est la version activement développée ») → 4 fiches.

**§4 — sondes réseau** : `api.github.com/repos/<slug>` avec `-L` sur 28 dépôts,
`pypi.org/pypi/<pkg>/json` sur 22 paquets, `curl -sL -w "%{http_code}
%{url_effective}"` sur les 58 URL, `raw.githubusercontent.com/<slug>/<branche>/LICENSE`
sur `MCPJam/inspector` et `mongodb-js/compass`. Aucun appel authentifié : le quota
non authentifié de 60 requêtes/heure a été la contrainte dimensionnante de cet audit
et justifie le `--limit` de l'annexe B.

**Sources web consultées** (au-delà des API) :
[OpenAI to acquire AI training tracker Neptune — InfoWorld](https://www.infoworld.com/article/4101200/openai-to-acquire-ai-training-tracker-neptune.html),
[Neptune press kit](https://neptune.ai/press-kit),
[OpenAI Buys Neptune for Under $400M — VKTR](https://www.vktr.com/ai-news/openai-buys-neptune-for-under-400m-in-ai-governance-push/),
[DataGrip Is Now Free for Non-Commercial Use — JetBrains Blog](https://blog.jetbrains.com/datagrip/2025/10/01/datagrip-is-now-free-for-non-commercial-use/),
[The free non-commercial licensing FAQ — JetBrains](https://sales.jetbrains.com/hc/en-gb/articles/18950890312210-The-free-non-commercial-licensing-FAQ),
[hydra-ecosystem/hydra](https://github.com/hydra-ecosystem/hydra),
[PrefectHQ/fastmcp releases](https://github.com/PrefectHQ/fastmcp/releases),
[FastMCP changelog](https://gofastmcp.com/changelog),
[hydra-core — PyPI](https://pypi.org/project/hydra-core/).
