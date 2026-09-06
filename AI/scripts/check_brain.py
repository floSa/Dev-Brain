# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_brain.py — valide la cohérence du DevBrain v2 (règles tenues par script).

Contrôle les pages actives v2 (Dev/ + Wiki/ hors réservoir v1). Sort en code != 0
si une règle DURE est violée : c'est le garde-fou qui évite le bazar de la v1.
Le skill enrichir-brain l'exécute en fin de protocole ; le hook Stop le lance en
fin de session (cf. AI/scripts/stop_check_brain.py) ; lançable aussi à la main.

Usage : uv run AI/scripts/check_brain.py

Contrat de conception (AI/audit/rapports/axe-2-integrite.md, annexe B) :
  RAPIDE, HORS LIGNE, DÉTERMINISTE. Un garde-fou lent devient contournable.
  → aucun appel réseau ici. La joignabilité des URLs (R10) est le travail de
    AI/scripts/verifier_fraicheur.py, hors du chemin critique de la session.
  → aucun accrochage en PostToolUse : un état intermédiaire légitime (page créée
    avant sa réciproque) violerait la réciprocité pendant quelques secondes.

Règles DURES (bloquent) :
  - frontmatter conforme au gabarit (champs requis présents, champs hors gabarit absents)
    pour les 4 rôles peuplés du vault : brique, notion, pattern, rule ; un
    `role:` inconnu ou absent est refusé, plus de page sans gabarit            [R3]
  - valeurs d'enum fermées (hosted, scaling, licence_type, maturite)
  - `hosted:` et `scaling:` n'existent QUE si `famille:` ∈ {plateforme, saas,
    application} — une bibliothèque ne s'héberge pas et ne « scale » pas      [R16]
  - famille ∈ énumération fermée de Documentation/general/taxonomie.md (bloc
    ```famille) sur le gabarit brique                                         [R14]
  - tags ⊆ vocabulaire contrôlé (Documentation/general/tags.md)
  - categorie ∈ taxonomie : bloc ```domaine + fences nus. Le vocabulaire de galaxie
    `concept/*` est sorti le 2026-09-05 ; une notion prend un domaine, comme une brique
  - domaines ⊆ vocabulaire de Documentation/general/themes.md                 [R4]
  - alternatives réciproques (si A cite B, B cite A)
  - cible d'alternative absente de l'index → échec explicite, plus de silence  [R12]
  - la section Alternatives (`##` en v2, `###` sous `## Écosystème` en v3) couvre
    toutes les cibles du frontmatter                                           [R11]
  - pitch réinjecté : la puce d'une cible listée en `alternatives:` commence par
    le `pitch:` courant de cette cible (normalisation `**` + espaces)          [R1]
  - aucun lien [[...]] mort, dans le corps ET dans le frontmatter              [R2]
  - `nom:` identique au nom du fichier, sauf caractère illégal en nom de fichier [R9]
  - toute page atteignable depuis un MOC                                       [R7]
  - frontmatter LISIBLE : une page qui ne parse pas est une erreur, jamais une
    absence. Elle était sautée en silence — hors du total, hors de toutes les
    autres règles, liens non résolus (remontée 44 du lot 4)                    [R17]
  - les DIX règles de brain-v3.md §10, durcies au lot 8 après mesure — la
    réciprocité et le pitch des DEUX listes de `## Écosystème`, pas seulement
    d'`alternatives:`                                          [R18, R22]
  - toute brique du dossier apparaît dans le hub du dossier                    [R19]
  - une redirection `Écarter si` vers une brique FICHÉE porte son wikilink
    (§10 règle 5, réécrite : sa forme d'origine était à 26 %)                  [R21]
  - `Mise en œuvre` porte ses cinq étiquettes, et pas d'autres                  [R23]
  - une cible ne se LISTE que dans une section de liste de liens
    (§10 règle 8, réécrite : sa forme d'origine était impossible)              [R24]
  - une brique porte au moins un lien vers une notion ou un hub — DURE depuis
    le lot 8, le passif de 102 fiches ayant été résorbé par le gabarit du
    lot 6 (121 avertissements fermés par construction)                         [R15]
Règles SOUPLES (avertissent) :
  - page trop longue → suggérer une sous-note
  - collisions d'alias : doublon interne, ou alias qui est le `nom:` d'une autre
    page du même rôle — souple, l'unicité globale détruirait des usages
    sémantiques légitimes (`shap`, `yolo`, `map`)                              [R5]
  - couverture des comparatifs `.base` — souple, créer un comparatif est une
    décision éditoriale, pas technique                                     [R8, R8e]
  - voisinage non déclaré : `alternatives:` vide dans un dossier peuplé.
    SOUPLE DÉFINITIVEMENT, par conception : une brique peut légitimement
    n'avoir aucune alternative — la signaler aide, l'interdire mentirait      [R20]
  - étiquette de `## Ressources` hors vocabulaire. Souple tant que l'ouverture
    du vocabulaire à `Site` et `Poids` n'est pas tranchée par floSa           [R23]
  - `## Définition` redit peut-être le bandeau. SOUPLE DÉFINITIVEMENT : la
    règle n'est pas scriptable — `production`, `application`, `open-source`
    sont des mots français ordinaires, et la mesure du lot 8 donne 9 faux
    positifs sur 11. Relecture assistée, pas garde-fou                        [R26]

Les sévérités ci-dessus sont le RÉSULTAT d'une mesure, jamais une intention :
cf. AI/migration/lot-8-durcissement.md, *Journal du lot 8*, qui porte le compte
de violations de chaque règle avant durcissement.
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/check_brain.py")

VAULT = Path(__file__).resolve().parents[2]
# Périmètre de balayage. Avant le lot 3, deux dossiers fixes : `Dev` et `Wiki`.
# Depuis, les pages descendent dans un arbre de DOMAINES à la racine (« Bases de
# données/ », « Machine Learning/ »…), et `Dev/`+`Wiki/` ne portent plus que les
# domaines pas encore migrés. On énumère donc par la NÉGATIVE : tout dossier de la
# racine qui n'est pas de l'outillage est un dossier de pages. Aucune table de
# domaines à tenir à jour, et le jour où `Dev/` et `Wiki/` disparaissent, rien à
# changer ici. Cf. AI/design/brain-v3.md §4 et §11.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}


def scan_dirs() -> list[str]:
    """Dossiers de premier niveau qui portent des pages, triés."""
    return sorted(d.name for d in VAULT.iterdir()
                  if d.is_dir() and d.name not in NON_PAGES)
DOC = VAULT / "Documentation" / "general"
MOC = VAULT / "MOC"

V1_MARKERS = {"maturite", "lecture_min", "auteurs_cles",
              "sous_categories", "score", "mes_projets", "clients_officiels",
              "plateforme", "remplace", "url_officiel", "licence"}

# Champs requis NON VIDES par gabarit. Dérivés des listes de champs constatées
# (audit axe 2, C4) : seuls les champs non vides sur 100 % des pages du type y
# entrent — sinon la règle naîtrait déjà en faute (ex. `remplace_par:`, vide sur
# 293 des 297 services).
REQUIRED = {
    "brique": ["role", "nom", "pitch", "categorie"],
    "notion": ["role", "nom", "categorie", "domaines"],
    "pattern": ["role", "contexte", "services_cles"],
    "rule": ["role", "domaine", "applicable", "strictness"],
    "hub": ["role", "nom", "pitch"],
    "comparatif": ["role", "nom", "categorie"],
}
# Champs EXACTS autorisés par gabarit (spec v3 §5) — tout champ hors liste = non conforme.
# `role: brique` fusionne les anciens gabarits `service` et `outil` : l'audit v2 avait
# démontré qu'ils ne se distinguaient par rien (57 fiches de nature identique réparties
# 34/23 sans discriminant). L'union de leurs champs est donc la liste de la brique —
# `os` et `domaines` viennent d'`outil`, `hosted`, `scaling` et `maturite` de `service`.
BRIQUE_ALLOWED = {"role", "nom", "alias", "pitch", "categorie", "famille", "domaines",
                  "licence_type", "langage", "os", "hosted", "scaling", "maturite",
                  "alternatives", "complements", "tags", "url_docs", "url_repo"}
NOTION_ALLOWED = {"role", "nom", "alias", "categorie", "domaines", "tags"}
# `role: pattern` / `role: rule` — gabarits sans `nom:` ni `categorie:` (la taxonomie
# ne les couvre pas, et c'est délibéré : un pattern enjambe plusieurs domaines, une règle
# est transverse). Leur porte d'entrée est le hub de leur dossier — « Patterns/ » et
# « Rules/ », nés à la clôture du lot 3 de `MOC/Types/` par `git mv`.
PATTERN_ALLOWED = {"role", "tags", "contexte", "services_cles", "projets_appliques"}
RULE_ALLOWED = {"role", "tags", "domaine", "applicable", "strictness"}
# `role: hub` — la page d'un dossier, née au lot 3 avec l'arborescence (spec v3 §9).
# Pas de `categorie:` : un hub ne se range pas, il EST le rangement — son domaine est
# son chemin. Le hub de domaine hérite du frontmatter de la notion chapeau qu'il
# absorbe (`alias`, `domaines`, `tags`), d'où ces trois champs facultatifs.
HUB_ALLOWED = {"role", "nom", "alias", "pitch", "domaines", "tags"}
# `role: comparatif` — né au lot 5 (spec v3 §8), quand les `.base` deviennent des
# pages. Un `.base` est un fichier YAML de requête : ni frontmatter, ni corps, donc
# ni couleur dans le graphe ni lien sortant — 44 comparatifs sur 47 étaient cités,
# aucun ne citait. La page porte le rôle, la couleur et les liens ; le `.base` reste
# à côté comme moteur de tableau, embarqué par un lien d'embed avec extension.
# Quatre champs, ceux du gabarit de `AI/migration/lot-5-comparatifs.md`, et pas un de
# plus : un comparatif ne se déploie pas (ni `famille:`, ni `licence_type:`) et son
# `pitch:` est la ligne « On tranche sur : … » du corps, qui n'a pas à être indexée.
COMPARATIF_ALLOWED = {"role", "nom", "categorie", "tags"}
ALLOWED = {"brique": BRIQUE_ALLOWED, "notion": NOTION_ALLOWED,
           "pattern": PATTERN_ALLOWED, "rule": RULE_ALLOWED, "hub": HUB_ALLOWED,
           "comparatif": COMPARATIF_ALLOWED}
# Valeurs autorisées (listes fermées) pour les champs de brique à enum.
# `hosted` est une LISTE depuis la v3 : `both` ne disait rien qu'une énumération ne
# dise mieux, et une brique peut être self-hébergeable ET managée sans que ce soit
# une troisième valeur à part.
VALUE_ENUMS = {
    "scaling": {"single-node", "distributed", "serverless"},
    "licence_type": {"open-source", "source-available", "proprietary", "open-core"},
    "maturite": {"production", "beta", "experimental", "deprecated"},
}
LIST_ENUMS = {"hosted": {"self", "managed"}}
# R16 — les seules familles pour lesquelles l'hébergement et le scaling ont un sens.
# Mesure v2 : 177 fiches `famille: paquet` portaient une valeur d'hébergement, et
# `scaling: single-node` sur 212 fiches n'était que la valeur par défaut de tout ce
# qui n'est pas distribué. Deux champs qui décrivent 100 % des fiches ne discriminent rien.
FAMILLES_HEBERGEES = {"plateforme", "saas", "application"}
SIZE_WARN = {"brique": 90, "notion": 200}
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
RE_ROLE_HUB = re.compile(r"^role: hub\s*$", re.M)
# La section des alternatives s'écrit `## Alternatives` en v2 et `### Alternatives`
# sous `## Écosystème` en v3 (spec §6). Le lot 6 convertit les 337 fiches dossier par
# dossier, en dix-sept conversations parallèles : les deux formes coexistent dans le
# vault pendant toute la durée du lot, et le validateur doit rester vert des deux côtés
# — sans quoi la première conversation qui convertit casse la branche des seize autres.
# Le niveau de titre est donc élargi, et la borne de fin avec lui : une section `###`
# s'arrête au `###` suivant (`Compléments`), pas au prochain `##`.
ALT_SECTION_RE = re.compile(r"\n#{2,3} Alternatives\n(.*?)(?=\n#{2,3} |\Z)", re.S)
ALT_BULLET_RE = re.compile(r"\s*-\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]\s*[—-]\s*(.+)")
# Caractères interdits dans un nom de fichier (Windows compris) : un `nom:` qui en
# porte un ne PEUT pas être le nom de son fichier — exemption de R9.
FS_ILLEGAL = set('/\\:*?"<>|')
# Seuil R8a : au-dessous, une catégorie n'a pas assez de membres pour qu'un
# comparatif ait un sens.
BASE_MIN_CAT = 3
BASE_MIN_MEMBRES = 2

# ============================ LOT 8 — les règles §10 ============================
# Ce bloc porte les règles de `brain-v3.md` §10 qui n'étaient pas encore écrites.
# Chaque sévérité est le RÉSULTAT d'une mesure faite le 2026-09-06 sur les 337
# briques, pas une intention : une règle passe en dure quand le vault est à zéro,
# et reste en avertissement AVEC UN MOTIF ÉCRIT sinon. On ne durcit jamais en
# ajoutant une exception. Cf. AI/migration/lot-8-durcissement.md, *Journal du lot 8*.

# La section `## Écosystème` porte deux listes symétriques. Les traiter par une
# TABLE et non par deux blocs de code est le correctif de fond du lot 8 : R1 et R11
# ne regardaient qu'`alternatives:`, et c'est ce qui a laissé la réciprocité de
# `complements:` sans aucun contrôle, puis douze moitiés orphelines pendant tout
# le lot 6 — un couple non réciproque ne se voit pas en relisant une seule page.
CHAMPS_ECOSYSTEME = (
    # champ, titre de section, code R réciprocité, code R couverture, code R pitch
    ("alternatives", "Alternatives", "R12", "R11", "R1"),
    ("complements",  "Compléments",  "R18", "R22", "R22"),
)
# R24 — les sections qui sont des LISTES DE LIENS. La règle 8 (« pas de double
# citation ») ne peut porter que sur celles-là : la prose de `## Définition` et les
# cellules du tableau de décision citent librement, et le DOIVENT — c'est la règle 2
# du lot 6 qui garde une redirection en `Écarter si` faute de comparatif d'accueil.
# Mesure : 242 violations en lisant « toutes sections », 0 en lisant « listes de
# liens ». C'est la lecture qui restitue le défaut d'origine (sur la page Faker,
# Mimesis apparaissait en `Alternatives` ET en `Liens`, deux listes de liens).
SECTIONS_LIENS = ("Alternatives", "Compléments", "Voir aussi")
# R23 — vocabulaires fermés des deux sections étiquetées (§10, règle 7).
RES_LABELS = {"Documentation", "Dépôt", "Tutoriel", "Article", "Papier", "Cours", "Vidéo"}
MEO_LABELS = {"Installation", "Point d'entrée", "Prérequis", "Exécution", "Coût"}
RE_TITRE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
RE_PUCE_ETIQ = re.compile(r"^\s*-\s+(.+?)\s+—\s")
# Liens d'ENTRÉE d'une puce : ce avec quoi la puce COMMENCE, éventuellement plusieurs
# enchaînés par `·`. C'est la définition de « listé » — un lien cité au milieu d'une
# phrase n'est pas une entrée de liste. Sans cette distinction, R24 punirait la forme
# que le lot 6 recommande pour une section Alternatives vide (« Aucune outillée dans
# le brain : l'approche concurrente est [[Diff-in-Diff]] » — CausalImpact.md).
RE_PUCE_ENTREE = re.compile(r"^\s*-\s*((?:\[\[[^\]]+\]\]\s*(?:·|,|/)?\s*)+)")
RE_LIEN_PAIRE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
# R21 — la flèche est le marqueur de redirection du vault : 345 des 1 388 cellules
# `Écarter si` en portent une, et c'est exactement là que se joue la règle 5.
RE_FLECHE = re.compile(r"→|->")
# R26 — motifs BORNÉS des valeurs rendues du bandeau. `production` est absent, et
# c'est délibéré : c'est un mot français ordinaire (« pensé dès l'origine pour le
# passage en production »). La mesure du lot 8 montre que `open-source`,
# `application`, `annuaire` et `extension` le sont tout autant — d'où le maintien
# de la règle 10 en avertissement, motif écrit à sa place dans le code.
MOT_LICENCE = {
    "open-source": r"\bopen[- ]source\b",
    "source-available": r"\bsource[- ]available\b",
    "proprietary": r"\b(?:propri[ée]taire|proprietary)\b",
    "open-core": r"\bopen[- ]core\b",
}
MOT_MATURITE = {
    "beta": r"\b(?:en )?b[êe]ta\b",
    "experimental": r"\bexp[ée]rimental(?:e|es)?\b",
    "deprecated": r"\b(?:d[ée]pr[ée]ci[ée]e?|deprecated)\b",
}


def hors_vault(p, racine) -> bool:
    """Le chemin est-il hors du perimetre logique du vault ?

    Les worktrees git vivent sous `.claude/worktrees/` et sont des copies completes :
    les balayer double tout. Le test porte sur le chemin RELATIF a la racine — un
    vault qui vit lui-meme sous `.claude/` (cas d'un worktree) reste entierement
    valide, seul son propre `.claude/` interne est ecarte.
    """
    try:
        parts = p.relative_to(racine).parts
    except ValueError:
        return True
    return bool(parts) and parts[0] in {".git", ".claude"}


def parse(text: str) -> tuple[dict | None, str, str | None]:
    """(frontmatter, corps, motif d'illisibilité). `fm` et `motif` s'excluent.

    **Le motif est retourné, jamais avalé** — correctif de la remontée 44 du lot 4.
    Cette fonction renvoyait `None` dans les quatre cas ci-dessous sans les
    distinguer, et `main()` sautait la page : elle sortait du total annoncé, aucune
    de ses seize règles n'était évaluée, ses wikilinks n'étaient pas résolus. Un
    `pitch:` non quoté contenant « : » suffisait à l'y faire entrer, et sur une
    brique ou une notion **rien** ne l'aurait signalé — le vault restait vert.
    Une page qui ne parse pas est une erreur, jamais une absence.
    """
    if not text.startswith("---"):
        return None, text, "aucun frontmatter (le fichier ne commence pas par `---`)"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text, "frontmatter non refermé (pas de second `---`)"
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        detail = str(e).splitlines()[0].strip()
        return None, parts[2], (f"YAML invalide — {detail}. Cause la plus fréquente : "
                                f"une valeur non quotée contenant « : » (`pitch:`, `nom:`)")
    if not isinstance(fm, dict):
        return None, parts[2], (f"frontmatter lu comme {type(fm).__name__}, pas comme "
                                f"un dictionnaire de champs")
    return fm, parts[2], None


def rel(p: Path) -> str:
    return p.relative_to(VAULT).as_posix()


def is_active_v2(scan_dir: str, fm: dict) -> bool:
    """Le réservoir v1 ne vit que sous `Wiki/` (même correctif que build_index)."""
    if scan_dir != "Wiki":
        return True
    return not (V1_MARKERS & set(fm.keys()))


def load_tag_vocab() -> set[str]:
    txt = (DOC / "tags.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", txt, re.M))


def load_theme_vocab() -> set[str]:
    """Vocabulaire fermé de `domaines:` — colonne 1 des tableaux de themes.md (R4)."""
    txt = (DOC / "themes.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*`([a-z0-9-]+)`", txt, re.M))


def _fences(nom_fichier: str) -> list[tuple[str, str]]:
    """Blocs de code d'un document de gouvernance, en (langue, contenu).

    La langue du fence sépare les vocabulaires : ```famille porte l'axe famille,
    un fence nu porte les catégories. Sans cette distinction, `load_categories`
    avalerait les 9 valeurs de famille et `categorie: paquet` deviendrait valide.
    """
    txt = (DOC / nom_fichier).read_text(encoding="utf-8")
    return re.findall(r"^```([a-z0-9-]*)\n(.*?)^```", txt, re.S | re.M)


def load_familles() -> set[str]:
    """Énumération fermée de `famille:` — bloc ```famille de taxonomie.md (R14)."""
    fam: set[str] = set()
    for langue, corps in _fences("taxonomie.md"):
        if langue == "famille":
            fam.update(tok for tok in re.findall(r"^[a-z][\w-]*$", corps, re.M))
    return fam


def load_categories() -> set[str]:
    """Vocabulaire fermé de `categorie:` — le DOMAINE.

    Deux sources, une par rôle :
      - bloc ```domaine — les 94 domaines des briques (Documentation/general/taxonomie.md) ;
      - fences nus — les vocabulaires des notions, `concept/*` et `skill/*`.
    L'ancien vocabulaire à 74 valeurs (`ml/framework`, `tooling/*`, `auth`…) a
    été retiré de taxonomie.md : il échoue désormais en dur. Aucune valeur legacy
    n'est codée ici — le vocabulaire vit dans le document de gouvernance, pas dans
    le script, et se ferme en retirant un bloc de code.
    """
    body = "\n".join(c for langue, c in _fences("taxonomie.md")
                     if not langue or langue == "domaine")
    cats: set[str] = set()
    # groupes prefix/{a, b, c} (peuvent s'étaler sur plusieurs lignes)
    for m in re.finditer(r"([a-z][\w-]*)/\{([^}]*)\}", body, re.S):
        for item in re.split(r"[,\n]", m.group(2)):
            item = item.strip()
            if item:
                cats.add(f"{m.group(1)}/{item}")
    # tokens nus restants (une valeur sans accolades, sur sa propre ligne)
    body2 = re.sub(r"[a-z][\w-]*/\{[^}]*\}", "", body, flags=re.S)
    for tok in re.findall(r"^[a-z][\w-]*(?:/[a-z][\w-]*)?$", body2, re.M):
        cats.add(tok.strip())
    return cats


def resolvable_names() -> set[str]:
    """Noms de fichiers (md + base) du vault, minuscules, pour résoudre [[liens]].

    Deux clés par fichier : le stem (`[[Postgres]]`, la convention nue du vault) ET
    le nom complet avec extension. La seconde naît au lot 5 : une page de comparatif
    embarque sa vue par un lien portant `.base`, seule syntaxe qui vise un fichier
    non-`.md`, et le stem seul faisait déclarer ce lien MORT. Porter les deux clés
    garde le test exact — un lien vers `Foo.base` ne résout que si `Foo.base` existe,
    jamais par repli sur un `Foo.md` de même stem.
    """
    names: set[str] = set()
    for ext in ("*.md", "*.base"):
        for p in VAULT.rglob(ext):
            if hors_vault(p, VAULT):
                continue
            names.add(p.stem.lower())
            names.add(p.name.lower())
    return names


def link_target_ok(tgt: str, names: set[str]) -> bool:
    tgt = tgt.strip()
    if "/" in tgt:  # lien qualifié par chemin
        return (VAULT / (tgt + ".md")).exists() or (VAULT / (tgt + ".base")).exists()
    return tgt.lower() in names


def alt_names(fm: dict) -> set[str]:
    out = set()
    for a in fm.get("alternatives") or []:
        m = re.search(r"\|([^\]]+)\]\]", a) or re.search(r"\[\[([^\]]+)\]\]", a)
        out.add((m.group(1) if m else a).split("/")[-1])
    return out


def fm_links(fm: dict) -> list[tuple[str, str]]:
    """Wikilinks portés par le FRONTMATTER (alternatives:, remplace_par:…) — R2.

    `check_brain` ne lisait que le corps : un renommage ou une suppression laissait
    un lien mort en frontmatter sans que rien ne le dise (796 liens concernés).
    """
    out: list[tuple[str, str]] = []
    for key, val in fm.items():
        for item in (val if isinstance(val, list) else [val]):
            if isinstance(item, str):
                out.extend((key, t) for t in LINK_RE.findall(item))
    return out


def alt_section(body: str) -> str | None:
    m = ALT_SECTION_RE.search(body)
    return m.group(1) if m else None


def norm_pitch(s: str) -> str:
    """Normalisation de comparaison des pitchs (R1) : gras et espaces seulement."""
    return re.sub(r"\s+", " ", re.sub(r"\*\*", "", s or "")).strip().rstrip(".")


def sections(body: str) -> dict[str, str]:
    """{titre : contenu} pour tous les `##` et `###` du corps.

    Un seul niveau de dictionnaire, sans hiérarchie : les titres du gabarit v3 sont
    uniques sur une fiche, et une section `###` s'arrête au titre suivant quel que
    soit son niveau. Sert R21, R22, R23, R24 et R26.
    """
    out: dict[str, str] = {}
    cur: str | None = None
    buf: list[str] = []
    for ligne in body.splitlines():
        m = RE_TITRE.match(ligne)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(2), []
        elif cur is not None:
            buf.append(ligne)
    if cur is not None:
        out[cur] = "\n".join(buf)
    return out


def ecarter_cells(body: str) -> list[str]:
    """Cellules de la colonne « Écarter si » du tableau de décision (R21)."""
    sec = sections(body).get("Prendre si / Écarter si")
    if sec is None:
        return []
    out: list[str] = []
    for ligne in sec.splitlines():
        ligne = ligne.strip()
        if not ligne.startswith("|"):
            continue
        cols = [c.strip() for c in ligne.strip("|").split("|")]
        if len(cols) < 2:
            continue
        if re.fullmatch(r":?-{2,}:?", cols[0]):        # ligne de séparation
            continue
        if cols[0].lower().startswith("prendre si"):   # en-tête
            continue
        if cols[1]:
            out.append(cols[1])
    return out


def entrees_puces(sec: str | None) -> list[str]:
    """Cibles LISTÉES par une section de liste de liens (R24)."""
    out: list[str] = []
    for ligne in (sec or "").splitlines():
        m = RE_PUCE_ENTREE.match(ligne)
        if not m:
            continue
        for a, b in RE_LIEN_PAIRE.findall(m.group(1)):
            out.append((b or a).split("/")[-1].strip())
    return out


def etiquettes(sec: str | None) -> list[str]:
    """Étiquettes des puces `- <Étiquette> — …` d'une section (R23).

    Une puce sans étiquette est rendue telle quelle, préfixée, pour que le message
    montre la ligne fautive au lieu de la taire.
    """
    out: list[str] = []
    for ligne in (sec or "").splitlines():
        m = RE_PUCE_ETIQ.match(ligne)
        if m:
            out.append(m.group(1).strip().replace("**", ""))
        elif ligne.strip().startswith("- "):
            out.append("(sans étiquette) " + ligne.strip()[2:][:60])
    return out


def index_briques(active: list[tuple[str, dict, str]]) -> dict[str, str]:
    """{nom ou alias en minuscules : `nom:` canonique} des `role: brique` (R21).

    Les alias de moins de trois caractères sont écartés : ils produisent des
    correspondances de hasard dans de la prose française. R5 signale par ailleurs
    les collisions d'alias légitimes (`map`, `shap`, `yolo`).
    """
    idx: dict[str, str] = {}
    for _, fm, _ in active:
        if fm.get("role") != "brique" or not fm.get("nom"):
            continue
        nom = str(fm["nom"])
        idx[nom.lower()] = nom
        for a in fm.get("alias") or []:
            if len(str(a)) >= 3:
                idx.setdefault(str(a).lower(), nom)
    return idx


def cible_frontmatter(fm: dict, champ: str) -> set[str]:
    """Cibles d'un champ de liste de liens du frontmatter (`alternatives`, `complements`)."""
    out: set[str] = set()
    for a in fm.get(champ) or []:
        m = re.search(r"\|([^\]]+)\]\]", a) or re.search(r"\[\[([^\]]+)\]\]", a)
        out.add((m.group(1) if m else a).split("/")[-1])
    return out


def hub_du_dossier(path: str) -> str:
    """Chemin du `role: hub` qui porte le dossier d'une page (R19).

    C'est la convention de la v3 : « tout dossier porte une page à son nom ». Le hub
    de `Bases de données/Vectoriel/` est `Bases de données/Vectoriel/Vectoriel.md`.
    """
    dossier = path.rsplit("/", 1)[0]
    return f"{dossier}/{dossier.rsplit('/', 1)[-1]}.md"


def pages_aiguillage() -> list[Path]:
    """Les pages qui servent de porte d'entrée : `MOC/`, les `role: hub`, `Home.md`.

    Le lot 3 remplace `MOC/` par les pages hub, domaine par domaine — les deux
    coexistent tant que les 20 domaines ne sont pas migrés. `Home.md` compte aussi :
    c'est lui qui cite les hubs de domaine, lesquels n'ont pas de parent.
    """
    out: list[Path] = list(MOC.rglob("*.md")) if MOC.exists() else []
    if (VAULT / "Home.md").exists():
        out.append(VAULT / "Home.md")
    for d in scan_dirs():
        for md in (VAULT / d).rglob("*.md"):
            tete = md.read_text(encoding="utf-8")[:400]
            if RE_ROLE_HUB.search(tete):
                out.append(md)
    return out


def moc_targets() -> tuple[set[str], set[str]]:
    """Cibles citées par les pages d'aiguillage — (chemins qualifiés, noms nus) (R7)."""
    qualifies: set[str] = set()
    nus: set[str] = set()
    for md in pages_aiguillage():
        for tgt in LINK_RE.findall(md.read_text(encoding="utf-8")):
            tgt = tgt.strip().split("#")[0]
            (qualifies if "/" in tgt else nus).add(tgt.lower())
    return qualifies, nus


# ---------------------------------------------------------------- R8 : comparatifs
STR = r'"([^"]*)"'


def base_match(expr, path: str, fm: dict) -> bool | None:
    """Évalue une clause de filtre `.base` sur une page. None = forme non reconnue.

    Couvre les seules formes employées par les 47 comparatifs du vault ; toute
    forme nouvelle rend le `.base` non évaluable et se signale comme telle,
    plutôt que de produire un décompte faux.
    """
    if isinstance(expr, dict):
        for op, agg in (("and", all), ("or", any)):
            if op in expr:
                res = [base_match(e, path, fm) for e in expr[op]]
                return None if None in res else agg(res)
        if "not" in expr:
            r = base_match(expr["not"], path, fm)
            return None if r is None else not r
        return None
    s = str(expr).strip()
    m = re.fullmatch(rf"file\.path\.startsWith\({STR}\)", s)
    if m:
        return path.startswith(m.group(1))
    m = re.fullmatch(rf"file\.name\s*==\s*{STR}", s)
    if m:
        return Path(path).stem == m.group(1)
    m = re.fullmatch(rf"(?:file\.hasTag|tags\.contains)\({STR}\)", s)
    if m:
        return m.group(1) in (fm.get("tags") or [])
    m = re.fullmatch(rf"([a-z_]+)\.startsWith\({STR}\)", s)
    if m:
        return str(fm.get(m.group(1)) or "").startswith(m.group(2))
    m = re.fullmatch(rf"([a-z_]+)\s*(==|!=)\s*(?:{STR}|null)", s)
    if m:
        champ, op, val = m.group(1), m.group(2), m.group(3)
        cur = fm.get(champ)
        egal = (cur in (None, "", [], {})) if val is None else (cur == val)
        return egal if op == "==" else not egal
    return None


def check_bases(active: list[tuple[str, dict, str]], cited: set[str]) -> list[str]:
    """R8 (souple) : couverture et santé des comparatifs `.base`.

    (a) catégorie Dev à 3+ pages couverte par un `.base` · (b) `.base` à 2 membres
    minimum · (c) `.base` cité par au moins une page · (d) aucun filtre par liste
    de noms codée en dur.
    """
    warn: list[str] = []
    membres: dict[str, list[str] | None] = {}
    for base in sorted(VAULT.rglob("*.base")):
        if hors_vault(base, VAULT):
            continue
        nom = rel(base)
        txt = base.read_text(encoding="utf-8")
        try:
            doc = yaml.safe_load(txt) or {}
        except yaml.YAMLError:
            warn.append(f"R8 — {nom} : YAML illisible")
            continue
        # (d) liste de noms codée en dur dans le filtre de base (pas des vues)
        durs = len(re.findall(r'file\.name\s*==\s*"', txt.split("views:")[0]))
        if durs >= 2:
            warn.append(f"R8d — {nom} : filtre par liste de {durs} noms codée en dur "
                        "(une page qui entre dans le thème n'entrera jamais dans la vue)")
        filt = doc.get("filters")
        if filt is None:
            warn.append(f"R8 — {nom} : aucun bloc `filters:` — membres indéterminables")
            membres[nom] = None
            continue
        sel: list[str] | None = []
        for path, fm, _ in active:
            r = base_match(filt, path, fm)
            if r is None:
                warn.append(f"R8 — {nom} : filtre non évaluable hors ligne — non compté")
                sel = None
                break
            if r:
                sel.append(path)
        membres[nom] = sel
        if sel is not None and len(sel) < BASE_MIN_MEMBRES:
            warn.append(f"R8b — {nom} : {len(sel)} membre(s) (< {BASE_MIN_MEMBRES}) "
                        "— comparatif sans comparaison")
        # (c) cité par au moins une page
        if base.stem.lower() not in cited:
            warn.append(f"R8c — {nom} : cité par aucune page de Dev/ ou Wiki/")

    # (a) catégorie Dev à 3+ pages sans comparatif qui en réunisse au moins 2 membres
    fm_par_path = {path: fm for path, fm, _ in active}
    compte = collections.Counter(
        fm.get("categorie") for _, fm, _ in active
        if fm.get("role") == "brique" and fm.get("categorie"))
    for cat, n in sorted(compte.items()):
        if n < BASE_MIN_CAT:
            continue
        couverte = any(
            sel is not None
            and sum(1 for p in sel if fm_par_path[p].get("categorie") == cat) >= BASE_MIN_MEMBRES
            for sel in membres.values())
        if not couverte:
            warn.append(f"R8a — categorie `{cat}` : {n} briques, aucun comparatif `.base` "
                        "ne les réunit")

    # (e) L'ANGLE MORT DE R8a, comblé au lot 8. R8a vérifie qu'une CATÉGORIE a un
    # comparatif ; elle ne vérifie pas que ses BRIQUES y entrent. Une vue filtre par
    # tag ou par liste de noms, et laisse dehors des briques de son propre dossier —
    # deux lots l'ont trouvé à la main, chacun croyant à un cas isolé : `ml/tabulaire`
    # (Featuretools, category_encoders, imbalanced-learn hors du `file.hasTag("boosting")`
    # de leur vue) et `ml/vision` (Kornia, timm, torchvision hors du filtre
    # `object-detection or segmentation`).
    #
    # Décompte du 2026-09-06, sur les 47 vues et les 337 briques :
    #   89 briques ne sont membres d'AUCUNE vue (26 %) ;
    #   51 d'entre elles relèvent des 13 catégories que R8a signale déjà ;
    #   38 sont INVISIBLES à R8a, sur 28 catégories.
    # Ces 38 ne sont pas un bloc homogène, et c'est ce que le lot 8 ajoute à la
    # mesure du lot 6 : 27 vivent dans une catégorie de 1 ou 2 briques, où aucun
    # comparatif n'a de sens (les seuils sont à 3 et 2) — les signaler produirait 27
    # avertissements irréparables. Les 11 autres sont le vrai défaut : une vue existe
    # pour leur catégorie, elle retient leurs pairs, et son filtre les a laissées
    # dehors. C'est cette formulation-là que R8e porte — la plus étroite qui attrape
    # les deux groupes trouvés à la main, et la seule qui soit réparable (élargir un
    # filtre). SOUPLE, comme toute la famille R8 : un comparatif est une décision
    # éditoriale, pas technique.
    retenues: set[str] = set()
    for sel in membres.values():
        if sel:
            retenues |= set(sel)
    cat_vue: set[str] = {fm_par_path[p].get("categorie") for p in retenues
                         if fm_par_path[p].get("role") == "brique"}
    for path, fm, _ in active:
        if fm.get("role") != "brique" or path in retenues:
            continue
        if fm.get("categorie") in cat_vue:
            warn.append(f"R8e — {path} : hors de toutes les vues, alors qu'une vue "
                        f"retient d'autres briques de `{fm.get('categorie')}` "
                        "— le filtre du comparatif l'a laissée dehors")
    return warn


def check_alias(active: list[tuple[str, dict, str]]) -> tuple[list[str], list[str]]:
    """R5 (souple) et R15 (DURE depuis le lot 8). Rend (avertissements, violations).

    R5 reste souple par décision d'audit — l'unicité globale des alias détruirait
    des usages sémantiques légitimes (`shap`, `yolo`, `map`).
    """
    warn: list[str] = []
    dur: list[str] = []
    noms: dict[tuple, str] = {}
    for path, fm, _ in active:
        if fm.get("nom"):
            noms[(fm.get("role"), str(fm["nom"]).lower())] = path
    for path, fm, _ in active:
        bas = [str(a).lower() for a in (fm.get("alias") or [])]
        dup = sorted({a for a in bas if bas.count(a) > 1})
        if dup:
            warn.append(f"R5 — {path} : alias en doublon interne {dup}")
        for a in sorted(set(bas)):
            proprio = noms.get((fm.get("role"), a))
            if proprio and proprio != path:
                warn.append(f"R5 — {path} : alias `{a}` est le `nom:` de `{proprio}` "
                            "(même rôle)")

    # R15 — une `role: brique` doit porter au moins un lien vers une notion ou un hub.
    # Le couple Dev<->Wiki est imposé par le skill enrichir-brain (étape 6) mais rien ne
    # le vérifiait : `check_brain` contrôle qu'un lien n'est pas mort, jamais qu'il existe.
    # SOUPLE, et elle doit le rester tant que le passif n'est pas résorbé : 102 fiches
    # service sur 297 ne portaient aucun lien vers un concept (cf. axe 3, constat C2), et
    # le lot 2 étend la règle aux 39 ex-`outil` devenus briques — le passif grossit avant
    # de se résorber, c'est le prix de la fusion des deux gabarits.
    # La cible attendue est une page à comprendre : `notion`, ou `hub` — le hub de
    # domaine ABSORBE la notion chapeau homonyme à l'étape 4 du lot 3, c'est la même
    # page. Le test lisait `Wiki/Concepts/*`, un chemin que le lot 3 vide.
    concepts = {Path(p).stem.lower() for p, f, _ in active
                if f.get("role") in {"notion", "hub"}}
    for path, fm, body in active:
        if fm.get("role") != "brique":
            continue
        cibles = {t.split("|")[0].split("/")[-1].strip().lower()
                  for t in LINK_RE.findall(body)}
        if not (cibles & concepts):
            dur.append(f"R15 — {path}: aucun lien vers une notion ou un hub "
                       "(`## Voir aussi` est le domicile de ce lien)")
    return warn, dur


def main() -> int:
    vocab = load_tag_vocab()
    themes = load_theme_vocab()
    cats = load_categories()
    familles = load_familles()
    if not familles:
        return print("taxonomie.md : bloc ```famille introuvable ou vide") or 1
    names = resolvable_names()
    moc_q, moc_n = moc_targets()

    active: list[tuple[str, dict, str]] = []  # (path, frontmatter, body)
    illisibles: list[str] = []                # R17 — pages qui ne parsent pas
    for d in scan_dirs():
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm, body, motif = parse(md.read_text(encoding="utf-8"))
            if fm is None:
                illisibles.append(f"R17 — {rel(md)}: frontmatter illisible — {motif}")
                continue
            if not is_active_v2(d, fm):
                continue
            active.append((rel(md), fm, body))

    by_name = {fm.get("nom"): fm for _, fm, _ in active}
    pitches = {fm.get("nom"): (fm.get("pitch") or "")
               for _, fm, _ in active if fm.get("nom")}
    cited_bases: set[str] = set()
    hard: list[str] = list(illisibles)
    warn: list[str] = []
    # --- LOT 8 : les trois index que les nouvelles règles consomment. Calculés
    # UNE fois, hors de la boucle : R21 confronte chaque cellule `Écarter si` aux
    # 337 noms et alias du vault, ce qui serait quadratique sinon.
    # R19 — {chemin du hub : cibles de ses wikilinks}
    hubs_cibles: dict[str, set[str]] = {
        p: {(b or a).split("/")[-1].strip()
            for a, b in RE_LIEN_PAIRE.findall(bd)}
        for p, f, bd in active if f.get("role") == "hub"}
    # R20 — {dossier : nombre de briques qu'il porte}
    briques_par_dossier: dict[str, int] = collections.Counter(
        p.rsplit("/", 1)[0] for p, f, _ in active if f.get("role") == "brique")
    # R21 — {nom ou alias : nom canonique}
    idx_briques = index_briques(active)

    for path, fm, body in active:
        typ = fm.get("role")
        nom = fm.get("nom") or path
        stem = Path(path).stem

        # 1. frontmatter conforme au gabarit (champs requis + aucun champ hors gabarit §5)
        for req in REQUIRED.get(typ, []):
            if not fm.get(req):
                hard.append(f"{path}: champ requis manquant `{req}`")
        if typ in ALLOWED:
            extra = set(fm.keys()) - ALLOWED[typ]
            if extra:
                hard.append(f"{path}: champ(s) hors gabarit §5 {sorted(extra)}")
        else:
            hard.append(f"R3 — {path}: `role: {typ or '(absent)'}` sans gabarit déclaré "
                        f"(connus : {sorted(ALLOWED)})")

        # 1b. valeurs d'enum : champs à liste fermée (scaling, licence_type, maturite)
        for field, vals in VALUE_ENUMS.items():
            v = fm.get(field)
            if v is not None and v not in vals:
                hard.append(f"{path}: `{field}: {v}` hors valeurs autorisées {sorted(vals)}")
        # 1b bis. enums portées par une LISTE (hosted) — chaque élément est contrôlé,
        # et une valeur scalaire est refusée : le champ a changé de forme en v3.
        for field, vals in LIST_ENUMS.items():
            v = fm.get(field)
            if v is None:
                continue
            if not isinstance(v, list):
                hard.append(f"{path}: `{field}: {v}` doit être une liste (v3), pas un scalaire")
                continue
            for item in v:
                if item not in vals:
                    hard.append(f"{path}: `{field}` contient `{item}`, hors valeurs "
                                f"autorisées {sorted(vals)}")

        # 1b ter. R16 — `hosted:` et `scaling:` sont conditionnels à `famille:`.
        for field in ("hosted", "scaling"):
            if field in fm and fm.get("famille") not in FAMILLES_HEBERGEES:
                hard.append(f"R16 — {path}: `{field}:` sur `famille: {fm.get('famille')}` "
                            f"— le champ n'existe que pour {sorted(FAMILLES_HEBERGEES)}")

        # 1c. R9 — `nom:` identique au nom du fichier. Exemption : un `nom:` portant
        # un caractère illégal en nom de fichier NE PEUT PAS l'être (« A/B testing »).
        if fm.get("nom") and not (FS_ILLEGAL & set(str(fm["nom"]))) and str(fm["nom"]) != stem:
            hard.append(f"R9 — {path}: `nom: {fm['nom']}` != nom de fichier `{stem}`")

        # 2. tags ⊆ vocabulaire
        for t in fm.get("tags") or []:
            if t not in vocab:
                hard.append(f"{path}: tag hors vocabulaire `{t}` (cf. tags.md)")

        # 3. categorie ∈ taxonomie
        cat = fm.get("categorie")
        if cat and cat not in cats:
            hard.append(f"{path}: categorie hors taxonomie `{cat}`")

        # 3a. R14 — famille ∈ énumération fermée (taxonomie.md). Un champ vide
        #     (fiche laissée en suspens, arbre non concluant) passe : c'est le signal
        #     assumé « à trancher », pas une valeur inventée.
        fam = fm.get("famille")
        if fam is not None and fam not in familles:
            hard.append(f"R14 — {path}: `famille: {fam}` hors énumération fermée "
                        f"{sorted(familles)} (cf. taxonomie.md, bloc ```famille)")

        # 3b. R4 — domaines ⊆ vocabulaire de themes.md
        for dom in fm.get("domaines") or []:
            if dom not in themes:
                hard.append(f"R4 — {path}: domaine hors themes.md `{dom}` "
                            f"(vocabulaire : {sorted(themes)})")

        # 4. Les deux listes de `## Écosystème`, par TABLE et non par deux blocs.
        #    Avant le lot 8, ce bloc ne connaissait qu'`alternatives:` : R12, la
        #    réciprocité, R11 et R1 s'arrêtaient là. `complements:` était déclaré au
        #    frontmatter, rendu dans la page, indexé — et contrôlé par rien. C'est ce
        #    qui a laissé douze moitiés orphelines pendant tout le lot 6, un couple
        #    non réciproque ne se voyant pas en relisant une seule page. Traiter les
        #    deux champs par la même boucle rend l'oubli impossible plutôt
        #    qu'improbable, ce qui est l'énoncé même du §10.
        #
        #    R12 / R18 — la cible existe dans l'index ;
        #    réciprocité — si A cite B, B cite A, dans le MÊME champ ;
        #    R11 / R22   — la section couvre toutes les cibles du frontmatter ;
        #    R1  / R22   — la puce commence par le `pitch:` courant de sa cible.
        #    Mesure du 2026-09-06 : 0 sur `alternatives:` (154 demi-arêtes) ; sur
        #    `complements:`, 0 en réciprocité et 2 en pitch, réparées avant
        #    durcissement (le couple fastmcp <-> mcpjam tronquait le pitch de sa
        #    cible au premier tiret).
        for champ, titre, code_recip, code_couv, code_pitch in CHAMPS_ECOSYSTEME:
            cibles = cible_frontmatter(fm, champ)
            for b in cibles:
                if b not in by_name:
                    hard.append(f"{code_recip} — {path}: {champ} `{b}` absent de "
                                "l'index (page inexistante, renommée ou hors périmètre)")
                elif nom not in cible_frontmatter(by_name[b], champ):
                    hard.append(f"{code_recip} — {path}: {champ} `{b}` non réciproque "
                                f"(manque `{nom}` dans son `{champ}:`)")
            if not cibles:
                continue
            sec = sections(body).get(titre) or ""
            en_section = {(b or a).split("/")[-1]
                          for a, b in RE_LIEN_PAIRE.findall(sec)}
            manquants = sorted(cibles - en_section)
            if manquants:
                hard.append(f"{code_couv} — {path}: cible(s) du frontmatter absente(s) "
                            f"de la section `{titre}` {manquants}")
            for line in sec.splitlines():
                m = ALT_BULLET_RE.match(line)
                if not m:
                    continue
                cible = (m.group(2) or m.group(1)).split("/")[-1]
                if cible not in cibles:
                    continue  # puce hors du champ — exemptée
                attendu = norm_pitch(pitches.get(cible, ""))
                if attendu and not norm_pitch(m.group(3)).startswith(attendu):
                    hard.append(f"{code_pitch} — {path}: la puce de `{cible}` en "
                                f"`{titre}` ne commence pas par son pitch courant "
                                f"« {attendu} »")

        # 5. liens morts — corps (historique) ET frontmatter (R2)
        for tgt in LINK_RE.findall(body):
            if not link_target_ok(tgt, names):
                hard.append(f"{path}: lien mort [[{tgt}]]")
            cible = tgt.strip().split("/")[-1].lower()
            cited_bases.add(cible)
            # R8c compare des stems : un embed portant `.base` cite bien ce comparatif.
            if cible.endswith(".base"):
                cited_bases.add(cible[:-5])
        for key, tgt in fm_links(fm):
            if not link_target_ok(tgt, names):
                hard.append(f"R2 — {path}: `{key}:` lien mort [[{tgt}]]")

        # 5b. R6 retirée avec `status:` (lot 2) : elle croisait deux champs dont l'un
        #     n'existe plus. `maturite: deprecated` se suffit — c'est le seul champ qui
        #     dit encore qu'une brique est morte.

        # 5c. R7 — la page doit être atteignable depuis un MOC
        if path[:-3].lower() not in moc_q and stem.lower() not in moc_n:
            hard.append(f"R7 — {path}: atteignable depuis aucun hub ni MOC "
                        "(relancer build_index puis build_mocs)")

        # ============ LOT 8 — §10, règles 3, 4, 5, 7, 8 et 10 ============
        # Ne portent que sur `role: brique` : le gabarit qu'elles décrivent est
        # celui de la brique (spec v3 §6).
        if typ == "brique":
            S = sections(body)

            # R19 (DURE) — §10 règle 3 : toute brique du dossier apparaît dans le
            # hub du dossier. Zone AUTO générée par `build_mocs.py`, donc vraie par
            # construction — ce que la règle attrape, c'est un hub NON régénéré, ou
            # absent. Mesure du 2026-09-06 : 0 sur 337.
            hub = hub_du_dossier(path)
            if hub not in hubs_cibles:
                hard.append(f"R19 — {path}: aucun hub `{hub}` pour ce dossier "
                            "(relancer build_index puis build_mocs)")
            elif stem not in hubs_cibles[hub]:
                hard.append(f"R19 — {path}: absente du hub de son dossier `{hub}` "
                            "(relancer build_index puis build_mocs)")

            # R20 (SOUPLE, DÉFINITIVE) — §10 règle 4 : voisinage déclaré. Une brique
            # peut légitimement n'avoir aucune alternative ; la signaler aide,
            # l'interdire mentirait. C'est la seule des dix qui reste en
            # avertissement PAR CONCEPTION et non par état du vault.
            # Mesure du 2026-09-06 : 62 briques sur 337.
            dossier = path.rsplit("/", 1)[0]
            if not fm.get("alternatives") and briques_par_dossier[dossier] > 1:
                warn.append(f"R20 — {path} : `alternatives:` vide alors que le dossier "
                            f"porte {briques_par_dossier[dossier] - 1} autre(s) "
                            "brique(s) — voisinage non déclaré")

            # R21 (DURE) — §10 règle 5, RÉÉCRITE au lot 8. La formulation d'origine
            # (« toute cellule `Écarter si` contient un wikilink ») est inatteignable :
            # 357 cellules sur 1 388, soit 26 %, et aucun enrichissement ne le
            # comblera — ce qui reste sur une fiche quand la redirection part au
            # comparatif est une BORNE de la brique seule, qui ne pointe vers
            # personne. Les deux reformulations proposées ne tiennent pas non plus,
            # prises séparément (mesures du 2026-09-06) :
            #   - lot 4, « toute exclusion qui nomme un besoin couvert par une autre
            #     brique porte son wikilink » : 177 violations. Elle confond « nommer
            #     une brique » et « nommer un besoin couvert par une brique » —
            #     « Centré Postgres : inutile dès qu'il faut un autre moteur » nomme
            #     Postgres sans rediriger vers lui ;
            #   - lot 5, « toute cellule dont le motif est une redirection porte un
            #     wikilink » : 18 violations, dont 5 flèches de VERSION (0.x vers 1.x)
            #     et 13 redirections vers une cible hors brain (argparse, mypy, « un
            #     wiki d'équipe »). Les exiger rendrait 25 outils non fichés
            #     obligatoires à ficher, ce qui n'est pas une décision de format.
            # La forme qui tient est leur CONJONCTION : le lot 5 donne la POSITION
            # (une redirection, marquée par la flèche), le lot 4 donne la CONDITION
            # (la cible est couverte par une brique du brain). Mesure sous cette
            # forme : 1 violation, réparée ; 0 aujourd'hui. Cf. le journal du lot 8.
            moi = {str(fm.get("nom") or "").lower()}
            moi |= {str(a).lower() for a in fm.get("alias") or []}
            for cellule in ecarter_cells(body):
                if not RE_FLECHE.search(cellule):
                    continue                      # ce n'est pas une redirection
                apres = RE_FLECHE.split(cellule, maxsplit=1)[1]
                if LINK_RE.search(apres):
                    continue                      # la redirection est déjà sourcée
                for cle, canon in idx_briques.items():
                    if cle in moi or canon.lower() in moi:
                        continue                  # la fiche elle-même
                    if re.search(r"(?<![\w.-])" + re.escape(cle) + r"(?![\w.-])",
                                 apres, re.I):
                        hard.append(f"R21 — {path}: redirection `Écarter si` vers "
                                    f"`{canon}`, qui est fiché, sans son wikilink "
                                    f"— « {cellule[:80]} »")
                        break

            # R23 (DURE sur `Mise en œuvre`, SOUPLE sur `Ressources`) — §10 règle 7.
            # Mesure du 2026-09-06 : 0 violation sur les cinq étiquettes de
            # `Mise en œuvre`, 337 fois ; 5 sur `Ressources` — quatre `Site`
            # (opencut.app, superwhisper.com, sniffnet.app, getcroc.com) et un
            # `Poids` (needle, poids du modèle sur HuggingFace). Ces cinq-là ne sont
            # PAS des fautes de rédaction : ce sont deux besoins que le vocabulaire
            # ne couvre pas, et l'arbitrage appartient à floSa — cf. décision 1 des
            # six décisions de forme du lot 6. Les durcir demanderait d'ouvrir le
            # vocabulaire, c'est-à-dire d'ajouter une exception pour faire passer la
            # règle : exactement l'inverse de ce lot. La moitié `Ressources` reste
            # donc en avertissement, avec ce motif, jusqu'à cet arbitrage.
            vus_meo = etiquettes(S.get("Mise en œuvre"))
            for lab in vus_meo:
                if lab not in MEO_LABELS:
                    hard.append(f"R23 — {path}: `Mise en œuvre` porte l'étiquette "
                                f"`{lab}`, hors des cinq du gabarit {sorted(MEO_LABELS)}")
            manque_meo = MEO_LABELS - set(vus_meo)
            if S.get("Mise en œuvre") is not None and manque_meo:
                hard.append(f"R23 — {path}: `Mise en œuvre` sans l'étiquette "
                            f"{sorted(manque_meo)}")
            for lab in etiquettes(S.get("Ressources")):
                if lab not in RES_LABELS:
                    warn.append(f"R23 — {path} : `Ressources` porte l'étiquette `{lab}`, "
                                f"hors vocabulaire {sorted(RES_LABELS)} — souple tant que "
                                "l'ouverture du vocabulaire n'est pas tranchée")

            # R24 (DURE) — §10 règle 8, RÉÉCRITE au lot 8. « Une même cible
            # n'apparaît pas dans deux sections » est arithmétiquement impossible
            # telle quelle : la règle 2 du lot 6 GARDE la cible en `Écarter si` faute
            # de comparatif d'accueil, et R11 EXIGE qu'elle figure en
            # `### Alternatives`. Deux contraintes dures et contradictoires — 242
            # violations mesurées. La règle porte sur les SECTIONS DE LISTE DE LIENS,
            # et sur ce qu'une puce LISTE (son entrée), pas sur ce qu'elle cite en
            # passant. Sous cette lecture : 0 sur 337, et le défaut d'origine est
            # toujours attrapé — Mimesis listé en `Alternatives` ET en `Liens` sur la
            # page Faker, deux listes de liens.
            listee: dict[str, set[str]] = collections.defaultdict(set)
            for titre in SECTIONS_LIENS:
                if S.get(titre) is None:
                    continue
                for cible in entrees_puces(S[titre]):
                    listee[cible].add(titre)
            for cible, ou in sorted(listee.items()):
                if len(ou) > 1:
                    hard.append(f"R24 — {path}: `{cible}` listé dans {sorted(ou)} "
                                "— une cible ne se liste que dans une section")

            # R26 (SOUPLE, DÉFINITIVE) — §10 règle 10. Reste en avertissement, et le
            # motif n'est pas l'état du vault : la règle N'EST PAS SCRIPTABLE.
            # `production`, `paquet`, `modèle`, `application` et `open-source` sont
            # des mots français ordinaires. Mesure du 2026-09-06 sur les seuls motifs
            # bornés : 11 candidats, dont 2 vrais — « Référence open-source de l'éval
            # RAG » (Ragas) redit bien le bandeau, mais « GLPK, HiGHS et SCIP côté
            # open source » (PuLP) parle des SOLVEURS, « Application de bureau »
            # (LM Studio) ajoute « de bureau », « un annuaire de liens » (osint4all)
            # est le cœur de la définition. Neuf faux positifs sur onze : durcir
            # rendrait la règle contournée, pas respectée. Elle sert de relecture
            # assistée, et c'est tout ce qu'elle peut être.
            d = S.get("Définition") or ""
            lic, mat = fm.get("licence_type"), fm.get("maturite")
            if lic in MOT_LICENCE and re.search(MOT_LICENCE[lic], d, re.I):
                warn.append(f"R26 — {path} : `## Définition` redit peut-être "
                            f"`licence_type: {lic}`, déjà au bandeau — à relire")
            if mat in MOT_MATURITE and re.search(MOT_MATURITE[mat], d, re.I):
                warn.append(f"R26 — {path} : `## Définition` redit peut-être "
                            f"`maturite: {mat}`, déjà au bandeau — à relire")

        # 6. taille (souple)
        n_lines = body.count("\n")
        limit = SIZE_WARN.get(typ)
        if limit and n_lines > limit:
            warn.append(f"{path}: {n_lines} lignes (> {limit}) → envisager une sous-note")

    w_alias, h_alias = check_alias(active)
    warn += w_alias
    hard += h_alias
    warn += check_bases(active, cited_bases)

    suffixe = f" ({len(illisibles)} illisible(s), cf. R17)" if illisibles else ""
    print(f"check_brain : {len(active)} pages actives contrôlées{suffixe}")
    for w in warn:
        print(f"  [WARN] {w}")
    if hard:
        print(f"\n{len(hard)} violation(s) DURE(s) :")
        for h in hard:
            print(f"  [FAIL] {h}")
        return 1
    print("OK — aucune violation dure." + (f" ({len(warn)} avertissement(s))" if warn else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
