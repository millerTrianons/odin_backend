from infrastructure.data_sources.external_apis_data_source import ExternalApisDataSource
from data.services.sql_connection_service import SqlConnectionService
from infrastructure.dtos.api_access import ApiAccess
from infrastructure.dtos.api_access_parameter import ApiAccessParameter
from presentation.api_access_data import ApiAccessData, ApiAccessParameterData, ApiAccessHeaderData


class ExternalApisDataSourceImpl(ExternalApisDataSource):
    connection: SqlConnectionService
    
    def __init__(self) -> None:
        self.connection = SqlConnectionService()

    async def create_external_api_access(self, content: ApiAccessData):
        api_access = ApiAccess.from_entity(content)

        await self.connection.insert(api_access)

        return {'api_access_uuid': api_access.uuid}
    
    async def create_external_api_access_parameter(self, content: ApiAccessParameterData):
        api_access_parameter = ApiAccessParameter.fromEntity(content)

        await self.connection.insert(api_access_parameter)

        return {'api_access_aparameter_uuid': api_access_parameter.uuid}
    

    async def create_external_api_access_header(self, content: ApiAccessHeaderData):
        api_access_header = ApiAccessParameter.fromEntity(content)

        await self.connection.insert(api_access_header)

        return {'api_access_header_uuid': api_access_header.uuid}

    async def list_external_api_access_by_site(self, site_route_uuid: str):
        statement = f"SELECT * FROM api_access WHERE user_site_route_uuid='{site_route_uuid}'"
        
        res = await self.connection.get(statement)

        print(res)

        return {'data': site_route_uuid}
    
    async def list_external_api_parameters(self, api_access_uuid: str):
        statement = f"SELECT * FROM api_access_parameter WHERE api_access_uuid='{api_access_uuid}'"
        
        res = await self.connection.get(statement)

        print(res)

        return {'data': api_access_uuid}
    
    async def list_external_api_headers(self, api_access_uuid: str):
        statement = f"SELECT * FROM api_access_header WHERE api_access_uuid='{api_access_uuid}'"
        
        res = await self.connection.get(statement)

        print(res)

        return {'data': api_access_uuid}