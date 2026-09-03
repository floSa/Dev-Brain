# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_arbo.py — le chemin d'une page concorde-t-il avec sa `categorie:` ?

Spec : AI/design/brain-v3.md §10 règle 2 et §11 · lot : AI/migration/lot-3-arborescence.md

Contrôle trois choses, et rien d'autre :

  1. **Concordance chemin / catégorie** — une page migrée vit dans le dossier que sa
     `categorie:` désigne (dérivation de AI/scripts/arbo.py). Le cas contraire est
     signalé avec le déplacement à faire.
  2. **Seuil de promotion** — un sous-domaine à 5 pages ou plus a son dossier ; un
     sous-domaine en dessous n'en a pas. Le seuil décide, pas l'humeur. Les pages
     `arbo.ROLES_HORS_SEUIL` (les `role: comparatif` du lot 5) sont vérifiées comme
     les autres mais ne comptent pas : un comparatif n'est pas un membre du comparatif.
  3. **Hub par dossier** — tout dossier de l'arbre porte une page `role: hub` à son nom.
  4. **Frontmatter lisible** — une page dont le frontmatter ne parse pas est une ERREUR,
     jamais une absence (remontée 44 du lot 4). Elle était silencieusement sautée : ni
     comptée, ni vérifiée. Le motif exact est affiché, parce que le symptôme observé
     décrivait la conséquence — « ce dossier n'a pas de hub » — et non la cause.

Sort en code 1 si un écart est trouvé. Une population est comptée à part, parce
qu'elle n'a pas de chemin à dériver : les `role: pattern` et `role: rule`
(`arbo.ROLES_SANS_CATEGORIE`), qui n'ont pas de `categorie:` par construction et
vivent dans « Patterns/ » et « Rules/ ».

Il y en avait deux : les pages restées sous `Dev/` puis `Wiki/` étaient comptées sans
être vérifiées, le temps que leur domaine passe. `arbo.LEGACY` est vide depuis la
clôture du lot 4 — plus aucune page du vault n'échappe au contrôle.

Usage : uv run AI/scripts/check_arbo.py
"""

from __future__ import annotations

import collections
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arbo  # noqa: E402

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/check_arbo.py")

VAULT = Path(__file__).resolve().parents[2]


def parse_fm(p: Path) -> tuple[dict | None, str | None]:
    """(frontmatter, motif d'illisibilité). Exactement l'un des deux est None.

    **Le motif est retourné, jamais avalé** — c'est le correctif de la remontée 44 du
    lot 4. Cette fonction renvoyait `None` dans les quatre cas ci-dessous sans les
    distinguer, et l'appelant sautait la page : elle disparaissait du total, n'était
    pas validée, son chemin n'était pas confronté à sa `categorie:`. Un `pitch:` non
    quoté contenant « : » suffisait, et sur une brique ou une notion **rien** ne
    l'aurait signalé. Une page qui ne parse pas est une erreur, jamais une absence.
    """
    txt = p.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None, "aucun frontmatter (le fichier ne commence pas par `---`)"
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return None, "frontmatter non refermé (pas de second `---`)"
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        detail = str(e).splitlines()[0].strip()
        return None, (f"YAML invalide — {detail}. Cause la plus fréquente : une valeur "
                      f"non quotée contenant « : » (`pitch:`, `nom:`)")
    if not isinstance(fm, dict):
        return None, (f"frontmatter lu comme {type(fm).__name__}, pas comme un "
                      f"dictionnaire de champs")
    return fm, None


def dossiers_de_pages() -> list[Path]:
    return sorted(d for d in VAULT.iterdir()
                  if d.is_dir() and d.name not in arbo.NON_PAGES)


def main() -> int:
    migrees: list[tuple[Path, str]] = []   # pages descendues dans l'arbre
    legacy = 0                             # pages sous un dossier `arbo.LEGACY`
    hors_arbre = 0                         # pages rangées par `role:`, pas par domaine
    hubs: set[str] = set()

    illisibles: list[str] = []
    for racine in dossiers_de_pages():
        for md in sorted(racine.rglob("*.md")):
            fm, motif = parse_fm(md)
            if fm is None:
                illisibles.append(f"{md.relative_to(VAULT).as_posix()} : "
                                  f"frontmatter illisible — {motif}")
                continue
            rel = md.relative_to(VAULT)
            if fm.get("role") == "hub":
                hubs.add(rel.parent.as_posix())
                continue
            if racine.name in arbo.LEGACY:
                legacy += 1
                continue
            if fm.get("role") in arbo.ROLES_SANS_CATEGORIE:
                hors_arbre += 1
                continue
            migrees.append((rel, str(fm.get("categorie") or ""),
                            str(fm.get("role") or "")))

    ecarts: list[str] = list(illisibles)

    # (2) seuil de promotion — calculé sur la population réelle des pages migrées
    try:
        promus = arbo.promotions([cat for _, cat, role in migrees
                                  if role not in arbo.ROLES_HORS_SEUIL])
    except KeyError as e:
        print(f"[FAIL] {e}")
        return 1

    # (1) concordance chemin / catégorie
    for rel, cat, _role in migrees:
        attendu = arbo.dossier_attendu(cat, promus)
        if attendu is None:
            ecarts.append(f"{rel.as_posix()} : `categorie: {cat or '(vide)'}` hors "
                          f"des 20 préfixes de DOM_LABEL — domaine indérivable")
            continue
        if rel.parent.as_posix() != attendu:
            ecarts.append(f"{rel.as_posix()} : `categorie: {cat}` attend "
                          f"`{attendu}/` — git mv à faire")

    # (3) un hub par dossier de l'arbre
    dossiers = {rel.parent.as_posix() for rel, _, _ in migrees}
    for d in sorted(dossiers):
        # tout niveau du chemin doit porter son hub, pas seulement la feuille
        parts = d.split("/")
        for i in range(1, len(parts) + 1):
            niveau = "/".join(parts[:i])
            if niveau not in hubs:
                ecarts.append(f"{niveau}/ : aucune page `role: hub` à son nom")

    par_dom: dict[str, int] = collections.Counter(
        rel.parts[0] for rel, _, _ in migrees)
    reste = (f"{legacy} page(s) encore sous {sorted(arbo.LEGACY)}, "
             if arbo.LEGACY else "")
    print(f"check_arbo : {len(migrees)} page(s) migrée(s) dans "
          f"{len(par_dom)} domaine(s) — {reste}{hors_arbre} rangée(s) par `role:` "
          f"({', '.join(sorted(arbo.ROLES_SANS_CATEGORIE))})")
    for dom, n in sorted(par_dom.items()):
        print(f"  {dom}/ — {n} page(s)")
    if ecarts:
        print(f"\n{len(ecarts)} écart(s) :")
        for e in sorted(set(ecarts)):
            print(f"  [FAIL] {e}")
        return 1
    print("OK — chemin et catégorie concordent partout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
