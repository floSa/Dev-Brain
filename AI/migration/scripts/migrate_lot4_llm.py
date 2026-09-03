# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_llm.py — descend les 56 notions `concept/llm` dans l'arbre.

Lot 4, domaine « LLM & IA générative ». Deux gestes par page : réécrire la ligne
`categorie:` du frontmatter, puis `git mv` vers le dossier que `AI/scripts/arbo.py`
dérive de cette catégorie. Le CORPS des notions n'est pas touché.

**Étape 0 d'abord** (remontées 1 et 12) : le corps du hub de domaine cite **35 des
56 notions nommément**, et ses paragraphes sont des familles — le RAG et ses étages,
l'éval contre l'observabilité, les deux façons de sortir autre chose que du texte,
la mémoire, MCP. Ce sont ces paragraphes qui rangent, pas les tags. Les 21 autres
ont été dérivées page par page, sur leur `## Aperçu` et leur section
`## Approches voisines` — c'est cette dernière qui a tranché les cas durs, parce
qu'elle nomme les voisines que la page se reconnaît :

  - `Routing and cascading` liste LiteLLM, OmniRoute et OpenRouter, soit les TROIS
    briques de `llm/passerelle`, et écrit « passerelles qui l'implémentent » ;
  - `LLM caching` liste LiteLLM (« caching intégré au niveau passerelle ») ;
  - `Reliability patterns` ne liste que des pages `llm/agents` ;
  - `Perplexity` liste Tokenization, Decoding strategies, Cross-entropy et Shannon
    entropy, et dit d'elle-même qu'elle est INTRINSÈQUE, l'éval applicative étant
    « une alternative » — donc `llm/modele`, pas `llm/eval` ;
  - `Server-Sent Events & streaming LLM` liste Decoding strategies, Tokenization et
    Inference optimization : le transport HTTP est le sujet apparent, le débit du
    serveur est le vrai — donc `llm/runtime`, pas `web/api` ;
  - `Sandboxing de code généré` liste Prompt injection, AI security, Guardrails et
    Human-in-the-loop : quatre des cinq voisines sont les pages `security/ia`.

**Trois valeurs ouvertes**, arbitrage de floSa du 2026-09-05 : `llm/modele`,
`llm/prompt` et `llm/protocole`. La troisième REMPLACE `llm/mcp`, qui nommait un
protocole précis et ne pouvait pas accueillir `a2a-protocol` sans mentir : ses deux
briques (`fastmcp`, `mcpjam`) sont recatégorisées ici, sans changer de dossier.

**Une notion sort du domaine** : `Sandboxing de code généré` -> `security/ia`.
Arbitrage de floSa, dans la ligne de la remontée 13 : la sécurité est une pratique
qui traverse les modèles. La promotion de dossier que ça déclenche dans « Sécurité »
n'est pas un argument — le seuil ne se négocie ni pour l'atteindre ni pour l'éviter,
la catégorie se décide sur le contenu et le dossier suit.

Usage : uv run AI/migration/scripts/migrate_lot4_llm.py [--dry-run]
"""

from __future__ import annotations

import collections
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

CIBLES = {
    # --- llm/rag : le RAG et ses étages. Le hub les tient en un paragraphe, dans
    #     l'ordre du pipeline, et nomme les neuf.
    "RAG": "llm/rag",
    "Advanced RAG": "llm/rag",
    "Chunking strategies": "llm/rag",
    "Hybrid retrieval": "llm/rag",
    "Reranking": "llm/rag",
    "Late-interaction retrieval": "llm/rag",
    "Query transformations": "llm/rag",
    "GraphRAG": "llm/rag",
    "Construction de graphes de connaissances": "llm/rag",

    # --- llm/eval : juger une application. Le hub sépare explicitement l'éval
    #     (jeu de tests, offline) de l'observabilité (production, online).
    "LLM eval metrics": "llm/eval",
    "LLM benchmarks": "llm/eval",
    "Code and math benchmarks": "llm/eval",
    "RAG eval": "llm/eval",
    "RAG benchmarks": "llm/eval",
    "LLM-as-judge": "llm/eval",
    "Agent evaluation": "llm/eval",

    # --- llm/observabilite : la production.
    "LLM observability": "llm/observabilite",

    # --- llm/finetuning : tout le post-training, alignement compris. Les quatre
    #     pages de RL (RL for LLMs, GRPO, RLHF and DPO, Reward modeling) NE vont
    #     pas en `ml/rl` : elles décrivent une étape qui suit le SFT sur un LLM, et
    #     elles se citent entre elles. `ml/rl` (6 pages) n'aurait rien à en faire.
    "SFT": "llm/finetuning",
    "PEFT": "llm/finetuning",
    "LoRA et QLoRA": "llm/finetuning",
    "RLHF and DPO": "llm/finetuning",
    "RL for LLMs": "llm/finetuning",
    "GRPO": "llm/finetuning",
    "Reward modeling": "llm/finetuning",
    "Synthetic data generation": "llm/finetuning",

    # --- llm/agents : la boucle, ses patrons, ses outils, ses garde-fous.
    "Agent patterns": "llm/agents",
    "Agent skills": "llm/agents",
    "agent-loops": "llm/agents",
    "Harnais d'agent": "llm/agents",
    "Multi-agent systems": "llm/agents",
    "Tool use patterns": "llm/agents",
    "tool-use": "llm/agents",
    "Human-in-the-loop": "llm/agents",
    "Reliability patterns": "llm/agents",

    # --- llm/runtime : ce qui décide de la latence et du débit côté serveur.
    #     `Multi-Token Prediction` est un ajout d'architecture, mais son résultat
    #     est un brouillon interne pour le décodage spéculatif : elle vit avec lui.
    "Inference optimization": "llm/runtime",
    "Speculative decoding": "llm/runtime",
    "Multi-Token Prediction": "llm/runtime",
    "prompt-caching": "llm/runtime",
    "Server-Sent Events & streaming LLM": "llm/runtime",

    # --- llm/sortie-structuree : garantir une FORME. À distinguer de `tool-use`,
    #     qui déclenche un EFFET — la confusion que le hub signale nommément.
    "Structured outputs": "llm/sortie-structuree",
    "Constrained decoding": "llm/sortie-structuree",

    # --- llm/memoire
    "Agent memory": "llm/memoire",

    # --- llm/protocole : VALEUR NOUVELLE, remplace `llm/mcp`.
    "mcp-protocol": "llm/protocole",
    "a2a-protocol": "llm/protocole",

    # --- llm/passerelle : router et ne pas rappeler. Les deux pages citent les
    #     trois briques du sous-domaine.
    "Routing and cascading": "llm/passerelle",
    "LLM caching": "llm/passerelle",

    # --- llm/modele : VALEUR NOUVELLE. Ce qu'EST un modèle, avant toute application.
    "Tokenization": "llm/modele",
    "Decoding strategies": "llm/modele",
    "Perplexity": "llm/modele",
    "Scaling laws": "llm/modele",
    "Small Language Models": "llm/modele",
    "Reasoning models": "llm/modele",

    # --- llm/prompt : VALEUR NOUVELLE. Ce qu'on met dans la fenêtre.
    "Prompt engineering": "llm/prompt",
    "Context engineering": "llm/prompt",
    "Chain-of-Thought": "llm/prompt",

    # --- security/ia : la seule qui sort du domaine.
    "Sandboxing de code généré": "security/ia",
}

# Briques que le remplacement de `llm/mcp` par `llm/protocole` recatégorise. Elles ne
# changent pas de dossier : les deux valeurs restent sous le seuil.
RECAT_BRIQUES = {
    "LLM & IA générative/fastmcp.md": "llm/protocole",
    "LLM & IA générative/mcpjam.md": "llm/protocole",
}

# Comparatifs qui suivent leurs membres (remontée 16 : la règle porte sur les
# MEMBRES, pas sur le nom du fichier). Les deux filtrent une catégorie promue et
# tous leurs membres descendent ; `Comparatif - Frameworks LLM` reste au niveau du
# domaine, ses membres enjambant socle, agents, rag et sortie-structuree.
COMPARATIFS = {
    "LLM & IA générative/Comparatif - Observabilité LLM.base": "llm/observabilite",
    "LLM & IA générative/Comparatif - Évaluation LLM.base": "llm/eval",
}

DOMAINES = ["LLM & IA générative", "Sécurité"]


def lignes_fm(md: Path) -> list[str]:
    return md.read_text(encoding="utf-8").split("\n")[:40]


def categorie(md: Path) -> str:
    for ligne in lignes_fm(md):
        if ligne.startswith("categorie:"):
            return ligne.split(":", 1)[1].strip()
    return ""


def est_hub(md: Path) -> bool:
    return any(ligne.strip() == "role: hub" for ligne in lignes_fm(md))


def population(dom: str) -> list[str]:
    return [categorie(md) for md in (VAULT / dom).rglob("*.md") if not est_hub(md)]


def recategoriser(path: Path, cible: str) -> None:
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def git_mv(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                    str(dest.relative_to(VAULT))], cwd=VAULT, check=True)


def main() -> int:
    dry = "--dry-run" in sys.argv
    manquants = [n for n in CIBLES if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")
    restants = [md.stem for md in SOURCE.glob("*.md")
                if categorie(md) == "concept/llm" and md.stem not in CIBLES]
    if restants:
        raise SystemExit(f"`concept/llm` non traitee(s) : {restants}")

    # --- l'effet de seuil, mesuré AVANT (remontée 3), par domaine ---
    promus: dict[str, str] = {}
    for dom in DOMAINES:
        avant = population(dom)
        apres = list(avant)
        apres += [c for c in CIBLES.values() if arbo.domaine(c) == dom]
        for chemin, c in RECAT_BRIQUES.items():
            if arbo.domaine(c) == dom:
                apres.remove(categorie(VAULT / chemin))
                apres.append(c)
        pa, pb = arbo.promotions(avant), arbo.promotions(apres)
        promus.update(pb)
        neufs = sorted(set(pb) - set(pa))
        defaits = sorted(set(pa) - set(pb))
        cnt = collections.Counter(apres)
        print(f"{dom} : {len(avant)} -> {len(apres)} pages")
        for cat in sorted(cnt):
            marque = "  <== NOUVEAU DOSSIER" if cat in neufs else ""
            print(f"    {cat:26} {cnt[cat]:3}{marque}")
        if defaits:
            raise SystemExit(f"ARRET — « {dom} » : le lot DEFAIT {defaits}. "
                             f"Non prevu ; l'arbitrage se rouvre.")
        print(f"    au niveau du domaine : "
              f"{len(apres) - sum(cnt[c] for c in pb)}")

    print()
    print(f"-- {len(CIBLES)} notions descendent --")
    par_cible = collections.defaultdict(list)
    for nom, cible in CIBLES.items():
        par_cible[cible].append(nom)
    for cible in sorted(par_cible):
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus)
        print(f"  {cible:24} -> {dest_dir.relative_to(VAULT).as_posix()}/")
        for nom in sorted(par_cible[cible]):
            print(f"       {nom}")
            if dry:
                continue
            recategoriser(SOURCE / f"{nom}.md", cible)
            git_mv(SOURCE / f"{nom}.md", dest_dir / f"{nom}.md")

    print()
    print("-- briques recategorisees (llm/mcp -> llm/protocole) --")
    for chemin, cible in sorted(RECAT_BRIQUES.items()):
        md = VAULT / chemin
        print(f"  {md.stem:24} {categorie(md)} -> {cible}")
        if not dry:
            recategoriser(md, cible)

    print()
    print("-- briques que la promotion deplace --")
    bouges = 0
    for dom in DOMAINES:
        for md in sorted((VAULT / dom).rglob("*.md")):
            if est_hub(md):
                continue
            attendu = VAULT / arbo.dossier_attendu(categorie(md), promus)
            if md.parent == attendu:
                continue
            bouges += 1
            print(f"  {md.stem:34} -> {attendu.relative_to(VAULT).as_posix()}/")
            if not dry:
                git_mv(md, attendu / md.name)

    print()
    print("-- comparatifs qui suivent leurs membres (remontee 16) --")
    for chemin, cat in sorted(COMPARATIFS.items()):
        base = VAULT / chemin
        dest = VAULT / arbo.dossier_attendu(cat, promus) / base.name
        print(f"  {base.name:40} -> {dest.relative_to(VAULT).as_posix()}")
        if not dry:
            git_mv(base, dest)

    print()
    verbe = "a deplacer" if dry else "deplacee(s)"
    print(f"{len(CIBLES)} notion(s) {verbe}, {bouges} brique(s) suivie(s), "
          f"{len(COMPARATIFS)} comparatif(s) descendu(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
