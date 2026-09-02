"""arbo.py — la dérivation `categorie:` -> chemin, écrite UNE fois.

Spec : AI/design/brain-v3.md §4 · arbre : AI/design/v3-arborescence.md

Le chemin d'une page se dérive de sa `categorie:` — personne ne choisit un dossier.
Deux consommateurs ont besoin de cette dérivation, et ils doivent l'appliquer à
l'identique, sinon le vault et son validateur divergent en silence :

  - AI/migration/scripts/migrate_lot3_arbo.py — la calcule pour DÉPLACER ;
  - AI/scripts/check_arbo.py                  — la calcule pour VÉRIFIER.

D'où ce module. Les deux tables ci-dessous sont la seule source de vérité.
"""

from __future__ import annotations

# Seuil de promotion d'un sous-domaine en dossier (brain-v3 §4, règle 2).
# Se compte sur les PAGES (`.md`) ; les vues `.base` suivent leur catégorie sans
# peser sur le seuil — un comparatif n'est pas un membre du comparatif.
SEUIL = 5

# Libellé français du domaine, un par préfixe de `categorie:`.
# Copie conforme de CAT_LABEL (AI/scripts/build_mocs.py) — 20 préfixes.
DOM_LABEL = {
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

# Préfixes de `categorie:` qui ne sont PAS des domaines et qu'une décision explicite
# rattache quand même à un dossier de l'arbre. DOM_LABEL reste la copie conforme de
# CAT_LABEL ; les exceptions vivent ici, nommées, avec leur date d'arbitrage.
#
# `skill/*` (taxonomie.md, « Skills Wiki ») désigne une pratique perso, pas un domaine
# technique. Sa seule page, `Obsidian`, va dans « Outils de développement » — tranché
# par floSa le 2026-09-04, cf. lot-3-arborescence.md, Remontées 5. `v3-arborescence.md`
# ne l'assigne à aucun domaine : il est muet, il ne contredit pas.
DOM_RATTACHE = {
    "skill": "Outils de développement",
}

# Libellé d'un sous-domaine promu en dossier. UNE ENTRÉE PAR SOUS-DOSSIER de
# AI/design/v3-arborescence.md, remplie domaine par domaine au fil du lot 3.
# Un sous-domaine qui franchit le seuil sans entrée ici fait ÉCHOUER les deux
# consommateurs plutôt que d'inventer un nom de dossier.
SUB_LABEL = {
    # Bases de données — v3-arborescence.md, « ### Bases de données · 47 pages »
    "database/vecteur": "Vectoriel",
    "database/admin": "Administration",
    "database/recherche": "Recherche",
    "database/relationnel": "Relationnel",
    # Outils de développement — « ### Outils de développement · 19 pages »
    "devtools/notebook": "Notebooks",
    # Design & diagrammes — « ### Design & diagrammes · 7 pages »
    "design/diagramme": "Diagrammes",
    # Stockage — « ### Stockage · 6 pages »
    "storage/objet": "Stockage objet",
    # Automatisation no-code — « ### Automatisation no-code · 5 pages »
    "automation/no-code": "No-code",
}

# Dossiers de la racine qui ne portent pas de pages du brain.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}
# Dossiers de la racine encore en v2, dont les pages n'ont pas de chemin à vérifier.
LEGACY = {"Dev", "Wiki"}


def domaine(categorie: str) -> str | None:
    """Libellé du dossier de domaine d'une `categorie:`, ou None si hors table."""
    pfx = (categorie or "").split("/")[0]
    return DOM_LABEL.get(pfx) or DOM_RATTACHE.get(pfx)


def dossier_attendu(categorie: str, promus: dict[str, str]) -> str | None:
    """Chemin du dossier d'accueil, relatif à la racine. None si domaine inconnu.

    `promus` : {categorie complète: libellé du sous-dossier} — les sous-domaines qui
    ont franchi le seuil. Calculé par `promotions()` sur la population réelle.
    """
    dom = domaine(categorie)
    if dom is None:
        return None
    sub = promus.get(categorie)
    return f"{dom}/{sub}" if sub else dom


def promotions(categories: list[str]) -> dict[str, str]:
    """Sous-domaines promus en dossier, d'après le seuil et SUB_LABEL.

    Lève KeyError sur un sous-domaine promu sans libellé déclaré : il faut le lire
    dans v3-arborescence.md et l'ajouter à SUB_LABEL, jamais l'inventer.
    """
    import collections
    compte = collections.Counter(categories)
    promus: dict[str, str] = {}
    for cat, n in sorted(compte.items()):
        if n < SEUIL or "/" not in cat:
            continue
        if cat not in SUB_LABEL:
            raise KeyError(
                f"`{cat}` atteint {n} pages (seuil {SEUIL}) sans libellé dans "
                f"SUB_LABEL — le lire dans AI/design/v3-arborescence.md")
        promus[cat] = SUB_LABEL[cat]
    return promus
