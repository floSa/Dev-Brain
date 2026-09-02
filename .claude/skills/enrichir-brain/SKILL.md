---
name: enrichir-brain
description: |
  Use this skill to capture knowledge into the DevBrain (Dev/ and Wiki/).
  Triggers: "ajoute <techno/sujet> au brain", "documente <X>", "ajoute le service Y",
  "ajoute le concept Z", or, at the end of a conversation, "mets à jour DevBrain" /
  "enrichis le brain" (sweep mode). Creates the requested page AND the missing
  connected pages (parent concept, alternatives, comparatif), wires links, keeps
  alternatives and pitches in sync bidirectionally. CAPTURE ONLY: closing the write
  (regenerate, validate, commit) belongs to the companion skill `cloturer-brain`.
  Also owns the UPDATE path — "le pitch de X a change", "X est abandonne",
  "reclasse X", a rename or a deletion: propagate the side effects of a changed
  field to its consumers (see *Procedure — mode mise a jour*).
---

# Skill — enrichir-brain

Skill de **capture** du DevBrain v2. Implémente le workflow W1 de `AI/design/brain-v2.md` (§2, §7.1). Exigence cardinale : **faire les choses bien, sans rien oublier** — la page demandée *et* ses pages connexes, les liens, la synchro bidirectionnelle, l'index.

## Quand l'utiliser

- **Mode ciblé** : ajouter une brique précise. « ajoute Weaviate », « ajoute le concept bases vectorielles ».
- **Mode balayage** : en fin de conversation, « mets à jour DevBrain » → repérer tout ce qui mérite une page et tout traiter.
- **Mode mise à jour** : une page existe déjà et un champ change. « le pitch de X a changé », « X est abandonné », « reclasse X en `<catégorie>` », un renommage, une suppression. C'est le cas le plus dangereux : la page a des **consommateurs**. Voir *Procédure — mode mise à jour*.

Distinct de :
- `planifier-projet` (consomme le brain pour cadrer un projet, n'écrit pas de fiches).

## Pré-requis

Mode build (pages Dev/) ou mode wiki (pages Wiki/). Ne jamais toucher au réservoir v1 (`Services/`, `Patterns/`, `Rules/`, `Bugs/` à la racine) — c'est de la référence en lecture seule.

## Appuis (à lire AVANT d'écrire)

- `AI/index/brain-index.json` — catalogue courant (pitch, tags, alternatives, complements, categorie, famille, role, maturite). **Ne jamais le charger en entier** : l'interroger par tranches via `AI/scripts/query_index.py` (existence, candidats d'une catégorie, pages d'un tag). C'est la règle qui tient quand le brain devient grand — la sortie est bornée par le nombre de correspondances, pas par la taille du brain.
- `Documentation/general/tags.md` — vocabulaire de tags **fermé**. Piocher ici, ne jamais inventer.
- `Documentation/general/taxonomie.md` — les **deux axes** de rangement : `categorie:` (le domaine) et `famille:` (la nature technique, 9 valeurs fermées, arbre de décision F1→F9). `role:` est un troisième champ, la nature **éditoriale** de la page (`brique`, `notion`, `pattern`, `rule`) — il ne se confond ni avec l'un ni avec l'autre.
- `Documentation/general/themes.md` — vocabulaire `domaines:`.
- `Templates/Service-Dev.md`, `Templates/Concept-Wiki.md` — gabarits stricts (§5).

## Conventions v2 non négociables


- **Rangement par NATURE, pas par audience** : tout ce qui est **technique** → `Dev/` (jamais `Wiki/`). Brique à déployer (service, framework, lib, BDD) → `Dev/Services/` ; **outil technique** que l'on utilise (client GUI, CLI, utilitaire — DBeaver, pgAdmin, uv…) → `Dev/Outils/` (`role: brique`, `categorie: <domaine>/<sous-domaine>` — **même vocabulaire de 94 valeurs que les Services**, il n'y a plus de préfixe `tooling/` : DBeaver → `database/admin`, uv → `devtools/paquet`). `Wiki/` = **notions** (`Concepts/`) + **skills/extensions de pratique perso** (`Outils/` : Claude Code, Obsidian, MCP). Doute « Dev ou Wiki ? » → est-ce technique ? alors Dev.
- **Ton impersonnel** partout : ni « tu » ni « vous ». Phrases courtes, hiérarchie parties + bullets.
- **Frontmatter exact** selon le gabarit (§5) : ni plus, ni moins de champs.
- **Pitch unique, une seule convention de réinjection** : chaque page Dev porte SON `pitch:` (une ligne), écrit une seule fois. Une donnée, trois usages (frontmatter, alternatives, propositions de `planifier-projet`). La convention de réinjection est **unique et arbitrée** (`AI/design/brain-v2.md` §5.1, *Convention unique de réinjection du pitch*), en trois clauses :
  1. cible listée dans le frontmatter `alternatives:` → la ligne **commence par** le `pitch:` courant de la cible, à la normalisation près (`**` retirés, espaces réduits, casse ignorée) ; **suffixe libre autorisé après** ;
  2. cible absente du frontmatter `alternatives:` → mention de voisinage, ligne libre mais **préfixée de `voisin :`** ;
  3. jamais de prose à la place du pitch d'une cible listée en `alternatives:` — soit la prose devient le suffixe (clause 1), soit la cible sort du frontmatter (clause 2).
  Le pitch se **copie** depuis la cible, il ne se retape jamais.
- **Liens qualifiés en cas de collision** : si un nom existe aussi dans le réservoir v1 (ex. `Services/VectorDB/Qdrant.md`), lier en `[[Dev/Services/Qdrant|Qdrant]]` pour viser le v2 sans ambiguïté. Sinon, lien nu.
- **Catégorie ou tag manquant → demander**, jamais inventer. L'ajout se fait d'abord dans `Documentation/general/`.
- **Faits vérifiés sur le web, d'office (sans demander la permission)** : avant d'écrire une fiche, vérifier en ligne (WebSearch / WebFetch) les champs factuels — `licence_type`, `langage`, `maturite`, `hosted`, `scaling`, `url_docs` / `url_repo`, statut actuel (actif / déprécié / racheté). Ne jamais demander l'autorisation de vérifier : le faire directement. Info introuvable ou ambiguë → laisser le champ vide, ne pas inventer.

## Procédure — mode ciblé

1. **Interroger l'état (par tranches, jamais l'index entier)** :
   - existence (nom + alias) : `uv run AI/scripts/query_index.py --name "<X>"` ;
   - candidats alternatives : `uv run AI/scripts/query_index.py --categorie "<cat>"` ;
   - vocabulaire de tags : `Documentation/general/tags.md` ; catégories : `taxonomie.md` (fichiers bornés).
2. **Vérifier l'existence** de la page (nom + `alias`). Si elle existe en v2 → **basculer sur la *Procédure — mode mise à jour*** ci-dessous (ne pas improviser un patch : une page qui existe a des consommateurs). Si elle n'existe qu'en réservoir v1 → créer la version v2 (ne pas modifier le v1).
3. **Identifier les pages connexes nécessaires** :
   - concept parent côté Wiki (un service vectoriel → `Bases de données vectorielles`) ;
   - comparatif `.base` de la catégorie ;
   - alternatives à citer (même `categorie:`).
   Lister celles qui manquent.
4. **Vérifier les faits sur le web (d'office), puis créer / mettre à jour chaque page** depuis le bon gabarit :
   - service → `Templates/Service-Dev.md` dans `Dev/Services/` ;
   - concept → `Templates/Concept-Wiki.md` dans `Wiki/Concepts/`.
5. **Poser les tags** depuis `tags.md` uniquement. Besoin d'un tag absent → le proposer, l'ajouter au vocabulaire, puis l'utiliser.
6. **Câbler les wikilinks** dans les deux sens du couple Dev↔Wiki (le service lie son concept ; le concept liste le service dans *Approches voisines*), plus le `.base` du comparatif.
7. **Synchroniser bidirectionnellement** :
   - **Alternatives** : si A liste B, alors B doit lister A. Mettre à jour le frontmatter `alternatives:` **et** la section *Alternatives* de chaque page concernée.
   - **Pitches** : la ligne affichée pour une cible dans une section *Alternatives* suit la **convention unique de réinjection** (clauses 1-3 ci-dessus). Vérifier avec `[V1]` de la table des effets de bord. Si un pitch a changé, ne pas resynchroniser à la main ici : passer par la *Procédure — mode mise à jour*.
8. **Clôturer** : invoquer le skill `cloturer-brain`. Il régénère les artefacts, fait
   passer `check_brain` au vert, vérifie la divergence avec `origin/main`, puis commet,
   pousse et intègre dans `main`. La capture n'est pas finie tant que la clôture n'a pas
   tourné — mais elle ne fait pas partie de ce skill-ci.

**Sortie explicite attendue de ce skill** : « la capture est faite, la clôture reste à
lancer » — ou, si `cloturer-brain` a déjà tourné, son résultat. Ne jamais laisser l'état
implicite : c'est ainsi qu'un index périmé survit à une session.

## Procédure — mode mise à jour

Déclencheurs : « enrichis la fiche X depuis cet article », « le pitch de X a changé »,
« X est abandonné », « reclasse X en `<catégorie>` », un renommage, une suppression — et
l'étape 2 de la procédure ciblée quand la page existe déjà. `CLAUDE-build.md` (workflow
général, point 5) renvoie ici.

**Règle d'or** : une modification de champ n'est pas finie quand la page est enregistrée.
Elle est finie quand ses **consommateurs** sont à jour et que la **commande de vérification**
de la table ci-dessous ne renvoie plus aucun écart. Une page qui existe a des consommateurs ;
une page qu'on crée n'en a pas. C'est toute la différence avec la procédure ciblée.

1. **Relever l'état avant**, avant toute écriture :
   ```bash
   sed -n '/^---$/,/^---$/p' "Dev/Services/<X>.md" | tee /tmp/avant-X.txt
   ```
   Fin d'étape vérifiable : le fichier contient la valeur d'origine de chaque champ.

2. **Déclarer les champs qui changent**, un par un, sous la forme `champ : avant → après`.
   Fin d'étape vérifiable : une liste explicite. Un champ absent de cette liste n'a pas le
   droit de bouger — l'étape 5 le contrôle.

3. **Dresser la liste nominative des consommateurs** : pour chaque champ déclaré, lire sa
   ligne dans la *table des effets de bord* et lancer sa **commande d'inventaire**. Fin
   d'étape vérifiable : une liste de **chemins de fichiers**, pas une intention. « Les
   citeurs de X » n'est pas une liste ; `Dev/Services/Qdrant.md, Dev/Services/Milvus.md…`
   en est une.

4. **Vérifier les faits sur le web (d'office)** si un champ factuel change (`maturite`,
   `licence_type`, `langage`, `url_docs`, `url_repo`). Fin d'étape vérifiable :
   source citée, ou champ laissé vide — jamais deviné.

5. **Patcher la page, section par section** — jamais de réécriture intégrale. Fin d'étape
   vérifiable :
   ```bash
   git diff --stat -- "Dev/Services/<X>.md"   # un seul fichier, delta borné
   git diff -- "Dev/Services/<X>.md"          # aucun champ hors de la liste de l'étape 2
   ```

6. **Propager chaque consommateur `[M]`** de la liste de l'étape 3. Le pitch se **copie**
   depuis la cible (convention unique, `AI/design/brain-v2.md` §5.1), il ne se retape pas.
   Fin d'étape vérifiable : chaque fichier de la liste de l'étape 3 apparaît dans
   `git diff --name-only`. Un fichier de la liste absent du diff = propagation oubliée.

7. **Lancer la commande de vérification de chaque champ modifié** (colonne *Vérification*
   de la table). Fin d'étape vérifiable : **0 écart** sur chacune. Ne pas passer à l'étape 8
   avec un écart restant — c'est exactement ainsi que naissent les pitchs périmés.

8. **Régénérer, puis contrôler que la régénération a bien pris** — ne pas la croire sur
   parole :
   ```bash
   uv run AI/scripts/build_index.py && uv run AI/scripts/build_mocs.py && uv run AI/scripts/build_links.py
   uv run AI/scripts/query_index.py --name "<X>" --fields nom,pitch,categorie,famille,role,maturite
   grep -rl "<X>" MOC/                 # hubs où la page apparaît désormais
   ```
   Fin d'étape vérifiable : l'index renvoie les valeurs **après**, et la page apparaît dans
   les hubs attendus — et plus dans ceux qu'elle a quittés.

9. **Relire le diff complet.** Il doit contenir exactement : la page, les fichiers de
   l'étape 3, les artefacts générés. Rien d'autre.
   ```bash
   git status --porcelain
   git diff --stat
   ```
   C'est la dernière occasion de voir une propagation oubliée ou une page touchée par
   accident. Un fichier inattendu dans ce diff est une erreur, pas une surprise.

10. **Clôturer** : invoquer `cloturer-brain`. Il est idempotent, donc relancer la
    régénération ne coûte rien, et c'est lui qui porte la validation finale, la
    vérification de divergence et l'intégration.

### Table des effets de bord — champ modifié → consommateurs → vérification

Conventions de la colonne *Consommateurs* : **[M]** propagation manuelle obligatoire (rien
ne la fera à votre place) · **[G]** corrigé par relance d'un générateur · **[D]** déjà
couvert par une règle dure de `check_brain` · **[!]** dérive silencieuse, aucun contrôle
n'existe encore. Source : annexe A de `AI/audit/rapports/axe-2-integrite.md`.

| Champ modifié | Consommateurs à repropager | Inventaire | Vérification (0 écart attendu) |
|---|---|---|---|
| `pitch:` | **[M]** lignes `## Alternatives` des pages qui citent la cible · **[G]** puces des MOC · **[G]** `brain-index.json/.md` · vues `.base` : lecture directe, rien à faire | `[V1] <X>` **avant** l'édition : il liste exactement les puces qui réinjectent le pitch, et elles seules — `grep -rln "Dev/Services/<X>" Dev/ Wiki/` ratisse trop large (corps et `## Liens` compris) | `[V1] <X>` **après** propagation : que des `OK` |
| `nom:` ou renommage du fichier | **[M]** nom du fichier et champ `nom:` · **[D]** wikilinks du corps · **[!]** wikilinks du **frontmatter** (`alternatives:`, `complements:`) · **[M]** libellés des puces `## Alternatives` · **[!]** listes de noms codées en dur dans les `.base` · **[G]** index, MOC, liens | `grep -rn "<Ancien nom>" Dev/ Wiki/ MOC/ Documentation/` | la même commande doit renvoyer **0 ligne** ; puis `grep -rn "file.name ==" Dev/Patterns/` et `uv run AI/scripts/check_brain.py` |
| `categorie:` | **[D]** valeur présente dans `taxonomie.md` · **[!]** entrée/sortie des comparatifs `.base` filtrés par catégorie · **[G]** hub `MOC/Categories/<tête>` — la page change de hub · **[M]** jeu d'alternatives pertinentes : les pairs de la nouvelle catégorie | `grep -l 'categorie == "<ancienne>"' Dev/Patterns/*.base` puis idem avec `<nouvelle>` ; ajouter `startsWith("<ancienne>` pour les filtres par préfixe | `uv run AI/scripts/check_brain.py` valide l'appartenance à la taxonomie (règle dure — les valeurs légales viennent des blocs de code de `taxonomie.md`, pas de ses puces de prose : ne pas se fier à un `grep`) ; `grep -l '^categorie: <ancienne>$' Dev/Services/*.md Dev/Outils/*.md \| wc -l` → le comparatif quitté garde **≥ 2 membres** (0 ou 1 = comparatif à vider ou à refiltrer) ; `grep -rl "<X>" MOC/Categories/` après `build_mocs` |
| `famille:` | **[D]** valeur ∈ énumération fermée du bloc de code `famille` de `taxonomie.md` (R14) · **[D]** champ indexé (`build_index.FIELDS`) et renvoyé par défaut par `query_index.py` — un consommateur machine filtre dessus · **[M]** aucune `.base` ne filtre encore sur `famille` : l'ajouter est une décision éditoriale, pas une propagation | `uv run AI/scripts/query_index.py --famille <valeur> --fields nom,path` | `uv run AI/scripts/check_brain.py` ; la famille doit être **dérivée** de l'arbre F1→F9 (première réponse positive gagne) et non choisie — si deux branches conviennent, c'est une règle de départage R1-R6 qui tranche ; si aucune ne tranche, laisser vide et demander |
| `tags:` | **[D]** tags présents dans `tags.md` · **[!]** entrée/sortie des comparatifs `.base` filtrés par tag · **[G]** index des tags de `liens.md` | `grep -l '"<tag>"' Dev/Patterns/*.base` | `grep -c "<tag>" Documentation/general/tags.md` → ≥ 1 ; `uv run AI/scripts/check_brain.py` |
| `role:` | **[D]** enum fermée de 4 valeurs peuplées (`brique`, `notion`, `pattern`, `rule` ; `hub` et `comparatif` arrivent aux lots 3 et 5) · **[D]** il choisit le **gabarit** que le validateur applique : changer `role:` change la liste des champs autorisés · **[G]** index, MOC, liens, couleur du graphe | `uv run AI/scripts/query_index.py --role brique --categorie <cat>` | `uv run AI/scripts/check_brain.py` — un champ hors gabarit sort en dur |
| `maturite:` | **[D]** enum fermée · **[!]** 6 `.base` filtrent `maturite != "deprecated"` ou `== "production"` — une page qui bascule sort de la vue sans bruit · **[D]** **indexé**, et c'est le SEUL critère éliminatoire depuis la suppression de `status:` : `planifier-projet` n'ouvre pas la fiche · **[M]** si `deprecated` : renseigner `alternatives:` (c'est lui qui dit quoi proposer à la place) **et** nommer le successeur dans le corps, pour le lecteur humain | `grep -l 'maturite' Dev/Patterns/*.base` | `sed -n '/^maturite:/p;/^alternatives:/p' "Dev/Services/<X>.md"` → une brique `deprecated` nomme ses successeurs ; `uv run AI/scripts/verifier_fraicheur.py` signale le contraire |
| `complements:` | **[D]** réciprocité, comme `alternatives:` : si A cite B, B cite A · **[M]** la section `## Alternatives` ne le couvre PAS — le lot 6 ouvrira une section `### Compléments` · **[G]** index | `grep -rn "complements:" Dev/ Wiki/` | `uv run AI/scripts/check_brain.py` |
| `alias:` | **[!]** résolution des liens `[[alias]]` · **[!]** détection d'existence à l'étape 1 de la procédure ciblée · **[!]** unicité — 52 collisions connues dans le vault | `uv run AI/scripts/query_index.py --name "<alias>" --fields nom,path` | la même commande, après `build_index`, renvoie `"count": 1` |
| `domaines:` | **[G]** comptes par sous-domaine des `MOC/Themes/*` · **[!]** appartenance au vocabulaire `themes.md` | `grep -c "<valeur>" Documentation/general/themes.md` | cette commande renvoie ≥ 1 ; `grep -rl "<X>" MOC/Themes/` après `build_mocs` |
| `alternatives:` | **[D]** réciprocité — si A cite B, B cite A · **[M]** la section `## Alternatives` liste les mêmes cibles · **[M]** la ligne de chaque cible suit la convention unique de réinjection | `grep -n "alternatives:" "Dev/Services/<X>.md"` | `uv run AI/scripts/check_brain.py` pour la réciprocité, puis `[V1] <X>` et `[V1]` sur chaque cible ajoutée |
| `licence_type:`, `hosted:`, `scaling:`, `langage:` | **[D]** enums fermées, sauf `langage` · **[!]** `hosted:` et `scaling:` sont **conditionnels à `famille:`** : ils n'existent que pour `plateforme`, `saas`, `application` — les poser ailleurs sort en dur (R16) · **[!]** `hosted:` est une **liste** (`[self]`, `[managed]`, `[self, managed]`), jamais un scalaire · lus en direct par les vues `.base`, rien à propager | — | `uv run AI/scripts/check_brain.py` |
| `url_docs:`, `url_repo:` | **[!]** joignabilité, aucun contrôle en place | — | `curl -sS -o /dev/null -w '%{http_code}\n' -L --max-time 10 "<url>"` → 2xx/3xx ; 403 et 429 tolérés, 404 et NXDOMAIN non |
| **Suppression d'une page** | **[D]** liens morts dans le corps des citeurs · **[!]** liens morts en **frontmatter** · **[!]** réciprocité : `check_brain` ignore en silence une cible absente de l'index · **[!]** un `.base` peut tomber à 0 membre · **[G]** index, MOC, liens | `grep -rn "<X>" Dev/ Wiki/ MOC/ Documentation/` | la même commande doit renvoyer **0 ligne** ; puis `grep -l '^categorie: <cat>$' Dev/Services/*.md Dev/Outils/*.md \| wc -l` sur chaque `.base` concerné (**≥ 2**) et `uv run AI/scripts/check_brain.py` |

### `[V1]` — vérification de la réinjection du pitch

Contrôle les trois clauses de la convention unique (`AI/design/brain-v2.md` §5.1) sur les
sections `## Alternatives` du vault. Avec un argument : une seule cible. Sans argument :
balayage complet. Lit les **fichiers**, pas l'index — donc utilisable avant toute
régénération. Code de retour 1 s'il reste une ligne à traiter.

```bash
cat > /tmp/verif_pitch.py <<'PY'
import re, sys, pathlib
cible = sys.argv[1] if len(sys.argv) > 1 else None
pages = sorted(list(pathlib.Path('Dev').rglob('*.md')) + list(pathlib.Path('Wiki').rglob('*.md')))
txt = {p: p.read_text(encoding='utf-8') for p in pages}
fm = lambda t: t.split('---')[1] if t.startswith('---') else ''
pit = {p.stem: (re.search(r'^pitch:\s*"?(.*?)"?\s*$', fm(t), re.M) or [None, None])[1] for p, t in txt.items()}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('**', '')).strip().lower()
ko = 0
for p, t in txt.items():
    sec = re.search(r'^## Alternatives\s*$(.*?)(^## |\Z)', t, re.M | re.S)
    if not sec:
        continue
    for li in re.findall(r'^\s*[-*] .*$', sec.group(1), re.M):
        m = re.search(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', li)
        if not m:
            continue
        c = (m.group(2) or m.group(1)).split('/')[-1]
        if cible and c != cible:
            continue
        aff = re.sub(r'^\s*[-*] *\[\[[^\]]*\]\] *[—–:-]? *', '', li).strip()
        if not pit.get(c):
            etat = 'SANS-PITCH'                       # cible sans pitch: -> arbitrer
        elif c not in fm(t):
            etat = 'VOISIN' if aff.lower().startswith('voisin') else 'VOISIN-SANS-MARQUEUR'
        elif norm(aff).startswith(norm(pit[c])):
            etat = 'OK'                               # clause 1, suffixe libre inclus
        else:
            etat = 'DERIVE'                           # pitch perime, ou prose (clause 3)
        if etat != 'OK':
            ko += 1
            print(f'{etat:22} {p} -> {c}\n{"":22} affiche : {aff}\n{"":22} pitch   : {pit.get(c)}')
        elif cible:
            print(f'{etat:22} {p} -> {c}')
print(f'\n{ko} ligne(s) a traiter' + (f' pour {cible}' if cible else ' dans tout le vault'))
sys.exit(1 if ko else 0)
PY
python3 /tmp/verif_pitch.py "<Cible>"    # sans argument : balaye tout le vault
```

État de référence au 2026-09-02, balayage complet : **26 lignes** à traiter sur 817
(9 `DERIVE`, 15 `VOISIN-SANS-MARQUEUR`, 2 `SANS-PITCH`). Ce reste est connu et documenté
(`AI/design/brain-v2.md` §5.1) ; une passe de contenu dédiée le balaiera. Une mise à jour
ne doit pas **augmenter** ce compte : c'est le seuil à ne pas dépasser tant que la passe
n'a pas eu lieu.

### Cas particulier — retour d'expérience daté

Un bug rencontré n'est pas une modification de champ : il s'écrit dans la section
`## Pièges` de la fiche concernée et ne déclenche aucune propagation.

- **Format** : `- YYYY-MM-DD — <symptôme> : <correctif>.` La date est ce qui distingue le
  vécu du piège documenté.
- **Imputation d'un incident né entre deux briques** : il s'inscrit **sous la brique qui a
  porté le correctif**, une seule fois, les autres briques nommées en clair dans la ligne.
  **La fiche de l'autre brique ne le mentionne pas** — une entrée dupliquée devient une
  seconde chose à synchroniser, c'est-à-dire le défaut même que cette procédure corrige. Le
  nom en clair suffit à la retrouver par `grep`.
- **Vérification** : `grep -n '^- [0-9]\{4\}-' "Dev/Services/<X>.md"` renvoie l'entrée, et
  `uv run AI/scripts/check_brain.py` reste vert — la fiche ne doit pas franchir le seuil
  d'avertissement de taille.

## Procédure — mode sujet / balayage (plan d'abord, PUIS go)

Déclencheurs : « fais-moi les pages sur les statistiques », « ajoute le sujet RAG », ou en fin de conversation « mets à jour DevBrain ».

1. **Cadrer le périmètre** → dresser la liste des pages candidates : notion(s) + briques/patterns. Pour chacune : nom, `role:`, catégorie pressentie, tags pressentis (du vocabulaire), alternatives pressenties, et si elle existe déjà (`query_index.py`). Au besoin, ouvrir l'ancienne page du sujet dans `Archive-v1/` (voir `Archive-v1/_inventaire.md`) pour en réutiliser le contenu.
2. **Présenter le plan et ATTENDRE le GO.** Ne rien créer avant validation. L'utilisateur ajoute / retire / renomme des pages.
3. **Écrire la file validée** dans `AI/backlog.md` (une page par ligne).
4. **Drainer la file une page à la fois**, chacune via la procédure ciblée ci-dessus. Cocher au fur et à mesure.
5. **Clôturer** : invoquer `cloturer-brain`. Repassable tant qu'il reste des items dans la file → rien d'oublié.

## Anti-patterns

- Créer la page demandée mais oublier le concept parent ou la réciprocité des alternatives.
- Inventer une catégorie, un tag ou un score (le score n'existe plus en v2).
- Recopier un pitch divergent au lieu de réinjecter le `pitch:` de la cible.
- **Modifier un champ d'une page existante sans dérouler la table des effets de bord** : c'est l'origine mesurée des pitchs périmés du vault (constat C1 de l'audit axe 2).
- Substituer une prose comparative au pitch d'une cible listée en `alternatives:` (clause 3 de la convention unique) — ou omettre le marqueur `voisin :` sur une puce dont la cible n'est pas dans `alternatives:`.
- Clore une mise à jour sur un écart restant de `[V1]`, ou en ayant augmenté le compte de référence.
- Dupliquer une entrée d'expérience datée sur les deux briques d'un incident inter-briques.
- Modifier une fiche du réservoir v1.
- Oublier `uv run AI/scripts/build_index.py` à la fin.
- Clore soi-même au lieu d'invoquer `cloturer-brain` : la régénération, la validation, la vérification de divergence et le commit y sont écrits une seule fois, et c'est ce qui empêche les trois versions divergentes d'autrefois.

## Voir aussi

- `cloturer-brain` — la clôture mécanique, appelée en fin de chaque procédure. **Seul
  endroit du vault où la politique git est écrite.**
- `planifier-projet` — consomme l'index produit par la clôture.
- `AI/design/brain-v2.md` §2, §5, §7.1 — spec de référence.
