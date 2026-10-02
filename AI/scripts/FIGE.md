---
nom: FIGE
---

# Instance FIGÉE — ce qui est copié, ce qui est perdu

Figée le 2026-09-29, depuis BrainKit `0.1.0`.

## Pourquoi

Une instance normale ne contient **pas de code** : le kit vit ailleurs, installé
une fois, et lit `brain.yml`. C'est ce qui garantit qu'une correction du
validateur atteint toutes les instances le même jour.

Ce vault a été **figé** : le kit y a été copié. C'est le mode prévu pour une
livraison on-prem, où l'instance ne peut pas dépendre d'un dépôt externe.

## Ce qui est copié

- `AI/scripts/brainkit/` — les deux validateurs, les quatre générateurs, le semis.
- `AI/scripts/valider.py`, `generer.py`, `semer.py` — trois lanceurs à en-tête
  PEP 723. Ils résolvent `brain.yml` et la racine du vault tout seuls.

```bash
uv run AI/scripts/valider.py
uv run AI/scripts/generer.py            # --check
uv run AI/scripts/generer.py --ecrire
```

## Ce qui est PERDU — et c'est le prix, pas un défaut

| Ce qui reste dehors | Conséquence |
|---|---|
| Les correctifs à venir | **Cette instance ne recevra plus rien.** Un défaut corrigé dans le kit reste ici. |
| `schema/brain.schema.json` et son validateur | Un `brain.yml` modifié ne se vérifie plus contre le contrat. |
| `outils/fidelite.py` et les jeux d'épreuve | Aucun moyen de prouver, sur place, que ce kit figé se comporte comme le kit. |
| La comparabilité | Deux instances figées à deux dates ne portent pas le même code, et rien ne le dit à l'ouverture. |

## Revenir en arrière

Il n'y a pas de `unfreeze`, et c'est délibéré : un dégel silencieux ferait
cohabiter deux versions du même code sans que personne ne le sache. Pour
rebrancher l'instance : supprimer `AI/scripts/brainkit/` et les trois lanceurs,
remettre `kit.mode: branche` dans `brain.yml`, et installer le kit.

## Report manuel du 2026-10-02 — la carte de lecture

Une exception à « cette instance ne recevra plus rien », décidée pour un cas
précis : le cinquième artefact (`genere.carte`, générateur `carte.py`) a été
reporté **à la main** depuis BrainKit au commit `5704de1`. Cinq fichiers de
`AI/scripts/brainkit/generer/` : `carte.py` (nouveau), `orchestre.py`,
`__main__.py`, `__init__.py`, `prose.py`. Le reste du paquet est inchangé, et la
copie est identique au kit à cet instant (`diff -rq` vide).

Ce n'est pas un re-gel : le kit refuse de figer une instance déjà figée, et ce
report ne contourne pas ce refus, il le remplace par un diff lisible. Toute
correction ultérieure du kit reste à reporter de la même façon, fichier par
fichier.

