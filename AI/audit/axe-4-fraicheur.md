# Axe 4 — Fraicheur & veracite

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-4-fraicheur.md`.

## Question centrale

**Combien de faits affirmes par ce brain sont devenus faux ?** Le vault n'affirme pas des
idees, il affirme des **donnees perissables** : licences, versions, prix, maturite, statut
de maintenance, scores de benchmark. Rien ne les re-verifie, rien ne les horodate.

## Le probleme, tel qu'il est diagnostique

Sur 337 fiches Dev, le brain declare **337 `status:`**, **336 `licence_type:`**,
**297 `maturite:`**, **334 `url_docs`**, **318 `url_repo`**, et mentionne un numero de
version dans **214 corps de page**, un prix dans 15, un nombre d'etoiles dans une dizaine.

Aucun de ces faits ne porte de date de verification. Consequence : une fiche ecrite en juin
et une fiche ecrite hier sont indiscernables, et un projet mort continue d'etre presente
comme `status: actif`.

Cas d'ecole survenu le 2026-09-02 : `osint4all` a ete fiche `status: abandonne` uniquement
parce qu'un agent est alle regarder la date du dernier commit — **2022-07-09**. Sans cette
verification manuelle, le brain aurait affirme qu'un projet mort depuis quatre ans etait vivant.
Le meme jour, trois autres faits fournis dans les consignes se sont reveles faux a la
verification (fonctions annoncees et non livrees, licence open-core presentee comme
open-source, pourcentages inexacts) — cf. le message du commit `a66d346`.

La question n'est donc pas *si* le brain contient des faux, mais **combien**.

## Questions a instruire

1. **Mesurer, par echantillon.** Tirer **30 fiches Dev au hasard** (graine fixee et notee,
   pour que le tirage soit reproductible) et verifier en ligne, pour chacune : le depot
   existe-t-il encore, quelle est la date du dernier commit, la licence declaree est-elle
   la bonne, la `maturite` et le `status` sont-ils defendables, les URLs repondent-elles.
   En deduire un **taux d'erreur estime** sur les 337, avec son intervalle.
2. **Quels champs pourrissent le plus vite ?** Classer par risque : `maturite` et `status`
   (mois), version (semaines), prix (mois), licence (rare mais grave), URL (rare).
3. **Que peut-on automatiser ?** L'API GitHub donne `pushed_at`, `archived`, `license` et
   `stargazers_count` en un appel par depot — 318 fiches portent un `url_repo`. Specifier
   un script de re-verification : ce qu'il lit, ce qu'il signale, ce qu'il ne doit **jamais**
   modifier tout seul (un `status:` ne se change pas sans lecture humaine).
4. **Faut-il un champ `verifie_le:`** dans le gabarit ? Peser : il resout la tracabilite mais
   ajoute un champ a maintenir sur 337 fiches, et `check_brain` interdit tout champ hors
   gabarit — la modification touche le validateur et les trois modeles.
5. **Quelle politique de peremption ?** Au-dela de quel age une fiche est-elle « a re-verifier » ?
   Que fait-on d'une fiche perimee : un avertissement, une section `## Pieges`, un `status`
   dedie ? Trancher avec l'usage reel en tete : le brain sert a **choisir une brique**, et une
   licence fausse ou un projet mort produisent une mauvaise decision projet.
6. **Les chiffres auto-declares.** Plusieurs fiches citent des benchmarks annonces par le
   projet lui-meme, parfois contradictoires entre deux fiches concurrentes (`pdf-inspector`
   annonce 0,875 et `OpenDataLoader PDF` 0,907 **sur le meme corpus**). La convention actuelle
   est de les presenter comme auto-declares. Suffit-il ?

## Hors perimetre

Le rangement (axe 1), les regles du validateur (axe 2). Ici on ne parle que de la **verite
et de l'age** de ce qui est ecrit.

## Livrable

Le rapport, plus **en annexe** : le tableau des 30 fiches echantillonnees avec, pour chacune,
champ verifie / valeur du brain / valeur constatee / verdict ; et la specification du script
de re-verification (entrees, sorties, ce qu'il refuse de faire).
