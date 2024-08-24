from presentation.fine_tunnig_by_site import FineTunnigBySite
from usecases.ai_manager_usecase import AIManagerUsecase
from fastapi import APIRouter, Body, Depends, Query, UploadFile, File
from infrastructure.entrypoints.dependencies import get_ai_manager_usecase

router = APIRouter()

@router.get("/list_ai/", summary="This is the endpoint where user lie avaliable ais")
async def list_ai(
    user_id: str,
    offset: int,
    quantity: int,
    usecase: AIManagerUsecase = Depends(get_ai_manager_usecase)
):
    return await usecase.list_ai(user_id, offset, quantity)

@router.post("/train_ai", summary="This is the endpoint where user can traina ai")
async def tarin_ai(
    api_key: str,
    file: UploadFile = File(...),
     usecase: AIManagerUsecase = Depends(get_ai_manager_usecase)
):
    return await usecase.train_ai(api_key, file)

@router.post("/scrap_user_site_route", summary="This endpoint is used to scrap a route")
async def scrap_user_site_route(
    user_site_route_uuid: str,
    usecase: AIManagerUsecase = Depends(get_ai_manager_usecase)
):
    return await usecase.scrap_user_site_route(user_site_route_uuid)

@router.post("/fine_tunning_by_site")
async def fine_tunning_by_site(
    content: FineTunnigBySite,
    usecase: AIManagerUsecase = Depends(get_ai_manager_usecase)
):
    return await usecase.fine_tunning_by_site(content.user_site_uuid)