# /// script
# requires-python = ">=3.10"
# dependencies = ["anthropic>=0.40"]
# ///
"""session_to_devbrain.py — hook Stop : écrit un résumé de session dans AI/sessions/.

Détecte si la session était en mode BUILD (dans le vault) ou PROJET (dans un
dossier de dev) et écrit un résumé adapté.

Déclaré dans `.claude/settings.json` du vault (clé `hooks.Stop`) :

    uv run "$CLAUDE_PROJECT_DIR/AI/scripts/session_to_devbrain.py"

Depuis un dépôt projet, pointer le script du vault et poser `DEVBRAIN_VAULT`.

Pré-requis : `ANTHROPIC_API_KEY` positionnée. Sans elle, le script ne fait rien
et sort en 0 — un hook ne casse jamais la session.

Résolution du vault (aucun chemin absolu en dur, cf. `Documentation/perso/machines.md`) :
racine git du `cwd` reçu dans le payload → `$DEVBRAIN_VAULT` → emplacement du script.
"""
import datetime
import json
import os
import subprocess
import sys
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("anthropic SDK non installe : pip install anthropic", file=sys.stderr)
    sys.exit(0)  # ne pas casser la session, juste logguer

MODEL = "claude-haiku-4-5-20251001"  # Haiku suffit pour des résumés courts
MAX_TRANSCRIPT_CHARS = 50000
GIT_TIMEOUT_S = 30


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
    """Un DevBrain a un AI/design/brain-v2.md."""
    return bool(path) and (path / "AI" / "design" / "brain-v2.md").is_file()


def resolve_vault(cwd: Path) -> Path:
    """Racine git du cwd → $DEVBRAIN_VAULT → emplacement du script.

    En mode projet, la racine git du cwd est celle du projet, pas du vault :
    la détection `looks_like_vault` la rejette et on retombe sur la variable
    d'environnement, puis sur l'emplacement du script (<vault>/AI/scripts/).
    C'est ce qui permet à `in_vault` plus bas de distinguer build et projet.
    """
    root = git_root(cwd)
    if looks_like_vault(root):
        return root

    env = os.environ.get("DEVBRAIN_VAULT")
    if env:
        candidate = Path(env).expanduser()
        if looks_like_vault(candidate):
            return candidate

    return Path(__file__).resolve().parents[2]


def main() -> None:
    # 1. Lire le payload du hook
    try:
        payload = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print("Payload hook invalide", file=sys.stderr)
        return

    session_id = payload.get("session_id", "unknown")
    cwd = Path(payload.get("cwd", "."))
    transcript_path_str = payload.get("transcript_path", "")
    if not transcript_path_str:
        print("Pas de transcript_path dans le payload", file=sys.stderr)
        return

    transcript_path = Path(transcript_path_str)
    if not transcript_path.exists():
        print(f"Transcript introuvable : {transcript_path}", file=sys.stderr)
        return

    # 2. Détecter le mode (BUILD si dans le vault, PROJECT sinon)
    vault = resolve_vault(cwd)
    sessions_dir = vault / "AI" / "sessions"
    try:
        in_vault = cwd.resolve().is_relative_to(vault.resolve())
    except (OSError, RuntimeError):
        in_vault = str(cwd).startswith(str(vault))
    mode = "build" if in_vault else "project"
    project_name = None if in_vault else cwd.name

    # 3. Lire le transcript (tronqué)
    transcript = transcript_path.read_text(encoding="utf-8")[-MAX_TRANSCRIPT_CHARS:]

    # 4. Prompt adapté au mode
    if mode == "build":
        prompt = build_prompt_for_build_mode(transcript)
    else:
        prompt = build_prompt_for_project_mode(transcript, project_name)

    # 5. Appeler Claude pour le resume
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY non positionnee, skip resume", file=sys.stderr)
        return

    try:
        client = Anthropic()
        resp = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        summary = resp.content[0].text
    except Exception as e:
        print(f"Erreur appel API: {e}", file=sys.stderr)
        return

    # 6. Ecrire dans AI/sessions/
    sessions_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.datetime.now()
    filename = f"{now:%Y-%m-%d-%H%M}-{mode}.md"
    target = sessions_dir / filename

    frontmatter = (
        "---\n"
        f"date: {now:%Y-%m-%d}\n"
        f"session_id: {session_id}\n"
        f"mode: {mode}\n"
        f"project: {project_name or 'devbrain'}\n"
        "type: ai-session\n"
        f"tags: [ai-session, mode-{mode}]\n"
        "---\n\n"
    )
    target.write_text(frontmatter + summary, encoding="utf-8")
    print(f"Session DevBrain sauvegardee : {target}", file=sys.stderr)


def build_prompt_for_build_mode(transcript: str) -> str:
    return f"""Voici le transcript d'une session de BUILD du DevBrain.
Genere un resume Markdown avec ces sections, en francais :

# Session BUILD - {datetime.datetime.now():%Y-%m-%d %H:%M}

## Objectif

## Fiches modifiees / creees
- type (Service / Pattern / Rule) - chemin

## Decisions de categorisation
- toute decision sur taxonomie

## A reprendre

## Patterns identifies

Reste factuel, max 300 mots.

Transcript :
{transcript}
"""


def build_prompt_for_project_mode(transcript: str, project_name: str) -> str:
    return f"""Voici le transcript d'une session de DEVELOPPEMENT du projet "{project_name}".
Genere un resume Markdown avec ces sections, en francais :

# Session PROJET {project_name} - {datetime.datetime.now():%Y-%m-%d %H:%M}

## Objectif

## Avancees

## Services consultes dans le devbrain
- liste des fiches lues / referencees

## Bugs logges
- pieges ajoutes dans la section `## Pieges` des fiches Service concernees

## Decisions

## A reprendre

Reste factuel, max 300 mots.

Transcript :
{transcript}
"""


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Ne jamais faire planter la session a cause du hook
        print(f"Hook DevBrain a echoue : {e}", file=sys.stderr)
    sys.exit(0)
