from typing import Optional
from usecases.adminstrator_usecase import AdministratorUsecase
from fastapi import APIRouter, Depends, Request
from infrastructure.entrypoints.dependencies import get_administrator_usecase

router = APIRouter()

@router.get("/list_users", summary="This is the endpoint to teh avaliable users")
async def list_users(
    request: Request,
    usecase: AdministratorUsecase = Depends(get_administrator_usecase)
):
    return await usecase.list_users()

@router.get("/list_api_keys", summary="This is the endpoint wto the api keys")
async def list_api_keys(
    usecase: AdministratorUsecase = Depends(get_administrator_usecase)
):
    return await usecase.list_api_keys()


@router.get("/list_messages_relations", summary="This is the endpoint to message relations")
async def list_messages_relations(
    limit: Optional[int] = 100,
    usecase: AdministratorUsecase = Depends(get_administrator_usecase)       
):
    return await usecase.list_messages_relations(limit)