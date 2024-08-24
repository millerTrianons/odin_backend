from infrastructure.data_sources.ai_manager_data_source import AIManagerDatasource
from domain.repositories.ai_manager_repository import AIManagerRepository
from fastapi import UploadFile, File

class AIManagerRepositoryImpl(AIManagerRepository):
    def __init__(self, ai_manager_data_source: AIManagerDatasource) -> None:
        self.ai_manager_data_source = ai_manager_data_source

    async def list_ais(self, user_id: str, offset: int = 0, quantity: int = 10) -> list[object]:
        return await self.ai_manager_data_source.list_ais(user_id, offset, quantity)
    
    async def train_ai(self, api_key: str, file: UploadFile = File(...)):
        return await self.ai_manager_data_source.train_ai(api_key, file)
    
    async def scrap_user_site_route(self, user_site_route_uuid: str) -> object:
        return await self.ai_manager_data_source.scrap_user_site_route(user_site_route_uuid)
    
    async def fine_tunning_by_site(self, user_site_uuid: str) -> object:
        return await self.ai_manager_data_source.fine_tunning_by_site(user_site_uuid)