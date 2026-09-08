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

<!-- AUTO:BANDEAU:START -->
> Moniteur de trafic réseau en Rust avec interface graphique multiplateforme : qui parle à qui, ports, protocoles, volumes, filtres, notifications et import/export PCAP.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Rust | open-source | Windows, macOS, Linux | — | à jour · 2026-07-22 |
<!-- AUTO:BANDEAU:END -->

## Définition

Analyseur de trafic réseau à interface graphique, écrit en Rust sur la bibliothèque GUI
`iced`. Il capture sur une interface choisie et répond à une question : qu'est-ce qui sort
de cette machine, vers qui, sur quel port, à quel volume. Pour chaque hôte distant, le nom
de domaine, l'ASN et le pays ; pour chaque flux, le protocole applicatif reconnu — le
projet revendique plus de 6 000 services et signatures — et le **programme local**
responsable. Il occupe la place entre `netstat`, instantané sans historique, et Wireshark,
dissection paquet par paquet à courbe d'apprentissage réelle : courbes temps réel,
favoris, notifications sur seuil ou sur liste noire d'IP, import et export PCAP. Le choix
de l'interface commande tout le résultat — le trafic d'un conteneur s'observe sur
l'interface bridge de l'hôte, jamais sur l'interface physique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vérifier ce qu'un service auto-hébergé émet réellement vers l'extérieur, avant une mise en production en réseau contraint | Dissection protocolaire fine, reconstruction de session, filtres BPF complexes : c'est le domaine de Wireshark et `tshark` (hors brain) |
| Identifier le processus qui consomme la bande passante sur un poste ou un serveur à accès graphique | Supervision continue et centralisée d'un parc : c'est une application locale, sans agent ni base historisée → [[Beszel]] |
| Confirmer qu'un traitement supposé hors ligne — modèle local, batch — ne fait aucun appel sortant | Serveur sans affichage : l'interface est graphique, il n'existe pas de mode terminal — sur une machine en SSH seul, l'outil ne s'utilise pas |
| Relire un PCAP fourni par une équipe réseau, sans monter Wireshark | Analyse de contenu chiffré : les métadonnées de flux sont visibles, les charges utiles TLS ne le sont pas |
| | Capture de longue durée : mémoire et fichiers PCAP croissent — l'outil est fait pour des sessions d'observation, pas pour tourner des semaines |
| | Se fier à l'étiquetage : la reconnaissance repose sur les ports et des signatures, un service sur port non standard reste générique, et l'attribution par programme dépend de l'OS — souvent non résolue pour les processus système ou les flux conteneurisés |

## Mise en œuvre

- Installation — Windows x64, arm64 et x86 par installeur ; Linux amd64, arm64, i386 et armhf en paquets DEB et RPM ou en AppImage ; macOS Intel et Apple Silicon
- Point d'entrée — application de bureau : on choisit l'interface, puis courbes, tableaux de flux, notifications et export PCAP
- Prérequis — **Npcap en mode compatible WinPcap** sous Windows, `libpcap` sous Linux : leur absence est le premier motif d'échec au lancement, et le message d'erreur ne le dit pas toujours clairement. Linux demande aussi ALSA, fontconfig et GTK 3 ; macOS n'a aucune dépendance supplémentaire
- Exécution — sur le poste, en local ; la capture exige des privilèges — sous Linux, `setcap cap_net_raw,cap_net_admin=eip <chemin>` plutôt que `sudo`, sous macOS une exécution en administrateur. Sans privilège, la liste des interfaces apparaît vide ou incomplète, symptôme trompeur qui ressemble à une panne de matériel
- Coût — gratuit, double licence MIT ou Apache-2.0 ; les données de géolocalisation et d'ASN proviennent de MaxMind et sont embarquées dans l'application

## Écosystème

### Alternatives

- *Aucune alternative déclarée : première entrée en `network/analyse`. Hors brain : Wireshark (dissection experte), `iftop`, `nethogs` et `bandwhich` (terminal, sans historique ni géolocalisation), ntopng (supervision réseau centralisée, bien plus lourde).*

## Ressources

- Documentation — https://github.com/GyulyVGC/sniffnet/wiki
- Dépôt — https://github.com/GyulyVGC/sniffnet
- Site — https://sniffnet.app

## Voir aussi

- [[Réseau]] — le hub du domaine
- [[Web-Check]] — l'angle inverse : ce qu'un service expose, vu de l'extérieur
- [[Docker]] — pour observer le trafic d'un conteneur, capturer sur l'interface bridge de l'hôte
