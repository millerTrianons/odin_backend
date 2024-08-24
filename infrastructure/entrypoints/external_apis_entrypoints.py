from presentation.api_access_data import ApiAccessData, ApiAccessParameterData, ApiAccessHeaderData
from usecases.external_apis_usecase import ExternalApisUsecase
from fastapi import APIRouter, Depends, Body
from infrastructure.entrypoints.dependencies import get_external_apis_usecase

router = APIRouter()

@router.post("/create_api_Access")
async def create_api_access(
    content: ApiAccessData = Body(...),
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.create_external_api_access(content)

@router.post("/create_api_access_parameter")
async def create_api_access_parameter(
    content: ApiAccessParameterData = Body(...),
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.create_external_api_access_parameter(content)

@router.post("/create_api_access_header")
async def create_api_access_parameter(
    content: ApiAccessHeaderData = Body(...),
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.create_external_api_access_header(content)

@router.get("/list_api_access")
async def list_api_access_by_site(
    site_route_uuid: str,
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.list_external_api_access_by_site(site_route_uuid)

@router.get("/list_api_access_parameters")
async def list_api_parameters(
    api_access_uuid: str,
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.list_external_api_parameters(api_access_uuid)

@router.get("/list_api_access_headers")
async def list_api_parameters(
    api_access_uuid: str,
    usecase: ExternalApisUsecase = Depends(get_external_apis_usecase)
):
    return await usecase.list_external_api_headers(api_access_uuid)


