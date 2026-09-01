---
galaxie: dev
type: outil
nom: SmartTube
alias: [SmartTubeNext, STN, yuliskov/SmartTube]
pitch: "Client YouTube alternatif pour Android TV et box (MIT, Java) : lecture sans publicité, SponsorBlock, sans Google Services. Distribué hors magasin par APK à installer soi-même."
categorie: media/video
famille: application
domaines: []
licence_type: open-source
os: "Android TV 4.3+ : téléviseurs Android/Google TV, box, NVIDIA Shield, Chromecast with Google TV, FireTV d'avant octobre 2025. Ni smartphone, ni tablette, ni Tizen, ni webOS, ni tvOS."
langage: Java
status: actif
alternatives: []
tags: [media-player, privacy]
url_docs: https://smarttubeapp.github.io
url_repo: https://github.com/yuliskov/SmartTube
---

# SmartTube

## Pourquoi

**Avertissement de rangement, à lire en premier** : c'est la page la plus éloignée du périmètre de ce brain, qui documente des briques data, ML et IA pour de l'ingénierie on-prem. Un client de lecture vidéo pour téléviseur n'a aucun rapport. Elle est classée en `tooling/video` faute de catégorie adéquate, son champ `domaines:` est **volontairement vide** (aucune des six valeurs du vocabulaire ne s'applique) et son champ `tags:` l'est aussi : aucun tag du vocabulaire fermé ne décrit un lecteur multimédia. Cette page est ici par utilité domestique, pas par cohérence.

Ce qu'elle documente : un client alternatif pour Android TV qui lit les contenus YouTube sans publicité, intègre SponsorBlock (saut des segments sponsorisés), ne requiert pas les Google Services, gère 8K, 60 fps et HDR, et expose une vitesse de lecture réglable. MIT, ~32 500 étoiles GitHub, dépôt actif (dernier push le 2026-09-01, release `32.38s` le même jour).

## Quand l'utiliser

- Remplacer l'application YouTube d'un téléviseur ou d'une box Android par un lecteur sans publicité.
- Faire revivre un appareil ancien (Android 4.3 suffit) que l'application officielle ne sert plus correctement.
- Sauter automatiquement les segments sponsorisés sur un écran de salon.

## Quand NE PAS l'utiliser

- Sur smartphone ou tablette : techniquement installable, mais non optimisé et sans support officiel.
- Sur un téléviseur non-Android (Samsung Tizen, LG webOS) ou Apple TV : incompatible, il faut passer par une box ou une clé.
- Sur les FireTV sortis à partir d'octobre 2025 (Fire Stick 4k Select et suivants) : VegaOS n'est plus Android, l'application ne fonctionne pas.
- Dans un contexte professionnel ou sur un parc géré : distribution hors magasin, dépendance à des API non publiques, et le projet décline explicitement toute responsabilité sur l'usage de services tiers.

## Installation & plateformes

Installation manuelle uniquement, par APK — le projet insiste : **ne rien installer depuis un magasin d'applications, un site d'APK ou un blog**, ces dépôts ne sont pas les siens. Deux canaux légitimes : les *releases* GitHub et F-Droid (`app.smarttube.fdroid`). Deux branches : *beta* (recommandée par le projet, corrections plus rapides) et *stable*.

Méthodes documentées : Downloader by AFTVnews sur le téléviseur, transfert de fichier depuis un autre appareil, clé USB avec un vrai gestionnaire de fichiers, ou `adb install` pour les utilisateurs avancés. Sur Chromecast with Google TV, il faut d'abord activer les options développeur puis les « sources inconnues ». L'application embarque un **updater** : le sideload n'est à faire qu'une fois, les mises à jour suivantes passent par l'application elle-même.

## Pièges

- **Ce type de client dépend d'API non publiques et casse régulièrement.** Une évolution côté YouTube peut interrompre la lecture jusqu'à la release suivante ; c'est structurel, pas accidentel.
- **Blocage anti-bot** : sans compte connecté, une plage d'IP peut être bloquée avec le message « Sign in to confirm you're not a bot ». La lecture suppose alors une connexion de compte.
- **Mises à jour hors magasin** : aucune vérification par un tiers, aucune révocation centralisée. La chaîne de confiance repose sur un dépôt et un canal Telegram.
- **Incident de sécurité annoncé par le mainteneur** : son environnement de développement a été infecté, quelques builds ont pu être affectés, les clés publiques ont pu être compromises. Le projet dit avoir réinstallé un poste propre et scanner désormais les builds via VirusTotal. À prendre en compte avant d'installer une version ancienne.
- **Absence de télémétrie non documentée** : le projet affirme ne contenir aucun code d'affichage de publicité et ne pas exiger les Google Services, mais aucune déclaration explicite sur la télémétrie n'a été trouvée. Rien n'est donc affirmé ici sur ce point.
- **Le README cite une clause « Limitation of Liability » numérotée 16**, vestige d'un texte de type GPL ; le fichier `LICENSE` du dépôt est bien MIT. En cas de doute, c'est le fichier qui fait foi.
- Limites reconnues par le projet : commentaires instables, recherche vocale et casting en retrait par rapport à l'application officielle selon l'appareil.

## Alternatives

- Aucune. Le brain ne contient aucun autre client de lecture vidéo, et [[Dev/Outils/OpenCut|OpenCut]] (montage) n'en est pas un substitut.

## Liens

- [[Dev/Outils/OpenCut|OpenCut]] — l'autre page `tooling/video` du brain ; montage, pas lecture, et le même avertissement de rangement
- [[Wiki/Concepts/Video generation|Video generation]] — synthèse de vidéo par modèle : sans rapport, cité seulement pour écarter la confusion de vocabulaire
- Repo : https://github.com/yuliskov/SmartTube
- Site : https://smarttubeapp.github.io
