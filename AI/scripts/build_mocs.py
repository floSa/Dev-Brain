# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""build_mocs.py — génère/maintient les pages hub (MOC) depuis l'index.

Pages de navigation qui relient les membres d'une famille par des [[liens]]
explicites (→ arêtes visibles dans le graphe Obsidian) :
  - MOC/Categories/<Label>.md : hub Dev par catégorie de tête (database → « Bases de données »)
  - MOC/Types/<Label>.md      : hub Dev par `type:` pour les types sans `categorie:` (pattern, rule)
  - MOC/Concepts/<Label>.md   : sous-hub Wiki par famille de catégorie (concept/stats → « Statistiques »)
  - MOC/Themes/<Label>.md     : MOC Wiki par domaine (data-eng → « Data Engineering »)

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
MOC_CAT = VAULT / "MOC" / "Categories"
MOC_TYPE = VAULT / "MOC" / "Types"
MOC_THEME = VAULT / "MOC" / "Themes"
MOC_CONCEPT = VAULT / "MOC" / "Concepts"

CAT_LABEL = {
    "database": "Bases de données", "framework": "Frameworks",
    "ui": "Interfaces & apps data", "language": "Langages", "devops": "DevOps",
    "llm": "LLM & IA générative", "ml": "Machine Learning", "data": "Data & pipelines",
    "compute": "Calcul distribué", "auth": "Auth", "storage": "Stockage",
    "observability": "Observabilité", "tooling": "Outils & libs",
    "network": "Réseau", "security": "Sécurité",
    "automation": "Automatisation no-code",
}
# Hubs Dev groupés sur `type:` et NON sur `categorie:` : les types pattern, rule et rex
# n'ont pas de `categorie:` (la taxonomie ne les couvre pas), une catégorie vide est falsy,
# ils sortaient donc de toutes les MOC. `type:` est présent et fiable sur 100 % des pages.
# On n'invente PAS de catégorie pour ces types : ce serait de la taxonomie, pas de la navigation.
# Les types déjà couverts par MOC/Categories (service, outil) ne sont pas repris ici.
TYPE_LABEL = {
    "pattern": "Patterns",
    "rule": "Rules",
    "rex": "REX",  # place réservée — voir REX_MIN
}
TYPE_INTRO = {
    "pattern": "Architectures type — combinaisons de briques `Dev/` déjà éprouvées.",
    "rule": "Règles transverses, applicables quelle que soit la stack du projet.",
    "rex": "Retours d'expérience — un fichier par service.",
}
# Le pilier REX n'est pas tranché (l'axe 6 de l'audit recommande une fusion). Tant que
# Dev/REX/ ne contient que la fiche d'exemple, le hub REX n'est pas généré : le code lui
# garde sa place, la décision reste à prendre.
REX_MIN = 2

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
# Familles wiki HORS `concept/*` : aucune page `galaxie: wiki` ne doit sortir des MOC
# (le filtre historique `concept/*` laissait Wiki/Outils/Obsidian.md hors de tout hub).
WIKI_LABEL = {
    "skill/knowledge": "Gestion des connaissances",
    "divers": "Divers (wiki)",  # pages wiki sans `categorie:`
}

AUTO_RE = re.compile(r"<!-- AUTO:START -->.*?<!-- AUTO:END -->", re.S)


def link(p: dict) -> str:
    path = p["path"][:-3] if p["path"].endswith(".md") else p["path"]
    return f"[[{path}|{p['nom']}]]"


def bullet(p: dict) -> str:
    desc = p.get("pitch")
    if not desc:
        doms = p.get("domaines") or []
        desc = ("domaines : " + ", ".join(doms)) if doms else ""
    return f"- {link(p)}" + (f" — {desc}" if desc else "")


def wiki_group(cat: str) -> tuple[str, str, str, str]:
    """(clé de groupe, libellé du sous-hub, périmètre indexé, intro) d'une page wiki.

    `concept/<sub>` garde le comportement historique (clé = `<sub>`) ; toute autre
    catégorie wiki est groupée sur la catégorie entière, pour qu'aucune page
    `galaxie: wiki` ne reste hors MOC.
    """
    if cat.startswith("concept/"):
        sub = cat.split("/", 1)[1]
        return (sub, CONCEPT_LABEL.get(sub, sub), f"concept/{sub}",
                f"Notions de la famille `concept/{sub}`.")
    key = cat or "divers"
    label = WIKI_LABEL.get(key, key.replace("/", " · "))
    return key, label, key, f"Pages wiki de la famille `{key}`."


def upsert(path: Path, title: str, intro: str, bullets: list[str],
           galaxie: str, scope: str) -> None:
    auto = ("<!-- AUTO:START -->\n" + intro + "\n\n" + "\n".join(bullets)
            + "\n<!-- AUTO:END -->")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        txt = path.read_text(encoding="utf-8")
        if AUTO_RE.search(txt):
            txt = AUTO_RE.sub(lambda m: auto, txt)  # remplace SEULEMENT la zone auto
        path.write_text(txt, encoding="utf-8")
    else:
        fm = (f"---\ntype: moc\nnom: {title}\ngalaxie: {galaxie}\n"
              f"indexe: {scope}\n---\n\n")
        path.write_text(fm + f"# {title}\n\n{auto}\n\n## Notes\n\n", encoding="utf-8")


def main() -> int:
    if not INDEX.exists():
        raise SystemExit("Index absent — lancer d'abord : uv run AI/scripts/build_index.py")
    pages = json.loads(INDEX.read_text(encoding="utf-8"))["pages"]
    written: list[tuple[str, str, int]] = []
    skipped: list[str] = []

    # Hubs Dev : par catégorie de tête (database/vector → database → « Bases de données »)
    cat_groups: dict[str, list[dict]] = {}
    for p in pages:
        if p.get("galaxie") != "dev":
            continue
        head = (p.get("categorie") or "").split("/")[0]
        if head:
            cat_groups.setdefault(head, []).append(p)
    for head, members in sorted(cat_groups.items()):
        label = CAT_LABEL.get(head, head.capitalize())
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CAT / f"{label}.md", label,
               f"Briques techniques de la catégorie `{head}/*`.",
               bullets, "dev", f"{head}/*")
        written.append(("Categories", label, len(members)))

    # Hubs Dev : par `type:`, pour les types que `categorie:` ne peut pas grouper.
    type_groups: dict[str, list[dict]] = {}
    for p in pages:
        typ = p.get("type")
        if typ in TYPE_LABEL:
            type_groups.setdefault(typ, []).append(p)
    for typ, members in sorted(type_groups.items()):
        label = TYPE_LABEL[typ]
        if typ == "rex" and len(members) < REX_MIN:
            skipped.append(f"MOC/Types/{label}.md — {len(members)} fiche(s) REX "
                           f"(< {REX_MIN}) : pilier REX non tranché (axe 6)")
            continue
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_TYPE / f"{label}.md", label, TYPE_INTRO[typ],
               bullets, "dev", f"type/{typ}")
        written.append(("Types", label, len(members)))

    # Sous-hubs Wiki : un MOC par famille de catégorie — étage intermédiaire.
    # Liste les feuilles ; c'est ce nœud (Statistiques, Maths du ML…) qui devient le gros hub concret.
    sub_groups: dict[str, list[dict]] = {}
    wiki_meta: dict[str, tuple[str, str, str]] = {}
    for p in pages:
        if p.get("galaxie") != "wiki":
            continue
        key, label, scope, intro = wiki_group(p.get("categorie") or "")
        sub_groups.setdefault(key, []).append(p)
        wiki_meta[key] = (label, scope, intro)
    for key, members in sorted(sub_groups.items()):
        label, scope, intro = wiki_meta[key]
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CONCEPT / f"{label}.md", label, intro, bullets, "wiki", scope)
        written.append(("Concepts", label, len(members)))

    # MOC Wiki par domaine → pointe vers les SOUS-HUBS (pas les feuilles).
    # Étage de navigation : domaine → sous-domaine → (graphe local) → feuille.
    theme_subs: dict[str, dict[str, int]] = {}
    for p in pages:
        if p.get("galaxie") != "wiki":
            continue
        key = wiki_group(p.get("categorie") or "")[0]
        for dom in p.get("domaines") or []:
            theme_subs.setdefault(dom, {})
            theme_subs[dom][key] = theme_subs[dom].get(key, 0) + 1
    for dom, subs in sorted(theme_subs.items()):
        label = THEME_LABEL.get(dom, dom)
        bullets = []
        for key, n in sorted(subs.items(), key=lambda e: (-e[1], e[0])):
            slab = wiki_meta[key][0]
            bullets.append(f"- [[MOC/Concepts/{slab}|{slab}]] — {n} notion(s)")
        upsert(MOC_THEME / f"{label}.md", label,
               f"Domaine **{label}** (`{dom}`) — explorer par sous-domaine, puis descendre via le graphe local.",
               bullets, "wiki", dom)
        written.append(("Themes", label, len(subs)))

    for kind, label, n in written:
        print(f"  MOC/{kind}/{label}.md ({n} membre(s))")
    for s in skipped:
        print(f"  [SKIP] {s}")
    print(f"{len(written)} MOC générés / mis à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
