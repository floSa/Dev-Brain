---
galaxie: dev
type: service
nom: Stirling PDF
alias: [stirling-pdf, stirling, s-pdf]
pitch: "Plateforme PDF web auto-hébergeable au cœur MIT : plus de 50 opérations (fusion, découpe, rotation, conversion, OCR, signature, rédaction, compression) exécutées sur son propre serveur, avec API REST et pipelines no-code ; SSO, audit et déploiement air-gapped réservés aux modules propriétaires."
categorie: tooling/document
famille: plateforme
licence_type: open-core
hosted: both
maturite: production
langage: Java
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [pdf, ocr, self-hosted]
url_docs: https://docs.stirlingpdf.com/
url_repo: https://github.com/Stirling-Tools/Stirling-PDF
---

# Stirling PDF

## Pourquoi

Remplace le triptyque « site de conversion gratuit + Acrobat + bricolage bureautique ». Application web Java lancée en un `docker run`, qui expose plus de 50 opérations sur des fichiers PDF : fusion, découpe, extraction et réorganisation de pages, rotation, conversion depuis et vers les formats bureautiques et images, OCR, signature, rédaction, compression, mots de passe, métadonnées. UI en plus de 40 langues, API REST sur la quasi-totalité des outils, et chaînage de pipelines sans code depuis l'interface.

L'argument central est la **non-circulation des documents**. Le traitement a lieu sur l'instance : le fichier reste sur la machine ou en mémoire du serveur le temps de l'opération. C'est la raison d'être en contexte on-prem, où un contrat, un dossier RH ou un plan client ne doit pas transiter par un service tiers.

Frontière avec la famille `data/parsing` : Stirling PDF produit un **document destiné à un humain** — un PDF fusionné, signé, allégé, lisible. Il ne produit pas de donnée structurée pour une machine : ni JSON à bounding boxes, ni ordre de lecture exploitable en aval d'un pipeline RAG. Ce besoin relève de [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]] et de ses voisins.

Modèle **open-core** assumé : le dépôt est sous MIT, sauf les répertoires `app/proprietary/`, `app/saas/`, `engine/` et plusieurs dossiers du frontend, chacun régi par sa propre licence. Projet très actif (v2.14.3 en août 2026, commits quotidiens, environ 91 000 étoiles GitHub).

## Quand l'utiliser

- Manipuler des PDF de façon régulière sans les envoyer sur un service en ligne : contrainte RGPD, données clients, réseau isolé.
- Mutualiser l'outillage PDF d'une équipe derrière une URL interne, plutôt que des installations poste par poste.
- Automatiser un traitement documentaire répétitif : l'API REST permet de scripter ce que l'UI fait à la main.
- Donner une interface d'appoint aux non-développeurs, à côté d'un pipeline Python existant.

## Quand NE PAS l'utiliser

- Extraire de la donnée structurée d'un PDF pour du RAG ou du ML → [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]], [[Dev/Services/Docling|Docling]], [[Dev/Services/Unstructured|Unstructured]].
- Manipuler des PDF depuis du code, sans serveur intermédiaire → [[Dev/Services/PyMuPDF|PyMuPDF]].
- Retoucher le contenu rédactionnel d'un document comme dans un traitement de texte : l'outil agit sur la structure du PDF, pas sur la rédaction.
- Besoin immédiat de SSO, d'audit, de base de données externe ou de déploiement air-gapped supporté : ces briques sont dans les modules payants.

## Déploiement & coût

- `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf`, puis `http://localhost:8080`. Images Docker officielles, Kubernetes, JAR bare-metal et clients desktop Windows, macOS et Linux.
- Trois variantes d'image : `latest` (standard, environ 1,5 Go, OCR et conversion bureautique inclus), `latest-ultra-lite` (environ 350 Mo compressés, sans Tesseract ni LibreOffice donc sans OCR ni conversion), `latest-fat` (plus de 2 Go, polices supplémentaires pour l'usage hors ligne).
- Deux JAR : celui par défaut sans authentification, et une variante `with-login` où l'authentification s'active par variables d'environnement (`SECURITY_ENABLELOGIN`).
- Cœur MIT gratuit. Le plan Server est annoncé par l'éditeur à 99 $/mois ou 999 $/an pour 100 utilisateurs, Enterprise sur devis ; une offre managée (Stirling Cloud) et un plan Processor à crédits existent séparément.
- Instance sans état : la montée en charge se fait par réplication derrière un répartiteur, chaque traitement restant sur un nœud.

## Pièges

- **« Gratuit » n'égale pas « illimité »** : la documentation éditeur annonce le plan gratuit « jusqu'à 5 utilisateurs ». Le plafond porte sur les composants propriétaires — une build excluant le répertoire `proprietary` reste régie par le seul MIT. À trancher avant de déployer pour une équipe.
- MIT et code propriétaire cohabitent dans le même arbre de fichiers : lire `LICENSE` répertoire par répertoire avant tout fork ou toute redistribution.
- L'image standard embarque LibreOffice (via unoserver), Tesseract et OCRmyPDF : d'où son poids, et une consommation CPU et mémoire notable sur l'OCR et la compression. Dimensionner en conséquence.
- Choisir `ultra-lite` par réflexe d'économie retire silencieusement l'OCR et la conversion bureautique.
- Le périmètre de fonctionnalités bouge vite d'une version à l'autre, y compris la répartition entre cœur libre et modules payants : épingler un tag d'image plutôt que `latest`.

## Alternatives

Aucune autre page de la catégorie `tooling/document` dans le brain à ce jour. Les substituts fonctionnels sont soit des services en ligne (exclus par l'hypothèse de non-circulation des documents), soit des bibliothèques appelées depuis du code comme [[Dev/Services/PyMuPDF|PyMuPDF]] — sans interface pour un utilisateur non technique.

## Liens

- [[Dev/Services/OpenDataLoader PDF|OpenDataLoader PDF]] — l'autre face du PDF : extraction structurée pour une machine, catégorie `data/parsing`.
- [[Comparatif - Parsing de documents]] — comparatif de la famille parsing, à ne pas confondre avec cet outil.
- [[OCR]] — concept : reconnaissance optique de caractères.
- Docs : https://docs.stirlingpdf.com/ · Repo : https://github.com/Stirling-Tools/Stirling-PDF
