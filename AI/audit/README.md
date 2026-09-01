# Audit du DevBrain — six axes

Chantier d'audit ouvert le **2026-09-02**. Objet : le vault a grandi au fil de l'eau
(647 pages, 112 categories, 321 tags) et son rangement, ses controles et ses skills
n'ont jamais ete instruits a froid. Chaque axe est autonome et s'instruit dans **une
conversation dediee**.

## Chaine de traitement

```
        AI/audit/axe-N-*.md                 AI/audit/rapports/axe-N-*.md
  brief ────────────────────► AUDITEUR ──────────────────────► ORCHESTRATEUR
  (ce dossier)               lit, mesure,                     arbitre ce qui
                             ne corrige RIEN                  est retenu
                                                                    │
                                                                    ▼
                                                              CORRECTEUR
                                                        applique, valide, commit
```

Trois roles, trois conversations distinctes. **Un auditeur ne corrige jamais** : il
constate, prouve, chiffre et recommande. Ce qui est retenu part ensuite vers une
conversation de correction, avec un perimetre ferme. Cette separation existe parce
qu'un agent qui corrige ce qu'il vient de trouver ne documente pas ses arbitrages.

## Socle factuel commun

`AI/audit/mesures-<date>.md`, produit par `AI/scripts/audit_mesures.py` (lecture seule).
**Tout auditeur commence par le relancer** — si un chiffre du brief a bouge, c'est le
vault qui fait foi, pas le brief.

```bash
uv run AI/scripts/audit_mesures.py > AI/audit/mesures-$(date +%F).md
```

## Les six axes

| # | Axe | Question centrale | Brief |
|---|-----|-------------------|-------|
| 1 | Rangement & taxonomie | Ou va une page, et qui le decide ? | `axe-1-rangement.md` |
| 2 | Integrite au fil de l'eau | Qu'est-ce qui casse sans que rien ne le dise ? | `axe-2-integrite.md` |
| 3 | Skills | Qu'est-ce qui garantit que la procedure soit suivie ? | `axe-3-skills.md` |
| 4 | Fraicheur & veracite | Combien de faits affirmes sont devenus faux ? | `axe-4-fraicheur.md` |
| 5 | Navigation & exploitabilite | Le brain sert-il ses deux consommateurs ? | `axe-5-navigation.md` |
| 6 | Pilier REX | Un pilier a 0,3 % d'usage : reparer ou assumer ? | `axe-6-rex.md` |

Ordre conseille : **2 et 4 d'abord** (ils mesurent des degats existants, sans decision
de conception), puis **1** (la refonte, qui depend de ce que 2 aura trouve), puis 3, 5, 6.

## Format de rapport imposé

Chaque auditeur ecrit **un seul fichier**, `AI/audit/rapports/axe-<N>-<slug>.md` :

```markdown
# Rapport d'audit — Axe <N> : <titre>

Auditeur : <conversation>, le <date>. Socle : mesures-<date>.md relance le <date>.

## Synthese
Cinq lignes maximum. Le constat principal, et la seule chose a faire si on n'en fait qu'une.

## Constats

### C1. <titre court> — gravite : bloquant | serieux | mineur
- **Constat** : ce qui est, factuellement.
- **Preuve** : la commande lancee et sa sortie (extrait suffisant, pas un dump).
- **Portee** : combien de pages / fichiers concernes.
- **Cause** : pourquoi c'est arrive (mecanisme, pas coupable).
- **Recommandation** : ce qu'il faut faire, precisement.
- **Effort** : S (< 1 h) | M (une session) | L (chantier), + fichiers impactes.

## Ce qui va bien
Ce qui n'a PAS besoin d'etre touche, et pourquoi. Section obligatoire : un audit qui ne
trouve que des problemes n'a pas cherche.

## Questions laissees ouvertes
Ce qui releve d'un arbitrage du proprietaire, pas d'un constat technique.
```

Regles de forme : francais, ton impersonnel, phrases courtes, aucun emoji. Une
recommandation non chiffree en effort ne compte pas. Un constat sans preuve reproductible
ne compte pas.

## Interdictions communes a tous les auditeurs

1. **Ne modifier aucune page** de `Dev/`, `Wiki/`, `MOC/`, `Documentation/`, `Templates/`.
2. **Ne rien committer, ne rien pousser.** Aucune commande git en ecriture.
3. **Ne pas relancer** `build_index.py`, `build_mocs.py`, `build_links.py` (ils ecrivent).
   `check_brain.py` et `audit_mesures.py` sont en lecture seule : les lancer librement.
4. **N'ecrire qu'un seul fichier** : son propre rapport dans `AI/audit/rapports/`.
5. **Ne pas proposer de refonte non demandee** hors du perimetre de son axe. Ce qui
   deborde va en *Questions laissees ouvertes*.

## Etat d'avancement

| Axe | Rapport rendu | Retenu par le proprietaire | Corrige |
|-----|---------------|----------------------------|---------|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |
| 4 | — | — | — |
| 5 | — | — | — |
| 6 | — | — | — |
