# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""audit_mesures.py — etat des lieux chiffre du DevBrain, pour les audits.

Ne modifie RIEN. Lit Dev/ + Wiki/ + Documentation/ + AI/scripts/ et ecrit un
rapport Markdown reproductible sur stdout. Sert de socle factuel commun aux six
axes d'audit (cf. AI/audit/README.md) : un auditeur commence par le relancer
pour verifier que les chiffres du brief sont toujours ceux du vault.

Usage : uv run AI/scripts/audit_mesures.py > AI/audit/mesures-<date>.md
"""

from __future__ import annotations

import collections
import glob
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/audit_mesures.py")

VAULT = Path(__file__).resolve().parents[2]
DOC = VAULT / "Documentation" / "general"


def parse(path: Path):
    t = path.read_text(encoding="utf-8")
    if not t.startswith("---"):
        return None, ""
    parts = t.split("---", 2)
    if len(parts) < 3:
        return None, ""
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, ""
    return (fm if isinstance(fm, dict) else None), parts[2]


def declared_categories() -> set[str]:
    """Meme parseur que check_brain : seuls les blocs ``` NUS de taxonomie.md comptent.

    Un fence a langue (```famille) porte un autre vocabulaire ferme — l'axe famille —
    et n'entre pas dans le compte des categories.
    """
    txt = (DOC / "taxonomie.md").read_text(encoding="utf-8")
    body = "\n".join(c for langue, c in
                     re.findall(r"^```([a-z0-9-]*)\n(.*?)^```", txt, re.S | re.M)
                     if not langue)
    cats: set[str] = set()
    for m in re.finditer(r"([a-z][\w-]*)/\{([^}]*)\}", body, re.S):
        for item in re.split(r"[,\n]", m.group(2)):
            if item.strip():
                cats.add(f"{m.group(1)}/{item.strip()}")
    body2 = re.sub(r"[a-z][\w-]*/\{[^}]*\}", "", body, flags=re.S)
    for tok in re.findall(r"^[a-z][\w-]*(?:/[a-z][\w-]*)?$", body2, re.M):
        cats.add(tok.strip())
    return cats


def main() -> int:
    pages: dict[str, tuple[dict, str]] = {}
    for pat in ("Dev/**/*.md", "Wiki/**/*.md"):
        for f in glob.glob(str(VAULT / pat), recursive=True):
            p = Path(f)
            fm, body = parse(p)
            if fm:
                pages[p.relative_to(VAULT).as_posix()] = (fm, body)

    out: list[str] = []
    w = out.append
    w("# Mesures — etat des lieux du DevBrain")
    w("")
    w(f"Genere par `AI/scripts/audit_mesures.py` sur **{len(pages)} pages** de `Dev/` et `Wiki/`.")
    w("Relancer avant tout audit : `uv run AI/scripts/audit_mesures.py`.")
    w("")

    # ---------- 1. taxonomie
    used = collections.Counter(fm.get("categorie") for fm, _ in pages.values() if fm.get("categorie"))
    declared = declared_categories()
    unused = sorted(declared - set(used))
    singles = sorted(c for c, n in used.items() if n == 1)
    orphan_cat = sorted(set(used) - declared)
    w("## 1. Taxonomie")
    w("")
    w(f"- Categories declarees dans `taxonomie.md` : **{len(declared)}**")
    w(f"- Categories reellement portees par une page : **{len(used)}**")
    w(f"- Declarees mais **jamais utilisees** : **{len(unused)}** — {', '.join(f'`{c}`' for c in unused) or 'aucune'}")
    w(f"- Categories a **une seule page** : **{len(singles)}** — {', '.join(f'`{c}`' for c in singles) or 'aucune'}")
    w(f"- Categories portees par une page mais **hors taxonomie** : {len(orphan_cat)} (doit rester 0, check_brain le bloque)")
    w("")
    w("Repartition par prefixe de domaine :")
    w("")
    head = collections.Counter(c.split("/")[0] for c in used.elements())
    for k, n in head.most_common():
        w(f"- `{k}/*` — {n} page(s)")
    w("")

    # ---------- 2. roles et gabarits
    w("## 2. Roles et gabarits")
    w("")
    by_role = collections.Counter(fm.get("role") for fm, _ in pages.values())
    for t, n in by_role.most_common():
        w(f"- `role: {t}` — {n} page(s)")
    w("")
    for t in sorted({fm.get("role") for fm, _ in pages.values() if fm.get("role")}):
        sub = [fm for fm, _ in pages.values() if fm.get("role") == t]
        keys = collections.Counter(k for fm in sub for k in fm)
        variable = {k: v for k, v in keys.items() if v != len(sub)}
        w(f"- `{t}` ({len(sub)} pages) — champs a geometrie variable : "
          + (", ".join(f"`{k}` sur {v}/{len(sub)}" for k, v in sorted(variable.items())) if variable
             else "**aucun, gabarit uniforme**"))
    w("")

    # ---------- 3. themes
    voc = set(re.findall(r"^\|\s*`([a-z0-9-]+)`", (DOC / "themes.md").read_text(encoding="utf-8"), re.M))
    dom_used = collections.Counter(d for fm, _ in pages.values() for d in (fm.get("domaines") or []))
    sans = sum(1 for fm, _ in pages.values() if not fm.get("domaines"))
    w("## 3. Themes (`domaines:`)")
    w("")
    w(f"- Vocabulaire declare : {', '.join(f'`{v}`' for v in sorted(voc))}")
    w("- Emploi : " + ", ".join(f"`{k}` x{n}" for k, n in dom_used.most_common()))
    w(f"- Valeurs **hors vocabulaire** : {sorted(set(dom_used) - voc) or 'aucune'} (non verifie par check_brain)")
    w(f"- Pages **sans** `domaines:` : **{sans}** (dont les `type: service`, a qui le gabarit l'interdit)")
    w("")

    # ---------- 4. synchro des pitchs
    pitch = {fm.get("nom"): (fm.get("pitch") or "").strip() for fm, _ in pages.values() if fm.get("nom")}
    desync: list[tuple[str, str]] = []
    checked = 0
    for f, (fm, body) in pages.items():
        sec = re.search(r"\n## Alternatives\n(.*?)(?=\n## |\Z)", body, re.S)
        if not sec:
            continue
        for line in sec.group(1).splitlines():
            m = re.match(r"\s*-\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]\s*[—-]\s*(.+)", line)
            if not m:
                continue
            target = (m.group(2) or m.group(1)).split("/")[-1]
            if not pitch.get(target):
                continue
            checked += 1
            if m.group(3).strip().rstrip(".") != pitch[target].rstrip("."):
                desync.append((f, target))
    w("## 4. Synchronisation des pitchs reinjectes")
    w("")
    w("Regle cardinale du skill `enrichir-brain` : la ligne affichee pour une cible dans une")
    w("section `## Alternatives` doit etre **exactement** le `pitch:` courant de cette cible.")
    w("**Aucun script ne le verifie aujourd'hui.**")
    w("")
    w(f"- Lignes verifiables : **{checked}**")
    w(f"- Lignes **desynchronisees** : **{len(desync)}**")
    for f, t in desync:
        w(f"  - `{f}` affiche un pitch perime de **{t}**")
    w("")

    # ---------- 5. coherence frontmatter / section
    gap = []
    for f, (fm, body) in pages.items():
        if fm.get("role") != "brique":
            continue
        front = {re.sub(r".*\|", "", a).rstrip("]").split("/")[-1] for a in (fm.get("alternatives") or [])}
        sec = re.search(r"\n## Alternatives\n(.*?)(?=\n## |\Z)", body, re.S)
        insec = {(b or a).split("/")[-1] for a, b in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", sec.group(1))} if sec else set()
        if front - insec:
            gap.append((f, sorted(front - insec)))
    w("## 5. Coherence `alternatives:` (frontmatter) vs section `## Alternatives`")
    w("")
    w(f"- Pages dont le frontmatter cite une cible **absente** de la section : **{len(gap)}**")
    for f, miss in gap[:20]:
        w(f"  - `{f}` — manquant(s) en section : {', '.join(miss)}")
    w("")

    # ---------- 6. pages orphelines
    inbound = collections.Counter()
    for f, (fm, body) in pages.items():
        for tgt in re.findall(r"\[\[([^\]|]+)", body):
            inbound[tgt.split("/")[-1].strip().lower()] += 1
    orphans = sorted(f for f, (fm, _) in pages.items() if inbound[(fm.get("nom") or Path(f).stem).lower()] == 0)
    w("## 6. Pages sans aucun lien entrant")
    w("")
    w(f"- **{len(orphans)}** page(s) sur {len(pages)} ne sont citees par aucune autre page.")
    by_dir = collections.Counter(f.rsplit("/", 1)[0] for f in orphans)
    for d, n in by_dir.most_common():
        w(f"  - `{d}/` — {n}")
    w("")
    for f in orphans:
        w(f"  - `{f}`")
    w("")

    # ---------- 7. tags
    vocab_tags = set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", (DOC / "tags.md").read_text(encoding="utf-8"), re.M))
    tag_used = collections.Counter(t for fm, _ in pages.values() for t in (fm.get("tags") or []))
    notag = [f for f, (fm, _) in pages.items() if not fm.get("tags")]
    w("## 7. Tags")
    w("")
    w(f"- Vocabulaire declare : **{len(vocab_tags)}** tags")
    w(f"- Tags reellement employes : **{len(tag_used)}**")
    w(f"- Declares mais **jamais employes** : **{len(vocab_tags - set(tag_used))}**")
    w(f"- Pages **sans aucun tag** : {len(notag)} — {', '.join(f'`{f}`' for f in notag) or 'aucune'}")
    w(f"- Tags employes **une seule fois** : {sum(1 for n in tag_used.values() if n == 1)}")
    w("")

    # ---------- 8. faits perissables
    w("## 8. Faits perissables declares")
    w("")
    counts = collections.Counter()
    for fm, body in pages.values():
        if fm.get("role") != "brique":
            continue
        counts["briques"] += 1
        for field in ("licence_type", "maturite", "url_repo", "url_docs"):
            if fm.get(field):
                counts[field] += 1
        if re.search(r"\bv?\d+\.\d+(\.\d+)?\b", body):
            counts["mentionne un numero de version"] += 1
        if re.search(r"\d[\d\s.,]*(k| )?\s*(etoiles|étoiles|stars)", body, re.I):
            counts["mentionne un nombre d'etoiles"] += 1
        if re.search(r"\d[\d\s.,]*\s*(\$|€|USD|EUR)", body):
            counts["mentionne un prix"] += 1
    for k, n in counts.most_common():
        w(f"- {k} : **{n}**")
    w("")
    w("Aucun de ces faits n'est horodate ni re-verifie par un script : c'est l'objet de l'axe 4.")
    w("")

    # ---------- 9. ce que check_brain verifie
    cb = (VAULT / "AI/scripts/check_brain.py").read_text(encoding="utf-8")
    w("## 9. Perimetre du validateur")
    w("")
    w("Regles DURES implementees dans `check_brain.py` :")
    w("")
    for label, marker in [
        ("frontmatter conforme au gabarit (champs requis + aucun champ hors liste)", "hors gabarit"),
        ("valeurs d'enum fermees (hosted, scaling, licence_type, maturite)", "hors valeurs autorisées"),
        ("tags inclus dans le vocabulaire", "tag hors vocabulaire"),
        ("categorie incluse dans la taxonomie", "categorie hors taxonomie"),
        ("reciprocite des alternatives", "non réciproque"),
        ("aucun wikilink mort", "lien mort"),
    ]:
        w(f"- {label} — {'**present**' if marker in cb else '**absent**'}")
    w("")
    declared_templates = re.findall(r'"(\w+)":\s*\w+_ALLOWED', cb)
    roles_present = sorted({fm.get("role") for fm, _ in pages.values() if fm.get("role")})
    unguarded = [t for t in roles_present if t not in declared_templates]
    w("- Gabarits declares dans `ALLOWED` : "
      + (", ".join(f"`{t}`" for t in declared_templates) if declared_templates else "aucun")
      + f" — soit {len(declared_templates)} sur les {len(roles_present)} roles presents dans le vault.")
    w(f"- Roles **sans aucun gabarit controle** : {', '.join(f'`{t}`' for t in unguarded) or 'aucun'}. "
      "Une page de ces roles peut porter n'importe quel champ sans que rien ne le signale.")
    w("")
    w("Non verifie (constate par lecture du script) : synchronisation des pitchs, valeurs de")
    w("`domaines:` contre `themes.md`, gabarits `pattern` / `rule`, joignabilite des URLs,")
    w("pages orphelines, couverture des comparatifs `.base`.")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
