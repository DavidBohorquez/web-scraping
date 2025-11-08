"""
Configuration centralisée de l'application. Charge et valide les variables d'environnement.
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Configuration de l'application avec validation automatique.
    Les valeurs sont chargées depuis les variables d'environnement (fichier .env)
    """
    # Configuration de l'application
    app_name: str = "FastAPI Market Analysis"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Configuration OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4o"
    openai_max_tokens: int = 500
    openai_temperature: float = 0.4
    
    # Configuration des templates
    templates_dir: str = "templates"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Utilise le cache pour éviter de recharger la config à chaque appel.
    """
    return Settings()
