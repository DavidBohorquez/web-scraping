# GraphQL API - FastAPI & React

Projet GraphQL complet avec un backend FastAPI utilisant Strawberry GraphQL et un frontend React avec Apollo Client. Ce projet démontre l'implémentation d'une API GraphQL moderne avec gestion des utilisateurs (CRUD complet).

## 📋 Table des matières

- [Description](#description)
- [Technologies utilisées](#technologies-utilisées)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Configuration](#configuration)
- [Démarrage](#démarrage)
- [Utilisation](#utilisation)
- [Endpoints](#endpoints)
- [Résolution de problèmes](#résolution-de-problèmes)

---

## Description

Ce projet est une application full-stack GraphQL qui permet de gérer des utilisateurs via une API GraphQL. Le backend utilise FastAPI avec Strawberry GraphQL pour exposer une API GraphQL type-safe, tandis que le frontend React utilise Apollo Client pour interroger et muter les données.

### Fonctionnalités

- ✅ API GraphQL complète avec queries et mutations
- ✅ Gestion CRUD des utilisateurs (Create, Read, Update, Delete)
- ✅ Base de données SQLite avec SQLAlchemy
- ✅ Frontend React avec TypeScript
- ✅ Apollo Client pour la gestion des requêtes GraphQL
- ✅ CORS configuré pour la communication frontend/backend
- ✅ Script d'initialisation de données

---

## Technologies utilisées

### Backend
- **FastAPI** - Framework web moderne et rapide
- **Strawberry GraphQL** - Framework GraphQL type-safe pour Python
- **SQLAlchemy** - ORM pour la gestion de la base de données
- **SQLite** - Base de données légère
- **Uvicorn** - Serveur ASGI

### Frontend
- **React 18** - Bibliothèque UI
- **TypeScript** - Typage statique
- **Apollo Client** - Client GraphQL
- **Vite** - Build tool moderne
- **GraphQL** - Langage de requête

---

## Structure du projet

```
graphQL/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Point d'entrée FastAPI
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # Configuration SQLAlchemy
│   │   │   └── models.py            # Modèles de données (User)
│   │   ├── graphql/
│   │   │   ├── __init__.py
│   │   │   └── schema.py           # Schéma GraphQL (Query, Mutation)
│   │   └── services/
│   │       ├── __init__.py
│   │       └── user_service.py     # Logique métier
│   ├── requirements.txt
│   └── scripts/
│       └── init_data.py            # Script d'initialisation BDD
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── apollo/
│   │   │   └── client.ts           # Configuration Apollo Client
│   │   └── components/
│   │       └── UserList.tsx        # Composant liste utilisateurs
│   ├── package.json
│   └── public/
└── README.md
```

---

## Installation

### Prérequis

- Python 3.8+ 
- Node.js 16+ et npm/yarn
- Git

### Installation du backend

1. **Naviguer vers le dossier backend :**
   ```bash
   cd backend
   ```

2. **Créer un environnement virtuel (recommandé) :**
   ```bash
   python -m venv venv
   
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances :**

   ⚠️ **Important : Solution pour éviter les problèmes avec Rust et Cargo**
   
   Certaines dépendances Python (comme `cryptography`, `bcrypt`, etc.) nécessitent Rust pour la compilation. Pour éviter les erreurs de compilation liées à Rust/Cargo, utilisez l'option `--only-binary` qui installe uniquement les binaires précompilés :
   
   ```bash
   pip install --only-binary :all: -r requirements.txt
   ```
   
   Si vous rencontrez toujours des problèmes, vous pouvez installer Rust et Cargo (voir section [Résolution de problèmes](#résolution-de-problèmes)).

### Installation du frontend

1. **Naviguer vers le dossier frontend :**
   ```bash
   cd frontend
   ```

2. **Installer les dépendances :**
   ```bash
   npm install
   # ou
   yarn install
   ```

---

## Configuration

### Variables d'environnement

Le projet utilise SQLite par défaut, donc aucune configuration supplémentaire n'est nécessaire pour démarrer. La base de données sera créée automatiquement lors du premier lancement.

Si vous souhaitez utiliser une autre base de données (PostgreSQL, MySQL), vous pouvez créer un fichier `.env` dans le dossier `backend/` :

```env
DATABASE_URL=sqlite:///./sql_app.db
# ou pour PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost/dbname
```

---

## Démarrage

### 1. Initialiser la base de données

Depuis le dossier `backend/` :

```bash
python scripts/init_data.py
```

Ce script va :
- Créer les tables dans la base de données
- Ajouter des données d'exemple (3 utilisateurs)

### 2. Lancer le backend

Depuis le dossier `backend/` :

```bash
uvicorn app.main:app --reload
```

Le serveur sera accessible sur : `http://localhost:8000`

- **API GraphQL** : `http://localhost:8000/graphql`
- **Documentation interactive** : `http://localhost:8000/graphql` (interface GraphQL Playground)
- **Health check** : `http://localhost:8000/health`

### 3. Lancer le frontend

Depuis le dossier `frontend/` :

```bash
npm run dev
# ou
yarn dev
```

Le frontend sera accessible sur : `http://localhost:3000`

---

## Utilisation

### Interface GraphQL

Accédez à `http://localhost:8000/graphql` pour utiliser l'interface GraphQL interactive.

### Exemples de requêtes GraphQL

#### Query - Récupérer tous les utilisateurs

```graphql
query {
  users {
    id
    name
    email
  }
}
```

#### Query - Récupérer un utilisateur par ID

```graphql
query {
  user(id: 1) {
    id
    name
    email
  }
}
```

#### Query - Récupérer les utilisateurs avec filtre et pagination

```graphql
query {
  users(filter: { name: "John" }, skip: 0, limit: 10) {
    id
    name
    email
  }
}
```

#### Mutation - Créer un utilisateur

```graphql
mutation {
  createUser(userInput: {
    name: "Alice Martin"
    email: "alice.martin@example.com"
  }) {
    id
    name
    email
  }
}
```

#### Mutation - Mettre à jour un utilisateur

```graphql
mutation {
  updateUser(id: 1, userInput: {
    name: "John Updated"
    email: "john.updated@example.com"
  }) {
    id
    name
    email
  }
}
```

#### Mutation - Supprimer un utilisateur

```graphql
mutation {
  deleteUser(id: 1)
}
```

---

## Endpoints

### Backend (FastAPI)

- `GET /` - Message de bienvenue
- `GET /health` - Health check
- `POST /graphql` - Endpoint GraphQL principal
- `GET /graphql` - Interface GraphQL Playground (développement)

### Frontend

- `http://localhost:3000` - Application React

---

## Résolution de problèmes

### Problèmes avec Rust et Cargo

Si vous rencontrez des erreurs liées à Rust/Cargo lors de l'installation des dépendances Python, voici deux solutions :

#### Solution 1 : Utiliser les binaires précompilés (Recommandé)

```bash
pip install --only-binary :all: -r requirements.txt
```

Cette commande installe uniquement les packages précompilés et évite la compilation nécessitant Rust.

#### Solution 2 : Installer Rust et Cargo

Si la solution 1 ne fonctionne pas ou si vous avez besoin de compiler certaines dépendances :

1. **Installer Rust :**
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. **Configurer les variables d'environnement :**

   Pour **Linux/macOS** :
   ```bash
   echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   Pour **Windows (PowerShell)** :
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$HOME\.cargo\bin", "User")
   ```

   Pour **Windows (Git Bash)** :
   ```bash
   echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Vérifier l'installation :**
   ```bash
   rustc --version
   cargo --version
   ```

4. **Réinstaller les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

### Autres problèmes courants

#### Erreur CORS

Si vous rencontrez des erreurs CORS entre le frontend et le backend, vérifiez que les URLs dans `backend/app/main.py` correspondent à votre configuration :

```python
allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"]
```

#### Base de données verrouillée

Si vous obtenez une erreur de base de données verrouillée, assurez-vous qu'aucun autre processus n'utilise le fichier `sql_app.db`.

#### Port déjà utilisé

Si le port 8000 ou 3000 est déjà utilisé, vous pouvez :
- Changer le port du backend : `uvicorn app.main:app --reload --port 8001`
- Changer le port du frontend : modifier `vite.config.ts` ou utiliser `npm run dev -- --port 3001`

---

## Développement

### Structure des fichiers principaux

- **`backend/app/main.py`** : Configuration FastAPI, CORS, routes
- **`backend/app/graphql/schema.py`** : Définition du schéma GraphQL (types, queries, mutations)
- **`backend/app/database/models.py`** : Modèles SQLAlchemy
- **`backend/app/services/user_service.py`** : Logique métier pour les utilisateurs
- **`frontend/src/apollo/client.ts`** : Configuration Apollo Client
- **`frontend/src/components/UserList.tsx`** : Composant React pour afficher les utilisateurs

### Ajouter de nouvelles fonctionnalités

1. **Ajouter un nouveau modèle** : Créer dans `backend/app/database/models.py`
2. **Ajouter un service** : Créer dans `backend/app/services/`
3. **Ajouter au schéma GraphQL** : Modifier `backend/app/graphql/schema.py`
4. **Créer un composant frontend** : Ajouter dans `frontend/src/components/`

---

## Auteur

David BOHORQUEZ - Ynov Master 1 Algorithms

---

## Ressources & Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Strawberry GraphQL Documentation](https://strawberry.rocks/)
- [Apollo Client Documentation](https://www.apollographql.com/docs/react/)
- [GraphQL Documentation](https://graphql.org/learn/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)