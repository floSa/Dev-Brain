# Rapport d'audit — Axe 5 : Navigation & exploitabilite

Auditeur : conversation « audit axe 5 », le 2026-09-02. Socle : `mesures-axe5.md`, relance le
2026-09-02 — **identique octet pour octet** a `mesures-2026-09-02.md` (`diff` vide). Les scripts
d'ecriture (`build_index`, `build_mocs`, `build_links`) n'ont pas ete lances ; seuls
`check_brain.py` et `audit_mesures.py` l'ont ete.

## Synthese

Le brain sert bien son consommateur humain sur 635 pages sur 647, et mal sur les 12 restantes,
qui sont exactement les 6 types de pages que la taxonomie ne couvre pas. La cause est unique et
mecanique : `build_mocs.py` groupe sur `categorie:`, or 11 pages (5 Patterns, 5 Rules, 1 REX)
n'ont pas ce champ — elles sortent de toutes les MOC, de l'index utile et du graphe. Cote agent,
l'index perd neuf champs eliminatoires presents sur 297 fiches service sur 297. Si on ne fait
qu'une chose : faire generer a `build_mocs.py` deux hubs supplementaires a partir de `type:`
(Patterns, Rules) et les cabler depuis `Home.md` — une heure, et 11 pages invisibles redeviennent
navigables.

## Ecarts avec le brief

Le socle relance ne bouge pas. Le **brief**, lui, s'ecarte du vault sur trois points. Le vault
fait foi.

| Brief `axe-5-navigation.md` | Vault au 2026-09-02 | Preuve |
|---|---|---|
| « 19 pages ne sont citees par aucune autre » | **12** selon la definition du socle ; **10** apres correction de deux artefacts de mesure ; **5** si les MOC comptent comme sources | `mesures-axe5.md` §6, et C9 ci-dessous |
| « les 5 Patterns et les 5 Rules — 100 % de ces deux dossiers » orphelins | **3 Patterns sur 5** orphelins ; **0 Rule** orpheline au sens de la mesure, mais **les 5 Rules sont inatteignables** (ilot ferme, C3) | C1, C3 |
| « Il n'existe aucune page d'entree unique du vault » | **`Home.md` existe** — mais il est ecrit a la main et ne cite que 3 MOC sur 31 | C2 |

Le brief est donc pessimiste sur le compte des orphelins et optimiste sur les Rules : la mesure
« lien entrant » les declare saines alors qu'elles ne sont accessibles par aucun chemin.

## Constats

### C1. Onze pages n'ont pas de `categorie:` et sortent de toutes les MOC — gravite : bloquant

- **Constat** : `build_mocs.py` groupe les pages `galaxie: dev` par tete de `categorie:`
  (`head = (p.get("categorie") or "").split("/")[0]`, ligne 106). Une categorie vide est falsy,
  la page est ignoree. Les 5 Patterns, les 5 Rules et le REX n'ont pas de `categorie:` — ni de
  `nom:`, ni de `pitch:`. Aucune MOC ne les liste. Ils ne sont pas non plus atteignables par les
  MOC/Themes, qui ne lisent que les pages `galaxie: wiki` de categorie `concept/*`.
- **Preuve** :
  ```
  $ python3 -c "import json; d=json.load(open('AI/index/brain-index.json'));
    print([p['path'] for p in d['pages'] if not p.get('categorie')])"
  ['Dev/Patterns/Pattern - Agent sur LLM auto-hébergé.md', ... 5 Patterns ...,
   'Dev/REX/REX - Postgres.md', 'Dev/Rules/Rule - Config typée.md', ... 5 Rules ...]   # 11
  ```
  Entree type dans l'index : `{"path": "Dev/Rules/Rule - Config typée.md", "nom": "Rule - Config
  typée", "alias": null, "type": "rule", "galaxie": "dev", "categorie": null, "domaines": null,
  "pitch": null, "tags": [...], "alternatives": null}` — six champs sur dix a `null`.
  Reachability, depuis `Home.md` + les 31 MOC, tous liens suivis a profondeur infinie :
  ```
  noeuds: 726 (dont 31 MOC)
  atteignables depuis Home + 31 MOC: 712  -> inatteignables: 14
     Dev/Patterns/Comparatif - Détection & segmentation.base
     Dev/Patterns/Comparatif - Forecasting.base
     Dev/Patterns/Comparatif - Suivi d'expériences ML.base
     Dev/Patterns/Pattern - Moteur de jeu pur + IA séparée.md
     Dev/Patterns/Pattern - Pipeline scraping → matching → optimisation.md
     Dev/Patterns/Pattern - RAG structuré graphe + human-in-the-loop.md
     Dev/Patterns/Pattern - Stack démo ML locale multi-services.md
     Dev/REX/REX - Postgres.md
     Dev/Rules/Rule - Config typée.md   (+ les 4 autres Rules)
     Wiki/Outils/Obsidian.md
  ```
  (script reproductible conserve hors vault ; il resout un wikilink par chemin complet, puis par
  nom de fichier, et parcourt en largeur depuis `Home.md` et les 31 MOC.)
- **Portee** : 12 pages `.md` non couvertes par une MOC (11 sans `categorie:` +
  `Wiki/Outils/Obsidian.md`, qui est `galaxie: wiki` mais de categorie `skill/knowledge`, donc
  hors du filtre `concept/*`). 14 nœuds inatteignables au total en comptant 3 vues `.base`
  (cf. C11). Soit 635 pages couvertes par une MOC sur 647.
- **Cause** : `Documentation/general/taxonomie.md` ne definit aucune categorie pour les types
  `pattern`, `rule`, `rex` (`grep -niE 'pattern|rule|rex' taxonomie.md` → aucune ligne). Les
  gabarits `Templates/Pattern.md` et `Templates/Rule.md` ne portent donc ni `nom:`, ni
  `categorie:`, ni `pitch:` — ils portent a la place `contexte:`, `services_cles:`, `domaine:`,
  `applicable:`, `strictness:`, `created:`, `modified:`, qu'aucun script ne lit. `build_mocs.py`
  a ete ecrit pour les deux gabarits controles (`service`, `concept`) et n'a jamais eu de branche
  pour les quatre autres.
- **Recommandation** : ajouter dans `build_mocs.py` un troisieme groupement, par `type:` et non
  par `categorie:`, produisant `MOC/Types/Patterns.md` et `MOC/Types/Rules.md` (et, quand l'axe 6
  aura tranche, `MOC/Types/REX.md`). Etendre le filtre wiki de `concept/*` a « toute page
  `galaxie: wiki` », ce qui rattrape `Wiki/Outils/Obsidian.md`. Ne **pas** inventer une
  `categorie:` pour ces types : ce serait de la taxonomie, donc de l'axe 1. Le champ `type:`
  existe deja, est fiable a 100 % et suffit.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_mocs.py` (~30 lignes : un
  dictionnaire `TYPE_LABEL`, une boucle calquee sur celle des categories, un dossier
  `MOC/Types/`), plus 2 lignes dans `Home.md`. Aucune page `Dev/` touchee.

### C2. La couche MOC n'a elle-meme pas de point d'entree — gravite : serieux

- **Constat** : 31 MOC existent, mais 17 d'entre elles ne recoivent aucun lien entrant. Rien ne
  les relie entre elles au niveau superieur : il n'y a pas de MOC des MOC. `Home.md` existe mais
  est ecrit a la main et cite 3 hubs sur 31. Un humain qui ouvre le vault sans connaitre
  l'arborescence ne trouve donc ni `MOC/Categories/Machine Learning`, ni `MOC/Themes/MLOps`,
  autrement que par l'explorateur de fichiers.
- **Preuve** :
  ```
  === MOC : liens entrants ===
    0 <- MOC/Categories/Auth.md
    0 <- MOC/Categories/Automatisation no-code.md
    1 <- MOC/Categories/Bases de données.md
    0 <- MOC/Categories/Calcul distribué.md          ... 14 des 15 MOC/Categories a 0
    0 <- MOC/Themes/Data Science.md
    0 <- MOC/Themes/ML Engineering.md
    0 <- MOC/Themes/MLOps.md                          ... 3 des 5 MOC/Themes a 0
  ```
  ```
  $ grep -c '^- \[\[MOC/' Home.md
  3
  ```
  Depuis `Home.md` seul, 649 nœuds sur 726 sont atteignables : **77 nœuds sont hors de portee**
  d'une navigation partant de l'accueil.
- **Portee** : 17 MOC sur 31 sans backlink ; 77 nœuds sur 726 hors de portee depuis `Home.md`.
- **Cause** : `build_mocs.py` genere les feuilles de l'arborescence de navigation mais pas sa
  racine. `Home.md` a ete ecrit a la main a un moment ou il y avait peu de MOC, et n'a pas de
  zone `<!-- AUTO:START -->` : il ne peut donc pas etre mis a jour par le generateur, contrairement
  aux MOC, qui en ont une.
- **Recommandation** : faire generer par `build_mocs.py` une page `MOC/Index.md` listant les 31
  hubs groupes par etage (Themes, Concepts, Categories, Types), sur le meme mecanisme
  `upsert()` deja en place. Poser dans `Home.md` un unique lien vers elle, et retirer les 3 liens
  MOC en dur, qui derivent des qu'un hub est cree ou renomme.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_mocs.py` (~15 lignes, reutilise
  `upsert()` et la liste `written` deja construite en fin de `main()`), `Home.md` (3 lignes).

### C3. Les 5 Rules forment un ilot ferme — gravite : serieux

- **Constat** : les 5 pages de `Dev/Rules/` se citent mutuellement, et **rien d'autre ne les
  cite**. Aucune fiche Service, aucun Outil, aucun Concept, aucune MOC ne pointe vers une Rule.
  La mesure « pages sans lien entrant » du socle les declare donc saines — a tort : leur seul
  lien entrant vient de l'interieur de l'ilot.
- **Preuve** :
  ```
  $ grep -rn --include='*.md' -oE '\[\[Dev/Rules/[^]|]+' Dev/ Wiki/ MOC/
  (aucune sortie)

  $ grep -rn --include='*.md' -oE '\[\[[^]|]*Rule - [^]|]*' Dev/ Wiki/ MOC/
  Dev/Rules/Rule - Config typée.md:59:[[Rule - Qualité stricte
  Dev/Rules/Rule - Config typée.md:59:[[Rule - Structure de projet
  ... 12 occurrences, toutes emises depuis Dev/Rules/
  ```
  Consequence en cascade : `Dev/Patterns/Pattern - Stack démo ML locale multi-services.md` n'a
  qu'un seul lien entrant, emis par `Dev/Rules/Rule - Packaging démo.md`. Il est donc atteignable
  depuis une page elle-meme inatteignable — d'ou sa presence dans la liste des 14 nœuds isoles
  de C1.
- **Portee** : 5 pages `Dev/Rules/`, plus 1 Pattern isole par ricochet.
- **Cause** : les Rules sont consommees par le skill `planifier-projet`, qui les injecte en fin de
  plan (section « Contraintes pour l'IA de dev »). Le skill les lit par chemin de dossier, pas par
  lien. Aucune boucle de retour ne les rattache au reste : une fiche Service n'a aucune raison,
  dans son gabarit, de citer une regle transverse.
- **Recommandation** : le hub `MOC/Types/Rules.md` de C1 suffit a rendre les 5 pages atteignables
  et est le correctif minimal. Ne pas chercher a cabler des liens Service → Rule : une regle est
  transverse par definition, un lien depuis 297 fiches serait du bruit. Corriger en revanche
  `AI/scripts/build_mocs.py` avant, sinon le correctif de C1 laisse le Pattern
  « Stack demo ML locale » toujours dependant de l'ilot.
- **Effort** : **S** (< 1 h), inclus dans C1. Aucun fichier `Dev/` touche.

### C4. Le seul REX du vault est reference en chemin brut, jamais en wikilink — gravite : serieux

- **Constat** : 46 fiches `Dev/Services/` mentionnent leur REX sous la forme d'un chemin entre
  backticks, `` `Dev/REX/REX - <X>.md` ``. Aucune ne le fait par wikilink. Il en resulte zero
  arete de graphe : `Dev/REX/REX - Postgres.md`, le seul REX qui existe reellement, est
  inatteignable et compte parmi les orphelins.
- **Preuve** :
  ```
  $ grep -rn "REX - " Dev/Services/ Dev/Outils/ | grep -c '`Dev/REX/'
  46
  $ grep -rn --include='*.md' -oE '\[\[[^]|]*REX[^]|]*' Dev/ Wiki/
  (aucune sortie)
  $ grep -n "REX" Dev/Services/Postgres.md
  51:- Retours d'expérience détaillés : `Dev/REX/REX - Postgres.md`.
  65:- `Dev/REX/REX - Postgres.md` — retours d'expérience
  ```
- **Portee** : 46 fiches emettrices, 1 page cible reellement existante. Les 45 autres references
  pointent vers des fichiers absents.
- **Cause** : choix delibere et rationnel a l'origine. `build_links.py` exclut explicitement les
  cibles `rex - *` de la liste des liens non resolus (`elif not key.startswith("rex - ")`,
  ligne 105) : la forme backtick a ete adoptee pour que 46 REX inexistants ne produisent pas 46
  liens morts et ne fassent pas echouer `check_brain.py`. Le prix a payer est que le REX qui
  existe reste invisible.
- **Recommandation** : convertir en wikilink la seule reference dont la cible existe
  (`Dev/Services/Postgres.md`, lignes 51 et 65), et inscrire la regle « des qu'un REX existe, sa
  reference passe en wikilink » dans le skill `enrichir-brain`. Garder la forme backtick pour les
  45 REX en attente. Le pilier REX lui-meme releve de l'axe 6 : si celui-ci conclut a la
  suppression du pilier, ce constat tombe.
- **Effort** : **S** (< 15 min). Fichiers impactes : `Dev/Services/Postgres.md` (2 lignes),
  `.claude/skills/enrichir-brain/SKILL.md` (1 ligne de convention). A coordonner avec l'axe 6.

### C5. L'index perd neuf champs eliminatoires presents sur 297 fiches service sur 297 — gravite : serieux

- **Constat** : `build_index.py` ne recopie que dix champs (`FIELDS`, ligne 37). Neuf autres
  champs, presents sur la totalite des fiches service, n'atteignent jamais l'index :
  `licence_type`, `hosted`, `maturite`, `langage`, `scaling`, `remplace_par`, `status`,
  `url_docs`, `url_repo`. `planifier-projet` filtre sur l'index « sans lire 160 fichiers », donc
  ne peut pas ecarter un candidat sur un critere qu'il possede pourtant deja en frontmatter.
- **Preuve** :
  ```
  champs des fiches service NON repris dans l'index :
    licence_type   297/297      status         297/297
    hosted         297/297      url_docs       297/297
    maturite       297/297      url_repo       297/297
    langage        297/297
    scaling        297/297      remplace_par   297/297
  ```
  Simulation, archetype 5 « RAG / app LLM » avec l'axe transverse on-prem strict de
  `Documentation/perso/archetypes.md`. Predicat applique :
  `hosted in (self, both) AND licence_type in (open-source, source-available) AND status == actif`.
  ```
  database/vector    index: 11 candidats | apres filtre: 10 | ecarte : Pinecone
  llm/framework      index: 33 candidats | apres filtre: 30 | ecartes : LM Studio Bionic, OpenRouter, Vanna
  llm/local          index:  9 candidats | apres filtre:  8 | ecarte : LM Studio
  llm/eval           index:  4 candidats | apres filtre:  4 | ecarte : aucun
  ```
  Simulation, archetype 2 « App data/ML interactive », meme predicat : `ui/data-app` 3 → 3,
  `ui/ml-demo` 1 → 1, `framework/frontend` 2 → 2, `tooling/viz` 8 → 8 — aucun ecarte.
  ```
  $ python3 -c "... status != actif ..."
  Counter({'actif': 328, 'abandonne': 5, 'en-eval': 4})
  ['Vanna','Neptune','pykan','TorchServe','Marqo','t3code','Maka','swarm-forge','osint4all']
  ```
- **Portee** : 297 fiches service et 39 fiches outil, soit les 336 pages sur lesquelles
  `planifier-projet` travaille. 9 services `abandonne` ou `en-eval` sont indistinguables des 328
  actifs dans l'index.
- **Cause** : `FIELDS` a ete fige a la creation de l'index sur ce qui servait a l'affichage
  humain (`brain-index.md`) plutot que sur ce qui sert au filtrage machine. Les vues
  `Comparatif - *.base` exposent au contraire ces champs au lecteur humain
  (`order: file.name, pitch, langage, licence_type, maturite, scaling, tags, alternatives` dans
  `Comparatif - Forecasting.base`) : l'humain a la table de decision, l'agent ne l'a pas.
- **Recommandation** : ajouter `hosted`, `licence_type`, `status`, `maturite`, `scaling` a
  `FIELDS`. Ces cinq champs sont des enums fermees, deja validees par `check_brain.py`, donc
  filtrables sans ambiguite et sans nouveau travail de saisie. Laisser `langage`, `url_docs`,
  `url_repo`, `remplace_par` dehors : ils ne servent pas a ecarter. Deux avertissements de
  cadrage : le filtre on-prem n'ecarte que 5 candidats sur 57 dans la simulation ci-dessus — le
  gain n'est pas le volume ecarte, c'est de ne plus avoir a ouvrir 57 fichiers pour l'etablir ; et
  ce constat est **distinct** de l'entree 1 de `AI/ameliorations-devbrain.md`, qui propose un
  champ `contraintes:` **nouveau** a saisir a la main. Ici les donnees existent deja, il ne manque
  que leur transport. La presente recommandation ne re-instruit pas l'entree 1 et ne la remplace
  pas : elle la rend moins urgente, puisqu'une partie des eliminations visees (LM Studio Bionic,
  cite en exemple dans l'entree 1) devient possible par `hosted`/`licence_type` seuls.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_index.py` (1 ligne : la liste
  `FIELDS`), `.claude/skills/planifier-projet/SKILL.md` (etape 5, pour dire sur quoi filtrer),
  `AI/scripts/query_index.py` (optionnel : des options `--hosted` / `--status`, ~10 lignes).
  L'index se regenere sans qu'aucune page ne bouge.

### C6. Le champ `domaines:` cote Dev ne produit aucune navigation — gravite : serieux

- **Constat** : 34 pages `galaxie: dev` portent un `domaines:`. `build_mocs.py` ne lit ce champ
  que sur les pages `galaxie: wiki` de categorie `concept/*` (lignes 129-139). Les 34 valeurs
  cote Dev ne produisent donc aucune arete, aucune MOC, aucun regroupement. Corollaire : le theme
  `infra-ops`, cree le 2026-09-02 et pose sur 3 fiches Dev, n'a genere aucune MOC — `MOC/Themes/`
  contient 5 fichiers alors que `THEME_LABEL` en declare 6.
- **Preuve** :
  ```
  $ python3 -c "... domaines par (valeur, galaxie, type) ..."
  ('ai-eng','dev','outil') 21     ('data-eng','dev','outil') 10    ('infra-ops','dev','outil') 3
  ('ai-eng','wiki','concept') 110 ('data-eng','wiki','concept') 16 ('data-sci','wiki','concept') 174
  ('ml-eng','wiki','concept') 163 ('mlops','wiki','concept') 13
  infra-ops: [('Sniffnet','dev','network/analysis'), ('croc','dev','network/transfer'),
              ('osint4all','dev','security/osint')]
  $ ls MOC/Themes/
  AI Engineering.md  Data Engineering.md  Data Science.md  ML Engineering.md  MLOps.md
  ```
  Aucune page `type: service` ne porte `domaines:` — le gabarit `Templates/Service-Dev.md` le lui
  interdit. Le champ n'est donc renseigne que sur 34 des 39 outils Dev.
- **Portee** : 34 pages Dev, 1 theme entier sans hub (`infra-ops`), et l'impossibilite de repondre
  a « quelles briques Dev pour le MLOps ? » par la navigation.
- **Cause** : `domaines:` a ete concu pour l'etagement Wiki (theme → sous-domaine → feuille) puis
  ouvert au gabarit Outil sans que le generateur soit etendu. Rien ne verifie l'ecart :
  `check_brain.py` ne controle pas les valeurs de `domaines:` (constat repris au §10 du socle).
- **Recommandation** : faire lire `domaines:` sur **toutes** les galaxies dans la construction des
  MOC/Themes, et y ajouter une seconde section « Briques Dev » a cote de la section
  « sous-domaines de concepts » existante. Cela cree `MOC/Themes/Infrastructure & Ops.md`
  automatiquement. Ne pas etendre `domaines:` aux 297 fiches service dans cet axe : c'est une
  decision de modele, donc de l'axe 1. **Point de convergence a verifier** : l'axe 1 examine
  `domaines:` du point de vue du modele et peut conclure a son retrait. Si c'est le cas, cette
  recommandation tombe et le theme `infra-ops` doit alors etre retire de `themes.md` et de
  `THEME_LABEL` plutot que dote d'une MOC vide. Les deux axes doivent trancher ensemble.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_mocs.py` (~20 lignes dans la
  boucle `theme_subs`). Sous reserve de l'arbitrage de l'axe 1.

### C7. Deux MOC de categorie deversent 91 et 86 entrees sans etage intermediaire — gravite : mineur

- **Constat** : l'etagement a trois niveaux decrit dans `Documentation/perso/obsidian-graph.md`
  (theme → sous-domaine → feuille) n'existe que cote Wiki. Cote Dev, `MOC/Categories/` est plat :
  une MOC par tete de categorie, qui liste toutes ses feuilles. Deux d'entre elles depassent 85
  entrees.
- **Preuve** :
  ```
  $ for f in MOC/Categories/*.md MOC/Concepts/*.md MOC/Themes/*.md; do
      printf "%4d  %s\n" "$(grep -c '^- \[\[' "$f")" "$f"; done | sort -rn | head -6
    91  MOC/Categories/Machine Learning.md
    86  MOC/Categories/Outils & libs.md
    67  MOC/Concepts/Machine learning (notions).md
    59  MOC/Categories/LLM & IA générative.md
    57  MOC/Concepts/LLM (notions).md
    52  MOC/Concepts/Deep learning.md
  ```
  A l'inverse, 8 MOC listent 4 entrees ou moins, dont `MOC/Categories/Auth.md` avec 1.
- **Portee** : 6 MOC au-dessus de 50 entrees, 8 en dessous de 5. La distribution est le symptome
  d'une taxonomie a granularite inegale (`ml/framework` : 64 pages ; `auth` : 1), pas d'un defaut
  du generateur.
- **Cause** : `build_mocs.py` groupe sur la **tete** de categorie (`database`, `ml`, `tooling`) et
  ignore le second segment (`ml/framework`, `ml/serving`, `ml/tracking`). L'information existe
  donc dans le vault mais n'est pas exploitee pour segmenter le hub.
- **Recommandation** : dans `MOC/Categories/`, sous-titrer par categorie complete
  (`### ml/framework`, `### ml/serving`) au lieu d'une liste a plat, quand la MOC depasse un
  seuil — 20 entrees convient. Correctif local au generateur, sans creation de page. Ne pas
  redecouper les categories elles-memes : c'est l'axe 1.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_mocs.py` (~10 lignes dans la
  boucle `cat_groups`). Les 15 MOC existantes sont regenerees dans leur zone AUTO ; leur section
  `## Notes` est preservee par `upsert()`.

### C8. La liste « 189 tags sans page concept » est a 55 % un artefact de mesure — gravite : mineur

- **Constat** : `build_links.py` declare un tag « sans page concept dediee » si aucun concept ne
  porte un `nom:` ou un `alias:` dont le slug est **exactement** egal au tag. La comparaison est
  litterale : `agents` ne matche pas « Agent patterns », `transformers` ne matche pas
  « Transformer architectures », `supervised` ne matche pas « Apprentissage supervise »,
  `forecasting` ne matche pas « Forecasting framing ». Sur les 189 tags signales, 105 sont
  pourtant portes par au moins une page concept Wiki : un point d'entree thematique existe deja.
- **Preuve** :
  ```
  189 tags sans page concept homonyme :
    - 105 sont portes par au moins une page concept Wiki (point d'entree existant)
    -  84 ne sont portes par AUCUNE page concept
  ```
  Sur ces 84, le haut de liste est majoritairement de l'outillage Dev, pas des notions :
  `distributed` 23, `orchestration` 15, `code-assistant` 14, `low-code` 12, `document-parsing` 10,
  `type-hints` 9, `testing` 8, `dataframe` 8, `db-client` 7, `dataviz` 7, `cli` 5, `linter` 3,
  `formatter` 2. Y figurent aussi `pattern` 5, `rule` 5 et `rex` 1, qui sont des marqueurs de type
  imposes par les gabarits (`Documentation/general/tags.md`, lignes 328-331) : ils n'auront jamais
  de page concept, par construction.
  Repartition par frequence des 189 : 30 tags a 10+ pages, 60 a 5-9, 63 a 2-4, 36 a 1 page.
  Sur les 75 tags a usage unique du vault, 36 sont dans cette liste.
- **Portee** : la section « Tags sans page concept dediee » de `AI/index/liens.md` — 189 lignes
  presentees comme des « sujets candidats a creer ». Environ 105 d'entre elles sont fausses.
- **Cause** : `slug()` (ligne 61 de `build_links.py`) fait un rapprochement exact apres
  normalisation ASCII. Il ne connait ni le pluriel, ni la traduction FR/EN, ni l'inclusion. La
  mesure est donc une heuristique de nommage presentee comme un inventaire de manques.
- **Recommandation** : ne rien creer en masse. Deux corrections, dans l'ordre. D'abord, dans
  `build_links.py`, considerer un tag comme couvert s'il est **porte par une page concept**, en
  plus du rapprochement par nom : la liste tombe de 189 a 84 et redevient lisible. Ensuite, filtrer
  les marqueurs de type (`pattern`, `rule`, `rex`, `bugs`) qui ne sont pas des sujets. Le reste du
  sujet — faut-il des tags a usage unique, faut-il un concept par tag — releve du **rangement,
  donc de l'axe 1** ; du point de vue de la navigation, le tag est deja un chemin d'acces en soi
  dans Obsidian (clic sur le tag en frontmatter → recherche), et ce chemin fonctionne pour les 321
  tags sans exception.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/build_links.py` (~5 lignes autour du
  calcul de `covered` et de `missing`). Aucune page creee.

### C9. La metrique « pages sans lien entrant » a deux faux positifs et masque les vrais isoles — gravite : mineur

- **Constat** : `audit_mesures.py` resout un lien entrant en comparant la derniere composante du
  wikilink au champ `nom:` de la page cible, jamais a son **nom de fichier**
  (`orphans = ... inbound[(fm.get("nom") or Path(f).stem).lower()] == 0`, ligne 178). Deux pages
  ont un `nom:` qui differe de leur nom de fichier, parce qu'il contient un `/`, caractere
  interdit dans un nom de fichier. Elles sont comptees orphelines alors qu'elles sont largement
  citees. Symetriquement, la metrique ne dit rien de l'atteignabilite : les 5 Rules, qui se citent
  entre elles, passent le test tout en etant inaccessibles (C3).
- **Preuve** :
  ```
  $ python3 -c "... nom != stem ..."
  2 pages ou nom: != nom de fichier
     Wiki/Concepts/A-B testing.md          nom: A/B testing
     Wiki/Concepts/ROC-AUC & courbe PR.md  nom: ROC-AUC / courbe PR
  $ grep -rn --include='*.md' -oiE '\[\[[^]|]*a-b testing[^]|]*' Dev/ Wiki/ | head -3
  Wiki/Concepts/Déploiement de modèles.md:40:[[A-B testing
  Wiki/Concepts/A priori conjugués.md:39:[[A-B testing
  Wiki/Concepts/Systèmes de recommandation.md:48:[[A-B testing
  ```
  Comptages corriges, avec une resolution par chemin complet puis par nom de fichier :
  | Definition | Compte |
  |---|---|
  | Socle `mesures-axe5.md` §6 (resolution par `nom:` seul, sources Dev+Wiki) | 12 |
  | 0 lien entrant depuis une page Dev/Wiki, resolution corrigee | **10** |
  | 0 lien entrant, MOC et `Home.md` comptes comme sources | **5** |
  | Inatteignables depuis `Home.md` + les 31 MOC (mesure de navigation) | **14** (dont 3 `.base`) |
- **Portee** : la ligne « 12 pages orphelines » du socle, reprise dans le brief sous la forme
  « 19 ». La metrique est utilisable mais doit etre lue avec sa marge d'erreur.
- **Cause** : la resolution par `nom:` a ete choisie pour coller a l'affichage ; or Obsidian
  resout un wikilink par **chemin de fichier**, jamais par frontmatter. Les deux modeles divergent
  des qu'un `nom:` n'est pas transposable en nom de fichier.
- **Recommandation** : dans `audit_mesures.py` §6, indexer les liens entrants sur `nom`, `alias`
  **et** nom de fichier. Ajouter a cote une mesure d'atteignabilite depuis `Home.md` + les MOC,
  qui est la question reellement posee par la navigation. Ne pas renommer les deux pages : leur
  `nom:` est correct pour l'humain, c'est la mesure qui doit s'adapter.
- **Effort** : **S** (< 1 h). Fichiers impactes : `AI/scripts/audit_mesures.py` (~15 lignes, §6).
  Fichier de mesures, hors perimetre des pages du vault.

### C10. Deux collisions de nom de page rendent douze wikilinks nus ambigus — gravite : mineur

- **Constat** : deux paires de fichiers partagent le meme nom de base a la casse pres. Un
  wikilink non qualifie vers l'une de ces cibles est resolu par Obsidian selon sa propre heuristique
  de proximite, sans que l'auteur controle la destination.
- **Preuve** :
  ```
  $ python3 -c "... collisions de stems ..."
  bases de données -> ['Wiki/Concepts/Bases de données.md', 'MOC/Categories/Bases de données.md']
  hdbscan          -> ['Dev/Services/hdbscan.md', 'Wiki/Concepts/HDBSCAN.md']

  liens ambigus (cible a stem multiple, lien non qualifie) : 12
    Wiki/Concepts/Clustering.md                     -> HDBSCAN   (x2)
    Wiki/Concepts/t-SNE and UMAP.md                 -> HDBSCAN   (x2)
    Wiki/Concepts/Clustering evaluation.md          -> HDBSCAN   (x2)
    Wiki/Concepts/DBSCAN.md                         -> HDBSCAN   (x2)
    Wiki/Concepts/Classification hiérarchique (CAH).md -> HDBSCAN
    Wiki/Concepts/Apprentissage non supervisé.md    -> HDBSCAN
    Wiki/Concepts/Web scraping.md                   -> Bases de données (x2)
  ```
  La collision `Bases de données` est la plus genante : elle oppose une page concept Wiki a une MOC
  generee. `Wiki/Concepts/Web scraping.md` ligne 49 ecrit
  `- [[Bases de données]] — où atterrissent les données collectées`, ce qui vise manifestement la
  page concept, mais peut resoudre vers le hub. Les 26 autres liens vers cette page sont, eux,
  qualifies (`[[Wiki/Concepts/Bases de données|…]]`).
- **Portee** : 12 wikilinks sur 5 971 aretes. Aucun lien mort : `check_brain.py` passe.
- **Cause** : la convention de wikilink qualifie par chemin, posee dans `CLAUDE.md` precisement
  pour eviter les collisions, n'est pas verifiee. `check_brain.py` valide qu'un lien **resout**,
  pas qu'il resout de facon **unique**. La collision `Bases de données` est de plus structurelle :
  `build_mocs.py` derive le nom du hub de `CAT_LABEL`, sans verifier qu'aucune page ne porte deja
  ce nom.
- **Recommandation** : ajouter a `check_brain.py` une regle « un wikilink non qualifie dont le nom
  de base correspond a plusieurs fichiers est une violation ». Elle attrape les 12 cas d'un coup et
  empeche la regression. En complement, faire echouer `build_mocs.py` si un libelle de `CAT_LABEL`
  ou de `CONCEPT_LABEL` entre en collision avec une page existante — le commentaire du code montre
  que le probleme etait connu pour `CONCEPT_LABEL` (« évite la collision avec la page chapeau
  "Traitement du signal" ») et resolu a la main, page par page.
- **Effort** : **S** (< 1 h) pour la regle de validation ; la correction des 12 liens est
  triviale mais touche 7 pages `Wiki/Concepts/` et releve de la conversation de correction.
  Fichiers impactes : `AI/scripts/check_brain.py`, `AI/scripts/build_mocs.py`, 7 pages
  `Wiki/Concepts/`.

### C11. Trois comparatifs `.base` ne sont cites par aucune fiche — gravite : mineur

- **Constat** : 47 vues `Comparatif - *.base` existent dans `Dev/Patterns/`. 44 sont citees depuis
  au moins une fiche Service ou Outil. 3 ne le sont jamais, et ne sont referencees par aucune MOC :
  elles ne sont accessibles que par l'explorateur de fichiers.
- **Preuve** :
  ```
  $ python3 -c "... comparatifs jamais cites ..."
  47 comparatifs, 3 jamais cites:
    ["Comparatif - Suivi d'expériences ML", 'Comparatif - Forecasting',
     'Comparatif - Détection & segmentation']
  ```
  Ces 3 fichiers figurent aussi dans la liste des 14 nœuds inatteignables de C1.
- **Portee** : 3 vues sur 47. Elles couvrent respectivement `ml/tracking` (7 pages),
  la categorie forecasting (tag `forecasting`, 14 pages) et la detection/segmentation
  (tags `object-detection` 5 + `segmentation` 4).
- **Cause** : le lien fiche → comparatif est pose a la main par le skill `enrichir-brain` au moment
  ou une fiche est ecrite. Un comparatif cree apres coup, ou cree pour un lot de fiches sans
  retour sur elles, n'obtient jamais son lien entrant. Rien ne le detecte : le socle §6 ne compte
  que les pages `.md`, les `.base` sortent du perimetre de la mesure d'orphelins.
- **Recommandation** : deux correctifs independants. Cote generation, faire lister par
  `MOC/Categories/<X>.md` les comparatifs dont le filtre porte sur cette categorie — le fichier
  `.base` contient son propre filtre (`file.path.startsWith("Dev/Services/")` +
  `file.hasTag(...)`), donc l'appariement est mecanisable. Cote mesure, etendre le §6 de
  `audit_mesures.py` aux `.base` pour que ce trou soit visible a l'avenir.
- **Effort** : **M** (une session) pour l'appariement dans `build_mocs.py` — il faut parser le
  YAML des `.base` ; **S** (< 30 min) pour la seule extension de la mesure. Fichiers impactes :
  `AI/scripts/build_mocs.py`, `AI/scripts/audit_mesures.py`.

## Ce qui va bien

- **L'integrite des liens est bonne.** `check_brain.py` passe sans violation sur 647 pages, et
  `AI/index/liens.md` ne signale **aucun lien non resolu** (`- aucun` dans la section « Liens non
  resolus »). Aucun des 5 971 liens du vault ne mene nulle part. Rien a corriger de ce cote.
- **La couverture MOC est haute la ou le generateur fonctionne** : 635 pages sur 647 sont listees
  par au moins une MOC. Les 12 exceptions sont toutes expliquees par une cause unique (C1). Ce
  n'est pas une derive diffuse, c'est un trou net.
- **L'etagement Wiki fait ce qu'il promet.** `Documentation/perso/obsidian-graph.md` decrit
  theme → sous-domaine → feuille ; les 5 MOC/Themes listent 3 a 8 sous-hubs chacune, et les 11
  MOC/Concepts listent les feuilles. Aucune MOC/Themes ne deverse 100 liens. Le dispositif tient.
- **Le maillage par `alternatives:` est dense et sain.** Degre moyen 16,4 sur 726 nœuds ; 669
  pages sur 726 ont entre 5 et 49 voisins. Aucun desert : seules 38 pages ont moins de 5 liens.
  La reponse au risque de « pelote illisible » — graphe local ancre a droite plutot que graphe
  global — est documentee et correcte pour cette densite. Le graphe global de 726 nœuds est
  effectivement illisible, mais ce n'est pas le mode de navigation prevu.
- **L'index sait deja resserrer un choix.** Sur `llm/framework` (33 candidats), le couple
  `categorie` + `tag` ramene a 10 candidats avec `rag`, puis le `pitch` — present sur les 337
  fiches Dev sans exception — permet de descendre a 2-3. Le probleme de C5 n'est pas le
  resserrement, c'est l'elimination sur contrainte dure.
- **Les vues `Comparatif - *.base` sont un bon chemin d'acces**, et le seul endroit ou l'humain
  voit `langage`, `licence_type`, `maturite` et `scaling` cote a cote. 44 sur 47 sont cablees.
- **`Home.md` existe** et pointe vers les deux index generes. Sa structure est la bonne ; c'est sa
  maintenance manuelle qui pose probleme (C2), pas sa conception.

## Questions laissees ouvertes

1. **Patterns et Rules : hub par `type:` ou entree dans la taxonomie ?** C1 recommande un hub par
   `type:`, qui est le correctif le moins invasif et ne prejuge de rien. L'axe 1 peut au contraire
   conclure qu'un `pattern/*` et un `rule/*` doivent entrer dans `taxonomie.md`, auquel cas le
   groupement par categorie existant les couvre sans code supplementaire. Arbitrage du
   proprietaire, a rendre avant la correction.
2. **`domaines:` : etendre, lire, ou retirer ?** Trois issues, trois couts. Le lire cote Dev
   coute une heure (C6) mais fige un champ que 297 fiches service n'ont pas le droit de porter.
   L'etendre aux services est un chantier de saisie sur 297 pages. Le retirer supprime les 5
   MOC/Themes. La navigation plaide pour le lire ; le modele est l'affaire de l'axe 1. **Les deux
   axes doivent converger avant toute ecriture** — c'est le seul point ou ce rapport depend d'un
   autre.
3. **Faut-il un `Home.md` genere ?** Le faire generer resout C2 durablement mais retire au
   proprietaire une page qu'il ecrit lui-meme. Une zone `<!-- AUTO:START -->` dans un `Home.md`
   par ailleurs manuel est un compromis possible ; il faut decider si l'accueil est un artefact ou
   une page perso.
4. **Un `nom:` doit-il pouvoir differer du nom de fichier ?** Deux pages le font (C9), pour une
   raison legitime (le `/`). Interdire la divergence simplifie toutes les mesures ; l'autoriser
   oblige chaque script a resoudre sur trois cles. A trancher une fois pour toutes.
5. **Le REX** : C4 propose un correctif a 15 minutes, mais il ne vaut que si l'axe 6 conserve le
   pilier. A ne pas appliquer avant sa conclusion.
6. **Quel seuil pour un hub trop gros ?** C7 propose 20 entrees, par analogie avec les MOC/Concepts
   qui restent lisibles a ce niveau. Le seuil est un choix de confort de lecture, pas un fait.

## Annexe A — Type de page → chemin d'acces → verdict

Chemin d'acces d'un humain qui **ne connait pas le nom** de la page qu'il cherche.

| Type | Pages | Via une MOC | Via un lien entrant | Via le tag en frontmatter | Via l'index agent | Verdict |
|---|---|---|---|---|---|---|
| `service` | 297 | oui — `MOC/Categories/<famille>` (336 pages Dev couvertes) | oui, dense (`alternatives:`, degre moyen 16,4) | oui | partiel — 9 champs eliminatoires absents (C5) | **sert** cote humain, **incomplet** cote agent |
| `outil` (Dev) | 39 | oui — `MOC/Categories/` | oui | oui | partiel, idem service | **sert** |
| `outil` (Wiki) | 1 | **non** — `skill/knowledge` hors du filtre `concept/*` | non — 0 lien entrant | oui (`note-taking`) | oui, entree complete | **invisible sauf par tag** |
| `concept` | 299 | oui — `MOC/Concepts/` **et** `MOC/Themes/` | oui, dense | oui | partiel — pas de `pitch:` dans l'index | **sert bien** |
| `pattern` | 5 | **non** — pas de `categorie:` | 2 sur 5 seulement ; 1 des 2 depend de l'ilot Rules | oui (tag `pattern`) | entree a 6 champs `null` sur 10 | **invisible sauf par tag** |
| `rule` | 5 | **non** — pas de `categorie:` | ilot ferme : 12 liens internes, 0 externe | oui (tag `rule`) | entree a 6 champs `null` sur 10 | **invisible sauf par tag** |
| `rex` | 1 | **non** — pas de `categorie:` | **0** — 46 references, toutes en chemin backtick | oui (tags `rex`, `bugs`) | entree a 6 champs `null` sur 10 | **invisible sauf par tag** |
| vue `.base` | 47 | non | 44 sur 47 depuis une fiche | sans objet | absente de l'index | **sert**, 3 exceptions |
| MOC generee | 31 | sans objet | 14 sur 31 seulement | sans objet | absente de l'index | **racine manquante** (C2) |

Le chemin par tag existe pour les 6 types, sans exception : `Documentation/general/tags.md`
documente `pattern`, `rule`, `rex` et `bugs` comme marqueurs de type imposes par les gabarits, et
un clic sur le tag en frontmatter ouvre la recherche Obsidian correspondante. C'est le seul chemin
d'acces des Patterns, Rules et REX aujourd'hui — il fonctionne, mais suppose de savoir que le tag
existe.

## Annexe B — Les orphelins : cause retenue et correctif

Le socle en compte 12. Deux sont des artefacts de mesure ; il en reste 10 reels au sens
« aucune page Dev ou Wiki ne me cite », dont 5 seulement restent orphelines quand les MOC comptent
comme sources.

| Page | Cause retenue | Correctif propose | Effort |
|---|---|---|---|
| `Wiki/Concepts/A-B testing.md` | **Faux positif.** `nom: A/B testing` ≠ nom de fichier ; la mesure resout par `nom:` seul. La page recoit au moins 5 liens entrants. | Corriger `audit_mesures.py` §6 (C9). Ne pas toucher la page. | S |
| `Wiki/Concepts/ROC-AUC & courbe PR.md` | **Faux positif.** Idem, `nom: ROC-AUC / courbe PR`. Citee depuis `Dev/Services/Scikit-Learn.md`. | Idem. | S |
| `Dev/Rules/*` (les 5) | Ilot ferme : 0 lien entrant externe, pas de `categorie:` donc aucune MOC. Non detecte par la mesure, qui les voit se citer entre elles. | `MOC/Types/Rules.md` genere par `type:` (C1). Ne pas cabler Service → Rule. | S |
| `Dev/Patterns/Pattern - Moteur de jeu pur + IA séparée.md` | Pas de `categorie:` (aucune MOC) **et** aucune fiche Service ne le cite : le pattern couvre un archetype (n°3, ML/IA algorithmique) sans brique dediee dans le vault. Defaut de contenu **et** de generation. | `MOC/Types/Patterns.md` (C1). En complement, cabler depuis les fiches de son domaine si l'axe 1 en cree. | S |
| `Dev/Patterns/Pattern - Pipeline scraping → matching → optimisation.md` | Idem. Ses briques existent pourtant (`data/scraping` 10 pages, `tooling/optim`, `PuLP`) mais aucune ne le cite : le lien retour fiche → pattern n'est pas dans le gabarit Service. Defaut de generation. | `MOC/Types/Patterns.md` (C1). | S |
| `Dev/Patterns/Pattern - RAG structuré graphe + human-in-the-loop.md` | Idem, avec des briques nombreuses (`database/graph`, `llm/framework`). Defaut de generation. | `MOC/Types/Patterns.md` (C1). | S |
| `Dev/REX/REX - Postgres.md` | Reference depuis `Dev/Services/Postgres.md` mais en chemin backtick, jamais en wikilink — convention adoptee pour ne pas produire 45 liens morts (C4). Defaut de convention, pas de contenu. | Passer les 2 references de `Postgres.md` en wikilink ; inscrire la regle dans `enrichir-brain`. Sous reserve de l'axe 6. | S |
| `Wiki/Outils/Obsidian.md` | `galaxie: wiki` mais `categorie: skill/knowledge`, hors du filtre `concept/*` de `build_mocs.py`. Seule page de `Wiki/Outils/`. Defaut de generation. | Elargir le filtre wiki de `build_mocs.py` a toute page `galaxie: wiki` (C1). | S |
| `Dev/Services/PyJWT.md` | Seul membre de la categorie `auth`, `alternatives: []`. Couvert par `MOC/Categories/Auth.md` (1 entree) donc atteignable. Defaut de contenu : rien a comparer. | Aucun correctif de navigation. La question « faut-il une categorie a 1 page » est de l'axe 1. | — |
| `Dev/Services/jupysql.md` | `tooling/notebook` (5 pages), `alternatives: []`. Couvert par `MOC/Categories/Outils & libs`. Defaut de contenu : alternatives non renseignees. | Renseigner `alternatives:` lors du prochain passage sur la fiche. Hors perimetre auditeur. | S |
| `Dev/Services/minim.md` | `data/scraping` (10 pages), `alternatives: []` alors que 9 pages voisines existent. Defaut de contenu. | Idem. | S |
| `Dev/Outils/croc.md` | `network/transfer`, seul membre, `alternatives: []`. Couvert par `MOC/Categories/Réseau` (2 entrees). Defaut de contenu. | Aucun correctif de navigation. | — |
| `Dev/Outils/Page to Markdown.md` | `tooling/capture`, seul membre, `alternatives: []`. Couvert par `MOC/Categories/Outils & libs`. Defaut de contenu. | Aucun correctif de navigation. | — |

**Verdict sur la question « defaut de contenu ou de generation ? »** : sur les 12,
**2 sont des artefacts de mesure**, **9 sont un defaut de generation** (les 5 Rules, 3 Patterns et
`Obsidian.md` — le generateur ne les regarde pas), et **4 sont un defaut de contenu** (`PyJWT`,
`jupysql`, `minim`, `croc`, `Page to Markdown` : `alternatives:` vide ou categorie a un seul
membre — mais tous restent atteignables par une MOC). Le REX est un cas a part : defaut de
convention d'ecriture des liens.

**Verdict sur « build_mocs doit-il couvrir Patterns et Rules ? »** : oui, et sous la forme d'**une
MOC par dossier**, generee a partir de `type:`, pas d'une integration dans les MOC de categorie
existantes. Deux raisons. Les Patterns et Rules sont transverses par nature — un pattern « RAG
structure graphe » traverse `database/graph`, `llm/framework` et `data/parsing` : le ranger dans
une categorie de tete serait arbitraire. Et le groupement par `type:` ne suppose aucune decision
de taxonomie, donc ne bloque pas l'axe 1 et ne sera pas a defaire selon ce qu'il conclut.
