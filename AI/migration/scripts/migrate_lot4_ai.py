# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_ai.py — descend les 4 notions `concept/ai` dans « Sécurité/ ».

Lot 4. Deux gestes par page : réécrire `categorie:`, puis `git mv`. Le CORPS des
notions n'est pas touché.

`AI/migration/lot-4-notions.md` annonçait ces quatre-là comme « une VRAIE décision,
à remonter » : le vocabulaire n'avait pas de domaine pour elles. Deux lectures
s'opposaient et les deux hubs concernés le disaient à voix haute — celui de
« LLM & IA générative » les revendiquait nommément, celui de « Sécurité » écrivait
qu'elles « ne sont pas descendues ici ». L'arbre de décision du domaine penche du
côté LLM (D1 passe avant D9 : sans modèle, pas d'injection de prompt).

Arbitrage de floSa, 2026-09-05 : **`security/ia`**. Deux raisons, et aucune n'est
un effet de seuil (3 -> 7 pages ne promeut aucun sous-dossier) :

  - ces pages portent `concept/ai` et non `concept/llm`. La famille large a été
    choisie exprès quand elles ont été écrites ;
  - la sécurité est une **pratique qui traverse les modèles**, pas un sous-sujet de
    l'IA générative.

Les deux phrases de hub qui disaient le contraire sont réécrites dans le même commit :
laisser un hub annoncer une page qu'il n'a plus est exactement le défaut que la
remontée 2 du pilote décrit, dans l'autre sens.

Usage : uv run AI/migration/scripts/migrate_lot4_ai.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

CIBLES = {
    "AI security": "security/ia",
    "Prompt injection": "security/ia",
    "Jailbreaking and defenses": "security/ia",
    "Guardrails": "security/ia",
}


def recategoriser(path: Path, cible: str) -> None:
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def main() -> int:
    dry = "--dry-run" in sys.argv
    manquants = [n for n in CIBLES if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")

    cats = list(CIBLES.values())
    for md in (VAULT / arbo.DOM_LABEL["security"]).rglob("*.md"):
        for ligne in md.read_text(encoding="utf-8").split("\n")[:40]:
            if ligne.startswith("categorie:"):
                cats.append(ligne.split(":", 1)[1].strip())
    promus = arbo.promotions(cats)
    print(f"sous-domaines promus : {promus or '{} (aucun — security/ia fait 4)'}")

    print()
    print("-- les notions qui descendent --")
    for nom, cible in sorted(CIBLES.items()):
        src = SOURCE / f"{nom}.md"
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:28} {cible:14} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    print()
    print(f"{len(CIBLES)} notion(s) {'a deplacer' if dry else 'deplacee(s)'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
