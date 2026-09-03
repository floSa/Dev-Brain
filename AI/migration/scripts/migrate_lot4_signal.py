# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_signal.py — descend les 5 notions `concept/signal` dans l'arbre.

Lot 4, domaine « Signal & audio ». Deux gestes par page : réécrire la ligne
`categorie:` du frontmatter, puis `git mv` vers le dossier dérivé par
`AI/scripts/arbo.py`. Le CORPS des notions n'est pas touché.

Le seul domaine du lot où l'arbre d'arrivée était **déjà écrit** : `v3-arborescence.md`
décrit `Traitement/` avec ses 7 pages depuis le lot 3, en précisant que c'est
« l'état visé APRÈS le lot 4 » — les 2 briques `signal/traitement` étaient sous le
seuil tant que les 5 notions portaient `concept/signal`. Rien à arbitrer : aucune des
5 ne parle d'audio, elles vont toutes en `signal/traitement`, et `librosa` reste seul
au niveau du domaine avec `signal/audio`.

Usage : uv run AI/migration/scripts/migrate_lot4_signal.py [--dry-run]
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
    "Traitement du signal": "signal/traitement",
    "Transformée de Fourier": "signal/traitement",
    "STFT et spectrogramme": "signal/traitement",
    "Filtrage numérique": "signal/traitement",
    "Ondelettes": "signal/traitement",
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
    for md in (VAULT / arbo.DOM_LABEL["signal"]).rglob("*.md"):
        for ligne in md.read_text(encoding="utf-8").split("\n")[:40]:
            if ligne.startswith("categorie:"):
                cats.append(ligne.split(":", 1)[1].strip())
    promus = arbo.promotions(cats)
    print(f"sous-domaines promus : {promus}")

    print()
    print("-- les notions qui descendent --")
    for nom, cible in sorted(CIBLES.items()):
        src = SOURCE / f"{nom}.md"
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:26} {cible:20} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    print()
    print("-- les briques que la promotion deplace --")
    bouges = 0
    dom = VAULT / arbo.DOM_LABEL["signal"]
    for md in sorted(dom.rglob("*.md")):
        fm = md.read_text(encoding="utf-8").splitlines()[:40]
        if any(l.strip() == "role: hub" for l in fm):
            continue
        cat = next((l.split(":", 1)[1].strip() for l in fm
                    if l.startswith("categorie:")), "")
        attendu = VAULT / arbo.dossier_attendu(cat, promus)
        if md.parent == attendu:
            continue
        bouges += 1
        print(f"  {md.stem:26} {cat:20} -> "
              f"{(attendu / md.name).relative_to(VAULT).as_posix()}")
        if dry:
            continue
        attendu.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                        str((attendu / md.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)

    # Le comparatif du domaine NE bouge pas, et c'est mesuré : son filtre est
    # `role == "brique"` + tag `signal-processing`, donc ses 3 membres enjambent
    # `signal/traitement` (scipy.signal, PyWavelets) et `signal/audio` (librosa).
    # Un comparatif vit dans le dossier de ses membres ; ici c'est le domaine.
    print()
    print("-- comparatifs : aucun (le filtre du seul .base enjambe les 2 sous-domaines)")

    verbe = "a deplacer" if dry else "deplacee(s)"
    print()
    print(f"{len(CIBLES)} notion(s) et {bouges} brique(s) {verbe}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
