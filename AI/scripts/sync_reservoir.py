# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""sync_reservoir.py — recoche le backlog de migration depuis l'index v2.

Source de vérité = AI/index/brain-index.json (nom + alias). Pour chaque ligne
`- ✅/⬜ **Nom** — ...` de Documentation/perso/reservoir-v1.md, met ✅ si la page
existe en v2, ⬜ sinon. On ne saisit JAMAIS les coches à la main.

En sortie : compteur global + par section, et le prochain lot suggéré (≤ 5 pages,
marge gardée pour les pages connexes créées par enrichir-brain).

Usage : uv run AI/scripts/sync_reservoir.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:  # console Windows cp1252 → forcer UTF-8 pour les accents / symboles
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # pragma: no cover
    pass

VAULT = Path(__file__).resolve().parents[2]
INDEX = VAULT / "AI" / "index" / "brain-index.json"
BACKLOG = VAULT / "Documentation" / "perso" / "reservoir-v1.md"
BATCH = 5  # plafond de pages explicites par conversation (hors pages connexes)

# Ligne gérée : "- ✅ **Nom** ...". L'émoji de statut est juste après le tiret.
LINE = re.compile(r"^(\s*-\s*)([✅⬜])(\s+\*\*)(.+?)(\*\*.*)$")
SEC = re.compile(r"^#+\s+(.*)$")


def load_done() -> dict[str, set[str]]:
    """Done-sets séparés par galaxie (évite les collisions nom lib ↔ nom concept,
    ex. le lib `hdbscan` vs le concept `HDBSCAN`)."""
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    pages = idx.get("pages", idx) if isinstance(idx, dict) else idx
    done: dict[str, set[str]] = {"dev": set(), "wiki": set()}
    for p in pages:
        gal = p.get("galaxie")
        bucket = done.get(gal)
        if bucket is None:
            continue
        if p.get("nom"):
            bucket.add(p["nom"].strip().lower())
        for a in p.get("alias") or []:
            bucket.add(str(a).strip().lower())
    done["all"] = done["dev"] | done["wiki"]
    return done


def main() -> int:
    if not INDEX.exists():
        sys.exit("brain-index.json absent — lancer d'abord build_index.py")
    done = load_done()
    lines = BACKLOG.read_text(encoding="utf-8").split("\n")

    section = "(début)"
    bucket = "all"  # galaxie attendue selon la PARTIE courante
    PART = re.compile(r"^#\s+PARTIE\s+([A-Z])")
    PART_BUCKET = {"A": "dev", "B": "wiki"}  # C/D = mixte → all
    counts: dict[str, list[int]] = {}
    todo: list[tuple[str, str]] = []
    out: list[str] = []
    flips = 0

    for ln in lines:
        mp = PART.match(ln)
        if mp:
            bucket = PART_BUCKET.get(mp.group(1), "all")
        ms = SEC.match(ln)
        if ms and not LINE.match(ln):
            section = ms.group(1).split("→")[0].split("⚠")[0].strip()
        m = LINE.match(ln)
        if m:
            name = m.group(4).strip()
            is_done = name.lower() in done[bucket]
            new_emoji = "✅" if is_done else "⬜"
            if new_emoji != m.group(2):
                flips += 1
            ln = m.group(1) + new_emoji + m.group(3) + m.group(4) + m.group(5)
            c = counts.setdefault(section, [0, 0])
            c[1] += 1
            if is_done:
                c[0] += 1
            else:
                todo.append((section, name))
        out.append(ln)

    BACKLOG.write_text("\n".join(out), encoding="utf-8")

    tot_d = sum(c[0] for c in counts.values())
    tot_t = sum(c[1] for c in counts.values())
    print(f"reservoir sync : {tot_d}/{tot_t} pages en v2  ({flips} coche(s) corrigée(s))")
    print("\nSections incomplètes :")
    for s, (d, t) in counts.items():
        if d < t:
            print(f"  [{d}/{t}] {s}")
    print(f"\nProchain lot suggéré (≤ {BATCH}, hors pages connexes) :")
    for s, n in todo[:BATCH]:
        print(f"  - {n}   ({s})")
    if not todo:
        print("  — backlog vide, tout est en v2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
