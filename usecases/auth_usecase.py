from domain.repositories.auth_repository import AuthRepository
from infrastructure.validators import email_is_valid
from fastapi import  HTTPException

class AuthUsecase:
    def __init__(self, authRepository: AuthRepository) -> None:
        self.repository = authRepository

    async def create_user(self, email: str,) -> object:
        is_valid = email_is_valid(email)

        if(is_valid):
            return await self.repository.create_user(email)
        else:
            raise HTTPException(status_code=400, detail="Invalid email")