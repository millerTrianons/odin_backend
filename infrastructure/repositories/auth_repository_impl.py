from domain.repositories.auth_repository import AuthRepository
from infrastructure.data_sources.auth_data_source import AuthDataSource

class AuthRepositoryImpl(AuthRepository):
    def __init__(self, authDataSource: AuthDataSource):
        self.auth_data_source = authDataSource

    async def create_user(self, email: str) -> object:
        return await self.auth_data_source.create_user(email)
