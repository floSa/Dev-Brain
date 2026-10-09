---
role: rule
domaine: git
applicable: global
strictness: must
tags: [rule, git-hooks, version-control]
---

# Rule — Git et identité

## Principe

L'identité des commits, l'absence de co-auteur et la taille des commits se tiennent par un contrôle mécanique (hooks git `commit-msg` et `pre-commit`), pas par une consigne écrite seule.

Retour d'expérience du DevBrain : la consigne était écrite dans le fichier de contexte, et cinq commits sont partis signés avec l'adresse professionnelle au lieu de l'adresse personnelle. Une fois poussée, une adresse entre dans la liste des contributeurs et n'en sort qu'en réécrivant l'historique. Deux hooks versionnés ont fermé le trou, la consigne seule ne l'avait pas fait.

## MUST

- Régler l'identité dans la config locale du dépôt : `git config --local user.name` et `user.email`.
- Ne jamais passer l'identité en ligne de commande : ni `-c user.email`, ni `--author`, ni `GIT_AUTHOR_EMAIL`.
- N'ajouter aucun trailer `Co-Authored-By` : chaque commit est attribué à son auteur seul.
- Faire des petits commits : un sujet par commit, jamais un commit fourre-tout.
- Installer les hooks `commit-msg` (refuse le trailer) et `pre-commit` (refuse une identité inattendue), versionnés dans `.githooks/`, avec `git config core.hooksPath .githooks` à refaire après chaque clone.
- Ne jamais contourner un hook par `--no-verify` : traiter ce qu'il signale.

## SHOULD

- Rejouer le contrôle en CI sur les commits poussés, ou dans un hook `pre-push` : `--no-verify` désactive `pre-commit` et `commit-msg`, la CI et la forge ne se contournent pas depuis le poste.
- Écrire le message de commit dans un fichier (`git commit -F`) et le relire avant de committer : les backticks d'un message passé en `-m` sont interprétés par le shell et remplacent le texte en silence.
- Ne jamais forcer un push (`--force`) ni réécrire un historique déjà poussé sans accord explicite.
- Faire suivre cette règle à l'agent de code comme à l'humain : la consigne va dans `AGENTS.md`, le hook fait foi.
- Dire dans le message de commit **pourquoi**, pas seulement quoi.

## NICE-TO-HAVE

- Gérer les hooks avec [[Lefthook]] ou [[pre-commit]] quand le projet en a plusieurs, à la place de scripts à la main.
- Interdire aussi, côté forge ([[Forgejo]], [[GitLab CE]]), les pushes directs sur la branche principale.

## Pour AGENTS.md

- Identité des commits : celle de la config locale du dépôt. Ne jamais la changer par `-c`, `--author` ni variable d'environnement.
- Aucun trailer `Co-Authored-By`, même si un outil le propose.
- Petits commits, un sujet par commit.
- Un hook qui refuse n'est pas à contourner : jamais `--no-verify`.

## Exemples

### Bon

```bash
# installe l'identité locale, les hooks .githooks/ et core.hooksPath en une commande
bash .claude/skills/planifier-projet/scripts/garde_fous.sh . "Prénom Nom" "adresse@perso.example"

# .githooks/commit-msg (le script reçoit le fichier du message en $1)
if grep -qiE '^co-authored-by:' "$1"; then
  echo "Commit refusé : aucun co-auteur." >&2; exit 1
fi
```

### Mauvais

```bash
# consigne écrite seulement, aucun hook : rien n'arrête l'erreur
echo "Ne jamais utiliser l'adresse pro." >> AGENTS.md
git -c user.email=pro@entreprise.example commit -m "feat: tout le lot en un commit"
```

## Exceptions

- Dépôt de mission où le client impose son identité ou sa convention : régler **son** adresse dans la config locale et dans le hook. La règle (un contrôle mécanique) reste, la valeur change.
- Dépôt jetable, local, jamais poussé : les hooks sont facultatifs ; l'identité locale reste réglée.

## Voir aussi

- [[Rule - Commits conventionnels et versions automatiques]] — le format du message, vérifié par le même hook `commit-msg`
- [[Rule - Projet assisté par agent]] — ce qui va dans `AGENTS.md` et ce qui va dans un hook
- [[Branches courtes et worktrees pour agents]] — petites unités de changement, une branche par tâche
- [[Fichiers de contexte pour agents]] — pourquoi une règle qui ne doit jamais être violée appartient à un hook, pas au fichier de contexte
- [[pre-commit]], [[Lefthook]] — les gestionnaires de hooks
