from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from infrastructure.entrypoints.dependencies import get_eva_usecase
from presentation.eva_data import EvaDataAskIn, EvaDataSpeakIn, EvaDataAskOut
from usecases.eva_usecase import EvaUseCase

router = APIRouter()

@router.post(
        '/ask', 
        summary='Send a question and receive a text response about this question',
        response_model=EvaDataAskOut
        )

async def ask(
    content: EvaDataAskIn,
    usecase: EvaUseCase = Depends(get_eva_usecase)
) -> EvaDataAskOut:
    return await usecase.ask(content)

@router.post(
        '/speak', 
        summary='Receive a speak as a string and return a audio file',
        )
async def speak(
    content: EvaDataSpeakIn,
    usecase: EvaUseCase = Depends(get_eva_usecase)
) -> FileResponse:
    return await usecase.response(content)

