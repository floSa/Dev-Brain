# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""lot6_regle2_audit.py — la règle 2 corrigée, appliquée aux six lots d'avant d8f81d6.

Pour chaque fiche du périmètre : relire ses puces `## Quand NE PAS l'utiliser`
d'ORIGINE (au commit passé en argument), en extraire les renvois
« besoin → [[cible]] », puis dire, pour chacun :

  - la brique et la cible sont-elles membres de la MÊME vue `.base` ?
  - le renvoi est-il présent aujourd'hui dans la colonne `Écarter si` ?

La règle corrigée (lot-6-gabarit.md, règle 2) : le renvoi ne part au comparatif
QUE si les deux sont membres de la même vue. Sinon il reste en `Écarter si`.

Usage : uv run AI/migration/scripts/lot6_regle2_audit.py <commit-origine>
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import check_brain as cb  # noqa: E402

PERIMETRES = {
    "pilote": ["Bases de données/Vectoriel", "Bases de données/Administration"],
    "lot-1": ["Bases de données"],
    "lot-2": ["Bases de données/Relationnel", "Bases de données/Recherche"],
    "lot-3": ["Machine Learning/Vision", "Machine Learning/Serving",
              "Machine Learning/Non supervisé"],
    "lot-4": ["Machine Learning/Apprentissage profond", "Machine Learning/Interprétabilité",
              "Machine Learning/Socle", "Machine Learning/Évaluation de modèles"],
    "lot-5": ["Machine Learning/Séries temporelles", "Machine Learning/Suivi d'expériences",
              "Machine Learning/Tabulaire"],
    "lot-6": ["Machine Learning/Apprentissage par renforcement", "Machine Learning/NLP",
              "Machine Learning"],
    "lot-7": ["LLM & IA générative/Agents de code", "LLM & IA générative/Agents"],
    "lot-8": ["LLM & IA générative/Runtimes", "LLM & IA générative/Assistants",
              "LLM & IA générative/Fine-tuning"],
    "lot-9": ["LLM & IA générative/Observabilité des LLM", "LLM & IA générative/Passerelles",
              "LLM & IA générative/RAG & retrieval", "LLM & IA générative/Sortie typée",
              "LLM & IA générative/Text-to-SQL", "LLM & IA générative/Évaluation"],
    "lot-10": ["LLM & IA générative"],
    "lot-11": ["Data & pipelines/Scraping", "Data & pipelines/Parsing"],
    "lot-12": ["Data & pipelines/Orchestration", "Data & pipelines/DataFrames",
               "Data & pipelines/Visualisation"],
    "lot-13": ["Data & pipelines"],
    "lot-14": ["Outils de développement", "Outils de développement/Notebooks"],
    "lot-15": ["Statistiques & inférence", "Statistiques & inférence/Analyse factorielle",
               "Statistiques & inférence/Bayésien", "Statistiques & inférence/Tests & estimation",
               "Design & diagrammes", "Design & diagrammes/Diagrammes", "Calcul distribué"],
    "lot-16": ["Web & API", "Stockage", "Automatisation no-code", "Médias",
               "Interfaces & apps data"],
    "lot-17": ["Sécurité", "Signal & audio", "Signal & audio/Traitement", "Observabilité",
               "Réseau", "Documents", "DevOps", "Mathématiques/Optimisation"],
}

LIEN = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")


def frontmatter(txt: str) -> dict:
    if not txt.startswith("---"):
        return {}
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def pages_actives() -> list[tuple[str, dict]]:
    out = []
    for md in sorted(VAULT.rglob("*.md")):
        if cb.hors_vault(md, VAULT):
            continue
        fm = frontmatter(md.read_text(encoding="utf-8"))
        if "role" in fm:
            out.append((cb.rel(md), fm))
    return out


def bases_membres(actives) -> dict[str, set[str]]:
    """nom du .base -> ensemble des `nom:` de ses membres."""
    out = {}
    for base in sorted(VAULT.rglob("*.base")):
        if cb.hors_vault(base, VAULT):
            continue
        doc = yaml.safe_load(base.read_text(encoding="utf-8")) or {}
        filt = doc.get("filters")
        if filt is None:
            continue
        membres, ko = set(), False
        for path, fm in actives:
            r = cb.base_match(filt, path, fm)
            if r is None:
                ko = True
                break
            if r:
                membres.add(Path(path).stem)
        if not ko:
            out[cb.rel(base)] = membres
    return out


def section(txt: str, titre: str) -> str:
    m = re.search(rf"\n## {re.escape(titre)}\n(.*?)(?=\n## |\Z)", txt, re.S)
    return m.group(1) if m else ""


def colonne_ecarter(txt: str) -> str:
    """Le texte de la colonne de droite du tableau Prendre si / Écarter si."""
    sec = section(txt, "Prendre si / Écarter si")
    cells = []
    for line in sec.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        parts = [c.strip() for c in line.strip("|").split("|")]
        if len(parts) >= 2 and parts[0] != "Prendre si":
            cells.append(parts[1])
    return "\n".join(cells)


def main() -> int:
    origine = sys.argv[1] if len(sys.argv) > 1 else "d8f81d6"
    # Le pilote est DÉJÀ converti dans `origine` : ses fiches doivent se relire
    # avant sa propre conversion, sinon la section d'origine n'existe plus.
    AVANT_PILOTE = "18e6453"
    actives = pages_actives()
    membres = bases_membres(actives)
    stem_de = {Path(p).stem: p for p, _ in actives}
    roles = {Path(p).stem: fm.get("role") for p, fm in actives}

    tot = {"garde": 0, "part": 0, "manquant": 0, "surnumeraire": 0}
    for lot, dossiers in PERIMETRES.items():
        lignes = []
        parlot = {"garde": 0, "part": 0, "manquant": 0, "surnumeraire": 0}
        for path, fm in actives:
            if fm.get("role") != "brique":
                continue
            parent = str(Path(path).parent).replace("\\", "/")
            if parent not in dossiers:
                continue
            stem = Path(path).stem
            try:
                base_lecture = AVANT_PILOTE if lot == "pilote" else origine
                vieux = subprocess.run(
                    ["git", "show", f"{base_lecture}:{path}"], cwd=VAULT,
                    capture_output=True, check=True).stdout.decode("utf-8")
            except subprocess.CalledProcessError:
                continue
            neuf = (VAULT / path).read_text(encoding="utf-8")
            ecarter = colonne_ecarter(neuf)
            vues_brique = {b for b, m in membres.items() if stem in m}
            for puce in re.findall(r"^- (.+)$", section(vieux, "Quand NE PAS l'utiliser"), re.M):
                cibles = [c.strip() for c in LIEN.findall(puce)]
                cibles = [c for c in cibles if c in stem_de and c != stem
                      and roles.get(c) == "brique"]
                if not cibles:
                    continue
                for cible in cibles:
                    vues_cible = {b for b, m in membres.items() if cible in m}
                    meme_vue = bool(vues_brique & vues_cible)
                    present = f"[[{cible}]]" in ecarter
                    if meme_vue:
                        tot["part"] += 1
                        parlot["part"] += 1
                        if present:
                            tot["surnumeraire"] += 1
                            parlot["surnumeraire"] += 1
                            lignes.append(f"  SURNUMERAIRE {stem} -> {cible} "
                                          f"(meme vue : {sorted(vues_brique & vues_cible)[0]})")
                    else:
                        tot["garde"] += 1
                        parlot["garde"] += 1
                        if not present:
                            tot["manquant"] += 1
                            parlot["manquant"] += 1
                            ailleurs = "ailleurs" if f"[[{cible}]]" in neuf else "ABSENT"
                            lignes.append(f"  MANQUANT[{ailleurs}] {stem} -> {cible}   | {puce}")
        print(f"=== {lot} ===  garde={parlot['garde']} (manquants={parlot['manquant']})  "
              f"part={parlot['part']} (surnumeraires={parlot['surnumeraire']})")
        for l in lignes:
            print(l)
        if not lignes:
            print("  (rien)")
    print()
    print(f"renvois qui DOIVENT rester en Écarter si : {tot['garde']}  "
          f"— absents aujourd'hui : {tot['manquant']}")
    print(f"renvois qui PARTENT au comparatif        : {tot['part']}  "
          f"— encore présents : {tot['surnumeraire']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
