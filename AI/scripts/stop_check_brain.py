# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""stop_check_brain.py — hook Stop : lance check_brain.py si la session a touché Dev/ ou Wiki/.

Déclaré dans `.claude/settings.json` (clé `hooks.Stop`). Reçoit le payload du hook
sur stdin (`session_id`, `cwd`, `transcript_path`, …).

Contrat : **il rapporte, il ne juge pas**. Aucune erreur, aucune violation, aucun
timeout ne doit faire échouer ni bloquer une session — le script sort *toujours* en 0.
Quand `check_brain.py` est vert, le hook est silencieux : friction nulle.
Quand il est rouge, le hook remonte un `systemMessage` et s'arrête là.

Détection « la session a touché Dev/ ou Wiki/ » — union de deux signaux :
  1. le transcript de session : un Write / Edit / MultiEdit / NotebookEdit visant
     une page sous `Dev/` ou `Wiki/` ;
  2. l'état git : au moins un fichier modifié sous `Dev/` ou `Wiki/` (couvre les
     écritures faites hors outils d'édition, par script ou par `Bash`).

Résolution du vault (aucun chemin absolu en dur, cf. `Documentation/perso/machines.md`) :
racine git du `cwd` du payload → `$DEVBRAIN_VAULT` → emplacement du script.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

SCAN_DIRS = ("Dev", "Wiki")
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
    """Le chemin `raw` désigne-t-il une page sous Dev/ ou Wiki/ du vault ?"""
    if not raw:
        return False
    try:
        rel = Path(raw).resolve().relative_to(vault)
    except (ValueError, OSError, RuntimeError):
        text = raw.replace("\\", "/")
        return text.startswith(SCAN_DIRS) or any(f"/{d}/" in text for d in SCAN_DIRS)
    return bool(rel.parts) and rel.parts[0] in SCAN_DIRS


def touched_in_transcript(transcript_path: Path, vault: Path) -> bool:
    """Le transcript contient-il une écriture visant Dev/ ou Wiki/ ?"""
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
    """Un fichier est-il modifié sous Dev/ ou Wiki/ dans l'arbre de travail ?"""
    try:
        out = subprocess.run(
            ["git", "-C", str(vault), "status", "--porcelain", "--", *SCAN_DIRS],
            capture_output=True, text=True, timeout=GIT_TIMEOUT_S,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0 and bool(out.stdout.strip())


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
        print("stop_check_brain : aucune écriture dans Dev/ ou Wiki/ — check_brain non lancé.",
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
