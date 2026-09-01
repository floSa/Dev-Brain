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

**Limite.** `AI/index/brain-index.json` ne stocke que douze champs :
`path, nom, alias, type, galaxie, categorie, domaines, pitch, tags, alternatives, status,
maturite`. (`status` et `maturite` ont été ajoutés le 2026-09-02 par le correctif L3-1 —
avant cela ils manquaient, et `planifier-projet` proposait des briques abandonnées sans le
savoir. Le fond de cette entrée reste entier : `contraintes:` n'existe toujours pas, et
`remplace_par:` n'est pas indexé non plus.)
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

---

## 3. Audit de taxonomie — séparer la nature du domaine

**Statut : demandé (2026-09-02), à conduire après le lot réseau/ops/média.**

**Constat.** Le vault mélange deux axes dans un seul champ. `type:` porte déjà la
**nature** (`service`, `outil`, `concept`, `pattern`, `rule`), mais `categorie:`
mélange le **domaine technique** (`database/`, `llm/`, `network/`) et la
**famille d'outillage** (`tooling/*`), qui n'est pas un domaine mais un fourre-tout
de natures. Résultat : le rangement d'une page dépend de qui l'écrit.

**Pièces à conviction relevées pendant le lot du 2026-09-02.**

1. `llm/framework` sert de fourre-tout : il contient à la fois des passerelles
   ([[Dev/Services/OpenRouter|OpenRouter]], [[Dev/Services/LiteLLM|LiteLLM]],
   [[Dev/Services/OmniRoute|OmniRoute]]) et des frameworks d'agents
   ([[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]]). Un
   `llm/gateway` manque manifestement — non créé dans ce lot parce qu'il
   imposerait de recatégoriser des fiches existantes, ce qui est le travail de
   l'audit, pas d'un lot d'ajout.
2. `tooling/media` est défini par son *usage* (« input multimodal pour un
   assistant IA »), pas par son sujet — d'où la création d'un `tooling/video`
   distinct, qui reste un contournement.
3. La règle « un Outil porte `categorie: tooling/<famille>` » a dû être assouplie :
   Sniffnet est en `network/analysis`, osint4all en `security/osint`. Le dossier
   ne détermine pas le domaine.
4. Le vocabulaire `domaines:` (5 thèmes, tous data/ML/AI) ne couvrait rien de ce
   lot — d'où l'ajout de `infra-ops`. Il reste des pages sans thème possible
   ([[Dev/Outils/OpenCut|OpenCut]], [[Dev/Outils/SmartTube|SmartTube]] :
   `domaines: []`).
5. Deux pages portent un « avertissement de rangement » en tête de corps
   ([[Dev/Outils/public-apis|public-apis]], [[Dev/Outils/osint4all|osint4all]]) :
   ce sont des **annuaires de liens**, ni service ni outil. Un `type: ressource`
   manque.
6. Asymétrie de gabarit non documentée : `check_brain.py` interdit `domaines:`
   sur une fiche `type: service` (hors `SERVICE_ALLOWED`) mais l'autorise sur un
   `type: outil` — qui n'est validé par **aucun** gabarit, `ALLOWED` ne couvrant
   que `service` et `concept`. Un Outil peut donc porter n'importe quel champ.

7. **Le champ `domaines:` d'une fiche Dev n'est lu par personne.** `build_mocs.py`
   (boucle « MOC Wiki par domaine ») ne retient que les pages `galaxie: wiki` dont la
   `categorie` commence par `concept/` : les `domaines:` portés par un Service ou un Outil
   ne produisent aucune MOC et ne servent à aucune navigation. Conséquence constatée le
   2026-09-02 : le thème `infra-ops` a été ajouté au vocabulaire et posé sur trois fiches
   Dev ([[Dev/Outils/Sniffnet|Sniffnet]], [[Dev/Outils/croc|croc]],
   [[Dev/Outils/osint4all|osint4all]]) — aucune `MOC/Themes/Infrastructure & Ops.md` n'a
   été générée, et il n'en existera pas tant qu'aucun **concept Wiki** ne portera ce thème.
   Le champ est donc soit à alimenter côté Wiki, soit à retirer des gabarits Dev, soit à
   faire lire par le script. En l'état il donne l'illusion d'un classement qui n'existe pas.
8. **Asymétrie miroir de la précédente** : `check_brain.py` **interdit** `domaines:` sur un
   `type: service` mais la convention observée l'**impose** sur un `type: outil`
   (toutes les fiches de `Dev/Outils/` en portent un). Deux natures voisines, deux règles
   opposées, pour un champ que rien ne consomme.

**Piste.** Deux champs au lieu d'un : `domaine:` (thématique — `llm`, `network`,
`data`, `security`, `observability`…) et `famille:` (nature d'outillage —
`framework`, `gateway`, `runtime`, `client`, `cli`, `annuaire`…), le couple
remplaçant `categorie:`. Segmenter finement est possible sans exploser le nombre
de valeurs, puisque le produit des deux axes fait le travail que 112 catégories
plates font aujourd'hui mal.

**Impacts.** `Documentation/general/taxonomie.md` (réécriture), les 3 gabarits,
`check_brain.py` (ajouter un gabarit `outil`), `build_index.py`, `build_mocs.py`
(les MOC Categories sont dérivées du préfixe de `categorie:`), et une migration
des ~330 fiches Dev. Chantier lourd : à cadrer avant d'écrire une ligne.
