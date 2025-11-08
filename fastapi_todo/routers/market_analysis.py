"""
Routes pour l'analyse de marché.
"""
from fastapi import APIRouter, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import Settings, get_settings
from services import LLMService
from schemas import MarketAnalysisRequest, MarketAnalysisResponse

router = APIRouter(
    tags=["Market Analysis"],
    responses={404: {"description": "Not found"}},
)

# Templates Jinja2
templates = Jinja2Templates(directory="templates")


def get_llm_service(settings: Settings = Depends(get_settings)) -> LLMService:
    """
    Dependency injection pour le service LLM.
    """
    return LLMService(settings)


@router.get("/", response_class=HTMLResponse, summary="Page d'accueil")
async def home(request: Request):
    """
    Affiche le formulaire d'analyse de marché.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@router.post(
    "/analyse_market",
    response_class=HTMLResponse,
    summary="Analyser un marché",
    description="Génère une analyse de marché pour un produit dans un secteur donné"
)
async def analyse_market(
    request: Request,
    produit: str = Form(..., min_length=2, max_length=200),
    secteur: str = Form(..., min_length=2, max_length=200),
    llm_service: LLMService = Depends(get_llm_service)
):
    """
    Endpoint pour analyser un marché via formulaire HTML.
    
    Args:
        request: Requête HTTP
        produit: Nom du produit à analyser
        secteur: Secteur d'activité
        llm_service: Service LLM injecté
        
    Returns:
        Page HTML avec l'analyse
    """
    try:
        # Validation basique
        if not produit.strip() or not secteur.strip():
            raise HTTPException(
                status_code=400,
                detail="Le produit et le secteur ne peuvent pas être vides"
            )
        
        # Appel au service
        texte = llm_service.analyze_market(produit.strip(), secteur.strip())
        
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "contenu": texte,
                "produit": produit,
                "secteur": secteur
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur inattendue: {str(e)}"
        )


@router.post(
    "/api/analyse",
    response_model=MarketAnalysisResponse,
    summary="API - Analyser un marché",
    description="Endpoint API REST pour générer une analyse de marché (retourne du JSON)"
)
async def api_analyse_market(
    data: MarketAnalysisRequest,
    llm_service: LLMService = Depends(get_llm_service)
) -> MarketAnalysisResponse:
    """
    Endpoint API pour analyser un marché (version JSON).
    
    Args:
        data: Données de la requête validées par Pydantic
        llm_service: Service LLM injecté
        
    Returns:
        Analyse de marché au format JSON
    """
    try:
        analyse = llm_service.analyze_market(data.produit, data.secteur)
        
        return MarketAnalysisResponse(
            produit=data.produit,
            secteur=data.secteur,
            analyse=analyse
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur inattendue: {str(e)}"
        )
