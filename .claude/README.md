# .claude/ — config Claude Code pour DevBrain

Ce dossier contient la config Claude Code spécifique au projet DevBrain.

## Fichiers

| Fichier | Versionné | Rôle |
|---|---|---|
| `settings.json` | ✅ | **Config partagée réelle** : permissions (read-only Bash, WebFetch ciblé, deny destructeur) **et hooks du vault**. Rien à copier, elle est dans le dépôt. |
| `settings.example.json` | ✅ | Ancien template de permissions, gardé comme référence de départ. `settings.json` en est issu. |
| `settings.local.example.json` | ✅ | Template perso à copier en `settings.local.json` |
| `settings.local.json` | ❌ (gitignored) | Permissions perso (push, identité) |

> Historique : jusqu'au 2026-09-02, ce tableau annonçait un `settings.json` « versionné après
> copie » qui n'avait jamais été créé — aucun hook du vault ne tournait donc (audit axe 3,
> constat C1). `settings.json` est désormais versionné tel quel : il n'y a plus de copie à faire.

## Setup

```bash
cp .claude/settings.local.example.json .claude/settings.local.json
```

`settings.json` est déjà là, versionné : ne le copie pas, ne le renomme pas. Seul le fichier
`settings.local.json` est à créer, et lui seul est gitignoré. Relis-le avant de l'utiliser :
tu peux durcir ou relâcher selon ta tolérance.

## Pourquoi deux fichiers ?

- **`settings.json`** — partagé via Git, utile à tous les contributeurs. Permissions
  read-only et inoffensives, plus les hooks qui font tourner l'automatisation du vault.
- **`settings.local.json`** — gitignored. Contient des permissions plus sensibles (push direct sur main, modification de config locale) que tu ne veux pas pousser pour d'autres.

## Hooks déclarés

Deux hooks `Stop`, dans cet ordre. Aucun des deux ne bloque ni ne fait échouer une session :
tous deux sortent **toujours** en 0.

| Hook | Script | Quand | Effet |
|---|---|---|---|
| `Stop` | `AI/scripts/stop_check_brain.py` | Seulement si la session a touché `Dev/` ou `Wiki/` | Lance `uv run AI/scripts/check_brain.py`. Silencieux si vert ; remonte un message si rouge. |
| `Stop` | `AI/scripts/session_to_devbrain.py` | Chaque fin de session | Écrit un résumé dans `AI/sessions/`. Ne fait rien sans `ANTHROPIC_API_KEY`. |

La détection « la session a touché `Dev/` ou `Wiki/` » croise deux signaux : les écritures
`Write` / `Edit` / `MultiEdit` visées dans le transcript, et `git status` sur ces deux dossiers.

Les deux scripts résolvent l'emplacement du vault par **racine git du `cwd` du payload →
`$DEVBRAIN_VAULT` → emplacement du script**. Aucun chemin absolu n'est écrit en dur, ni dans
les scripts ni dans `settings.json` (qui passe par `$CLAUDE_PROJECT_DIR`) — c'est la règle de
`Documentation/perso/machines.md`.

## Si tu modifies les permissions

Claude Code recharge `settings.json` au démarrage de session. Pour rappel, les conventions de format :

- `"Bash(commande:*)"` — autorise toute invocation commençant par `commande`
- `"Bash(commande arg)"` — autorise exactement `commande arg`
- `"WebFetch(domain:example.com)"` — autorise le fetch sur ce domaine
- L'ordre : `deny` gagne toujours sur `allow`

Doc complète : https://docs.claude.com/en/docs/claude-code/settings
