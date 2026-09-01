---
role: brique
nom: Sniffnet
alias: [sniffnet, gyulyvgc/sniffnet]
pitch: "Moniteur de trafic réseau en Rust avec interface graphique multiplateforme : qui parle à qui, ports, protocoles, volumes, filtres, notifications et import/export PCAP."
categorie: network/analyse
famille: application
domaines: [infra-ops]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: Rust
alternatives: []
complements: []
tags: [networking, traffic-analysis]
url_docs: https://github.com/GyulyVGC/sniffnet/wiki
url_repo: https://github.com/GyulyVGC/sniffnet
---

# Sniffnet

## Pourquoi

Analyseur de trafic réseau **à interface graphique**, écrit en Rust (bibliothèque GUI `iced`), double licence MIT ou Apache-2.0. Il capture sur une interface choisie et répond à la question « qu'est-ce qui sort de cette machine, vers qui, sur quel port, à quel volume ». Pour chaque hôte distant : nom de domaine, ASN, pays. Pour chaque flux : protocole applicatif reconnu (le projet revendique plus de 6 000 services, protocoles et signatures connues), et le **programme local** responsable du trafic.

Positionnement : la couche entre `netstat` (instantané, sans historique) et Wireshark (dissection paquet par paquet, courbe d'apprentissage réelle). Sniffnet se lit d'un coup d'œil, avec courbes temps réel, favoris, notifications déclenchées sur seuil ou sur liste noire d'IP, et import/export de fichiers PCAP.

En contexte on-prem, c'est l'outil de première intention pour caractériser le comportement réseau d'un service déployé chez un client : un conteneur qui appelle un domaine inattendu, un pipeline qui sature un lien, une machine coupée du monde qui parle quand même.

## Quand l'utiliser

- Vérifier ce qu'un service auto-hébergé émet réellement vers l'extérieur, avant une mise en production en réseau contraint.
- Identifier le processus qui consomme la bande passante sur un poste ou un serveur avec accès graphique.
- Confirmer qu'un traitement supposé hors ligne (modèle local, batch) ne fait aucun appel sortant.
- Relire un PCAP fourni par une équipe réseau, sans monter Wireshark.

## Quand NE PAS l'utiliser

- Dissection protocolaire fine, reconstruction de session, filtres BPF complexes : c'est le domaine de Wireshark / `tshark`.
- Supervision continue et centralisée d'un parc : Sniffnet est une application locale, sans agent ni base de données historisée → voir [[Dev/Services/Beszel|Beszel]] pour la supervision d'hôtes.
- Serveur sans affichage : l'interface est graphique, il n'y a pas de mode terminal. Sur une machine distante en SSH seul, l'outil ne s'utilise pas.
- Analyse de contenu chiffré : les métadonnées de flux sont visibles, pas les charges utiles TLS.

## Installation & plateformes

- **Windows** (x64, arm64, x86) : installeur, plus **Npcap** en mode compatible WinPcap — dépendance obligatoire.
- **Linux** (amd64, arm64, i386, armhf) : paquets DEB et RPM, AppImage. Dépendances système `libpcap`, ALSA, fontconfig, GTK 3.
- **macOS** (Intel et Apple Silicon) : aucune dépendance supplémentaire.

La capture demande des privilèges. Sur Linux, plutôt que `sudo`, accorder les capacités au binaire : `setcap cap_net_raw,cap_net_admin=eip <chemin>`. Sur macOS, exécution en administrateur requise. Les données de géolocalisation et d'ASN proviennent de MaxMind, embarquées dans l'application.

## Pièges

- **La dépendance de capture est le premier motif d'échec au lancement** : Npcap absent sur Windows, `libpcap` absent sur Linux. Le message d'erreur ne le dit pas toujours clairement.
- Sans privilège adéquat, la liste des interfaces apparaît vide ou incomplète — symptôme trompeur qui ressemble à un problème de matériel.
- L'attribution par programme dépend de l'OS et n'est pas toujours résolue pour les processus système ou les flux conteneurisés.
- Un flux passant par un conteneur Docker s'observe sur l'interface bridge de l'hôte, pas sur l'interface physique : choisir la bonne interface change tout le résultat.
- La reconnaissance de service repose sur les ports et des signatures : un service sur port non standard sera étiqueté de façon générique.
- Capture longue durée = mémoire et fichiers PCAP qui croissent ; l'outil est fait pour des sessions d'observation, pas pour tourner des semaines.

## Alternatives

Aucune fiche du brain ne couvre le même terrain aujourd'hui — Sniffnet est la première entrée en `network/analysis`. Les comparables hors brain sont Wireshark (dissection experte), `iftop` / `nethogs` / `bandwhich` (terminal, sans historique ni géolocalisation) et ntopng (supervision réseau centralisée, bien plus lourde).

## Liens

- [[Dev/Services/Beszel|Beszel]] — supervision des hôtes et conteneurs, complémentaire : Beszel dit *comment va la machine*, Sniffnet dit *ce qui circule*
- [[Dev/Services/Web-Check|Web-Check]] — l'angle inverse : ce qu'un service expose vu de l'extérieur
- [[Dev/Services/Docker|Docker]] — pour observer le trafic d'un conteneur, capturer sur l'interface bridge de l'hôte
- Site : https://sniffnet.app
- Repo : https://github.com/GyulyVGC/sniffnet
