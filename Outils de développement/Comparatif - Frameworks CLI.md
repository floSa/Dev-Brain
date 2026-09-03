---
role: comparatif
nom: Comparatif - Frameworks CLI
categorie: devtools/cli
tags: [cli, terminal-ui]
---

# Comparatif - Frameworks CLI

> On tranche sur : déclarer les commandes ou peindre la sortie — ce sont deux couches, pas deux options.

![[Comparatif - Frameworks CLI.base]]

## Ce qui départage

- [[Typer]] — ne rend rien à l'écran : il **déduit la CLI des annotations de type**, arguments, validation, `--help` et complétion shell compris. Couche au-dessus de Click, dont il faut parfois redescendre l'API pour les cas tordus.
- [[Rich]] — ne parse aucune commande : il **compose la sortie** — tables, barres de progression, Markdown, tracebacks reformatés — et c'est lui que Typer appelle pour son aide enrichie. Hors d'un TTY il désactive les couleurs, ce qui surprend en CI.
