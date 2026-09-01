# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""build_mocs.py — génère/maintient les pages hub (MOC) depuis l'index.

Pages de navigation qui relient les membres d'une famille par des [[liens]]
explicites (→ arêtes visibles dans le graphe Obsidian) :
  - MOC/Categories/<Label>.md : hub Dev par catégorie de tête (database → « Bases de données »)
  - MOC/Types/<Label>.md      : hub Dev par `role:` pour les rôles sans `categorie:` (pattern, rule)
  - MOC/Concepts/<Label>.md   : sous-hub Wiki par famille de catégorie (concept/stats → « Statistiques »)
  - MOC/Themes/<Label>.md     : MOC Wiki par domaine (data-eng → « Data Engineering »)

Le partage Dev / Wiki se lit sur le CHEMIN et non sur un champ : `galaxie:` a disparu au
lot 2, et l'arborescence ne bouge qu'au lot 3. Ce script est de toute façon appelé à être
réécrit à ce moment-là — il ne générera plus `MOC/` mais les zones AUTO des pages hub
(cf. AI/design/brain-v3.md §11). Redécouper la navigation sur `role:` dès maintenant
déplacerait des pages d'un hub à l'autre pour rien, deux fois de suite.

Les liens sont régénérés entre les balises AUTO ; la zone « ## Notes » est
préservée à chaque régénération (place pour tes ajouts manuels).

Le script rend compte de ce qu'il écarte (R13, audit axe 2, annexe B) : une ligne
`[SKIP]` donne le nombre de pages Dev sans `categorie:` sorties des hubs
MOC/Categories, combien sont rattrapées par MOC/Types, et la liste nominative de
celles qui restent hors de TOUT hub. Ce reste est le seul chiffre inquiétant : une
page hors MOC est invisible à la navigation, et `check_brain` la refuse (R7).

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

# Libellé français d'un préfixe de tête de `categorie:`. UN LIBELLÉ PAR PRÉFIXE :
# un préfixe absent de cette table sort en anglais capitalisé (« Devtools »), défaut
# déjà corrigé une fois pour `network` et `security`. Les 20 préfixes du vocabulaire
# en vigueur sont listés dans Documentation/general/taxonomie.md.
CAT_LABEL = {
    "ml": "Machine Learning", "llm": "LLM & IA générative",
    "database": "Bases de données", "data": "Data & pipelines",
    "devtools": "Outils de développement", "stats": "Statistiques & inférence",
    "compute": "Calcul distribué", "design": "Design & diagrammes",
    "storage": "Stockage", "web": "Web & API",
    "automation": "Automatisation no-code", "media": "Médias",
    "ui": "Interfaces & apps data", "observability": "Observabilité",
    "security": "Sécurité", "signal": "Signal & audio",
    "network": "Réseau", "devops": "DevOps",
    "docs": "Documents", "math": "Mathématiques",
}
# Hubs Dev groupés sur `role:` et NON sur `categorie:` : les rôles pattern et rule
# n'ont pas de `categorie:` (la taxonomie ne les couvre pas), une catégorie vide est falsy,
# ils sortaient donc de toutes les MOC. `role:` est présent et fiable sur 100 % des pages.
# On n'invente PAS de catégorie pour ces rôles : ce serait de la taxonomie, pas de la navigation.
# Le rôle déjà couvert par MOC/Categories (brique) n'est pas repris ici.
ROLE_LABEL = {
    "pattern": "Patterns",
    "rule": "Rules",
}
ROLE_INTRO = {
    "pattern": "Architectures type — combinaisons de briques `Dev/` déjà éprouvées.",
    "rule": "Règles transverses, applicables quelle que soit la stack du projet.",
}

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
        fm = (f"---\nrole: hub\nnom: {title}\n"
              f"indexe: {scope}\n---\n\n")
        path.write_text(fm + f"# {title}\n\n{auto}\n\n## Notes\n\n", encoding="utf-8")


def main() -> int:
    if not INDEX.exists():
        raise SystemExit("Index absent — lancer d'abord : uv run AI/scripts/build_index.py")
    pages = json.loads(INDEX.read_text(encoding="utf-8"))["pages"]
    written: list[tuple[str, str, int]] = []
    skipped: list[str] = []

    # Hubs Dev : par catégorie de tête (database/vecteur → database → « Bases de données »)
    cat_groups: dict[str, list[dict]] = {}
    sans_categorie: list[dict] = []
    for p in pages:
        if not p["path"].startswith("Dev/"):
            continue
        head = (p.get("categorie") or "").split("/")[0]
        if head:
            cat_groups.setdefault(head, []).append(p)
        else:
            sans_categorie.append(p)  # R13 : compté, plus jamais écarté en silence
    for head, members in sorted(cat_groups.items()):
        label = CAT_LABEL.get(head, head.capitalize())
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CAT / f"{label}.md", label,
               f"Briques techniques de la catégorie `{head}/*`.",
               bullets, f"{head}/*")
        written.append(("Categories", label, len(members)))

    # Hubs Dev : par `type:`, pour les types que `categorie:` ne peut pas grouper.
    role_groups: dict[str, list[dict]] = {}
    for p in pages:
        role = p.get("role")
        if role in ROLE_LABEL:
            role_groups.setdefault(role, []).append(p)
    for role, members in sorted(role_groups.items()):
        label = ROLE_LABEL[role]
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_TYPE / f"{label}.md", label, ROLE_INTRO[role],
               bullets, f"role/{role}")
        written.append(("Types", label, len(members)))

    # R13 (audit axe 2, annexe B) : le groupement par `categorie:` écarte des pages Dev,
    # et le faisait sans le dire. On imprime combien, et surtout combien restent hors de
    # tout hub après le rattrapage par `type:` — c'est ce reste qui est un vrai trou.
    if sans_categorie:
        rattrapees = [p for p in sans_categorie if p.get("role") in ROLE_LABEL]
        orphelines = [p for p in sans_categorie if p.get("role") not in ROLE_LABEL]
        par_role: dict[str, int] = {}
        for p in orphelines:
            par_role[str(p.get("role"))] = par_role.get(str(p.get("role")), 0) + 1
        skipped.append(
            f"{len(sans_categorie)} page(s) Dev sans `categorie:` hors des hubs "
            f"MOC/Categories — dont {len(rattrapees)} rattrapée(s) par MOC/Types "
            f"({', '.join(f'{t}' for t in sorted(ROLE_LABEL))})")
        if orphelines:
            detail = ", ".join(f"{t} x{n}" for t, n in sorted(par_role.items()))
            skipped.append(f"{len(orphelines)} page(s) Dev hors de TOUT hub ({detail}) :")
            for p in sorted(orphelines, key=lambda e: e["path"]):
                skipped.append(f"    {p['path']}")

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
    for key, members in sorted(sub_groups.items()):
        label, scope, intro = wiki_meta[key]
        bullets = [bullet(p) for p in sorted(members, key=lambda e: e["nom"].lower())]
        upsert(MOC_CONCEPT / f"{label}.md", label, intro, bullets, scope)
        written.append(("Concepts", label, len(members)))

    # MOC Wiki par domaine → pointe vers les SOUS-HUBS (pas les feuilles).
    # Étage de navigation : domaine → sous-domaine → (graphe local) → feuille.
    theme_subs: dict[str, dict[str, int]] = {}
    for p in pages:
        if not p["path"].startswith("Wiki/"):
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
               bullets, dom)
        written.append(("Themes", label, len(subs)))

    for kind, label, n in written:
        print(f"  MOC/{kind}/{label}.md ({n} membre(s))")
    for s in skipped:
        print(f"  [SKIP] {s}")
    print(f"{len(written)} MOC générés / mis à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
