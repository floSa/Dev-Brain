# Rapport d'audit — Axe 3 : Skills

Auditeur : conversation `audit-axe-3-skills`, le 2026-09-02. Socle : `mesures-axe3.md`,
relancé le 2026-09-02 — **identique au caractère près** à `mesures-2026-09-02.md`
(`diff` sur les deux fichiers, hors ligne d'en-tête : aucune différence). Aucun écart à signaler.

## Synthèse

Rien ne garantit qu'un skill soit suivi, et rien ne peut le garantir en l'état : la seule
mécanique automatique annoncée par le vault — le hook `Stop` — n'a jamais tourné une seule
fois, et ne peut pas tourner (aucun `settings.json`, chemin de vault faux en dur). Sur les
11 étapes d'`enrichir-brain`, 2 sont vérifiées par script, 2 le sont partiellement, 7 ne
laissent aucune trace ; les omissions constatées (file `AI/backlog.md`, pitchs, concept
parent) tombent toutes dans les 7. Trois documents se contredisent frontalement sur le
commit automatique. **S'il ne faut faire qu'une chose : versionner `.claude/settings.json`
avec un hook `Stop` qui lance `check_brain.py` quand la session a touché `Dev/` ou `Wiki/`.**
C'est le seul point où l'omission cesse d'être silencieuse, pour moins d'une heure de travail.

## Constats

### C1. Le hook `Stop` n'a jamais tourné et ne peut pas tourner — gravité : bloquant

- **Constat** : `CLAUDE.md` (§Protocole de session) et `CLAUDE-build.md:271` annoncent un
  résumé de session écrit automatiquement par `AI/scripts/session_to_devbrain.py`. Ce hook
  n'est déclaré nulle part, et son chemin de vault est faux sur cette machine. Les deux
  seuls fichiers de `AI/sessions/` ont été écrits à la main.
- **Preuve** :
  ```
  $ ls .claude/
  README.md  settings.example.json  settings.local.example.json  settings.local.json  skills/
      → aucun settings.json : le fichier que .claude/README.md:11 déclare « ✅ versionné » n'existe pas.

  $ cat ~/.claude/settings.json
  { "theme": "dark", "effortLevel": "high" }          → aucune clé "hooks"
  $ grep -c '"hooks"' ~/.claude.json
  0
  $ ls /etc/claude-code/  →  No such file or directory

  $ sed -n '42p' AI/scripts/session_to_devbrain.py
  VAULT = Path.home() / "DevBrain"
  $ ls ~/DevBrain  →  No such file or directory
      (le vault est en /home/florianhorellou/Projets/DevBrain)
  ```
  Les deux fichiers de `AI/sessions/` ne portent pas la signature du hook. Celui-ci écrit
  un frontmatter `session_id / project / type: ai-session / tags: [ai-session, mode-<x>]`
  (lignes 105-114) et borne le résumé à 300 mots (ligne 137). Les fichiers présents portent
  `galaxie: meta / type: session`, aucun `session_id`, et pèsent 656 et 357 mots.
- **Portée** : la totalité de l'automatisation du vault. Un seul script concerné,
  `session_to_devbrain.py` (176 lignes), plus l'absence de `.claude/settings.json`.
- **Cause** : le setup décrit dans `.claude/README.md` n'a été fait qu'à moitié —
  `settings.local.json` a bien été copié depuis son exemple (les deux fichiers sont
  identiques au caractère près), `settings.json` ne l'a jamais été. Et le chemin en dur
  `~/DevBrain` date d'une machine antérieure : il contredit la règle explicite de
  `Documentation/perso/machines.md:12` (« aucun chemin absolu ne doit fuiter dans les
  scripts ou la config »). La même adresse périmée se retrouve dans `CLAUDE-project.md:39`.
- **Recommandation** : créer `.claude/settings.json` versionné (le `.gitignore:24` n'ignore
  que `settings.local.json`, rien n'empêche de committer l'autre) et y déclarer les hooks.
  Dans `session_to_devbrain.py`, remplacer `Path.home() / "DevBrain"` par une résolution
  relative — la racine git du `cwd` reçu dans le payload, avec repli sur une variable
  d'environnement. Corriger `~/DevBrain` dans `CLAUDE-project.md:39`.
- **Effort** : S (< 1 h). Fichiers : `.claude/settings.json` (création),
  `AI/scripts/session_to_devbrain.py`, `CLAUDE-project.md`, `.claude/README.md`.

### C2. Sept des onze étapes d'`enrichir-brain` ne laissent aucune trace — gravité : bloquant

- **Constat** : le skill décrit 11 étapes. Deux sont tenues par un contrôle dur
  (`check_brain.py`), deux le sont partiellement, sept sont invisibles : rien, ni pendant
  ni après, ne distingue une étape faite d'une étape sautée. Le tableau complet est en
  annexe A. Les trois omissions déjà constatées dans la vie du vault tombent toutes dans
  ces sept.
- **Preuve** — les trois omissions, mesurées sur le vault :
  ```
  $ uv run AI/scripts/check_brain.py
  check_brain : 647 pages actives contrôlées
  OK — aucune violation dure.
  ```
  Le validateur est vert, et pourtant :
  - **Étape 7, pitchs** : `mesures-axe3.md` §4 relève **14 lignes désynchronisées** sur 801
    vérifiables. Aucun script ne les voit. Elles étaient déjà listées comme « À reprendre »
    dans `AI/sessions/2026-09-01-1643-build.md` — une session plus tard, elles sont toujours là.
  - **Étapes 3 et 6, concept parent et comparatif** :
    ```
    Dev/Services : 297 fiches ; sans aucun lien vers Wiki/Concepts : 102 (34 %)
    comparatifs .base : 47 ; catégories service à >=2 fiches : 38 ; couvertes : 26 ; non couvertes : 12
    ```
    (script de comptage jetable : parcours de `Dev/Services/*.md`, extraction des `[[...]]`,
    test d'appartenance à `Wiki/Concepts/` ; puis extraction du `categorie == "..."` de
    chaque `Comparatif - *.base`.) Le couple Dev↔Wiki que l'étape 6 impose n'existe pas sur
    un tiers des fiches. `check_brain` vérifie qu'un lien n'est pas mort, jamais qu'il existe.
  - **Étape 3 du mode balayage, file dans `AI/backlog.md`** : la dernière entrée du fichier
    est datée du 2026-07-17. Les deux lots suivants — 15 pages le 2026-09-01, 14 le
    2026-09-02 (commit `a66d346`) — n'y figurent pas. L'étape a été sautée deux fois de suite.
- **Portée** : les 11 étapes du skill, appliquées à toute écriture dans `Dev/` et
  `Wiki/Concepts/` — 647 pages.
- **Cause** : le skill est un texte de procédure, pas un exécutable. Un agent qui le lit
  sans le charger, ou qui le charge et en saute une étape, produit exactement la même trace
  qu'un agent qui l'a suivi. Les seuls points où l'écart devient visible sont ceux qui
  passent par `check_brain` — c'est-à-dire les deux étapes que quelqu'un a pris la peine de
  coder. Le reste repose sur la mémoire de l'agent.
- **Recommandation** : deux mouvements, dans cet ordre.
  1. **Rendre l'omission visible** (pas la rendre impossible) : un hook `PostToolUse` sur
     `Write|Edit` filtré sur `Dev/|Wiki/` qui écrit le chemin touché dans un journal de
     session, plus un hook `Stop` qui, si ce journal n'est pas vide, lance `check_brain.py`
     et signale un code de retour non nul. Un garde-fou qui *refuse* l'écriture hors skill
     n'est pas implémentable — un hook ne sait pas quel skill est chargé — et se
     contournerait de toute façon. Un garde-fou qui *constate* suffit : l'omission cesse
     d'être silencieuse, et la friction est nulle tant que tout est vert.
  2. **Faire descendre trois étapes invisibles dans `check_brain.py`** : la synchro des
     pitchs (la logique existe déjà, écrite pour `audit_mesures.py` §4 — il s'agit de la
     déplacer et de la passer en règle dure), la présence d'au moins un lien Dev→Wiki sur
     une fiche `type: service`, et la couverture `.base` d'une catégorie à ≥2 services.
     Les deux dernières doivent d'abord passer en règle souple : 102 et 12 violations
     existantes, un contrôle dur bloquerait immédiatement.
- **Effort** : S pour le mouvement 1 (deux hooks, ~40 lignes, une fois `.claude/settings.json`
  créé par C1). M pour le mouvement 2 (`AI/scripts/check_brain.py` : ~80 lignes ajoutées,
  trois règles, dont une réutilise du code existant). Le rattrapage des 102 + 12 + 14
  violations est un chantier distinct (L), qui relève des axes 2 et 5.

### C3. Trois documents se contredisent sur le commit automatique — gravité : sérieux

- **Constat** : la même action — committer et pousser après validation — est décrite trois
  fois, dans trois termes incompatibles.
- **Preuve** :
  ```
  $ sed -n '76p' .claude/skills/enrichir-brain/SKILL.md
  11. **Commit + push + intégration dans `main` (d'office, sans demander)** : […]
      Ne jamais répondre « à toi de committer / merger ».

  $ sed -n '275p' CLAUDE-build.md
  **Ne commit et ne push jamais automatiquement.** Propose le commit une fois une fiche/un
  lot vérifié, mais attends la validation explicite de l'utilisateur avant `git commit`/`git push`

  $ sed -n '70p' CLAUDE.md
  - Commit + push automatiques après validation (sans demander) ; jamais de --force/rebase sans accord
  ```
  Le skill dit « d'office, ne jamais demander ». `CLAUDE-build.md` dit « jamais
  automatiquement, attends la validation explicite ». `CLAUDE.md` range l'action dans la
  liste « ce que tu NE fais PAS sans confirmation explicite » tout en la qualifiant de
  « automatiques […] sans demander » — la phrase se contredit elle-même.
- **Portée** : trois fichiers, une action à effet externe (push sur `origin/main`).
- **Cause** : la règle a été durcie dans le skill sans que les consignes soient reprises.
  C'est le mode de défaillance générique de la duplication : 610 lignes de `CLAUDE*.md`
  face à 182 lignes de skills, sans aucune règle disant lequel gagne.
- **Recommandation** : trancher une fois, écrire la décision **au seul endroit qui la
  porte** — le skill, puisque c'est lui qui exécute — et remplacer les deux autres passages
  par un renvoi (« la clôture git est décrite dans `enrichir-brain`, étape 11 »). Poser
  dans `CLAUDE.md` la règle d'arbitrage manquante : en cas de divergence entre une consigne
  et un skill, le skill fait foi sur l'exécution, la consigne sur le périmètre.
- **Effort** : S (< 1 h). Fichiers : `CLAUDE.md:70`, `CLAUDE-build.md:273-285`,
  `.claude/skills/enrichir-brain/SKILL.md:76`.

### C4. Une consigne enseigne une valeur d'enum que le validateur refuse — gravité : sérieux

- **Constat** : `CLAUDE-build.md` documente le champ `scaling` avec la valeur
  `serverless-ok`. Ni le validateur ni le gabarit ne connaissent cette valeur. Un agent qui
  suit la consigne à la lettre écrit une fiche que `check_brain.py` rejette.
- **Preuve** :
  ```
  $ sed -n '57p' CLAUDE-build.md
  scaling: single-node | distributed | serverless-ok

  $ sed -n '56p' AI/scripts/check_brain.py
      "scaling": {"single-node", "distributed", "serverless"},

  $ sed -n '33p' Templates/Service-Dev.md
  <!-- self-host vs managé, prix indicatif, scaling (single-node | distributed | serverless) -->
  ```
  Le vault emploie `serverless` sur 11 fiches, `serverless-ok` sur aucune (comptage du
  frontmatter des 336 fiches `Dev/` : `{'single-node': 212, 'distributed': 74,
  'serverless': 11, None: 39}`). La consigne est seule contre le gabarit, le validateur
  et l'usage.
- **Portée** : une ligne, mais c'est le seul des cinq enums où consigne et validateur
  divergent — les quatre autres (`hosted`, `licence_type`, `maturite`, `status`) concordent.
- **Cause** : la valeur a été renommée dans `check_brain.py` sans reprise de la consigne.
  Même mécanisme que C3, en plus étroit.
- **Recommandation** : corriger `CLAUDE-build.md:57`. Plus généralement, ne pas recopier
  les enums dans une consigne : `CLAUDE-build.md:95` applique déjà ce principe pour la
  taxonomie (« c'est la source de vérité, ne la duplique pas ici de mémoire ») — l'étendre
  aux valeurs fermées, dont `check_brain.py:54-60` est la source.
- **Effort** : S (< 15 min). Fichier : `CLAUDE-build.md:53-60`.

### C5. `planifier-projet` ne peut pas filtrer sur les critères qu'il annonce — gravité : sérieux

- **Constat** : le skill fait trancher l'utilisateur tôt sur l'axe on-prem / air-gapped
  (étape 3) au motif que ces réponses « éliminent d'emblée des candidats », puis filtre
  l'index (étape 5). L'index ne porte aucun des champs qui permettraient cette élimination.
  Le skill n'a par ailleurs jamais tourné : `Projects/` est vide.
- **Preuve** :
  ```
  $ sed -n '34,35p' AI/scripts/build_index.py
  FIELDS = ["nom", "alias", "type", "galaxie", "categorie", "domaines",
            "pitch", "tags", "alternatives"]
  ```
  Dix champs avec `path`. Absents de l'index, alors qu'ils sont renseignés dans le
  frontmatter : `hosted` (297 fiches), `licence_type` (336), `maturite` (297),
  `status` (336), `scaling` (297). L'axe on-prem se lit directement dans `hosted` —
  distribution mesurée : `{'self': 205, 'managed': 10, 'both': 82}` : 10 candidats
  éliminables d'office, invisibles depuis l'index.

  Second point, la volumétrie. Le skill dit « filtrer les candidats sans lire 160 fichiers »
  (`SKILL.md:30`) mais, contrairement à `enrichir-brain`, ne mentionne jamais
  `query_index.py` — il désigne le fichier brut :
  ```
  $ ls -l AI/index/brain-index.json
  469990 octets  (~117 000 tokens)
  $ uv run AI/scripts/query_index.py --categorie ml/framework | wc -c
  37841        (64 candidats, ~9 500 tokens)
  $ uv run AI/scripts/query_index.py --categorie database/vector | wc -c
  6067         (11 candidats)
  ```
  Le nombre « 160 fichiers » est par ailleurs périmé : le brain compte 337 fiches Dev.
  Et sur `ml/framework`, la plus grosse catégorie, l'étape 5 doit ramener 64 candidats
  indifférenciés à 2-3 sans aucun champ pour les départager.
- **Portée** : les 82 lignes de `planifier-projet`, son étape 5 (le cœur du skill), et
  `build_index.py`.
- **Cause** : `build_index.py` a été conçu pour le catalogue de `enrichir-brain` (nom,
  pitch, alternatives) et `planifier-projet` a été écrit en supposant un index plus riche.
  Le point est **déjà identifié et parqué** par le propriétaire dans
  `AI/ameliorations-devbrain.md` §1 (« parqué le 2026-08-08 »), sous l'angle d'un nouveau
  champ `contraintes:` à créer. Cet audit constate que quatre champs *déjà remplis* sur
  297 à 336 fiches suffiraient à couvrir l'essentiel du besoin sans rien créer.
- **Recommandation** : ajouter `hosted`, `licence_type`, `maturite`, `status` à
  `FIELDS` dans `build_index.py` — aucun contenu à écrire, les valeurs existent. Ajouter à
  `query_index.py` les options de filtre correspondantes. Réécrire l'étape 5 de
  `planifier-projet` pour qu'elle passe par `query_index.py`, comme le fait `enrichir-brain`,
  et corriger « 160 fichiers ». La question du champ `contraintes:` reste ouverte et
  distincte : elle vise les incompatibilités qu'aucun champ existant ne capte.
- **Effort** : M (une session). Fichiers : `AI/scripts/build_index.py:34-35`,
  `AI/scripts/query_index.py`, `.claude/skills/planifier-projet/SKILL.md:30,45`.
  Régénération de l'index nécessaire ensuite.

### C6. Les skills et les consignes s'appuient sur des chemins qui n'existent plus — gravité : sérieux

- **Constat** : `enrichir-brain` consacre cinq passages à un « réservoir v1 » et à un
  dossier `Archive-v1/` qui n'existent pas dans le dépôt. `CLAUDE-build.md` renvoie à un
  skill absent. `CLAUDE-project.md` construit toute sa section d'accès sur un serveur MCP
  qui n'est déclaré nulle part.
- **Preuve** :
  ```
  $ for f in Services Patterns Rules Bugs Archive-v1 Archive-v1/_inventaire.md; do
        [ -e "$f" ] && echo "OK $f" || echo "ABSENT $f"; done
  ABSENT Services      ABSENT Patterns      ABSENT Rules
  ABSENT Bugs          ABSENT Archive-v1    ABSENT Archive-v1/_inventaire.md
  ```
  Occurrences : `SKILL.md:26` (« ne jamais toucher au réservoir v1 : `Services/`,
  `Patterns/`, `Rules/`, `Bugs/` à la racine »), `:43` (exemple de collision
  `Services/VectorDB/Qdrant.md`), `:53` (« si elle n'existe qu'en réservoir v1 → créer la
  version v2 »), `:82` (« ouvrir l'ancienne page dans `Archive-v1/` »), `:93` (anti-pattern).
  ```
  $ sed -n '262p' CLAUDE-build.md
  Si l'utilisateur fournit une URL : utilise le skill `defuddle` (kepano) […]
  $ ls ~/.claude/skills/ .claude/skills/
  aosis-deck-builder documentation enrichir-brain generer-documentation generer-tutoriel
  jupytext-notebooks local-whisper planifier-projet watch watch-md   |   enrichir-brain planifier-projet
      → pas de defuddle
  ```
  ```
  $ python3 -c "import json; d=json.load(open('~/.claude.json')); print(d.get('mcpServers'))"
  {}
  $ ls .mcp.json  →  No such file or directory
      → le serveur `devbrain` de CLAUDE-project.md:20-28 (5 outils mcp__devbrain__*) n'existe pas
  ```
- **Portée** : 5 passages sur 100 lignes de `enrichir-brain` (5 %), 1 dans
  `CLAUDE-build.md`, une section entière de `CLAUDE-project.md`.
- **Cause** : la migration v1→v2 a supprimé le réservoir sans repasser dans les skills.
  Le résidu est coûteux au-delà du bruit : les instructions de lien qualifié
  (`SKILL.md:43`, reprises dans `CLAUDE.md` §Conventions de nommage) n'ont plus de raison
  d'être — elles existaient pour désambiguïser des collisions v1/v2 qui ne peuvent plus se
  produire. Le vault applique donc partout une convention dont la cause a disparu.
- **Recommandation** : supprimer les cinq passages « réservoir v1 » et « Archive-v1 » de
  `enrichir-brain`. Décider séparément si la convention de lien qualifié se maintient pour
  d'autres raisons (lisibilité, robustesse au renommage) ou tombe avec sa cause — le choix
  n'est pas neutre, il touche des milliers de wikilinks. Remplacer le renvoi à `defuddle`
  par le mécanisme réellement disponible. Marquer explicitement la section MCP de
  `CLAUDE-project.md` comme « à configurer dans le dépôt projet », puisque ce fichier est un
  gabarit destiné à être copié ailleurs.
- **Effort** : S (< 1 h) pour les suppressions. La question du lien qualifié va en
  *Questions laissées ouvertes*. Fichiers : `.claude/skills/enrichir-brain/SKILL.md`,
  `CLAUDE-build.md:262`, `CLAUDE-project.md:18-28`.

### C7. Le découpage actuel noie la seule partie mécanisable du skill — gravité : mineur

- **Constat** : les étapes 8 à 11 d'`enrichir-brain` (régénérer, valider, vérifier la
  divergence, committer) sont purement mécaniques, identiques dans les deux modes, et ne
  dépendent d'aucun choix éditorial. Elles constituent 4 des 11 étapes et concentrent
  l'intégralité de ce qu'un script peut tenir. Elles ne sont pas invocables séparément.
- **Preuve** : le mode balayage ne les redécrit pas, il y renvoie —
  `SKILL.md:86` : « **Clôturer** : `build_index.py`, `build_mocs.py`, `build_links.py`,
  `check_brain.py` (doit passer), puis **commit + push + intégration dans `main` d'office
  (cf. étapes 10-11)** ». Le renvoi est l'aveu que ce bloc est une unité autonome.
  Conséquence pratique observable : la session du 2026-09-02 a écrit ses 14 pages hors
  skill, et il n'existait aucun moyen de rattraper la seule clôture — l'index est pourtant
  à jour aujourd'hui (recalcul en mémoire de la logique de `build_index.py` et comparaison
  à `brain-index.json` : 647 pages des deux côtés, 0 page manquante, 0 entrée orpheline,
  0 champ divergent), ce qui n'a pu se faire qu'en réexécutant les scripts à la main.
- **Portée** : les deux modes du skill.
- **Cause** : le skill a été écrit comme une procédure linéaire, pas comme une composition.
- **Recommandation** : scinder en deux skills — sommaire cible en annexe B. Le coût de
  coordination est faible : un seul point de passage, en fin de capture, et le second skill
  est idempotent (relançable sans dommage). Le bénéfice est double : la clôture devient
  rattrapable après une écriture hors skill, et elle devient la cible naturelle du hook
  `Stop` de C2 — un `Stop` qui constate « des pages ont bougé, la clôture n'a pas tourné »
  a un objet nommé à désigner. Réserve honnête : deux skills font deux choses à oublier
  plutôt qu'une ; le découpage ne vaut que couplé au garde-fou de C2, sinon il aggrave le
  problème qu'il prétend résoudre.
- **Effort** : M (une session), et **à ne faire qu'après C1 et C2**. Fichiers :
  `.claude/skills/enrichir-brain/SKILL.md`, création de `.claude/skills/cloturer-brain/SKILL.md`,
  renvois dans `CLAUDE-build.md:28-38`.

### C8. L'exercice d'audit lui-même n'est outillé qu'à moitié — gravité : mineur

- **Constat** : `audit_mesures.py` couvre 10 sections, toutes portant sur le **contenu** du
  brain. Aucune ne porte sur la mécanique : hooks, skills, cohérence entre les consignes et
  les scripts. Les cinq mesures dont cet axe a eu besoin ont dû être écrites à la volée et
  seront perdues.
- **Preuve** : les cinq mesures absentes de `audit_mesures.py`, chacune écrite ici en
  script jetable de 10 à 25 lignes :
  1. fraîcheur de l'index (recalcul en mémoire vs `brain-index.json` — 0 écart) ;
  2. couverture concept parent (`Dev/Services` → `Wiki/Concepts` : 102/297 sans lien) ;
  3. couverture des comparatifs `.base` (12 catégories à ≥2 services non couvertes) ;
  4. distribution des champs non indexés (`hosted`, `licence_type`, `maturite`, `scaling`) ;
  5. concordance des enums entre `CLAUDE-build.md` et `check_brain.py:54-60` (1 divergence).
  Les mesures 1 et 5 sont des contrôles binaires : elles répondent oui/non, sans jugement.
- **Portée** : les six axes de ce chantier, et toute répétition ultérieure.
- **Cause** : `audit_mesures.py` a été écrit pour ouvrir ce chantier, à partir de ce qui
  était connu à ce moment. Les besoins de mesure émergent en auditant.
- **Recommandation** : ne **pas** créer de skill d'audit — le jugement d'un audit n'est pas
  automatisable, et un skill de 6 axes reproduirait exactement le défaut de C2. Ajouter en
  revanche les mesures 1, 3 et 5 à `audit_mesures.py` (les mesures 2 et 4 ont vocation à
  descendre dans `check_brain.py`, cf. C2). Le format de rapport de `AI/audit/README.md`
  suffit comme gabarit : il est explicite et a tenu sur cet axe sans ambiguïté.
- **Effort** : M (une session). Fichier : `AI/scripts/audit_mesures.py`, ~90 lignes ajoutées,
  trois sections.

## Ce qui va bien

- **`check_brain.py` tient ce qu'il annonce, et il est vert.** 647 pages contrôlées, zéro
  violation dure, sur six règles réellement implémentées (gabarit, enums, tags, catégorie,
  réciprocité, liens morts). Les deux étapes du skill qui y sont adossées — tags (étape 5)
  et réciprocité des alternatives (étape 7, premier volet) — n'ont, elles, jamais dérivé.
  C'est la démonstration inverse de C2 : ce qui est codé tient.
- **L'index est exactement à jour.** Recalcul en mémoire de la logique de `build_index.py`
  et comparaison champ par champ à `brain-index.json` : 647 pages des deux côtés, aucune
  page absente, aucune entrée orpheline, aucun champ divergent. L'étape 8 est honorée en
  pratique, y compris par les sessions qui n'ont pas chargé le skill.
- **`query_index.py` est le bon outil, et il fonctionne.** 86 lignes, testé sur trois
  requêtes : une catégorie ramène 6 à 38 ko là où l'index entier en pèse 470. La discipline
  qu'il porte est ce qui permettra au brain de doubler sans casser les skills. Ne pas y
  toucher — seulement l'étendre (C5) et le câbler dans `planifier-projet`.
- **Les lots récents sont bien connectés.** Les 15 pages du lot du 2026-09-01 portent 3 à 6
  liens vers `Wiki/Concepts/` chacune, sauf `public-apis` (0 lien, et par ailleurs seule
  page sans tag du vault). Les 102 fiches sans concept parent sont du stock ancien, pas une
  dérive en cours : la pratique s'est améliorée, c'est le rattrapage qui manque.
- **Les appuis de `planifier-projet` sont réels.** `archetypes.md` liste bien 7 archétypes,
  `questions-projet.md` porte bien les 6 rubriques annoncées et l'axe on-prem. Le squelette
  du skill est sain ; seul son étape de filtrage est infaisable (C5).
- **`AI/ameliorations-devbrain.md` fonctionne comme il doit.** La limite des dix champs de
  l'index y était déjà consignée, datée et parquée, avec ses impacts listés. Un point connu
  et assumé n'est pas une dette silencieuse.

## Questions laissées ouvertes

1. **Le commit d'office : lequel des trois textes dit la vérité voulue ?** C3 constate la
   contradiction, il ne la tranche pas. Pousser sur `main` sans demander est une action à
   effet externe ; le choix appartient au propriétaire, pas à l'auditeur.
2. **La convention de wikilink qualifié survit-elle à la disparition de sa cause ?** Elle a
   été instituée pour désambiguïser des collisions v1/v2 qui ne peuvent plus se produire
   (C6). Elle garde des mérites propres (robustesse au renommage, lecture du chemin dans le
   lien). La maintenir est défendable — mais alors il faut réécrire sa justification, qui
   est aujourd'hui fausse. Le choix engage des milliers de liens.
3. **Le champ `contraintes:` de `AI/ameliorations-devbrain.md` §1 reste-t-il parqué ?**
   C5 montre que quatre champs déjà remplis couvrent l'essentiel sans rien créer. Reste à
   dire si le besoin résiduel — les incompatibilités qu'aucun champ existant ne capte —
   justifie un champ de plus.
4. **`.claude/settings.json` doit-il porter des hooks partagés ?** C1 le recommande, mais
   des hooks versionnés s'exécutent chez quiconque clone le dépôt. Sur un vault personnel
   c'est sans objet ; si le dépôt est destiné à être partagé, l'arbitrage change.
5. **Que faire du mode projet et de son MCP ?** `CLAUDE-project.md` décrit un mécanisme
   d'accès inexistant sur cette machine. Faut-il le configurer, ou acter que le mode projet
   passe désormais par autre chose ? La question déborde cet axe.

---

## Annexe A — Vérifiabilité des 11 étapes d'`enrichir-brain`

Légende : **script** = un contrôle automatique existe et bloque · **lecture** = un humain ou
un agent peut le constater après coup en ouvrant les fichiers · **invisible** = rien ne
distingue l'étape faite de l'étape sautée.

| # | Étape | Verdict | Ce qui la tient, ou ce qui manque |
|---|-------|---------|-----------------------------------|
| 1 | Interroger l'état par tranches (`query_index.py`) | invisible | aucune trace ; rien ne distingue une requête bornée d'une lecture des 470 ko |
| 2 | Vérifier l'existence (nom + `alias`) | invisible | `check_brain` ne détecte pas les doublons : `by_name` (ligne 152) écrase silencieusement. Aucun doublon de `nom` aujourd'hui, mais 6 noms de fiches sont aussi l'`alias` d'une autre page (`shap`, `lime`, `deepspeed`, `doctr`, `jupytext`, `tensorrt-llm`) : `--name` y répond de façon ambiguë |
| 3 | Identifier les pages connexes manquantes | invisible | l'omission ne laisse aucune trace ; mesuré a posteriori : 102/297 services sans concept parent, 12/38 catégories sans `.base` |
| 4 | Vérifier les faits sur le web, puis créer depuis le gabarit | partiel | **gabarit : script** (`check_brain`, champs requis + champs autorisés) — mais seulement pour `service` et `concept`. Les types `outil` (40 pages), `pattern` (5), `rule` (5), `rex` (1) n'ont aucun gabarit contrôlé. **Vérification web : invisible** |
| 5 | Poser les tags depuis `tags.md` | **script** | règle dure, vocabulaire fermé de 321 tags, 0 violation |
| 6 | Câbler les wikilinks Dev↔Wiki et le `.base` | partiel | **script** pour l'absence de lien mort ; rien ne vérifie qu'un lien *existe*, ni la réciprocité du couple Dev↔Wiki, ni la couverture `.base` |
| 7a | Synchroniser les alternatives (réciprocité) | **script** | règle dure, 0 violation |
| 7b | Synchroniser les pitchs réinjectés | invisible | la logique existe dans `audit_mesures.py` §4 mais n'est pas une règle : **14 désynchronisations vivantes** sur 801 lignes, connues depuis le 2026-09-01 |
| 8 | Régénérer index / MOC / liens | lecture | recalculable et comparable a posteriori (fait ici : 0 écart), mais rien ne l'impose ni ne le signale |
| 9 | Corriger jusqu'au vert | lecture | `check_brain` rend un code de retour exploitable — encore faut-il que quelqu'un le lance |
| 10 | Vérifier la divergence `origin/main` | invisible | aucune trace de la vérification, seulement de son résultat en cas d'échec |
| 11 | Commit + push + merge `--ff-only` | lecture | constatable dans l'historique, mais l'instruction est contredite par `CLAUDE-build.md:275` (C3) |
| B3 | *(mode balayage)* Écrire la file dans `AI/backlog.md` | invisible | omise deux fois de suite (lots des 2026-09-01 et 2026-09-02 absents du fichier) |

**Bilan : 2 étapes tenues par script, 2 partiellement, 4 constatables par lecture,
4 invisibles** (plus l'étape de balayage). Les trois omissions réelles documentées dans la
vie du vault — file de balayage, pitchs, concept parent — sont toutes dans la colonne
invisible. Aucune omission n'a jamais été constatée sur une étape tenue par script.

## Annexe B — Sommaire du découpage proposé (C7)

Structure seulement, pas le contenu. À n'écrire qu'après C1 et C2.

**`enrichir-brain`** — capture. Étapes 1 à 7 actuelles, inchangées sur le fond.
- Quand l'utiliser · Pré-requis · Appuis · Conventions v2 non négociables
- Procédure — mode ciblé : interroger, vérifier l'existence, identifier les connexes,
  vérifier les faits et écrire, tagger, câbler, synchroniser
- Procédure — mode balayage : cadrer, présenter le plan, **attendre le GO**, écrire la file
  dans `AI/backlog.md`, drainer
- Sortie explicite : « la capture est faite, la clôture reste à lancer »
- Anti-patterns de capture · Voir aussi : `cloturer-brain`

**`cloturer-brain`** — clôture. Étapes 8 à 11 actuelles, idempotent, invocable seul.
- Quand l'utiliser : après une capture, **ou après toute écriture manuelle dans `Dev/` ou
  `Wiki/`** — c'est le point qui manque aujourd'hui
- Procédure : régénérer (`build_index`, `build_mocs`, `build_links`) → valider
  (`check_brain`) → corriger jusqu'au vert → vérifier la divergence `origin/main` →
  committer / pousser / intégrer
- **Seul endroit du vault où la politique git est écrite** (résout C3 par construction)
- Anti-patterns de clôture · Voir aussi : `enrichir-brain`

Point de couplage unique : la dernière ligne d'`enrichir-brain` nomme `cloturer-brain`.
Le hook `Stop` de C2 vérifie que la clôture a produit un `check_brain` vert dès lors que la
session a touché `Dev/` ou `Wiki/`.
