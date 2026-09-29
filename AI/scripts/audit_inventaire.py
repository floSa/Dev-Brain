# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""audit_inventaire.py — l'inventaire du vault est-il fidèle à ce qu'il dit de lui-même ?

    uv run AI/scripts/audit_inventaire.py             # verdict + tableau des écarts
    uv run AI/scripts/audit_inventaire.py --json      # même contenu, lisible par une machine
    uv run AI/scripts/audit_inventaire.py --racine X  # auditer une copie du vault

Lecture seule, sans réseau, déterministe, ~1 s. **Pas de `--fix`** : un écart se
corrige en relançant les générateurs (artefacts) ou à la main (prose) — jamais ici.

Sortie : un verdict en une ligne, puis une ligne par écart.
Code : 0 conforme · 1 au moins un écart · 2 aucun écart mais un contrôle sauté (SKIP).
Un écart l'emporte sur un SKIP : si les deux existent, le code est 1.

# Ce que ce script contrôle — et ce qu'il laisse au validateur

`check_brain.py` juge le CONTENU des pages (champs, corps, liens, tailles). Ce script
juge l'INVENTAIRE : ce que les artefacts et la prose DISENT du vault, contre ce que
le disque contient. Il ne répète aucune règle du validateur.

  N1  index ↔ fichiers   pages absentes de l'index, pages fantômes, champs divergents
                         (nom, role, categorie, pitch, tags). Le périmètre vient de
                         `brain.yml` (`genere.non_pages`) : tout dossier de la racine
                         qui n'est pas de l'outillage porte des pages.
  N2  artefacts dérivés  les trois en-têtes « N pages actives » (json, md, liens.md) ;
                         chaque zone AUTO de hub contre le contenu réel du dossier
                         (ENSEMBLES de liens — l'ordre est l'affaire du générateur) ;
                         les quatre générateurs en `--check` si le kit est trouvable,
                         sinon « SKIP : kit introuvable ».
  N3  prose chiffrée     les nombres de Home.md, CLAUDE.md et taxonomie.md.

# Ce que N3 NE regarde PAS (choix écrit, pas oubli)

Les chiffres datés d'un passé révolu — « 336 fiches Dev », « le domaine passe de 7
à 20 pages », « 37 notions descendues » — sont de l'histoire, pas un état : les
« corriger » les ferait mentir. N3 ne contrôle que des affirmations au présent, que
la liste `_assertions_*` nomme une à une. Une affirmation absente de cette liste
n'est pas contrôlée : l'ajouter, c'est ajouter une fonction ici.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent.parent
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

# Les rôles qu'un dossier de domaine ne range pas, mais qui ont un dossier à la racine.
HORS_DOMAINE = {"Métiers", "Patterns", "Rules", "Comparatifs"}
GENERATEURS = ["build_index.py", "build_mocs.py", "build_links.py", "build_bandeau.py",
               "build_carte.py"]


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


# ------------------------------------------------------------------ constats
class Constats:
    def __init__(self) -> None:
        self.ecarts: list[dict] = []
        self.skips: list[dict] = []

    def ecart(self, niveau: str, cible: str, objet: str, annonce, mesure) -> None:
        self.ecarts.append({"niveau": niveau, "cible": cible, "objet": objet,
                            "annonce": str(annonce), "mesure": str(mesure)})

    def skip(self, niveau: str, objet: str, motif: str) -> None:
        self.skips.append({"niveau": niveau, "objet": objet, "motif": motif})


# --------------------------------------------------------------- lecture disque
def frontmatter(texte: str) -> dict | None:
    if not texte.startswith("---"):
        return None
    fin = texte.find("\n---", 3)
    if fin < 0:
        return None
    try:
        d = yaml.load(texte[3:fin], Loader=LOADER)
    except yaml.YAMLError:
        return None
    return d if isinstance(d, dict) else None


def lire_manifeste(racine: Path) -> dict:
    return yaml.load((racine / "brain.yml").read_text(encoding="utf-8"), Loader=LOADER)


def dossiers_de_pages(racine: Path, non_pages: set[str]) -> list[str]:
    return sorted(d.name for d in racine.iterdir()
                  if d.is_dir() and not d.name.startswith(".") and d.name not in non_pages)


def pages_disque(racine: Path, dossiers: list[str]) -> dict[str, dict]:
    """chemin relatif posix -> {fm, texte}. Une page sans frontmatter lisible reste listée."""
    out: dict[str, dict] = {}
    for d in dossiers:
        for p in sorted((racine / d).rglob("*.md")):
            texte = p.read_text(encoding="utf-8")
            out[p.relative_to(racine).as_posix()] = {"fm": frontmatter(texte) or {}, "texte": texte}
    return out


def norm_pitch(v) -> str:
    return " ".join(str(v).split()) if v else ""


def norm_liste(v) -> list[str]:
    return sorted(str(x) for x in (v or []))


# ------------------------------------------------------------------------- N1
def n1(c: Constats, disque: dict, index: dict) -> None:
    par_chemin = {p["path"]: p for p in index["pages"]}
    for chemin in sorted(set(disque) - set(par_chemin)):
        c.ecart("N1", chemin, "page non indexée", "absente de brain-index.json", "présente sur disque")
    for chemin in sorted(set(par_chemin) - set(disque)):
        c.ecart("N1", chemin, "page fantôme", "présente dans brain-index.json", "absente du disque")
    for chemin in sorted(set(disque) & set(par_chemin)):
        fm, ix = disque[chemin]["fm"], par_chemin[chemin]
        nom_fm = fm.get("nom") or Path(chemin).stem
        paires = {
            "nom": (nom_fm, ix.get("nom")),
            "role": (fm.get("role"), ix.get("role")),
            "categorie": (fm.get("categorie"), ix.get("categorie")),
            "pitch": (norm_pitch(fm.get("pitch")), norm_pitch(ix.get("pitch"))),
            "tags": (norm_liste(fm.get("tags")), norm_liste(ix.get("tags"))),
        }
        for champ, (a, b) in paires.items():
            if (a or None) != (b or None):
                c.ecart("N1", chemin, f"champ {champ}", f"index : {str(b)[:60]}", f"frontmatter : {str(a)[:60]}")


# ------------------------------------------------------------------------- N2
def liens(bloc: str) -> list[str]:
    return [nfc(m.split("|")[0].split("#")[0].strip()) for m in re.findall(r"\[\[([^\]]+)\]\]", bloc)]


def zone_auto(texte: str) -> str | None:
    m = re.search(r"<!-- AUTO:START -->(.*?)<!-- AUTO:END -->", texte, re.S)
    return m.group(1) if m else None


def sections(zone: str) -> dict[str, str]:
    """`### Titre` -> corps, dans la zone AUTO."""
    out: dict[str, str] = {}
    morceaux = re.split(r"^### +(.+?)\s*$", zone, flags=re.M)
    for i in range(1, len(morceaux), 2):
        out[morceaux[i].strip()] = morceaux[i + 1]
    return out


def n2_entetes(c: Constats, racine: Path, index: dict, n_disque: int) -> None:
    mesures = {"brain-index.json : clé count": index.get("count"),
               "brain-index.json : len(pages)": len(index["pages"])}
    for nom in ("brain-index.md", "liens.md"):
        tete = (racine / "AI/index" / nom).read_text(encoding="utf-8")[:600]
        m = re.search(r"(\d+) pages actives", tete)
        mesures[nom] = int(m.group(1)) if m else None
    for objet, v in mesures.items():
        if v != n_disque:
            c.ecart("N2", f"AI/index/{objet.split(' ')[0]}", f"compte de pages ({objet})", v, n_disque)


def enfants_directs(disque: dict, dossier: str) -> list[tuple[str, dict]]:
    pre = dossier + "/"
    return [(ch, d) for ch, d in disque.items()
            if ch.startswith(pre) and "/" not in ch[len(pre):]]


def n2_zones(c: Constats, racine: Path, disque: dict) -> int:
    n = 0
    for chemin, d in disque.items():
        if d["fm"].get("role") != "hub":
            continue
        dossier = str(Path(chemin).parent.as_posix())
        zone = zone_auto(d["texte"])
        if zone is None:
            c.ecart("N2", chemin, "zone AUTO", "balises attendues", "absentes")
            continue
        n += 1
        reel: dict[str, set[str]] | None = None
        premier = dossier.split("/")[0]
        if premier == "Métiers":
            continue  # traité à part (n2_metiers)
        if dossier == "Comparatifs":
            attendu = {nfc(Path(ch).stem) for ch, x in disque.items() if x["fm"].get("role") == "comparatif"}
            vu = set(liens(zone))
            for lien in sorted(attendu - vu):
                c.ecart("N2", chemin, "zone AUTO : comparatif manquant", "absent de la zone", lien)
            for lien in sorted(vu - attendu):
                c.ecart("N2", chemin, "zone AUTO : lien en trop", lien, "aucun comparatif de ce nom")
            continue
        directs = enfants_directs(disque, dossier)
        reel = {
            "Sous-domaines": {nfc(s.name) for s in (racine / dossier).iterdir()
                              if s.is_dir() and (s / f"{s.name}.md").exists()},
            "Notions": {nfc(Path(ch).stem) for ch, x in directs if x["fm"].get("role") == "notion"},
            "Briques": {nfc(Path(ch).stem) for ch, x in directs if x["fm"].get("role") == "brique"},
            "Patterns": {nfc(Path(ch).stem) for ch, x in directs if x["fm"].get("role") == "pattern"},
            "Rules": {nfc(Path(ch).stem) for ch, x in directs if x["fm"].get("role") == "rule"},
            "Comparatifs": {nfc(p.stem) for p in (racine / dossier).glob("*.base")},
        }
        vus = {t: set(liens(corps)) for t, corps in sections(zone).items()}
        for titre, attendu in reel.items():
            vu = vus.get(titre, set())
            for lien in sorted(attendu - vu):
                c.ecart("N2", chemin, f"zone AUTO « {titre} » : manquant", "absent de la zone", lien)
            for lien in sorted(vu - attendu):
                c.ecart("N2", chemin, f"zone AUTO « {titre} » : en trop", lien, "pas dans le dossier")
        for titre in sorted(set(vus) - set(reel)):
            c.ecart("N2", chemin, f"zone AUTO : section inconnue « {titre} »", titre, "aucun générateur")
    return n


def n2_metiers(c: Constats, disque: dict) -> None:
    """Hub transverse : une puce « [[Domaine]] — N page(s) » par domaine.

    N = briques et notions du domaine qui portent la clé dans `domaines:`. Les hubs ne
    comptent pas (mesuré : 69 = 56 notions + 13 briques pour ai-eng dans « LLM & IA
    générative » ; avec les hubs on trouve 82). Un critère deviné faisait 30 faux écarts.
    """
    for chemin, d in disque.items():
        if not chemin.startswith("Métiers/") or d["fm"].get("role") != "hub":
            continue
        zone = zone_auto(d["texte"]) or ""
        m = re.search(r"\(`([\w-]+)`\)", zone)
        if not m:
            c.ecart("N2", chemin, "zone AUTO Métiers", "clé de métier entre parenthèses", "introuvable")
            continue
        cle = m.group(1)
        for dom, n in re.findall(r"^- \[\[(.+?)\]\] — (\d+) page", zone, flags=re.M):
            reel = sum(1 for ch, x in disque.items()
                       if ch.startswith(nfc(dom) + "/") and x["fm"].get("role") in ("brique", "notion")
                       and cle in (x["fm"].get("domaines") or []))
            if reel != int(n):
                c.ecart("N2", chemin, f"zone AUTO : {dom}", f"{n} page(s)", f"{reel} page(s) (briques+notions) portant `{cle}`")


def trouver_kit(racine: Path) -> Path | None:
    """Même ordre que `_pont_kit.py` : $BRAINKIT_RACINE, AI/scripts/brainkit/, voisinage."""
    env = os.environ.get("BRAINKIT_RACINE")
    if env and (Path(env) / "brainkit/__init__.py").exists():
        return Path(env)
    if (racine / "AI/scripts/brainkit/__init__.py").exists():
        return racine / "AI/scripts/brainkit"
    for parent in racine.parents:
        if (parent / "BrainKit/brainkit/__init__.py").exists():
            return parent / "BrainKit"
    return None


def n2_generateurs(c: Constats, racine: Path) -> None:
    if trouver_kit(racine) is None:
        c.skip("N2", "générateurs --check", "kit introuvable ($BRAINKIT_RACINE, AI/scripts/brainkit/, <parent>/BrainKit)")
        return
    for g in GENERATEURS:
        r = subprocess.run([sys.executable, str(racine / "AI/scripts" / g), "--check"],
                           capture_output=True, text=True, cwd=racine, timeout=120)
        if r.returncode == 2:
            c.ecart("N2", f"AI/scripts/{g}", "générateur --check", "code 0", "code 2 (écart)")
        elif r.returncode != 0:
            c.ecart("N2", f"AI/scripts/{g}", "générateur --check", "code 0", f"code {r.returncode} (erreur)")


# ------------------------------------------------------------------------- N3
def valeurs_domaine(taxo: str) -> tuple[int, int, int]:
    """(valeurs du bloc ```domaine, préfixes, valeurs sous skill/*)."""
    m = re.search(r"^```domaine\n(.*?)^```", taxo, re.S | re.M)
    bloc = m.group(1) if m else ""
    groupes = re.findall(r"(\w+)/\{([^}]*)\}", bloc)
    n = sum(len([v for v in vals.split(",") if v.strip()]) for _, vals in groupes)
    s = re.search(r"skill/\{([^}]*)\}", taxo)
    return n, len(groupes), len([v for v in (s.group(1) if s else "").split(",") if v.strip()])


def valeurs_famille(taxo: str) -> int:
    m = re.search(r"^```famille\n(.*?)^```", taxo, re.S | re.M)
    return len([ligne for ligne in (m.group(1) if m else "").splitlines() if ligne.strip()])


def mesures_vault(racine: Path, dossiers: list[str], disque: dict) -> dict:
    def n(role: str, prefixe: str = "") -> int:
        return sum(1 for ch, d in disque.items() if d["fm"].get("role") == role and ch.startswith(prefixe))
    domaines = [d for d in dossiers if d not in HORS_DOMAINE]
    return {
        "briques": n("brique"), "notions": n("notion"), "comparatifs": n("comparatif"),
        "patterns": n("pattern"), "rules": n("rule"), "hubs": n("hub"),
        "domaines": domaines, "roles": len({d["fm"].get("role") for d in disque.values()} - {None}),
        "briques_par": {d: n("brique", d + "/") for d in domaines},
        "notions_par": {d: n("notion", d + "/") for d in domaines},
        "sous_par": {d: {nfc(s.name) for s in (racine / d).iterdir()
                         if s.is_dir() and (s / f"{s.name}.md").exists()} for d in domaines},
        "metiers": sum(1 for ch, d in disque.items() if ch.startswith("Métiers/") and d["fm"].get("role") == "hub"),
    }


def a_plat(texte: str) -> tuple[str, list[int]]:
    """Texte sans retours ni « > », et la position où commence chaque ligne d'origine."""
    morceaux, debuts, pos = [], [], 0
    for ligne in texte.splitlines():
        debuts.append(pos)
        morceau = ligne.lstrip("> ").rstrip() + " "
        morceaux.append(morceau)
        pos += len(morceau)
    return "".join(morceaux), debuts


def n3(c: Constats, racine: Path, mes: dict) -> None:
    def cmp(src: str, ligne: int | str, objet: str, annonce: int, mesure: int) -> None:
        if int(annonce) != int(mesure):
            c.ecart("N3", f"{src}:{ligne}", objet, annonce, mesure)

    def ligne_de(texte: str, motif: str) -> int:
        i = texte.find(motif)
        return texte.count("\n", 0, i) + 1 if i >= 0 else 0

    # ---- Home.md
    home = (racine / "Home.md").read_text(encoding="utf-8")
    vus = set()
    for i, l in enumerate(home.splitlines(), 1):
        m = re.match(r"^- \[\[(.+?)\]\] — (\d+) briques?(?:, (\d+) sous-domaines?)?(?: : (.*))?$", l)
        if m:
            dom = nfc(m.group(1))
            if dom not in mes["briques_par"]:
                c.ecart("N3", f"Home.md:{i}", "domaine cité", dom, "aucun dossier de ce nom")
                continue
            vus.add(dom)
            cmp("Home.md", i, f"{dom} : briques", m.group(2), mes["briques_par"][dom])
            reel = mes["sous_par"][dom]
            if m.group(3) is not None:
                cmp("Home.md", i, f"{dom} : sous-domaines (nombre)", m.group(3), len(reel))
            elif reel:
                c.ecart("N3", f"Home.md:{i}", f"{dom} : sous-domaines", "aucun annoncé", f"{len(reel)} dossiers promus")
            if m.group(4) is not None:
                cites = set(liens(m.group(4)))
                for s in sorted(reel - cites):
                    c.ecart("N3", f"Home.md:{i}", f"{dom} : sous-domaine non cité", "absent de la ligne", s)
                for s in sorted(cites - reel):
                    c.ecart("N3", f"Home.md:{i}", f"{dom} : sous-domaine cité en trop", s, "aucun dossier promu")
        for motif, cle, objet in ((r"\[\[Patterns\]\] — (\d+) architectures", "patterns", "Patterns"),
                                  (r"\[\[Rules\]\] — (\d+) règles", "rules", "Rules"),
                                  (r"\[\[Comparatifs\]\] — (\d+) comparatifs", "comparatifs", "Comparatifs")):
            m = re.search(motif, l)
            if m:
                cmp("Home.md", i, f"{objet} : nombre", m.group(1), mes[cle])
    for dom in sorted(set(mes["domaines"]) - vus):
        c.ecart("N3", "Home.md", "domaine non cité", "absent de Home.md", dom)

    # ---- CLAUDE.md (texte mis à plat : les phrases coupent sur les « > » et les retours)
    brut = (racine / "CLAUDE.md").read_text(encoding="utf-8")
    plat, debuts = a_plat(brut)

    def ligne(pos: int) -> int:
        return bisect_right(debuts, pos)

    m = re.search(r"Les (\d+) briques, les \*\*(\d+) notions\*\*, les (\d+) comparatifs(?: \([^)]*\))?, les (\d+) patterns et les (\d+) règles", plat)
    if m:
        ln = ligne(m.start())
        for v, cle in zip(m.groups(), ("briques", "notions", "comparatifs", "patterns", "rules")):
            cmp("CLAUDE.md", ln, f"inventaire : {cle}", v, mes[cle])
    else:
        c.ecart("N3", "CLAUDE.md", "phrase d'inventaire", "« Les N briques, les N notions… »", "introuvable")
    for motif, cle, objet in ((r"Les (\d+) fiches sont au nouveau gabarit", "briques", "fiches au gabarit"),
                              (r"les (\d+) comparatifs, eux, restent", "comparatifs", "comparatifs rangés"),
                              (r"les (\d+) comparatifs sont des pages", "comparatifs", "comparatifs en pages"),
                              (r"les (\d+) pages `role: comparatif`", "comparatifs", "pages comparatif"),
                              (r"(\d+) hubs transverses", "metiers", "hubs Métiers")):
        for mm in re.finditer(motif, plat):
            cmp("CLAUDE.md", ligne(mm.start()), objet, mm.group(1), mes[cle])
    for mm in re.finditer(r"l'arbre des (\d+) domaines", plat):
        cmp("CLAUDE.md", ligne(mm.start()), "domaines", mm.group(1), len(mes["domaines"]))
    taxo = (racine / "Documentation/general/taxonomie.md").read_text(encoding="utf-8")
    n_val, n_pref, n_skill = valeurs_domaine(taxo)
    mm = re.search(r"(\d+) valeurs en (\d+) préfixes", plat)
    if mm:
        ln = ligne(mm.start())
        cmp("CLAUDE.md", ln, "valeurs de categorie (bloc domaine)", mm.group(1), n_val)
        cmp("CLAUDE.md", ln, "préfixes de categorie", mm.group(2), n_pref)
    mm = re.search(r"« Machine Learning/ » \(\d+\).*?(?=\n\n|\Z)", brut, re.S)
    if mm:
        ln = brut.count("\n", 0, mm.start()) + 1
        annonce = {nfc(d): int(n) for d, n in re.findall(r"« (.+?)/ » \((\d+)\)", mm.group(0))}
        for dom, n in annonce.items():
            if dom not in mes["notions_par"]:
                c.ecart("N3", f"CLAUDE.md:{ln}", "notions par domaine", dom, "aucun dossier de ce nom")
            else:
                cmp("CLAUDE.md", ln, f"notions de {dom}", n, mes["notions_par"][dom])
        for dom, n in mes["notions_par"].items():
            if n and dom not in annonce:
                c.ecart("N3", f"CLAUDE.md:{ln}", f"notions de {dom}", "domaine non cité", n)

    # ---- taxonomie.md
    nom = "Documentation/general/taxonomie.md"
    mm = re.search(r"(\d+) valeurs sous le bloc `domaine`, plus (\d+) sous `skill/\*`", taxo)
    if mm:
        ln = ligne_de(taxo, mm.group(0)[:20])
        cmp(nom, ln, "valeurs du bloc domaine", mm.group(1), n_val)
        cmp(nom, ln, "valeurs skill/*", mm.group(2), n_skill)
    mm = re.search(r"le domaine \((\d+) valeurs, (\d+) préfixes de tête\)", taxo)
    if mm:
        ln = ligne_de(taxo, mm.group(0))
        cmp(nom, ln, "valeurs du bloc domaine (titre)", mm.group(1), n_val)
        cmp(nom, ln, "préfixes de tête (titre)", mm.group(2), n_pref)
    for motif, mesure, objet in ((r"\| (\d+) valeurs, cf\. section \*Axe `famille:`", valeurs_famille(taxo), "valeurs de famille (tableau)"),
                                 (r"Axe `famille:` — la nature de la brique \((\d+) valeurs", valeurs_famille(taxo), "valeurs de famille (titre)"),
                                 (r"### Les (\d+) valeurs, définition", valeurs_famille(taxo), "valeurs de famille (définitions)"),
                                 (r"Axe `role:` — la nature éditoriale de la page \((\d+) valeurs", mes["roles"], "valeurs de role")):
        mm = re.search(motif, taxo)
        if mm:
            cmp(nom, ligne_de(taxo, mm.group(0)[:25]), objet, mm.group(1), mesure)


# ---------------------------------------------------------------------- sortie
def rendre(c: Constats, n_pages: int, n_zones: int, kit: str) -> tuple[str, list[str]]:
    par = {n: sum(1 for e in c.ecarts if e["niveau"] == n) for n in ("N1", "N2", "N3")}
    detail = f"N1 {par['N1']} · N2 {par['N2']} · N3 {par['N3']}"
    skip = f" · {len(c.skips)} SKIP" if c.skips else ""
    base = f"{n_pages} pages, {n_zones} zones AUTO, kit : {kit}"
    if c.ecarts:
        verdict = f"ÉCART — {len(c.ecarts)} écart(s) ({detail}){skip} — {base}"
    elif c.skips:
        verdict = f"CONFORME SOUS RÉSERVE — aucun écart, {len(c.skips)} contrôle(s) sauté(s) — {base}"
    else:
        verdict = f"CONFORME — aucun écart — {base}"
    lignes = [f"{e['niveau']} | {e['cible']} | {e['objet']} | annoncé : {e['annonce']} | mesuré : {e['mesure']}"
              for e in c.ecarts]
    lignes += [f"SKIP : {s['objet']} — {s['motif']}" for s in c.skips]
    return verdict, lignes


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Audit de l'inventaire du vault (lecture seule).")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--racine", type=Path, default=VAULT, help="racine du vault à auditer")
    ap.add_argument("--max", type=int, default=50, help="lignes d'écart imprimées (le reste : --json)")
    ns = ap.parse_args()
    racine = ns.racine.resolve()

    c = Constats()
    manifeste = lire_manifeste(racine)
    non_pages = set(manifeste["genere"]["non_pages"])
    dossiers = dossiers_de_pages(racine, non_pages)
    disque = pages_disque(racine, dossiers)
    index = json.loads((racine / "AI/index/brain-index.json").read_text(encoding="utf-8"))

    n1(c, disque, index)
    n2_entetes(c, racine, index, len(disque))
    n_zones = n2_zones(c, racine, disque)
    n2_metiers(c, disque)
    n2_generateurs(c, racine)
    n3(c, racine, mesures_vault(racine, dossiers, disque))

    kit = trouver_kit(racine)
    verdict, lignes = rendre(c, len(disque), n_zones, str(kit) if kit else "introuvable")
    code = 1 if c.ecarts else (2 if c.skips else 0)
    if ns.json:
        print(json.dumps({"verdict": verdict, "code": code, "pages": len(disque), "zones_auto": n_zones,
                          "ecarts": c.ecarts, "skips": c.skips}, ensure_ascii=False, indent=2))
        return code
    print(verdict)
    for ligne in lignes[:ns.max]:
        print(ligne)
    if len(lignes) > ns.max:
        print(f"… {len(lignes) - ns.max} ligne(s) de plus — voir --json")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
