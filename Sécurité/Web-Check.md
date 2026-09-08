---
role: brique
nom: Web-Check
alias: [web-check, lissy93/web-check]
pitch: "Audit d'un site depuis sa seule URL, sans accès privilégié : DNS, TLS, en-têtes de sécurité, technologies détectées, redirections, ports, traceroute, listes de blocage et archives — auto-hébergeable en Docker."
categorie: security/recon
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: single-node
alternatives: []
complements: []
tags: [recon, networking, osint, self-hosted]
url_docs: https://web-check.xyz/about
url_repo: https://github.com/Lissy93/web-check
---

# Web-Check

<!-- AUTO:BANDEAU:START -->
> Audit d'un site depuis sa seule URL, sans accès privilégié : DNS, TLS, en-têtes de sécurité, technologies détectées, redirections, ports, traceroute, listes de blocage et archives — auto-hébergeable en Docker.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-08-27 |
<!-- AUTO:BANDEAU:END -->

## Définition

On saisit une URL, l'outil lance une trentaine de sondes en parallèle et rend une page de
fiches : résolution IP et géolocalisation, enregistrements DNS (A, MX, NS, CNAME, TXT),
chaîne de certificats TLS, en-têtes HTTP et en-têtes de sécurité, WHOIS du domaine,
technologies et serveur détectés, redirections, ports ouverts, traceroute, présence dans
des listes de blocage, historique Wayback Machine, empreinte carbone estimée. Rien
n'exige d'authentification ni d'accès au serveur cible — mais le balayage de ports et le
traceroute restent des actions **actives**, et la façade « saisir une URL » ne l'efface
pas. C'est une liste de contrôle exécutable, pas un audit : une fiche vide signale une
clé d'API absente ou un délai dépassé, jamais un verdict sur la cible.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recette de mise en ligne : vérifier de l'extérieur ce qu'un service déployé expose réellement | Test d'intrusion ou balayage de vulnérabilités : ce n'est pas un scanner, il ne cherche aucune faille applicative |
| Contrôler d'un geste les en-têtes de sécurité et la configuration TLS d'un domaine, sans un outil dédié par sujet | Audit TLS à valeur d'attestation : Qualys SSL Labs reste la mesure citée dans les rapports (hors brain) |
| Reconnaissance préliminaire sur un domaine tiers : fournisseur, technologies, historique | Supervision continue : l'outil rend un instantané, il n'historise rien et n'alerte pas → [[Beszel]] |
| Comparer l'avant et l'après d'un changement d'infrastructure — migration, ajout de CDN, changement de certificat | Cible qui n'appartient pas au demandeur, sans autorisation écrite : balayage de ports et traceroute engagent une responsabilité, même sur de la donnée publique |
| | Conclure sur une version ou une technologie : la détection repose sur des empreintes, les faux positifs et les versions périmées sont fréquents |
| | Analyse de code, de dépendances ou de conteneurs : périmètre entièrement différent |

## Mise en œuvre

- Installation — `docker run -p 3000:3000 lissy93/web-check`, ou déploiement Netlify, Vercel, Render, ou construction depuis les sources (Node.js et Yarn). L'instance publique `web-check.xyz` convient à une vérification ponctuelle, mais elle envoie l'URL auditée à un tiers — ce qui suffit à l'exclure d'un contexte client
- Point d'entrée — application web : une URL saisie, une trentaine de fiches rendues en parallèle
- Prérequis — Node.js hors conteneur ; clés d'API **optionnelles** pour certaines sondes (Google Cloud PageSpeed, Shodan, WhoAPI, SecurityTrails, urlscan.io, BuiltWith) — sans elles ces fiches restent vides et le reste fonctionne. Les plateformes sans sockets bruts (Netlify, Vercel) tronquent le traceroute et le balayage de ports
- Exécution — auto-hébergé ou instance publique, mono-nœud ; délai d'expiration par sonde (25 s par défaut) et limitation de débit configurables
- Coût — gratuit, MIT ; les clés d'API tierces relèvent chacune de leur propre offre. Version publiée au 2026-07-28 : 2.2.0

## Écosystème

### Alternatives

- *Aucune alternative déclarée : première entrée en `security/recon`. Comparables hors brain, sujet par sujet : Qualys SSL Labs et `testssl.sh` (TLS), Mozilla Observatory et `securityheaders.com` (en-têtes), `nmap` (ports, bien plus complet), Shodan et Censys (empreinte Internet), `dnsrecon` (DNS). Web-Check n'égale aucun d'eux ; il évite d'en lancer six.*

## Ressources

- Documentation — https://web-check.xyz/about
- Dépôt — https://github.com/Lissy93/web-check

## Voir aussi

- [[Sécurité]] — le hub du domaine
- [[osint4all]] — l'annuaire où trouver les outils spécialisés que Web-Check ne remplace pas
- [[Sniffnet]] — l'angle inverse : le trafic vu depuis l'intérieur de la machine
- [[Docker]] — la voie d'auto-hébergement, la seule qui active toutes les sondes
