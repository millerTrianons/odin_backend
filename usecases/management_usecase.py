from domain.repositories.management_repository import ManagementRepository
from infrastructure.dtos.user_style_sheet import UserStyleSheet
from infrastructure.dtos.user_site import UserSite
from infrastructure.dtos.user_site_route import UserSiteRoute
from infrastructure.dtos.user_site_route_scrap import UserSiteRouteScrap
from presentation.create_site_route_data import CreateSiteRouteData
from presentation.create_site_data import CreateSiteData
from presentation.user_style_sheet_data import UserStyleSheetData
from presentation.user_site_scrap_data import UserSiteScrapData, UserSiteScrapDataBody

class ManagementUseCase:
    def __init__(self, managementRepository: ManagementRepository) -> None:
        self.managementRepository = managementRepository

    async def create_site_route(self, content: CreateSiteRouteData) -> object:
        return await self.managementRepository.create_site_route(content)
    
    async def create_user_site(self, content: CreateSiteData) -> object:
        return await self.managementRepository.create_user_site(UserSite.from_entity(content, None))
    
    async def create_user(self, email: str) -> object:
        return await self.managementRepository.create_user(email)
    
    async def list_routes(self, user_site_uuid: str) -> object:
        return await self.managementRepository.list_routes(user_site_uuid)
    
    async def list_sites(self, user_uuid: str) -> list[object]:
        return await self.managementRepository.list_sites(user_uuid)
    
    async def list_chat_by_site(self, user_site_uuid: str) -> object:
        return await self.managementRepository.list_chat_by_site(user_site_uuid)
    
    async def create_api_key(self, user_uuid: str) ->  object:
        return await self.managementRepository.create_api_key(user_uuid)
    
    async def list_api_keys(self, user_uuid: str) -> object:
        return await self.managementRepository.list_api_keys(user_uuid)
    
    async def scrap_user_site_route(self, content: UserSiteScrapDataBody) -> object:
        return await self.managementRepository.scrap_user_site_route(content)
    
    async def list_scrap_by_user_site_route(self, user_site_route_uuid: str) -> object:
        return await self.managementRepository.list_scrap_by_user_site_route(user_site_route_uuid)
    
    async def get_user_site_route_uuid_by_url(self, url: str) -> object:
        return await self.managementRepository.get_user_site_route_uuid_by_url(url)
    
    async def delete_site_route(self, uuid: str) -> None:
        await self.managementRepository.delete_site_route(uuid)

    async def delete_site_route_scrap(self, uuid: str) -> None:
        await self.managementRepository.delete_site_route_scrap(uuid)

    async def create_user_style_sheet(self, user_style_sheet: UserStyleSheetData) -> object:
        return await self.managementRepository.create_user_style_sheet(
            user_style_sheet=UserStyleSheet.from_entity(user_style_sheet, None)
        )
    
    async def list_user_style_sheets(self, user_uuid: str) -> object:
        return await self.managementRepository.list_user_style_sheets(user_uuid)
    
    async def delete_style_sheet(self, uuid: str) -> None:
        await self.managementRepository.delete_style_sheet(uuid)

    
    async def update_site(
        self,
        user_site_uuid: str,
        user_site_data: CreateSiteData
    ):
        return await self.managementRepository.update_site(
                UserSite.from_entity(user_site_data, user_site_uuid)
            )

    async def update_site_route(
        self,
        user_site_route_uuid: str,
        user_site_route_data: CreateSiteRouteData
    ):
        return await self.managementRepository.update_site_route(
                UserSiteRoute.from_entity(user_site_route_data, user_site_route_uuid)
            )
    
    async def update_site_style_sheet(
        self,
        user_site_style_sheet_uuid: str,
        user_site_style_sheet_data: UserStyleSheetData 
    ):
        return await self.managementRepository.update_site_style_sheet(
                UserStyleSheet(user_site_style_sheet_data, user_site_style_sheet_uuid)
            )

    async def update_site_route_scrap(
        self,
        user_site_route_scrap_uuid: str,
        user_site_route_scrap_data: UserSiteScrapData
    ):
        return await self.managementRepository.update_site_route_scrap(
                UserSiteRouteScrap.from_entity(user_site_route_scrap_data, user_site_route_scrap_uuid)
            )

    
    