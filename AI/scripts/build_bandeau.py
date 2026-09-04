# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_bandeau.py — compose le bandeau de haut de page des `role: brique`.

Le panneau natif d'Obsidian est masqué (lot 0) : dix-huit propriétés rendues avant
le titre poussaient `## Définition` sous la ligne de flottaison. Le lecteur a besoin
de quatre faits, la machine des dix-huit. Ce script rend les quatre — Nature,
Licence, Exécution, Maturité — dans une zone AUTO du corps, le frontmatter restant
intact pour l'index et le validateur. Cf. AI/design/brain-v3.md §5 et §6.

TOUT le contenu du bandeau est DÉRIVÉ du frontmatter, sans exception : rien à
écrire, rien à tenir à jour, rien à resynchroniser. Une cellule sans source dans le
frontmatter affiche un tiret cadratin — jamais une valeur plausible. C'est la règle
la plus dure du lot 6 : une fiche vide honnêtement vaut mieux qu'une fiche remplie
au jugé.

Idempotent : relancé sur un vault déjà traité, il n'écrit aucun octet. La zone est
délimitée par des balises, jamais éditée à la main, et remplacée en bloc.

Usage :
    uv run AI/scripts/build_bandeau.py                    # tout le vault
    uv run AI/scripts/build_bandeau.py "Bases de données/Vectoriel"
    uv run AI/scripts/build_bandeau.py --check "Bases de données"

Le ou les CHEMINS limitent l'écriture à ce qui vit dessous — fichier ou dossier.
Sans argument, le script traite le vault entier : c'est le mode d'une conversation
d'intégration, pas celui d'une conversation de conversion. Le scope existe parce
que le lot 6 se déroule dossier par dossier : une conversation qui convertit
« Vectoriel/ » n'a aucune raison de réécrire les 322 autres fiches, et un `git
diff` limité à son périmètre est la seule façon de relire son propre travail.

`--check` n'écrit rien et sort en code 2 s'il reste un bandeau absent ou périmé.
C'est la forme vérifiable de la règle 9 de la spec (« le bandeau généré concorde
avec le frontmatter »), utilisable en clôture.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/build_bandeau.py")

VAULT = Path(__file__).resolve().parents[2]

# Même énumération par la négative que build_index.py : tout dossier de la racine
# qui n'est pas de l'outillage porte des pages. `Templates/` en est exclu et doit
# le rester — ses deux `role: brique` sont des GABARITS, pas des fiches : leur
# frontmatter est un exemple à trous, dont le bandeau dérivé n'aurait aucun sens.
# L'exclusion vaut même sous un scope explicite, pour la même raison.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}

START = "<!-- AUTO:BANDEAU:START -->"
END = "<!-- AUTO:BANDEAU:END -->"
# Balises propres au bandeau : `build_mocs.py` possède déjà `<!-- AUTO:START -->`
# dans les hubs, et deux zones AUTO homonymes dans le même vault finiraient par se
# marcher dessus le jour où un script balaiera les deux rôles.
ZONE_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
H1_RE = re.compile(r"^# .+$", re.M)
VIDE = "—"

# --- Nature : `famille:` donne le mot, `langage:` le qualifie -------------------
# L'énumération est celle du bloc ```famille de Documentation/general/taxonomie.md,
# fermée et contrôlée en dur par check_brain (R14) : une famille inconnue ici est
# donc un bug de taxonomie, pas un cas à absorber en silence.
NATURE = {
    "paquet": "Librairie",
    "plateforme": "Plateforme",
    "application": "Application",
    "cli": "CLI",
    "saas": "SaaS",
    "extension": "Extension",
    "specification": "Spécification",
    "modele": "Modèle",
    "annuaire": "Annuaire",
}

# --- Licence : rendu français de l'énumération de `licence_type:` ---------------
# Table un pour un, donc réversible : la concordance se vérifie par égalité de
# chaînes, sans interprétation.
LICENCE = {
    "open-source": "open-source",
    "open-core": "open-core",
    "source-available": "source-available",
    "proprietary": "propriétaire",
}

# --- Exécution ------------------------------------------------------------------
# Ce qu'une brique demande pour tourner. Pour les familles qui ne s'hébergent pas,
# la réponse est dans la famille elle-même — c'est précisément ce que R16 a acté en
# supprimant `hosted:` des 177 paquets qui le portaient sans raison.
EXECUTION_FAMILLE = {
    "paquet": "en bibliothèque, rien à héberger",
    "cli": "en ligne de commande, rien à héberger",
    "extension": "dans le moteur hôte, rien à héberger",
    "specification": "rien à exécuter",
    "annuaire": "rien à exécuter",
    "modele": "à charger dans un runtime",
}
# Les trois familles hébergées (R16) lisent `hosted:` puis `scaling:`.
HEBERGEES = {"plateforme", "saas", "application"}
HOSTED = {
    ("self",): "self-hébergé",
    ("managed",): "managé",
    ("managed", "self"): "self-hébergé ou managé",
}
SCALING = {
    "single-node": "mono-nœud",
    "distributed": "distribué",
    "serverless": "serverless",
}


def rel(p: Path) -> str:
    return p.relative_to(VAULT).as_posix()


def parse(text: str) -> dict | None:
    """Frontmatter, ou None si la page n'en porte pas de lisible.

    Le motif n'est pas remonté ici : `check_brain.py` porte déjà cette règle (R17)
    et la traite comme une erreur. Ce script se contente de ne pas toucher une page
    qu'il ne comprend pas — écrire un bandeau dérivé d'un frontmatter à moitié lu
    serait pire que ne rien écrire.
    """
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def cellule(valeur: str | None) -> str:
    """Une cellule vide se voit. `|` est échappé : il couperait la ligne du tableau."""
    v = (valeur or "").strip()
    return v.replace("|", r"\|") if v else VIDE


def nature(fm: dict) -> str:
    """`famille:` donne le mot, `langage:` le qualifie — sauf pour un `saas`.

    Le bandeau répond à trois questions : qu'est-ce que c'est, est-ce que je peux le
    faire tourner, est-ce que c'est mûr. Pour un service qu'on n'exécute jamais
    soi-même, le langage d'implémentation ne fait pas partie de ce que la chose EST :
    « SaaS Rust » occupe une cellule sans rien apprendre au lecteur. L'exception est
    inscrite ici plutôt que devinée — une règle qui produit une cellule inutile n'est
    pas uniforme, elle est seulement inconditionnelle.
    """
    fam_brute = str(fm.get("famille") or "").strip()
    fam = NATURE.get(fam_brute)
    lang = str(fm.get("langage") or "").strip()
    if not fam:
        return VIDE
    if fam_brute == "saas":
        return fam
    return f"{fam} {lang}" if lang else fam


def licence(fm: dict) -> str:
    return LICENCE.get(str(fm.get("licence_type") or "").strip(), VIDE)


def execution(fm: dict) -> str:
    fam = str(fm.get("famille") or "").strip()
    if fam in EXECUTION_FAMILLE:
        return EXECUTION_FAMILLE[fam]
    if fam in HEBERGEES:
        hosted = fm.get("hosted")
        if isinstance(hosted, list) and hosted:
            base = HOSTED.get(tuple(sorted(str(h).strip() for h in hosted)))
            if base:
                sc = SCALING.get(str(fm.get("scaling") or "").strip())
                return f"{base} · {sc}" if sc else base
        # Une application de bureau ne porte pas `hosted:` — elle porte `os:`, et
        # « où ça tourne » est exactement la question à laquelle Exécution répond.
        if fam == "application" and fm.get("os"):
            return str(fm["os"]).strip()
    return VIDE


COLONNES = ("Nature", "Licence", "Exécution", "Maturité")


def cellules(fm: dict) -> list[str]:
    """Les quatre cellules, dans l'ordre des colonnes."""
    return [cellule(nature(fm)), cellule(licence(fm)), cellule(execution(fm)),
            cellule(str(fm.get("maturite") or ""))]


def colonnes_vides(cells: list[str]) -> list[str]:
    """Les colonnes sans source dans le frontmatter.

    Le test porte sur les CELLULES, jamais sur la zone rendue : le tiret cadratin
    est aussi un signe de ponctuation courant, et douze pitchs du domaine en
    portent un. Chercher `—` dans le texte du bandeau signalait onze trous
    inexistants au premier essai.
    """
    return [c for c, v in zip(COLONNES, cells) if v == VIDE]


def bandeau(fm: dict) -> str:
    """La zone AUTO complète : le pitch, puis les quatre faits.

    Le pitch est dans la zone parce qu'il vient lui aussi du frontmatter. L'y
    laisser dehors aurait créé la seule chose que la v3 cherche à supprimer : une
    valeur recopiée à deux endroits, dont l'un se périme sans que rien le dise.
    """
    pitch = " ".join(str(fm.get("pitch") or "").split())
    lignes = [START]
    if pitch:
        lignes += [f"> {pitch}", ""]
    lignes += [
        "| " + " | ".join(COLONNES) + " |",
        "|---|---|---|---|",
        "| " + " | ".join(cellules(fm)) + " |",
        END,
    ]
    return "\n".join(lignes)


def applique(texte: str, zone: str) -> str | None:
    """Texte de la page avec sa zone AUTO à jour, ou None si rien à faire.

    Deux cas seulement : la zone existe et se remplace en bloc, ou elle n'existe
    pas et s'insère juste sous le titre H1. Aucun troisième cas n'est deviné — une
    page sans H1 est laissée telle quelle et signalée par l'appelant.
    """
    if ZONE_RE.search(texte):
        neuf = ZONE_RE.sub(lambda _: zone, texte, count=1)
        return neuf if neuf != texte else None
    m = H1_RE.search(texte)
    if not m:
        return None
    fin = m.end()
    reste = texte[fin:].lstrip("\n")
    return texte[:fin] + "\n\n" + zone + "\n\n" + reste


def cibles(args: list[str]) -> tuple[list[Path], list[str]]:
    """Les pages du scope, triées, plus les chemins refusés.

    Sans argument : les dossiers de pages de la racine. Avec : uniquement ce qui
    vit sous les chemins donnés, un fichier étant un scope légitime d'une page. Un
    chemin hors du vault est refusé plutôt qu'ignoré — c'est la garantie que la
    conversation d'à côté ne verra pas ses fiches réécrites.
    """
    refus: list[str] = []
    racines: list[Path] = []
    if not args:
        racines = sorted(d for d in VAULT.iterdir()
                         if d.is_dir() and d.name not in NON_PAGES)
    else:
        for a in args:
            p = Path(a)
            p = (p if p.is_absolute() else Path.cwd() / p).resolve()
            try:
                parts = p.relative_to(VAULT).parts
            except ValueError:
                refus.append(f"{a} — hors du vault ({VAULT})")
                continue
            if not p.exists():
                refus.append(f"{a} — chemin inexistant")
                continue
            if parts and parts[0] in NON_PAGES:
                refus.append(f"{a} — dossier d'outillage, jamais de bandeau ici")
                continue
            racines.append(p)
    pages: set[Path] = set()
    for r in racines:
        if r.is_file():
            if r.suffix == ".md":
                pages.add(r)
            else:
                refus.append(f"{rel(r)} — pas un fichier .md")
            continue
        for md in r.rglob("*.md"):
            parts = md.relative_to(VAULT).parts
            if parts[0] in NON_PAGES:
                continue
            pages.add(md)
    return sorted(pages), refus


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Compose le bandeau des pages `role: brique` depuis leur frontmatter.")
    ap.add_argument("chemins", nargs="*",
                    help="fichiers ou dossiers à traiter ; vide = tout le vault")
    ap.add_argument("--check", action="store_true",
                    help="n'écrit rien ; sort en 2 s'il reste un bandeau à poser ou à rafraîchir")
    ns = ap.parse_args()

    pages, refus = cibles(ns.chemins)
    for r in refus:
        print(f"  [REFUS] {r}")
    if refus:
        return 1

    portee = ", ".join(ns.chemins) if ns.chemins else "vault entier"
    briques = ecrits = sans_titre = 0
    a_faire: list[str] = []
    trous: list[str] = []
    for md in pages:
        texte = md.read_text(encoding="utf-8")
        fm = parse(texte)
        if not fm or fm.get("role") != "brique":
            continue
        briques += 1
        zone = bandeau(fm)
        manque = colonnes_vides(cellules(fm))
        if manque:
            trous.append(f"{rel(md)} — {', '.join(manque)}")
        neuf = applique(texte, zone)
        if neuf is None:
            if not H1_RE.search(texte) and not ZONE_RE.search(texte):
                sans_titre += 1
                print(f"  [SAUT] {rel(md)} : aucun titre `# ` — bandeau non posé")
            continue
        a_faire.append(rel(md))
        if not ns.check:
            md.write_text(neuf, encoding="utf-8")
            ecrits += 1

    mode = "check" if ns.check else "écriture"
    print(f"build_bandeau ({mode}) — portée : {portee}")
    print(f"  {len(pages)} page(s) balayée(s), {briques} `role: brique`")
    if trous:
        # Signalé, jamais comblé : une cellule vide dit qu'un champ manque au
        # frontmatter, et c'est une information. La remplir au jugé l'effacerait.
        print(f"  {len(trous)} bandeau(x) à cellule vide — champ absent du frontmatter :")
        for t in trous:
            print(f"    - {t}")
    if sans_titre:
        print(f"  {sans_titre} page(s) sans titre `# `, sautée(s)")
    if ns.check:
        if a_faire:
            print(f"  {len(a_faire)} bandeau(x) absent(s) ou périmé(s) :")
            for p in a_faire:
                print(f"    - {p}")
            return 2
        print("  OK — tous les bandeaux concordent avec leur frontmatter.")
        return 0
    print(f"  {ecrits} bandeau(x) écrit(s), {briques - ecrits - sans_titre} déjà à jour")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
