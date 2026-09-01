# Rapport d'audit — Axe 2 : Integrite au fil de l'eau

Auditeur : conversation dediee « audit axe 2 », le 2026-09-02.
Socle : `AI/audit/mesures-axe2.md`, relance le 2026-09-02 — **identique au bit pres a
`mesures-2026-09-02.md`** (`diff` vide). Aucun ecart entre le socle et le vault.

**Un ecart existe en revanche entre le brief et le vault.** `axe-2-integrite.md` annonce
« 19 pages orphelines, dont les 5 Patterns et les 5 Rules — 100 % de ces deux dossiers ».
La mesure donne **12** pages sans lien entrant, dont **3** Patterns et **0** Rule. Le vault
fait foi. La nuance est instructive et non cosmetique : les 5 Rules **se citent entre
elles**, ce qui leur donne un lien entrant sans les rendre joignables. Le bon indicateur
n'est pas « citee par personne » mais « atteignable depuis un hub » — sur ce critere,
**11 pages** sont hors du graphe navigable, dont 100 % des Rules (cf. C5).

## Synthese

Le vault est propre : `check_brain` passe au vert, les six artefacts generes sont
rigoureusement synchrones avec le frontmatter courant (0 derive sur 647 pages), et 787 des
801 pitchs reinjectes sont exacts. Le trou n'est pas dans les regles : il est dans le
**declencheur**. Aucun controle n'est branche ailleurs que dans le skill de creation —
ni hook, ni CI, ni hook git — et le protocole de **mise a jour** d'une page tient en cinq
mots dans `CLAUDE-build.md` : « patch la fiche concernee ». Si on ne fait qu'une chose :
ecrire la procedure de mise a jour avec sa table d'effets de bord (annexe A), et brancher
`check_brain` sur un declencheur qui ne depende pas de la bonne volonte de l'agent.

## Constats

### C1. Aucun protocole de mise a jour : la seule instruction est « patch la fiche » — gravite : bloquant

- **Constat** : le skill `enrichir-brain` synchronise pitchs et alternatives, mais
  seulement *a l'interieur* d'un flux de creation (etape 7 de sa procedure ciblee). Le cas
  « une page existe deja et un champ change » est route ailleurs, vers une instruction sans
  contenu. `CLAUDE-build.md:36` : « **D'enrichir une fiche existante** depuis un article web
  ou une experience → patch la fiche concernee. » Aucune mention de propagation, aucun
  script a relancer, aucun renvoi vers le skill. Le skill lui-meme (`SKILL.md:2` de sa
  procedure) dit « proposer une mise a jour plutot qu'une creation » sans decrire laquelle.
- **Preuve** :
  ```
  $ grep -n -A2 "D'enrichir une fiche existante" CLAUDE-build.md
  36:6. **De refactorer une partie du brain** ... les scripts check_brain.py et audit-vault.ps1 peuvent aider.
  # ligne 36 precedente : « D'enrichir une fiche existante ... → patch la fiche concernee. »
  $ grep -c "mise a jour\|mise à jour" .claude/skills/enrichir-brain/SKILL.md
  2      # les deux occurrences sont des renvois, aucune procedure
  ```
  Consequence mesuree : 5 lignes d'`## Alternatives` affichent un pitch reellement perime
  (cf. C2), c'est-a-dire 5 cas ou un `pitch:` a ete reecrit sans que les citeurs suivent.
- **Portee** : tout le vault. 337 fiches Dev portent des champs propages ; 801 lignes
  reinjectent un pitch ; 47 vues `.base` filtrent sur `categorie` ou `tags`.
- **Cause** : le brain a ete construit en creation massive (647 pages en trois mois). Le
  protocole a ete ecrit pour ce regime. Le regime de maintenance — ou l'on modifie plus
  qu'on ne cree — n'a pas encore ete instruit, donc pas outille.
- **Recommandation** : ajouter au skill `enrichir-brain` une **procedure « mise a jour »**
  symetrique de la procedure ciblee, pilotee par la table de l'annexe A : pour chaque champ
  modifie, la liste des consommateurs a repropager et la commande qui le verifie. Rediriger
  `CLAUDE-build.md:36` vers cette procedure au lieu de « patch la fiche ».
- **Effort** : M (une session). Fichiers : `.claude/skills/enrichir-brain/SKILL.md`,
  `CLAUDE-build.md`, `AI/design/brain-v2.md` §5.1 (mecanique du pitch).

### C2. La regle cardinale du pitch est inapplicable telle qu'ecrite : quatre conventions coexistent — gravite : serieux

- **Constat** : la regle dit « la ligne affichee pour une cible dans une section
  `## Alternatives` doit etre **exactement** le `pitch:` courant de cette cible ». Le vault
  la respecte a 787/801. Mais les 14 restants ne sont **pas 14 defauts** : ils se rangent en
  quatre familles dont deux sont des choix editoriaux deliberes. Coder la regle telle
  qu'ecrite detruirait du contenu ecrit a la main.
  | Famille | Lignes | Nature |
  |---|---|---|
  | Conforme au mot | 787 | rien a faire |
  | Pitch perime | **5** | derive reelle, resynchronisation mecanique |
  | Cosmetique (`**gras**` ajoute au pitch) | 2 | texte identique apres normalisation |
  | Pitch + suffixe comparatif | 2 | pitch en prefixe, remarque ajoutee volontairement |
  | Prose comparative, cible **hors** `alternatives:` | 3 | mention de voisinage, pas une alternative |
  | Prose comparative, cible **dans** `alternatives:` | 2 | comparaison redigee (Guidance ↔ Outlines) |
- **Preuve** : classification reproductible (similarite de Jaccard entre ligne affichee et
  `pitch:`, plus appartenance au frontmatter `alternatives:`) —
  `/tmp/.../probe6.py`, sortie :
  ```
  lignes verifiables: 801
    strict_ok: 787 | cosmetique: 2 | prefixe_pitch_plus_suffixe: 2
    prose_hors_frontmatter: 3 | pitch_perime: 5 | prose_dans_frontmatter: 2
  -- pitch_perime
     ('Dev/Services/OpenAI Agents SDK.md', 'Agno', 0.78)
     ('Dev/Services/OpenAI Agents SDK.md', 'smolagents', 0.78)
     ('Dev/Services/smolagents.md', 'Agno', 0.78)
     ('Dev/Services/Agno.md', 'smolagents', 0.78)
     ('Dev/Services/Faker.md', 'Mimesis', 0.79)
  -- prose_hors_frontmatter
     ('Dev/Services/Loki.md', 'Elasticsearch')   # « approche concurrente par indexation du contenu »
     ('Dev/Services/Mimesis.md', 'SDV')          # « autre nature : synthese par modeles apprise »
     ('Dev/Services/Faker.md', 'SDV')
  ```
  Le recoupement est net : les 3 cas `prose_hors_frontmatter` sont exactement les 3 seules
  pages ou la section cite une cible absente du frontmatter `alternatives:` (probe5, §Y).
  La prose n'est donc pas un oubli de synchro : c'est la convention utilisee pour signaler
  un voisin qui n'est **pas** une alternative.
- **Portee** : 801 lignes sur 334 pages a section `## Alternatives` ; 7 lignes a corriger,
  sur 5 pages (`OpenAI Agents SDK`, `smolagents`, `Agno`, `Faker`, `Modal`, `E2B`).
- **Cause** : la regle a ete ecrite pour la generation automatique (une donnee, trois
  usages). L'usage reel y a superpose de l'annotation comparative — utile, mais qui casse
  l'egalite stricte. Personne n'a arbitre entre les deux, donc les deux coexistent.
- **Recommandation** : reformuler la regle avant de la coder, en deux clauses verifiables :
  1. si la cible figure dans `alternatives:`, la ligne affichee doit **commencer** par le
     `pitch:` courant de la cible, apres normalisation (`**` et espaces multiples ignores) ;
     un suffixe libre est autorise apres le pitch ;
  2. si la cible ne figure pas dans `alternatives:`, la ligne est libre (mention de
     voisinage) — mais alors la puce doit etre distinguee typographiquement pour que la
     regle 1 ne s'y applique pas par accident (par exemple prefixe « voisin : »).
  Sous cette formulation, le vault compte **7 violations** (5 pitchs perimes + 2 gras) et
  non 14, et les 7 se corrigent mecaniquement, la source de verite etant le `pitch:` de la
  cible. Un script de resynchronisation est donc possible, **sous trois conditions** : il ne
  touche que le prefixe et preserve tout suffixe ; il ignore les puces dont la cible est
  hors `alternatives:` ; il refuse d'agir sur les 2 cas `prose_dans_frontmatter`
  (Guidance ↔ Outlines), qui relevent d'un arbitrage humain — soit la prose devient le
  pitch, soit la puce est reclassee en voisinage.
- **Effort** : S pour reformuler la regle + corriger les 7 lignes a la main.
  M si l'on veut le script de resynchronisation avec ses garde-fous. Fichiers :
  `.claude/skills/enrichir-brain/SKILL.md`, `AI/design/brain-v2.md` §5.1,
  les 6 pages listees, `AI/scripts/check_brain.py`.

### C3. Aucun controle branche hors du skill : le vault n'est valide que quand un agent veut bien le valider — gravite : serieux

- **Constat** : `check_brain.py` n'est declenche par rien d'automatique. Pas de `settings.json`
  dans le vault (seul `settings.local.json` existe, sans section `hooks`), pas de hooks dans
  la configuration globale de l'utilisateur, pas de `.github/`, aucun hook git installe. Le
  hook Stop documente (`AI/scripts/session_to_devbrain.py`) n'est pas cable : `AI/sessions/`
  contient **2** fichiers pour un vault construit sur trois mois. Consequence : toute
  edition faite dans Obsidian, ou par un agent qui n'invoque pas `enrichir-brain`, entre
  dans le vault sans qu'aucune des six regles dures ne soit evaluee.
- **Preuve** :
  ```
  $ ls .claude/                 → README.md settings.example.json settings.local.example.json settings.local.json skills
  $ grep -c hooks .claude/settings.local.json   → 0
  $ python3 -c "import json;print(json.load(open('~/.claude/settings.json')).get('hooks'))"  → None
  $ ls .github                  → No such file or directory
  $ ls $(git rev-parse --git-common-dir)/hooks | grep -v sample   → (vide)
  $ ls AI/sessions/ | wc -l     → 2
  ```
- **Portee** : les 647 pages, en permanence.
- **Cause** : le controle a ete pense comme une **etape de protocole** (etape 8 du skill) et
  non comme un **garde-fou d'infrastructure**. Un protocole ne se declenche que si l'agent
  lit le protocole.
- **Recommandation** : deux branchements, pas un.
  1. **Hook `Stop`** (pas `PostToolUse`) : `check_brain.py` prend ~2 s sur 647 pages, mais un
     `PostToolUse` sur chaque `.md` le relancerait des dizaines de fois par session et
     signalerait des etats intermediaires normaux (une page creee avant sa reciproque). En
     `Stop`, il tourne une fois, sur un etat stable, et le rapport arrive avant le commit.
  2. **CI GitHub Actions** sur `push` : c'est le seul filet qui couvre les editions faites
     dans Obsidian, hors de toute session Claude. Un job `uv run AI/scripts/check_brain.py`
     suffit ; y ajouter `audit_mesures.py` en artefact donne la serie temporelle gratuitement.
  Le cout de friction est nul dans les deux cas (aucune saisie humaine ajoutee) ; le degat
  evite est la classe entiere des C2/C4/C6.
- **Effort** : S (< 1 h). Fichiers : `.claude/settings.example.json` + `settings.json`
  (section `hooks`), `.github/workflows/check-brain.yml` (a creer), `AI/scripts/README.md`.

### C4. Quatre des six types n'ont ni gabarit controle ni gabarit specifie — gravite : mineur (latent, non realise)

- **Constat** : `check_brain.ALLOWED` ne declare que `service` et `concept`. Les types
  `outil` (40 pages), `pattern` (5), `rule` (5), `rex` (1) peuvent porter n'importe quel
  champ sans signalement. Le risque est **latent** : les 51 pages sont aujourd'hui
  parfaitement uniformes. Mais deux causes de cette uniformite sont fragiles :
  `type: outil` n'a **aucun fichier dans `Templates/`** (seuls Service-Dev, Concept-Wiki,
  Pattern, Rule, REX, REX-entry existent), et `AI/design/brain-v2.md` §5.3 ne specifie pour
  ces types que la structure du **corps**, jamais le frontmatter. Les 40 pages `outil`
  partagent 15 champs identiques par heritage d'un lot de creation unique, pas par regle.
  De plus, `Dev/Outils/` n'apparait meme pas dans §5.3, qui situe les « Outils » dans
  `Wiki/Outils/`.
- **Preuve** :
  ```
  $ ls Templates/
  Concept-Wiki.md  Pattern.md  REX-entry.md  REX.md  Rule.md  Service-Dev.md   # pas d'Outil
  $ # champs par type (probe1) — 0 champ a geometrie variable :
  outil   (40) : alias alternatives categorie domaines galaxie langage licence_type nom os
                 pitch status tags type url_docs url_repo
  pattern  (5) : contexte created galaxie modified projets_appliques services_cles tags type
  rule     (5) : applicable created domaine galaxie modified strictness tags type
  rex      (1) : created galaxie modified service tags type
  ```
- **Portee** : 51 pages, 0 divergence a ce jour. Le cout de mise en conformite est donc
  **nul** : les gabarits se derivent mecaniquement de l'existant.
- **Cause** : la v2 a specifie finement les deux gabarits qui portent la valeur (service,
  concept) et repris les autres « quasi inchanges de v1 » sans les reecrire. `outil` est
  apparu apres la spec.
- **Recommandation** : figer les quatre gabarits depuis les listes de champs ci-dessus, les
  ajouter a `ALLOWED` et `REQUIRED`, et creer `Templates/Outil-Dev.md`. A faire **maintenant
  precisement parce que le cout est nul** : chaque nouvelle page ecrite sans gabarit rend
  l'operation plus chere. Deux anomalies a trancher au passage : `pattern`/`rule`/`rex`
  portent `created`/`modified`, qui figurent dans `V1_MARKERS` — inoffensif tant que ces
  pages sont dans `Dev/` (ou `is_active_v2` renvoie `True` sans condition), mais une page de
  ce type deplacee sous `Wiki/` disparaitrait silencieusement de l'index ; et `rule` porte
  `domaine:` (singulier, valeurs `security`/`dependencies`/`tests`/`code-style`/`docs`), un
  cinquieme vocabulaire non declare dans `Documentation/general/`.
- **Effort** : S (< 1 h). Fichiers : `AI/scripts/check_brain.py`, `Templates/Outil-Dev.md`,
  `AI/design/brain-v2.md` §5.3, `Documentation/general/` (vocabulaire `domaine` des rules).

### C5. Onze pages hors du graphe navigable : defaut de generation, pas de contenu — gravite : serieux

- **Constat** : la question 7 du brief se tranche nettement du cote generation.
  `build_mocs.py` groupe les pages Dev par **tete de `categorie:`** (`head = (p.get("categorie")
  or "").split("/")[0]` ; `if head:`). Or les 5 Patterns, les 5 Rules et le REX **n'ont pas
  de champ `categorie:`** — ils sont donc exclus du groupement, sans erreur ni avertissement.
  Aucun hub ne les liste, et rien ne le signale.
- **Preuve** : parcours en largeur depuis les 31 MOC, en suivant les wikilinks
  (`/tmp/.../probe7.py`) :
  ```
  noeuds: 678 (dont 31 MOC) ; pages Dev/Wiki inatteignables depuis un MOC: 11
  Counter({'Dev/Rules': 5, 'Dev/Patterns': 4, 'Dev/REX': 1, 'Wiki/Outils': 1})
  ```
  Le 5e Pattern (`Pattern - Agent sur LLM auto-heberge`) est joignable, parce que six fiches
  Service le citent — donc le contenu n'est pas le probleme : quand un lien existe, la page
  entre dans le graphe. Les 5 Rules, elles, forment une clique fermee : chacune a 1 a 3 liens
  entrants, tous venant des quatre autres. Elles passent le test « a un lien entrant » et
  echouent le test « est joignable ».
- **Portee** : 11 pages sur 647 (1,7 %), mais 100 % de `Dev/Rules/` et 80 % de
  `Dev/Patterns/`. A distinguer des 12 pages « sans lien entrant » de `mesures-axe2.md` §6 :
  les deux ensembles ne se recouvrent qu'a moitie. Les 2 concepts Wiki orphelins
  (`A-B testing`, `ROC-AUC & courbe PR`) sont, eux, parfaitement joignables via
  `MOC/Concepts/` — ils n'ont pas de probleme d'integrite.
- **Cause** : `build_mocs` a ete ecrit pour les deux familles peuplees (services par
  categorie, concepts par sous-domaine). Patterns et Rules etaient trop peu nombreux pour
  qu'on remarque leur absence, et le script ne compte pas ce qu'il n'a pas indexe.
- **Recommandation** : deux corrections, dans cet ordre.
  1. Faire echouer le silence : `build_mocs.py` doit compter les pages Dev qu'il a ecartees
     faute de `categorie:` et l'imprimer (`11 page(s) Dev sans categorie, hors MOC`). Un
     script qui ignore ne doit pas ignorer sans le dire.
  2. Choisir la porte d'entree. Deux options exclusives, a arbitrer par le proprietaire
     (cf. *Questions ouvertes*) : soit doter Patterns et Rules d'une `categorie:` et laisser
     `build_mocs` faire son travail — mais il faut alors ouvrir `pattern/*` et `rule/*` dans
     la taxonomie, ce qui empiete sur l'axe 1 ; soit ajouter a `build_mocs` deux hubs
     dedies, `MOC/Categories/Patterns.md` et `MOC/Categories/Regles.md`, groupes par `type:`
     et non par `categorie:` — sans toucher a la taxonomie. La seconde est la moins
     couteuse et la moins intrusive.
  3. Puis regle souple dans `check_brain` : toute page Dev/Wiki doit etre atteignable depuis
     un MOC — 11 violations aujourd'hui, 0 apres le point 2.
- **Effort** : M (une session) pour les trois points. Fichiers : `AI/scripts/build_mocs.py`,
  `AI/scripts/check_brain.py`, `MOC/Categories/` (genere).

### C6. Unicite de `nom:` et `alias:` non controlee : la detection de doublons du skill est faussee — gravite : serieux

- **Constat** : rien ne garantit qu'un `alias:` soit unique. Or c'est exactement la cle sur
  laquelle le skill `enrichir-brain` verifie qu'une page n'existe pas deja (etape 1 :
  `query_index.py --name "<X>"`, qui matche `nom` **et** `alias`). Trois anomalies :
  **41 alias** sont revendiques par 2 pages ou plus ; **10 d'entre eux sont le `nom:` exact
  d'une autre page** ; et **10 pages listent le meme alias deux fois a la casse pres**.
- **Preuve** :
  ```
  # alias revendique par 2+ pages (41 cas) — extrait :
  'shap'        : ['Dev/Services/SHAP.md', 'Wiki/Concepts/Explicabilite des modeles.md']
  'yolo'        : ['Dev/Services/Ultralytics YOLO.md', "Wiki/Concepts/Detection d'objets.md"]
  'map'         : ['Wiki/Concepts/Metriques vision.md', 'Wiki/Concepts/Estimation MAP.md',
                   'Wiki/Concepts/Ranking metrics.md']       # trois pages
  'tensorrt-llm': ['Dev/Services/TensorRT-LLM.md', 'Dev/Services/TensorRT.md']  # alias == nom voisin
  # doublon interne a la casse pres (10 pages) — extrait :
  Dev/Services/Spark.md            : ['Apache Spark', 'spark', 'PySpark', 'pyspark']
  Dev/Services/Neo4j.md            : ['neo4j', 'neo4J', 'neo 4j']
  Dev/Services/PyTorch Geometric.md: ['PyG', 'pyg', 'torch-geometric', 'torch_geometric']
  # collision de nom, insensible a la casse (1 cas) :
  'hdbscan' : ['Dev/Services/hdbscan.md', 'Wiki/Concepts/HDBSCAN.md']
  ```
  Effet direct : `uv run AI/scripts/query_index.py --name shap` renvoie 2 correspondances.
  L'agent qui suit l'etape 2 du skill (« verifier l'existence de la page ») doit alors
  arbitrer sans regle, sur un signal ambigu. `[[hdbscan]]` en lien nu est de meme ambigu
  dans Obsidian ; il n'existe que 4 collisions de stem dans tout le vault, dont celle-la.
- **Portee** : 52 anomalies (41 + 10 + 1) sur 337 fiches portant des alias. Aucune n'est
  aujourd'hui une erreur factuelle : `shap` *est* legitimement un alias du concept et le nom
  du service. Ce sont des collisions structurelles, pas des fautes de contenu.
- **Cause** : les alias servent deux usages incompatibles qu'on n'a pas distingues — la
  **resolution de liens** (doit etre unique) et le **rappel semantique** (« ce concept parle
  aussi de SHAP », qui n'a aucune raison d'etre unique).
- **Recommandation** : ne pas imposer l'unicite globale — elle detruirait un usage
  legitime. Trancher l'ambiguite la ou elle nuit :
  1. dedupliquer d'abord les 10 doublons internes a la casse (pur bruit, 0 arbitrage) ;
  2. rendre `query_index.py --name` **explicite sur l'ambiguite** : lorsqu'il renvoie plus
     d'une correspondance, le signaler comme tel, en indiquant la galaxie de chacune, pour
     que le skill sache qu'il doit choisir ;
  3. puis regle **souple** dans `check_brain` : un alias qui est le `nom:` d'une autre page
     dans la **meme galaxie** est un vrai conflit (10 cas au total, dont 4 intra-`dev/` :
     `tensorrt-llm`, `neo4j`, `jupysql`, `doctr`). Inter-galaxie (`dev` ↔ `wiki`), c'est
     l'usage semantique : ne pas le signaler.
- **Effort** : S pour le point 1, S pour le point 2, M pour le point 3 (l'arbitrage des
  4 cas intra-dev demande une lecture). Fichiers : 10 fiches `Dev/Services/`,
  `AI/scripts/query_index.py`, `AI/scripts/check_brain.py`.

### C7. Joignabilite des URLs : 8 liens morts sur 652, mesures exhaustivement — gravite : mineur

- **Constat** : le brief propose d'echantillonner 20-30 fiches pour estimer le taux. Le
  balayage complet des 652 URLs coute ~90 s avec 12 requetes en parallele — l'echantillon
  n'etait pas necessaire. Resultat exact : **8 URLs mortes** (1,2 %), sur 7 pages.
- **Preuve** : `curl -sS -o /dev/null -w '%{http_code}' -L --max-time 25` sur les 652
  valeurs de `url_docs` / `url_repo`, puis verification DNS des echecs de connexion :
  ```
  638 x 200 | 5 x 404 | 3 x 403 | 3 x 000 | 1 x 429 | 1 x 307 | 1 x 302

  # mortes (8) — a corriger :
  404  https://github.com/stan-smith/FossFLOW              Dev/Outils/FossFLOW.md  (url_docs ET url_repo)
  404  https://lancedb.com/documentation/                  Dev/Services/LanceDB.md
  404  https://www.drawio.com/doc/                         Dev/Outils/draw.io.md
  404  https://docs.langchain.com/oss/.../sql_database     Dev/Services/LangChain SQL agent.md
  000  https://jupysql.ploomber.io/       → NXDOMAIN       Dev/Services/jupysql.md
  000  https://segment-anything.com/      → NXDOMAIN       Dev/Services/segment-anything.md
  000  https://www.nnsight.net            → TLS echoue sur www ; https://nnsight.net = 200
                                                            Dev/Services/nnsight.md
  # a l'oeil, pas des defauts du vault (6) : 403 dev.mysql.com x2, 403 docs.opencv.org,
  # 429 web-check.xyz, 302 en boucle milvus.io/docs, 307 sans Location lmstudio.ai/docs
  ```
  `nnsight` est le cas le plus instructif : le domaine existe, seul le prefixe `www.` casse
  le certificat. Un controle qui se contente du code HTTP le detecte ; une relecture humaine
  ne l'aurait jamais vu.
- **Portee** : 652 URLs, 337 fiches, 7 pages a corriger.
- **Cause** : les URLs sont verifiees a la creation (le skill l'impose : « faits verifies sur
  le web, d'office ») et jamais apres. Un lien de documentation se perime par
  reorganisation du site amont, sans aucun signal cote vault.
- **Recommandation** : **ne pas** mettre ce controle dans `check_brain` — il rendrait le
  garde-fou dependant du reseau et couterait 90 s a chaque validation. Un script distinct
  (`AI/scripts/check_urls.py`), lance mensuellement en CI planifiee (`schedule: cron`),
  ecrivant un rapport plutot que sortant en erreur. Tolerer 403/429 (protections anti-bot)
  et ne remonter durement que 404 et NXDOMAIN.
- **Effort** : S (< 1 h) pour le script + le workflow planifie ; S pour corriger les
  7 pages. Fichiers : `AI/scripts/check_urls.py` (a creer),
  `.github/workflows/check-urls.yml` (a creer), 7 fiches Dev.

### C8. `remplace_par:` est un champ mort, et l'incoherence `status` / `maturite` n'est pas vue — gravite : mineur

- **Constat** : `remplace_par:` est present sur les 297 fiches `service` et **rempli sur
  aucune**. Il n'a donc aucune coherence a controler — la question 5 du brief (« une page
  remplacee doit-elle rester `status: actif` ? ») n'a pas d'objet en l'etat. En revanche une
  incoherence voisine existe et n'est pas vue : `AutoGen` porte `maturite: deprecated` et
  `status: actif`.
- **Preuve** :
  ```
  # pages avec remplace_par non vide : aucune (297 champs, tous [] ou None)
  # status != actif (9) — remplace_par vide dans les 9 cas :
  Vanna abandonne | Neptune abandonne | TorchServe abandonne | Marqo abandonne
  pykan en-eval | t3code en-eval | Maka en-eval | swarm-forge en-eval | osint4all abandonne
  # maturite == deprecated (4) :
  AutoGen    status=actif      <-- incoherent
  Neptune    status=abandonne | TorchServe status=abandonne | Marqo status=abandonne
  ```
- **Portee** : 1 incoherence reelle ; 297 champs inutilises.
- **Cause** : `remplace_par` a ete repris de la v1 dans le gabarit v2 sans usage
  identifie. C'est exactement le motif que la spec reproche a `score` et `mes_projets`
  (`brain-v2.md` §5.1 : « jamais remplis a la main → ils mentent »).
- **Recommandation** : arbitrage du proprietaire (cf. *Questions ouvertes*) — soit
  supprimer `remplace_par` du gabarit, soit le documenter avec sa regle d'emploi. Dans les
  deux cas, ajouter une regle **souple** : `maturite: deprecated` implique
  `status != actif` (1 violation), et `status: abandonne` sans `remplace_par` ni mention
  d'alternative merite un avertissement (4 violations).
- **Effort** : S (< 1 h). Fichiers : `AI/scripts/check_brain.py`,
  `Templates/Service-Dev.md`, `AI/design/brain-v2.md` §5.1, `Dev/Services/AutoGen.md`.

### C9. Les comparatifs `.base` derivent silencieusement avec `categorie` et `tags` — gravite : mineur

- **Constat** : l'appartenance d'une fiche a un comparatif n'est pas ecrite dans la fiche :
  elle est **deduite** d'un filtre. Sur 47 `.base`, 28 filtrent sur `categorie ==`, 16 sur
  `file.hasTag()`, 3 autrement — dont un qui **code en dur une liste de noms**. Modifier la
  `categorie` ou un `tag` d'une page la fait donc entrer ou sortir d'un comparatif sans
  aucune trace. Symetriquement, rien ne verifie qu'un comparatif a encore des membres.
- **Preuve** : reevaluation des 47 filtres contre le vault, avec prise en charge de
  `categorie ==`, `.startsWith()`, `file.hasTag()`, `tags.contains()` et `file.name ==`
  (`/tmp/.../probe8.py`) :
  ```
  pages Dev service/outil : 336 | couvertes par >=1 comparatif : 282 | dans aucun : 54
  comparatif a moins de 2 membres (1) :
    "Comparatif - Solveurs d'optimisation"  filtre = categorie == tooling/optim  -> 1 membre
  categories Dev a 3+ pages partiellement ou totalement hors comparatif (5) :
    storage 6/6 hors | tooling/notebook 5/5 | tooling/test 3/3
    tooling/package 6/9 | framework/backend 2/3
  .base jamais cites par aucune page (3) : 'Detection & segmentation', 'Forecasting',
                                            "Suivi d'experiences ML"
  # 'Comparatif - Frontends web legers' a bien 5 membres, mais par liste de noms codee en
  # dur : file.name == "FastAPI" | "HTMX" | "Streamlit" | "Gradio" | "Dash".
  ```
- **Portee** : 47 comparatifs, 54 fiches hors couverture, 5 categories a combler,
  1 comparatif a un seul membre, 3 non cites, 1 filtre code en dur.
- **Cause** : les `.base` sont des vues dynamiques Obsidian — c'est leur interet — mais rien
  ne relie la vue a la population qu'elle est censee couvrir. Le seul comparatif a liste
  codee en dur (`Frontends web legers`) est la trace d'un contournement de ce manque.
- **Recommandation** : regle **souple** dans `check_brain`, en trois volets :
  (a) toute categorie Dev a 3 pages ou plus doit etre couverte par un `.base` — 5 violations ;
  (b) tout `.base` doit avoir au moins 2 membres — 1 violation ;
  (c) tout `.base` doit etre cite par au moins une page — 3 violations.
  Convertir le filtre par noms de `Frontends web legers` en filtre par `categorie`/`tags`,
  faute de quoi un renommage le videra sans bruit.
- **Effort** : S (< 1 h) pour la regle ; M si l'on cree les 5 comparatifs manquants.
  Fichiers : `AI/scripts/check_brain.py`, `Dev/Patterns/*.base`.

### C10. La documentation du controle decrit un outillage qui n'existe plus — gravite : mineur

- **Constat** : `AI/scripts/README.md` — le document qu'un mainteneur lit pour savoir
  comment auditer le vault — ne mentionne **aucun** des six scripts Python de la v2
  (`check_brain`, `build_index`, `build_mocs`, `build_links`, `query_index`,
  `audit_mesures`). Il decrit cinq scripts PowerShell qui ciblent l'arborescence v1, renvoie
  vers un dossier de sortie `AI/audits/` qui n'existe pas, et vers un skill `add-service`
  qui n'existe pas non plus.
- **Preuve** :
  ```
  $ grep -c check_brain AI/scripts/README.md      → 0
  $ ls AI/audits                                   → No such file or directory
  $ grep -n "add-service" AI/scripts/README.md
  | gen-stubs-batch.ps1 | ... (deprecie — utiliser le skill `add-service`) |
  $ ls .claude/skills/                             → enrichir-brain  planifier-projet
  $ grep -l 'Services/VectorDB\|"Bugs"' AI/scripts/*.ps1
  audit-links.ps1  discover-links.ps1  audit-vault.ps1  gen-stubs-batch.ps1
  ```
  `CLAUDE-build.md:37` aggrave le point : il oriente vers `audit-vault.ps1` a egalite avec
  `check_brain.py` pour « auditer » — vers un script v1 donc.
- **Portee** : 1 fichier de doc, 4 scripts `.ps1` obsoletes, 1 renvoi errone dans
  `CLAUDE-build.md`.
- **Cause** : la v2 a ajoute son outillage a cote de celui de la v1 sans retirer l'ancien ni
  reecrire l'index qui le decrit.
- **Recommandation** : reecrire `AI/scripts/README.md` autour des scripts v2, en marquant
  explicitement les `.ps1` comme heritage v1 lecture seule (ou les deplacer sous
  `AI/scripts/v1/`), et corriger le renvoi de `CLAUDE-build.md:37`. Un garde-fou dont la
  documentation designe le mauvais outil ne sera pas lance.
- **Effort** : S (< 1 h). Fichiers : `AI/scripts/README.md`, `CLAUDE-build.md`.

## Ce qui va bien

- **Les six artefacts generes sont exactement synchrones avec le vault.** C'est le resultat
  le plus solide de l'audit, et il etait le moins previsible. `brain-index.json` : 647/647
  pages, 0 champ divergent sur les 9 champs indexes des 647 pages. Les 31 MOC : 0 pitch
  perime, 0 lien mort. `liens.md` : 0 page en trop, 0 page manquante. Preuve :
  ```
  index count: 647 | pages vault: 647
  dans l'index mais plus dans le vault: [] | dans le vault mais absentes de l'index: []
  champs derives: {}
  31 MOC ; lignes a pitch perime: 0 ; liens morts: 0
  liens.md : 0 en trop, 0 manquant
  ```
  Conclusion pratique : la sequence `build_index` → `build_mocs` → `build_links` est
  reellement relancee en fin de flux, et elle est idempotente. **Il n'y a rien a corriger
  cote generation** — c'est le declencheur du *controle* qui manque (C3), pas celui de la
  *generation*.
- **Les six regles dures de `check_brain` tiennent.** `647 pages actives controlees / OK —
  aucune violation dure`, 0 avertissement de taille. Sur 796 wikilinks presents dans les
  frontmatter (`alternatives:`, `remplace_par:`) — que le script ne scanne pourtant pas,
  puisqu'il ne lit que le corps — **0 est mort**. Le trou existe (annexe B, R2) mais n'a
  jamais ete exploite.
- **Le frontmatter est d'une uniformite remarquable pour 647 pages ecrites au fil de l'eau** :
  0 champ a geometrie variable sur les 6 types, y compris les 4 types non controles. La
  discipline de gabarit a tenu sans script pour la faire tenir.
- **La coherence frontmatter → section `## Alternatives` est parfaite** : 0 page sur 337
  cite une alternative en frontmatter sans la lister en section. Les 3 ecarts existants vont
  dans l'autre sens et sont deliberes (C2).
- **`domaines:` est propre** : 0 valeur hors de `themes.md` sur 6 valeurs declarees et
  330 emplois — et cela **sans aucun controle**. La regle R4 de l'annexe B peut donc etre
  durcie immediatement, a cout nul.
- **Le vocabulaire de tags est exactement satur** : 321 declares, 321 employes, 0 orphelin.
  1 seule page sans tag sur 647 (`Dev/Outils/public-apis.md`).
- **`audit_mesures.py` est un bon socle** : reproductible, sans horodatage, et il documente
  lui-meme son propre perimetre d'aveuglement (§10). C'est ce qui a rendu cet audit possible
  en une passe. Ne pas le modifier.

## Questions laissees ouvertes

1. **Guidance ↔ Outlines (C2)** : les deux pages remplacent le pitch de l'autre par une
   comparaison redigee (« meme famille mais orientee schema → sortie » / « ... orientee
   langage de controle »). C'est du contenu de meilleure qualite que le pitch reinjecte,
   mais il viole la regle. Faut-il autoriser une **surcharge editoriale explicite** de la
   ligne d'alternative — par exemple un champ `## Alternatives` a deux niveaux, pitch puis
   commentaire — ou aligner ces deux pages sur la regle et perdre la comparaison ?
2. **`remplace_par:` (C8)** : champ supprime du gabarit, ou documente avec sa regle d'emploi ?
   Les 297 occurrences vides plaident pour la suppression, mais la question de la succession
   d'un outil abandonne reste, elle, legitime.
3. **Porte d'entree des Patterns et Rules (C5)** : leur donner une `categorie:` — ce qui
   ouvre `pattern/*` et `rule/*` dans la taxonomie, donc empiete sur l'axe 1 — ou ajouter a
   `build_mocs` deux hubs groupes par `type:` sans toucher a la taxonomie ? Arbitrage a
   coordonner avec l'axe 1.
4. **Vocabulaire `domaine:` des Rules (C4)** : les 5 valeurs (`security`, `dependencies`,
   `tests`, `code-style`, `docs`) constituent un cinquieme vocabulaire non declare, a cote
   de `tags.md`, `taxonomie.md`, `themes.md` et de l'enum `applicable`/`strictness`. Le
   declarer dans `Documentation/general/`, ou fusionner ces valeurs dans les tags existants ?
5. **Sequence de durcissement** : l'annexe B propose 5 regles durcissables a cout nul
   (0 violation) et 6 regles souples. Faut-il durcir les 5 immediatement, en un lot, avant
   toute correction de contenu — ou attendre que l'axe 1 ait tranche le rangement, au risque
   que de nouvelles pages soient ecrites sans garde-fou entre-temps ?
6. **Perimetre du controle** : `check_brain` ne scanne que `Dev/` et `Wiki/`. `MOC/` est
   genere donc suppose sain (verifie : 0 lien mort), mais `Documentation/`, `Templates/`,
   `Projects/` et `AI/` ne sont controles par rien. Un lien mort dans `Documentation/` casse
   la gouvernance sans que rien ne le dise. Etendre le scan, ou l'assumer ?

---

## Annexe A — Champ modifie → effets de bord a propager

Convention : **[M]** = propagation manuelle obligatoire (rien ne la fera a votre place) ;
**[G]** = corrige par relance d'un script generateur ; **[D]** = deja couvert par une regle
dure de `check_brain` ; **[!]** = derive silencieuse, aucun controle n'existe.

| Champ modifie | Consommateurs a repropager | Volume dans le vault | Verification |
|---|---|---|---|
| `pitch:` | **[M]** lignes `## Alternatives` des pages qui citent la cible · **[G]** puces des MOC (`build_mocs`) · **[G]** `brain-index.json/.md` · lu en direct par 47 vues `.base` (colonne `pitch`, rien a faire) | 801 lignes reinjectees ; 2,4 citeurs par page en moyenne | **[!]** aucune — objet de C2 et de la regle R1 |
| `nom:` | **[M]** nom du fichier (`.md`) · **[D]** wikilinks `[[nom]]` du corps des autres pages · **[!]** wikilinks du frontmatter `alternatives:` / `remplace_par:` des reciproques · **[M]** libelles des puces `## Alternatives` · **[!]** listes de noms codees en dur dans les `.base` (1 fichier, 5 noms) · **[M]** nom du fichier `Dev/REX/REX - <nom>.md` et champ `service:` de ce REX · **[G]** index, MOC, liens | 796 liens en frontmatter ; 1 `.base` a liste dure | partielle : corps oui **[D]**, frontmatter non **[!]** (R2) |
| `categorie:` | **[D]** doit exister dans `taxonomie.md` · **[!]** appartenance a 28 comparatifs `.base` filtres par `categorie ==` ou `.startsWith()` — entree/sortie silencieuse · **[G]** hub `MOC/Categories/<tete>` (la page change de hub) · **[M]** jeu d'alternatives pertinentes (les pairs de categorie) | 28 `.base` ; 86 categories portees | partielle : valeur oui **[D]**, effet sur les vues non **[!]** (R8) |
| `tags:` | **[D]** doivent exister dans `tags.md` · **[!]** appartenance a 19 comparatifs `.base` filtres par `file.hasTag()` / `tags.contains()` — entree/sortie silencieuse · **[G]** index des tags de `liens.md` et liste « tags sans page concept » | 19 `.base` ; 321 tags | partielle : valeur oui **[D]**, effet sur les vues non **[!]** (R8) |
| `status:` | **[!]** 2 `.base` filtrent `status == "actif"`, 19 vues l'affichent ou l'ordonnent — une page peut disparaitre d'une vue sans bruit · **[!]** coherence avec `maturite` et `remplace_par` | 19 vues | **[!]** aucune (R6) |
| `maturite:` | **[D]** enum fermee · **[!]** 3 `.base` filtrent `maturite != "deprecated"`, 1 filtre `== "production"`, 41 vues l'affichent · **[!]** coherence avec `status` (1 incoherence actuelle) | 41 vues | partielle : enum oui **[D]**, coherence non **[!]** (R6) |
| `alias:` | **[!]** resolution des liens `[[alias]]` · **[!]** detection d'existence du skill (`query_index --name`, etape 1-2) · unicite | 337 fiches a alias ; 52 collisions | **[!]** aucune (R5) — objet de C6 |
| `domaines:` | **[G]** comptes par sous-domaine des `MOC/Themes/*` · **[!]** appartenance au vocabulaire `themes.md` | 330 emplois, 6 valeurs | **[!]** aucune (R4), 0 violation de fait |
| `alternatives:` | **[D]** reciprocite (si A cite B, B cite A) · **[M]** la section `## Alternatives` doit lister les memes cibles · **[M]** la ligne de chaque cible doit porter son pitch (C2) | 796 liens ; 334 sections | reciprocite **[D]** ; section ⊇ frontmatter **[!]** (R11, 0 violation) |
| `licence_type:`, `hosted:`, `scaling:`, `langage:` | **[D]** enums fermees (sauf `langage`) · lus en direct par les vues `.base` (59, 34, 47, 71 vues) — rien a propager | — | **[D]** |
| Renommage du fichier | **[D]** liens `[[Dev/Services/X\|X]]` du corps · **[!]** memes liens en frontmatter · **[M]** champ `nom:` · **[!]** listes de noms codees en dur (`Frontends web legers`) · **[G]** index, MOC, liens | 796 liens en frontmatter | partielle **[D]** / **[!]** (R2) |
| Suppression d'une page | **[D]** liens morts dans le corps des citeurs · **[!]** liens morts en frontmatter · **[!]** reciprocite : `check_brain` ignore silencieusement une cible absente de l'index (`if b in by_name`) · **[G]** index, MOC, liens · **[!]** un `.base` peut tomber a 0 membre | 0 cible d'alternative hors index aujourd'hui | partielle **[D]** / **[!]** (R2, R8) |
| `url_docs:`, `url_repo:` | **[!]** joignabilite (8 mortes sur 652) | 652 URLs | **[!]** aucune (R10) — objet de C7 |

Lecture : la colonne **[!]** est la surface exacte de l'axe 2. Sept champs sur douze ont au
moins un consommateur qu'aucun controle ne surveille, et le pire cas n'est pas le lien mort
— celui-la se voit — mais la **sortie silencieuse d'une vue `.base`** : la page reste
valide, le comparatif reste valide, et l'information disparait sans erreur.

## Annexe B — Regles a ajouter a `check_brain`, par ordre de mise en oeuvre

Le nombre de violations actuelles est le **cout de mise en conformite avant durcissement**.
Une regle a 0 violation se durcit le jour meme ; une regle a 52 violations doit rester
souple jusqu'a arbitrage, sinon elle bloque tout le vault.

### Lot 1 — durcissables immediatement (cout de conformite nul)

| # | Regle | Violations | Durete | Effort |
|---|---|---|---|---|
| R2 | Les wikilinks du **frontmatter** (`alternatives:`, `remplace_par:`) entrent dans le controle de liens morts, au meme titre que ceux du corps | **0** / 796 liens | dure | S |
| R3 | Gabarits `outil`, `pattern`, `rule`, `rex` declares dans `ALLOWED` + `REQUIRED`, derives des listes de champs constatees (C4) | **0** / 51 pages | dure | S |
| R4 | `domaines:` ⊆ vocabulaire de `themes.md` | **0** / 330 emplois | dure | S |
| R11 | La section `## Alternatives` liste au moins toutes les cibles du frontmatter `alternatives:` | **0** / 337 fiches | dure | S |
| R12 | La reciprocite echoue explicitement si la cible d'une alternative est absente de l'index, au lieu d'etre ignoree en silence (`if b in by_name`) | **0** | dure | S |

Ces cinq regles ferment cinq angles morts sans exiger la moindre correction de contenu.
C'est le lot a passer en premier, et sans arbitrage prealable.

### Lot 2 — a corriger, puis durcir

| # | Regle | Violations | Sequence | Effort |
|---|---|---|---|---|
| R1 | Pitch reinjecte, **reformule** : si la cible est dans `alternatives:`, la ligne commence par le `pitch:` courant (normalisation `**` et espaces) ; suffixe libre autorise ; puce hors `alternatives:` exemptee | **7** (5 pitchs perimes + 2 gras) — 14 sous la formulation actuelle | corriger les 7, arbitrer Guidance ↔ Outlines, puis dure | S + M (script) |
| R6 | `maturite: deprecated` ⇒ `status != actif` | **1** (`AutoGen`) | corriger, puis dure | S |
| R10 | Joignabilite des URLs — **hors `check_brain`**, script dedie en CI planifiee ; 404 et NXDOMAIN durs, 403/429 tolerés | **8** / 652 | corriger les 7 pages, puis dure dans le job dedie | S |

### Lot 3 — souples, en attente d'arbitrage

| # | Regle | Violations | Pourquoi souple | Effort |
|---|---|---|---|---|
| R5 | Un `alias:` qui est le `nom:` d'une autre page **de la meme galaxie** est un conflit ; doublons internes a la casse interdits | **52** au total, dont **10** doublons internes (bruit pur) et **4** conflits intra-`dev` | l'unicite globale detruirait l'usage semantique legitime (`shap`, `yolo`, `map`) | S puis M |
| R7 | Toute page `Dev/` ou `Wiki/` doit etre atteignable depuis un MOC | **11** | depend de l'arbitrage C5/Q3 (categorie vs hub par type) | S apres C5 |
| R8 | (a) categorie Dev a 3+ pages couverte par un `.base` ; (b) `.base` a 2 membres minimum ; (c) `.base` cite par au moins une page ; (d) aucun filtre `.base` par liste de noms codee en dur | (a) **5** · (b) **1** · (c) **3** · (d) **1** | creer 5 comparatifs est une decision editoriale, pas technique | S (regle) / M (contenu) |
| R9 | `nom:` identique au nom du fichier | **2** (`A/B testing`, `ROC-AUC / courbe PR`) | les 2 cas sont legitimes : `/` est interdit dans un nom de fichier — la regle doit prevoir l'exemption | S |
| R13 | `build_mocs.py` imprime le nombre de pages Dev ecartees faute de `categorie:` | **11** ecartees aujourd'hui, en silence | ce n'est pas une regle de `check_brain` mais la fin d'un silence dans un generateur | S |

### Ce qui ne doit **pas** entrer dans `check_brain`

- **La joignabilite des URLs** (R10) : 652 appels reseau, ~90 s, dependance a des services
  tiers et a des protections anti-bot. Un garde-fou doit etre rapide, hors-ligne et
  deterministe. Job planifie separe.
- **Un controle en `PostToolUse`** : il signalerait des etats intermediaires legitimes — une
  page creee avant sa reciproque viole la reciprocite pendant quelques secondes. Le bon
  point d'accroche est `Stop` (etat stable, une fois par session) double d'une CI sur
  `push` (seul filet qui couvre les editions faites dans Obsidian).
