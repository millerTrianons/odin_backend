from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import FileResponse

from infrastructure.entrypoints.dependencies import get_eva_usecase
from presentation.eva_data import EvaDataAskIn, EvaDataSpeakIn, EvaDataAskOut
from usecases.eva_usecase import EvaUseCase

router = APIRouter()

@router.post(
        '/ask', 
        summary='Send a question and receive a text response about this question',
        status_code=status.HTTP_200_OK,
        response_model=EvaDataAskOut
        )

async def ask(
    content: EvaDataAskIn = Body(...),
    usecase: EvaUseCase = Depends(get_eva_usecase)
) -> EvaDataAskOut:
    return await usecase.ask(content)

@router.post(
        '/speak', 
        summary='Receive a speak as a string and return a audio file',
        status_code=status.HTTP_200_OK
    )
async def speak(
    content: EvaDataSpeakIn = Body(...),
    usecase: EvaUseCase = Depends(get_eva_usecase),
) -> FileResponse:
    return await usecase.response(content)

@router.post(
        '/prompt',
        summary='Create a new prompt',
        status_code=status.HTTP_201_CREATED
    )
async def create_prompt(
    prompt: str = Body(...),
    usecase: EvaUseCase = Depends(get_eva_usecase)
) -> None:
    return await usecase.add_prompt(prompt)

@router.delete(
    '/reset_prompt_and_messages',
    summary='Delete a prompt from database',
    status_code=status.HTTP_202_ACCEPTED
)
async def reset_prompt_and_messages(
    usecase: EvaUseCase = Depends(get_eva_usecase)
) -> None:
    return await usecase.reset_prompt_and_messages()




