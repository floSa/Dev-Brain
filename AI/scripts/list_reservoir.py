# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""list_reservoir.py — inventorie le réservoir v1 archivé.

Génère Archive-v1/_inventaire.md : la liste des pages de la v1, groupées par dossier.
Sert de menu d'inspiration — on y pioche un sujet, puis on demande au skill
enrichir-brain de (re)créer la page au format v2.

Usage : uv run AI/scripts/list_reservoir.py
Cross-OS, chemins relatifs, sortie déterministe.
"""

from __future__ import annotations

from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
RESERVOIR = VAULT / "Archive-v1"
OUT = RESERVOIR / "_inventaire.md"


def main() -> int:
    if not RESERVOIR.exists():
        print("Archive-v1/ absent — rien à inventorier.")
        return 0

    by_folder: dict[str, list[str]] = {}
    total = 0
    for md in RESERVOIR.rglob("*.md"):
        if md.name == OUT.name:
            continue
        folder = md.parent.relative_to(RESERVOIR).as_posix() or "."
        by_folder.setdefault(folder, []).append(md.stem)
        total += 1

    lines = [
        "# Inventaire du réservoir v1",
        "",
        "> Généré par `AI/scripts/list_reservoir.py`. Ne pas éditer à la main.",
        f"> {total} pages v1 conservées comme **référence** (hors brain v2).",
        "> Pour recréer un sujet au format v2 : demander au skill `enrichir-brain`.",
        "",
    ]
    for folder in sorted(by_folder):
        lines.append(f"## {folder}")
        for title in sorted(by_folder[folder], key=str.lower):
            lines.append(f"- {title}")
        lines.append("")

    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Inventaire écrit : {OUT.relative_to(VAULT).as_posix()} ({total} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
