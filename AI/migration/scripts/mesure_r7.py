"""Mesure R7 : pour chaque page du brain, quelles pages d'aiguillage la citent.

Jetable — sert à conditionner la suppression d'une MOC (lot 4).
Usage : uv run AI/migration/_r7_mesure.py <chemin de MOC à retirer> ...
"""
import re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"\[\[([^\]|#]+)")
RE_HUB = re.compile(r"^role: hub\s*$", re.M)
NON = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
       "Projects", "docs", "MOC"}


def aiguillages():
    out = list((VAULT / "MOC").rglob("*.md"))
    out.append(VAULT / "Home.md")
    for d in VAULT.iterdir():
        if d.is_dir() and d.name not in NON:
            for md in d.rglob("*.md"):
                if RE_HUB.search(md.read_text(encoding="utf-8")[:400]):
                    out.append(md)
    return out


def main():
    retires = {(VAULT / a).resolve() for a in sys.argv[1:]}
    pages = []
    for d in VAULT.iterdir():
        if d.is_dir() and d.name not in NON:
            pages += list(d.rglob("*.md"))
    aig = aiguillages()
    cite = {}
    for a in aig:
        txt = a.read_text(encoding="utf-8")
        for t in LINK_RE.findall(txt):
            cite.setdefault(t.strip().lower(), set()).add(a.resolve())
    perdus, deja = [], []
    for p in pages:
        src = cite.get(p.stem.lower(), set())
        src = {s for s in src if s != p.resolve()}
        if not src:
            deja.append(p.relative_to(VAULT).as_posix())
        elif src <= retires:
            perdus.append((p.relative_to(VAULT).as_posix(),
                           sorted(s.relative_to(VAULT).as_posix() for s in src)))
    print(f"pages du brain : {len(pages)}  ·  aiguillages : {len(aig)}")
    print(f"deja sans aiguillage (hors perimetre) : {len(deja)}")
    for x in deja:
        print("   [ORPHELIN]", x)
    print(f"perdraient leur SEULE porte si retrait : {len(perdus)}")
    for x, s in perdus:
        print("   [PERDU]", x, "<-", s)


main()
