# Axe 2 — Integrite au fil de l'eau

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-2-integrite.md`.

## Question centrale

**Qu'est-ce qui casse dans ce vault sans que rien ne le dise ?** Et en particulier :
la mecanique de controle est pensee pour la **creation** d'une page. Que se passe-t-il
quand une page est **modifiee** ?

## Le probleme, tel qu'il est diagnostique

`AI/scripts/check_brain.py` tient six regles dures et les tient bien. Mais son perimetre
laisse passer des choses qui degradent le brain silencieusement — dont **la regle
cardinale du skill `enrichir-brain`**.

Preuve deja obtenue : la reinjection de pitch (« la ligne affichee pour une cible dans une
section `## Alternatives` doit etre exactement le `pitch:` courant de cette cible ») est
**violee 14 fois sur 801 lignes**, et aucun script ne peut le detecter. Mecanisme : quand
le pitch d'une page evolue, les N pages qui le citent gardent l'ancien. La creation est
correcte ; c'est la **mise a jour** qui derive.

## Faits de depart (cf. `mesures-<date>.md`, a relancer)

Verifie par `check_brain` : gabarit et champs, enums fermees, tags ⊆ vocabulaire,
categorie ∈ taxonomie, reciprocite des `alternatives`, aucun wikilink mort.

**Non verifie**, constate par lecture du script :

- la **synchronisation des pitchs** reinjectes → 14 cas actifs ;
- les valeurs de `domaines:` contre `themes.md` (0 ecart aujourd'hui, mais par chance) ;
- les gabarits des types `outil`, `pattern`, `rule`, `rex` → **4 des 6 types du vault
  n'ont aucun gabarit controle** ; en pratique les 40 outils sont uniformes, donc le
  risque est **latent, pas realise** : le chiffrer avant de le prioriser ;
- la **joignabilite des URLs** (`url_docs`, `url_repo` sur 334 et 318 fiches) ;
- la coherence de `remplace_par:` (une page remplacee doit-elle rester `status: actif` ?) ;
- les **pages orphelines** : 19 pages ne sont citees par personne, dont **les 5 Patterns
  et les 5 Rules — 100 % de ces deux dossiers** ;
- la couverture des comparatifs `.base` (une categorie a 3+ entrees devrait-elle en avoir un ?) ;
- l'unicite des `nom:` et des `alias:` (deux pages peuvent-elles revendiquer le meme alias ?).

## Questions a instruire

1. **Chiffrer chaque trou** ci-dessus sur le vault reel. Une regle manquante qui ne
   produit aucun degat aujourd'hui se documente mais ne se code pas en priorite.
2. **Le cas « page mise a jour »** : quand le `pitch:`, le `nom:`, la `categorie:` ou le
   `status:` d'une page change, quelles autres pages doivent suivre ? Etablir la table
   des **effets de bord par champ modifie**. C'est le coeur de l'axe.
3. **Quelles regles ajouter a `check_brain`**, dans quel ordre, et lesquelles doivent etre
   dures (bloquantes) plutot que souples (avertissement) ? Une regle dure sur un vault qui
   la viole deja 14 fois bloque tout : prevoir la sequence (corriger, puis durcir).
4. **Un script de reparation est-il possible** pour les pitchs desynchronises — la
   resynchronisation est mecanique, la source de verite etant le `pitch:` de la cible ?
   L'ecrire n'est pas votre role ; dire s'il est possible et sous quelles conditions, oui.
5. **Ou brancher le controle** : a la main, en hook `PostToolUse` sur ecriture de `.md`,
   en hook `Stop`, en CI GitHub Actions ? Peser le cout de friction contre le degat evite.
6. **Les URLs** : verifier la joignabilite coute un appel reseau par fiche. Echantillonner
   (20-30 fiches tirees au hasard) pour estimer le taux de liens morts avant de recommander
   un controle systematique.
7. **Les orphelins** : est-ce un defaut de contenu (personne ne cite ces pages) ou de
   generation (`build_mocs` ne couvre pas `Dev/Patterns/` ni `Dev/Rules/`) ? Trancher.

## Hors perimetre

Le rangement des pages (axe 1). La verite des faits affirmes (axe 4). L'ecriture effective
des correctifs — un autre agent les appliquera depuis votre rapport.

## Livrable

Le rapport, plus **en annexe** : la table « champ modifie → effets de bord a propager »,
et la liste priorisee des regles a ajouter a `check_brain` avec, pour chacune, le nombre
de violations actuelles (donc le cout de la mise en conformite avant durcissement).
