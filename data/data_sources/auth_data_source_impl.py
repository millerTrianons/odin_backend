from infrastructure.data_sources.auth_data_source import AuthDataSource
from infrastructure.dtos.user import User
from data.services.sql_connection_service import SqlConnectionService
from datetime import datetime
import uuid

class AuthDataSourceImpl(AuthDataSource):
    def __init__(self) -> None:
        self.connection = SqlConnectionService()

    async def create_user(self, email: str) -> object:
        user: User = User(
            uuid= uuid.uuid4(),
            user_email=email,
        )

        await self.connection.insert([user])
        
        return {
            'uuid': user.uuid,
        }