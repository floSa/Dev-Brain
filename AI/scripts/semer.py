# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""semer — lanceur d une instance FIGEE.

    uv run AI/scripts/semer.py

Aucune installation : l en-tete PEP 723 ci-dessus dit a `uv` ce qu il faut, et
le paquet est a cote, dans `AI/scripts/brainkit/`. C est le chemin de lancement
d une instance `kit.mode: fige` — cf. `AI/scripts/FIGE.md`.
"""

from __future__ import annotations

import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
VAULT = ICI.parents[1]
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

from brainkit.semer.__main__ import main   # noqa: E402

if __name__ == "__main__":
    if not any(a.startswith("--manifeste") for a in sys.argv[1:]):
        sys.argv += ["--manifeste", str(VAULT / "brain.yml")]
    if not any(a.startswith("--vault") for a in sys.argv[1:]):
        sys.argv += ["--vault", str(VAULT)]
    raise SystemExit(main())
