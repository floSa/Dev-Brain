---
galaxie: meta
nom: lot-5-comparatifs
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 5 — Les comparatifs deviennent des pages

Effort : **une session**. 47 fichiers.

Prérequis : lot 3 fait — chaque comparatif doit savoir dans quel dossier il atterrit.

## Contexte

Un `.base` est un fichier YAML de requête : **ni frontmatter, ni corps**. Il ne peut donc ni
porter de couleur dans le graphe, ni pointer vers ce qu'il compare. Mesure au 2026-09-04 :
44 comparatifs sur 47 sont cités par une fiche, et **aucun ne cite quoi que ce soit**. Ce sont
47 culs-de-sac gris, par construction et non par négligence.

Trois ne sont cités par personne : `Détection & segmentation`, `Forecasting`,
`Suivi d'expériences ML`.

## Périmètre

- Les 47 fichiers `Dev/Patterns/Comparatif - *.base`.
- Les fiches qui les citent, pour que le lien pointe vers la page et non vers le `.base`.

**Hors périmètre** : les 5 `Pattern - *.md`, les Rules, le corps des briques.

## Décision préalable

Le lot 0 a testé si une requête de base s'écrit directement en bloc de code dans une page.

- **Si le test a réussi** : un seul fichier par comparatif. Le `.base` disparaît, la page
  porte la requête en bloc de code. 47 fichiers supprimés, rien à synchroniser.
- **Si le test a échoué** : deux fichiers. La page embarque la vue par `![[X.base]]`, syntaxe
  vérifiée le 2026-09-04.

Lire les *Remontées* du pilote avant de commencer. En l'absence de résultat, prendre la
version à deux fichiers, qui est sûre.

## Gabarit cible

```markdown
---
role: comparatif
nom: Comparatif - Bases vectorielles
categorie: database/vecteur
tags: [vector-db]
---

# Comparatif - Bases vectorielles

> On tranche sur : self-host possible, filtrage pendant la recherche, volume.

![[Comparatif - Bases vectorielles.base]]

## Ce qui départage

- [[Qdrant]] — filtrage payload appliqué pendant la recherche, pas après
- [[Weaviate]] — l'embedding est délégué à la base
- [[pgvector]] — le bon choix si du Postgres est déjà en place
```

La ligne d'accroche dit **le critère de décision**, pas le sujet. « On tranche sur : … » est
la formule imposée : c'est elle qui distingue un comparatif utile d'un tableau de plus.

Chaque puce de `## Ce qui départage` nomme **ce qui rend cette brique différente des autres du
tableau** — pas son pitch, qui est déjà dans la colonne du tableau. C'est la seule section où
l'on écrit une comparaison plutôt qu'une description.

## Procédure

1. Pour chaque `.base`, déterminer son dossier d'accueil depuis son filtre `categorie`.
   **Neuf comparatifs ne filtrent pas sur `categorie`** — ils passent par les tags. Leur
   dossier se pose à la main ; ils sont listés en fin de `v3-arborescence.md`.
2. Créer la page `.md` au gabarit ci-dessus, dans ce dossier.
3. Écrire la ligne « On tranche sur : … » et la section `Ce qui départage`. Cette partie se
   **lit dans les fiches comparées**, elle ne s'invente pas : chaque puce doit être vérifiable
   dans le corps de la brique correspondante.
4. Repointer les liens entrants vers la page, plus vers le `.base`.
5. Traiter les trois comparatifs orphelins : soit les citer depuis le hub de leur dossier,
   soit les signaler comme inutiles dans les *Remontées*.

## Critères d'acceptation

- [ ] 47 pages `role: comparatif`, chacune dans le dossier de son domaine.
- [ ] Chaque page porte une ligne « On tranche sur : … » et au moins deux puces liées.
- [ ] Aucun lien entrant ne pointe plus directement vers un `.base`.
- [ ] Chaque comparatif est cité par le hub de son dossier.
- [ ] `check_brain.py` au vert.

## Interdictions

- Ne pas inventer un critère de départage. S'il n'est pas dans les fiches comparées, il se
  demande — ou la puce ne s'écrit pas.
- Ne pas modifier le corps des briques comparées.
- Ne pas supprimer un `.base` tant que sa page ne fonctionne pas.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md puis AI/migration/lot-5-comparatifs.md, et vérifie les
Remontées de AI/migration/README.md pour savoir quelle variante appliquer.

Commence par les 6 comparatifs du domaine Bases de données et montre-les-moi avant
de dérouler les 41 autres.

Chaque puce de « Ce qui départage » doit être vérifiable dans la fiche de la brique
concernée : cite-moi la source quand tu me les montres. Clôture avec cloturer-brain.
```
