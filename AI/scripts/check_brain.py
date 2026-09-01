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
    pour les 5 types du vault : service, concept, outil, pattern, rule ; un
    `type:` inconnu ou absent est refusé, plus de page sans gabarit            [R3]
  - valeurs d'enum fermées (hosted, scaling, licence_type, maturite, status)
  - famille ∈ énumération fermée de Documentation/general/taxonomie.md (bloc
    ```famille) sur les gabarits service et outil                             [R14]
  - tags ⊆ vocabulaire contrôlé (Documentation/general/tags.md)
  - categorie ∈ taxonomie (Documentation/general/taxonomie.md)
  - domaines ⊆ vocabulaire de Documentation/general/themes.md                 [R4]
  - alternatives réciproques (si A cite B, B cite A)
  - cible d'alternative absente de l'index → échec explicite, plus de silence  [R12]
  - la section `## Alternatives` couvre toutes les cibles du frontmatter       [R11]
  - pitch réinjecté : la puce d'une cible listée en `alternatives:` commence par
    le `pitch:` courant de cette cible (normalisation `**` + espaces)          [R1]
  - aucun lien [[...]] mort, dans le corps ET dans le frontmatter              [R2]
  - `maturite: deprecated` ⇒ `status != actif`                                 [R6]
  - `nom:` identique au nom du fichier, sauf caractère illégal en nom de fichier [R9]
  - toute page atteignable depuis un MOC                                       [R7]
Règles SOUPLES (avertissent) :
  - page trop longue → suggérer une sous-note
  - collisions d'alias : doublon interne, ou alias qui est le `nom:` d'une autre
    page de la même galaxie — souple, l'unicité globale détruirait des usages
    sémantiques légitimes (`shap`, `yolo`, `map`)                              [R5]
  - couverture des comparatifs `.base` — souple, créer un comparatif est une
    décision éditoriale, pas technique                                         [R8]
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
SCAN_DIRS = ["Dev", "Wiki"]
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
    "service": ["nom", "pitch", "categorie", "galaxie", "status"],
    "concept": ["nom", "categorie", "galaxie", "domaines"],
    "outil": ["nom", "pitch", "categorie", "galaxie", "status"],
    "pattern": ["galaxie", "contexte", "services_cles"],
    "rule": ["galaxie", "domaine", "applicable", "strictness"],
}
# Champs EXACTS autorisés par gabarit (§5) — tout champ hors liste = non conforme.
SERVICE_ALLOWED = {"galaxie", "type", "nom", "alias", "pitch", "categorie", "famille",
                   "licence_type", "hosted", "maturite", "langage", "scaling",
                   "alternatives", "remplace_par", "status", "tags",
                   "url_docs", "url_repo"}
CONCEPT_ALLOWED = {"galaxie", "type", "nom", "alias", "categorie", "domaines", "tags"}
# `type: outil` — même socle que service, moins les champs de déploiement
# (hosted, scaling, maturite, remplace_par), plus `os` et `domaines`.
OUTIL_ALLOWED = {"galaxie", "type", "nom", "alias", "pitch", "categorie", "famille",
                 "domaines", "licence_type", "langage", "os", "alternatives", "status",
                 "tags", "url_docs", "url_repo"}
# `type: pattern` / `type: rule` — gabarits sans `nom:` ni `categorie:` (la
# taxonomie ne les couvre pas ; leur porte d'entrée est MOC/Types/, cf. build_mocs).
PATTERN_ALLOWED = {"galaxie", "type", "tags", "contexte", "services_cles", "projets_appliques"}
RULE_ALLOWED = {"galaxie", "type", "tags", "domaine", "applicable", "strictness"}
ALLOWED = {"service": SERVICE_ALLOWED, "concept": CONCEPT_ALLOWED,
           "outil": OUTIL_ALLOWED, "pattern": PATTERN_ALLOWED, "rule": RULE_ALLOWED}
# Valeurs autorisées (listes fermées) pour les champs Service à enum.
VALUE_ENUMS = {
    "hosted": {"self", "managed", "both"},
    "scaling": {"single-node", "distributed", "serverless"},
    "licence_type": {"open-source", "source-available", "proprietary", "open-core"},
    "maturite": {"production", "beta", "experimental", "deprecated"},
    "status": {"actif", "en-eval", "abandonne"},
}
SIZE_WARN = {"service": 90, "concept": 200}
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
ALT_SECTION_RE = re.compile(r"\n## Alternatives\n(.*?)(?=\n## |\Z)", re.S)
ALT_BULLET_RE = re.compile(r"\s*-\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]\s*[—-]\s*(.+)")
# Caractères interdits dans un nom de fichier (Windows compris) : un `nom:` qui en
# porte un ne PEUT pas être le nom de son fichier — exemption de R9.
FS_ILLEGAL = set('/\\:*?"<>|')
# Seuil R8a : au-dessous, une catégorie n'a pas assez de membres pour qu'un
# comparatif ait un sens.
BASE_MIN_CAT = 3
BASE_MIN_MEMBRES = 2


def parse(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, parts[2]
    return (fm if isinstance(fm, dict) else None), parts[2]


def rel(p: Path) -> str:
    return p.relative_to(VAULT).as_posix()


def is_active_v2(scan_dir: str, fm: dict) -> bool:
    if scan_dir == "Dev":
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
    body = "\n".join(c for langue, c in _fences("taxonomie.md") if not langue)
    cats: set[str] = set()
    # groupes prefix/{a, b, c} (peuvent s'étaler sur plusieurs lignes)
    for m in re.finditer(r"([a-z][\w-]*)/\{([^}]*)\}", body, re.S):
        for item in re.split(r"[,\n]", m.group(2)):
            item = item.strip()
            if item:
                cats.add(f"{m.group(1)}/{item}")
    # tokens nus restants (auth, storage, compute/distributed…)
    body2 = re.sub(r"[a-z][\w-]*/\{[^}]*\}", "", body, flags=re.S)
    for tok in re.findall(r"^[a-z][\w-]*(?:/[a-z][\w-]*)?$", body2, re.M):
        cats.add(tok.strip())
    return cats


def resolvable_names() -> set[str]:
    """Tous les noms de fichiers (md + base) du vault, minuscules, pour résoudre [[liens]]."""
    names: set[str] = set()
    for ext in ("*.md", "*.base"):
        for p in VAULT.rglob(ext):
            if ".git" in p.parts:
                continue
            names.add(p.stem.lower())
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


def moc_targets() -> tuple[set[str], set[str]]:
    """Cibles citées par les MOC — (chemins qualifiés, noms nus), minuscules (R7)."""
    qualifies: set[str] = set()
    nus: set[str] = set()
    if not MOC.exists():
        return qualifies, nus
    for md in MOC.rglob("*.md"):
        for tgt in LINK_RE.findall(md.read_text(encoding="utf-8")):
            tgt = tgt.strip()
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
        if ".git" in base.parts:
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
        if fm.get("galaxie") == "dev" and fm.get("categorie"))
    for cat, n in sorted(compte.items()):
        if n < BASE_MIN_CAT:
            continue
        couverte = any(
            sel is not None
            and sum(1 for p in sel if fm_par_path[p].get("categorie") == cat) >= BASE_MIN_MEMBRES
            for sel in membres.values())
        if not couverte:
            warn.append(f"R8a — categorie `{cat}` : {n} pages Dev, aucun comparatif `.base` "
                        "ne les réunit")
    return warn


def check_alias(active: list[tuple[str, dict, str]]) -> list[str]:
    """R5 (souple) : collisions d'alias. Souple par décision d'audit — l'unicité
    globale détruirait des usages sémantiques légitimes (`shap`, `yolo`, `map`)."""
    warn: list[str] = []
    noms: dict[tuple, str] = {}
    for path, fm, _ in active:
        if fm.get("nom"):
            noms[(fm.get("galaxie"), str(fm["nom"]).lower())] = path
    for path, fm, _ in active:
        bas = [str(a).lower() for a in (fm.get("alias") or [])]
        dup = sorted({a for a in bas if bas.count(a) > 1})
        if dup:
            warn.append(f"R5 — {path} : alias en doublon interne {dup}")
        for a in sorted(set(bas)):
            proprio = noms.get((fm.get("galaxie"), a))
            if proprio and proprio != path:
                warn.append(f"R5 — {path} : alias `{a}` est le `nom:` de `{proprio}` "
                            "(même galaxie)")
    return warn


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
    for d in SCAN_DIRS:
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm, body = parse(md.read_text(encoding="utf-8"))
            if fm is None or not is_active_v2(d, fm):
                continue
            active.append((rel(md), fm, body))

    by_name = {fm.get("nom"): fm for _, fm, _ in active}
    pitches = {fm.get("nom"): (fm.get("pitch") or "")
               for _, fm, _ in active if fm.get("nom")}
    cited_bases: set[str] = set()
    hard: list[str] = []
    warn: list[str] = []

    for path, fm, body in active:
        typ = fm.get("type")
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
            hard.append(f"R3 — {path}: `type: {typ or '(absent)'}` sans gabarit déclaré "
                        f"(connus : {sorted(ALLOWED)})")

        # 1b. valeurs d'enum : champs à liste fermée (hosted, scaling, licence_type, maturite, status)
        for field, vals in VALUE_ENUMS.items():
            v = fm.get(field)
            if v is not None and v not in vals:
                hard.append(f"{path}: `{field}: {v}` hors valeurs autorisées {sorted(vals)}")

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

        # 4. réciprocité des alternatives
        #    R12 — une cible absente de l'index échoue désormais explicitement, au lieu
        #    d'être ignorée en silence (l'ancien `if b in by_name` avalait la faute).
        front_alts = alt_names(fm)
        for b in front_alts:
            if b not in by_name:
                hard.append(f"R12 — {path}: alternative `{b}` absente de l'index "
                            "(page inexistante, renommée ou hors périmètre v2)")
            elif nom not in alt_names(by_name[b]):
                hard.append(f"{path}: alternative `{b}` non réciproque (manque `{nom}`)")

        # 4b. R11 — la section `## Alternatives` couvre toutes les cibles du frontmatter
        #     R1  — et la puce de chaque cible commence par le `pitch:` courant de la cible
        if front_alts:
            sec = alt_section(body) or ""
            en_section = {(b or a).split("/")[-1]
                          for a, b in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", sec)}
            manquants = sorted(front_alts - en_section)
            if manquants:
                hard.append(f"R11 — {path}: cible(s) du frontmatter absente(s) de "
                            f"`## Alternatives` {manquants}")
            for line in sec.splitlines():
                m = ALT_BULLET_RE.match(line)
                if not m:
                    continue
                cible = (m.group(2) or m.group(1)).split("/")[-1]
                if cible not in front_alts:
                    continue  # puce hors `alternatives:` — exemptée
                attendu = norm_pitch(pitches.get(cible, ""))
                if attendu and not norm_pitch(m.group(3)).startswith(attendu):
                    hard.append(f"R1 — {path}: la puce de `{cible}` ne commence pas par son "
                                f"pitch courant « {attendu} »")

        # 5. liens morts — corps (historique) ET frontmatter (R2)
        for tgt in LINK_RE.findall(body):
            if not link_target_ok(tgt, names):
                hard.append(f"{path}: lien mort [[{tgt}]]")
            cited_bases.add(tgt.strip().split("/")[-1].lower())
        for key, tgt in fm_links(fm):
            if not link_target_ok(tgt, names):
                hard.append(f"R2 — {path}: `{key}:` lien mort [[{tgt}]]")

        # 5b. R6 — `maturite: deprecated` ⇒ `status != actif`
        if fm.get("maturite") == "deprecated" and fm.get("status") == "actif":
            hard.append(f"R6 — {path}: `maturite: deprecated` avec `status: actif` "
                        "(une brique dépréciée n'est pas un choix actif)")

        # 5c. R7 — la page doit être atteignable depuis un MOC
        if path[:-3].lower() not in moc_q and stem.lower() not in moc_n:
            hard.append(f"R7 — {path}: atteignable depuis aucun MOC "
                        "(relancer build_index puis build_mocs)")

        # 6. taille (souple)
        n_lines = body.count("\n")
        limit = SIZE_WARN.get(typ)
        if limit and n_lines > limit:
            warn.append(f"{path}: {n_lines} lignes (> {limit}) → envisager une sous-note")

    warn += check_alias(active)
    warn += check_bases(active, cited_bases)

    print(f"check_brain : {len(active)} pages actives contrôlées")
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
