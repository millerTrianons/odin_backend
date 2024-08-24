from domain.repositories.administrator_repository import AdministratorRepository

class AdministratorUsecase:
    def __init__(self, administrator_repository: AdministratorRepository) -> None:
        self.administrator_repository = administrator_repository

    async def list_users(self) -> list[object]:
        return await self.administrator_repository.list_users()
    
    async def list_api_keys(self) -> list[object]:
        return await self.administrator_repository.list_api_keys()
    
    async def list_messages_relations(self, limit: int) -> list[object]:
        return await self.administrator_repository.list_messages_relations(limit)
