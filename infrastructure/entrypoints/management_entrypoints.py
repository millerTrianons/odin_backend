from presentation.create_site_route_data import CreateSiteRouteData
from presentation.create_site_data import CreateSiteData
from presentation.user_style_sheet_data import UserStyleSheetData
from usecases.management_usecase import ManagementUseCase
from fastapi import APIRouter, Depends, Body
from infrastructure.entrypoints.dependencies import get_management_usecase
from presentation.user_site_scrap_data import UserSiteScrapData, UserSiteScrapDataBody

router = APIRouter()

@router.post("/create_site", summary="Create a new site")
async def create_site(
    content: CreateSiteData = Body(...), 
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.create_user_site(content)

@router.post("/create_site_route", summary="Create a new route of site")
async def create_chat(
    content: CreateSiteRouteData = Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.create_site_route(content)


@router.post("/create_api_key", summary="Create a new route of site")
async def create_api_key(
    user_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.create_api_key(user_uuid)

@router.post("/create_user_site_style_sheet")
async def create_user_style_sheet(
        user_style_sheet: UserStyleSheetData = Body(...),
        usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.create_user_style_sheet(user_style_sheet)


@router.post("/create_user_site_route_scrap", summary="Scrap a site route")
async def scrap_user_site_route(
    content: UserSiteScrapDataBody=Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.scrap_user_site_route(content)

@router.get("/list_sites/", summary="This is the endpoint where user lie avaliable sites")
async def list_ai(
    user_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.list_sites(user_uuid)


@router.get("/list_site_routes/", summary="This is the endpoint where user lie avaliable sites")
async def list_ai(
    site_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.list_routes(site_uuid)

@router.get("/list_chats_by_site/", summary="This is the endpoint where user lie avaliable sites")
async def create_chat(
    user_site_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.list_chat_by_site(user_site_uuid)

@router.get("/list_user_api_keys", summary="List all api key of the user")
async def list_api_keys(
    user_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)                   
):
    return await usecase.list_api_keys(user_uuid)

@router.get("/list_user_site_route_scraps")
async def list_scrap_by_user_site_route(
    user_site_route_uuid: str, 
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.list_scrap_by_user_site_route(user_site_route_uuid)

@router.get("/get_user_site_route_uuid_by_url")
async def get_user_site_route_uuid_by_url(
    url: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.get_user_site_route_uuid_by_url(url)

@router.get("/list_user_style_sheets")
async def list_user_style_sheets(
    user_uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.list_user_style_sheets(user_uuid)

@router.patch("/update_user_site")
async def update_site(
    user_site_uuid: str,
    user_site_data: CreateSiteData = Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.update_site(
            user_site_uuid, 
            user_site_data
        ) 

@router.patch("/update_user_site_route")
async def update_site_route(
    user_site_route_uuid: str,
    user_site_route_data: CreateSiteRouteData = Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.update_site_route(
            user_site_route_uuid, 
            user_site_route_data
        )

@router.patch("/update_user_site_style_sheet")
async def update_site_style_sheet(
    user_site_style_sheet_uuid: str,
    user_site_style_sheet_data: UserStyleSheetData = Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.update_site_style_sheet(
            user_site_style_sheet_uuid, 
            user_site_style_sheet_data
        )

@router.patch("/update_user_site_route_scrap")
async def update_site_route_scrap(
    user_site_route_scrap_uuid: str,
    user_site_route_scrap_data: UserSiteScrapData = Body(...),
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.update_site_route_scrap(
            user_site_route_scrap_uuid, 
            user_site_route_scrap_data
        )

@router.delete("/delete_site")
async def delete_sitee(
    uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.delete_site_route(uuid)


@router.delete("/delete_site_route")
async def delete_site_route(
    uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.delete_site_route(uuid)


@router.delete("/delete_site_route_scrap")
async def delete_site_route_scrap(
    uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
) -> None:
    return await usecase.delete_site_route_scrap(uuid)

@router.delete("/delete_style_sheet")
async def delete_style_sheet(
    uuid: str,
    usecase: ManagementUseCase = Depends(get_management_usecase)
):
    return await usecase.delete_style_sheet(uuid)

    