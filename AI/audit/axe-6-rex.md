# Axe 6 — Le pilier REX

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-6-rex.md`.

## Question centrale

Le brain declare cinq piliers cote `Dev/` : Services, Outils, Patterns, Rules, **REX**.
Le pilier REX compte **une seule fiche** (`REX - Postgres`) pour **297 services** fiches,
soit **0,3 % de couverture**. Reparer, ou assumer l'abandon ?

## Pourquoi cet axe existe

Un pilier documente mais inutilise coute plus qu'il ne rapporte : il apparait dans les
gabarits, dans les conventions de nommage, dans les consignes (`CLAUDE.md`,
`CLAUDE-project.md`, le skill `enrichir-brain`), et dans `check_brain` — qui exempte
explicitement les liens `[[REX - *]]` du controle de liens morts, « assumes en attente ».
Autrement dit : le validateur a une exception permanente pour un pilier qui ne se remplit pas.

C'est le seul axe dont la conclusion legitime peut etre **« supprimer »**.

## Faits de depart

- `Dev/REX/` : 1 fichier. 297 services, 40 outils.
- Convention : un fichier par service, `Dev/REX/REX - <Nom>.md`, entrees datees
  `## YYYY-MM-DD — <symptome>`.
- Deux gabarits existent : `Templates/REX.md` et `Templates/REX-entry.md`.
- `check_brain.py` : les liens `[[REX - *]]` sont **exclus** du controle de liens morts.
- `CLAUDE.md` autorise, en mode projet, d'ajouter un REX sans toucher a la fiche service.
- Le mecanisme de creation d'un REX est donc prevu partout, et declenche nulle part.

## Questions a instruire

1. **Pourquoi c'est vide.** Trois hypotheses a departager avec des elements, pas des
   impressions : (a) rien ne declenche l'ecriture d'un REX ; (b) le format demande trop
   d'effort au mauvais moment (en plein incident) ; (c) le besoin n'existe pas parce que
   l'usage reel du brain est le **choix** de briques, pas leur **exploitation**.
   Chercher dans `AI/sessions/`, les messages de commit, `Dev/REX/REX - Postgres.md`
   lui-meme (quand a-t-il ete ecrit, dans quel contexte).
2. **Qui ecrirait un REX, et quand ?** Le brain est alimente depuis le vault (mode build) et
   consomme depuis un projet (mode projet). Un REX nait forcement en mode projet, cote
   projet — le chemin de retour vers le vault existe-t-il concretement ?
3. **Le format est-il le bon ?** Une fiche par service avec des entrees datees suppose qu'on
   sache d'avance a quel service imputer le probleme. Beaucoup d'incidents reels sont a
   l'intersection de deux briques. Un journal chronologique unique serait-il plus honnete ?
4. **L'exception dans `check_brain`.** Si le pilier est conserve, l'exemption des liens
   `[[REX - *]]` doit-elle rester permanente ? Elle masque de vrais liens morts.
5. **La decision.** Trois issues possibles, a recommander explicitement :
   - **reparer** — un declencheur, un format allege, et le chemin projet → vault ;
   - **fusionner** — les retours d'experience vont en `## Pieges` de la fiche service, et le
     pilier disparait (que devient alors `REX - Postgres` ?) ;
   - **assumer** — le pilier reste, vide, documente comme optionnel, et l'on cesse de le
     compter comme un manque.
   Chiffrer le cout des trois : fichiers touches, consignes a reecrire, gabarits a supprimer.

## Hors perimetre

Les autres piliers. Le contenu de `REX - Postgres`. La navigation (axe 5), meme si les
orphelins et le REX se recoupent — s'y referer sans le re-instruire.

## Livrable

Le rapport, avec une **recommandation unique et argumentee** parmi les trois issues, et le
chiffrage des trois. C'est un axe de decision : un rapport qui ne tranche pas a echoue.
