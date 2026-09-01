# Axe 3 — Skills

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-3-skills.md`.

## Question centrale

Pas « les skills sont-ils bien ecrits », mais **qu'est-ce qui garantit qu'un skill soit
suivi ?** Un skill qu'un agent peut reimplementer de memoire ne garantit rien.

## Le cas reel qui ouvre cet axe

Le 2026-09-02, une session a integre 14 fiches dans le brain (commit `a66d346`) **sans
invoquer `enrichir-brain`** : l'agent a lu `SKILL.md` et recopie ses regles a la main dans
les consignes de quatre sous-agents. Resultat correct sur le fond, mais :

- l'etape « ecrire la file validee dans `AI/backlog.md` » a ete **omise** — si la session
  avait echoue en cours, aucune trace de ce qui etait prevu ne subsistait ;
- l'etape « creer les pages connexes manquantes, dont le concept parent Wiki » a ete
  **volontairement ecartee** (arbitrage annonce et valide, mais c'est une entorse) ;
- rien, a aucun moment, n'a signale que le skill n'avait pas ete charge.

C'est le materiau de depart : un skill de 100 lignes et 11 etapes, contournable sans
alarme, et dont l'omission ne laisse pas de trace.

## Faits de depart

- Deux skills : `enrichir-brain` (100 lignes, 11 etapes, mode cible + mode balayage) et
  `planifier-projet` (82 lignes).
- **Aucun `settings.json` versionne** dans `.claude/` — seulement `settings.example.json`
  et `settings.local.example.json`. Les hooks ne sont donc pas partages avec le depot.
- `AI/scripts/session_to_devbrain.py` existe (hook `Stop` annonce dans `CLAUDE.md`) mais
  `AI/sessions/` ne contient que **2 fichiers** : verifier si le hook est reellement branche.
- 610 lignes de consignes reparties sur `CLAUDE.md`, `CLAUDE-build.md`, `CLAUDE-project.md`.

## Questions a instruire

1. **Le skill est-il executable ou recitable ?** Relire les 11 etapes d'`enrichir-brain` et
   marquer chacune : verifiable par script / verifiable par lecture / invisible. Toute etape
   invisible est une etape qui sera omise un jour.
2. **Le decoupage.** Un skill de 11 etapes couvrant capture + verification + regeneration +
   commit + merge + push est-il la bonne unite ? Evaluer un decoupage (capture / cloture)
   contre le cout de la coordination entre deux skills.
3. **Le declenchement.** Quel mecanisme rendrait l'omission impossible ou visible : un hook
   `PostToolUse` qui refuse une ecriture dans `Dev/` hors skill, un hook `Stop` qui verifie
   que `check_brain` a tourne, une entree dans `CLAUDE.md`, ou rien de tout cela ? Peser la
   friction : un garde-fou trop strict se contourne, et alors il ne garantit plus rien.
4. **La redondance consignes / skill.** 610 lignes de `CLAUDE*.md` plus 182 lignes de skills :
   qu'est-ce qui est dit deux fois, et que se passe-t-il quand les deux versions divergent ?
5. **Les hooks non versionnes.** `settings.json` absent du depot signifie que la mecanique
   d'automatisation n'est pas reproductible sur une autre machine. Est-ce un choix ou un oubli ?
   (cf. `Documentation/perso/machines.md`)
6. **`planifier-projet`** : a-t-il jamais tourne ? `Projects/` est un scaffold vide. Un skill
   jamais exercice est un skill non teste — le confronter a l'index reel et dire s'il
   fonctionnerait aujourd'hui, notamment son filtrage sur les 10 champs de `brain-index.json`.
7. **Que devrait faire un skill d'audit ?** Cet axe-ci et les cinq autres sont conduits a la
   main. Si l'exercice doit se repeter, une partie merite-t-elle d'etre outillee ?

## Hors perimetre

L'ecriture ou la reecriture des skills. Le contenu du brain. Les autres axes.

## Livrable

Le rapport, plus **en annexe** : le tableau des 11 etapes d'`enrichir-brain` avec leur
verifiabilite, et la recommandation de decoupage si elle est retenue, sous forme de
sommaire des skills cibles (pas leur contenu).
