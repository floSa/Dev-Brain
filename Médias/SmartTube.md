---
role: brique
nom: SmartTube
alias: [SmartTubeNext, STN, yuliskov/SmartTube]
pitch: "Client YouTube alternatif pour Android TV et box (MIT, Java) : lecture sans publicité, SponsorBlock, sans Google Services. Distribué hors magasin par APK à installer soi-même."
categorie: media/video
famille: application
domaines: []
licence_type: open-source
os: "Android TV 4.3+ : téléviseurs Android/Google TV, box, NVIDIA Shield, Chromecast with Google TV, FireTV d'avant octobre 2025. Ni smartphone, ni tablette, ni Tizen, ni webOS, ni tvOS."
langage: Java
alternatives: []
complements: []
tags: [media-player, privacy]
url_docs: https://smarttubeapp.github.io
url_repo: https://github.com/yuliskov/SmartTube
---

# SmartTube

<!-- AUTO:BANDEAU:START -->
> Client YouTube alternatif pour Android TV et box (MIT, Java) : lecture sans publicité, SponsorBlock, sans Google Services. Distribué hors magasin par APK à installer soi-même.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Java | open-source | Android TV 4.3+ : téléviseurs Android/Google TV, box, NVIDIA Shield, Chromecast with Google TV, FireTV d'avant octobre 2025. Ni smartphone, ni tablette, ni Tizen, ni webOS, ni tvOS. | — |
<!-- AUTO:BANDEAU:END -->

## Définition

**Avertissement de rangement, à lire en premier** : c'est la page la plus éloignée du périmètre
de ce brain, qui documente des briques data, ML et IA pour de l'ingénierie on-prem. Un client
de lecture vidéo pour téléviseur n'a aucun rapport. Elle est classée en `media/video` faute de
catégorie adéquate, et son champ `domaines:` est **volontairement vide** — aucune des six
valeurs du vocabulaire ne s'applique, ce qui l'exclut par construction des hubs de `Métiers/`.
Cette page est ici par utilité domestique, pas par cohérence.

Ce qu'elle documente : un client alternatif pour Android TV qui lit les contenus YouTube sans
publicité, intègre SponsorBlock pour sauter les segments sponsorisés, ne requiert pas les
Google Services, gère 8K, 60 fps et HDR, et expose une vitesse de lecture réglable. Environ
32 500 étoiles GitHub, dépôt actif — dernier push le 2026-09-01, release `32.38s` le même jour.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Remplacer l'application YouTube d'un téléviseur ou d'une box Android par un lecteur sans publicité | **Ce type de client dépend d'API non publiques et casse régulièrement** : une évolution côté YouTube peut interrompre la lecture jusqu'à la release suivante. C'est structurel, pas accidentel |
| Faire revivre un appareil ancien — Android 4.3 suffit — que l'application officielle ne sert plus correctement | **Incident de sécurité annoncé par le mainteneur** : son environnement de développement a été infecté, quelques builds ont pu être affectés et les clés publiques compromises. Poste réinstallé et builds désormais scannés via VirusTotal — à peser avant d'installer une version ancienne |
| Sauter automatiquement les segments sponsorisés sur un écran de salon | **Mises à jour hors magasin** : aucune vérification par un tiers, aucune révocation centralisée ; la chaîne de confiance tient à un dépôt et à un canal Telegram |
| | **Blocage anti-bot** : sans compte connecté, une plage d'IP peut être bloquée par « Sign in to confirm you're not a bot » — la lecture suppose alors une connexion |
| | Contexte professionnel ou parc géré : distribution hors magasin, dépendance à des API non publiques, et le projet décline explicitement toute responsabilité sur l'usage de services tiers |
| | Smartphone ou tablette : techniquement installable, mais non optimisé et sans support officiel |
| | Téléviseur non-Android (Samsung Tizen, LG webOS) ou Apple TV : incompatible, il faut une box ou une clé |
| | FireTV sortis à partir d'octobre 2025 (Fire Stick 4k Select et suivants) : VegaOS n'est plus Android, l'application ne fonctionne pas |
| | Aucune déclaration explicite sur la **télémétrie** n'a été trouvée : le projet affirme ne contenir aucun code publicitaire et ne pas exiger les Google Services, rien de plus n'est affirmé ici |
| | Limites reconnues par le projet : commentaires instables, recherche vocale et casting en retrait par rapport à l'application officielle selon l'appareil |

## Mise en œuvre

- Installation — manuelle, par APK. Le projet insiste : **ne rien installer depuis un magasin d'applications, un site d'APK ou un blog**, ces dépôts ne sont pas les siens. Deux canaux légitimes, les *releases* GitHub et F-Droid (`app.smarttube.fdroid`), et deux branches — *beta*, recommandée par le projet pour la rapidité des correctifs, et *stable*
- Point d'entrée — l'application sur le téléviseur ; méthodes documentées : Downloader by AFTVnews, transfert de fichier depuis un autre appareil, clé USB avec un vrai gestionnaire de fichiers, ou `adb install`. Sur Chromecast with Google TV, activer d'abord les options développeur puis les sources inconnues
- Prérequis — Android TV 4.3 ou plus : téléviseurs Android/Google TV, box, NVIDIA Shield, Chromecast with Google TV, FireTV d'avant octobre 2025
- Exécution — sur l'appareil ; l'application embarque un **updater**, le sideload n'est donc à faire qu'une fois
- Coût — gratuit, MIT. Le `README` cite une clause « Limitation of Liability » numérotée 16, vestige d'un texte de type GPL ; le fichier `LICENSE` du dépôt est bien MIT, et c'est lui qui fait foi

## Écosystème

### Alternatives

<!-- Aucune : le brain ne contient aucun autre client de lecture vidéo, et OpenCut (montage) n'en est pas un substitut. -->

## Ressources

- Documentation — https://smarttubeapp.github.io
- Dépôt — https://github.com/yuliskov/SmartTube

## Voir aussi

- [[Médias]] — le hub du domaine
- [[OpenCut]] — l'autre page `media/video` du brain ; montage et non lecture, et le même avertissement de rangement
- [[Video generation]] — synthèse de vidéo par modèle : sans rapport, cité seulement pour écarter la confusion de vocabulaire
