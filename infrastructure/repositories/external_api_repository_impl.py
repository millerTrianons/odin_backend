from domain.repositories.external_apis_repository import ExternalApisRepository
from infrastructure.data_sources.external_apis_data_source import ExternalApisDataSource
from presentation.api_access_data import ApiAccessData, ApiAccessParameterData, ApiAccessHeaderData


class ExternalApiRepositoryImpl(ExternalApisRepository):
    def __init__(self, external_apis_data_source: ExternalApisDataSource) -> None:
        self.external_apis_data_source = external_apis_data_source


    async def create_external_api_access(self, content: ApiAccessData):
        return await self.external_apis_data_source.create_external_api_access(content)

    async def create_external_api_access_parameter(self, content: ApiAccessParameterData):
        return await self.external_apis_data_source.create_external_api_access_parameter(content)

    async def list_external_api_access_by_site(self, site_route_uuid: str):
        return await self.external_apis_data_source.list_external_api_access_by_site(site_route_uuid)
    
    async def list_external_api_parameters(self, api_access_uuid: str):
        return await self.external_apis_data_source.list_external_api_parameters(api_access_uuid)
    
    async def list_external_api_headers(self, api_access_uuid: str):
        return await self.external_apis_data_source.list_external_api_headers(api_access_uuid)
    
    async def create_external_api_access_header(self, content: ApiAccessHeaderData):
        return await self.external_apis_data_source.create_external_api_access_header(content)