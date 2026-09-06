---
role: brique
nom: Stirling PDF
alias: [stirling-pdf, stirling, s-pdf]
pitch: "Plateforme PDF web auto-hébergeable au cœur MIT : plus de 50 opérations (fusion, découpe, rotation, conversion, OCR, signature, rédaction, compression) exécutées sur son propre serveur, avec API REST et pipelines no-code ; SSO, audit et déploiement air-gapped réservés aux modules propriétaires."
categorie: docs/pdf
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Java
scaling: single-node
alternatives: []
complements: []
tags: [pdf, ocr, self-hosted]
url_docs: https://docs.stirlingpdf.com/
url_repo: https://github.com/Stirling-Tools/Stirling-PDF
---

# Stirling PDF

<!-- AUTO:BANDEAU:START -->
> Plateforme PDF web auto-hébergeable au cœur MIT : plus de 50 opérations (fusion, découpe, rotation, conversion, OCR, signature, rédaction, compression) exécutées sur son propre serveur, avec API REST et pipelines no-code ; SSO, audit et déploiement air-gapped réservés aux modules propriétaires.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java | open-core | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web Java lancée en un `docker run`, qui expose plus de 50 opérations sur des
fichiers PDF : fusion, découpe, extraction et réorganisation de pages, rotation,
conversion depuis et vers les formats bureautiques et images, OCR, signature, rédaction,
compression, mots de passe, métadonnées. Interface en plus de 40 langues, API REST sur la
quasi-totalité des outils, et chaînage de pipelines sans code depuis l'interface.
L'argument central est la **non-circulation des documents** : le traitement a lieu sur
l'instance, le fichier reste sur la machine le temps de l'opération. La frontière à tenir
est celle du destinataire — Stirling PDF produit un document destiné à un **humain**,
fusionné, signé, allégé, lisible ; jamais de la donnée structurée pour une machine, ni
JSON à bounding boxes, ni ordre de lecture exploitable en aval d'un pipeline RAG.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Manipuler des PDF régulièrement sans les envoyer sur un service en ligne : contrainte RGPD, données clients, réseau isolé | Extraire de la donnée structurée d'un PDF pour du RAG ou du ML → [[OpenDataLoader PDF]], [[Docling]], [[Unstructured]] |
| Mutualiser l'outillage PDF d'une équipe derrière une URL interne, plutôt qu'une installation poste par poste | Manipuler des PDF depuis du code, sans serveur intermédiaire → [[PyMuPDF]] |
| Automatiser un traitement documentaire répétitif : l'API REST scripte ce que l'interface fait à la main | Retoucher le contenu rédactionnel d'un document comme dans un traitement de texte : l'outil agit sur la structure du PDF, pas sur la rédaction |
| Donner une interface d'appoint aux non-développeurs, à côté d'un pipeline Python existant | SSO, audit, base de données externe ou déploiement air-gapped supporté attendus d'emblée : ces briques sont dans les modules payants, et l'éditeur annonce le plan gratuit « jusqu'à 5 utilisateurs » |
| | Fork ou redistribution sans revue de licence : cœur MIT et code propriétaire cohabitent dans le même arbre de fichiers, `LICENSE` se lit répertoire par répertoire |

## Mise en œuvre

- Installation — `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf`, puis `http://localhost:8080`. Images Docker officielles, Kubernetes, JAR bare-metal, clients desktop Windows, macOS et Linux. Le périmètre bouge vite d'une version à l'autre, y compris la répartition entre cœur libre et modules payants : épingler un tag d'image plutôt que `latest`
- Point d'entrée — application web en plus de 40 langues, API REST sur la quasi-totalité des outils, pipelines chaînés sans code
- Prérequis — trois variantes d'image, à choisir en connaissance de cause : `latest` (environ 1,5 Go, OCR et conversion bureautique inclus), `latest-ultra-lite` (environ 350 Mo compressés, **sans** Tesseract ni LibreOffice, donc sans OCR ni conversion — l'économie retire la fonction silencieusement), `latest-fat` (plus de 2 Go, polices supplémentaires pour l'usage hors ligne). Deux JAR : celui par défaut sans authentification, et une variante `with-login` activée par `SECURITY_ENABLELOGIN`
- Exécution — auto-hébergé ou managé (Stirling Cloud) ; instance sans état, montée en charge par réplication derrière un répartiteur, chaque traitement restant sur un nœud. L'image standard embarque LibreOffice via unoserver, Tesseract et OCRmyPDF : CPU et mémoire notables sur l'OCR et la compression, à dimensionner
- Coût — cœur MIT gratuit ; plan Server annoncé à 99 $/mois ou 999 $/an pour 100 utilisateurs, Enterprise sur devis ; offre managée et plan Processor à crédits séparés

## Écosystème

### Alternatives

- *Aucune alternative déclarée : seule page de la catégorie `docs/pdf`. Les substituts fonctionnels sont soit des services en ligne — exclus par l'hypothèse de non-circulation des documents —, soit des bibliothèques appelées depuis du code, sans interface pour un utilisateur non technique, pointées dans le tableau ci-dessus.*

## Ressources

- Documentation — https://docs.stirlingpdf.com/
- Dépôt — https://github.com/Stirling-Tools/Stirling-PDF

## Voir aussi

- [[Documents]] — le hub du domaine
- [[OCR]] — la notion : reconnaissance optique de caractères
- [[Comparatif - Parsing de documents]] — l'autre face du PDF : l'extraction pour une machine, à ne pas confondre avec cet outil
