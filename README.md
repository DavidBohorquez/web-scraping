# Algorithms - Master 1 Ynov

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

Ce dépôt contient les exercices et projets réalisés dans le cadre du cours **Algorithms** du Master 1 à Ynov. Le dépôt regroupe plusieurs sous-projets (scraping, petites API, exemples LLM, etc.) et fournit des scripts/boilerplates réutilisables.

## Table des matières

- [Objectifs du cours](#objectifs-du-cours)
- [Projets inclus](#projets-inclus)
  - [fastapi_todo — FastAPI Market Analysis (boilerplate)](#fastapi_todo---fastapi-market-analysis-boilerplate)
  - [web_scraping — Books.toscrape.com Scraper](#web_scraping---bookstoscrapecom-scraper)
- [Installation générale](#installation-g%C3%A9n%C3%A9rale)
- [Usage & exemples par projet](#usage--exemples-par-projet)
- [Bonnes pratiques & sécurité](#bonnes-pratiques--s%C3%A9curit%C3%A9)
- [TODO / Améliorations possibles](#todo--am%C3%A9liorations-possibles)
- [Licence](#licence)
- [Contribution & contact](#contribution--contact)
- [Ressources & Documentation](#ressources--documentation)

---

## Objectifs du cours

- Comprendre les concepts fondamentaux des algorithmes et structures de données.
- Maîtriser les techniques de résolution de problèmes algorithmiques.
- Appliquer des algorithmes sur des cas concrets (scraping, analyse).
- Analyser la complexité et produire du code propre et documenté.

---

## Projets inclus

### fastapi_todo — FastAPI Market Analysis (boilerplate)
Un boilerplate FastAPI pour générer des analyses de marché à l'aide d'un LLM (ex. OpenAI). Principales caractéristiques :
- Architecture modulaire (routers, services, schemas).
- Validation Pydantic, templates Jinja2, docs automatiques (Swagger / ReDoc).
- Exemple d'interface web + endpoints JSON pour analyser un produit/secteur.

Structure (extrait)
```
fastapi_todo/
├─ main.py
├─ config.py
├─ requirements.txt
├─ .env.example
├─ routers/
│  └─ market_analysis.py
├─ schemas/
│  └─ market.py
├─ services/
│  └─ llm_service.py
└─ templates/
   ├─ index.html
   └─ result.html
```

Points clés (endpoints)
- `GET /` : Interface web (formulaire)
- `POST /analyse_market` : Soumettre une analyse via HTML
- `POST /api/analyse` : API REST pour analyser un marché (JSON)
- `GET /health` : Health check

Voir le README dans `fastapi_todo/` pour la documentation détaillée du projet (installation, variables d'environnement, exemples d'usage et personnalisation).

---

### web_scraping — Books.toscrape.com Scraper
Script pour extraire les informations des livres sur https://books.toscrape.com :
- titre complet, URL détail, prix, note (1-5), catégories, description, stock, URL image.
- Suivi de la pagination et sauvegarde JSON horodaté.

Usage rapide
```bash
python main.py
```
Après exécution, un fichier `books_YYYYMMDD_HHMMSS.json` est généré.

---

## Installation générale

Ces instructions couvrent l'installation d'un environnement Python commun au dépôt ; certains sous-projets possèdent leur propre `requirements.txt`.

1. Cloner le dépôt
```bash
git clone https://github.com/DavidBohorquez/web-scraping.git
cd web-scraping
```

2. Créer et activer un environnement virtuel (exemple)
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Installer les dépendances globales (si présentes)
```bash
pip install -r requirements.txt
```
Note : certains sous-dossiers (ex. `fastapi_todo`) ont leur propre `requirements.txt`. Installer les dépendances spécifiques avant d'exécuter ces projets.

---

## Usage & exemples par projet

### fastapi_todo
1. Aller dans le dossier :
```bash
cd fastapi_todo
```
2. Copier le fichier d'exemple d'environnement et remplir la clé API OpenAI si nécessaire :
```powershell
cp .env.example .env
# Éditer .env et ajouter OPENAI_API_KEY=sk-...
```
3. Installer dépendances et lancer :
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Accès :
- Interface web : http://localhost:8000
- Swagger : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

Exemple d'API JSON (POST /api/analyse)
Request body:
```json
{
  "produit": "Application mobile de fitness",
  "secteur": "Santé et bien-être"
}
```
Response (exemple):
```json
{
  "produit": "Application mobile de fitness",
  "secteur": "Santé et bien-être",
  "analyse": "Analyse détaillée du marché..."
}
```

### web_scraping
Depuis la racine du repo :
```bash
cd web_scraping
python main.py
```
Le script parcourt les pages, extrait et sauvegarde les données en JSON.

---

## Bonnes pratiques & sécurité

- Ne jamais commiter les fichiers `.env` contenant des clés/secrets.
- Ajouter `.env` à `.gitignore`.
- En production, configurer correctement CORS et limiter les accès à l'API.
- Utiliser des variables d'environnement / gestion secrète pour les clés API (OpenAI, etc.).
- Ajouter des tests unitaires (pytest) et linters (flake8 / black).

---

## TODO / Améliorations possibles

- [ ] Ajouter tests unitaires (pytest)
- [ ] Dockeriser certains services (fastapi_todo)
- [ ] Ajouter une base de données (SQLAlchemy + PostgreSQL)
- [ ] Implémenter un cache (Redis)
- [ ] Mettre en place CI/CD (GitHub Actions)
- [ ] Ajouter authentification (JWT) pour les endpoints sensibles
- [ ] Logs structurés et monitoring

---

## Licence

MIT License — Libre d'utilisation et de modification.

---

## Contribution & contact

Les contributions sont les bienvenues : ouvrez une issue ou une pull request.
Contact : David BOHORQUEZ — Ynov Master 1 Algorithms

---

## Ressources & Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

*Ce dépôt contient du contenu créé dans le cadre du cours d'algorithmes du Master 1 Intelligence Artificielle chez Ynov.*