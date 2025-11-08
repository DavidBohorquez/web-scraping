"""
Schémas de validation pour l'analyse de marché.
"""
from pydantic import BaseModel, Field, field_validator


class MarketAnalysisRequest(BaseModel):
    produit: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Nom du produit à analyser",
        examples=["Application mobile de fitness"]
    )
    secteur: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Secteur d'activité",
        examples=["Santé et bien-être"]
    )
    
    @field_validator('produit', 'secteur')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        """Vérifie que les champs ne sont pas vides ou composés uniquement d'espaces."""
        if not v or not v.strip():
            raise ValueError("Le champ ne peut pas être vide")
        return v.strip()
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "produit": "Application mobile de fitness",
                "secteur": "Santé et bien-être"
            }
        }
    }


class MarketAnalysisResponse(BaseModel):
    produit: str = Field(..., description="Produit analysé")
    secteur: str = Field(..., description="Secteur analysé")
    analyse: str = Field(..., description="Contenu de l'analyse de marché")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "produit": "Application mobile de fitness",
                "secteur": "Santé et bien-être",
                "analyse": "Analyse détaillée du marché..."
            }
        }
    }