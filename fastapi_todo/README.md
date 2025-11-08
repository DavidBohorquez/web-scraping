# ============================================
# FastAPI Market Analysis - Boilerplate
# ============================================

![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

Application FastAPI professionnelle pour générer des analyses de marché via l'utilisation d'un LLM

## 🚀 Fonctionnalités

- ✅ **Architecture modulaire** (routers, services, schemas)
- ✅ **Validation des données** avec Pydantic
- ✅ **Gestion centralisée** de la configuration
- ✅ **Gestion d'erreurs** robuste
- ✅ **Documentation API** automatique (Swagger/ReDoc)
- ✅ **Interface web** avec templates HTML
- ✅ **API REST** avec réponses JSON
- ✅ **Dependency injection** FastAPI
- ✅ **Type hints** complets

## 📁 Structure du projet

```
fastapi_todo/
├── main.py                 # Point d'entrée de l'application
├── config.py               # Configuration centralisée
├── requirements.txt        # Dépendances Python
├── .env                    # Variables d'environnement (à créer)
├── .env.example           # Template des variables d'environnement
│
├── routers/               # Routes de l'API
│   ├── __init__.py
│   └── market_analysis.py # Routes pour l'analyse de marché
│
├── schemas/               # Modèles Pydantic
│   ├── __init__.py
│   └── market.py          # Schémas de validation
│
├── services/              # Logique métier
│   ├── __init__.py
│   └── llm_service.py     # Service OpenAI
│
└── templates/             # Templates HTML
    ├── index.html         # Formulaire
    └── result.html        # Résultats
```

## 🔧 Installation

### 1. Cloner le projet (ou utiliser votre projet existant)

```bash
cd fastapi_todo
```

### 2. Créer un environnement virtuel

```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances

```powershell
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

```powershell
# Copier le template
Copy-Item .env.example .env

# Éditer .env et ajouter votre clé API OpenAI
# OPENAI_API_KEY=sk-...
```

## 🎯 Utilisation

### Démarrer l'application

```powershell
# Mode développement (avec auto-reload)
uvicorn main:app --reload

# Mode production
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Accéder à l'application

- **Interface web**: http://localhost:8000
- **Documentation Swagger**: http://localhost:8000/docs
- **Documentation ReDoc**: http://localhost:8000/redoc
- **Health check**: http://localhost:8000/health

## 📡 Endpoints

### Interface Web

- `GET /` - Formulaire d'analyse de marché
- `POST /analyse_market` - Soumettre une analyse (HTML)

### API REST

- `POST /api/analyse` - Analyser un marché (JSON)
  
  **Request Body:**
  ```json
  {
    "produit": "Application mobile de fitness",
    "secteur": "Santé et bien-être"
  }
  ```
  
  **Response:**
  ```json
  {
    "produit": "Application mobile de fitness",
    "secteur": "Santé et bien-être",
    "analyse": "Analyse détaillée du marché..."
  }
  ```

### Monitoring

- `GET /health` - Vérifier l'état de l'application

## 🛠️ Technologies utilisées

- **FastAPI** - Framework web moderne et rapide
- **Pydantic** - Validation et sérialisation des données
- **Jinja2** - Moteur de templates
- **OpenAI API** - Génération d'analyses via GPT
- **Uvicorn** - Serveur ASGI

## 🎨 Personnalisation

### Ajouter un nouveau module

1. Créer un nouveau router dans `routers/`
2. Créer les schemas dans `schemas/`
3. Créer la logique dans `services/`
4. Enregistrer le router dans `main.py`

### Exemple:

```python
# routers/new_feature.py
from fastapi import APIRouter

router = APIRouter(prefix="/feature", tags=["Feature"])

@router.get("/")
async def get_feature():
    return {"message": "Hello from new feature"}

# main.py
from routers.new_feature import router as feature_router
app.include_router(feature_router)
```

## 🔐 Sécurité

- ⚠️ **Ne jamais commiter** le fichier `.env`
- ✅ Ajouter `.env` dans `.gitignore`
- ✅ Utiliser des variables d'environnement pour les secrets
- ✅ En production, configurer CORS correctement

## 📝 TODO / Améliorations possibles

- [ ] Ajouter des tests unitaires (pytest)
- [ ] Implémenter un système de cache (Redis)
- [ ] Ajouter une base de données (SQLAlchemy + PostgreSQL)
- [ ] Implémenter l'authentification (JWT)
- [ ] Ajouter des logs structurés
- [ ] Dockeriser l'application
- [ ] Ajouter CI/CD

## 📄 Licence

MIT License - Libre d'utilisation et de modification

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📚 Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

**Créé lors du cours d'algorithmes au master 1 d'Intelligence artificielle chez Ynov !**
