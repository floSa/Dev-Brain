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

# Plafond du seuil — arbitrage de floSa du 2026-09-04, sur la remontée 8 de
# AI/migration/lot-3-arborescence.md : un sous-domaine ne se promeut PAS s'il ne
# laisse AUCUNE page au niveau du domaine. Un dossier fils qui redouble son parent
# n'apporte aucune information et ajoute un niveau à la navigation.
#
# Mesuré sur deux domaines déjà migrés — « Stockage » (6 pages, toutes
# `storage/objet`) et « Automatisation no-code » (5, toutes `automation/no-code`) —
# où la règle 2 appliquée nue produisait `Stockage/Stockage objet/` et
# `Automatisation no-code/No-code/`, seuls fils de leur parent. Les deux ont été
# défaits rétroactivement le 2026-09-04.
#
# La condition est `n == total du domaine`, pas « fils unique » : deux sous-domaines
# de 5 pages qui se partagent un domaine de 10 se promeuvent tous les deux — ils
# séparent quelque chose, donc ils informent. Le plafond ne vise que le fils qui EST
# son parent. Les libellés restés dans SUB_LABEL ne sont pas retirés : la promotion
# reprendra d'elle-même le jour où le domaine gagne une seconde population.

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
    # Data & pipelines — « ### Data & pipelines · 46 pages »
    "data/scraping": "Scraping",
    "data/parsing": "Parsing",
    "data/orchestration": "Orchestration",
    "data/tableau": "DataFrames",
    "data/viz": "Visualisation",
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
    """Sous-domaines promus en dossier, d'après le seuil, son plafond et SUB_LABEL.

    Accepte les catégories de PLUSIEURS domaines : le seuil comme son plafond se
    comptent par domaine, jamais sur le total. `check_arbo.py` passe le vault entier,
    `migrate_lot3_arbo.py` un seul domaine — les deux doivent trouver le même arbre.

    Lève KeyError sur un sous-domaine promu sans libellé déclaré : il faut le lire
    dans v3-arborescence.md et l'ajouter à SUB_LABEL, jamais l'inventer.
    """
    import collections
    par_dom: dict[str, collections.Counter] = collections.defaultdict(
        collections.Counter)
    for cat in categories:
        dom = domaine(cat)
        if dom is not None:
            par_dom[dom][cat] += 1

    promus: dict[str, str] = {}
    for dom in sorted(par_dom):
        compte = par_dom[dom]
        total = sum(compte.values())
        for cat, n in sorted(compte.items()):
            if n < SEUIL or "/" not in cat:
                continue
            if n == total:
                continue  # plafond : le fils redoublerait son parent — cf. en-tête
            if cat not in SUB_LABEL:
                raise KeyError(
                    f"`{cat}` atteint {n} pages (seuil {SEUIL}) sans libellé dans "
                    f"SUB_LABEL — le lire dans AI/design/v3-arborescence.md")
            promus[cat] = SUB_LABEL[cat]
    return promus
