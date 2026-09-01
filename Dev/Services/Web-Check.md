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

## Pourquoi

On saisit une URL, l'outil lance une trentaine de sondes en parallèle et rend une page de fiches : résolution IP et géolocalisation, enregistrements DNS (A, MX, NS, CNAME, TXT), chaîne de certificats TLS, en-têtes HTTP et en-têtes de sécurité, WHOIS du domaine, technologies et serveur détectés, redirections, ports ouverts, traceroute, présence dans des listes de blocage malware/hameçonnage, historique Wayback Machine, empreinte carbone estimée.

Tout est **non intrusif** : uniquement de l'information publiquement observable, sans authentification ni accès au serveur cible. Licence MIT, écrit en TypeScript (Astro, Svelte, Node.js).

L'utilité pratique pour qui auto-héberge : après avoir mis un service derrière un reverse proxy chez un client, obtenir en une passe la vue extérieure — le certificat est-il bien servi sur toute la chaîne, `Strict-Transport-Security` est-il présent, quels ports répondent, le domaine fuit-il des enregistrements oubliés. C'est une liste de contrôle exécutable plutôt qu'un audit de sécurité.

## Quand l'utiliser

- Recette de mise en ligne : vérifier de l'extérieur ce qu'un service déployé expose réellement.
- Contrôle rapide des en-têtes de sécurité et de la configuration TLS d'un domaine, sans outil dédié par sujet.
- Reconnaissance préliminaire sur un domaine tiers : fournisseur, technologies, historique.
- Comparer avant/après un changement d'infrastructure (migration, ajout de CDN, changement de certificat).

## Quand NE PAS l'utiliser

- Test d'intrusion ou balayage de vulnérabilités : ce n'est pas un scanner, il ne cherche aucune faille applicative.
- Audit TLS de référence à valeur d'attestation : Qualys SSL Labs reste la mesure citée dans les rapports.
- Supervision continue de disponibilité : l'outil rend un instantané, il n'historise rien ni n'alerte → [[Dev/Services/Beszel|Beszel]] pour l'état des machines.
- Analyse de code, de dépendances ou de conteneurs : périmètre entièrement différent.
- Cible n'appartenant pas au demandeur, sans autorisation : le balayage de ports et le traceroute engagent une responsabilité, même sur des données publiques.

## Déploiement & coût

Deux voies. Instance publique sur `web-check.xyz`, gratuite, pratique pour une vérification ponctuelle — mais l'URL auditée est envoyée à un tiers, ce qui suffit à l'exclure de certains contextes clients.

Auto-hébergement : `docker run -p 3000:3000 lissy93/web-check`, ou déploiement sur Netlify, Vercel, Render, ou construction depuis les sources (Node.js et Yarn). Coût logiciel nul. Plusieurs sondes s'enrichissent de clés d'API **optionnelles** (Google Cloud pour PageSpeed, Shodan, WhoAPI, SecurityTrails, urlscan.io, BuiltWith) : sans clés, ces fiches restent vides, le reste fonctionne. Un délai d'expiration par sonde (25 s par défaut) et une limitation de débit configurable évitent les blocages. Version publiée au 2026-07-28 : 2.2.0.

## Pièges

- **Les fiches vides ne signalent pas un problème sur la cible** mais l'absence de clé d'API ou un dépassement de délai : lire l'outil comme un faisceau d'indices, pas comme un verdict.
- L'instance publique divulgue au tiers ce que l'on audite. Pour un domaine client, auto-héberger.
- Le balayage de ports et le traceroute sont des actions actives : dans certains pays et sur certains contrats, elles exigent une autorisation écrite. La façade « saisir une URL » ne l'efface pas.
- Le déploiement sans conteneur (Netlify, Vercel) tronque les sondes qui demandent des sockets bruts : le traceroute et les ports ne fonctionnent pas partout de la même façon.
- Détection de technologies fondée sur des empreintes : faux positifs et versions obsolètes fréquents.
- Aucune persistance : rien n'est conservé d'une exécution à l'autre, il n'y a pas de suivi de dérive intégré.

## Alternatives

Champ vide, faute de fiche réciproque : première entrée en `security/recon`. Comparables hors brain, par sujet : Qualys SSL Labs et `testssl.sh` (TLS), Mozilla Observatory et `securityheaders.com` (en-têtes), `nmap` (ports, bien plus complet), Shodan et Censys (empreinte Internet), `dnsrecon` (DNS). Web-Check n'égale aucun d'eux ; il évite d'en lancer six.

## Liens

- [[Dev/Outils/osint4all|osint4all]] — l'annuaire de liens où trouver les outils spécialisés que Web-Check ne remplace pas
- [[Dev/Outils/Sniffnet|Sniffnet]] — l'angle inverse : le trafic vu depuis l'intérieur de la machine
- [[Dev/Services/Docker|Docker]] — voie d'auto-hébergement recommandée, la seule qui active toutes les sondes
- Démo publique : https://web-check.xyz
- Repo : https://github.com/Lissy93/web-check
