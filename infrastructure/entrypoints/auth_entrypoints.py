from usecases.auth_usecase import AuthUsecase
from fastapi import APIRouter, Depends
from infrastructure.entrypoints.dependencies import get_auth_usecase

router = APIRouter()

@router.post("/create_user", summary="This is the endpoint where user get api key")
async def create_user(
    email: str,
    usecase: AuthUsecase = Depends(get_auth_usecase)
):
    return await usecase.create_user(email)