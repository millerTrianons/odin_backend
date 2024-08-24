from domain.repositories.administrator_repository import AdministratorRepository
from infrastructure.data_sources.administrator_data_source import AdministratorDataSource


class AdministratorRepositoryImpl(AdministratorRepository):
    def __init__(self, administrator_data_source: AdministratorDataSource) -> None:
        self.administrator_data_source = administrator_data_source

    async def list_users(self) -> list[object]:
        return  await self.administrator_data_source.list_users()
    
    async def list_api_keys(self) -> list[object]:
        return await self.administrator_data_source.list_api_keys()
    
    async def list_messages_relations(self, limit: int) -> list[object]:
        return await self.administrator_data_source.list_messages_relations(limit)
    