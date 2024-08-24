from abc import ABC, abstractmethod

class AdministratorDataSource(ABC):
    @abstractmethod
    async def list_users(self) -> list[object]:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_api_keys(self) -> list[object]:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_messages_relations(self, limit: int) -> list[object]:
        raise NotImplementedError()