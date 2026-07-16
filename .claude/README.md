# .claude/ — config Claude Code pour DevBrain

Ce dossier contient la config Claude Code spécifique au projet DevBrain.

## Fichiers

| Fichier | Versionné | Rôle |
|---|---|---|
| `settings.example.json` | ✅ | Template public à copier en `settings.json` |
| `settings.local.example.json` | ✅ | Template perso à copier en `settings.local.json` |
| `settings.json` | ✅ (après copie) | Permissions partagées (read-only Bash, WebFetch ciblé, deny destructeur) |
| `settings.local.json` | ❌ (gitignored) | Permissions perso (push, identité) |

## Setup

```bash
cd .claude
cp settings.example.json settings.json
cp settings.local.example.json settings.local.json
```

Relis chaque fichier avant de l'utiliser. Tu peux durcir/relâcher selon ta tolérance.

## Pourquoi deux fichiers ?

- **`settings.json`** — partagé via Git, utile à tous les contributeurs. Read-only et inoffensif.
- **`settings.local.json`** — gitignored. Contient des permissions plus sensibles (push direct sur main, modification de config locale) que tu ne veux pas pousser pour d'autres.

## Si tu modifies les permissions

Claude Code recharge `settings.json` au démarrage de session. Pour rappel, les conventions de format :

- `"Bash(commande:*)"` — autorise toute invocation commençant par `commande`
- `"Bash(commande arg)"` — autorise exactement `commande arg`
- `"WebFetch(domain:example.com)"` — autorise le fetch sur ce domaine
- L'ordre : `deny` gagne toujours sur `allow`

Doc complète : https://docs.claude.com/en/docs/claude-code/settings
