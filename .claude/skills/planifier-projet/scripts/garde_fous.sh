#!/usr/bin/env bash
# garde_fous.sh — installe dans un projet deux contrôles de commit.
#
#   1. refuse tout message portant un trailer Co-Authored-By ;
#   2. refuse un commit dont l'auteur n'est pas l'adresse attendue.
#
# Une consigne écrite seule ne suffit pas : un contrôle mécanique refuse le commit.
#
# Usage : garde_fous.sh <dossier-du-projet> <nom> <adresse>
# Effet : règle l'identité locale, écrit .githooks/, active core.hooksPath.
# Rien n'est écrit hors du dossier du projet.

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "usage : $0 <dossier-du-projet> <nom> <adresse>" >&2
  exit 2
fi

projet="$1"; nom="$2"; adresse="$3"

git -C "$projet" rev-parse --git-dir >/dev/null 2>&1 || {
  echo "$projet n'est pas un dépôt git. Faire git init d'abord." >&2
  exit 1
}

git -C "$projet" config --local user.name "$nom"
git -C "$projet" config --local user.email "$adresse"

mkdir -p "$projet/.githooks"

cat > "$projet/.githooks/commit-msg" <<'HOOK'
#!/usr/bin/env bash
# Refuse tout trailer Co-Authored-By.
if grep -qiE '^co-authored-by:' "$1"; then
  echo "Commit refusé : aucun co-auteur dans ce projet (trailer Co-Authored-By)." >&2
  exit 1
fi
HOOK

cat > "$projet/.githooks/pre-commit" <<HOOK
#!/usr/bin/env bash
# Refuse un commit dont l'auteur n'est pas l'identité du projet.
attendu="$adresse"
courant="\$(git config user.email)"
auteur="\${GIT_AUTHOR_EMAIL:-\$courant}"
if [ "\$auteur" != "\$attendu" ] || [ "\$courant" != "\$attendu" ]; then
  echo "Commit refusé : identité \$auteur, attendue \$attendu." >&2
  exit 1
fi
HOOK

chmod +x "$projet/.githooks/commit-msg" "$projet/.githooks/pre-commit"
git -C "$projet" config --local core.hooksPath .githooks
echo "Contrôles installés dans $projet/.githooks (identité : $nom <$adresse>)."
