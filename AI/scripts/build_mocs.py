# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""build_mocs.py — génère/maintient les pages hub (MOC) depuis l'index.

Pages de navigation qui relient les membres d'une famille par des [[liens]]
explicites (→ arêtes visibles dans le graphe Obsidian) :
  - MOC/Categories/<Label>.md : hub Dev par catégorie de tête (database → « Bases de données »)
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
MOC_THEME = VAULT / "MOC" / "Themes"
MOC_CONCEPT = VAULT / "MOC" / "Concepts"

CAT_LABEL = {
    "database": "Bases de données", "framework": "Frameworks",
    "ui": "Interfaces & apps data", "language": "Langages", "devops": "DevOps",
    "llm": "LLM & IA générative", "ml": "Machine Learning", "data": "Data & pipelines",
    "compute": "Calcul distribué", "auth": "Auth", "storage": "Stockage",
    "observability": "Observabilité", "tooling": "Outils & libs",
    "automation": "Automatisation no-code",
}
THEME_LABEL = {
    "data-sci": "Data Science", "data-eng": "Data Engineering", "mlops": "MLOps",
    "ml-eng": "ML Engineering", "ai-eng": "AI Engineering",
}
# Étage intermédiaire : un sous-hub par sous-domaine de concept (concept/<sub>).
# Libellés sans collision avec les pages concepts ni les MOC de catégories.
CONCEPT_LABEL = {
    "stats": "Statistiques", "ml": "Machine learning (notions)", "math": "Maths du ML",
    "dl": "Deep learning", "rl": "Apprentissage par renforcement",
    "ts": "Séries temporelles", "llm": "LLM (notions)", "ai": "IA & sécurité",
    "data": "Données (notions)", "devops": "DevOps (notions)",
    # "(notions)" : évite la collision avec la page chapeau « Traitement du signal ».
    "signal": "Traitement du signal (notions)", "nlp": "NLP (notions)",
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

    # Sous-hubs Wiki : un MOC par sous-domaine de concept (concept/<sub>) — étage intermédiaire.
    # Liste les feuilles ; c'est ce nœud (Statistiques, Maths du ML…) qui devient le gros hub concret.
    sub_groups: dict[str, list[dict]] = {}
    for p in pages:
        if p.get("galaxie") != "wiki":
            continue
        cat = p.get("categorie") or ""
        if cat.startswith("concept/"):
            sub_groups.setdefault(cat.split("/", 1)[1], []).append(p)
    for sub, members in sorted(sub_groups.items()):
        label = CONCEPT_LABEL.get(sub, sub)
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CONCEPT / f"{label}.md", label,
               f"Notions de la famille `concept/{sub}`.",
               bullets, "wiki", f"concept/{sub}")
        written.append(("Concepts", label, len(members)))

    # MOC Wiki par domaine → pointe vers les SOUS-HUBS (pas les feuilles).
    # Étage de navigation : domaine → sous-domaine → (graphe local) → feuille.
    theme_subs: dict[str, dict[str, int]] = {}
    for p in pages:
        if p.get("galaxie") != "wiki":
            continue
        cat = p.get("categorie") or ""
        if not cat.startswith("concept/"):
            continue
        sub = cat.split("/", 1)[1]
        for dom in p.get("domaines") or []:
            theme_subs.setdefault(dom, {})
            theme_subs[dom][sub] = theme_subs[dom].get(sub, 0) + 1
    for dom, subs in sorted(theme_subs.items()):
        label = THEME_LABEL.get(dom, dom)
        bullets = []
        for sub, n in sorted(subs.items(), key=lambda e: (-e[1], e[0])):
            slab = CONCEPT_LABEL.get(sub, sub)
            bullets.append(f"- [[MOC/Concepts/{slab}|{slab}]] — {n} notion(s)")
        upsert(MOC_THEME / f"{label}.md", label,
               f"Domaine **{label}** (`{dom}`) — explorer par sous-domaine, puis descendre via le graphe local.",
               bullets, "wiki", dom)
        written.append(("Themes", label, len(subs)))

    for kind, label, n in written:
        print(f"  MOC/{kind}/{label}.md ({n} membre(s))")
    print(f"{len(written)} MOC générés / mis à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
