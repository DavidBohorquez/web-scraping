"""
Service pour interagir avec un LLM.
"""
import requests
from typing import Optional
from fastapi import HTTPException, status
from config import Settings


class LLMService:
    """
    Service pour gérer les appels au LLM.
    """
    
    def __init__(self, settings: Settings):
        """
        Initialise le service avec la configuration.
        
        Args:
            settings: Configuration de l'application
        """
        self.settings = settings
        self.api_url = "https://api.openai.com/v1/chat/completions"
    
    def _get_headers(self) -> dict:
        """
        Retourne les headers pour l'API OpenAI.
        """
        return {
            "Authorization": f"Bearer {self.settings.openai_api_key}",
            "Content-Type": "application/json",
        }
    
    def _build_prompt(self, produit: str, secteur: str) -> str:
        """
        Construit le prompt pour l'analyse de marché.
        
        Args:
            produit: Nom du produit
            secteur: Secteur d'activité
            
        Returns:
            Le prompt formaté
        """
        return f"""Fais une étude de marché synthétique pour le produit '{produit}' dans le secteur '{secteur}'. Inclus les éléments suivants :
        1. Concurrents principaux
        2. Tendances du marché  
        3. Points forts et faibles
        4. Opportunités et menaces"""
    
    def analyze_market(self, produit: str, secteur: str) -> str:
        """
        Effectue une analyse de marché via l'API OpenAI.
        
        Args:
            produit: Nom du produit à analyser
            secteur: Secteur d'activité
            
        Returns:
            L'analyse de marché générée
            
        Raises:
            HTTPException: En cas d'erreur lors de l'appel à l'API
        """
        prompt = self._build_prompt(produit, secteur)
        
        payload = {
            "model": self.settings.openai_model,
            "messages": [{"role": "user",
                          "content": prompt}],
            "max_tokens": self.settings.openai_max_tokens,
            "temperature": self.settings.openai_temperature,
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self._get_headers(),
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            return data["choices"][0]["message"]["content"]
            
        except requests.exceptions.Timeout:
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Le service OpenAI a mis trop de temps à répondre"
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Erreur d'authentification avec OpenAI. Vérifiez votre clé API."
                )
            elif e.response.status_code == 429:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Quota OpenAI dépassé. Réessayez plus tard."
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Erreur lors de l'appel à OpenAI: {str(e)}"
                )
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erreur de connexion à OpenAI: {str(e)}"
            )
        except (KeyError, IndexError) as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Réponse inattendue de l'API OpenAI"
            )
