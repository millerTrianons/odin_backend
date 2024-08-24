from domain.repositories.ai_manager_repository import AIManagerRepository
from fastapi import UploadFile, File

class AIManagerUsecase:
    def __init__(self, ai_manager_repository: AIManagerRepository) -> None:
        self.ai_manager_repository = ai_manager_repository

    async def list_ai(self, user_id: str, offset: int = 0, quantity: int = 10) -> list[object]:
        return await self.ai_manager_repository.list_ais(user_id, offset, quantity)
    

    async def train_ai(self, api_key: str,  file: UploadFile = File(...)) -> object:
        return await self.ai_manager_repository.train_ai(api_key, file)
    
    async def scrap_user_site_route(self, user_site_route_uuid: str) -> object:
        return await self.ai_manager_repository.scrap_user_site_route(user_site_route_uuid)
    
    async def fine_tunning_by_site(self, user_site_uuid: str) -> object:
        return await self.ai_manager_repository.fine_tunning_by_site(user_site_uuid)