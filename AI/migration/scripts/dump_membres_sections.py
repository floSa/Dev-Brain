# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""dump_membres_sections.py — les sections décisionnelles des membres d'un `.base`.

Lot 5. Le pilote a mesuré que le poste dominant du lot n'est ni l'écriture ni
l'arbitrage : c'est la LECTURE des fiches comparées (~230 fiches pour les 41
comparatifs restants). Il a mesuré aussi OÙ le critère de départage se lit —
`## Pourquoi` sur 45 puces sur 45, `## Pièges` sur 38, `## Quand NE PAS
l'utiliser` sur 1. Cf. remontée 6 de `AI/migration/lot-5-comparatifs.md`, qui
appelle ce script en toutes lettres.

Ce script ne juge rien et n'écrit rien dans le vault : il énumère les membres
d'un `.base` (même prédicat que `mesure_membres_bases.py`, donc mêmes membres)
et recopie, pour chacun, ses trois sections décisionnelles. Le critère se lit
dans la sortie ; il ne s'y invente pas.

Usage : uv run AI/migration/scripts/dump_membres_sections.py "<motif du .base>"
"""

from __future__ import annotations

import sys
from pathlib import Path

# La sortie porte des flèches, des guillemets français et des accents : sur une
# console Windows en cp1252, `print` lève UnicodeEncodeError sur le premier `→`.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import check_brain as cb  # noqa: E402

import yaml  # noqa: E402

SECTIONS = ("## Pourquoi", "## Quand l'utiliser", "## Quand NE PAS l'utiliser", "## Pièges")


def pages() -> list[tuple[str, dict, Path]]:
    out = []
    for md in sorted(VAULT.rglob("*.md")):
        if cb.hors_vault(md, VAULT):
            continue
        txt = md.read_text(encoding="utf-8")
        if not txt.startswith("---"):
            continue
        parts = txt.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and "role" in fm:
            out.append((cb.rel(md), fm, md))
    return out


def extrait(md: Path) -> str:
    txt = md.read_text(encoding="utf-8")
    lignes, garde, buf = txt.splitlines(), False, []
    for ln in lignes:
        if ln.startswith("## "):
            garde = any(ln.startswith(s) for s in SECTIONS)
        if garde:
            buf.append(ln)
    return "\n".join(buf).strip()


def main(motif: str) -> int:
    actives = pages()
    cibles = [b for b in sorted(VAULT.rglob("*.base"))
              if not cb.hors_vault(b, VAULT) and motif.lower() in b.name.lower()]
    if not cibles:
        print(f"aucun `.base` ne correspond à « {motif} »")
        return 1
    for base in cibles:
        doc = yaml.safe_load(base.read_text(encoding="utf-8")) or {}
        filt = doc.get("filters")
        print("=" * 78)
        print(f"BASE  {cb.rel(base)}")
        print("=" * 78)
        for path, fm, md in actives:
            if cb.base_match(filt, path, fm):
                print(f"\n{'-' * 70}\n### {md.stem}   [{fm.get('categorie')}]  {path}")
                print(f"pitch: {fm.get('pitch')}")
                print(extrait(md) or "(aucune section décisionnelle)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else ""))
