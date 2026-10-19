#!/usr/bin/env bash
# suivi_lots.sh — où en sont les lots lancés en arrière-plan ? Lecture seule.
# Pour chaque copie de travail d'agent : commits pas encore poussés, fichiers en cours,
# dernier commit et son heure. Plus les derniers commits poussés sur GitHub.
set -u
principal="${DEVBRAIN_PRINCIPAL:-$HOME/Projets/DevBrain}"
git -C "$principal" fetch -q --prune origin 2>/dev/null
echo "Derniers commits sur GitHub (main) :"
git -C "$principal" log origin/main -5 --format='  %h %ar  %s' | cut -c1-120
echo
for w in $(git -C "$principal" worktree list --porcelain | grep '^worktree .*/agent-' | cut -d' ' -f2-); do
  n=$(git -C "$w" rev-list --count origin/main..HEAD 2>/dev/null)
  f=$(git -C "$w" status --short | wc -l)
  echo "$(basename "$w") : $n commit(s) non poussés, $f fichier(s) en cours"
  git -C "$w" log -1 --format='  dernier commit %ar : %s' | cut -c1-120
done
