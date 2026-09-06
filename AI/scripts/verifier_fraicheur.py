# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""verifier_fraicheur.py — re-vérifie à froid les faits périssables des fiches Dev.

Spécification : AI/audit/rapports/axe-4-fraicheur.md, annexe B (+ constats C2, C5, C8).

C'est un RAPPORT, pas un validateur : code de retour **0 sur les constats**.
Bloquer un commit sur la santé d'un dépôt tiers rendrait le vault otage de l'amont.
Une seule exception, posée au lot 8 : **3** quand l'autotest de démarrage montre
qu'une règle est MUETTE — filtre de section qui ne matche plus rien après une
refonte de gabarit. Là, ce n'est pas l'amont qui est en panne, c'est ce script, et
c'est ce silence-là qui a laissé la règle C2 morte pendant tout le lot 6.

Périmètre : `role: brique` **et** `role: comparatif` (les onze puces datées de fin
de vie vivent sur les comparatifs — cf. `comparatifs_vs_maturite`, règle C2').

Ce qu'il refuse de faire (annexe B) : aucun mode --fix ; il n'écrit jamais dans Dev/,
Wiki/, MOC/, Documentation/, Templates/ ; il ne réécrit ni un url_repo transféré ni une
url_docs détournée ; il ne déduit jamais licence_type du spdx_id (NOASSERTION se
signale, ne se traduit pas) ; il ne régénère ni brain-index.json ni les MOC ; il
n'exige aucun jeton GitHub. Sa seule sortie fichier est AI/index/fraicheur.json.

Usage : uv run AI/scripts/verifier_fraicheur.py [--limit N] [--seuil-jours 365]
                                                [--age-max-jours 7] [--graine N]
Les règles hors ligne (C2, C5, C4) tournent toujours sur les 336 fiches : elles ne
coûtent aucun appel. --limit ne borne que les sondes réseau. La reprise saute les
fiches déjà sondées depuis moins de --age-max-jours. GITHUB_TOKEN optionnel dans
l'environnement (60 appels/h sans, 5000 avec) — jamais écrit dans le vault.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/verifier_fraicheur.py")

VAULT = Path(__file__).resolve().parents[2]
SORTIE = VAULT / "AI" / "index" / "fraicheur.json"
UA = {"User-Agent": "devbrain-verifier-fraicheur"}

GH_SLUG = re.compile(r"^https?://github\.com/([^/\s]+)/([^/\s?#]+?)(?:\.git)?/?$")
# C2 : sections qui parlent du sujet lui-même. **Réécrites le 2026-09-06, à la clôture
# du lot 6** : les quatre noms d'avant — « Pourquoi », « Déploiement & coût »,
# « Installation & plateformes », « Pièges » — n'existent plus sur aucune des 337 fiches,
# et `lignes_sujet()` ne rendait donc plus une seule ligne. La règle C2
# (`corps_declin_vs_maturite_vive`) était morte sur le vault entier, en silence : le
# script sort 0 en toutes circonstances, et une règle qui ne trouve rien ressemble à une
# règle satisfaite. Correspondance du lot 6 : `Pourquoi` → `Définition` ;
# `Déploiement & coût` et `Installation & plateformes` → `Mise en œuvre` ; `Pièges`
# dissoute vers la colonne `Écarter si` du tableau de décision et vers `Définition`.
SECTIONS = {"## Définition", "## Mise en œuvre", "## Prendre si / Écarter si",
            "## Retours"}
DECLIN = re.compile(r"dormant|déclin(?:e|ant)?\b|(?:plus|non) maintenu|"
                    r"maintenance (?:très )?ralentie|sans commit depuis", re.I)
# FIN_DE_VIE — les faits de CYCLE DE VIE, ajoutés au lot 8. `DECLIN` décrit un
# projet qui ralentit ; ceux-ci décrivent un projet dont la vie s'arrête, et ce
# sont eux que portent les onze puces datées des pages de comparatif : un dépôt
# archivé, un rachat suivi d'un passage en maintenance mode, un service hébergé
# fermé, une bascule de licence en BSL, un tier fermé aux nouveaux clients.
# Cherchés dans les DEUX périmètres — une fiche qui écrit « dépôt archivé » en
# gardant `maturite: production` porte exactement le même défaut.
FIN_DE_VIE = re.compile(
    r"d[ée]p[ôo]t\s+\*{0,2}archiv|archiv[ée]e?\s+(?:le|depuis)|maintenance mode|"
    r"rachet[ée]\s+par|service h[ée]berg[ée]\s+\*{0,2}arr[êe]t|"
    r"(?:pass[ée]|bascul[ée])\s+en\s+\*{0,2}BSL|"
    r"ferm[ée]\s+aux nouveaux|maintenance\s+(?:s'arr[êe]te|arr[êe]t[ée]e)", re.I)
# Annexe C §3 : formulations qui présentent une version comme *courante*.
VERSION_COURANTE = re.compile(r"la version courante|dernière version|"
                              r"est la version activement développée", re.I)
SPDX_RE = re.compile(r"\b(?:Apache|A?GPL|LGPL|BSD|MPL|CC0|CC-BY|EPL|MIT|BUSL|SSPL|"
                     r"Elastic|Artistic|BSL)-[\d.]+(?:-[\w+]+)*", re.I)
PYTHON_RE = re.compile(r"Python\s*[≥><=]*\s*3\.\d+")
# Licences non-OSI : incompatibles avec licence_type: open-source (table explicite).
SPDX_FERMEES = {"SSPL-1.0", "BUSL-1.1", "BUSL-1.0", "Elastic-2.0", "FSL-1.1-ALv2",
                "FSL-1.1-MIT", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "Commons-Clause"}
# Tri de la sortie humaine : du plus grave au plus mineur.
GRAVITE = ["depot_disparu", "url_morte", "version_perimee", "depot_transfere",
           "corps_declin_vs_maturite_vive", "comparatif_declin_vs_maturite_vive",
           "depot_archive", "push_ancien",
           "deprecie_sans_alternative",
           "licence_divergente", "url_domaine_change"]
# Le lot 2 de la migration v3 a supprimé `status:` et `remplace_par:`. Les cinq règles
# qui les lisaient sont reportées sur les deux champs qui survivent :
#   status != actif                  -> maturite == deprecated   (le seul champ qui dit
#                                       encore qu'une brique est morte)
#   status_maturite_incoherents      -> supprimée : elle croisait deux champs dont l'un
#                                       n'existe plus, il ne reste rien à croiser
#   abandonne_sans_remplacement      -> deprecie_sans_alternative : `alternatives:` a
#                                       absorbé `remplace_par:` (les 7 cibles des 4 fiches
#                                       qui le portaient y étaient déjà)
MATURITE_MORTE = "deprecated"


def parse(texte: str) -> tuple[dict | None, str]:
    """Frontmatter + corps, même découpage que check_brain.py."""
    if not texte.startswith("---"):
        return None, texte
    parts = texte.split("---", 2)
    if len(parts) < 3:
        return None, texte
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, parts[2]
    return (fm if isinstance(fm, dict) else None), parts[2]


# Dossiers de la racine qui ne portent PAS de pages du brain. `Templates/` en est,
# et son absence était un défaut de périmètre corrigé au lot 8 : `Service-Dev.md` et
# `Outil-Dev.md` portent `role: brique`, donc le script annonçait « 339 fiches »
# quand le vault en compte 337, et sondait les URL de deux gabarits.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}


def _pages(role: str) -> list[tuple[str, dict, str]]:
    """Les pages d'un `role:`, triées par chemin."""
    out = []
    for p in sorted(VAULT.rglob("*.md"), key=lambda q: q.as_posix()):
        parts = p.relative_to(VAULT).parts
        if not parts or parts[0] in NON_PAGES:
            continue
        fm, corps = parse(p.read_text(encoding="utf-8"))
        if fm and fm.get("role") == role:
            out.append((p.relative_to(VAULT).as_posix(), fm, corps))
    return out


def fiches() -> list[tuple[str, dict, str]]:
    """Les pages `role: brique` du vault, triées par chemin (annexe C §1).

    Balayait `Dev/` avant le lot 3 ; balaye la racine depuis, puisque les briques
    descendent dans l'arbre des domaines. Les dossiers d'outillage sont écartés —
    un worktree est une copie complète du vault, le balayer doublerait tout, et
    `Templates/` porte deux gabarits en `role: brique` qui ne sont pas des fiches.
    """
    return _pages("brique")


def comparatifs() -> list[tuple[str, dict, str]]:
    """Les pages `role: comparatif`, entrées dans le périmètre au lot 8.

    Onze puces datées y vivent — Helicone en maintenance mode depuis le rachat
    Mintlify, le dépôt OSS de Vanna archivé le 29 mars 2026, TorchServe archivé le
    7 août 2025, Seldon basculé en BSL le 22 janvier 2024, le service Neptune
    arrêté le 5 mars 2026… Ce sont exactement les faits que ce script existe pour
    surveiller, et il ne les voyait pas : son périmètre s'arrêtait à `role: brique`.
    Une page de comparatif est une page comme une autre depuis la clôture du lot 5.
    """
    return _pages("comparatif")


# Wikilinks du corps. Depuis le lot 3, les liens du vault sont NUS : le test
# historique `"[[Dev/" not in ligne` ne repérait plus une seule citation de brique.
# On résout donc par nom de fichier, comme Obsidian — cf. AI/migration/lot-3-arborescence.md.
LIEN_RE = re.compile(r"\[\[([^\]|#]+)")
_BRIQUES: set[str] | None = None


def briques() -> set[str]:
    """Noms de fichier (minuscules) des pages `role: brique`. Calculé une fois."""
    global _BRIQUES
    if _BRIQUES is None:
        _BRIQUES = {c.rsplit("/", 1)[-1][:-3].lower() for c, _, _ in fiches()}
    return _BRIQUES


def cite_une_brique(ligne: str) -> bool:
    """La ligne cite-t-elle une AUTRE fiche brique ? (nu ou qualifié, indifféremment)"""
    return any(c.strip().split("/")[-1].lower() in briques()
               for c in LIEN_RE.findall(ligne))


def lignes_sujet(corps: str):
    """Lignes des sections qui parlent du sujet, hors lignes citant une autre fiche."""
    section = None
    for ligne in corps.splitlines():
        if ligne.startswith("## "):
            section = ligne.strip()
        elif section in SECTIONS and not cite_une_brique(ligne):
            yield ligne.strip()


def majeure_affirmee(nom: str, corps: str) -> tuple[bool, int | None]:
    """(la fiche affirme-t-elle une version courante ?, majeure affirmée)."""
    trouve = False
    for ligne in corps.splitlines():
        if cite_une_brique(ligne) or not VERSION_COURANTE.search(ligne):
            continue
        trouve = True
        s = PYTHON_RE.sub(" ", SPDX_RE.sub(" ", ligne))
        maj = [int(m) for m in re.findall(r"\bv?(\d+)\.\d+(?:\.\d+)?\b", s)]
        maj += [int(m) for m in re.findall(rf"{re.escape(nom)}\s+(\d+)\b", s, re.I)]
        if maj:
            return True, max(maj)
    return trouve, None


def hors_ligne(fm: dict, corps: str) -> list[tuple[str, str, str, str]]:
    """Règles sans réseau (C2, C5, C4). Tuple : code, valeur brain, constaté, jeton."""
    sig, mat = [], fm.get("maturite")
    if mat == MATURITE_MORTE and not fm.get("alternatives"):
        etat = "alternatives=[]" if "alternatives" in fm else "alternatives absent"
        sig.append(("deprecie_sans_alternative", f"maturite={mat}", etat, f"maturite={mat}"))
    if mat is not None and mat != MATURITE_MORTE:
        for ligne in lignes_sujet(corps):
            if DECLIN.search(ligne) or FIN_DE_VIE.search(ligne):
                sig.append(("corps_declin_vs_maturite_vive", f"maturite: {mat}",
                            ligne[:90], ""))
                break
    return sig


# Une puce de comparatif : `- [[Cible]] — <ce qui la départage>`. Seule l'ENTRÉE de
# la puce désigne la brique dont elle parle ; un lien cité au milieu de la glose
# parle d'autre chose.
PUCE_COMPARATIF = re.compile(r"^\s*-\s*\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]\s*[—-]\s*(.+)$")


def comparatifs_vs_maturite(cmps, index) -> list[tuple[str, str, str, str, str]]:
    """C2' — un comparatif décrit la fin de vie d'une brique que son frontmatter dit
    vivante. Rend : (chemin de la BRIQUE, code, valeur brain, constaté, comparatif).

    C'est une règle CROISÉE, et c'est ce qui la rend nécessaire : le fait est écrit
    sur le comparatif, le champ qu'il contredit vit sur la fiche, et personne ne
    relit les deux ensemble. Brancher le script sur `role: comparatif` SANS cette
    règle n'aurait rien produit — les deux règles hors ligne existantes lisent
    `maturite:` et `alternatives:`, qu'un comparatif ne porte pas ; le compteur
    serait resté à zéro, ce qui ressemble à une règle satisfaite. C'est le piège que
    le lot 6 a trouvé sur `SECTIONS`, et il n'était pas à retomber dedans.
    """
    sig = []
    for chemin, _, corps in cmps:
        for ligne in corps.splitlines():
            m = PUCE_COMPARATIF.match(ligne)
            if not m:
                continue
            glose = m.group(2)
            if not (DECLIN.search(glose) or FIN_DE_VIE.search(glose)):
                continue
            entree = index.get(m.group(1).split("/")[-1].strip())
            if entree is None:
                continue
            chemin_brique, fm = entree
            mat = fm.get("maturite")
            if mat is None or mat == MATURITE_MORTE:
                continue
            sig.append((chemin_brique, "comparatif_declin_vs_maturite_vive",
                        f"maturite: {mat}", glose[:80],
                        chemin.rsplit("/", 1)[-1][:-3]))
    return sig


def http_final(url: str) -> tuple[int, str]:
    """Code HTTP final et domaine final, redirections suivies (C8)."""
    for methode in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=methode, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status, urlsplit(r.url).netloc
        except urllib.error.HTTPError as e:
            if methode == "HEAD" and e.code in (403, 405, 429, 501):
                continue
            return e.code, urlsplit(getattr(e, "url", url) or url).netloc
        except OSError:
            return 0, ""
    return 0, ""


def http_json(url: str, token: str | None) -> tuple[dict | None, int]:
    """GET JSON, redirections suivies — c'est la redirection qui révèle un transfert."""
    req = urllib.request.Request(url, headers={**UA, "Accept": "application/vnd.github+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r), r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except OSError:
        return None, 0


def sonder(fm: dict, corps: str, token: str | None) -> dict:
    """Un appel API dépôt + PyPI si version affirmée + HEAD sur les URL déclarées."""
    rec: dict = {"sonde_le": date.today().isoformat()}
    m = GH_SLUG.match((fm.get("url_repo") or "").strip())
    if m:
        slug = f"{m.group(1)}/{m.group(2)}"
        data, code = http_json(f"https://api.github.com/repos/{slug}", token)
        rec["repo"] = slug
        rec["http_api"] = code
        if data:
            rec |= {"full_name": data.get("full_name"),
                    "archived": bool(data.get("archived")),
                    "pushed_at": (data.get("pushed_at") or "")[:10],
                    "license_spdx": ((data.get("license") or {}).get("spdx_id")),
                    "stars": data.get("stargazers_count"),
                    "default_branch": data.get("default_branch")}
    affirme, majeure = majeure_affirmee(str(fm.get("nom") or ""), corps)
    if affirme:
        rec["majeure_affirmee"] = majeure
        vus = []
        for cand in [fm.get("nom"), *(fm.get("alias") or [])]:
            pkg = str(cand or "").strip().lower().replace(" ", "-")
            if not pkg or pkg in vus:
                continue
            vus.append(pkg)
            data, _ = http_json(f"https://pypi.org/pypi/{pkg}/json", None)
            if data:
                rec |= {"pypi": pkg, "pypi_version": (data.get("info") or {}).get("version")}
                break
            if len(vus) >= 3:
                break
    rec["urls"] = {}
    for champ in ("url_repo", "url_docs"):
        url = (fm.get(champ) or "").strip()
        if url.startswith("http"):
            code, netloc = http_final(url)
            rec["urls"][champ] = {"url": url, "code": code, "netloc_final": netloc}
    return rec


def en_ligne(fm: dict, rec: dict, seuil: int) -> list[tuple[str, str, str, str]]:
    """Règles dérivées des faits sondés — recalculées à chaque passe depuis fraicheur.json."""
    sig, mat = [], fm.get("maturite")
    if rec.get("http_api") == 404:
        sig.append(("depot_disparu", rec.get("repo", ""), "HTTP 404 sur l'API", "404"))
    plein = rec.get("full_name")
    if plein and rec.get("repo") and plein.lower() != rec["repo"].lower():
        sig.append(("depot_transfere", rec["repo"], plein, plein))
    if rec.get("archived") and mat != MATURITE_MORTE:
        sig.append(("depot_archive", f"maturite={mat}", "archived=true", "archived"))
    pushe = rec.get("pushed_at")
    if pushe and mat is not None and mat != MATURITE_MORTE:
        jours = (date.today() - date.fromisoformat(pushe)).days
        if jours > seuil:
            sig.append(("push_ancien", f"maturite: {mat}",
                        f"pushed_at={pushe} ({jours} j)", f"{jours}j"))
    spdx, lt = rec.get("license_spdx"), fm.get("licence_type")
    if "license_spdx" in rec and lt:
        if spdx in (None, "NOASSERTION", "NONE", ""):
            sig.append(("licence_divergente", f"licence_type={lt}",
                        f"spdx={spdx or 'aucun'} — lecture humaine requise",
                        f"spdx={spdx or 'aucun'}"))
        elif lt == "open-source" and spdx in SPDX_FERMEES:
            sig.append(("licence_divergente", f"licence_type={lt}", f"spdx={spdx}",
                        f"spdx={spdx}"))
    maj, pv = rec.get("majeure_affirmee"), rec.get("pypi_version")
    if maj and pv and re.match(r"\d+", pv) and int(re.match(r"\d+", pv).group()) > maj:
        sig.append(("version_perimee", f"corps : majeure {maj}",
                    f"{rec.get('pypi')} {pv} sur PyPI", f"{maj}->{pv}"))
    for champ, u in (rec.get("urls") or {}).items():
        if u["code"] >= 400 or u["code"] == 0:
            sig.append(("url_morte", f"{champ}={u['url']}", f"code {u['code']}",
                        f"{champ}:{u['code']}"))
        elif u["netloc_final"] and u["netloc_final"] != urlsplit(u["url"]).netloc:
            sig.append(("url_domaine_change", urlsplit(u["url"]).netloc,
                        f"{u['netloc_final']} ({champ})", u["netloc_final"]))
    return sig


def main() -> int:
    ap = argparse.ArgumentParser(description="Rapport de fraîcheur du DevBrain (ne corrige rien).")
    ap.add_argument("--limit", type=int, default=None,
                    help="nombre max de fiches sondées en ligne sur cette passe")
    ap.add_argument("--seuil-jours", type=int, default=365,
                    help="seuil du code push_ancien (question ouverte 1 : à arbitrer)")
    ap.add_argument("--age-max-jours", type=int, default=7,
                    help="reprise : ne pas re-sonder une fiche sondée depuis moins de N jours")
    ap.add_argument("--graine", type=int, default=None,
                    help="tirage reproductible de l'échantillon sondé (annexe C §1)")
    args = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or None

    pages = fiches()
    cmps = comparatifs()
    index_briques = {str(fm.get("nom")): (chemin, fm) for chemin, fm, _ in pages
                     if fm.get("nom")}

    # ------------------------------- AUTOTEST : une règle muette est une règle morte
    # Le lot 6 a trouvé la règle C2 morte sur le vault ENTIER, en silence : la
    # constante `SECTIONS` portait les quatre noms de sections d'avant le gabarit,
    # `lignes_sujet()` ne rendait plus une seule ligne, et comme ce script sort 0 en
    # toutes circonstances, « zéro signalement » ressemblait à « tout va bien ».
    # Le contrat « toujours 0 » protège le vault d'un dépôt tiers en panne ; il ne
    # couvre pas le script lui-même en panne. Un filtre sur un nom de section est
    # cassé par toute refonte de gabarit, et il ne le dit pas : on le lui fait dire.
    lignes_balayees = sum(1 for _, _, corps in pages for _ in lignes_sujet(corps))
    puces_comparatif = sum(
        1 for _, _, corps in cmps for ligne in corps.splitlines()
        if PUCE_COMPARATIF.match(ligne))
    muettes = []
    if pages and lignes_balayees == 0:
        muettes.append("`SECTIONS` ne matche AUCUNE section des "
                       f"{len(pages)} fiches — la règle C2 est morte")
    if cmps and puces_comparatif == 0:
        muettes.append("`PUCE_COMPARATIF` ne matche AUCUNE puce des "
                       f"{len(cmps)} comparatifs — la règle C2' est morte")
    if muettes:
        print("!" * 78)
        print("verifier_fraicheur : REGLE(S) MORTE(S) — le script ne mesure plus "
              "ce qu'il croit mesurer.")
        for m in muettes:
            print(f"  - {m}")
        print("Un compteur a zero n'est pas une bonne nouvelle. Reparer les motifs "
              "avant de lire\nquoi que ce soit de la sortie ci-dessous.")
        print("!" * 78)

    ancien = json.loads(SORTIE.read_text(encoding="utf-8")) if SORTIE.exists() else {}
    aujourdhui = datetime.now(timezone.utc).date()

    # Le side-car est indexé par CHEMIN de page, et un chemin bouge. Constaté à la
    # clôture du lot 8 : ses 101 entrées étaient toutes en `Dev/Outils/…` et
    # `Dev/Services/…`, chemins qui n'existent plus depuis le lot 3. Aucune ne
    # correspondait plus à une page, donc `frais()` ne trouvait jamais rien : le
    # mécanisme de reprise — « ne pas re-sonder une fiche sondée depuis moins de
    # --age-max-jours » — était mort, et le script re-sondait tout le vault à chaque
    # passage sans que rien ne le dise. Troisième défaut de la même famille dans ce
    # seul fichier, après `SECTIONS` et le périmètre : une clé dérivée d'un chemin ou
    # d'un nom de section est cassée par toute réorganisation, et elle se taît.
    # On ne peut pas y remédier par une clé stable — une page n'a pas d'identifiant —
    # mais on peut refuser de se taire.
    connus = {chemin for chemin, _, _ in pages} | {chemin for chemin, _, _ in cmps}
    orphelines = sorted(set(ancien) - connus)
    if orphelines:
        print(f"verifier_fraicheur : {len(orphelines)} entrée(s) du side-car ne visent "
              "plus aucune page — page renommée, déplacée ou supprimée. Leurs sondes "
              "en ligne sont perdues et seront refaites.")
        for chemin in orphelines[:5]:
            print(f"  - {chemin}")
        if len(orphelines) > 5:
            print(f"  … et {len(orphelines) - 5} autre(s)")

    def frais(chemin: str) -> bool:
        d = (ancien.get(chemin) or {}).get("sonde_le")
        return bool(d) and (aujourdhui - date.fromisoformat(d)).days < args.age_max_jours

    # Sondable = au moins une URL déclarée ; l'appel API n'a lieu que si url_repo
    # est de forme github.com/owner/repo (316 fiches), les URL sont testées partout.
    a_sonder = [c for c, fm, _ in pages
                if any((fm.get(ch) or "").strip().startswith("http")
                       for ch in ("url_repo", "url_docs"))]
    if args.graine is not None:  # échantillon reproductible tiré sur les 336 fiches
        random.seed(args.graine)
        tires = set(random.sample([c for c, _, _ in pages], args.limit or 30))
        a_sonder = [c for c in a_sonder if c in tires]
    a_sonder = [c for c in a_sonder if not frais(c)]  # reprise sur le side-car
    if args.limit is not None and args.graine is None:
        a_sonder = a_sonder[:args.limit]
    a_sonder_set = set(a_sonder)

    resultat, lignes = {}, []
    for chemin, fm, corps in pages:
        rec = dict(ancien.get(chemin) or {})
        if chemin in a_sonder_set:
            rec = sonder(fm, corps, token)
        sig = hors_ligne(fm, corps) + (en_ligne(fm, rec, args.seuil_jours) if rec else [])
        if not sig and not rec:
            continue
        rec["signalements"] = [f"{c}:{j}" if j else c for c, _, _, j in sig]
        resultat[chemin] = rec
        for code, brain, constate, _ in sig:
            lignes.append((GRAVITE.index(code) if code in GRAVITE else 99,
                           chemin, code, brain, constate))

    # C2' — les faits de fin de vie écrits sur un comparatif, confrontés au
    # `maturite:` de la brique dont la puce parle. Versés dans le side-car sous la
    # fiche concernée, pas sous le comparatif : c'est la fiche qui porte le champ à
    # corriger, et c'est là qu'on veut retrouver le signalement.
    for chemin, code, brain, constate, source in comparatifs_vs_maturite(cmps, index_briques):
        rec = resultat.setdefault(chemin, dict(ancien.get(chemin) or {}))
        rec.setdefault("signalements", [])
        jeton = f"{code}:{source}"
        if jeton not in rec["signalements"]:
            rec["signalements"].append(jeton)
        lignes.append((GRAVITE.index(code) if code in GRAVITE else 99,
                       chemin, code, brain, f"{constate}  [{source}]"))

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(json.dumps(dict(sorted(resultat.items())), ensure_ascii=False,
                                 indent=1, sort_keys=True) + "\n", encoding="utf-8")

    print(f"# Fraîcheur du brain — {aujourdhui.isoformat()}")
    print(f"{len(cmps)} comparatif(s) lus · {puces_comparatif} puce(s) confrontées "
          f"au `maturite:` de leur cible · {lignes_balayees} ligne(s) de fiche balayées")
    print(f"{len(pages)} fiches Dev lues · {len(a_sonder)} sondées en ligne "
          f"(jeton : {'oui' if token else 'non'}) · seuil push_ancien : "
          f"{args.seuil_jours} j · {len(lignes)} signalement(s)\n")
    print(f"{'fiche':<34} {'code':<31} {'valeur brain':<26} valeur constatée")
    print("-" * 130)
    for _, chemin, code, brain, constate in sorted(lignes):
        nom = chemin.rsplit("/", 1)[-1][:-3]
        print(f"{nom[:33]:<34} {code:<31} {brain[:25]:<26} {constate}")
    print(f"\nSide-car écrit : {SORTIE.relative_to(VAULT).as_posix()} "
          f"({len(resultat)} fiche(s)). Rapport seul : rien n'a été corrigé.")
    # 0 sur les CONSTATS — un dépôt tiers en panne ne bloque pas le vault (annexe B).
    # 3 si l'AUTOTEST a parlé : là, ce n'est pas l'amont qui est en panne, c'est ce
    # script. Le contrat « toujours 0 » n'a jamais couvert ce cas, et c'est ce
    # silence qui a laissé la règle C2 morte pendant tout le lot 6.
    return 3 if muettes else 0


if __name__ == "__main__":
    sys.exit(main())
