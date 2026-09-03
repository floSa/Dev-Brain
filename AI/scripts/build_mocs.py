# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""build_mocs.py — génère/maintient les pages hub (MOC) depuis l'index.

Pages de navigation qui relient les membres d'une famille par des [[liens]]
explicites (→ arêtes visibles dans le graphe Obsidian) :
  - la zone AUTO de chaque page `role: hub` de l'arbre — son périmètre est son DOSSIER
  - MOC/Concepts/<Label>.md   : sous-hub Wiki par famille de catégorie (concept/stats → « Statistiques »)
  - Métiers/<Label>.md        : hub transverse par `domaines:` (data-eng → « Data Engineering »)

Le lot 3 a vidé `Dev/` : les 337 briques sont descendues dans l'arbre des domaines, les
5 patterns et les 5 règles dans « Patterns/ » et « Rules/ ». Les deux boucles qui
généraient `MOC/Categories/` et `MOC/Types/` ont donc été retirées — le hub d'un dossier
liste ce que ce dossier contient, quel que soit le `role:` de ses pages, et c'est tout
l'intérêt de l'arborescence (brain-v3 §10). Il ne reste de `MOC/` que `MOC/Concepts/`,
seule porte d'entrée des 297 notions qui attendent le lot 4 : elle meurt avec elles.

Les liens sont régénérés entre les balises AUTO ; la zone « ## Notes » est
préservée à chaque régénération (place pour tes ajouts manuels).

Usage : uv run AI/scripts/build_mocs.py   (après build_index.py)
Cross-OS, chemins relatifs, sortie déterministe.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
INDEX = VAULT / "AI" / "index" / "brain-index.json"
MOC = VAULT / "MOC"
# Les 5 hubs transverses de `domaines:` sont descendus à la racine au lot 3 (arbitrage
# de floSa) : ils sont le seul axe qui traverse un arbre rangé par domaine TECHNIQUE.
# Le dossier ne s'appelle pas « Domaines » — le mot désigne déjà les 20 dossiers de
# l'arbre, l'homonymie serait un piège. Cf. AI/migration/lot-3-arborescence.md,
# remontée 21 (collision de vocabulaire, à trancher au lot 8).
METIERS = VAULT / "Métiers"
MOC_CONCEPT = VAULT / "MOC" / "Concepts"

# Un hub de `Métiers/` est rempli par la boucle `domaines:` ci-dessous, PAS par
# `zone_hub()` : son périmètre est un champ, pas un dossier. Le lister dans les deux
# ferait écraser la vue transverse par le contenu du dossier (cinq hubs, rien d'autre).
HUBS_TRANSVERSES = {"Métiers"}

THEME_LABEL = {
    "data-sci": "Data Science", "data-eng": "Data Engineering", "mlops": "MLOps",
    "ml-eng": "ML Engineering", "ai-eng": "AI Engineering",
    "infra-ops": "Infrastructure & Ops",
}

# Étage intermédiaire : un sous-hub par famille de catégorie wiki (concept/<sub>).
# Libellés sans collision avec les pages concepts ni les MOC de catégories.
CONCEPT_LABEL = {
    "stats": "Statistiques", "ml": "Machine learning (notions)", "math": "Maths du ML",
    "dl": "Deep learning", "rl": "Apprentissage par renforcement",
    "ts": "Séries temporelles", "llm": "LLM (notions)", "ai": "IA & sécurité",
    "data": "Données (notions)", "devops": "DevOps (notions)",
    # "(notions)" : évite la collision avec la page chapeau « Traitement du signal ».
    "signal": "Traitement du signal (notions)", "nlp": "NLP (notions)",
}
# Familles wiki HORS `concept/*` : aucune page sous `Wiki/` ne doit sortir des MOC
# (le filtre historique `concept/*` laissait Wiki/Outils/Obsidian.md hors de tout hub).
WIKI_LABEL = {
    "skill/knowledge": "Gestion des connaissances",
    "divers": "Divers (wiki)",  # pages wiki sans `categorie:`
}

AUTO_RE = re.compile(r"<!-- AUTO:START -->.*?<!-- AUTO:END -->", re.S)


def link(p: dict) -> str:
    """Lien NU vers la page — le vault n'a plus de lien qualifié depuis le lot 3.

    Un lien qualifié porte le chemin ; il casse au premier `git mv`. Le lot 3 en
    déplace 682, les lots 4 à 6 encore. Obsidian résout par nom de fichier, et le
    vault n'a plus de collision de nom (la dernière, `hdbscan` / `HDBSCAN`, est
    tombée avec le renommage de la notion). Cf. AI/migration/lot-3-arborescence.md.
    """
    stem = Path(p["path"]).stem
    return f"[[{stem}]]" if stem == p["nom"] else f"[[{stem}|{p['nom']}]]"


def bullet(p: dict) -> str:
    desc = p.get("pitch")
    if not desc:
        doms = p.get("domaines") or []
        desc = ("domaines : " + ", ".join(doms)) if doms else ""
    return f"- {link(p)}" + (f" — {desc}" if desc else "")


def wiki_group(cat: str) -> tuple[str, str, str, str]:
    """(clé de groupe, libellé du sous-hub, périmètre indexé, intro) d'une page wiki.

    `concept/<sub>` garde le comportement historique (clé = `<sub>`) ; toute autre
    catégorie wiki est groupée sur la catégorie entière, pour qu'aucune page sous
    `Wiki/` ne reste hors MOC.
    """
    if cat.startswith("concept/"):
        sub = cat.split("/", 1)[1]
        return (sub, CONCEPT_LABEL.get(sub, sub), f"concept/{sub}",
                f"Notions de la famille `concept/{sub}`.")
    key = cat or "divers"
    label = WIKI_LABEL.get(key, key.replace("/", " · "))
    return key, label, key, f"Pages wiki de la famille `{key}`."


def upsert(path: Path, title: str, intro: str, bullets: list[str],
           scope: str) -> None:
    auto = ("<!-- AUTO:START -->\n" + intro + "\n\n" + "\n".join(bullets)
            + "\n<!-- AUTO:END -->")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        txt = path.read_text(encoding="utf-8")
        if AUTO_RE.search(txt):
            txt = AUTO_RE.sub(lambda m: auto, txt)  # remplace SEULEMENT la zone auto
        path.write_text(txt, encoding="utf-8")
    else:
        # `indexe:` n'appartient pas au gabarit `role: hub` (check_brain, HUB_ALLOWED) :
        # une page recréée hors de `MOC/` avec ce champ serait refusée par le validateur.
        # Il ne survit que sous `MOC/`, dossier que check_brain ne balaye pas et qui meurt
        # au lot 4 avec Wiki/Concepts/. Ailleurs, le hub porte le `pitch:` qu'il exige.
        sous_moc = MOC in path.parents
        cle = f"indexe: {scope}" if sous_moc else f"pitch: {intro}"
        fm = f"---\nrole: hub\nnom: {title}\n{cle}\n---\n\n"
        corps = f"# {title}\n\n{auto}\n"
        path.write_text(fm + corps + ("\n## Notes\n\n" if sous_moc else ""),
                        encoding="utf-8")


# ---------------------------------------------------------------- pages hub (v3)

RE_ROLE_HUB = re.compile(r"^role: hub\s*$", re.M)
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}
# Sections de la zone AUTO d'un hub, dans l'ordre, une par `role:` groupable. `pattern`
# et `rule` s'y sont ajoutés à la clôture du lot 3 : leurs pages n'ont pas de `categorie:`
# (la taxonomie ne les couvre pas), elles sortaient donc de tout groupement par catégorie
# et il avait fallu `MOC/Types/` pour les rattraper. Un hub groupe par DOSSIER, pas par
# catégorie : « Patterns/ » et « Rules/ » les listent sans rattrapage, et `MOC/Types/`
# n'a plus lieu d'être — ses deux pages SONT devenues ces deux hubs, par `git mv`.
ROLE_SECTION = [("notion", "Notions"), ("brique", "Briques"),
                ("pattern", "Patterns"), ("rule", "Rules")]


def dossiers_de_pages() -> list[Path]:
    return sorted(d for d in VAULT.iterdir()
                  if d.is_dir() and d.name not in NON_PAGES)


def hubs() -> list[Path]:
    """Les pages `role: hub` du vault — une par dossier de l'arbre des domaines."""
    out = []
    for racine in dossiers_de_pages():
        for md in sorted(racine.rglob("*.md")):
            if RE_ROLE_HUB.search(md.read_text(encoding="utf-8")[:400]):
                out.append(md)
    return out


def zone_hub(hub: Path, pages: list[dict]) -> list[str]:
    """Contenu de la zone AUTO d'un hub : ses sous-dossiers, puis SES pages.

    Le perimetre d'un hub est son DOSSIER, pas une requete sur `categorie:` — c'est
    tout l'interet de l'arborescence (brain-v3 §10) : le voisinage d'une page est
    `ls` de son dossier, il ne se devine plus. Les pages d'un sous-dossier sont
    listees par le hub de ce sous-dossier, jamais deux fois.
    """
    dossier = hub.parent
    rel = dossier.relative_to(VAULT).as_posix()
    lignes: list[str] = []

    sous = []
    for sd in sorted(d for d in dossier.iterdir() if d.is_dir()):
        fils = sd / (sd.name + ".md")
        if fils.exists() and RE_ROLE_HUB.search(fils.read_text(encoding="utf-8")[:400]):
            sous.append(sd.name)
    if sous:
        lignes += ["### Sous-domaines",
                   "- " + " · ".join("[[" + s + "]]" for s in sous), ""]

    ici = [q for q in pages
           if q["path"].rsplit("/", 1)[0] == rel and Path(q["path"]).stem != hub.stem]
    for role, titre in ROLE_SECTION:
        membres = sorted((q for q in ici if q.get("role") == role),
                         key=lambda e: e["nom"].lower())
        if membres:
            lignes += ["### " + titre] + [bullet(q) for q in membres] + [""]

    bases = sorted(b.stem for b in dossier.glob("*.base"))
    if bases:
        lignes += ["### Comparatifs"] + ["- [[" + b + "]]" for b in bases] + [""]

    return lignes or ["*(dossier vide)*"]


def main() -> int:
    if not INDEX.exists():
        raise SystemExit("Index absent — lancer d'abord : uv run AI/scripts/build_index.py")
    pages = json.loads(INDEX.read_text(encoding="utf-8"))["pages"]
    written: list[tuple[str, str, int]] = []
    skipped: list[str] = []

    # Les deux boucles `Dev/` — `MOC/Categories/` par `categorie:` de tête, `MOC/Types/`
    # par `role:` — ont été RETIRÉES à la clôture du lot 3 : plus aucune page ne vit sous
    # `Dev/`. Les 337 briques sont descendues dans l'arbre, où le hub de leur dossier les
    # liste ; les 5 patterns et les 5 règles sont dans « Patterns/ » et « Rules/ », dont
    # les hubs sont issus de `MOC/Types/` par `git mv`. Le rattrapage R13 (audit axe 2,
    # annexe B) disparaît avec elles : une page sans `categorie:` n'est plus écartée d'un
    # groupement par catégorie, elle est listée par le hub de son dossier comme les autres.

    # Sous-hubs Wiki : un MOC par famille de catégorie — étage intermédiaire.
    # Liste les feuilles ; c'est ce nœud (Statistiques, Maths du ML…) qui devient le gros hub concret.
    sub_groups: dict[str, list[dict]] = {}
    wiki_meta: dict[str, tuple[str, str, str]] = {}
    for p in pages:
        if not p["path"].startswith("Wiki/"):
            continue
        key, label, scope, intro = wiki_group(p.get("categorie") or "")
        sub_groups.setdefault(key, []).append(p)
        wiki_meta[key] = (label, scope, intro)
    # Un sous-hub MOC/Concepts dont le LIBELLÉ est désormais porté par une page
    # `role: hub` de l'arbre a été absorbé par ce hub (`git mv`), comme une MOC de
    # domaine l'est par le hub de son dossier — cf. remontées 6 et 15 de
    # AI/migration/lot-3-arborescence.md. Le recréer remettrait DEUX fichiers du même
    # nom dans le vault, et un lien nu n'y résout plus de façon déterministe. Ses
    # notions restent atteignables (R7) par les citations en clair du hub, jusqu'à ce
    # que le lot 4 les descende dans son dossier.
    portes_par_un_hub = {h.stem for h in hubs()}
    for key, members in sorted(sub_groups.items()):
        label, scope, intro = wiki_meta[key]
        if label in portes_par_un_hub:
            skipped.append(f"MOC/Concepts/{label}.md non recréé — absorbé par la page "
                           f"`role: hub` du même nom ({len(members)} notion(s) "
                           f"`{scope}` citées par ce hub jusqu'au lot 4)")
            continue
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CONCEPT / f"{label}.md", label, intro, bullets, scope)
        written.append(("Concepts", label, len(members)))

    # Hubs transverses `Métiers/` — les 5 axes métier du champ `domaines:`, pointant
    # vers les SOUS-HUBS et non vers les feuilles. Seule vue qui traverse l'arbre des
    # domaines TECHNIQUES ; c'est ce qui justifie de la garder (arbitrage du lot 3).
    #
    # Le périmètre était resté celui de la v2 — les seules pages `Wiki/` — et le lot 4
    # devait le rebâtir sur l'arbre. Fait ici, parce que ne PAS le faire érode ces
    # 5 pages à chaque lot de domaine, en silence : descendre les 37 notions
    # `concept/stats` a fait disparaître la ligne « Statistiques — 37 notion(s) » de
    # « Métiers/Data Science.md », sans qu'aucune règle du validateur s'en aperçoive
    # (R7 tient toujours, les notions étant citées par le hub de leur dossier).
    #
    # La règle est donc : une page groupe par SON HUB. Sous `Wiki/`, c'est encore le
    # sous-hub `MOC/Concepts/` ; dans l'arbre, c'est le dossier de domaine. Les hubs
    # eux-mêmes sont exclus — ils portent `domaines:` et se compteraient eux-mêmes.
    # Mesure au 2026-09-05 : 260 pages `Wiki/` et 68 pages de l'arbre portent
    # `domaines:`, dont les 37 notions de statistiques et 31 briques.
    theme_subs: dict[str, dict[str, int]] = {}
    theme_labels: dict[str, str] = {}
    for p in pages:
        if p.get("role") == "hub":
            continue
        if p["path"].startswith("Wiki/"):
            key = wiki_group(p.get("categorie") or "")[0]
            theme_labels[key] = wiki_meta[key][0]
        else:
            key = "arbre:" + p["path"].split("/")[0]
            theme_labels[key] = p["path"].split("/")[0]
        for dom in p.get("domaines") or []:
            theme_subs.setdefault(dom, {})
            theme_subs[dom][key] = theme_subs[dom].get(key, 0) + 1
    for dom, subs in sorted(theme_subs.items()):
        label = THEME_LABEL.get(dom, dom)
        bullets = []
        for key, n in sorted(subs.items(), key=lambda e: (-e[1], e[0])):
            # « page(s) » et non « notion(s) » : un groupe de l'arbre mêle notions et
            # briques, le compte ne peut plus annoncer un seul rôle.
            bullets.append(f"- [[{theme_labels[key]}]] — {n} page(s)")
        upsert(METIERS / f"{label}.md", label,
               f"Axe métier **{label}** (`{dom}`) — explorer par sous-domaine, puis "
               "descendre via le graphe local.",
               bullets, dom)
        written.append(("Métiers", label, len(subs)))

    # Zones AUTO des pages hub (v3) — elles remplacent `MOC/` domaine par domaine.
    # Les pages deja descendues dans l'arbre sortent d'elles-memes des boucles MOC
    # ci-dessus, qui filtrent sur `Dev/` et `Wiki/`. Les hubs transverses de
    # `Métiers/` sont exclus : leur périmètre est un CHAMP, pas un dossier — la
    # boucle ci-dessus les a déjà remplis.
    for hub in hubs():
        if hub.relative_to(VAULT).parts[0] in HUBS_TRANSVERSES:
            continue
        lignes = zone_hub(hub, pages)
        txt = hub.read_text(encoding="utf-8")
        if not AUTO_RE.search(txt):
            skipped.append(hub.relative_to(VAULT).as_posix() + " : aucune zone "
                           "<!-- AUTO:START -->/<!-- AUTO:END --> — hub non rempli")
            continue
        nl = "\r\n" if "\r\n" in txt else "\n"
        auto = ("<!-- AUTO:START -->" + nl + nl.join(lignes).rstrip()
                + nl + "<!-- AUTO:END -->")
        hub.write_text(AUTO_RE.sub(lambda m: auto, txt), encoding="utf-8")
        written.append(("hub", hub.relative_to(VAULT).as_posix(), len(lignes)))

    for kind, label, n in written:
        if kind == "hub":
            print(f"  {label} (zone AUTO : {n} ligne(s))")
        else:
            print(f"  MOC/{kind}/{label}.md ({n} membre(s))")
    for s in skipped:
        print(f"  [SKIP] {s}")
    print(f"{len(written)} MOC générés / mis à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
