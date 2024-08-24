from abc import ABC, abstractmethod

class AuthDataSource(ABC):
    @abstractmethod
    async def create_user(self,  email: str) -> object:
        raise NotImplementedError()