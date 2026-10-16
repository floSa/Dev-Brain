#!/usr/bin/env bash
# verifier_depot.sh — le dépôt est-il propre ? À lancer après chaque lot.
#
# Contrôle, sans rien modifier :
#   1. GitHub ne porte qu'une branche : main ;
#   2. le main local du vault principal est identique à origin/main ;
#   3. aucune branche locale n'a de commit non poussé ;
#   4. aucun worktree (hors le vault principal et celui-ci) n'a de changement non commité ;
#   5. la copie Obsidian, si son chemin est donné, est sur le même commit.
#
# Usage : bash AI/scripts/verifier_depot.sh [chemin-de-la-copie-obsidian]
# Sortie : une ligne par contrôle, OK ou PROBLÈME. Code 1 s'il y a un problème.

set -u
principal="${DEVBRAIN_PRINCIPAL:-$HOME/Projets/DevBrain}"
copie="${1:-}"
statut=0
ok()  { echo "OK       $1"; }
pb()  { echo "PROBLÈME $1"; statut=1; }

git -C "$principal" fetch -q --prune origin 2>/dev/null || pb "fetch impossible"

distantes=$(git -C "$principal" ls-remote --heads origin | sed 's#.*refs/heads/##')
n=$(printf '%s\n' "$distantes" | grep -c .)
if [ "$n" -eq 1 ] && [ "$distantes" = "main" ]; then ok "GitHub : main seule"
else pb "GitHub porte $n branche(s) : $(printf '%s' "$distantes" | tr '\n' ' ')"; fi

local_main=$(git -C "$principal" rev-parse main)
dist_main=$(git -C "$principal" rev-parse origin/main)
if [ "$local_main" = "$dist_main" ]; then ok "main local = origin/main ($(echo "$local_main" | cut -c1-7))"
else pb "main local ($(echo "$local_main" | cut -c1-7)) différent d'origin/main ($(echo "$dist_main" | cut -c1-7))"; fi

# Commits de branches locales absents de origin/main (hors main lui-même).
for b in $(git -C "$principal" for-each-ref --format='%(refname:short)' refs/heads | grep -v '^main$'); do
  a=$(git -C "$principal" rev-list --count "origin/main..$b")
  [ "$a" -gt 0 ] && pb "branche locale $b : $a commit(s) absents de origin/main"
done
git -C "$principal" for-each-ref --format='%(refname:short)' refs/heads | grep -v '^main$' | grep -q . \
  || ok "aucune branche locale en plus de main"

ici=$(git rev-parse --show-toplevel 2>/dev/null || echo "")
while read -r w; do
  [ "$w" = "$principal" ] && continue
  [ "$w" = "$ici" ] && continue
  c=$(git -C "$w" status --short | wc -l)
  [ "$c" -gt 0 ] && pb "worktree $w : $c fichier(s) non commités"
done < <(git -C "$principal" worktree list --porcelain | grep '^worktree ' | cut -d' ' -f2-)
nw=$(git -C "$principal" worktree list | wc -l)
echo "INFO     $nw worktree(s) (le vault principal compte pour un)"

if [ -n "$copie" ]; then
  c=$(git -C "$copie" rev-parse HEAD 2>/dev/null)
  if [ "$c" = "$dist_main" ]; then ok "copie Obsidian à jour"
  else pb "copie Obsidian en retard ($(echo "$c" | cut -c1-7))"; fi
fi

exit "$statut"
