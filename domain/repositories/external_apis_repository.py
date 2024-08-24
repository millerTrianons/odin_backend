from abc import ABC, abstractmethod

from presentation.api_access_data import ApiAccessData, ApiAccessParameterData, ApiAccessHeaderData

class ExternalApisRepository(ABC):
    @abstractmethod
    async def create_external_api_access(self, content: ApiAccessData):
        raise NotImplementedError()
    
    @abstractmethod
    async def create_external_api_access_parameter(self, content: ApiAccessParameterData):
        raise NotImplementedError()
    
    @abstractmethod
    async def create_external_api_access_header(self, content: ApiAccessHeaderData):
        raise NotImplementedError()

    @abstractmethod
    async def list_external_api_access_by_site(self, site_route_uuid: str):
        raise NotImplementedError()
    
    @abstractmethod
    async def list_external_api_parameters(self, api_access_uuid: str):
        raise NotImplementedError()
    
    @abstractmethod
    async def list_external_api_headers(self, api_access_uuid: str):
        raise NotImplementedError()