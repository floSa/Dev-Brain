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
    # LLM & IA générative — « ### LLM & IA générative · 131 pages »
    "llm/agent-de-code": "Agents de code",
    "llm/runtime": "Runtimes",
    "llm/agents": "Agents",
    "llm/finetuning": "Fine-tuning",
    "llm/text-to-sql": "Text-to-SQL",
    "llm/assistant": "Assistants",
    # Les six suivants naissent au lot 4 : les 56 notions `concept/llm` font franchir
    # le seuil à quatre sous-domaines qui n'avaient que des briques, et deux valeurs
    # nouvelles arrivent déjà au-dessus. Quatre libellés s'écartent de leur catégorie,
    # et chaque fois pour une raison mesurée (cf. remontées 8 et 17) :
    #  - « RAG » est le nom de fichier d'une NOTION QUI VIT DANS LE DOSSIER — le cas
    #    exact de `signal/traitement` au lot 4, un lien nu ne résoudrait plus de façon
    #    déterministe ; le libellé nomme donc la population, retrieval compris ;
    #  - « Observabilité » est le hub du DOMAINE homonyme, et « Observabilité LLM » est
    #    un `alias:` de la notion qui vit dans le dossier — les deux sont pris ;
    #  - « Sortie structurée » et « Sorties structurées » sont des `alias:` de
    #    `Structured outputs`, « Génération contrainte » et « Décodage contraint » des
    #    `alias:` de `Constrained decoding` — les quatre vivent dans le dossier ;
    #  - « Passerelles » au pluriel : le singulier lirait comme la notion, pas le dossier.
    "llm/rag": "RAG & retrieval",
    "llm/eval": "Évaluation",
    "llm/observabilite": "Observabilité des LLM",
    "llm/sortie-structuree": "Sortie typée",
    "llm/passerelle": "Passerelles",
    "llm/modele": "Modèles de langage",
    # Sécurité — la 5e page de `security/ia` arrive du lot 4 (`Sandboxing de code
    # généré`) et fait franchir le seuil. Le libellé n'est PAS « Sécurité des systèmes
    # IA » : il redoublerait le nom du domaine parent, défaut déjà écarté pour
    # « Inférence » sous « Statistiques & inférence » (remontée 8). Arbitrage de floSa
    # du 2026-09-05 : « Systèmes IA ».
    "security/ia": "Systèmes IA",
    # Machine Learning — « ### Machine Learning · 241 pages »
    "ml/apprentissage-profond": "Apprentissage profond",
    "ml/rl": "Apprentissage par renforcement",
    "ml/series-temporelles": "Séries temporelles",
    "ml/nlp": "NLP",
    "ml/serving": "Serving",
    "ml/vision": "Vision",
    "ml/tracking": "Suivi d'expériences",
    "ml/interpretabilite": "Interprétabilité",
    "ml/tabulaire": "Tabulaire",
    # Les trois suivants naissent au lot 4, avec la DERNIÈRE famille de notions
    # (`concept/ml`, 67). Ce sont les seules promotions que ce lot paie : la
    # remontée 35 en annonçait six, et `ml/hyperopt` (4), `ml/monitoring` (3),
    # `ml/feature-store` (2) et `ml/embeddings` (2) ne franchissent rien.
    # Les trois libellés s'écartent tous du nom de leur catégorie, et deux y sont
    # forcés par les ensembles de la remontée 26 :
    #  - « Évaluation » est le nom de fichier du hub `LLM & IA générative/Évaluation/`
    #    (ensemble nº 3) — un lien nu ne résoudrait plus de façon déterministe ;
    #  - « Non supervisé » plutôt qu'« Apprentissage non supervisé », qui est le nom
    #    d'une NOTION VIVANT DANS LE DOSSIER (ensemble nº 4) ;
    #  - « Socle » reprend le mot du corps du hub de domaine, qui appelle cette
    #    population « le socle généraliste » depuis le lot 3.
    "ml/socle": "Socle",
    "ml/eval": "Évaluation de modèles",
    "ml/non-supervise": "Non supervisé",
    # Statistiques & inférence — « ### Statistiques & inférence · 47 pages », lot 4.
    # Les libellés ne recopient pas le nom de la catégorie, et deux fois exprès :
    # « Inférence » est déjà un alias du hub « Serving » (même rôle → avertissement R5)
    # et redoublerait le nom du domaine parent ; « Analyse factorielle » nomme la
    # population réelle du sous-domaine (Prince, Fanalysis, PCA/CA/MCA/FAMD/MFA/GPA)
    # là où « Exploratoire » se confondrait avec `data/eda`.
    "stats/inference": "Tests & estimation",
    "stats/exploratoire": "Analyse factorielle",
    "stats/bayesien": "Bayésien",
    "stats/probabilite": "Probabilités",
    # Mathématiques — « ### Mathématiques · 27 pages », lot 4. Les 26 notions du
    # domaine se rangent sur les QUATRE piliers que le corps du hub nomme depuis le
    # lot 3 — algèbre linéaire, optimisation, théorie de l'information, théorie de
    # l'apprentissage — et ses quatre puces les citent toutes les 26, une seule fois
    # chacune. Les quatre franchissent le seuil et aucun n'égale le total (27) : le
    # domaine n'a plus de page à son niveau, seulement quatre sous-dossiers.
    "math/optimisation": "Optimisation",
    "math/information": "Théorie de l'information",
    "math/algebre-lineaire": "Algèbre linéaire",
    # Le libellé garde « Théorie de » que la catégorie porte déjà : « Apprentissage »
    # seul, à côté de « Machine Learning/Apprentissage profond/ », se lirait comme
    # apprentissage automatique.
    "math/theorie-apprentissage": "Théorie de l'apprentissage",
    # Signal & audio — « ### Signal & audio · 8 pages », lot 4. Le sous-dossier est
    # décrit dans v3-arborescence.md depuis le lot 3 comme « l'état visé APRÈS le
    # lot 4 » : les 2 briques `signal/traitement` étaient sous le seuil, les 5 notions
    # le font franchir. Le libellé est « Traitement » et non « Traitement du signal »
    # parce que ce dernier est le `nom:` d'une notion QUI VIT DANS LE DOSSIER — un
    # lien nu ne résoudrait plus de façon déterministe (cf. remontée 8).
    "signal/traitement": "Traitement",
    # `stats/experimentation` et `stats/causal` restent SOUS le seuil (4 et 3 pages) :
    # pas de dossier, donc pas de libellé. Le jour où l'un franchit 5, `promotions()`
    # lève un KeyError qui dit d'aller le lire dans v3-arborescence.md — c'est le
    # comportement voulu, pas un oubli.
}

# Rôles qui n'ont PAS de `categorie:` et que la dérivation ci-dessous ne concerne donc
# pas : la taxonomie ne les couvre pas, et c'est délibéré — un pattern enjambe plusieurs
# domaines par construction, une règle est transverse par définition. C'est `role:` qui
# les groupe, dans « Patterns/ » et « Rules/ » à la racine (clôture du lot 3, arbitrage
# de floSa) ; leur chemin ne se dérive pas, il se lit sur le rôle.
ROLES_SANS_CATEGORIE = {"pattern", "rule"}

# Dossiers de la racine qui ne portent pas de pages du brain.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}
# Dossiers de la racine encore en v2, dont les pages n'ont pas de chemin à vérifier.
# `Dev/` en est sorti à la clôture du lot 3 : il n'existe plus. `Wiki/` survit jusqu'au
# lot 4, qui descendra ses 297 notions `concept/*` dans l'arbre des domaines.
LEGACY = {"Wiki"}


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
