# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_index.py — génère l'index du DevBrain v2 (machine + humain).

Scanne les galaxies DEV (Dev/) et WIKI (Wiki/) et produit, dans AI/index/ :
  - brain-index.json : catalogue machine, lu par les skills via query_index.py
  - brain-index.md   : document humain, propre — Dev et Wiki séparés, par domaine

Portée « v2 only » : Dev/ est 100 % v2 ; côté Wiki, le réservoir v1 (pages portant
des champs hérités v1) est ignoré — il reste en place comme référence, hors index actif.

Usage : uv run AI/scripts/build_index.py
Cross-OS, chemins relatifs, sortie déterministe (triée, sans horodatage).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/build_index.py")

VAULT = Path(__file__).resolve().parents[2]
SCAN_DIRS = ["Dev", "Wiki"]
OUT_JSON = VAULT / "AI" / "index" / "brain-index.json"
OUT_MD = VAULT / "AI" / "index" / "brain-index.md"

# Champs repris dans l'index. Ordre stable.
FIELDS = ["nom", "alias", "type", "galaxie", "categorie", "domaines",
          "pitch", "tags", "alternatives"]

# Champs hérités v1 : leur présence dans une page Wiki = réservoir → hors index actif.
V1_MARKERS = {"created", "modified", "maturite", "lecture_min", "auteurs_cles",
              "sous_categories", "score", "mes_projets", "clients_officiels",
              "plateforme", "remplace", "url_officiel", "licence"}


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def is_active_v2(scan_dir: str, fm: dict) -> bool:
    """Dev/ = entièrement v2 ; Wiki/ = v2 seulement si aucun champ hérité v1."""
    if scan_dir == "Dev":
        return True
    return not (V1_MARKERS & set(fm.keys()))


def collect() -> tuple[list[dict], list[str], int]:
    pages: list[dict] = []
    skipped: list[str] = []
    reservoir = 0
    for d in SCAN_DIRS:
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm = parse_frontmatter(md.read_text(encoding="utf-8"))
            if fm is None:
                skipped.append(rel(md))
                continue
            if not is_active_v2(d, fm):
                reservoir += 1
                continue
            entry: dict = {"path": rel(md)}
            for f in FIELDS:
                entry[f] = fm.get(f)
            if not entry.get("nom"):
                entry["nom"] = md.stem
            pages.append(entry)
    pages.sort(key=lambda e: e["path"])
    return pages, skipped, reservoir


def build_tags_index(pages: list[dict]) -> dict[str, list[str]]:
    ti: dict[str, list[str]] = {}
    for p in pages:
        for t in p.get("tags") or []:
            ti.setdefault(t, []).append(p["nom"])
    return {t: sorted(set(v)) for t, v in sorted(ti.items())}


# --- rendu du document humain ---------------------------------------------

GAL_LABEL = {
    "dev": "Dev — briques techniques (galaxie dev)",
    "wiki": "Wiki — notions (galaxie wiki)",
}
TYPE_ORDER = ["service", "pattern", "rule", "rex", "concept", "workflow", "outil"]


def descriptor(p: dict) -> str:
    """Ligne « solution » : pitch côté Dev ; domaines/alias côté Wiki."""
    if p.get("pitch"):
        return p["pitch"]
    bits = []
    if p.get("domaines"):
        bits.append("domaines : " + ", ".join(p["domaines"]))
    if p.get("alias"):
        bits.append("alias : " + ", ".join(p["alias"]))
    return " · ".join(bits) if bits else "—"


def render_md(pages: list[dict], reservoir: int) -> str:
    lines = [
        "# Index — DevBrain v2",
        "",
        "> Document généré par `AI/scripts/build_index.py`. Ne pas éditer à la main.",
        f"> {len(pages)} pages actives. Réservoir v1 ({reservoir} pages Wiki) : "
        "référence, non indexé.",
        "",
    ]
    by_gal: dict[str, list[dict]] = {}
    for p in pages:
        by_gal.setdefault(p.get("galaxie") or "?", []).append(p)

    for gal in ["dev", "wiki"]:
        group = by_gal.get(gal)
        if not group:
            continue
        lines += [f"## {GAL_LABEL.get(gal, gal)}", ""]
        by_type: dict[str, list[dict]] = {}
        for p in group:
            by_type.setdefault(p.get("type") or "?", []).append(p)
        for typ in sorted(by_type, key=lambda t: (
                TYPE_ORDER.index(t) if t in TYPE_ORDER else 99, t)):
            lines += [f"### {typ}", ""]
            by_cat: dict[str, list[dict]] = {}
            for p in by_type[typ]:
                by_cat.setdefault(p.get("categorie") or "(sans catégorie)", []).append(p)
            for cat in sorted(by_cat):
                lines.append(f"#### {cat}")
                for p in sorted(by_cat[cat], key=lambda e: e["nom"].lower()):
                    lines.append(f"- **{p['nom']}** — {descriptor(p)}")
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    pages, skipped, reservoir = collect()
    index = {
        "generated_by": "AI/scripts/build_index.py",
        "scanned": SCAN_DIRS,
        "scope": "v2-only (réservoir v1 exclu)",
        "count": len(pages),
        "tags_index": build_tags_index(pages),
        "pages": pages,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    OUT_MD.write_text(render_md(pages, reservoir), encoding="utf-8")

    by_gal: dict[str, int] = {}
    for p in pages:
        key = p.get("galaxie") or "?"
        by_gal[key] = by_gal.get(key, 0) + 1
    print(f"Index écrit : {rel(OUT_JSON)} + {rel(OUT_MD)}")
    print(f"  {len(pages)} pages actives — {by_gal} ; réservoir v1 ignoré : {reservoir}")
    if skipped:
        print(f"  {len(skipped)} fichier(s) sans frontmatter ignoré(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
