# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""stop_check_brain.py — hook Stop : lance check_brain.py si la session a touché une page.

Déclaré dans `.claude/settings.json` (clé `hooks.Stop`). Reçoit le payload du hook
sur stdin (`session_id`, `cwd`, `transcript_path`, …).

Contrat : **il rapporte, il ne juge pas**. Aucune erreur, aucune violation, aucun
timeout ne doit faire échouer ni bloquer une session — le script sort *toujours* en 0.
Quand `check_brain.py` est vert, le hook est silencieux : friction nulle.
Quand il est rouge, le hook remonte un `systemMessage` et s'arrête là.

Détection « la session a touché une page » — union de deux signaux :
  1. le transcript de session : un Write / Edit / MultiEdit / NotebookEdit visant
     une page du brain ;
  2. l'état git : au moins un `.md` / `.base` de page modifié dans l'arbre de travail
     (couvre les écritures faites hors outils d'édition, par script ou par `Bash`).

Le périmètre est défini **en négatif**, et c'est le correctif du 2026-09-05. Il était
écrit en positif, sur les deux galaxies de la v2 : `Dev/` a disparu à la clôture du
lot 3, `Wiki/` à celle du lot 4, et le hook ne trouvait donc plus jamais rien à
vérifier. Il **ne lançait plus check_brain depuis le lot 3**, sans un mot — indiscernable
d'un vert. Une liste positive de dossiers de pages serait à tenir à jour à chaque
promotion de domaine ; la liste des dossiers qui n'en portent PAS, elle, ne bouge pas
(c'est `arbo.NON_PAGES`, recopié ici pour garder le hook sans dépendance).

Résolution du vault (aucun chemin absolu en dur, cf. `Documentation/perso/machines.md`) :
racine git du `cwd` du payload → `$DEVBRAIN_VAULT` → emplacement du script.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

# Dossiers de la racine qui ne portent aucune page du brain — miroir de `arbo.NON_PAGES`.
# Tout le reste en porte : les 20 dossiers de domaine, « Métiers/ », « Patterns/ »,
# « Rules/ », et les pages posées à la racine (`Home.md`).
NON_PAGES = {".git", ".github", ".githooks", ".claude", ".obsidian",
             "AI", "Documentation", "Templates", "Projects", "docs"}
PAGE_SUFFIXES = (".md", ".base")
EDIT_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
CHECK_TIMEOUT_S = 300
GIT_TIMEOUT_S = 30
MAX_MESSAGE_CHARS = 2000


def git_root(start: Path) -> Path | None:
    """Racine du dépôt git contenant `start`, ou None."""
    try:
        out = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=GIT_TIMEOUT_S,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    root = out.stdout.strip()
    return Path(root) if root else None


def looks_like_vault(path: Path | None) -> bool:
    """Un DevBrain a un AI/design/brain-v2.md et un dossier Dev/."""
    return bool(path) and (path / "AI" / "design" / "brain-v2.md").is_file()


def resolve_vault(cwd: Path) -> Path:
    """Racine git du cwd → $DEVBRAIN_VAULT → emplacement du script."""
    root = git_root(cwd)
    if looks_like_vault(root):
        return root

    env = os.environ.get("DEVBRAIN_VAULT")
    if env:
        candidate = Path(env).expanduser()
        if looks_like_vault(candidate):
            return candidate

    # Le script vit dans <vault>/AI/scripts/ : dernier repli, toujours correct
    # puisque le hook l'invoque depuis le vault lui-même.
    return Path(__file__).resolve().parents[2]


def in_scope(raw: str, vault: Path) -> bool:
    """Le chemin `raw` désigne-t-il une page du brain ?

    Une page est un `.md` / `.base` qui n'est pas sous un dossier de `NON_PAGES`.
    Un chemin qu'on ne sait pas rapporter au vault est tenu HORS périmètre : le
    signal git ci-dessous le rattrapera, et le hook rapporte — il ne devine pas.
    """
    if not raw or not raw.lower().endswith(PAGE_SUFFIXES):
        return False
    try:
        rel = Path(raw).resolve().relative_to(vault)
    except (ValueError, OSError, RuntimeError):
        return False
    return bool(rel.parts) and rel.parts[0] not in NON_PAGES


def touched_in_transcript(transcript_path: Path, vault: Path) -> bool:
    """Le transcript contient-il une écriture visant une page du brain ?"""
    try:
        handle = transcript_path.open(encoding="utf-8", errors="replace")
    except OSError:
        return False
    with handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            message = record.get("message")
            content = message.get("content") if isinstance(message, dict) else None
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                if block.get("name") not in EDIT_TOOLS:
                    continue
                params = block.get("input")
                if not isinstance(params, dict):
                    continue
                target = params.get("file_path") or params.get("notebook_path") or ""
                if isinstance(target, str) and in_scope(target, vault):
                    return True
    return False


def touched_in_git(vault: Path) -> bool:
    """Une page du brain est-elle modifiée dans l'arbre de travail ?"""
    try:
        out = subprocess.run(
            ["git", "-C", str(vault), "status", "--porcelain", "-z"],
            capture_output=True, text=True, timeout=GIT_TIMEOUT_S,
            encoding="utf-8", errors="replace",
        )
    except (OSError, subprocess.SubprocessError):
        return False
    if out.returncode != 0:
        return False
    for entree in out.stdout.split("\0"):
        # `XY <chemin>` ; un renommage émet la cible puis la source en deux entrées
        # séparées par le NUL — les deux passent par ce test.
        chemin = entree[3:] if len(entree) > 3 else ""
        if not chemin.lower().endswith(PAGE_SUFFIXES):
            continue
        if chemin.replace("\\", "/").split("/")[0] not in NON_PAGES:
            return True
    return False


def run_check_brain(vault: Path) -> tuple[int, str]:
    """Lance check_brain.py. Retourne (code, sortie agrégée)."""
    script = vault / "AI" / "scripts" / "check_brain.py"
    if not script.is_file():
        return 0, f"check_brain.py introuvable : {script}"
    try:
        out = subprocess.run(
            ["uv", "run", str(script)],
            cwd=str(vault), capture_output=True, text=True, timeout=CHECK_TIMEOUT_S,
        )
    except FileNotFoundError:
        return 0, "uv introuvable — check_brain non lancé."
    except subprocess.TimeoutExpired:
        return 0, f"check_brain a dépassé {CHECK_TIMEOUT_S}s — abandon sans blocage."
    except (OSError, subprocess.SubprocessError) as exc:
        return 0, f"check_brain n'a pas pu être lancé : {exc}"
    return out.returncode, (out.stdout + out.stderr).strip()


def main() -> None:
    raw_payload = sys.stdin.read() if not sys.stdin.isatty() else ""
    try:
        payload = json.loads(raw_payload) if raw_payload.strip() else {}
    except json.JSONDecodeError:
        payload = {}

    cwd = Path(payload.get("cwd") or os.getcwd())
    vault = resolve_vault(cwd)

    transcript_raw = payload.get("transcript_path") or ""
    touched = bool(transcript_raw) and touched_in_transcript(Path(transcript_raw), vault)
    if not touched:
        touched = touched_in_git(vault)

    if not touched:
        print("stop_check_brain : aucune écriture dans une page — check_brain non lancé.",
              file=sys.stderr)
        return

    code, output = run_check_brain(vault)
    if code == 0:
        print(f"stop_check_brain : check_brain vert.\n{output}", file=sys.stderr)
        return

    tail = output[-MAX_MESSAGE_CHARS:] if output else "(aucune sortie)"
    print(json.dumps({
        "systemMessage": (
            "check_brain a relevé des violations sur les pages touchées "
            f"(code {code}). Le hook ne bloque pas ; à corriger avant commit.\n{tail}"
        )
    }, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 — un hook ne casse jamais la session
        print(f"stop_check_brain a échoué : {exc}", file=sys.stderr)
    sys.exit(0)
