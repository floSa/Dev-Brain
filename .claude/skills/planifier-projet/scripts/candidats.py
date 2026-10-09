#!/usr/bin/env python3
"""candidats.py — interroge le DevBrain pour un cadrage de projet, à bas coût.

Lit `AI/index/brain-index.json` (jamais en entier dans le contexte de l'agent),
puis ouvre seulement l'en-tête des pages candidates pour lire ce que l'index ne
porte pas : `licence_type`, `hosted`, `url_repo`. Sortie courte, une ligne par page.
Bibliothèque standard seulement. Aucune écriture.

Où est le DevBrain : `--vault`, sinon la variable DEVBRAIN_PATH, sinon le dossier
parent du skill s'il est dans le vault, sinon ~/Projets/DevBrain.

    candidats.py domaines
    candidats.py besoin --categorie database/vecteur --commercial non --sur-site
    candidats.py comparatif --categorie database/vecteur
    candidats.py regles --mot python
    candidats.py usage Qdrant
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


def trouve_vault(arg: str | None) -> Path:
    essais = [arg, os.environ.get("DEVBRAIN_PATH")]
    ici = Path(__file__).resolve()
    for parent in ici.parents:
        if (parent / "AI" / "index" / "brain-index.json").exists():
            essais.append(str(parent))
            break
    essais.append(str(Path.home() / "Projets" / "DevBrain"))
    for e in essais:
        if e and (Path(e) / "AI" / "index" / "brain-index.json").exists():
            return Path(e)
    sys.exit("DevBrain introuvable. Donner --vault ou définir DEVBRAIN_PATH.")


def charge_index(vault: Path) -> list[dict]:
    return json.loads((vault / "AI" / "index" / "brain-index.json").read_text(encoding="utf-8"))["pages"]


def en_tete(vault: Path, chemin: str) -> dict:
    """Champs simples du frontmatter. Ne lit que les 45 premières lignes."""
    champs: dict = {}
    try:
        with open(vault / chemin, encoding="utf-8") as f:
            for i, ligne in enumerate(f):
                if i == 0:
                    continue
                if ligne.strip() == "---" or i > 45:
                    break
                m = re.match(r"^([a-z_]+):\s*(.*)$", ligne.rstrip())
                if m:
                    champs[m.group(1)] = m.group(2).strip().strip('"')
    except OSError:
        pass
    return champs


def liste(valeur: str) -> list[str]:
    return [x.strip().strip('"\'') for x in valeur.strip("[]").split(",") if x.strip()]


RESTREINTE = re.compile(r"\b(AGPL|SSPL|BUSL|Commons Clause|GPL)\b", re.I)


def usage_projets(vault: Path, nom: str) -> int:
    """Combien de pages du journal de projets citent ce nom. 0 si le journal est vide."""
    dossier = vault / "Projects"
    if not dossier.exists():
        return 0
    cible = f"[[{nom}"
    n = 0
    for p in dossier.rglob("*.md"):
        if "_archive" in p.parts:
            continue
        try:
            if cible in p.read_text(encoding="utf-8"):
                n += 1
        except OSError:
            pass
    return n


def cmd_domaines(vault: Path, pages: list[dict], _a) -> None:
    from collections import Counter
    c = Counter(p.get("categorie") for p in pages if p.get("role") == "brique" and p.get("categorie"))
    for cat, n in sorted(c.items()):
        print(f"{cat}\t{n}")


def accepte(champs: dict, p: dict, a) -> tuple[bool, str]:
    lic = champs.get("licence_type", "")
    hebergement = liste(champs.get("hosted", "")) if champs.get("hosted") else []
    note = []
    if a.commercial == "oui":
        if lic in ("proprietary", "source-available"):
            return False, ""
        if lic == "open-core":
            note.append("open-core : vérifier l'édition libre")
        if RESTREINTE.search(p.get("pitch") or "") or RESTREINTE.search(champs.get("pitch", "")):
            note.append("licence à copyleft ou restreinte : lire avant de livrer")
    else:
        if lic == "proprietary":
            note.append("fermé : vérifier qu'il est gratuit")
        if lic == "source-available":
            note.append("code visible, usage commercial limité")
    if a.sur_site:
        if p.get("famille") == "saas":
            return False, ""
        if hebergement == ["managed"]:
            return False, ""
    return True, " ; ".join(note)


def cmd_besoin(vault: Path, pages: list[dict], a) -> None:
    exclus = {x.strip().lower() for x in (a.exclure or "").split(",") if x.strip()}
    gardes, deprecies = [], []
    for p in pages:
        if p.get("role") != "brique":
            continue
        if a.categorie and not (p.get("categorie") or "").startswith(a.categorie):
            continue
        if a.tag and a.tag not in (p.get("tags") or []):
            continue
        if a.famille and p.get("famille") != a.famille:
            continue
        if a.langage and str(p.get("langage") or "").lower() != a.langage.lower():
            continue
        if str(p.get("nom", "")).lower() in exclus:
            continue
        if p.get("maturite") == "deprecated":
            deprecies.append(p["nom"])
            continue
        champs = en_tete(vault, p["path"])
        ok, note = accepte(champs, p, a)
        if not ok:
            continue
        gardes.append((p, champs, note))
    rang = {"production": 0, "beta": 1, "experimental": 2, None: 3}
    # Ordre : d'abord ce que le journal de projets a déjà utilisé, puis la maturité, puis le nom.
    # Pas de classement par popularité : le jugement vient du comparatif et du cadrage.
    gardes.sort(key=lambda t: (-usage_projets(vault, t[0]["nom"]), rang.get(t[0].get("maturite"), 3),
                               t[0]["nom"].lower()))
    total = len(gardes)
    if a.json:
        out = [{"nom": p["nom"], "famille": p.get("famille"), "langage": p.get("langage"),
                "maturite": p.get("maturite"), "licence": c.get("licence_type"), "hebergement": c.get("hosted"),
                "note": n, "pitch": p.get("pitch"), "page": p["path"], "depot": c.get("url_repo"),
                "projets": usage_projets(vault, p["nom"])} for p, c, n in gardes[: a.max]]
        print(json.dumps({"total": total, "candidats": out, "dépréciés": deprecies}, ensure_ascii=False, indent=1))
        return
    print(f"{total} candidat(s) — {min(total, a.max)} affiché(s)")
    for p, c, n in gardes[: a.max]:
        pitch = (p.get("pitch") or "").replace("\n", " ")
        pitch = pitch if len(pitch) <= 150 else pitch[:150].rsplit(" ", 1)[0] + " …"
        u = usage_projets(vault, p["nom"])
        print(f"- {p['nom']} | {p.get('famille')} {p.get('langage') or ''} | {p.get('maturite')} | "
              f"{c.get('licence_type', '?')} | héb. {c.get('hosted', 'n/a')}"
              + (f" | projets {u}" if u else "") + (f" | ! {n}" if n else "")
              + f"\n  {pitch}\n  page: {p['path']}")
    if total > a.max:
        print("Autres, non affichés : " + ", ".join(p["nom"] for p, _, _ in gardes[a.max:]))
    if deprecies:
        print("Écartés (dépréciés) : " + ", ".join(deprecies))


def cmd_comparatif(vault: Path, pages: list[dict], a) -> None:
    trouves = []
    for p in pages:
        if p.get("role") != "comparatif":
            continue
        cat = p.get("categorie") or ""
        if a.categorie and not cat.startswith(a.categorie) and a.categorie not in p["path"]:
            continue
        trouves.append(p)
    if not trouves:
        print("Aucun comparatif pour ce domaine.")
        return
    for p in trouves:
        print(f"- {p['nom']} | page: {p['path']}")


def cmd_regles(vault: Path, pages: list[dict], a) -> None:
    mot = (a.mot or "").lower()
    for p in pages:
        if p.get("role") not in ("rule", "pattern"):
            continue
        texte = " ".join([str(p.get("nom", "")), str(p.get("pitch", "")), " ".join(p.get("tags") or [])]).lower()
        if mot and mot not in texte:
            continue
        print(f"- [{p['role']}] {p['nom']} | page: {p['path']}")


def cmd_usage(vault: Path, pages: list[dict], a) -> None:
    print(usage_projets(vault, a.nom))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("domaines")
    b = sub.add_parser("besoin")
    b.add_argument("--categorie", help="préfixe de categorie:, ex. database/vecteur ou llm")
    b.add_argument("--tag")
    b.add_argument("--famille")
    b.add_argument("--langage")
    b.add_argument("--commercial", choices=["oui", "non"], default="non",
                   help="oui : le produit sera vendu ou livré ; écarte les licences restrictives")
    b.add_argument("--sur-site", action="store_true", help="écarte les services cloud seulement")
    b.add_argument("--exclure", help="noms à ne pas proposer, séparés par des virgules")
    b.add_argument("--max", type=int, default=8)
    b.add_argument("--json", action="store_true")
    c = sub.add_parser("comparatif")
    c.add_argument("--categorie")
    r = sub.add_parser("regles")
    r.add_argument("--mot")
    u = sub.add_parser("usage")
    u.add_argument("nom")
    a = ap.parse_args()
    vault = trouve_vault(a.vault)
    pages = charge_index(vault)
    {"domaines": cmd_domaines, "besoin": cmd_besoin, "comparatif": cmd_comparatif,
     "regles": cmd_regles, "usage": cmd_usage}[a.cmd](vault, pages, a)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
