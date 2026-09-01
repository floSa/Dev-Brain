---
galaxie: meta
nom: Rapport audit axe 6 - REX
type: meta-doc
tags: [meta]
---

# Rapport d'audit — Axe 6 : le pilier REX

Auditeur : conversation « audit axe 6 », le 2026-09-02.
Socle : `AI/audit/mesures-axe6.md`, relancé le 2026-09-02 — **identique au bit près** à
`AI/audit/mesures-2026-09-02.md` (`diff` vide). Aucun écart à signaler.

## Synthèse

Le pilier REX n'a jamais produit une seule entrée réelle : son unique fiche est un exemple
étiqueté comme tel, orphelin, écrit le 2026-06-08 et jamais suivi (86 jours). Ce qu'il devait
contenir est déjà capturé ailleurs, à 100 % : les 297 fiches Service portent toutes une section
`## Pièges` remplie. Le pilier ne coûte pas rien : 34 pointeurs morts invisibles du validateur,
une exception permanente dans deux scripts qui ne protège aucun lien, deux gabarits, une
section entière de `CLAUDE-build.md`. **Recommandation : fusionner** — les retours vont en
`## Pièges`, le pilier disparaît. Effort M, une session.

## Constats

### C1. Le pilier ne contient aucun retour d'expérience réel — gravité : bloquant

- **Constat** : `Dev/REX/` contient un fichier, `REX - Postgres.md`. Sa seule entrée est
  intitulée `## 2026-04-12 — Connection pool exhaustion en prod (exemple)` et son champ
  `Référence` vaut littéralement `exemple — remplacer par le lien projet`. C'est une
  démonstration de gabarit, pas un incident vécu. Le taux de couverture réel du pilier
  n'est pas 0,3 % : il est de **0 %**.
- **Preuve** :
  ```
  $ ls Dev/REX/
  .gitkeep   REX - Postgres.md
  $ grep -n "exemple" "Dev/REX/REX - Postgres.md"
  16:## 2026-04-12 — Connection pool exhaustion en prod (exemple)
  30:**Référence** : exemple — remplacer par le lien projet (`Projects/<projet>/Bugs#YYYY-MM-DD`)
  $ grep -n "REX" AI/sessions/2026-06-04-build-v2-fondation.md
  41:- `.gitkeep` dans `Dev/Rules` et `Dev/REX` (vides après le batch).
  ```
  Frontmatter du fichier : `created: 2026-06-08`. La session du 2026-06-04 acte le dossier
  vide. Entre le 2026-06-08 et aujourd'hui (2026-09-02), soit **86 jours**, zéro entrée
  ajoutée — alors que `AI/backlog-enrichissement-brain.md:207` nomme trois incidents vécus
  non capitalisés (Playwright/session, WSL2+GPU+Docker, NebulaGraph).
- **Portée** : 1 fichier sur 297 services, 0 entrée réelle.
- **Cause** : rien ne déclenche l'écriture. Le seul skill du mode build, `enrichir-brain`,
  ne mentionne **jamais** REX (`grep -c REX .claude/skills/enrichir-brain/SKILL.md` → 0).
  Côté projet, `README.md:35` l'écrit noir sur blanc : « pas de skill dédié aujourd'hui,
  Claude écrit à la main ». Un geste manuel, en plein incident, sur un vault distant : il
  n'a jamais eu lieu.
- **Recommandation** : cesser de compter `REX - Postgres` comme une couverture. C'est le
  point d'entrée de la décision du §D.
- **Effort** : S — inclus dans l'option retenue.

### C2. 34 pointeurs REX morts, invisibles du validateur — gravité : sérieux

- **Constat** : 35 fiches Service pointent vers un fichier `Dev/REX/REX - <Nom>.md`
  (46 occurrences). Un seul de ces 35 fichiers existe. Ces pointeurs sont écrits en
  **chemin entre backticks**, pas en wikilink — ils échappent donc doublement au contrôle :
  `check_brain` ne teste que les `[[...]]`, et il exempte de surcroît les `[[REX - *]]`.
  Le vault contient **zéro** wikilink `[[REX ...]]` : l'exception protège un ensemble vide
  tout en désarmant le contrôle pour de futurs vrais liens morts.
- **Preuve** :
  ```
  $ grep -rho "Dev/REX/REX - [^\`]*\.md" Dev/ | sort -u | wc -l
  35
  $ grep -rho "Dev/REX/REX - [^\`]*\.md" Dev/ | sort -u | while read -r p; do [ -f "$p" ] || echo x; done | wc -l
  34
  $ grep -rn "\[\[.*REX" Dev/ Wiki/ MOC/ | wc -l
  0
  $ uv run AI/scripts/check_brain.py | tail -2
  check_brain : 647 pages actives contrôlées
  OK — aucune violation dure.
  ```
  Extrait du mécanisme (`AI/scripts/check_brain.py:190-193`) :
  ```python
  # 5. liens morts (hors REX - * assumés)
  for tgt in LINK_RE.findall(body):
      base = tgt.strip().split("/")[-1]
      if base.lower().startswith("rex - "):
          continue
  ```
  Même exception dans `AI/scripts/build_links.py:100` et `:133` — d'où la ligne
  `AI/index/liens.md:3570` : « **Liens non résolus** … : - aucun ».
- **Portée** : 35 fiches `Dev/Services/`, 46 occurrences, 34 cibles mortes ; 2 scripts.
- **Cause** : les pointeurs ont été semés en lot au moment de la reconstruction v2, en
  anticipation d'un remplissage qui n'est pas venu. L'exception a été ajoutée pour que le
  validateur reste vert malgré cette anticipation — elle est devenue permanente.
- **Recommandation** : supprimer les 46 occurrences (une passe `sed` sur un motif unique,
  la ligne `- Retours d'expérience détaillés : \`Dev/REX/REX - <X>.md\`.`), puis **retirer
  l'exception** des deux scripts. Elle ne protège rien et masque la classe entière des
  liens morts nommés `REX - *`.
- **Effort** : S (< 1 h) — `Dev/Services/*.md` (35 fichiers, une commande),
  `AI/scripts/check_brain.py`, `AI/scripts/build_links.py`.

### C3. Le chemin projet → vault n'existe pas concrètement — gravité : bloquant

- **Constat** : un REX naît en mode projet. `CLAUDE-project.md:83` prescrit d'écrire dans
  `Dev/REX/REX - <service>.md` via `mcp__devbrain__patch_content` / `append_content`. Trois
  ruptures se cumulent sur ce chemin.
  1. **Aucun serveur MCP `devbrain` n'est configuré.** Le vault n'a ni `.mcp.json` ni
     `.claude/settings.json` ; la configuration utilisateur ne déclare aucun serveur.
  2. **Les noms d'outils MCP se contredisent entre deux documents de gouvernance.**
     `CLAUDE-project.md` annonce `search` / `get_file_contents` / `patch_content` /
     `append_content` ; `CONTRIBUTING.md` annonce `search_files` / `read_file_content` /
     `create_file` / `append_to_file`. Deux jeux de noms différents pour le même serveur :
     ni l'un ni l'autre n'a jamais été exécuté.
  3. **Le champ `Référence` du format REX est structurellement non remplissable.** Il doit
     pointer vers `Projects/<projet>/Bugs#YYYY-MM-DD` ; `Projects/` ne contient qu'un
     `_archive/.gitkeep`.
- **Preuve** :
  ```
  $ ls .mcp.json .claude/settings.json 2>&1
  ls: cannot access '.mcp.json': No such file or directory
  ls: cannot access '.claude/settings.json': No such file or directory
  $ python3 -c "import json,os;d=json.load(open(os.path.expanduser('~/.claude.json')));print(list((d.get('mcpServers') or {}).keys()))"
  []
  $ grep -n "mcp__devbrain__" CLAUDE-project.md CONTRIBUTING.md
  CLAUDE-project.md:21:- `mcp__devbrain__search` — recherche full-text dans le brain
  CLAUDE-project.md:25:- `mcp__devbrain__patch_content` — modifier une section (utilisé pour logger un REX)
  CONTRIBUTING.md:136:- `mcp__devbrain__read_file_content` au lieu de `Read` pour les .md du vault
  CONTRIBUTING.md:137:- `mcp__devbrain__create_file` / `patch_content` / `append_to_file` …
  $ find Projects -type f
  Projects/_archive/.gitkeep
  ```
- **Portée** : `CLAUDE-project.md`, `CONTRIBUTING.md`, `INSTALL.md` §10, `Projects/`.
- **Cause** : la procédure a été rédigée à partir de la spec (`brain-v2.md`) et non d'une
  exécution. Trois documents décrivent le même pont sans qu'aucun ne l'ait traversé.
- **Recommandation** : ne pas réparer ce pont pour le seul besoin REX. Si le MCP est
  installé plus tard pour d'autres raisons, unifier d'abord les noms d'outils entre les
  deux documents — c'est un défaut indépendant du sort du pilier.
- **Effort** : L pour réparer le chemin complet (installation MCP + vérification +
  unification des noms + convention `Projects/`) ; S pour la seule unification des noms.

### C4. Le format « un fichier par service » ne convient pas aux incidents réels — gravité : sérieux

- **Constat** : le format suppose qu'on sache à quel service imputer l'incident. Sur les
  trois incidents vécus que le backlog nomme, un seul se range proprement.
  | Incident (backlog:207) | Brique d'imputation | Fiche existante ? |
  |---|---|---|
  | Playwright / session | Playwright | oui |
  | NebulaGraph | Nebula Graph | oui |
  | WSL2 + GPU + Docker | WSL2 ? GPU ? Docker ? | **WSL2 : aucune fiche** |
- **Preuve** :
  ```
  $ ls Dev/Services/ Dev/Outils/ | grep -iE "docker|wsl|nebula|playwright"
  Docker.md
  Nebula Graph.md
  Playwright.md
  ```
  Le tiers des incidents nommés est à l'intersection de trois briques, dont une qui n'est
  pas fichée. Le format n'a aucun emplacement pour lui.
- **Portée** : conception du pilier, `CLAUDE-build.md:132-188`.
- **Cause** : le format a été calqué sur la structure du vault (une fiche = une brique),
  pas sur la forme des incidents (un incident = une intersection).
- **Recommandation** : quel que soit le sort du pilier, poser la règle d'imputation
  explicitement — **un incident inter-briques se range sous la brique qui a porté le
  correctif**, avec mention des autres en clair. Une ligne de convention, pas un dossier.
- **Effort** : S — une ligne dans `CLAUDE-build.md`.

### C5. Le gabarit REX n'est contrôlé par rien, et il est cassé — gravité : mineur

- **Constat** : `check_brain.ALLOWED` ne couvre que `service` et `concept`. Le type `rex`
  n'a aucun contrôle de frontmatter. Et `Templates/REX-entry.md` se termine par une ligne
  parasite `galaxie: dev` après le séparateur `---` : coller ce gabarit dans une fiche y
  injecte du frontmatter en plein corps.
- **Preuve** :
  ```
  $ grep -n "^ALLOWED" AI/scripts/check_brain.py
  52:ALLOWED = {"service": SERVICE_ALLOWED, "concept": CONCEPT_ALLOWED}
  $ tail -3 Templates/REX-entry.md
  
  ---
  galaxie: dev
  ```
- **Portée** : `Templates/REX-entry.md` (2 lignes), `AI/scripts/check_brain.py`.
- **Cause** : copier-coller depuis `Templates/REX.md` lors de la scission du gabarit en
  deux fichiers ; jamais détecté parce que jamais utilisé.
- **Recommandation** : le défaut disparaît avec le gabarit si l'on fusionne. Sinon,
  supprimer les deux lignes et ajouter `rex` à `ALLOWED`.
- **Effort** : S.

## D. La décision : chiffrage des trois issues

Les trois options ont été chiffrées en fichiers réellement touchés, comptés commande à
l'appui. Un fichier « touché » signifie une édition manuelle ; les 35 fiches Service se
traitent par une passe mécanique unique et comptent pour un geste.

### Option A — réparer

Ce qu'il faut construire, dans l'ordre : un déclencheur (skill `log-rex`, aucun n'existe,
et `enrichir-brain` ignore le sujet) ; le pont projet → vault (installation et vérification
du MCP `devbrain`, unification des noms d'outils entre `CLAUDE-project.md` et
`CONTRIBUTING.md`, création de la convention `Projects/<projet>/Bugs.md` pour rendre le
champ `Référence` remplissable) ; l'allègement du format (5 champs → 3) ; la réparation des
34 pointeurs, qui ne redeviennent vivants qu'au fil des REX écrits, donc jamais
mécaniquement ; la correction de `Templates/REX-entry.md` ; l'ajout de `rex` à
`check_brain.ALLOWED` et le retrait de l'exception.

| Poste | Volume |
|---|---|
| Skill à écrire | 1 (`.claude/skills/log-rex/SKILL.md`, ~200 lignes) |
| Infrastructure | 1 serveur MCP à installer et vérifier |
| Consignes à réécrire | 4 (`CLAUDE-project.md`, `CONTRIBUTING.md`, `CLAUDE-build.md`, `README.md`) |
| Gabarits | 2 à corriger et alléger |
| Scripts | 2 (`check_brain.py`, `build_links.py`) |
| Convention à créer | `Projects/<projet>/Bugs.md` (dossier vide aujourd'hui) |
| Pointeurs morts | 34, non résolus par la réparation |

**Effort : L (chantier, ≥ 2 sessions).** Et c'est un pari : la même mécanique, entièrement
documentée depuis le 2026-06-08, a produit zéro entrée en 86 jours. Réparer, c'est ajouter
un déclencheur à une chaîne dont trois maillons sur trois sont rompus (C3), en supposant que
seul le déclencheur manquait.

### Option B — fusionner

Les retours partent en `## Pièges` de la fiche Service, le pilier disparaît.

Fait décisif : la cible de fusion **existe déjà et fonctionne à 100 %**.

```
$ ls Dev/Services/*.md | wc -l
297
$ grep -l "^## Pièges" Dev/Services/*.md | wc -l
297
```
Aucune des 297 sections n'est vide ; médiane 4 lignes, maximum 6. Le contenu y est déjà de
la bonne nature — extrait de `Dev/Services/FastAPI.md` :
> - Une route déclarée `def` (et non `async def`) qui fait de l'I/O bloque l'event loop sous
>   charge → la basculer en `async def` ou la déporter dans un threadpool.

| Poste | Volume |
|---|---|
| Suppressions | 4 fichiers : `Dev/REX/REX - Postgres.md`, `Dev/REX/.gitkeep`, `Templates/REX.md`, `Templates/REX-entry.md` |
| Fiches Service | 35 fichiers, 46 lignes — **une passe `sed`, un geste** |
| Contenu à reporter | **aucun** : l'unique entrée est un exemple auto-déclaré (C1) |
| Consignes à réécrire | 8 : `CLAUDE.md` (7 mentions), `CLAUDE-build.md` (20 mentions dont la section `## Conventions REX`, l. 132-188), `CLAUDE-project.md` (5, dont la section « Log de bug » l. 79-99), `CONTRIBUTING.md` (2 lignes), `README.md` (4), `INSTALL.md` (2), `AI/design/brain-v2.md` (4), `.claude/skills/planifier-projet/SKILL.md` (2) |
| Gouvernance | `Documentation/general/tags.md` : retirer `rex` et `bugs` (portés par 1 seule page, celle qu'on supprime) → vocabulaire 321 → 319 |
| Gabarit | `Templates/Service-Dev.md` : 1 ligne (le commentaire de la section `## Pièges`) |
| Scripts | 6 : `check_brain.py` (l. 18, 190-193), `build_links.py` (l. 100, 133), `build_index.py` (l. 108), `audit_mesures.py` (§8, l. 204-212), `session_to_devbrain.py` (l. 158), `gen-stubs-batch.ps1` (l. 85) |
| Régénération | `build_index`, `build_links`, `build_mocs` |

**Effort : M (une session).** Rien à construire, rien à migrer, le seul contenu à trancher
est un exemple.

Contrainte honnête à signaler : les fiches Service ont une médiane de 63 lignes, un p90 à
69, un maximum à 87, pour un seuil d'avertissement `check_brain` à 90. Une fiche du p90 ne
supporte que 4 à 6 entrées datées avant de déclencher le WARN. Au rythme observé — zéro
entrée en 86 jours — la contrainte n'est pas mordante, mais elle existe et il faudra la
relever si l'usage décolle un jour.

### Option C — assumer

Le dossier reste, vide, documenté comme optionnel.

| Poste | Volume |
|---|---|
| Consignes à amender | 4 : `CLAUDE.md`, `README.md`, `AI/design/brain-v2.md`, `CLAUDE-build.md` (« cinq piliers » → « quatre + REX optionnel ») — ~10 lignes |
| Pointeurs morts | 34 à supprimer **quand même** (même passe `sed` que B) |
| Exception validateur | à retirer **quand même** : elle protège 0 wikilink (C2) |
| Gabarits | 2 conservés, dont 1 cassé à corriger (C5) |
| `REX - Postgres` | à supprimer (exemple orphelin) ou à étiqueter |
| Scripts | 2 à 3 |

**Effort : S à M.** Moins cher que B à court terme, mais il conserve la totalité de la
surface de gouvernance : la section `## Conventions REX` de `CLAUDE-build.md` (57 lignes),
deux gabarits, une convention de nommage, une ligne dans la table des types, un dossier.
Cette surface continue d'être lue par tout agent qui ouvre `CLAUDE-build.md`, et le compteur
`## 8. Couverture REX` de `audit_mesures.py` continue d'afficher un manque qu'on aura décidé
de ne pas combler. C'est le coût récurrent qu'on paie pour ne pas trancher.

### Recommandation : fusionner (option B)

Cinq raisons, dans l'ordre de poids.

1. **Le pilier n'a jamais fonctionné, et pas faute de documentation.** 86 jours, 0 entrée
   réelle, alors que le mécanisme est décrit dans 6 documents et 2 gabarits (C1).
2. **La cible de fusion existe déjà, à 100 % de couverture.** 297/297 fiches Service ont un
   `## Pièges` rempli, de la bonne nature. Il n'y a rien à construire ni à migrer.
3. **Réparer, c'est réparer trois choses à la fois.** Pas de déclencheur, pas de MCP, pas de
   `Projects/` : le chemin de retour est rompu en trois points indépendants (C3). L'option A
   parie que le déclencheur suffira.
4. **Le pilier coûte aujourd'hui.** 34 pointeurs morts qu'aucun contrôle ne voit, une
   exception permanente dans deux scripts qui ne protège aucun lien, un gabarit cassé jamais
   détecté parce que jamais utilisé (C2, C5).
5. **Le format est faux pour les incidents réels.** Un tiers des incidents nommés est
   inter-briques et n'a aucun emplacement (C4). La fusion règle le cas par une règle
   d'imputation d'une ligne au lieu d'un dossier.

Deux conventions à poser en même temps que la fusion, sans quoi elle perd ce que le pilier
promettait :

- **Entrée datée dans `## Pièges`** pour un incident vécu, distinct d'un piège générique :
  `- 2026-09-02 — <symptôme> : <correctif en une ligne>.` La date est ce qui distingue le
  vécu du documenté ; c'est le seul élément du format REX qui mérite d'être conservé.
- **Imputation inter-briques** : sous la brique qui a porté le correctif, les autres citées
  en clair dans la ligne (C4).

## Ce qui va bien

- **La section `## Pièges` est le pilier REX qui a réussi.** 297 fiches sur 297, aucune
  vide, médiane 4 lignes, contenu opérationnel et non générique. Elle a atteint sans
  déclencheur ce que REX n'a pas atteint avec six documents et deux gabarits — parce
  qu'elle est remplie au moment où la fiche est écrite, par le skill qui l'écrit. Ne pas
  y toucher : c'est la cible de la fusion, pas un chantier.
- **Le pilier a été correctement isolé.** Aucune fuite : `Home.md`, `MOC/` et
  `Documentation/general/taxonomie.md` ne mentionnent REX nulle part. La navigation ne
  dépend pas de lui, ce qui rend la suppression peu coûteuse. La section §8 de
  `audit_mesures.py` mesurait honnêtement le trou depuis le début.
- **Le gabarit de fiche Service prévoyait déjà l'articulation.** `Templates/Service-Dev.md`
  ligne 36 : « court ; les vrais retours d'expérience vont dans `Dev/REX/…` ». L'intention
  de séparation était claire et cohérente — c'est le chemin d'écriture qui a manqué, pas
  la conception de la fiche.
- **Le contenu de `REX - Postgres` est un bon gabarit.** Symptôme → cause racine → fix
  numéroté → référence → leçon : le format est juste, l'exemple est réaliste et pédagogique.
  Sa faute n'est pas sa qualité, c'est qu'il soit resté seul.

## Questions laissées ouvertes

1. **Que faire du contenu de `REX - Postgres` ?** L'auditeur constate que c'est un exemple
   auto-déclaré et recommande de le supprimer. Si le propriétaire estime que l'incident
   décrit est réel (pool exhaustion, PgBouncer) et non fictif, ses trois lignes de leçon
   ont leur place dans `Dev/Services/Postgres.md` `## Pièges`. Arbitrage du propriétaire :
   exemple inventé ou incident vécu maquillé en exemple ?
2. **Un journal chronologique unique est-il souhaité ailleurs ?** L'axe demandait si un
   journal serait plus honnête que la fiche par service. La réponse de cet audit est qu'il
   le serait — mais un journal reste un pilier à alimenter, avec le même problème de
   déclencheur. Le recommander reviendrait à remplacer un pilier vide par un autre. Si le
   propriétaire veut malgré tout un journal, c'est une décision de conception hors du
   périmètre de cet axe.
3. **Le MCP `devbrain` doit-il être installé ?** C3 le constate absent et les noms d'outils
   contradictoires entre deux documents. Ce défaut est indépendant du sort de REX : il
   affecte tout le mode projet. Il déborde de cet axe.
4. **Le seuil `SIZE_WARN` des fiches Service (90 lignes) doit-il monter ?** Il ne mord pas
   aujourd'hui (max observé 87), mais il mordra si les entrées datées s'accumulent après
   la fusion. À trancher le jour où une fiche dépasse.
5. **Les tags `rex` et `bugs` disparaissent-ils du vocabulaire ?** Ils ne sont portés que
   par la page supprimée. Les retirer fait passer le vocabulaire de 321 à 319 tags. Sauf
   volonté de les réserver pour un usage futur.
