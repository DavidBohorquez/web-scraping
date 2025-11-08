"""
Application FastAPI - Analyse de Marché
Point d'entrée principal de l'application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from config import get_settings
from routers import market_router


# Configuration
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gère le cycle de vie de l'application.
    Code exécuté au démarrage et à l'arrêt.
    """
    # Startup
    print(f"🚀 Démarrage de {settings.app_name} v{settings.app_version}")
    print(f"📝 Mode debug: {settings.debug}")
    yield
    # Shutdown
    print("👋 Arrêt de l'application")


# Initialisation de l'application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API pour générer des analyses de marché via OpenAI",
    debug=settings.debug,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


# Configuration CORS (à adapter selon vos besoins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez les origines autorisées
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Montage des fichiers statiques (si vous en avez)
# app.mount("/static", StaticFiles(directory="static"), name="static")


# Inclusion des routers
app.include_router(market_router, prefix="", tags=["Market Analysis"])


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint de vérification de l'état de l'application.
    """
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }


if __name__ == "__main__":
    import uvicorn
    
    # Lancement de l'application en mode développement
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )