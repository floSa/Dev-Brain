#!/usr/bin/env python3
"""
Hook Stop pour DevBrain.

Détecte si la session était en mode BUILD (dans le vault) ou PROJET (dans
un dossier de dev) et écrit un résumé approprié dans AI/sessions/.

Configuration dans ~/.claude/settings.json :
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python ~/DevBrain/AI/scripts/session_to_devbrain.py"
          }
        ]
      }
    ]
  }
}

Pré-requis :
- pip install anthropic
- variable d'env ANTHROPIC_API_KEY positionnée
- adapter la constante VAULT ci-dessous au chemin de ton vault
"""
import datetime
import json
import os
import sys
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("anthropic SDK non installe : pip install anthropic", file=sys.stderr)
    sys.exit(0)  # ne pas casser la session, juste logguer

# === CONFIG : adapte au chemin de ton DevBrain ===
VAULT = Path.home() / "DevBrain"
SESSIONS_DIR = VAULT / "AI" / "sessions"
MODEL = "claude-haiku-4-5-20251001"  # Haiku suffit pour des résumés courts
MAX_TRANSCRIPT_CHARS = 50000


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
    in_vault = str(cwd).startswith(str(VAULT))
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
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.datetime.now()
    filename = f"{now:%Y-%m-%d-%H%M}-{mode}.md"
    target = SESSIONS_DIR / filename

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
- references vers les REX ajoutes au brain

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
