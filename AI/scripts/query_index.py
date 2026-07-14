# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""query_index.py — interroge AI/index/brain-index.json sans charger tout le brain.

Indispensable à l'échelle : le skill enrichir-brain (et l'humain) récupèrent
SEULEMENT le voisinage utile — existence d'une page, candidats alternatives d'une
catégorie, pages d'un tag — au lieu d'ingérer l'index entier. La sortie est bornée
par le nombre de correspondances, pas par la taille du brain.

Exemples :
    uv run AI/scripts/query_index.py --name Weaviate                # existe ? (nom + alias)
    uv run AI/scripts/query_index.py --categorie database/vector    # candidats alternatives
    uv run AI/scripts/query_index.py --tag rag --galaxie dev        # pages d'un tag
    uv run AI/scripts/query_index.py --tag-of "Weaviate"            # tags d'une page

Lit seulement l'index (pas de re-scan du vault). Cross-OS, chemins relatifs.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
INDEX = VAULT / "AI" / "index" / "brain-index.json"


def main() -> int:
    ap = argparse.ArgumentParser(description="Requête bornée sur brain-index.json")
    ap.add_argument("--name", help="existence par nom OU alias (insensible à la casse)")
    ap.add_argument("--categorie")
    ap.add_argument("--tag")
    ap.add_argument("--galaxie", choices=["dev", "wiki"])
    ap.add_argument("--tag-of", metavar="NOM", help="liste les tags d'une page")
    ap.add_argument(
        "--fields",
        default="nom,categorie,galaxie,pitch,tags,alternatives,path",
        help="champs renvoyés (csv)",
    )
    args = ap.parse_args()

    if not INDEX.exists():
        sys.exit("Index absent — lancer d'abord : uv run AI/scripts/build_index.py")
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    pages = data["pages"]

    # Cas dédié : tags d'une page donnée.
    if args.tag_of:
        n = args.tag_of.lower()
        for p in pages:
            if str(p.get("nom", "")).lower() == n:
                print(json.dumps({"nom": p["nom"], "tags": p.get("tags") or []},
                                 ensure_ascii=False, indent=2))
                return 0
        print(json.dumps({"nom": args.tag_of, "tags": None, "trouve": False},
                         ensure_ascii=False, indent=2))
        return 0

    def keep(p: dict) -> bool:
        if args.galaxie and p.get("galaxie") != args.galaxie:
            return False
        if args.categorie and p.get("categorie") != args.categorie:
            return False
        if args.tag and args.tag not in (p.get("tags") or []):
            return False
        if args.name:
            wanted = args.name.lower()
            noms = [str(p.get("nom", "")).lower()]
            noms += [str(a).lower() for a in (p.get("alias") or [])]
            if wanted not in noms:
                return False
        return True

    fields = [f.strip() for f in args.fields.split(",") if f.strip()]
    matches = [{k: p.get(k) for k in fields} for p in pages if keep(p)]
    print(json.dumps({"count": len(matches), "matches": matches},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
