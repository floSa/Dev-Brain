# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_brain.py — valide la cohérence du DevBrain v2 (règles tenues par script).

Contrôle les pages actives v2 (Dev/ + Wiki/ hors réservoir v1). Sort en code != 0
si une règle DURE est violée : c'est le garde-fou qui évite le bazar de la v1.
Le skill enrichir-brain l'exécute en fin de protocole ; lançable aussi à la main.

Usage : uv run AI/scripts/check_brain.py

Règles DURES (bloquent) :
  - frontmatter conforme au gabarit (champs requis présents, champs morts v1 absents)
  - tags ⊆ vocabulaire contrôlé (Documentation/general/tags.md)
  - categorie ∈ taxonomie (Documentation/general/taxonomie.md)
  - alternatives réciproques (si A cite B, B cite A)
  - aucun lien [[...]] mort (hors [[REX - *]] assumés en attente)
Règles SOUPLES (avertissent) :
  - page trop longue → suggérer une sous-note
"""

from __future__ import annotations

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

V1_MARKERS = {"created", "modified", "maturite", "lecture_min", "auteurs_cles",
              "sous_categories", "score", "mes_projets", "clients_officiels",
              "plateforme", "remplace", "url_officiel", "licence"}

REQUIRED = {
    "service": ["nom", "pitch", "categorie", "galaxie", "status"],
    "concept": ["nom", "categorie", "galaxie", "domaines"],
}
# Champs EXACTS autorisés par gabarit (§5) — tout champ hors liste = non conforme.
SERVICE_ALLOWED = {"galaxie", "type", "nom", "alias", "pitch", "categorie",
                   "licence_type", "hosted", "maturite", "langage", "scaling",
                   "alternatives", "remplace_par", "status", "tags",
                   "url_docs", "url_repo"}
CONCEPT_ALLOWED = {"galaxie", "type", "nom", "alias", "categorie", "domaines", "tags"}
ALLOWED = {"service": SERVICE_ALLOWED, "concept": CONCEPT_ALLOWED}
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


def load_categories() -> set[str]:
    txt = (DOC / "taxonomie.md").read_text(encoding="utf-8")
    body = "\n".join(re.findall(r"```(.*?)```", txt, re.S))
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


def main() -> int:
    vocab = load_tag_vocab()
    cats = load_categories()
    names = resolvable_names()

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
    hard: list[str] = []
    warn: list[str] = []

    for path, fm, body in active:
        typ = fm.get("type")
        nom = fm.get("nom") or path

        # 1. frontmatter conforme au gabarit (champs requis + aucun champ hors gabarit §5)
        for req in REQUIRED.get(typ, []):
            if not fm.get(req):
                hard.append(f"{path}: champ requis manquant `{req}`")
        if typ in ALLOWED:
            extra = set(fm.keys()) - ALLOWED[typ]
            if extra:
                hard.append(f"{path}: champ(s) hors gabarit §5 {sorted(extra)}")

        # 1b. valeurs d'enum : champs à liste fermée (hosted, scaling, licence_type, maturite, status)
        for field, vals in VALUE_ENUMS.items():
            v = fm.get(field)
            if v is not None and v not in vals:
                hard.append(f"{path}: `{field}: {v}` hors valeurs autorisées {sorted(vals)}")

        # 2. tags ⊆ vocabulaire
        for t in fm.get("tags") or []:
            if t not in vocab:
                hard.append(f"{path}: tag hors vocabulaire `{t}` (cf. tags.md)")

        # 3. categorie ∈ taxonomie
        cat = fm.get("categorie")
        if cat and cat not in cats:
            hard.append(f"{path}: categorie hors taxonomie `{cat}`")

        # 4. réciprocité des alternatives
        for b in alt_names(fm):
            if b in by_name and nom not in alt_names(by_name[b]):
                hard.append(f"{path}: alternative `{b}` non réciproque (manque `{nom}`)")

        # 5. liens morts (hors REX - * assumés)
        for tgt in LINK_RE.findall(body):
            base = tgt.strip().split("/")[-1]
            if base.lower().startswith("rex - "):
                continue
            if not link_target_ok(tgt, names):
                hard.append(f"{path}: lien mort [[{tgt}]]")

        # 6. taille (souple)
        n_lines = body.count("\n")
        limit = SIZE_WARN.get(typ)
        if limit and n_lines > limit:
            warn.append(f"{path}: {n_lines} lignes (> {limit}) → envisager une sous-note")

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
