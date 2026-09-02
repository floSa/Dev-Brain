---
role: hub
nom: Réseau
alias: [reseau, network]
pitch: Voir ce qui circule sur un lien, et faire circuler un fichier d'une machine à l'autre.
domaines: [infra-ops]
tags: [networking, traffic-analysis, file-transfer]
---

# Réseau

> Voir ce qui circule sur un lien, et faire circuler un fichier d'une machine à l'autre.

## Ce qu'il faut comprendre

- Deux besoins ponctuels, deux briques, aucune pile : ce domaine n'est pas une couche d'architecture mais une paire d'outils qu'on lance quand la question se pose.
- **Observer** ([[Sniffnet]]) répond à « qui parle à qui, sur quel port, à quel débit ». C'est le premier réflexe utile quand un service on-prem est lent ou qu'une machine parle à quelqu'un d'inattendu — et le complément naturel de [[Web-Check]], qui regarde depuis l'extérieur.
- **Transférer** ([[croc]]) répond à « envoyer ce fichier à cette autre machine, maintenant ». L'intérêt technique est le PAKE : une phrase de passe courte, échangée hors bande, suffit à établir un canal chiffré de bout en bout sans clé à distribuer ni compte à créer. Le relais public ne voit passer que du chiffré, et s'auto-héberge.
- La question du **stockage** durable de fichiers n'est pas ici mais dans [[Stockage]] : un transfert est un geste, pas un dépôt.

## Choisir

- Comprendre le trafic d'une machine, avec une interface plutôt qu'un `tcpdump` → [[Sniffnet]].
- Envoyer un fichier ou un dossier entre deux machines, sans cloud → [[croc]].

<!-- AUTO:START -->
### Briques
- [[croc]] — Transfert de fichiers de machine à machine par phrase de passe : chiffrement de bout en bout via PAKE, relais public ou auto-hébergé, reprise sur interruption, un seul binaire.
- [[Sniffnet]] — Moniteur de trafic réseau en Rust avec interface graphique multiplateforme : qui parle à qui, ports, protocoles, volumes, filtres, notifications et import/export PCAP.
<!-- AUTO:END -->
