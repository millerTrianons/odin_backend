from domain.repositories.external_apis_repository import ExternalApisRepository
from presentation.api_access_data import ApiAccessData, ApiAccessParameterData, ApiAccessHeaderData

class ExternalApisUsecase:
    def __init__(self, external_apis_repository: ExternalApisRepository) -> None:
        self.external_apis_repository = external_apis_repository

    async def create_external_api_access(self, content: ApiAccessData):
        return await self.external_apis_repository.create_external_api_access(content)

    async def create_external_api_access_parameter(self, content: ApiAccessParameterData):
        return await self.external_apis_repository.create_external_api_access_parameter(content)
    
    async def create_external_api_access_header(self, content: ApiAccessHeaderData):
        return await self.external_apis_repository.create_external_api_access_header(content)

    async def list_external_api_access_by_site(self, site_route_uuid: str):
        return await self.external_apis_repository.list_external_api_access_by_site(site_route_uuid)
    
    async def list_external_api_parameters(self, api_access_uuid: str):
        return await self.external_apis_repository.list_external_api_parameters(api_access_uuid)
    
    async def list_external_api_headers(self, api_access_uuid: str):
        return await self.external_apis_repository.list_external_api_headers(api_access_uuid)