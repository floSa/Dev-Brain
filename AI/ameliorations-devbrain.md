# Améliorations DevBrain — pistes pour une prochaine version

Idées d'évolution **structurelles** du vault : gabarits, frontmatter, scripts
d'index, gouvernance. Distinct de `AI/backlog.md`, qui suit les **contenus** à
écrire (fiches, grappes de concepts).

Règle : rien n'est appliqué depuis ce fichier sans validation explicite. Une
entrée décrit le besoin constaté, la piste envisagée et ce qu'elle impacte.

---

## 1. Champ `contraintes:` indexé

**Statut : parqué (2026-08-08). Pas de besoin bloquant pour l'instant.**

**Constat.** Les pièges et contraintes vont dans la section `## Pièges` de la
fiche, comme le prévoient les gabarits — c'est la règle et elle convient à la
lecture humaine.

**Limite.** `AI/index/brain-index.json` ne stocke que dix champs :
`path, nom, alias, type, galaxie, categorie, domaines, pitch, tags, alternatives`.
Le skill `planifier-projet` filtre ses candidats sur cet index (« sans lire
160 fichiers ») et n'ouvre la fiche qu'après sélection. Une contrainte
éliminatoire écrite en corps de page alimente donc la **justification**, jamais
le **filtrage**.

Exemple concret : si le serving imposé est Ollama, le skill ne peut pas écarter
d'office [[Dev/Services/LM Studio Bionic|LM Studio Bionic]], qui n'accepte pas
d'endpoint arbitraire — l'incompatibilité n'existe que dans le corps de la fiche.

**Piste.** Un champ `contraintes:` (1 à 3 lignes dures, filtrables) dans le
frontmatter Service, remonté par `build_index.py`. À poser d'abord sur les seules
fiches où la contrainte est réellement éliminatoire (agents, runtimes) plutôt
qu'à généraliser à vide — un champ obligatoire vide partout ne vaut rien.

**Impacts.** `Templates/Service-Dev.md`, `AI/scripts/build_index.py`,
`AI/scripts/check_brain.py`, et le skill `planifier-projet`. Décision de
gouvernance : à valider avant toute écriture.

---

## 2. Wikilinks aliasés dans les tableaux Markdown

**Statut : à trancher.**

**Constat.** Dans une cellule de tableau, Obsidian impose d'échapper le pipe
(`[[page\|alias]]`). `check_brain.py` lit alors un lien mort `[[page\]]` et
échoue. Le cas s'est produit deux fois le 2026-08-08.

**Contournement actuel.** Utiliser un lien **nu** dans les cellules
(`[[LM Studio]]`), ce qui fonctionne et reste lisible.

**Piste.** Soit apprendre l'échappement à `check_brain.py`, soit inscrire la
convention « pas de lien aliasé dans un tableau » dans
`Documentation/general/` pour que la règle soit explicite plutôt que
redécouverte à chaque fois.
